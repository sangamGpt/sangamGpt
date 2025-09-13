<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Premium E-commerce</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

  <style>
    body {
      margin: 0;
      font-family: 'Roboto', sans-serif;
      background: #111;
      color: white;
    }
    body::before {
      content: '';
      position: fixed;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet, red);
      background-size: 400% 400%;
      animation: rgb 15s ease infinite;
      z-index: -1;
      filter: blur(100px);
    }
    @keyframes rgb {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* Login Box */
    #login-container {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(0,0,0,0.85);
      padding: 40px;
      border-radius: 20px;
      text-align: center;
      width: 350px;
    }
    #login-container h1 {
      margin-bottom: 30px;
      animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
      from { text-shadow: 0 0 5px #fff, 0 0 10px #ff00ff; }
      to   { text-shadow: 0 0 20px #00ffff, 0 0 30px #ff00ff; }
    }
    #login-container input {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      border-radius: 10px;
      border: none;
      outline: none;
      background: rgba(255,255,255,0.1);
      color: #fff;
    }
    #login-container button {
      width: 100%;
      padding: 14px;
      margin-top: 15px;
      border: none;
      border-radius: 10px;
      font-size: 16px;
      cursor: pointer;
      color: #fff;
      background: linear-gradient(45deg,#ff0055,#00ffff,#ffdd00);
      background-size: 200% 200%;
      animation: btnAnim 3s linear infinite;
      transition: transform 0.3s;
    }
    #login-container button:hover {
      transform: scale(1.05);
    }
    @keyframes btnAnim {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* Header */
    header {
      padding: 15px 40px;
      background: linear-gradient(90deg,#ff4b2b,#ff416c);
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 1.8rem;
      margin: 0;
    }
    nav a {
      color: white;
      text-decoration: none;
      margin-left: 25px;
      font-weight: 500;
      transition: 0.3s;
    }
    nav a:hover { color: #00f0ff; }

    /* Products Grid */
    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 25px;
      padding: 40px;
    }
    .product-card {
      background: #1a1a1a;
      border-radius: 15px;
      overflow: hidden;
      text-align: center;
      box-shadow: 0 0 20px rgba(0,255,255,0.2);
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .product-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 0 40px rgba(0,255,255,0.6);
    }
    .product-card img { width: 100%; border-bottom: 1px solid #333; }
    .product-card h2 { margin: 15px 0 5px; font-family: 'Playfair Display', serif; }
    .product-card p { margin: 0 0 15px; color: #ccc; }

    /* Buttons */
    .buy-btn, .admin-btn {
      display: inline-block;
      margin: 10px 5px 15px;
      padding: 10px 18px;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      font-weight: bold;
      transition: 0.3s;
    }
    .buy-btn {
      background: linear-gradient(45deg,#ff416c,#ff4b2b);
      color: white;
    }
    .buy-btn:hover { box-shadow: 0 0 20px #ff4b2b; }
    .admin-btn {
      background: #00ffff;
      color: #111;
    }
    .admin-btn:hover { box-shadow: 0 0 20px #00ffff; }

    /* Admin Panel */
    #adminPanel {
      margin: 20px;
      padding: 20px;
      background: rgba(255,255,255,0.05);
      border-radius: 15px;
    }
    #adminPanel input {
      width: 30%;
      padding: 8px;
      margin: 8px;
      border: none;
      border-radius: 8px;
      outline: none;
    }

    @media(max-width:600px){
      #login-container { width: 90%; padding: 25px; }
      #adminPanel input { width: 90%; display: block; margin: 10px auto; }
    }
  </style>
</head>
<body>

  <!-- Login -->
  <div id="login-container">
    <h1>Login</h1>
    <input type="text" placeholder="Name" id="username">
    <input type="email" placeholder="Gmail" id="useremail">
    <input type="password" placeholder="Password" id="userpass">
    <button onclick="login()">Login</button>
  </div>

  <!-- Products Section -->
  <section id="products-section" style="display:none;">
    <header>
      <h1>Premium Shop</h1>
      <nav>
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">Contact</a>
        <a href="#">Account</a>
      </nav>
    </header>

    <div class="products" id="productsList"></div>

    <!-- Admin Panel -->
    <div id="adminPanel" style="display:none;">
      <h2>Admin Panel</h2>
      <input type="text" id="prodName" placeholder="Product Name">
      <input type="number" id="prodPrice" placeholder="Product Price">
      <input type="text" id="prodImg" placeholder="Image URL">
      <button class="admin-btn" onclick="addProduct()">Add Product</button>
    </div>
  </section>

  <script>
    // Products
    let products = [
      {name:"Product 1", price:1500, img:"https://via.placeholder.com/300x200.png?text=Product+1"},
      {name:"Product 2", price:2500, img:"https://via.placeholder.com/300x200.png?text=Product+2"},
    ];

    // Admin credentials
    const adminCred = {
      username:"zero",
      email:"ffzero8434@gmail.com",
      password:"ffsangam813205"
    };

    let isAdmin = false;

    // Login
    function login(){
      const name = document.getElementById("username").value.trim();
      const email = document.getElementById("useremail").value.trim();
      const pass = document.getElementById("userpass").value.trim();

      if(!name || !email || !pass){
        alert("सभी फ़ील्ड भरें");
        return;
      }

      if(name === adminCred.username && email === adminCred.email && pass === adminCred.password){
        isAdmin = true;
        document.getElementById("adminPanel").style.display = "block"; // Admin gets panel
      } else {
        isAdmin = false;
        document.getElementById("adminPanel").style.display = "none"; // User only view
      }

      document.getElementById("login-container").style.display = "none";
      document.getElementById("products-section").style.display = "block";

      renderProducts();
    }

    // Render products
    function renderProducts(){
      const container = document.getElementById("productsList");
      container.innerHTML = "";
      products.forEach((prod,index)=>{
        const div = document.createElement("div");
        div.className = "product-card";
        let adminBtn = isAdmin 
            ? `<button class="admin-btn" onclick="deleteProduct(${index})">Delete</button>` 
            : '';
        div.innerHTML = `
          <img src="${prod.img}" alt="${prod.name}">
          <h2>${prod.name}</h2>
          <p>₹${prod.price}</p>
          <button class="buy-btn">Buy</button>
          ${adminBtn}
        `;
        container.appendChild(div);
      });
    }

    // Add product (admin only)
    function addProduct(){
      if(!isAdmin) return;
      const name = document.getElementById("prodName").value.trim();
      const price = document.getElementById("prodPrice").value.trim();
      const img = document.getElementById("prodImg").value.trim();

      if(name && price && img){
        products.push({name, price, img});
        renderProducts();

        document.getElementById("prodName").value = "";
        document.getElementById("prodPrice").value = "";
        document.getElementById("prodImg").value = "";
      } else {
        alert("Fill all fields");
      }
    }

    // Delete product (admin only)
    function deleteProduct(index){
      if(!isAdmin) return;
      products.splice(index,1);
      renderProducts();
    }
  </script>
</body>
</html>
