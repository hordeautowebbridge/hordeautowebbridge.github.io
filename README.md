# HordeAutoWebBridge
# [hordeautowebbridge.github.io](https://hordeautowebbridge.github.io)

A Javascript based Stable Horde Worker bridging **Automatic1111 API with Stable Horde API** that runs **entirely in browser**. (Yay javascript)
No Python, no extra 20 GB downloads, or duplicate installs... just edit one line, open a browser, click and share any/all of your own local SD models from A111.
Unlike the existing Automatic1111 worker extension, this worker also supports **hosting multiple selected models simultaneously**, and does the switching for you. 
It also attempts to automatically determine the horde name of the models you have based on filename.
Supports running workers for txt2img, img2img, inpainting, and all default horde worker flags.

Caveats: 
1. Although the user can express a preference to avoid nsfw, it cannot be guaranteed as this worker runs entirely from the web, it cannot (and should not) download/install new models for the user, and without CompVis stable-diffusion-safety-checker it means it will not have a NSFW filter. 
2. For now, R2 not directly supported. As we are running from browser, accessing/uploading to R2 buckets may present some issue with CORS restrictions, since it's on different domains, don't wanna deal with it yet. Thus this uses bridge_version 7 and support only b64 *for now*.  
3. The .ckpt filenames many A1111 users use may have different filenames from the "official" horde model names. Since calculating hashes on file system is not possible in browser, plus many people use different variants of the same model (fp16/32/pruned), I match them via db.json list of ckpt filenames instead. As this may have inaccuracies, I've also added a way for users to rename their local model identifiers based on the list of models from horde.
4. API documentation is limited, I have tried to make this as standards compliant as possible, so let me know if something is not right. To aid debugging, this worker uses client_agent = "HordeAutoWebBridge:1" so any misbehavior can be monitored and reported.

Do give it a try and let me know. It's fully open source so feel free to look, but if anyone has concerns I'd suggest using a different API key for peace of mind.
