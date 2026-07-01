# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-274**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-274**

---

### 251. [Analytic Cut in Epistemic Logics with Distributed Knowledge](https://arxiv.org/abs/2606.31886)

**<font color=#1a73e8>作者：</font>** Ryo Murai, Sizhuo Liu, Katsuhiko Sano  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Distributed knowledge is a notion of group knowledge studied in multi-agent epistemic logic. Semantically, the distributed knowledge of a group is interpreted via an accessibility relation given by the intersection of the epistemic accessibility relations of the agents in that group. This paper investigates sequent calculi for epistemic logics of distributed knowledge based on K45, KD45, and S5. While cut elimination holds in existing sequent calculi for modal logics K45 and KD45, it fails in all the systems mentioned above. Instead, we establish the analytic cut property for all three systems by adapting Takano' s (2018) strategy, which restricts the cut formulas to the set of subformulas of the conclusion of the cut rule. As a corollary, the Craig interpolation theorem holds for all logics considered. We also show that all proof-theoretic results remain valid when the empty group is allowed for the distributed-knowledge operator, in which case the distributed knowledge for the empty group is interpreted as the global modality.

---


### 252. [RESOLVE: A Multi-Resolution and Multi-Modal Dataset for Roadside Cooperative Perception](https://arxiv.org/abs/2606.31895)

**<font color=#1a73e8>作者：</font>** Shaozu Ding, Linan Song, Marco De Vincenzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR has increasingly been integrated into traffic cameras to expand coverage and mitigate occlusion in roadside cooperative perception. However, how unimodal and camera-LiDAR fusion architectures behave under variations in LiDAR point sparsity induced by sensor configurations and scene-dependent sensing conditions remains underexplored. We introduce RESOLVE, a large-scale real-world benchmark dataset featuring multi-resolution roadside LiDAR and synchronized camera-LiDAR sensing for systematic evaluation of unimodal and fusion-based architectures in roadside 3D detection and tracking. RESOLVE contains over 100k images and 26k point cloud frames with 220k manually annotated bounding boxes, captured at a real-world urban intersection across diverse lighting and weather conditions and spanning 10 classes of traffic participants. In particular, RESOLVE enables controlled evaluation across three LiDAR resolution levels while keeping all other sensing and environmental factors fixed. This allows fair cross-architecture comparisons under point cloud distribution shifts resulting from resolution variations, sensing distance, and training-inference resolution mismatches. Results from extensive benchmark experiments reveal insights into how multimodal fusion can compensate for LiDAR point sparsity, offering clues for designing cost-efficient roadside multimodal perception. The dataset and benchmark codes are available at this https URL.

---


### 253. [Sequential RC-TGAN: Generating Relational Time Series with Spectral Envelope Loss](https://arxiv.org/abs/2606.31904)

**<font color=#1a73e8>作者：</font>** Mohamed Gueye, Yazid Attabi, Manuel Morales 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The generation of synthetic relational databases often involves modeling complex temporal dynamics, such as transaction logs or event sequences. A significant challenge in this domain is the handling of categorical time series (e.g., status codes), where standard encoding methods like one-hot encoding fail to capture intrinsic frequency-domain features such as seasonality and cyclicity. In this paper, we introduce Sequential RC-TGAN (Seq. RC-TGAN), a temporal extension of the RC-TGAN framework, equipped with a novel integrated loss function based on the \textit{Spectral Envelope Theory}. This differentiable loss allows the generator to directly optimize the preservation of latent periodic structures via backpropagation. While spectral envelope theory is inherently designed for categorical sequences, we extend this frequency-domain regularization to continuous time series by employing a Variational Gaussian Mixture Model (VGM) discretization strategy. To establish a mathematically rigorous evaluation standard, we simulate categorical time series governed by a parameter $\alpha$, with exactly known theoretical spectral envelopes. Integrating these dynamic sequences into the child tables of a relational database yields a robust ground-truth benchmark for evaluating the frequency-domain fidelity of our generative framework. Furthermore, we address the lack of robust evaluation standards for relational time series by proposing two new metrics: Spectral Density Divergence and Spectral Envelope Divergence. Experimental results on real-world datasets, as well as our simulated benchmarks, demonstrate that our end-to-end approach significantly outperforms state-of-the-art systems in reproducing cyclic patterns and long-term seasonality across both categorical and continuous features.

