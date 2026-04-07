package com.jupiter.biometrics.fingerprint;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.machinezoo.sourceafis.FingerprintImage;
import com.machinezoo.sourceafis.FingerprintImageOptions;
import com.machinezoo.sourceafis.FingerprintMatcher;
import com.machinezoo.sourceafis.FingerprintTemplate;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.Executors;

public class App {
    private static final ObjectMapper MAPPER = new ObjectMapper()
        .setSerializationInclusion(JsonInclude.Include.NON_NULL);

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8081), 0);
        server.createContext("/health", new HealthHandler());
        server.createContext("/match", new MatchHandler());
        server.setExecutor(Executors.newFixedThreadPool(8));
        server.start();
        System.out.println("matcher-fingerprint listening on 0.0.0.0:8081");
    }

    static final class HealthHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!Objects.equals(exchange.getRequestMethod(), "GET")) {
                writeJson(exchange, 405, Map.of("error", "method not allowed"));
                return;
            }
            writeJson(exchange, 200, Map.of("status", "ok", "service", "fingerprint"));
        }
    }

    static final class MatchHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!Objects.equals(exchange.getRequestMethod(), "POST")) {
                writeJson(exchange, 405, Map.of("error", "method not allowed"));
                return;
            }
            try (InputStream body = exchange.getRequestBody()) {
                MatchRequest request = MAPPER.readValue(body, MatchRequest.class);
                double galleryDpi = request.gallery_dpi != null ? request.gallery_dpi : 500.0;
                double probeDpi = request.probe_dpi != null ? request.probe_dpi : 500.0;

                FingerprintTemplate galleryTemplate = createTemplate(request.gallery_image_b64, galleryDpi);
                FingerprintTemplate probeTemplate = createTemplate(request.probe_image_b64, probeDpi);

                double score = new FingerprintMatcher(probeTemplate).match(galleryTemplate);
                Boolean matched = request.threshold != null ? score >= request.threshold : null;

                writeJson(exchange, 200, new MatchResponse(score, matched));
            } catch (IllegalArgumentException e) {
                writeJson(exchange, 400, Map.of("error", e.getMessage()));
            } catch (Exception e) {
                writeJson(exchange, 422, Map.of("error", e.getMessage()));
            }
        }

        private FingerprintTemplate createTemplate(String imageB64, double dpi) {
            byte[] image = Base64.getDecoder().decode(imageB64);
            FingerprintImageOptions options = new FingerprintImageOptions().dpi(dpi);
            FingerprintImage fingerprintImage = new FingerprintImage(image, options);
            return new FingerprintTemplate(fingerprintImage);
        }
    }

    static void writeJson(HttpExchange exchange, int status, Object payload) throws IOException {
        byte[] json = MAPPER.writeValueAsString(payload).getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.sendResponseHeaders(status, json.length);
        try (OutputStream output = exchange.getResponseBody()) {
            output.write(json);
        }
    }

    public static final class MatchRequest {
        public String gallery_image_b64;
        public String probe_image_b64;
        public Double gallery_dpi;
        public Double probe_dpi;
        public Double threshold;
    }

    public record MatchResponse(double score, Boolean matched) {
    }
}
