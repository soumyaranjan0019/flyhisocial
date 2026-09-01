import os, re

files = ["cloud-computing.html", "erp-consulting.html", "app-web-development.html", "digital-marketing.html", "event-management.html", "marine-consultancy.html", "ai.html"]

footer_template = """  <!-- Premium Rebuilt Footer -->
  <footer class="relative z-10 bg-[#050505] pt-32 pb-12 overflow-hidden border-t border-white/5">
      <div class="relative z-10 max-w-7xl mx-auto px-6 md:px-12 grid grid-cols-1 md:grid-cols-12 gap-12 lg:gap-16 mb-24">
        
        <!-- Column 1: Brand & Desc -->
        <div class="md:col-span-4">
          <a href="index.html" class="flex items-center gap-3 mb-8 select-none hover-target group inline-flex">
            <svg class="h-12 w-auto group-hover:scale-105 transition-transform duration-300" viewBox="0 0 250 84" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="56" y="0" width="24" height="24" fill="#E52D12"/>
              <rect x="28" y="28" width="24" height="24" fill="#FFFFFF"/>
              <rect x="56" y="28" width="24" height="24" fill="#FFFFFF"/>
              <rect x="0" y="56" width="24" height="24" fill="#FFFFFF"/>
              <rect x="28" y="56" width="24" height="24" fill="#FFFFFF"/>
              <text x="100" y="34" fill="#FFFFFF" font-family="Space Grotesk, sans-serif" font-weight="700" font-size="40" letter-spacing="-0.01em">FLYHi</text>
              <text x="100" y="74" fill="#FFFFFF" font-family="Space Grotesk, sans-serif" font-weight="600" font-size="25" letter-spacing="0.08em">SOCIAL</text>
            </svg>
          </a>
          <p class="text-base text-zinc-400 leading-relaxed font-light pr-4 max-w-sm">
            System implementation specialists accelerating enterprise business solutions.
          </p>
        </div>
        
        <!-- Column 2: Services -->
        <div class="md:col-span-3">
          <h2 class="text-white font-display font-bold mb-8 text-sm uppercase tracking-widest">Services</h2>
          <ul class="space-y-4 text-sm font-light text-zinc-400">
            <li><a href="cloud-computing.html" class="hover-target hover:text-white transition-colors block">Cloud Computing & AI</a></li>
            <li><a href="erp-consulting.html" class="hover-target hover:text-white transition-colors block">ERP Solutions</a></li>
            <li><a href="app-web-development.html" class="hover-target hover:text-white transition-colors block">App & Web-development</a></li>
            <li><a href="digital-marketing.html" class="hover-target hover:text-white transition-colors block">Digital-Marketing</a></li>
            <li><a href="event-management.html" class="hover-target hover:text-white transition-colors block">Event Management</a></li>
            <li><a href="marine-consultancy.html" class="hover-target hover:text-white transition-colors block">Marine Consultancy</a></li>
          </ul>
        </div>
        
        <!-- Column 3: Company -->
        <div class="md:col-span-2">
          <h2 class="text-white font-display font-bold mb-8 text-sm uppercase tracking-widest">Company</h2>
          <ul class="space-y-4 text-sm font-light text-zinc-400">
            <li><a href="index.html" class="hover-target hover:text-white transition-colors block">Corporate Home</a></li>
            <li><a href="index.html#about" class="hover-target hover:text-white transition-colors block">About Us</a></li>
            <li><a href="index.html#contact" class="hover-target hover:text-white transition-colors block">Contact Us</a></li>
          </ul>
        </div>
        
        <!-- Column 4: Contact Desk -->
        <div class="md:col-span-3">
          <h2 class="text-white font-display font-bold mb-8 text-sm uppercase tracking-widest">Contact Desk</h2>
          <p class="text-sm text-zinc-400 leading-relaxed font-light mb-6">
            {contact_desc}
          </p>
          <span class="text-xs text-zinc-500 block uppercase font-bold mb-2 tracking-widest">Direct Routing Number</span>
          <a href="tel:+919090031316" class="text-lg font-mono text-accent font-bold hover:text-white transition-colors block hover-target">+91 9090031316</a>
        </div>
      </div>
      
      <!-- Copyright / Bottom Bar -->
      <div class="relative z-10 max-w-7xl mx-auto px-6 md:px-12 pt-8 border-t border-white/10 flex justify-center text-sm text-zinc-500 font-light tracking-wide">
        <p>&copy; 2026 FLYHISOCIAL. All rights reserved.</p>
      </div>
  </footer>"""

for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the Contact Desk description
    m = re.search(r'<p class="[^"]*">\s*(Connect directly with our[^<]+?)\s*</p>', content)
    contact_desc = m.group(1).strip() if m else "Connect directly with our Lead Solutions Architect."
    
    new_footer = footer_template.replace('{contact_desc}', contact_desc)
    
    # Replace the existing footer
    content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file}")
