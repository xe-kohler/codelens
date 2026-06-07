import React from "react";

export default function Header() {
  return (
    <header className="sticky top-0 bg-[#121212] min-w-full py-5 px-8 mb-10 flex flex-col md:flex-row sm:items-left lg:items-center justify-between gap-4 border-b border-gray-100/10 text-stone-400 font-[Montserrat]">
      {/* Left: Logo + Title */}
      <div className="flex items-center gap-2">
        <img
          src="/CodelensLogo.png"
          alt="Codelens logo"
          className="h-8 w-8 object-contain"
        />
        <h1 className="text-3xl font-black font-[Montserrat] text-[#EBEBEB]">CodeLens</h1>
      </div>

      {/* Center: Tagline */}
      <div className="text-left">
        <p className="text-sm lg:text-md font-medium text-stone-400">
         Your AI-Powered Python Investigator 🕵️‍♂️ 🐍  Built By Xavier Kohler | React, Python, Gemini & GPT 🚀 Non-Commercial 💘
        </p>
      </div>

      {/* Right: GitHub Link */}
      <div className="space-x-8">
         <a
          href="https://github.com/xavedtheday/codelens"
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm lg:text-sm font-light lg:font-medium"
        >
          <span className="underline hover:italic">GitHub</span>
        </a>
           <a
          href="https://xekohler-portfolio.web.app"
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm lg:text-sm font-light lg:font-medium "
        > 
          <span className="underline hover:italic ml-2 text-[#EBEBEB] font-bold">XEK: Portfolio</span>
        </a>
      </div>
    </header>
  );
}
