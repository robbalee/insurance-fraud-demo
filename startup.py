# Azure Web Apps startup file
import os
from app import app

if __name__ == "__main__":
    # Use Azure's PORT environment variable
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
