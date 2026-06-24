# 📦 其他研究 | 2026年06月25日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-219**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-219**

---

### 201. [AerialFusionMapNet: Online HD Map Construction with Aerial-Onboard BEV Fusion](https://arxiv.org/abs/2606.24784)

**<font color=#1a73e8>作者：</font>** Daniel Lengerer, Mathias Pechinger, Klaus Bogenberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution aerial imagery has recently emerged as a complementary modality for automated driving perception and has shown potential to improve birds-eye-view (BEV) scene understanding when fused with onboard sensors. Prior work demonstrated performance gains for online high-definition (HD) map construction through aerial-onboard fusion; however, conventional end-to-end fusion does not fully exploit the structural information contained in aerial representations. In this work, we introduce AerialFusionMapNet, a fusion-based mapping framework with a structured two-stage training strategy that explicitly enhances the contribution of aerial features within a unified pipeline. The proposed training scheme enables more effective integration of structural aerial priors. On the nuScenes geographic split, AerialFusionMapNet achieves up to 54.7 mAP, improving over prior aerial-onboard fusion baselines from 48.8 mAP by +5.9 absolute and +12.1% relative. The results suggest that structured training design, rather than increased architectural complexity, plays a more decisive role in unlocking the full potential of aerial imagery for online HD map construction. Code and trained models are available at this https URL.

---


### 202. [Counting Trees from Satellite Imagery with Noisy Supervision](https://arxiv.org/abs/2606.24786)

**<font color=#1a73e8>作者：</font>** Dimitri Gominski, Maurice Mugabowindekwe, Qiue Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counting individual trees is a fundamental task for environmental monitoring, yet remains largely unexplored with satellite imagery. At these resolutions, isolated trees may still be identifiable, but crown boundaries become ambiguous in dense forests, making the notion of an individual tree inherently ill-defined. Moreover, large-scale manual annotations of individual trees are prohibitively expensive. While scalable supervision can be derived from airborne LiDAR, the resulting annotations are noisy and difficult to exploit effectively.
We address these challenges by formulating tree counting as a spatial density matching problem supervised through Unbalanced Optimal Transport. This formulation naturally accommodates both precise localization of isolate trees and robust density estimation in dense forests. We further introduce a self-correction mechanism that leverages transport residuals to progressively refine noisy supervision during training.
We evaluate our approach on TinyTrees, a new benchmark spanning three continents and three satellite sensors, comprising over 215 million tree annotations (including 773K manually verified instances) across 23,000 this http URL. Our method consistently outperforms detection-based, regression-based, and transport-based distribution-matching baselines, demonstrating the effectiveness of unbalanced transport and reliability-aware supervision for large-scale tree counting from satellite imagery. Code, data and models are available at this https URL.

---


### 203. [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)

**<font color=#1a73e8>作者：</font>** Leshu Li, Jie Peng, Yang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at this https URL.

---


### 204. [OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799)

**<font color=#1a73e8>作者：</font>** Chenrui Fan, Paolo Favaro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

---


### 205. [DDStereo: Efficient Dual Decoder Transformers for Stereo 3D Road Anomaly Detection](https://arxiv.org/abs/2606.24805)

**<font color=#1a73e8>作者：</font>** Shiyi Mu, Zichong Gu, Zhiqi Ai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo-based 3D object detection still faces two critical safety challenges: real-time performance and open-set generalization. Existing stereo 3D methods typically achieve twice the accuracy of monocular methods but suffer from significantly lower inference speeds, making them unsuitable for real-time applications. Meanwhile, recent advances in open-world detection have introduced open-set and open-vocabulary algorithms in monocular 2D and 3D settings, yet stereo-based open-set detection remains largely unexplored. To bridge this gap, we propose DDStereo, a novel Dual-Decoder Stereo Transformer for real-time open-set 3D object detection. DDStereo features two lightweight decoder branches: one for open-set foreground 2D detection and the other for 3D attribute regression. These decoders share object-level queries to achieve unified target-level alignment. To enhance inference efficiency, we designed a compact disparity feature extractor and a streamlined decoder architecture. Experiments on public stereo 3D benchmarks demonstrate that DDStereo achieves state-of-the-art accuracy under both closed-set and open-set protocols. Notably, our method surpasses existing stereo 3D detectors in inference speed and, for the first time, achieves real-time performance comparable to monocular approaches.

---


### 206. [High-Fidelity Synthetic Transmission Electron Microscopy Image Generation Using Diffusion Probabilistic Models for Data-Limited Semiconductor Metrology](https://arxiv.org/abs/2606.24817)