---


### 254. [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)

**<font color=#1a73e8>作者：</font>** Junzhe Jiang, Zipei Ma, Zijie Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-curated 3D assets hinders large-scale deployment. To address these challenges, we propose DriveWeaver, a novel framework for controllable vehicle insertion in autonomous driving simulation. Specifically, for a masked target insertion area, DriveWeaver performs video inpainting conditioned on vehicle point clouds to generate high-quality, temporally consistent vehicles. This video-inpainting-based approach ensures seamless blending between the foreground and background, while the readily available point cloud conditions enable superior generalization. To support long-term generation, we further design a global-to-local hierarchical inpainting strategy, ensuring the consistent identity and appearance of the inserted vehicles. Meanwhile, we extract explicit 3D Gaussian representations of the inserted vehicles through an urban reconstruction pipeline to enable real-time rendering for autonomous driving simulation. Extensive experiments across diverse datasets demonstrate that our method outperforms existing baselines in visual realism and geometric consistency, providing a robust tool for scalable autonomous driving scene augmentation.

---


### 255. [Interface-Aware Neural Newton Preconditioning for Robust Cohesive Zone Model Simulations](https://arxiv.org/abs/2606.31921)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Huanhuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cohesive Zone Models (CZMs) are widely used to simulate interface fracture, delamination, adhesive failure, and fiber--matrix debonding in aerospace composite structures. In implicit quasi-static finite element analyses, cohesive softening may introduce negative interface tangents, solution jumps, and Newton-basin mismatch, so the previous converged state can become a poor initial guess for the next increment. This may lead to stagnation, wrong-branch convergence, or repeated step cuts. Existing remedies, including viscous regularization, path following, dynamic relaxation, and manual Newton--Raphson (NR) modification, either alter the effective response, increase cost, or rely on hand-crafted interface rules. This work proposes an Interface-Aware Neural Newton Preconditioner (IA-NNP) for difficult CZM increments. IA-NNP recasts manual NR modification as rule-based interface lifting and generalizes it into a learned, state-dependent interface correction. The method acts only on active interface variables and preserves the original traction--separation law, residual assembly, tangent evaluation, history update, and dissipation checks. Two realizations are developed: IA-NNP-Init for learned initial-guess lifting and IA-NNP-NL for iteration-level nonlinear right preconditioning. Interface graph features encode opening, traction, tangent, damage/history variables, mode mixity, residuals, and neighboring states. The correction is bounded, confidence-gated, and accepted only through the original CZM Newton solve. A root-equivalence property shows that IA-NNP changes the path to convergence but not the discrete CZM solution set. Tests on horizontal, circular, two-interface, and active-front benchmarks show improved difficult-increment convergence, better branch recovery, and fewer failures than standard NR and manual NR modification, while preserving the force--displacement response.

---


### 256. [InstanceControl: Controllable Complex Image Generation without Instance Labeling](https://arxiv.org/abs/2606.31924)

**<font color=#1a73e8>作者：</font>** Xiaoyu Liu, Huan Wang, Fan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable image generation methods, such as ControlNet, have demonstrated a remarkable capacity to introduce visual conditions(e.g., depth maps) to guide image generation. However, these methods often struggle with complex multi-instance scenes, frequently leading to attribute confusion among instances. While recent approaches attempt to mitigate this via manual instance labeling, such requirements are labor-intensive. In this paper, we propose InstanceControl, a novel multi-instance controllable generation method that eliminates the need for instance labeling. We identify the primary bottleneck in existing methods as the inability to accurately associate instance descriptions with their corresponding regions within visual conditions. To address this, we leverage the Vision-Language Model (VLM) to establish instance-level correspondences between text prompts and visual conditions. Specifically, the VLM automatically parses instance descriptions from the text prompts and simultaneously predicts instance masks based on the visual conditions. Furthermore, since the predicted masks may contain noise, we introduce an adaptive mask refinement strategy that dynamically refines these instance masks during the generation process. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods, achieving superior fidelity and precise instance-level control.

