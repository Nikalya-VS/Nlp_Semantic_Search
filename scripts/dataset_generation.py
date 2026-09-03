import random
import pandas as pd
from faker import Faker

fake = Faker()

TOTAL_RECORDS = 50000

knowledge_base = {
    "Authentication": {
        "Password Reset": {
            "queries": [
                "I forgot my password",
                "Reset my password",
                "Can't login",
                "Forgot login credentials",
                "Password reset process",
                "Need password help",
                "Unable to sign in",
                "Forgot account password"
            ],
            "titles": [
                "Password Reset Guide",
                "Recover Your Password",
                "Forgot Password Instructions"
            ],
            "contents": [
                "If you forgot your password, click the Forgot Password option on the login page. Enter your registered email address and follow the instructions to create a new password.",
                "Password recovery is available through your registered email. Complete the verification process before choosing a strong new password.",
                "Use the password reset feature to regain access to your account. Reset links expire after a limited time."
            ],
            "keywords": [
                "password","reset","login","forgot",
                "account","security","credentials","authentication"
            ]
        },

        "Account Locked": {
            "queries":[
                "My account is locked",
                "Unlock my account",
                "Unable to login",
                "Too many failed login attempts",
                "Login blocked"
            ],
            "titles":[
                "Account Unlock Guide",
                "Recover Locked Account",
                "Account Lock Resolution"
            ],
            "contents":[
                "Accounts may be locked after multiple failed login attempts. Wait for the lock period or contact support.",
                "Verify your identity to unlock your account securely.",
                "Your account was temporarily locked to protect against unauthorized access."
            ],
            "keywords":[
                "locked","login","security","unlock",
                "authentication","access","support","account"
            ]
        }
    },

    "Payments": {
        "Payment Failed": {
            "queries":[
                "Payment failed",
                "Transaction declined",
                "Unable to pay",
                "Card payment failed",
                "Checkout payment error"
            ],
            "titles":[
                "Payment Failure Guide",
                "Resolve Payment Errors",
                "Payment Troubleshooting"
            ],
            "contents":[
                "Payment failures can occur due to insufficient balance, incorrect card information or temporary banking issues.",
                "Verify your payment information and retry the transaction.",
                "If the problem continues, contact your bank or use another payment method."
            ],
            "keywords":[
                "payment","transaction","card","bank",
                "billing","checkout","failed","declined"
            ]
        }
    },

    "Orders": {
        "Track Order": {
            "queries":[
                "Where is my order?",
                "Track my package",
                "Order status",
                "Shipment tracking",
                "When will my order arrive?"
            ],
            "titles":[
                "Track Your Order",
                "Order Tracking Guide",
                "Shipment Status"
            ],
            "contents":[
                "Use your order number in the tracking page to monitor your shipment in real time.",
                "Tracking information is updated whenever the courier scans your package.",
                "Delivery estimates depend on your shipping method."
            ],
            "keywords":[
                "order","tracking","shipment","delivery",
                "courier","package","status","order id"
            ]
        }
    },

    "Refunds": {
        "Refund Status": {
            "queries":[
                "Where is my refund?",
                "Refund not received",
                "Refund status",
                "Money not credited",
                "Refund taking too long"
            ],
            "titles":[
                "Refund Processing",
                "Refund Status Guide",
                "Refund Timeline"
            ],
            "contents":[
                "Refunds are usually processed within 5 to 10 business days depending on your payment provider.",
                "You can monitor refund progress from your orders page.",
                "Contact support if your refund exceeds the expected processing time."
            ],
            "keywords":[
                "refund","payment","money","bank",
                "credit","transaction","return","status"
            ]
        }
    }
}

rows = []

doc_id = 1

while len(rows) < TOTAL_RECORDS:

    category = random.choice(list(knowledge_base.keys()))

    issue = random.choice(list(knowledge_base[category].keys()))

    data = knowledge_base[category][issue]

    query = random.choice(data["queries"])

    title = random.choice(data["titles"])

    content = random.choice(data["contents"])

    keywords = ", ".join(random.sample(data["keywords"], k=min(5, len(data["keywords"]))))

    content += f" Reference ID: {fake.uuid4()}."
    content += f" Ticket Number: {fake.random_number(digits=6)}."
    content += f" Contact Email: {fake.email()}."

    rows.append({
        "Document ID": doc_id,
        "Category": category,
        "User Query": query,
        "Title": title,
        "Content": content,
        "Keywords": keywords
    })

    doc_id += 1

df = pd.DataFrame(rows)

df.to_csv("semantic_search_dataset.csv", index=False)

print(df.head())

print(f"\nGenerated {len(df)} records successfully!")