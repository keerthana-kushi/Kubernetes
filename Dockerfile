# Use an official lightweight Java image
FROM eclipse-temurin:17-jdk-alpine

# Add a volume pointing to /tmp
VOLUME /tmp

# Argument for the JAR file
ARG JAR_FILE=target/*.jar

# Copy the JAR file into the image
COPY ${JAR_FILE} app.jar

# Run the JAR file
ENTRYPOINT ["java","-jar","/app.jar"]
