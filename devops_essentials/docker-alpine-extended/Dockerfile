FROM alpine:latest

RUN apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

COPY config.txt /app/config.txt

CMD ["sh"]