---


### 257. [No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs](https://arxiv.org/abs/2606.31933)

**<font color=#1a73e8>作者：</font>** Haojian Huang, Harold Haodong Chen, Meng Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VidPair-Halluc, a new benchmark for evaluating video hallucination in large video models (LVMs) under rigorous and controlled conditions. Unlike previous benchmarks that primarily rely on text-based perturbations or adversarial questions while neglecting the consistency of visual backgrounds, VidPair-Halluc features video pairs with highly similar backgrounds but distinctly different foreground semantics, enabling precise attribution of model errors to genuine hallucination rather than background variation. The benchmark is constructed through PairFlow, a pipeline that leverages recent advances in text-to-image and video generation to systematically compose stories, generate coherent video clips, and assemble them into adversarial pairs. Covering both spatial and temporal reasoning across ten semantic aspects, VidPair-Halluc comprises 1K high-quality adversarial video pairs and 11K spatio-temporal QA pairs with control over background and foreground variations. Evaluations on mainstream LVMs show persistent difficulty with robust fine-grained video understanding in adversarial settings, and code and data are available at the this https URL.

---


### 258. [Making Sense of Touch from the Child's View for Contrastive Learning](https://arxiv.org/abs/2606.31943)

**<font color=#1a73e8>作者：</font>** Max Whitton, Zecheng Wang, Puchen Liu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Is the sense of touch a mechanism for human babies' learning of visual concepts? If so, can we quantify its importance, and to what extent do babies rely on their sense of touch for visual learning? To approach these questions in a principled way, we propose a structured coding system for baby-centric touch events, yielding a dataset of 264k two-second clips of touch events coded according to this system. Using this dataset, we pretrain developmentally grounded models that reveal promising insights into the nature of baby learning from touch.

---


### 259. [World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration](https://arxiv.org/abs/2606.31946)

**<font color=#1a73e8>作者：</font>** Ye Chen, Xuanhong Chen, Yupeng Zhu 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance level $4D$ $(3D + T)$ physical world. Consequently, content creators cannot specify geometry, motion, camera parameters, or lighting in a deterministic, quantitative way, leading to the infamous ''gacha'' loop that makes professional content creation prohibitively inefficient and expensive. To address this, we introduce the World Narrative Model (WNM), a paradigm that decouples what to render -- the structured physical narrative -- from how to render -- the pixel generation process. WNM replaces end-to-end black-box sampling with orchestrated $4D$ pre-visualization for media generation. Collaborative agents translate sparse multimodal inputs, including text, reference videos, and sketches, into a fully editable world representation with scene geometry, object layouts, character/animal skeleton motion, trajectories, camera motion, and lighting at quantitative, physically meaningful granularity. This representation acts as a deterministic structural blueprint that drives existing video foundation models, either frozen or lightly adapted, to render final footage, turning the base model into a faithful neural shader. Built on this engine, our human-AI platform supports automatic world generation and pre-visualization aligned with professional filmmaking pipelines, while director consoles enable seamless human refinement. Experiments show that WNM greatly reduces probabilistic ``gacha'' calls and produces videos whose layout, motion, and cinematography closely follow creator intent. The framework is open and modular, allowing each component, such as world representation, control agents, and adapters, to be independently improved. Project website: this https URL.

---