**<font color=#1a73e8>作者：</font>** Johannes Boehm, Bappaditya Dey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advanced semiconductor nodes drastically increased demand for Transmission Electron Microscopy (TEM), yet destructive sample preparation, slow imaging and high costs severely limit the availability of diverse datasets needed for downstream machine learning (ML). Synthetic data generation is becoming essential, but current generative models often miss TEM-specific noise, structural detail, and stochastic variability crucial for evaluation. We present a Denoising Diffusion Probabilistic Model (DDPM) framework for synthetic TEM image generation under extreme data scarcity. A progressive patch-based training strategy scales from low-resolution patches to full images, enabling from-scratch training with only 15 samples. We integrate a custom TrivialAugment adaptation, cross-process domain transfer, classifier guidance, and RePaint-style inpainting, culminating in full-image generation that preserves global structural and spatial relationships in compliance with FAB metrology requirements. Beyond synthesis, we repurpose DDPM feature representations for segmentation, partitioning encoder feature maps to obtain coherent region masks. Our synthetic images achieve up to MS-SSIM > 0.98 and qualitative expert assessment consistent with structural similarity results, facilitating downstream ML training for defect detection, segmentation, and metrology while preserving statistical and physical realism.

---


### 207. [Solving Inverse Problems of Chaotic Systems with Bidirectional Conditional Flow Matching](https://arxiv.org/abs/2606.24824)

**<font color=#1a73e8>作者：</font>** Peiyan Hu, Jian Zhang, Jiashu Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling chaotic systems is crucial yet challenging. Inverse problems in chaotic dynamics, namely inferring initial conditions from final states, remain largely unsolved because of ill-posedness, non-uniqueness, instability, and potentially chaotic time-reverse dynamics. We address this open problem with Bidirectional Conditional Flow Matching (Bi-CFM), which learns bidirectional mappings between distributions of initial and final states to capture the stochasticity of chaotic evolution and mitigate exponential error accumulation over time. Furthermore, for systems with conservation laws, we extend it to Conservation-constrained Bi-CFM (CBi-CFM). Across the classic Lorenz, Circuit, and high-dimensional Lorenz 96 systems, Bi-CFM improves five distribution-level metrics over baselines while achieving a speedup of more than two orders of magnitude. In the three-body planet-planet scattering problem in planetary dynamics, CBi-CFM better respects conservation laws, with conservation errors comparable to those of the ground truth. Finally, on real observations of globular clusters, collisional million-body systems shaped by $\sim 10^{10}$ years (10 Gyr) of evolution, our method represents an advance in accuracy, establishing a scalable route to solving inverse problems of long-timescale real-world chaotic dynamics.

---


### 208. [L3Cube-MahaPOS: A Marathi Part-of-Speech Tagging Dataset and BERT Models](https://arxiv.org/abs/2606.24825)

**<font color=#1a73e8>作者：</font>** Hariom Ingle, Ronit Ghode, Ishwari Gondkar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Part-of-Speech (POS) tagging is a foundational NLP task underpinning machine translation, information extraction, and syntactic parsing. Despite Marathi being spoken by over 83 million people and ranking among the top twenty most spoken languages worldwide, it remains severely under-resourced in annotated corpora and standardised evaluation benchmarks. Marathi presents unique challenges for computational modelling owing to its rich morphology, relatively free word order, lack of capitalisation conventions, and pervasive code-mixing with Hindi and English. We introduce L3Cube-MahaPOS, a gold-standard POS tagging dataset for Marathi comprising 32,354 manually annotated sentences drawn from news text. Annotation was performed entirely manually by a team of Marathi-proficient annotators following a 16-tag Universal Dependencies-aligned scheme. A structured preprocessing pipeline covering Unicode normalisation, Devanagari-aware tokenisation, and noise filtering ensures label consistency across all splits. We benchmark the dataset across six model families spanning HMM, CRF, BiLSTM, BiLSTM+CharCNN, MuRIL, and the Marathi-specific transformer MahaBERT-v2. The best system achieves 88.67\% token-level accuracy and a macro-F1 of 81.67% over 15 evaluated tag classes. We release the dataset, annotation guidelines, and trained model checkpoints to foster further research in Marathi NLP.

---


### 209. [Virtual Simulation for Mental Health](https://arxiv.org/abs/2606.24826)

