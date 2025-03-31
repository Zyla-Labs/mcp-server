# 🔌  Zyla API Hub MCP Server

This MCP server allows any large language model (LLM) using the [Model Context Protocol (MCP)](https://github.com/microsoft/mcp) to access **any public API** from the [Zyla API Hub](https://zylalabs.com) by providing:

- ✅ HTTP method (GET, POST, PUT, DELETE, etc.)
- ✅ Full API endpoint (URL)
- ✅ Headers (like `Authorization`)
- ✅ Query parameters or JSON body

---

## ✨ Features

- 🌐 Generic API caller — supports any Zyla API Hub endpoint
- 🔐 Secure — API keys passed via headers
- 🚀 Dockerized — easy to deploy

---

## 🧪 Example Use

Input to the MCP tool:

```json
{
  "method": "GET",
  "url": "https://www.zylalabs.com/api/824/crime+data+by+zipcode+api/583/get+crime+rates+by+zip",
  "headers": {
    "Authorization": "Bearer YOUR_ZYLA_API_KEY"
  }
}