### 260. [LuxEmo: Expressive Text-to-Speech Corpus for Luxembourgish](https://arxiv.org/abs/2606.31947)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani, Sandipana Dowerah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology research. In this work, we introduce LuxEmo, a 21-hour conversational expressive speech corpus for Luxembourgish with 4 emotion categories. LuxEmo is derived from Radio Télévision Luxembourg (RTL) youth broadcasts, using automated detection followed by human validation. We propose a semi-automatic curation workflow combining voice activity detection, denoising, language identification, LuxASR-based segmentation, automatic emotion prediction, lexical cues, and targeted human review. Additionally, we benchmark five expressive TTS systems covering German-based cross-lingual transfer, multilingual Luxembourgish support, Luxembourgish adaptation, and non-parametric prosody transfer. Performance is evaluated using both objective metrics and human evaluation.

---


### 261. [AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint Transfer](https://arxiv.org/abs/2606.31959)

**<font color=#1a73e8>作者：</font>** Xinyu Hou, Xiaoming Li, Zongsheng Yue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth-of-field control is a fundamental tool in photography, yet post-capture bokeh editing from a single image remains challenging. A practical editor should handle images captured under arbitrary focus and aperture settings. Existing methods typically assume an all-in-focus input, or first recover an all-in-focus image before rendering new bokeh. Such pipelines can discard useful blur cues from the source image and propagate reconstruction artifacts into the final edit. We introduce AnyBokeh, a physics-guided framework for any-to-any bokeh editing. Instead of treating source blur merely as a degradation to be removed, AnyBokeh estimates the source blur state with a signed circle-of-confusion map and a disparity map. By modeling the linear relation between signed circle of confusion and disparity difference, AnyBokeh estimates a source-specific optical fingerprint and transfers the source optical characteristics to the desired focus and aperture setting. A generative editor conditioned on both source and target circle-of-confusion maps then performs relative blur synthesis, enabling spatially adaptive deblurring, preservation, and defocus rendering. To support physically supervised learning, we further construct a high-fidelity synthetic dataset with accurate depth, focus distance, and full EXIF metadata. Experiments on real-world benchmarks show that AnyBokeh achieves faithful and controllable editing across any-to-any bokeh editing, all-in-focus-to-bokeh rendering, and defocus deblurring, while avoiding all-in-focus reconstruction and test-time bokeh-level calibration commonly required by existing approaches. The code and dataset will be available at this https URL.

---


### 262. [Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings](https://arxiv.org/abs/2606.31979)

**<font color=#1a73e8>作者：</font>** Gabi Pragier, Matan Karklinsky, David Ungarish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we propose a unified framework that leverages them as a source of geometric constraints. Our key insight is that each planar surface visible across multiple views provides an independent estimate of relative camera poses through homography decomposition. By aggregating estimates from multiple planes or even from a single dominant plane we achieve robust pose recovery in scenarios where traditional methods fail. We introduce a novel graph-based approach that constructs a pose-graph from homography estimates and employs spectral embedding to identify and filter unreliable edges. Our method maps homography-based pose estimates onto the real line based on their geometric and visual consistency, enabling efficient extraction of a maximally consistent spanning tree for pose recovery. This approach naturally handles both highly planar scenes, such as indoor sports arenas, and general $3$D environments. We demonstrate superior performance on basketball court imagery where existing methods struggle, while matching or exceeding state-of-the-art results on unconstrained outdoor scenes from the IMC Phototourism benchmark.

---


### 263. [LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981)

**<font color=#1a73e8>作者：</font>** Peng Li, Rawal Khirodkar, Junxuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based motion regressor disentangles global rigid motion from fine-grained local dynamics to capture both coherent movement and subtle non-rigid effects. To resolve the inherent ambiguity of 2D-to-3D lifting while scaling beyond fitted datasets, we introduce hybrid supervision that distills soft structural priors from an LBS teacher and a loss that supports training on both limited fitted data and large in-the-wild unlabeled videos. Extensive experiments show LUNA achieves competitive visual fidelity compared to LBS-based approaches, while delivering realistic human motion and zero-shot cross-identity generalization across diverse driving modalities. To the best of our knowledge, LUNA is the first end-to-end 3D animatable model that supports implicit 2D driving.