**<font color=#1a73e8>作者：</font>** Anna Fang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Poorly designed interventions or those deployed without adequate safeguards can harm the communities they aim to serve, thus exacerbating existing vulnerabilities and leaving individuals unsupported. This is especially the case for the mental health context, where there is a growing trend of relying on technological interventions due to their accessibility and ability to deliver large-scale support. However, the mental health context is also particularly sensitive to change and risks of failure are dire; at their worst, failures in mental health interventions can result in lasting negative outcomes for individuals and tragic losses as people fall through the cracks. Thus, enabling safe ways to experiment in the mental health context is vital to allow both individuals and communities to engage with new interventions without risk of their real-world consequences. Virtual simulation, which uses virtual environments to replicate real-world interactions, processes, and behaviors, offers a promising opportunity for enabling safe, controlled experimentation with its ability to accurately replicate social situations, fears, stressors, and the potential outcomes of specific interactions. This work explores how simulation approaches can support emerging mental health processes through (1) evaluating community-level outcomes using agent-based modeling and (2) individual training in the mental health context through embodied, controlled spaces. I demonstrate this use of virtual simulation systems through a grounded human-centered approach, where system design is guided by empirical understanding of current real-world needs and challenges. By leveraging simulation to create environments where mental health strategies can be safely tested and practiced, this work aims to open new possibilities for designing scalable, user-centered systems that are effective and safe.

---


### 210. [Less is More: Quality-Aware Training Data Selection for Scientific Summarization](https://arxiv.org/abs/2606.24828)

**<font color=#1a73e8>作者：</font>** Maria Nefeli Paraskevopoulou, Tatiana Passali, Grigorios Tsoumakas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific long-document summarization datasets commonly treat author-written abstracts as gold reference summaries, although their quality and alignment with the source article vary. At the same time, publicly available scientific summarization datasets remain limited in scale and structure for modern long-context models. In this work, we address both challenges by a) constructing and releasing one of the largest biomedical and life science datasets for long-document summarization, containing 1.88 million PMC articles, and b) analyzing the reference quality of author-written abstracts with source-grounded and model-based metrics. We show that author-written abstracts vary in their alignment with the full article and that these quality signals can guide training-data selection. Training on selected high-quality subsets outperforms random sampling at matched training sizes and can match or exceed larger random subsets on factuality-oriented metrics. Our findings suggest that reference quality is an important factor in scientific summarization and that quality-aware data selection can improve training efficiency.

---


### 211. [GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction](https://arxiv.org/abs/2606.24829)

**<font color=#1a73e8>作者：</font>** Chenrui Fan, Paolo Favaro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-prompted text-to-video (T2V) models are increasingly used to synthesize virtual camera captures, such as orbiting objects or moving through static scenes. For these outputs, visual plausibility is insufficient: the generated frames should also provide coherent multi-view evidence for a single static 3D scene. We introduce GeoT2V-Bench, a reconstruction-based diagnostic benchmark for evaluating whether camera-prompted T2V clips can support explicit rigid 3D reconstruction. Our pipeline estimates per-frame camera intrinsics and poses with VGGT-style geometry estimation, fits DeformableGS, derives a static MedianGS proxy by temporal-median aggregation, and renders this proxy along the estimated camera path. Instead of producing a pass/fail label or a single scalar score, GeoT2V-Bench reports a continuous reconstruction profile covering apparent image motion, estimated trajectory behavior, MedianGS static rendering error, static-render flow agreement, and the gap between flexible and static fits. On a fair-format four-seed evaluation with 3,840 completed reconstructions from 12 open-weight model configurations and 80 GeCo-Eval static-scene prompts, we find that visible motion, static rendering error, flow agreement, and flexible-vs-static behavior often disagree. GeoT2V-Bench therefore captures complementary failure modes that emerge when generated videos are tested as global static-scene acquisitions.

---


### 212. [Difference-Making without Making a Difference](https://arxiv.org/abs/2606.24832)

**<font color=#1a73e8>作者：</font>** Sander Beckers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over a series of seven papers, Andreas & Günther have introduced seven definitions of actual causation and have classified them as belonging to three different, competing, types of accounts: factual difference-making, counterfactual difference-making, and regularity-based. I show that their most recent - factual difference-making - definition instantiates all three types, thereby proving that these are distinctions without a difference. I further compare their novel account to the other six accounts on several crucial examples, revealing that this undermines all seven of their accounts.

---


### 213. [Bridging the Manifold Gap: Riemannian Residual Line Search for One-Step Image Editing](https://arxiv.org/abs/2606.24844)

