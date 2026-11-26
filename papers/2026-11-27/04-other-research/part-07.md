# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-314**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-314**

---

### 301. [Focus Only on What's Important: Training-Free Focus Maps for Frozen Vision Transformers in Long-Video Object Segmentation](https://arxiv.org/abs/2611.34863)

**<font color=#1a73e8>作者：</font>** Harsha Karipineni, Rajesh Reddy Chintha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers are strong but costly image encoders for video object segmentation. Training-free token merging cuts compute uniformly across the frame, including on tracked objects. We give a frozen DINOv3 ViT inside a trained Cutie head a training-free focus map: full resolution where the segmenter expects its objects and coarser merging elsewhere. Protecting only the previous frame's mask works on short clips but fails on long videos, where fast motion pushes targets outside the margin and into background merging, locking in loss. Our policy instead takes the union of velocity-shifted and block-matched masks, runs a camera-compensated surprise check, delegates uncertain regions to the compared merger, and falls back to it when all objects are lost. On long videos (LVOS V2 valid, pre-specified protocol, three ViT-S seeds), it beats ALGM 0.98 by +2.76 J&F (95% object CI [+1.22,+4.44]; video-cluster [+0.99,+4.52]) at 16% fewer counted encoder FLOPs (0.385 vs. 0.459), sitting 1.0 J&F point below the dense-encoder baseline; at ViT-B the gain over ALGM 0.95 is +3.89 [+2.03,+5.87]. On DAVIS 2017 val it stays within -0.19 J&F of the dense encoder at ViT-S (-0.12 at ViT-B). Controls qualify the result: protecting only the previous mask under ALGM matches or exceeds accuracy at higher FLOPs (0.486), so expectation and surprise mainly reduce counted encoder compute. Practically, lower counted encoder compute did not reduce startup-inclusive mean Cutie step time on a 12-video LVOS sample (3%-8% lower in steady state; an equally engineered ALGM is faster at ViT-S and ViT-B). Section 5.2 separately examines a Cutie permanent-memory schedule and its latency and memory trade-offs. Code: this https URL

---


### 302. [SoK: When FL Clients Cannot Train -- Delegated Federated Learning for IoT](https://arxiv.org/abs/2611.34876)

**<font color=#1a73e8>作者：</font>** Hamed Mohammed Alkharsh, Aydin Abadi, Jakub Szelag 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) assumes that a client can perform the computation required to produce its own contribution. This assumption is often unrealistic for resource-constrained Internet of Things (IoT) devices, motivating designs that delegate some or all client-side training to more capable parties. We systematize this setting as delegated federated learning (Delegated FL), where data ownership and execution of owner-attributed learning are separated. We develop a framework that examines three dimensions over the same delegated transition: delegate-view privacy, delegated attribution, and constrained-owner feasibility. Our audit of 29 systems reveals a recurring composition gap. Privacy mechanisms protect selected artifacts without necessarily characterizing the accumulated view. Attribution mechanisms establish individual execution relations without necessarily binding the complete delegated transition. Furthermore, computational offloading does not establish whether the remaining workload fits the owner's resource budget. Two controlled studies on Raspberry Pi devices illustrate these gaps. We show that encrypted inputs can coexist with information leakage through an exposed residual and that locally retained labels remain inferable from split-learning gradients. We also show that message authentication can reject tampering without establishing that the executor performed the prescribed computation. Our findings demonstrate why individually established guarantees do not necessarily support the same end-to-end claim and motivate evaluating privacy, attribution, and residual owner cost over the same delegated transition.

---


### 303. [Interpretable and Accurate Hybrid Decision Trees with Selective Case-Based Splits](https://arxiv.org/abs/2611.34887)

**<font color=#1a73e8>作者：</font>** Cristiano Landi, Alessio Cascione, Riccardo Guidotti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees are among the most well-known interpretable models in Machine Learning. Over the years, a wide variety of strategies have been proposed to define split conditions within the greedy learning framework, aiming to guide instance routing and enhance predictive performance. These strategies range from axis-parallel and oblique splits based on feature values to proximity-based splits using exemplar instances and more complex hybrid approaches. However, no single method has emerged as universally superior. In this work, we present two key contributions to the construction of greedy decision trees. First, we propose a hybrid tree architecture that integrates both feature-based and case-based splits, allowing for heterogeneous splits throughout the tree. Second, we introduce a novel type of split that leverages a selective case-based approach: when a split is needed, our method searches for the most informative subset of features to define the split, effectively balancing the specificity of case-based methods with the simplicity of feature-based ones. Experiments on a diverse set of tabular datasets show that our method outperforms standard decision trees and achieves performance on par with ensemble methods, while producing shallow trees that retain or even improve predictive accuracy.

