#-------------------𝐷𝑂𝑁'𝑇 𝑇𝑅𝑌 𝑇𝑂 𝐸𝐷𝐼𝑇 𝑇𝐻𝐼𝑆 𝑆𝐶𝑅𝐼𝑃𝑇-----------------#
import platform,subprocess 
subprocess.call(["git", "pull"])
if __name__ == '__main__':
    try:
      if platform.machine() == "aarch64":
            subprocess.call(["bash", "turn", "switch"])
            subprocess.call(["bash", "required"])
            subprocess.call(["chmod", "+x", "ANTI"])
            subprocess.call(["./ANTI"])
      elif platform.machine() == "x86_64":
            subprocess.call(["bash", "turn", "switch"])
            subprocess.call(["bash", "required"])
            subprocess.call(["chmod", "+x", "ANTI"])
            subprocess.call(["./ANTI"])
      elif platform.machine() == "armv8l":
            subprocess.call(["bash", "required"])
            subprocess.call(["chmod", "+x", "ANTI"])
            subprocess.call(["./ANTI"])
      elif platform.machine() == "armv7l":
            subprocess.call(["bash", "required"])
            subprocess.call(["chmod", "+x", "ANTI"])
            subprocess.call(["./ANTI"])
      else:
            print(f"YOUR {platform.machine()} bit, SUPPORT ONLY  aarch64 , armv8l , x86_64!")
            exit()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        print(f"[Error] {str(e).capitalize()}!")
        exit()
      
#---------------------------------------------------------#
#               𝑇𝐻𝐼𝑆 𝑇𝑂𝑂𝐿 𝐼𝑆 𝑂𝑁𝐿𝑌 𝐹𝑂𝑅 𝑈𝑆𝐸𝑅'𝑆
#                  • 𝐴𝑁𝑇𝐼 𝑆𝑃𝐼𝑅𝐴𝐿 •
#---------------------------------------------------------#
 