---


### 264. [Amplifying Membership Signal Through Chained Regeneration](https://arxiv.org/abs/2606.31991)

**<font color=#1a73e8>作者：</font>** Wojciech Łapacz, Stanisław Pawlak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI) attacks often rely on one-shot generations, which yield weak signals and limited sensitivity across modalities. Inspired by Model Autophagy Disorder (MAD), we introduce MADreMIA, a model-agnostic framework that enhances white-, gray-, and black-box MIA and DI. Rather than relying on shadow model training -- often infeasible for large generative models -- our framework facilitates scalable inference by leveraging inherent signals through iterative trajectories. This process utilizes chained generations across diverse modalities, where each output serves as the subsequent input, to improve membership evidence at low FPR. We demonstrate that memorized training samples exhibit significantly higher coherence and slower degradation during iterative regeneration than non-member generations. Our results show that MADreMIA provides richer signals across diverse model families and modalities; we present comprehensive evaluations for IARs, diffusion, and language models, alongside preliminary results demonstrating its potential for audio models.

---


### 265. [Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis of Delayed Generalization](https://arxiv.org/abs/2606.32000)

**<font color=#1a73e8>作者：</font>** Srijan Tiwari, Aditya Chauhan, Manjot Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why do neural networks memorize algorithmic training data long before they generalize? We present a geometric case study demonstrating that, on tasks where generalization requires discovering structured low-dimensional circuits, the memorization-generalization delay is driven by radial inflation of hidden representations under cross-entropy optimization. We formalize a radial-angular decomposition of activation-space dynamics and derive three testable propositions: (i) that penalizing radial inflation induces anisotropic, data-dependent weight regularization; (ii) that it suppresses radial gradient energy below the isotropic random baseline, forcing predominantly angular updates; and (iii) that it biases convergence toward flatter minima. To empirically validate these propositions, we study a single-hyperparameter norm penalty that softly constrains activations to a sqrt(d)-radius hypersphere. On modular arithmetic, this penalty accelerates grokking up to 6x across MLPs and Transformers, and halves training steps for a 10M-parameter nanoGPT on 3-digit addition.

---


### 266. [PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines](https://arxiv.org/abs/2606.32004)

**<font color=#1a73e8>作者：</font>** Sameer Malik, Ayush Singh, Amar Prakash Azad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizational policy guidance into an executable review engine consisting of typed relational logic rules and atom-level extraction questions. During review, LLMs answer these local questions using retrieved document evidence, and a symbolic evaluator applies the formal rules to detect non-compliance. We instantiate and evaluate PolicyGuard on company-specific NDA compliance review, where contract clauses must be checked against organization-specific negotiation policies. By separating policy formalization, local document interpretation, and symbolic compliance evaluation, PolicyGuard makes document review more explicit, maintainable, and systematically testable.

---


### 267. [Scalable Behaviour Cloning on Browser Using via Skill Distillation](https://arxiv.org/abs/2606.32014)

**<font color=#1a73e8>作者：</font>** Kaisen Yang, Zheng Jiang, Yuzhao Peng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human browsing a highly scalable but under-exploited source of reusable browser skills. We argue that the bottleneck for browser agents is decision-making under incomplete information rather than low-level operation, and that the priors agents lack are already implicit in human interaction traces. We therefore study scalable behavior cloning for browser agents via skill distillation, converting user interaction trajectories into compact natural-language skills that agents can read, retrieve, reuse, and compose directly. We further organize the distilled skills into a skill graph so that growth proceeds through consolidation rather than unbounded accumulation. This suggests that the scalability of browser agents may come less from manually designed tasks and more from the collective skills already expressed by internet users. Our project is available at: this https URL.

---


### 268. [Automated Background Swapping for Robustness against Spurious Backgrounds](https://arxiv.org/abs/2606.32018)

