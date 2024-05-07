const CACHE_NAME = 'weather-data-cache-v2'; // Increment version to signal an update
const urlsToCache = [
    '/static/js/main.js',
    '/static/css/main.css',
    '/todo/',  // Add pages or additional static files if needed
];

// Installation event - cache resources
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
            .catch(error => console.error('Error opening cache: ', error))
    );
});

// Activation event - clear old caches
self.addEventListener('activate', event => {
    const cacheWhitelist = ['weather-data-cache-v2']; // Update this to your new cache name
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});


// Fetch event - serve cached resources, and cache new ones
self.addEventListener('fetch', event => {
    // Skip non-GET requests and Chrome extension URLs
    if (event.request.method !== 'GET' || event.request.url.startsWith('chrome-extension')) return;

    event.respondWith(
        caches.match(event.request)
            .then(cachedResponse => {
                if (cachedResponse) {
                    return cachedResponse;
                }

                return fetch(event.request).then(response => {
                    // Check if we received a valid response
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    const responseToCache = response.clone();
                    caches.open(CACHE_NAME)
                        .then(cache => {
                            cache.put(event.request, responseToCache);
                        });

                    return response;
                });
            })
    );
});