**<font color=#1a73e8>作者：</font>** Hongzhu Yi, Zhongtian Luo, Tong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step diffusion editors are fast because they avoid inversion and iterative optimization, but a single transport update must be aggressive enough to realize the target prompt and conservative enough to preserve the source image--and no fixed update strength satisfies both demands across edit types. We treat this tension as a post-hoc candidate-selection problem on top of energy-field transport rather than as a new editing model. Our proposed method, Riemannian Residual Line Search, first builds a stronger edit by estimating the local time curvature of the prompt-delta field and projecting the corrected direction back onto the update norm of the original first-order energy-field transport estimation. It then forms a small residual path from the source image to this strong edit, retains the original first-order output as one candidate, and picks the final image by maximizing target-prompt CLIP alignment. On a 700-sample PIE-Bench++ evaluation across 10 edit type IDs, our method achieves state-of-the-art (SOTA) performance among current one-step update algorithms.

---


### 214. [Spherical-to-ERP Epipolar Rectification for Single-Axis Disparity in 360 Stereo](https://arxiv.org/abs/2606.24847)

**<font color=#1a73e8>作者：</font>** Sahereh Obeidavi, Dieter Landes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional stereo images provide full-surround perception but violate the geometric assumptions of classical disparity estimation: in spherical or fisheye views, epipolar correspondences follow curved great-circle paths, producing two-dimensional displacements that cannot be treated as single-axis disparity before geometric rectification. In this work, we adopt a standard spherical-to-equirectangular (ERP) projection as a preprocessing step, which straightens epipolar curves and restores a one-dimensional disparity structure - horizontal for left-right rigs and vertical for top-bottom rigs. Building on our previously introduced RAFT + Epipolar-Aligned Channel Selection (EACS) framework, originally developed for rectilinear and ERP stereo, we examine whether the same modular pipeline remains accurate when the input originates from spherical stereo imagery. After ERP projection, dense optical flow from RAFT is reduced to disparity by retaining only the baseline-aligned flow component. Experiments on synthetic fisheye stereo datasets show that this spherical-to-ERP-to-RAFT+EACS pipeline produces accurate, smooth, and structurally consistent disparity maps at real-time speed. These findings confirm that established ERP preprocessing can be effectively combined with our earlier RAFT+EACS method to enable practical, interpretable, and efficient disparity estimation from spherical stereo, providing a straightforward pathway for extending conventional stereo pipelines to 360 imaging.

---


### 215. [Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment](https://arxiv.org/abs/2606.24851)

**<font color=#1a73e8>作者：</font>** Jason Sulskis, Sathya Ravi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier Neural Operators (FNO) learn solution operators of partial differential equations by parameterizing global convolutions in the complex Fourier domain. For real-valued PDE solutions, the complex FFT carries representational redundancy through conjugate symmetry. We introduce the Hartley Neural Operator (HNO), the exact real-valued mirror of FNO: it replaces the FFT with the purely real Discrete Hartley Transform and learns a single real multiplier per retained spectral mode, with no complex arithmetic. Because the real Hartley spectrum is not halved by conjugate symmetry, HNO retains twice as many frequency corners as FNO but one real weight where FNO carries a complex pair, so the two operators are iso-parametric at equal width and differ only in spectral basis. Our central thesis is that the best basis is a property of the operator. Self-adjoint elliptic operators (Poisson, biharmonic) have real, symmetric Green's functions that the real Hartley multiplier diagonalizes exactly, and HNO is favored there. Time-dependent operators carry phase, from oscillation in the wave equation to transport in advection, Burgers, and Navier-Stokes, which a real diagonal multiplier cannot represent, so FNO is favored there, and increasingly so with the operator's phase content, leaving the phaseless heat equation as the borderline case. Training both operators identically and benchmarking across PDE classes, initial-condition families, and boundary conditions, we find an elliptic-versus-time-dependent split that is monotone in operator phase content and matches the Green's-function theory we develop. Rather than a universal winner, our findings give a predictive rule: match the spectral basis to the symmetry of the solution operator.

---


### 216. [It's Complicated: On the Design and Evaluation of AI-Powered AAC Interfaces](https://arxiv.org/abs/2606.24854)

**<font color=#1a73e8>作者：</font>** Blade Frisch, Will Wade, Dylan Gaines 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) can enhance what people who use augmentative and alternative communication (AAC) are able to do with their systems. However, evaluating AI-powered AAC interfaces can be difficult. People are intersectional beings and current evaluation metrics can struggle to capture the multifaceted and nuanced desires people may have for their AAC. We explore the complicated nature of six AAC problem spaces, explore how AI might be used in these spaces, and suggest more robust methods of evaluation that take the intersectional nuances of people into account. We also discuss broader issues that arise across these problem spaces and how they could be addressed using our proposed evaluation methods.

---


### 217. [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874)