---


### 304. [What a Drop Reveals: Sim-to-Real Material Estimation for Deformable Objects from Video](https://arxiv.org/abs/2611.34894)

**<font color=#1a73e8>作者：</font>** Ziyue Peng, Yanxi Hu, Junyoung Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How an object deforms when it hits the ground reveals what it is made of. From a single real video of a drop, we estimate a deformable object's density-normalized stiffness $E/\rho$, and its yield stress $\sigma_Y/\rho$ when the impact causes plastic deformation, with a feed-forward predictor trained only in simulation. Real videos carry no material labels, so such predictors are developed and validated on synthetic data alone. We show that synthetic validation ranks their geometric inputs in the wrong order. Material acts through 3D deformation, and tracklets lifted to 3D with estimated depth are indeed the most accurate input in simulation. However, on real drops they are the least accurate, and better depth does not repair them: the failure persists with simulator depth in training, LiDAR depth at test time, and exact depth on rendered replays of the real drops. Short 2D optical-flow tracklets do the opposite: they improve nothing in simulation, yet they transfer best. Material is therefore better read from what perception measures consistently in both domains than from what is most informative in simulation. Our predictor, PhysReader, reads the video and 2D tracklets and learns the lift to 3D in simulation by matching a teacher that sees exact 3D deformation. To measure transfer, we introduce PhysReader-Real: 16 everyday objects dropped five times each, with reference materials fit jointly to each object's drops and checked against tensile tests. On PhysReader-Real, PhysReader is closer to the reference materials than every other input and baseline. The one exception is a per-scene optimizer started from PhysReader's prediction, which ends slightly closer but takes 49 minutes per video instead of 12 seconds.

---


### 305. [Enhancing Maritime Domain Awareness using Latent Space Representations](https://arxiv.org/abs/2611.34899)

**<font color=#1a73e8>作者：</font>** Rikard Vinge, Miguel A. Belenguer-Plomer, Isabelle Wittmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly on compressed latent-space representations rather than on the original Sentinel-1 imagery, this approach directly addresses the data gravity bottleneck that increasingly constrains operational EO processing, in line with the objectives of the Embed2Scale project. In particular, linear and non-linear probing of compressed embeddings, latent space representations of synthetic aperture radar (SAR) imagery, is used to detect, localise, and characterise vessels from Sentinel-1 GRD images. Vessel detection achieves a ROC-AUC of 0.95, while vessel localisation has a median error of around 300 m for vessels longer than 100 m, and vessel AIS type-code classification achieves 62% accuracy for the majority classes. The latter, however, is highly correlated with vessel length. These results reveal both the potential and current limitations of Geospatial Foundation Models (GeoFMs) when applied to fine-grained MDA understanding in real-world scenarios.
Additionally, a new maritime remote sensing dataset is released, pairing about 2,000 Sentinel-1 images with temporally aligned AIS signals from commercial vessels. Through manual inspection, each candidate sample was verified for bounding-box quality and for consistency between the AIS-reported vessel length and the observed vessel extent, cross-checking vessel identity and location against publicly available vessel records and, where available, photographs. The dataset was made ready for use with the NeuCo-Bench neural compression benchmark framework, publicly available on HuggingFace through this https URL .

---


### 306. [$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920)

**<font color=#1a73e8>作者：</font>** Qihao Lin, Guanxu Chen, Shuhang Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $\mu$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated profiles of goals, knowledge, and permissions, adapting to the agent's speech and tool outcomes. Across 20 domains, 100 scenarios vary group size, acoustics, and follow-up demands to form 800 cases (408 tool-augmented, 392 tool-free). Joint Task Success (JTS) requires all user goals, privacy boundaries, and terminal states to hold jointly, while Pure JTS further disallows unauthorized tool calls; Attribution, Threading, and Coordination (ATC) diagnostics localize failures. Across 13 voice agents, proprietary systems peak at 62.24\% tool-free and 65.44\% tool-augmented success, while open-weight models remain below 20\%. ATC diagnostics show that open-weight models lag primarily in multi-turn attribution and threading, and controlled contrasts reveal that larger groups consistently degrade joint task success across capable systems. By coupling reactive multi-user simulation with verifiable session-level outcomes, $\mu$-Bench provides a rigorous testbed for shared voice agents.

