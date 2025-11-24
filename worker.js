export default {
    async fetch(request, env) {
        // Handle CORS preflight
        if (request.method === 'OPTIONS') {
            return new Response(null, {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type',
                },
            });
        }

        const url = new URL(request.url);

        // API endpoint for form submissions
        if (url.pathname === '/api/leads' && request.method === 'POST') {
            return handleLeadSubmission(request, env);
        }

        // List all leads (admin endpoint)
        if (url.pathname === '/api/leads/list' && request.method === 'GET') {
            return listLeads(env);
        }

        return new Response('Not Found', { status: 404 });
    },
};

async function handleLeadSubmission(request, env) {
    try {
        // Parse form data
        const formData = await request.formData();
        const email = formData.get('email');
        const niche = formData.get('niche');
        const niche_name = formData.get('niche_name') || 'Unknown';

        // Validate email
        if (!email || !email.includes('@')) {
            return new Response('Invalid email', { status: 400 });
        }

        // Insert into D1 database
        const result = await env.DB.prepare(
            'INSERT INTO leads (email, niche, niche_name) VALUES (?, ?, ?)'
        )
            .bind(email, niche, niche_name)
            .run();

        // Send Telegram notification
        await sendTelegramNotification(env, {
            email,
            niche,
            niche_name,
            id: result.meta.last_row_id,
        });

        // Redirect to thank-you page
        return Response.redirect('https://blatik.github.io/rustdev-network/thank-you.html', 302);
    } catch (error) {
        console.error('Error handling lead:', error);
        return new Response('Internal Server Error: ' + error.message, { status: 500 });
    }
}

async function sendTelegramNotification(env, lead) {
    const message = `
🎯 *New Lead Received!*

📧 Email: \`${lead.email}\`
🏷️ Niche: ${lead.niche_name}
🆔 ID: ${lead.id}
📅 Time: ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}
  `;

    const telegramUrl = `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`;

    try {
        const response = await fetch(telegramUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id: env.TELEGRAM_CHAT_ID,
                text: message,
                parse_mode: 'Markdown',
            }),
        });

        if (!response.ok) {
            console.error('Telegram API error:', await response.text());
        }
    } catch (error) {
        console.error('Failed to send Telegram notification:', error);
    }
}

async function listLeads(env) {
    try {
        const { results } = await env.DB.prepare(
            'SELECT * FROM leads ORDER BY created_at DESC LIMIT 100'
        ).all();

        return new Response(JSON.stringify(results, null, 2), {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        });
    } catch (error) {
        return new Response('Error fetching leads: ' + error.message, { status: 500 });
    }
}