**<font color=#1a73e8>作者：</font>** Cesar Roder, Kajetan Schweighofer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the target label in the training data but are not causally linked and thus fail to generalize. For the vision domain, many such spurious correlations manifest themselves within the background of the image, where only the foreground is predictive of the class label. In this paper, we introduce Automated Background Swapping (AutoBackSwap) to reduce the reliance of classifiers on such spurious backgrounds. AutoBackSwap uses a secondary network to disentangle the foreground and background, followed by infilling to synthesize complete backgrounds, and finally combines different foregrounds and inpainted backgrounds to augment the training data. We find that patch-wise labeling of just a few hundred samples suffices to train the secondary network and automatically augment the full training dataset on challenging image classification tasks. In contrast to many previous methods, AutoBackSwap proves very effective even if there is not a single sample in the training data breaking the spurious correlation. Across a range of image classification tasks with spurious backgrounds, AutoBackSwap consistently outperforms prior methods.

---


### 269. [Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers](https://arxiv.org/abs/2606.32020)

**<font color=#1a73e8>作者：</font>** Anh Nguyen, Ngan Nguyen, Duc Vu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern one-step diffusion models achieve impressive quality through distribution-based timestep distillation. Yet, they rely on a critical assumption: Teacher and Student must inhabit the same latent space. This Shared-Space constraint prevents knowledge transfer from modern high-capacity Teachers (e.g., SD 3.5 and Flux) into compact, deployment-friendly Students such as SD 1.5, whose latent resolution and VAE parameterization differ from the Teacher. We formalize this overlooked regime as Cross-Space Distillation, where Teacher and Student differ in both latent resolution and VAE space. To enable distillation under this mismatch, we introduce the Bridge, a lightweight latent interface that maps Student latents into the Teacher space without modifying the Student backbone. Bridge combines a frozen Student VAE decoder as a spatial prior with a compact learnable projector, and is trained with latent reconstruction and attention fidelity objectives for stable Teacher-space alignment. Across diverse modern Teachers, Bridge enables substantial gains for compact one-step Students; for example, it improves SD 1.5 from 5.4 to 9.4 HPSv3 while preserving one-step inference, low latency, and broad ecosystem compatibility. These results show that heterogeneous large Teachers can be distilled into efficient, deployable backbones through a lightweight latent-space interface.

---


### 270. [FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data](https://arxiv.org/abs/2606.32023)

**<font color=#1a73e8>作者：</font>** Emilie Vautier, Clément Mallet, Cédric Vega  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forest attributes are essential for national-scale resource monitoring. Airborne LiDAR metrics are among the auxiliary variables most strongly correlated with forest attributes used in National Forest Inventory (NFI) estimates. However, producing wall-to-wall predictions remains challenging when LiDAR data are acquired under heterogeneous conditions. As national LiDAR programs expand across Europe, variability in sensors, flight parameters, seasons, and scan angles limits the robustness of existing models, which are often calibrated for local conditions. We present FLORA (Forest LiDAR Octree Regression with Auxiliary Data), a deep learning framework that predicts six forest attributes: dominant height, total volume, deciduous volume, coniferous volume, basal area, and stem density from heterogeneous LiDAR point clouds. FLORA combines an octree-based backbone with ecological and spatiotemporal auxiliary variables through a late-fusion gating mechanism. Models are trained and evaluated on 32,052 National Forest Inventory plots across mainland France using data from the French LiDAR HD program. A single model trained on both leaf-on and leaf-off acquisitions outperforms season-specific models and improves cross-season robustness. Auxiliary variables provide modest overall gains but contribute more strongly to species-specific volume prediction. FLORA achieves an rRMSE of about 12.3% (R2 = 0.88) for dominant height and 39% (R2 = 0.74) for total volume, providing a robust baseline for large-scale forest attribute estimation from heterogeneous national LiDAR programs.

---


