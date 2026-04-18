# 👻 Macmask
                                        
# #          ## #                       
###  ## ### #   ###  ## ##  ### ### ### 
### # # #   #   # # # # # # # # ##  #   
# # ### ### #   # # ### # #  ## ### #   
# #          ##             ###         
    >> IDENTITY: CLOAKED | STATUS: GHOST <<
> *"The ghost is in the shell. The footprints are gone."*

**Macmask** is a minimalist Python script designed to automate MAC address randomization on **Arch Linux** systems. Built for those who avoid shortcuts and demand total control over their network identity.

---

## 🛠️ Requirements
The system must have the following packages installed:

*   **Python 3.x**
*   **macchanger** (`sudo pacman -S macchanger`)
*   **iproute2** (Standard on Arch)

## 📋 Features
- [x] **Interface Management**: Automatically toggles state (Target: `wlan0 and wlan1`)
- [x] **Full Randomization**: Generates a completely new MAC with random OUI
- [x] **Stealth Feedback**: "Ghost Ops" style status messages
- [x] **Robustness**: Integrated error handling for subprocess calls
- [x] **Identity Recovery**: Dedicated script to restore original hardware MAC

To hide indentity run:
 sudo python Macmask.py

To restore identity run: 
 sudo python Macunmask.py

## 📬 Contact & Support
If you encounter any issues, have questions, or just want to talk about Analog Horror and Arch Linux:

*   **GitHub Issues**: Open a ticket here on GitHub (preferred for bugs).
*   **Discord**: [goldenfredddy17330]
*   **TikTok** [sayori_246]

*"Stay safe, stay anonymous."*