---


### 307. [High-Fidelity Image Matting with Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2611.34929)

**<font color=#1a73e8>作者：</font>** Baihan Yang, Xin Lin, Yufan Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown strong potential for image matting by transferring generative priors learned from large-scale pretraining. However, existing approaches largely rely on latent diffusion models, whose compressed representations and VAE-based reconstruction introduce a mismatch with the high-frequency precision required for matting. We present PixelMatte, a framework that adapts pretrained pixel-space diffusion transformers for high-fidelity image matting. We show that strong image-conditioned matting capabilities can be acquired even from a pure text-to-image model without paired image-to-image pretraining. Our approach reuses the backbone's native patch embedding to jointly process the input image, trimap, and noisy alpha matte as spatially aligned tokens, enabling direct pixel-space prediction without additional condition encoders or adapters. With pixel-accurate synthetic supervision and real-image fine-tuning, PixelMatte predicts alpha mattes in a single forward pass. Two lightweight calibration modules, LayerShift and High-Pass Refiner, further improve regional opacity accuracy and boundary fidelity. Experiments across four benchmarks and two distinct pixel diffusion backbones demonstrate substantial improvements over existing methods, reducing SAD and gradient errors by 24-44% relative to RenderMatte on P3M-500-NP and AM-2K, while achieving competitive performance on AIM-500 and RenderMatte-2K. These results demonstrate the effectiveness of pixel-space generative priors for precision-sensitive image matting. Project page: this https URL.

---


### 308. [DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation](https://arxiv.org/abs/2611.34931)

**<font color=#1a73e8>作者：</font>** Agelos Kratimenos, Yile Hua, Kostas Daniilidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction with the structure of the motion itself. Building on DynMF, we model a scene's motion as a handful of SE(3) trajectories, each rigid, and let every point follow one of them alone, never a blend. DynMF2 computes this factorization directly from 3D point trajectories, with no rendering, by Expectation-Maximization (EM). Its M-step fits, in closed form, every rigid motion to the points assigned to it, and its E-step reassigns every point to the motion that explains it with the least error. The background is simply one more motion, the camera's, so no masks are needed. Three tools then revise the factorization: requery adds trajectories where the rendering shows parts the tracker missed, merge joins motions that move together, and split separates those that do not. Thus the number of motions follows the scene. Without masks, DynMF2 clearly outperforms the mask-based baselines in view synthesis on iPhone and NVIDIA and in 3D tracking on iPhone. It recovers what masks leave out, from thin parts and details to small movers far in the background. Its motions segment the moving parts of MOVi-F and iTACO scenes competitively, although DynMF2 is never trained to segment. What moves in a scene is not decided in advance: it emerges from the rigid motions themselves.

---


### 309. [Tokenisation is not in APX](https://arxiv.org/abs/2611.34938)

**<font color=#1a73e8>作者：</font>** Violeta Kastreva, Philip Whittington, Dennis Komm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we prove that, unless P=NP, no polynomial-time algorithm can find a tokeniser whose objective is within any constant factor of the optimum, meaning that tokenisation is not in the APX complexity class. We prove this for direct and bottom-up tokenisation, under both a compression or unigram log-likelihood objectives, and for binary or larger alphabets. We further show that, even over unary alphabets, direct tokenisation is APX-hard, and thus admits no polynomial-time approximation scheme.

---


### 310. [A Mesh for Every Moment](https://arxiv.org/abs/2611.34939)

**<font color=#1a73e8>作者：</font>** Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels. The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. Although common in real captures, large and fast motion poses a challenge that dynamic Gaussian splatting methods usually overlook. To account for it, we design a track-based initialization scheme that fits each Gaussian's initial trajectory to point tracks in closed form. We evaluate MEMO on Blender-Moments, a new benchmark of nine animated scenes with ground-truth meshes at every frame, and on two real-world datasets. MEMO reconstructs the most accurate geometry among state-of-the-art methods, and remains competitive in novel-view synthesis and training time. Project page: this https URL

---


### 311. [LuxAvatar: Real-Time Relightable Head Avatars via Causal Neural Shading of 3D Intrinsic Proxies](https://arxiv.org/abs/2611.34940)