### 271. [SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical RoPE](https://arxiv.org/abs/2606.32033)

**<font color=#1a73e8>作者：</font>** Or Hirschorn, Aaron Olender, Eli Alshan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a zero-shot, training-free and optimization-free framework for generating 360 panoramic images and videos by directly injecting spherical priors into pre-trained diffusion transformers. Existing methods either rely on costly fine-tuning on scarce panoramic data that limits generalization, or leverage multi-step optimization that incurs prohibitive inference latency. We observe that contemporary generative models natively exhibit some panoramic priors from large-scale training. However, these emergent capabilities are insufficient, as the models fundamentally fail to satisfy the rigorous topological constraints imposed by equirectangular projection (ERP). We introduce a zero-shot and optimization-free approach that resolves these constraints at inference time. Spherical RoPE replaces standard rotary position embeddings: low-frequency channels are re-parameterized as 3D Cartesian coordinates to natively encode the spherical manifold, while high-frequency channels are harmonically quantized to enforce exact periodicity. Coupled with complementary Semantic Distortion classifier-free guidance (CFG) that explicitly steers geometry, we avoid retraining and inherit the full creative breadth of state-of-the-art models. Our approach generalizes across diverse backbones and 360 generation modalities. We demonstrate this across text-to-panorama using Flux.1, Flux.2, and LTX-Video backbones, achieving competitive performance against baselines, all while remaining training-free. Project page: this https URL

---


### 272. [PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036)

**<font color=#1a73e8>作者：</font>** Yujie Guo, Yudong Jin, Lingteng Qiu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

---


### 273. [Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision](https://arxiv.org/abs/2606.32038)

**<font color=#1a73e8>作者：</font>** Zifan Carl Guo, Laura Ruis, Jacob Andreas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different families, frequently produce explanations more faithful to their own current behaviors than to those of their training targets. This "introspective" coupling between LM explanations and behaviors occurs when training explanations remain sufficiently correlated with current behaviors over the course of training, even as behaviors themselves shift. We also show that introspective coupling tracks behavior shifts: when explanation training is provided concurrently with other post-training objectives, explanations track those shifts without requiring updated supervision. This phenomenon appears in multiple tasks, including sycophancy and refusal, and is robust to label noise. Overall, our results show that even fixed datasets of counterfactual explanations can provide scalable and generalizable post-training signal for introspection.

---


### 274. [GEAR: Guided End-to-End AutoRegression for Image Synthesis](https://arxiv.org/abs/2606.32039)

**<font color=#1a73e8>作者：</font>** Bin Lin, Zheyuan Liu, Chenguo Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generative models are typically trained in two stages. A tokenizer is first trained for reconstruction and then frozen, after which a generator is trained on its discrete indices or continuous latents. This decoupling leaves the tokenizer unaware of what the generator finds easy to model. We present GEAR (Guided End-to-end AutoRegression), which trains a vector-quantized (VQ) tokenizer and an autoregressive (AR) generator jointly and end-to-end, guided by representation alignment. The key obstacle is that the VQ index fed to the AR model is non-differentiable, so gradients cannot reach the tokenizer, and a straight-through estimator collapses. GEAR resolves this with a dual read-out of the codebook assignment. A hard, one-hot branch trains the AR with next-token prediction, while a differentiable soft branch carries a representation-alignment loss that flows back to guide only the tokenizer. The AR model thereby steers its tokenizer toward an index distribution it can predict more easily. This shifts the alignment burden from the tokenizer to the AR: the tokenizer's own features become less DINOv2-like while the AR's become more so, the opposite of diffusion-side recipes that make the latent itself semantic. GEAR speeds up ImageNet gFID convergence by up to 10x relative to the strong LlamaGen-REPA baseline, learns markedly better patch-level and spatially-coherent features, and generalizes across quantizers (VQVAE, LFQ, IBQ) and to text-to-image generation.

---


> [!TIP]
> 当前位于：**251-274**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-274**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
