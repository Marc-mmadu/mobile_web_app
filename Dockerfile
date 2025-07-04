# Step 1: Build stage
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the app source code
COPY . .

# Build the production-ready app
RUN yarn build

# Step 2: Production stage using Nginx
FROM nginx:stable-alpine

# Copy the built app from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx config (optional but recommended for SPAs)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]