**<font color=#1a73e8>作者：</font>** Haorui Ji, Weizhe Liu, Hongdong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse voxel representation has emerged as a scalable foundation for image-to-3D Gaussian Splatting (3DGS) generation, yet current methods struggle to preserve high-frequency visual details of input images due to two structural bottlenecks. First, they adopt discriminative 2D features optimized for semantic abstraction to construct sparse voxel latents, which suppress reconstructive cues and induce a representation bottleneck. Second, in the generation stage, standard diffusion transformers lack effective mechanisms to align dense 2D image tokens with sparse 3D voxel latents, resulting in a cross-modal correspondence bottleneck. To address these issues, we propose FLUX3D, a scalable image-to-3DGS framework that boosts both representation learning and cross-modal alignment during generation. We first revisit 2D feature selection for sparse-voxel-based 3D representation learning, propose Diffusion-Aligned Structured Latents (DA-SLAT) and couple it with a decoder-only architecture to improve 3DGS reconstruction fidelity. We also design a sparse-structure-aware diffusion framework, which integrates the Sparse-structure Multimodal Diffusion Transformer (SMDiT) and Modal-Aware Rotary Positional Embedding (MARoPE) to achieve geometry-agnostic 2D-3D alignment. Extensive benchmark experiments demonstrate that FLUX3D yields substantial improvements in appearance fidelity and significantly outperforms all state-of-the-art (SOTA) methods in generating high-quality 3DGS assets.

---


### 218. [FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876)

**<font color=#1a73e8>作者：</font>** Orest Kupyn, Goutam Bhat, Philipp Henzler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating explorable 3D scenes from a single image requires strong generative priors and accurate geometric representations suitable for downstream use. Current video diffusion models offer high-quality generation and implicitly encode multi-view geometric structure in latent space. However, existing feedforward latent scene decoders typically output volumetric 3D Gaussians that lack a well-defined surface, limiting their use in simulation or standard graphics pipelines. This motivates decoding surface-aligned primitives that are not only renderable but also closer to explicit geometric assets. We ask whether compressed video diffusion latents can be mapped directly to explicit surface primitives in a single pass. To this end, we introduce FLAT and, for the first time, show that triangle splats can be decoded directly from video diffusion latents. Compared with decoding 3D Gaussians, predicting flat primitives is notoriously more challenging due to high sensitivity to primitive orientations, oftentimes leading to poor gradient flow. FLAT solves with two key ingredients: a ray-centered rotation parameterization for triangle regression and a novel product window function that improves gradient flow during differentiable triangle rendering. On standard benchmarks, FLAT achieves significantly better geometric accuracy while maintaining competitive visual quality compared to state-of-the-art feedforward baselines. We further show that a lightweight test-time refinement step converts the predicted triangle soup into a fully opaque, game-engine-ready representation that supports real-time rendering. By evaluating 3DGS, 2DGS, and triangle splatting variants under an identical training setup, we provide the first systematic analysis of representation tradeoffs in feedforward scene generation. The project page is available at this https URL

---


### 219. [DiffusionBench: On Holistic Evaluation of Diffusion Transformers](https://arxiv.org/abs/2606.24888)

**<font color=#1a73e8>作者：</font>** Xingjian Leng, Jaskirat Singh, Zhanhao Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformer (DiT) research on image generation has converged to a single evaluation setup: class-conditional generation on ImageNet. While methods improve the FID and related metrics, it is increasingly unclear whether they reflect real progress in generative modeling. The natural alternative, i.e., text-to-image (T2I) generation, is perceived as too costly or inconvenient to train and evaluate and is often skipped. We argue that this perception no longer holds. We introduce NanoGen, a unified DiT training and evaluation framework. NanoGen matches state-of-the-art DiT baselines on ImageNet and, with 12 lines of configuration change, also trains competitive text-to-image models. It currently supports RAE, VAE, pixel-space, and MeanFlow diffusion methods under both ImageNet and T2I setups. Under NanoGen, training T2I requires comparable compute to ImageNet. After training 21 latent diffusion models with NanoGen, we observe that method ranking shows no strong correlation between ImageNet and T2I generation: Pearson correlation is between -0.377 and -0.580 across three metrics. This suggests that a method which improves class-conditional ImageNet FID may show no corresponding improvement on T2I, clearly indicating the necessity of evaluating DiTs on both tasks. To this end, we summarize ImageNet and text-to-image results, which yields DiffusionBench, a holistic benchmark for DiT research. We recommend reporting DiffusionBench in place of ImageNet alone: methods that improve DiffusionBench are more likely to reflect broader progress.

---


> [!TIP]
> 当前位于：**201-219**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-219**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