**<font color=#1a73e8>作者：</font>** Yipengjing Sun, Chenyang Wang, Boyao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LuxAvatar, a feed-forward framework for real-time head avatar animation and relighting from a single portrait. To achieve both 3D controllability and complex facial light transport, we factorize avatar synthesis into an animatable 3D intrinsic Gaussian proxy and a causal autoregressive neural shader. This proxy disentangles canonical geometry and reflectance attributes, rapidly rasterizing deformed Gaussians into view- and motion-consistent PBR buffers. Conditioned on these buffers, our neural shader formulates forward rendering as a conditional video diffusion process, bypassing explicit PBR computation to synthesize realistic shading effects under target illumination. We achieve real-time streaming through heterogeneous distillation from a pretrained multi-step bidirectional relighting teacher to a two-step causal autoregressive neural shader, inheriting broad synthetic lighting priors while minimizing conditioning and decoding latency. To further specialize these priors to human heads, we construct a hybrid relighting dataset for domain-specific fine-tuning, capturing authentic facial dynamics and physically grounded light transport. Extensive experiments show that our framework enables 3D-controllable, real-time portrait animation and relighting, outperforming state-of-the-art methods in visual fidelity, motion control, and lighting accuracy.

---


### 312. [Improving and Expanding Video Editing Capabilities Without Videos](https://arxiv.org/abs/2611.34941)

**<font color=#1a73e8>作者：</font>** Ji Xie, Yanhao Jia, Xiangpeng Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks using an image editor. It enables efficient post-training with no architectural changes and no new videos, using only individual images. Our key idea is to let the video editor role-play as an image editor: it edits an image as a one-frame video, with the image editor guiding the video editor's predictions at each denoising step. Although the video editor sees only single images during training, at test time it applies the improved and expanded capabilities to whole video clips while preserving temporal consistency. To push the boundaries of video editing, we introduce OpenVE++, an extension of OpenVE-Bench that adds four new editing tasks useful for video production, including action changes, expression changes, body movements, and scene relighting. Our experiments across three different video editors show that I2VT improves existing editing capabilities and expands them to new tasks, and our models achieve state-of-the-art (SOTA) performance on both OpenVE-Bench and OpenVE++.

---


### 313. [AnyCam: Anything Can Represent Camera for Video Generation](https://arxiv.org/abs/2611.34944)

**<font color=#1a73e8>作者：</font>** Weijie Lyu, Zhixin Shu, Yuntian Ke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an object-centric scene, remains difficult. Existing methods condition either on camera parameters, which are scale-ambiguous in monocular video, or on explicit geometry such as warped point clouds or depth, which breaks down under large viewpoint changes. We present AnyCam, a method that represents the camera with an anchor object in the scene: we reconstruct it in 3D and render it along the target trajectory, a camera signal that is scale-aware, view-complete and easy to specify relative to the object. A video diffusion model transfers the content and dynamics of the source video to the new viewpoint. Its H-Concat layout aligns source and target frames in time, so the model can be distilled into AnyCam-AR, a streaming few-step generator for on-the-fly camera control. Both models are trained on paired videos with pixel-aligned anchor renderings from multi-camera videos and static-scene captures. Experiments on diverse datasets and trajectories show that AnyCam performs favorably against camera-controlled video generation and 3D reconstruction methods in camera control and visual quality.

---


### 314. [MidasTUI: Instant Tangible User Interfaces for Wearable Displays using Everyday Objects](https://arxiv.org/abs/2611.34945)

**<font color=#1a73e8>作者：</font>** Wen Ying, Xuweiyi Chen, Zezhou Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While wearable displays can bring digital workspaces anywhere, interaction remains limited by mid-air gestures that lack tactile feedback and induce fatigue, or controllers that are cumbersome to carry. We present MidasTUI, a system that instantly transforms arbitrary everyday objects into opportunistic tangible user interfaces through brief interaction demonstrations. For example, a user can slide an earbud case across a table as a mouse, enabling opportunistic interaction without carrying a dedicated input device. MidasTUI detects when a user is holding and moving an object using the wearable display camera and a Transformer-based temporal classifier. It then infers the intended input modality (e.g., slider, mouse, keypad) from hand movement and maps the tracked hand-object interaction to an application function. Our evaluations demonstrate reliable cross-object and cross-user generalization. A comparative user study further shows that grounding interaction in everyday objects reduces physical burden and improves perceived usability and control relative to mid-air interaction.

---


> [!TIP]
> 当前位于：**301-314**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-314**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
