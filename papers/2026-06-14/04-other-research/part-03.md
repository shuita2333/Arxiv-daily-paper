# 📦 其他研究 | 2026年06月14日

> 本类共 **251** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

---

### 101. [A Mathematical Forum Platform for Collaborative Problem Solving and Dataset Generation for AI Reasoning](https://arxiv.org/abs/2606.12976)

**<font color=#1a73e8>作者：</font>** Akbar Erkinov, Nurmukhammad Abdurasulov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sharing mathematical content in online forums remains a significant friction point for students and educators: writing raw LATEX is error-prone, standalone optical character recognition tools require platform switching, and current forum software offers no integrated path from a photograph of a formula to a rendered post. We present a unified system that eliminates this friction by embedding an image to LATEX conversion pipeline directly inside a forum posting interface. A user uploads or captures an image of a mathematical expression; the system routes it through the Mathpix OCR API, detects whether the returned output is LATEX or plain text containing inline math, applies the appropriate delimiter normalisation, and renders a live preview in either LATEX or Markdown mode before the post is committed to the database. The architecture is organized in three loosely coupled layers: image processing, rendering, and storage, and supports both desktop and mobile clients. A provisional US patent application has been filed covering the core methods. We describe the full system design, each component in detail, the data schema, and the key technical innovations, and we position the work against existing standalone tools and forum platforms to demonstrate the practical gap it closes. Beyond immediate usability, we argue that a deployed platform of this kind constitutes a continuously growing, community-validated dataset of mathematical problems and step-by-step solutions, a resource that can be used to train and benchmark AI systems for accurate mathematical reasoning

---


### 102. [Efficient, Robust, and Anti-Collusion Fingerprinting of Image Diffusion Models](https://arxiv.org/abs/2606.12977)

**<font color=#1a73e8>作者：</font>** Jianwei Fei, Yunshu Dai, Zhihua Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model fingerprinting, embedding user-specific identifiers (fingerprints) into generated outputs, has recently emerged as a popular solution to protect the intellectual property rights (IPR) of generative text-to-image (T2I) models and prevent unauthorized redistribution. In this work, we reveal a previously unexplored systematic vulnerability in existing generative model fingerprinting methods: they lack robustness against collusion attacks, where multiple attackers combine their models to remove or obscure the fingerprints. To address this issue, we take the first step towards a robust fingerprinting method for T2I models with anti-collusion capabilities. The proposed method encodes strings of bits, namely fingerprints, into the coefficients of a personalized normalization module (PNM) incorporated into T2I models, so that fingerprints can be reliably recovered from any generated image. To defend against collusion attacks and prevent unauthorized model redistribution, we introduce an anti-collusion mechanism based on lossless function-invariant parameter transformations. This mechanism significantly degrades the image generation quality of colluded models, making them effectively unusable. Moreover, our method allows developers to efficiently create multiple copies of fingerprinted T2I models by reparameterizing the PNM without the need for retraining. We also introduce a worst-case optimization strategy to improve robustness against model-level attacks. Our experiments demonstrate that the proposed method achieves high fidelity and robustness across multiple T2I image generation and editing tasks, with fingerprint extraction accuracy exceeding 99.5%. Compared with existing methods, our method demonstrates, for the first time, a notable proactive robustness to collusion attacks by significantly increasing the FID of colluded models.

---


### 103. [Camera and LiDAR BEV Fusion for Cooperative 3D Object Detection on TUMTraf V2X](https://arxiv.org/abs/2606.12981)

**<font color=#1a73e8>作者：</font>** Muhammad Shahbaz, Shaurya Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe a Camera and LiDAR fusion detector developed for the TUMTraf V2X cooperative 3D object detection track of the DriveX 2026 challenge. The detector fuses three roadside cameras with a fused infrastructure-plus-vehicle point cloud in a shared bird's-eye-view space and predicts boxes through a CenterPoint-style head with a generalized IoU regression loss and an IoU quality re-ranking head. Trained on the provided train and validation splits, the model reaches a 3D mAP of 0.85 on the public Codabench test split. While iterating on the system, we observed that 44 of the 50 test frames are also present in the released train (40) and validation (4) splits with their labels. We therefore conducted two additional studies to quantify how this overlap affects the final score: (1) a finetuning run that oversamples the 44 overlapping frames, reaching 0.89 mAP, and (2) a post-processing run that replaces predictions on those frames with the released ground truth, reaching 0.99 mAP (uploaded to our Codabench account for testing but not published on the leaderboard). All three configurations and their per-class results are reported.

---


### 104. [SkillChain: Closing the Loop on Skill Evolution for Image-Based E-Commerce AI Assistants](https://arxiv.org/abs/2606.12984)

**<font color=#1a73e8>作者：</font>** Yimin Hu, Mengtao Xu, Hao Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Image-based AI assistants are now deployed at production scale on e-commerce platforms, where a single uploaded image can trigger fundamentally different user intents: product search, style recommendation, visual encyclopedia, or utility tool calls, each demanding its own response format, tool invocation, and domain knowledge. Without per-intent behavioral constraints, LLM-based systems conflate these heterogeneous modes and fall short of domain quality standards, while the breadth and dynamism of the intent space render manual engineering infeasible. To address this, we present SkillChain, which closes the production feedback loop on Skill evolution, automating the lifecycle of Skills through three stages: Skill Creator for bootstrapping from task specs and trajectories, Route Optimizer for routing alignment, and Body Refiner for iterative Skill Body refinement via dual-path LLM-Judge evaluation. Deployed on a production-scale e-commerce image assistant, SkillChain substantially improves aggregate response quality, with the strongest gains on structural compliance and content quality; a one-week online A/B experiment further confirms significant gains in user engagement, content consumption, and long-term retention.

---


### 105. [Objects Before Words: Object-First Inductive Biases for Grounding Language in Child-View Video](https://arxiv.org/abs/2606.12985)

**<font color=#1a73e8>作者：</font>** Sathira Silva, Abrham Kahsay Gebreselasie, Muhammad Umer Sheikh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning grounded word meaning from natural experience requires resolving two ambiguities in infant-view recordings: when the named referent appears and where it is in a cluttered frame. In SAYCam-style data, caregiver speech is sparse and weakly synchronized with egocentric video, so single-frame contrastive pairing yields noisy positives in which the intended object is absent or entangled with distractors. We propose BabyMind, an object-first bias for child-view contrastive learning under sparse, noisy supervision. BabyMind extracts candidate object embeddings using an offline mask-based region interface, links candidates across a short utterance-centered window into lightweight object files via tracking, and aligns utterances to bags of object files with a prototype-space multiple-instance contrastive objective. Track-coherence and global-object agreement regularizers stabilize learning and transfer object-file structure into the global frame embedding used at evaluation. On SAYCam-S, BabyMind improves Labeled-S 15 forced-choice accuracy by +2.6 points over CVCL and yields consistent gains on in-vocabulary out-of-distribution benchmarks. Code is available at this https URL.

---


### 106. [Diffusion Transformer World-Action Model for AV Scene Prediction](https://arxiv.org/abs/2606.12987)

**<font color=#1a73e8>作者：</font>** Ruslan Sharifullin, Benjamin Jiang, Kai Xi Chew  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models let an autonomous vehicle predict future camera scenes from its own planned controls, enabling planning and simulation without real-world rollouts, but at compact, trainable scale the futures are ambiguous and the field's standard distortion metrics actively mislead: they reward a blurry regression mean over a realistic prediction. We confront this with a compact latent world model that, given the present front-camera latent and a sequence of ego-actions, predicts future scene latents a frozen decoder renders to $256 \times 256$ frames up to 8 seconds ahead, evaluated on 150 held-out nuScenes scenes. We first benchmark where to predict: across six frozen encoders spanning four representation families, V-JEPA2 with temporal context reduces steering RMSE by 40% over the best single-frame encoder. We then train a latent Diffusion Transformer (DiT) and, through a controlled diagnosis, identify the four ingredients it needs: spatial tokens, the $x_0$ objective, residual anchoring, and sampling matched to target uncertainty. In a Stable-Diffusion-VAE encode-predict-decode pipeline we expose the central tension: distortion metrics (cosine similarity, SSIM) favor the blurry mean, masking that the diffusion model is far closer to the real frame distribution. Inception-based FID and KID reveal a clean perception-distortion frontier: diffusion attains KID 0.078 versus 0.375 for regression ($4.8\times$ better), and a deployable train-derived calibration makes this practical without test-time ground truth. The model is genuinely action-controllable (steering drives scene displacement, Spearman $\rho = 0.81$, vs $-0.18$ for regression). We trace limited single-pass motion to a shared-present anchor and engineer a compact 1.7M-parameter "jump" model that recovers full ground-truth motion magnitude ($1.02\times$ GT), where single-pass models capture less than half.

---


### 107. [A Machine Learning Framework for Real-Time Personalized Ergonomic Pose Analysis](https://arxiv.org/abs/2606.12988)

**<font color=#1a73e8>作者：</font>** Manex Atxa, Bruno Simoes, Julen Balzategui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a new methodology for real-time prediction of ergonomic and non-ergonomic human poses using volumetric video data in three dimensions. Although the methodology was designed for ergonomic assessments, it can be adapted to other applications requiring real-time analysis of human posture. One aspect that makes this system stand out is its ability to analyze 3D point clouds during the assessment, enabling computation from multiple angles. This overcomes a critical limitation of cameras which provide often a fixed viewpoint, thereby restricting the data available for a thorough postural evaluation, especially when occlusions occur. The system continuously and automatically performs pose inference using the chosen perspective on the real-time streaming data; however, only the poses manually selected and labeled by the user are used to train the personalized deep learning classifier. The methodology has been refined through a case study in which RGB-D cameras captured subjects performing load-lifting tasks, enabling real-time skeletal labeling. The model was trained on this data and, following the training phase, performs inference on new streaming data in real time. This research offers a scalable and pragmatic approach for real-time ergonomic evaluation by combining state-of-the-art 3D data technologies and traditional 2D pose estimation algorithms. It addresses the increasing need for safety and health monitoring in workplace environments, marking a notable contribution to the domain.

---


### 108. [Exposure Bias as Epistemic Underidentification in Recursive Forecasting](https://arxiv.org/abs/2606.12990)

**<font color=#1a73e8>作者：</font>** Riku Green, Zahraa S. Abdallah, Telmo M Silva Filho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive multi-step forecasting is usually framed as distribution shift: models are trained on observed histories but deployed on their own predictions. We show this framing is incomplete by proving that, under partial observability or state truncation, recursive rollout is also an epistemic underidentification problem. Even with deterministic latent dynamics, one-step Bayes supervision identifies behavior only on observed contexts and need not identify the deployed recursive predictor once rollout queries self-generated induced states whose correct local targets are not determined by numeric state alone. We formalize this with induced states $Z$ and provenance variables $P$, and derive a decomposition of induced-state error into teacher-forcing/rollout mismatch, representation--class approximation, and provenance information gaps. Empirically, we show that rollout enters a distinct induced-state regime, that fixed induced states define a distinct local corrective task, and that closed-loop gains arise not only from local adaptation but also from changing the induced states visited during rollout. Using a simple binary provenance encoding, provenance-aware correction can further improve performance, though gains are conditional rather than uniform. These results recast exposure bias as reasoning under self-induced epistemic uncertainty.

---


### 109. [APCyc: Property-Informed Design of Cyclic Peptides via Automated Cyclization](https://arxiv.org/abs/2606.12991)

**<font color=#1a73e8>作者：</font>** Yifan Zhao, Lang Qin, Jintai Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyclic peptides represent a promising class of therapeutic compounds in modern drug discovery, often offering improved stability and binding affinity. However, the de novo design of cyclic peptides remains challenging because methods must identify pocket-adaptive cyclization patterns and linkage sites while simultaneously controlling drug-relevant properties. This challenge is particularly pronounced for recent generative models trained predominantly on linear peptide data, which may fail to capture cyclization-specific constraints. To address the limitation, we introduce APCyc, a target-aware de novo cyclic peptide generation framework that explicitly models cyclization and jointly optimizes multiple essential physicochemical properties. By using an expanded residue vocabulary and explicitly encoding cyclization-site and linkage-type information, APCyc learns cyclization-aware representations and leverages Bayesian posterior guidance to steer sampling toward cyclic peptides satisfying multiple property objectives. Experimental results demonstrate that our model learns target-dependent cyclization preferences, and enables effective and controllable multi-property optimization for cyclic peptide design. The source code of this paper is available at this https URL.

---


### 110. [Reliability of Probabilistic Emulation of Physical Systems](https://arxiv.org/abs/2606.12997)

**<font color=#1a73e8>作者：</font>** Sam F. Greenbury, Radka Jersakova, Paolo Conti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two dominant approaches have emerged for generating probabilistic forecasts of physical systems: generative models, such as diffusion or flow matching; and ensembles of deterministic models with stochasticity injected, trained using the continuous ranked probability score (CRPS) loss. While both approaches have demonstrated strong predictive accuracy, the reliability of their uncertainties has not been systematically assessed. We address this gap by developing a framework to evaluate both approaches across diverse 2D spatiotemporal physical systems, under matched model size and computational budget. We assess the reliability of probabilistic emulation by inspecting the empirical coverage of predictive intervals, while also considering accuracy and computational efficiency metrics. CRPS-trained ensembles typically achieve more reliable uncertainties on both single-step prediction and autoregressive rollouts, demonstrating better coverage than the standard alternative of training generative models in a latent space. Moreover, the CRPS approach offers significantly faster inference. When generative models are trained in ambient rather than a compressed latent space, which is often infeasible for high-dimensional problems, they exhibit comparable coverage to CRPS-trained ensembles, though with substantially larger inference latency. In contrast, when CRPS-trained ensembles are trained in latent space they do not show a marked degradation in coverage with respect to ambient space. Both generative models and CRPS-trained ensembles demonstrate good predictive accuracy. To facilitate future research and application, we release AutoCast, a modular framework implementing both generative models and CRPS-trained ensembles, alongside AutoSim, a flexible dataset generation package for rapid prototyping.

---


### 111. [SoK: The Constant Time Model](https://arxiv.org/abs/2606.13000)

**<font color=#1a73e8>作者：</font>** Billy Bob Brumley  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Constant time programming patterns is the primary defense against timing attacks on cryptographic implementations, yet what "constant time" means varies across academia and industry. This work systematizes constant time models and their evolution, identifies a recurring gap between what models protect and what specifications assume, and distills an offensive methodology for discovering timing vulnerabilities that originate outside the cryptographic primitive boundary. Applying this methodology, we locate a specification-level vulnerability related to private key loading, and confirm the leak in both OpenSSL and BoringSSL. Counterintuitively, BoringSSL's per-observation signal is several orders of magnitude stronger than OpenSSL's, despite an explicitly stricter threat model.

---


### 112. [The Illusion of Multi-Agent Advantage](https://arxiv.org/abs/2606.13003)

**<font color=#1a73e8>作者：</font>** Prathyusha Jwalapuram, Hehai Lin, Chuyuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prevailing wisdom posits that Multi-Agent Systems (MAS) are superior to Single-Agent Systems (SAS), citing advantages like context protection, parallel processing and distributed decision-making. However, empirical support for this claim relies primarily on comparisons with SAS baselines using benchmarks that prioritize isolated reasoning tasks, which do not adequately assess these advantages. Focusing on automatically generated MAS that are designed for enhanced generalizability over manually-designed counterparts, we perform a rigorous, systematic evaluation against SAS, specifically Chain-of-Thought with Self-Consistency (CoT-SC). Across traditional reasoning datasets and tasks with interactive multi-step workflows (e.g., BrowseComp-Plus), we demonstrate that automatic MAS consistently underperform CoT-SC despite being up to 10x more expensive. To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization potential. We show that expert-architected MAS consistently outperforms automatically generated architectures in both raw performance and cost-efficiency on this dataset, demonstrating that existing evaluation frameworks mask critical architectural gaps and inefficiencies of complex MAS by failing to account for the marginal utility of increased computational cost. Critically, systematic deconstruction of the generated MAS architectures reveals that current automated design paradigms produce architectural bloat that prioritizes superficial complexity which does not translate into functional utility, exposing a fundamental misalignment with multi-agent principles.

---


### 113. [Otters++: A Time-to-first-spike Based Energy Efficient Optical Spiking Transformer](https://arxiv.org/abs/2606.13016)

**<font color=#1a73e8>作者：</font>** Zhanglu Yan, Jiayi Mao, Kaiwen Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) are promising for energy-efficient inference, and time-to-first-spike (TTFS) coding is especially attractive because each neuron fires at most once. In practice, however, this benefit is often reduced by the cost of computing a temporal decay term and multiplying it by the synaptic weight. We address this issue by turning a physical hardware "bug," the natural signal decay in optoelectronic devices, into the main computation of TTFS, named Otters++. Specifically, we use the measured decay of a custom In$_2$O$_3$ optoelectronic synapse to directly realize the TTFS temporal term, removing the need for explicit digital decay computation. To scale this idea to Transformer models, we establish a layer-wise functional equivalence between the Otters++ and a quantized neural network (QNN), and develop a hybrid training method that uses device-faithful SNN computation in the forward pass and QNN straight-through gradients through the equivalent QNN path in the backward pass, together with model distillation. This avoids differentiation through discrete first-spike events and reduces the over-sparsity problem in direct TTFS-SNN training. We further make training aware of measured device noise by sampling run-to-run variation, and refine the system-level energy model by accounting for device sharing and multi-hop communication. On GLUE dataset, Otters++ improves the average score to 84.17\% while maintaining a clear energy advantage over prior spiking Transformer baselines. These results show that physically grounded TTFS computing can be efficient, trainable, and robust under realistic hardware effects.

---


### 114. [Quality-Preserving Imperceptible Adversarial Attack on Skeleton-based Human Action Recognition](https://arxiv.org/abs/2606.13022)

**<font color=#1a73e8>作者：</font>** Ziyi Chang, Kanglei Zhou, Xiaohui Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on skeletal human action recognition have received significant attention. However, existing methods typically introduce noise-like perturbations that degrade motion quality post-attack, and thereby are inherently perceptible with recent advancements in S-HAR systems. We discover that this degradation stems from the gap between empirical and true risks during the optimization process of previous adversarial attacks. To address this issue, we propose an attack where adversarial motions are obtained without compromising their motion quality. To minimize the risk gap and preserve motion quality, we propose a distribution-based adversarial attack method without introducing noise-like perturbations. To faithfully evaluate the motion quality, we propose a new metric that aligns with human perception on real-world naturalness. Experiments have been conducted on the state-of-the-art S-HAR methods across two datasets, demonstrating the superiority of our method in both the attack success rate and the post-attack motion quality through qualitative and quantitative analyses. The success of our quality-preserving attack application and distribution-based method raises serious concerns about the robustness of action recognizers, highlighting the need for further enhancements in this domain.

---


### 115. [A Multi-Modal Framework with Cross-Subject Pseudo-Labeling and Semantic Alignment for Micro-Gesture Recognition](https://arxiv.org/abs/2606.13030)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Haokun Zhang, Pengyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-gestures (MGs) are spontaneous and subtle body movements that frequently convey hidden human emotions. Recognizing MGs in untrimmed videos remains highly challenging due to their extremely low signal-to-noise ratio, severe long-tailed class distribution, and the inherent domain shift encountered in cross-subject evaluation scenarios. In this paper, we propose a comprehensive multi-modal framework for Track 1 of the 4th MiGA-IJCAI Challenge. To capture fine-grained representations, we design a saliency-guided multi-modal extraction pipeline integrating 68-keypoint skeleton joint coordinates, 3D heatmap volumes, and high-resolution RGB visual features. We introduce a gentle square-root smoothed weighting mechanism paired with an Orthogonal Semantic Embedding Loss to protect tail classes without compromising overall recognition capabilities. More importantly, to bridge the cross-subject generalization gap, we propose a Cross-Modal Pseudo-Labeling (CMPL) strategy for unsupervised domain adaptation, which significantly boosts single-modal robustness. A temperature-scaled soft-voting mechanism is finally utilized to alleviate overconfidence during late fusion. Extensive experiments demonstrate that our framework achieves a competitive F1-score of 68.13\%, securing the 4th place.

---


### 116. [GeoCFNet: Geometry-Aware Confidence Field Network for Robot-Assisted Endoscopic Submucosal Dissection](https://arxiv.org/abs/2606.13032)

**<font color=#1a73e8>作者：</font>** Rui Tang, Guankun Wang, Long Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advanced surgical robotics has made robot-assisted endoscopic submucosal dissection (ESD) a promising approach for the en-bloc resection of large lesions, with the potential to reduce recurrence and improve long-term outcomes. However, the technical complexity and risk of complications in ESD demand stable and precise visual guidance to maintain an accurate dissection corridor and a safe tissue margin. Dense confidence fields provide an effective representation for this purpose by describing both the preferred dissection region and its spatial transition to surrounding tissue. However, reliable confidence field estimation remains challenging in dynamic endoscopic scenes due to smoke, specular highlights, tissue deformation, weak texture, and the thin geometric structure of the target region. To address these challenges, we formulate dissection guidance as a geometry-aware confidence field estimation problem and propose GeoCFNet, a geometry-aware confidence field network built on a pretrained DINOv3 backbone. GeoCFNet integrates a Token-Differentiated Fusion module to aggregate class-token context with dense patch representations, a SegFormer decoder for confidence regression, and Geometry-Aware Spatial Regularization (GASR) to preserve spatial coherence and local geometric transitions. Experimental results show that GeoCFNet achieves RMSE 0.0480, PSNR 27.1995, SSIM 0.3397, and CC 0.2466, indicating accurate and geometrically stable confidence field estimation for robot-assisted ESD guidance.

---


### 117. [SAM-Deep-EIoU: Selective Mask Propagation for Multi-Object Tracking](https://arxiv.org/abs/2606.13033)

**<font color=#1a73e8>作者：</font>** Alexander Holmberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking has a heavy-tailed difficulty distribution: most frames are easy for a lightweight base tracker, while a small fraction are intrinsically hard. Video object segmentation (VOS) models can often preserve identity through the hard frames where the base tracker fails, but they are much more expensive in compute and memory. We propose selective mask propagation, a tracking algorithm that dispatches from a base tracker to a VOS model only on windows where an assignment-uncertainty signal fires. The base tracker's output is modified only when the VOS model makes a confident prediction that contradicts the base tracker's identity assignment; weak or inconclusive predictions preserve the base output. The method is training-free, treats both the base tracker and the VOS model as black boxes, and can benefit from replacing the VOS component with a more capable model. On DanceTrack, selective mask propagation improves three different base trackers. On SportsMOT, where identity preservation is central to sports analytics, SAM3-Deep-EIoU with global track association achieves state-of-the-art performance on the benchmark with 86.8 HOTA.

---


### 118. [DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities](https://arxiv.org/abs/2606.13037)

**<font color=#1a73e8>作者：</font>** Andrew Bao, Haochen Zeng, Peng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One-day vulnerabilities pose significant risks due to delayed or incomplete patch adoption. Generating proof-of-concept (PoC) inputs is therefore essential for assessing real-world impact. The key challenge is identifying necessary constraints for triggering the vulnerability and solving them effectively. Existing directed fuzzing approaches prioritize inputs toward target locations, but neither explicitly identify necessary constraints nor solve them effectively, relying instead on target-distance feedback and random mutation. Agentic approaches show strong potential through code reasoning and structured input generation, but goal drift in long-horizon reasoning limits their effectiveness.
DIG addresses this challenge by exploiting a key property of one-day vulnerabilities: patches often reveal necessary preconditions for triggering. DIG uses an LLM to analyze the patch and synthesize an oracle making these conditions explicit. The oracle supports effective PoC generation at two levels. At the high level, DIG performs oracle-guided generator evolution, where an agent infers and solves constraints to satisfy the oracle. At the low level, DIG instruments the oracle into the target program and uses branch-distance feedback to guide random mutation in directed fuzzing. Evaluation shows DIG outperforms 2 state-of-the-art agents and 10 fuzzers across 138 real-world CVEs. DIG triggers 80 vulnerabilities, surpassing prior results and outperforming the best baseline by 40% (57 vs. 80 CVEs). Notably, DIG exclusively triggers 9 vulnerabilities no existing technique can trigger. Compared to the average of other tools, DIG triggers vulnerabilities faster in 92.9% of cases, achieving over 100x speedup in 48.8% of cases, with a maximum speedup of 3,664x. Beyond one-day PoC generation, DIG uncovers 6 previously unknown vulnerabilities in widely deployed libraries, enabling zero-day discovery.

---


### 119. [SeamEdit: A Black-Box VLM-Agnostic Pipeline for Large-Image Semantic Editing](https://arxiv.org/abs/2606.13041)

**<font color=#1a73e8>作者：</font>** Xiangyu Lyu, Dan Lei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic region editing for large images must satisfy two requirements at the same time: high generative quality and natural integration with surrounding content. Some related methods rely on white-box models and leave the strong generation capability of closed-source models underexplored. Directly applying closed-source models to tiled editing, however, introduces several failure modes: semantic deformation, canvas-level alignment drift, and visible seam artifacts. This paper presents SeamEdit, a training-free and model-agnostic pipeline that treats any VLM with inpainting capability as a black-box oracle. SeamEdit mitigates these issues through a five-stage post-hoc pipeline: overlay-based tile decomposition, black-box VLM inpainting, geometric and color-consistency correction, seam-risk-based multi-candidate ranking, and dynamic-programming curved seam fusion. The pipeline reduces seam visibility and supports semantic modification of arbitrary tile regions.

---


### 120. [Augmentation techniques for video surveillance in the visible and thermal spectral range](https://arxiv.org/abs/2606.13042)

**<font color=#1a73e8>作者：</font>** Vanessa Buhrmester, Ann-Kristin Grosselfinger, David Munch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In intelligent video surveillance, cameras record image sequences during day and night. Commonly, this demands different sensors. To achieve a better performance it is not unusual to combine them. We focus on the case that a long-wave infrared camera records continuously and in addition to this, another camera records in the visible spectral range during daytime and an intelligent algorithm supervises the picked up imagery. More accurate, our task is multispectral CNN-based object detection. At first glance, images originating from the visible spectral range differ between thermal infrared ones in the presence of color and distinct texture information on the one hand and in not containing information about thermal radiation that emits from objects on the other hand. Although color can provide valuable information for classification tasks, effects such as varying illumination and specialties of different sensors still represent significant problems. Anyway, obtaining sufficient and practical thermal infrared datasets for training a deep neural network poses still a challenge. That is the reason why training with the help of data from the visible spectral range could be advantageous, particularly if the data, which has to be evaluated contains both visible and infrared data. However, there is no clear evidence of how strongly variations in thermal radiation, shape, or color information influence classification accuracy. To gain deeper insight into how Convolutional Neural Networks make decisions and what they learn from different sensor input data, we investigate the suitability and robustness of different augmentation techniques...

---


### 121. [No Hidden Prompts Needed! You Can Game AI Peer Review with Presentation-Only Revisions](https://arxiv.org/abs/2606.13044)

**<font color=#1a73e8>作者：</font>** Xu Yang, Zhizhou Sha, Junbo Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI-generated reviews move from experimental tools into peer-review infrastructure, most robustness concerns have focused on explicit attacks such as hidden instructions and prompt injection. We study a harder and more policy-relevant failure mode: no hidden text, no prompt injection, and no changes to methods, experiments, figures, equations, proofs, or numerical results. The attacker modifies only presentation-level content, such as the abstract, contribution framing, related work, discussion, and narrative structure. We introduce adversarial repackaging: a closed-loop attack that uses AI-reviewer feedback to search for presentation-level revisions while keeping the scientific evidence fixed. Across three mainstream AI reviewers, adversarial repackaging achieves a 75.1% attack success rate and a mean score gain of +1.21/10. The effect is not explained by ordinary prose polishing. We also reveal that strategies that change how the reviewer interprets the paper, such as related-work repositioning and analytical discussion expansion, substantially outperform surface edits such as local polishing, table formatting, and algorithm boxes.
Our analysis reveals two deeper structural failure modes. First, AI reviewers are easier to impress than to convince: highlighting strengths reliably increases perceived merit, while attempts to dissolve weaknesses frequently backfire. Second, AI reviewers can confuse the appearance of addressing a limitation with actually resolving it, allowing unchanged evidence to be reinterpreted as stronger scientific contribution. These results show that the deployment risk is not only malicious hidden instructions, but the emergence of paper presentation itself as an optimization surface. We release a contamination-free rolling benchmark and attack framework for testing whether AI reviewers remain anchored to scientific content under presentation-only edits.

---


### 122. [AAbAAC: An Annotated Corpus for Autoimmunity Information Extraction](https://arxiv.org/abs/2606.13051)

**<font color=#1a73e8>作者：</font>** Fabien Maury, Solène Grosdidier, Maud de Dieuleveult 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite advances in information extraction driven by deep learning and large language models, performance gaps remain in highly specialized biomedical fields, where domainspecific complexity poses challenges for generalist models. In this work, we focus on the domain of autoimmunity, where the main entities of interest are autoimmune diseases, autoantibodies (i.e., molecules that may mark or cause these diseases), their molecular targets, their location in the body, and their associated clinical signs. Herein, we present AAbAAC (AutoAntibodies and Autoimmunity Annotated Corpus), a corpus of 115 abstracts selected from PubMed, where we manually annotated entities and their relationships. First, AAbAAC was used to evaluate several methods on the task of named entity recognition (NER), and secondly, to fine-tune NER models. Our study demonstrates the utility of AAbAAC for information extraction in the domain of autoimmunity, showing expected improvement in NER performance after finetuning. This illustrates the value of small-scale annotation efforts for specialized domains and contributes to the computational study of autoimmunity. The AAbAAC corpus is available at this https URL.

---


### 123. [A green solvent screening tool for emerging materials via uncertainty aware, transformer enhanced transfer learning](https://arxiv.org/abs/2606.13060)

**<font color=#1a73e8>作者：</font>** Ioannis Kouroudis, Simon Ternes, Zhaosu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of solubility remains a central challenge across materials science and sustainable chemistry. In particular due to emerging technologies like organic and hybrid photovoltaics, batteries, and catalysis, solvent usage is expected to increase significantly within the coming years. Therefore, substituting solvents with greener alternatives is vital. This is where machine learning can have substantial impact. However, the limited data on critical parameters of solubility significantly constraints machine learning efficacy. In this work, we transfer a pre-trained foundational model on QM9 targets to our application with minimal data requirements. Additionally, the pipeline integrates uncertainty quantification, allowing the user to gauge the confidence of the predictions. As baseline, we succeed in predicting the Hansen solubility parameters and Dielectric Constant for which extensive databases exist. Importantly, we achieve high model performance on additional targets, such as Gutmann Donor and Acceptor numbers, where the available data is extremely limited. Overall, we augment data on solubility descriptors by orders of magnitude with high quality predictions. For effective dissemination, we deploy easy-to-use, easily integrateable with high throughput labs, customizable tool for ranking and screening possible solvent substitutes. Finally, we rediscovered known green solvent alternatives and proposed new candidates proving its relevance for finding eco-friendly solvents.

---


### 124. [Limits of spectral learning under noise](https://arxiv.org/abs/2606.13067)

**<font color=#1a73e8>作者：</font>** Sabin Roman, Ljupco Todorovski, Saso Dzeroski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning functional relationships from noisy data is a central problem in scientific inference. Spectral methods approximate unknown functions by expanding them in a basis and estimating the corresponding coefficients from data, but the stability of these coefficients under noise remains poorly understood. Here we study supervised regression with additive label noise using sparse spectral representations across multiple bases and dimensions. We show that noise induces a predictable drift in the learned coefficient vector whose magnitude depends on the effective number of active spectral modes. After whitening the empirical feature geometry, we derive a closed-form expression for the overlap between noisy and noiseless coefficient vectors, revealing a universal degradation curve governed by a single intrinsic noise scale. Numerical experiments across Fourier, Legendre, Bessel, and Haar bases confirm the theoretical prediction. The results demonstrate that spectral learning exhibits a fundamental noise threshold beyond which coefficient estimates become unstable, placing intrinsic limits on recovering functional structure from noisy data.

---


### 125. [Effects of Social Interactions in Self-Organising Railway Traffic Management](https://arxiv.org/abs/2606.13068)

**<font color=#1a73e8>作者：</font>** Fabio Oddi, Federico Naldini, Leo D'Amato 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent research is exploring self-organised traffic management as a solution for scaling to complex real-world networks. In such a system, trains predict their neighbourhood, produce traffic plan hypotheses, and agree via consensus with neighbours on a future traffic plan to be implemented. This paper investigates a structural parameter within this pipeline: the predictive neighbourhood horizon. The horizon is used by trains to identify future potential conflicts with neighbours, and to establish the local interaction topology, that is, the subset of trains to negotiate with. As the primary design variable, the horizon directly determines the size and density of the social interaction graph, whereas its impact on the complexity of local sub-problems and the distributed consensus dynamics represents a trade-off to be explored. Through a closed-loop simulation framework the study evaluates how variations of the horizon impact the overall decentralised coordination process, from initial conflict detection to distributed schedule consensus. The analysis focuses on investigating the potential trade-off introduced by the horizon choice: balancing local tractability and computational responsiveness with the need for global schedule coherence and feasibility in safety-critical environments. Contrary to intuition, our empirical results indicate that the short time horizons suffice, while long values compromise local tractability and computational responsiveness with no gain in global schedule optimality.

---


### 126. [$α$-fair heterogeneous agent reinforcement learning](https://arxiv.org/abs/2606.13076)

**<font color=#1a73e8>作者：</font>** Yao-hua Franck Xu, Tayeb Lemlouma, Jean-Marie Bonnin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperation in multi-agent systems is typically optimized through utilitarian objectives that maximize overall efficiency but fail to account for reward distribution, often resulting in inequitable "leader-follower" dynamics. While fairness-based approaches encourage pro-social behaviors where every agent benefits from cooperation, many current algorithms - including those utilizing reward shaping - break the stationarity of Markov Games or lack rigorous theoretical guarantees. This creates a critical gap between fair objective methods and theoretically safe learning frameworks. We propose a novel framework that bridges $\alpha$-fairness with Heterogeneous-Agent Trust Region Learning (HATRL), ensuring monotonic improvement and convergence toward Nash Equilibria. Our approach leverages a fair advantage function that dynamically weights agent utilities based on their expected returns, allowing the global objective to transition from purely utilitarian efficiency to $\alpha$-fairness welfare based on the parameter $\alpha$. We introduce two practical algorithms, $\alpha$-fair HATRPO and $\alpha$-fair HAPPO, and demonstrate through experiments in sequential social dilemmas like CleanUp and CommonHarvest that they perform better than HATRL's algorithms from a utilitarian point of view while achieving socially higher outcomes.

---


### 127. [Emotional regulation improves deep learning-based image classification](https://arxiv.org/abs/2606.13081)

**<font color=#1a73e8>作者：</font>** Riccardo Emanuele Landi, João M. F. Rodrigues, Marta Chinnici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emotion significantly influences cognition, enhancing memory and learning under certain conditions. Drawing on this principle, emotion-augmented deep learning investigates how affective states can improve neural network architectures and learning paradigms, achieving better generalization than non-emotional models. However, existing methods often rely solely on objective neurophysiological factors, neglecting the role of subjectivity in emotion. To bridge this gap, the present study introduces Emotional Regulation, a novel framework for modeling emotion in deep learning through artificial subjective experience. The method employs pre-training based on affective stimuli, balancing non-emotional and emotionally-influenced responses in downstream task optimization. Extensive experimentation was conducted in image classification, pre-training ResNet and ViT architectures on four emotional datasets, using CIFAR-10 and -100 as target benchmarks. Results reveal improvements over the aforementioned backbones, providing evidence of Emotional Regulation as a promising method for defining emotion-augmented deep learning through artificial subjective experience. Furthermore, the proposed approach overcomes the related work in image classification based on CIFAR, revealing Emotional Regulation as the new state-of-the-art in emotion-augmented deep learning for large-scale vision datasets. The study also enforces evidence of the impact of affective states in improving machine learning tasks' optimization, encouraging further investigation on emotion-inspired architectures.

---


### 128. [Unified MRI Brain Image Translation via Hierarchical Tumor Structure Comparison](https://arxiv.org/abs/2606.13096)

**<font color=#1a73e8>作者：</font>** Yupeng Cai, Jia Wei, Jianlong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal MRI brain image translation via available modalities holds significant practical importance in modern medicine, providing robust support for early diagnosis, treatment planning, and outcome assessment of diseases. For this purpose, it is important to ensure the fidelity of the tumor regions after translation. However, existing brain image translation methods ignore the structure information of different tumor regions, which could assist translation models in enhancing the quality and clinical applicability of the translated images.
In this work, we propose a novel translation model called HTSCGAN, which is a unified multi-modal brain image translation generative adversarial model integrating the structural information within tumor regions with the aim of improving the quality of brain image translation. Specifically, the generator employs three Patch Contrast Module (PCM) with different patch sizes to capture the hierarchical structural information of the tumor regions. In addition, a pretrained Patch Classifier (PC) and a pretrained Structure-Aware Encoder (SAE) are employed to derive the generated image containing the same tumor region structure as the ground truth image via patch classification loss and tumor perceptual loss, respectively. The experiments on BraTS2020 and BraTS2021 demonstrate strong performance of our model in both translation tasks and down stream segmentation tasks, highlighting its effectiveness in enhancing the quality and clinical relevance of the translated brain images. Our code is available at this https URL.

---


### 129. [LEDGER: A Long-Context Benchmark of Corporate Annual Reports for Grounded Financial Retrieval and Extraction](https://arxiv.org/abs/2606.13100)

**<font color=#1a73e8>作者：</font>** Charles Moslonka, Amaury de Vitry, Arthur Garnier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Finance reporting is a natural proving ground for large language models, and the very-long-context capabilities of recent models across all sizes make rigorous evaluation in this domain an increasingly pressing need. Yet most public financial resources reduce the task to plain-text SEC 10-K filings paired with a handful of question-answer items. We release LEDGER (Long-context Evaluation of Documents for Grounded Extraction and Retrieval), a corpus of 4,999 digitized corporate annual reports - full documents with figures, tables, and narrative, not just regulatory filings. Each report is labeled with 31 consolidated financial KPIs to be extracted and linked to the market's reaction at the earnings date. From this data we derive three evaluation benchmarks spanning the difficulty spectrum: a pure page-level KPI retrieval task with TREC-style relevance judgments over 118,048 questions in natural language, a conversational "needle-in-a-haystack" single-value lookup, and a full KPI extraction task, both from long, numerically dense reports. We additionally provide human OCR-quality annotations with inter-annotator agreement and the complete extraction, validation, and scoring toolchain. We further demonstrate the dataset's research utility with a case study linking CEO-letter rhetoric to post-publication market impact.

---


### 130. [Disparate Impact in Synthetic Data Generation](https://arxiv.org/abs/2606.13105)

**<font color=#1a73e8>作者：</font>** Paul Andrey, Michaël Perrot, Batiste Le Bars 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit the fairness notion of disparate impact for synthetic data generation (SDG), that assesses whether the utility of generated records is the same across sensitive groups. Our approach departs from existing work on fair SDG, that address the problem of correcting for undue biases in the observed distribution, hence redefining SDG as learning a distribution that is not that of the real data. By contrast, non-disparate impact is notably achieved when the synthetic and real distributions are the same. We expose reasons why SDG may fail to reach that solution and discuss why approximation and estimation errors occur and can be disparate across groups. We notably look into the expressive power of SDG methods relative to distribution complexity, sampling errors due to group proportions, and estimation errors induced by differential privacy mechanisms. We illustrate cases of disparate impact on both artificial and real-world data, focusing on SDG methods that rely on probabilistic graphical models. We also introduce a strategy of learning group-wise SDG models and illustrate how it can improve both the overall utility and its parity in many settings.

---


### 131. [Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning](https://arxiv.org/abs/2606.13106)

**<font color=#1a73e8>作者：</font>** Jiayu Yang, Chao Chen, Shengen Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent chain-of-thought compresses reasoning by replacing visible reasoning traces with continuous hidden-state recurrence, but existing formulations are difficult to optimize with standard on-policy reinforcement learning (RL) and hard to interpret causally. Our key insight is that a single pair of explicit boundary tokens can address both issues at once: discrete entry and exit anchors make the latent block compatible with standard on-policy RL, and the same anchors offer a natural foothold for mechanistic analysis. Motivated by this, we propose SWITCH, a switchable latent reasoning framework. The model emits <swi> to enter latent mode and </swi> to exit. Because the boundaries are ordinary discrete tokens, the GRPO policy ratio is well-defined at every decision point. The same anchors also expose the latent steps to direct probing and causal intervention. We train the model with a visible-to-latent curriculum and a Switch-GRPO objective that propagates gradients through recurrent latent computation. SWITCH consistently outperforms prior hidden-state-recurrence latent reasoning approaches at similar scale. Mechanistic analysis through the boundary tokens further reveals three findings: (i) <swi> is a sharply localised, learned switching policy rather than a stylistic artefact; (ii) the latent step it opens performs problem-specific, causally important computation rather than acting as an inert placeholder; and (iii) that computation is concentrated at a single hidden-state transition on entry. Together, these results show that hidden-state-recurrence latent reasoning is both RL-trainable and open to direct mechanistic analysis, including of how on-policy RL itself improves the model from the inside.

---


### 132. [The Invisible Ink of the Android Malware World: A Longitudinal Study on the Usage of Covert Communication Channels](https://arxiv.org/abs/2606.13107)

**<font color=#1a73e8>作者：</font>** Zeya Umayya, Manan Aggarwal, Manan Chugh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proxies, VPNs and Tor have long helped the privacy community and users in censored regions to fight censorship. However, the same tools can be maliciously exploited by malware and botnets to conceal their communication to external command and control servers. Despite being a critical concern fueled by the proliferation of malware based attacks, no longitudinal studies have analyzed how malware applications use covert channels (CC) to evade detection.
We fill this gap by performing the first study of the usage of covert channels in the Android malware ecosystem. To that end, we develop a multistage pipeline that combines static and dynamic analysis to investigate both system and network-level features. We applied this pipeline on a corpus of 3.5M Android malware spanning 2009 to July 2025. Our carefully crafted static validation rules uncovered 288K APKs that used CCs spanning 511 malware families and CC usage growing exponentially from 0.30\% (2012) to 50\% (2025). Overall, in dynamic analysis, we identified 19,308 unique IP addresses being contacted in 85 countries, out of which we were able to explicitly validate the presence of CCs for 59 IP addresses across 17 countries. Further, we performed a longitudinal dataset study spanning over 16 years for CC based malware and found that CC usage has evolved, \textit{e.g.,} some malware adopted by using more than one CCs; others switched between them periodically (one family switched CC usage 40 times from 2019 to 2025).

---


### 133. [EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge](https://arxiv.org/abs/2606.13120)

**<font color=#1a73e8>作者：</font>** Yunhan Wang, Jiaan Wang, Lianzhe Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search Agents -- large language models augmented with search tools -- have intensified the need for future-proof evaluation benchmarks. Existing benchmarks such as BrowseComp rely on static knowledge, making them vulnerable to test-set contamination and parametric memorization. Consequently, models can achieve high scores through fact recall rather than genuine retrieval, obscuring true browsing competence via reasoning shortcuts.
In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal. To collect these questions, we design a three-agent collaborative framework: (1) a QA synthesis agent that retrieves fresh knowledge from the live web to synthesize QA pairs; (2) an information filtering agent that filters retrieved knowledge in terms of credibility and popularity to block parametric shortcuts; and (3) a high-level guidance agent that formalizes questions into reasoning graphs to reduce logical redundancy and shortcuts in synthesized QA pairs. Because the framework supports fully automated synthesis, EvoBrowseComp can be regularly updated to prevent data contamination and maintain temporal freshness. Extensive experiments confirm its great difficulty, requiring broad horizontal search. It establishes a scalable paradigm for auto-updatable, high-difficulty benchmarking that keeps pace with both evolving world knowledge and advancing agent capabilities.

---


### 134. [NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation](https://arxiv.org/abs/2606.13121)

**<font color=#1a73e8>作者：</font>** Dongwook Lee, Youngho Cho, Sangkwon Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech-to-speech translation aims to enable near-real-time communication by minimizing latency, offering a compelling, real-time alternative to the high latency of consecutive translation. However, the excessive pursuit of low latency often results in fragmented chunk-wise speech. Consequently, listeners are subjected to an unnatural acoustic flow punctuated by frequent pauses, which could increase their cognitive load. To bridge this gap, we introduce a fluency-aware optimization framework designed to discover the sweet spot between the low-latency benefits of simultaneous translation and the natural flow of consecutive translation. Our framework minimizes inter-chunk silences by leveraging model-internal signals, including linguistic diversity and induced temporal variability in speech durations. Experiments on short- and long-form benchmarks show that our framework produces natural speech flow while maintaining competitive latency and translation quality.

---


### 135. [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/abs/2606.13126)

**<font color=#1a73e8>作者：</font>** Nathan Ordonez, Thomas Parnell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented and agentic workloads repeatedly prefill recurring predictable structured inputs (which we call "spans") such as documents and code files. Yet, prefix caching in engines such as vLLM cannot reuse their KV entries unless they share identical prefixes with another request, while Position-Independent Caching (PIC) implementations within production-grade inference servers typically either require substantial server code changes or keep KV state outside the server, incurring host-to-device transfer overhead. We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives. MiniPIC stores unrotated K vectors in the KV cache, applies RoPE to K tiles inside attention using per-request logical positions, and exposes three user-facing and token-level primitives: block-aligned padding, span separator (SSep), and prompt depend (PDep), that modify hashing behavior and effective block-level causal attention structure. With fewer than 100 lines of core-engine changes plus a custom attention backend, these primitives are sufficient to realize multiple PIC methods, including Block-Attention, EPIC, and Prompt Cache, within the same running vLLM instance, while natively integrating with KV cache CPU offload implementations. On 2WikiMultihopQA, MiniPIC with interleaved scheduling improves prefill throughput by 49% over baseline vLLM, reduces cached-span time-to-first-token by up to two orders of magnitude, preserves the linear prefill scaling of uncached spans, and incurs only 5.7% worst-case overhead.

---


### 136. [Fully Distributed Multi-View 3D Tracking in Real-Time](https://arxiv.org/abs/2606.13127)

**<font color=#1a73e8>作者：</font>** Byron Hernandez, Fangyu Li, Aotian Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera tracking with overlapping fields of view typically relies on centralized fusion, which creates computational bottlenecks that prevent deployment at scale. We present MV3DT, a fully distributed framework for real-time multi-view 3D tracking that achieves accurate identity propagation and occlusion recovery through peer-to-peer coordination, eliminating the need for central aggregation. Each camera node executes a lightweight modular pipeline comprising monocular 3D perception, distributed multi-view association, and collaborative fusion via lightweight messaging. MV3DT achieves 94.3% IDF1 and 93.3% MOTA on WILDTRACK, competitive with state-of-the-art centralized methods, while demonstrating superior scalability by sustaining 30 FPS on 100 cameras with less than 10 ms inter-camera latency and only 2.2% communication overhead. MV3DT operates in a zero-shot regime given camera calibrations, requiring no scene-specific learning and making it directly deployable in new environments. These results establish MV3DT as a practical solution for real-time multi-view tracking in large-scale overlapping camera networks.

---


### 137. [Cascade Classification of Dermoscopic Images of Skin Neoplasms with Controllable Sensitivity and External Clinical Validation](https://arxiv.org/abs/2606.13135)

**<font color=#1a73e8>作者：</font>** Elena S. Kozachok, Sergey S. Seregin, Aleksandr V. Kozachok 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose. To compare deep learning architectures and classification schemes for dermoscopic images of skin neoplasms and assess their generalization on transfer from open international datasets to independent clinical datasets of Russian practice.
Methods. Four architectures (ViT-B/16, Swin-S, ConvNeXt-S, EfficientNetV2-S) were compared in three schemes: binary (malignant/benign), single-stage four-class (benign, MEL, SCC, BCC), and a two-stage cascade (binary triage, then three-class differentiation MEL/SCC/BCC). All models used ImageNet-pretrained weights and a single augmentation protocol on aggregated open ISIC Archive data, and were evaluated on an internal held-out sample and two clinical datasets (Melanoscope AI mobile system; Sechenov University).
Results. Internally the binary stage attains ROC-AUC 0.952-0.966; on Sechenov University it drops to 0.797-0.893, sensitivity to 0.53-0.67, and ECE rises from 0.02 to 0.27-0.39 with underestimation of malignancy, quantifying a generalization gap in ranking and calibration. Paired tests confirm one inter-architecture result on clinical data: the deficit of ViT-B/16 at the binary stage (p<0.05); at the differentiation stage no architecture has a proven advantage. The cascade raises macro F1 over single-stage four-class classification for most architectures, but significantly only for ViT-B/16, by recovering malignant lesions assigned to the dominant benign class. On ISIC MILK10k, direct 11-class classification yields mean-class sensitivity 0.525.
Conclusion. A tunable triage threshold gives sensitivity control not attainable in standard single-stage (argmax) classification and better reproduces clinical differential-diagnosis logic. The persistent generalization gap mandates external clinical validation and recalibration before deployment.

---


### 138. [An Extensible and Lightweight Unified Architecture for Demosaicing Pixel-bin Image Sensors](https://arxiv.org/abs/2606.13136)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar, Nutan Sairam Yenneti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-bin image sensors are becoming the default choice for smartphone cameras due to their resolution vs light-gathering trade-off. However, their larger inter-color separation compared to the Bayer color filter array (CFA) makes them challenging to demosaic. Furthermore, existing deep learning-based demosaicing methods are CFA-specific, requiring multiple individual models that take up precious onboard resources and demand larger development and maintenance efforts. In this work, we propose a modular unified architecture for demosaicing various pixel-bin sensors that provides higher image quality while being extensible and lightweight. Additionally, to enable plug-and-play operation, we introduce a learning-free CFA-identification module to detect the CFA type of raw data accurately.

---


### 139. [HyPE: Category-Aware Hypergraph Encoding with Persistent Edge Embeddings for Persona-Grounded Dialogue](https://arxiv.org/abs/2606.13142)

**<font color=#1a73e8>作者：</font>** Sangwon Youn, Yoonjin Jang, Youngjoong Ko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona-grounded dialogue systems aim to produce responses consistent with a speaker's persona, yet existing methods treat personas as a flat set of sentences and fail to model the high-order relations among persona attributes-e.g., that several persona sentences share a topical category. We propose HyPE (Hypergraph Persona Encoder), a framework that (i) analyzes each persona-bearing text as a (Core, Expression, Sentiment, Category) quadruple, and (ii) organizes persona elements into a hypergraph whose hyperedges are induced by shared category labels. An HyperGCN hypergraph neural network propagates this structure into a persona summary vector and a soft-memory bank that condition the response generator. We further propose Persistent Edge Embeddings (PEE), lightweight per-category learnable priors fused into the HyperGCN message-passing step. On PersonaChat under greedy decoding, HyPE consistently outperforms sentence-level pooling baselines across GPT-2, LLaMA-3.2-3B, and Qwen2.5-3B backbones by demonstrating that structured hyperedge-level persona encoding provides a transferable advantage across model scales.

---


### 140. [When Does Routing Become Interpretable? Causal Probes on Block Attention Residuals](https://arxiv.org/abs/2606.13168)

**<font color=#1a73e8>作者：</font>** Aydin Javadov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block Attention Residuals (Block AttnRes) by replace fixed additive residuals with a learned softmax over earlier depth-source representations, surfacing cross-layer routing as an inspectable tensor in the forward pass. This is a tempting interpretability target: information flow normally inferred indirectly is now directly observable. We ask whether such exposure suffices for mechanistic interpretation. We probe two same-scale ($0.6$B) Block AttnRes checkpoints under identical routing-ablation interventions: a vanilla Qwen3 inference-wrapped through a deterministic recency-bias schedule that the codebase admits as a routing-equivalent loading path, and a Block AttnRes Qwen3 trained from scratch with routing as part of optimisation. The wrapped baseline's routing weights are content-independent and reproduce the schedule's analytic prediction. The trained AttnRes checkpoint instead exhibits three localised routing motifs: an embedding-source pathway through early-layer MLP, a current-state pathway through early-layer attention and MLP, and an older-history pathway through late-layer attention. Beyond this stratification, we find a sharp dissociation between average routing mass and causal importance: in both sublayers, the largest mass slice is not the largest causal contribution, and one source family carries appreciable mass with no detectable causal role under intervention. Architectural exposure of routing is therefore necessary but not sufficient for mechanistic interpretation: structured depth routing emerges only when routing has been part of training, and even then, descriptive routing summaries should be treated as candidate hypotheses to be tested by causal interventions, not as evidence of mechanism in their own right.

---


### 141. [Detecting Explanatory Insufficiency in Learned Representations: A Framework for Representational Vigilance](https://arxiv.org/abs/2606.13172)

**<font color=#1a73e8>作者：</font>** Jacques Raynal, Pierre Slangen, Elsa Raynal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations are central to modern machine learning and are commonly evaluated through predictive performance, robustness, uncertainty estimation, or generalization. However, a learned representation may remain operationally successful while progressively failing to organize persistent residual structures that are not fully captured by conventional evaluation metrics. This article introduces VER, the Vigilant Evaluator of Representations, a conceptual framework for monitoring representational adequacy in learned representations. VER does not propose a new learning algorithm, loss function, or model architecture. Instead, it formalizes a diagnostic process through which persistent residual structures may be identified, analyzed, and interpreted as potential indicators of explanatory insufficiency. The framework distinguishes representational inadequacy from ordinary prediction error, uncertainty, noise, and distribution shift. It introduces a monitoring sequence based on representation identification, explanatory-domain delimitation, residual-structure detection, explanatory-resistance evaluation, and vigilance signaling. VER is intended as a contribution to representation diagnostics in machine learning. Its objective is not to replace existing evaluation methods but to complement them by treating representational adequacy as an explicit object of inquiry. A path toward empirical evaluation through representational-vigilance benchmarks is also outlined.

---


### 142. [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/abs/2606.13174)

**<font color=#1a73e8>作者：</font>** Yujun Zhou, Kehan Guo, Haomin Zhuang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Unlike runtime checks written ahead of time by developers, TRACE skills come from the user's own chat corrections. We evaluate TRACE with simulated user-in-the-loop experiments on ClawArena coding-agent tasks and MemoryArena-derived memory-intensive tasks. On ClawArena, TRACE reduces held-out preference violation from 100.0% to 37.6% on in-distribution tasks and from 100.0% to 2.0% on out-of-distribution tasks. On MemoryArena-derived tasks, TRACE reduces in-distribution violation from 100.0% to 60.5% while matching or exceeding the strongest memory baseline on task pass. These results suggest that compiling corrections into runtime enforcement can address a repeated-friction failure mode that memory alone does not reliably solve, reducing the need for users to restate the same correction across future sessions. Experiment code is available at this https URL, and the deployable skill is available at this https URL.

---


### 143. [Loss-Shift Transfer via Bayes Quotients](https://arxiv.org/abs/2606.13178)

**<font color=#1a73e8>作者：</font>** Vasileios Sevetlidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning is usually studied as a consequence of distribution shift. This paper identifies an orthogonal failure mode in which the data distribution is fixed and the loss changes. This setting is called \emph{loss shift}. A loss determines which information in \(X\) is Bayes-relevant, and two losses may therefore require different representations even under the same joint law \(P(X,Y)\). The idea is formalized using Bayes quotients, which allow losses to be ordered by refinement. In the Bayes-quotient formulation, strict refinement gives an immediate qualitative obstruction. A source-minimal representation for a coarser loss is insufficient for a strictly finer target loss. For finite-output log loss, this obstruction becomes an exact quantitative identity. The excess risk is the conditional information about \(Y\) discarded by the representation. Experiments in controlled, learned, synthetic-image, and real-image settings show the predicted effect, i.e., classification-equivalent representations can have different optimal log-loss performance under a fixed data distribution.

---


### 144. [LAUKIN: A Multi-jurisdictional Common Law Contract Dataset](https://arxiv.org/abs/2606.13184)

**<font color=#1a73e8>作者：</font>** Amrita Singh, Aditya Joshi, Jiaojiao Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multinational companies increasingly require cross-jurisdictional contract review, yet existing legal NLP datasets are largely restricted to a single jurisdiction. We introduce LAUKIN (Legal equivalence dataset of Australia, UK, and INdia), a dataset of clause pairs (AU-UK, UK-IN, IN-AU) labelled for boolean legal equivalence. We develop a novel multi-stage retrieval and reranking pipeline to construct the initial clause pair mapping, with a subset of clause pairs subsequently annotated by legal experts as Equivalent or Not Equivalent. The dataset comprises 14,727 clause pairs from 204 contracts across 8 agreement types, of which 3,000 are manually labelled: 900 train, 600 dev, and 1,500 test. We evaluate 12 models across 4 techniques, achieving a best macro-F1 of 65.11%, establishing LAUKIN as a challenging benchmark. Results reveal that, despite shared legal heritage, drafting conventions diverge significantly across jurisdictions, making cross-jurisdictional equivalence classification non-trivial. LAUKIN also includes 11,727 unlabelled training pairs to support future semi-supervised learning research in legal NLP.

---


### 145. [A Context-Aware Dataset for Stance Detection in Bioethical Controversies on Reddit](https://arxiv.org/abs/2606.13187)

**<font color=#1a73e8>作者：</font>** Hu Huang, Genan Dai, Fuqiang Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bioethical debates increasingly unfold on social media, yet stance detection research lacks large-scale, domain-specific resources for modeling such context-dependent discourse. We present BioStance, a context-aware dataset of 39,600 annotated Post-Comment pairs from Reddit bioethical discussions. BioStance covers six controversial targets across three dimensions of bioethical controversy: fundamental value conflicts, individual liberty versus collective responsibility, and technological uncertainty. Each instance preserves hierarchical conversational context and is labeled by three independent annotators using a three-class stance scheme: Favor, Against, and None. The annotations achieve a mean Krippendorff's $\alpha$ of 0.82, indicating substantial reliability. By combining thematic diversity, conversational structure, and high-quality human annotation, BioStance supports research on context-aware stance detection, argument mining, and computational analysis of bioethical discourse.

---


### 146. [Transformer-Guided Graph Attention for Direct Cardiac Mesh Reconstruction: A Structural Digital Twin Framework](https://arxiv.org/abs/2606.13188)

**<font color=#1a73e8>作者：</font>** Abhishek H S, Akash Ganamukhi, Abhimanyu Suresh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building patient-specific cardiac models sits at the heart of precision cardiology, yet getting those models into clinical use keeps running into the same wall: mesh generation is slow, messy, and frustrating. The standard workflow -- segmenting the image, running Marching Cubes, and then manually cleaning up the result -- is time-consuming, inconsistent across operators, and demands specialist knowledge most clinical teams do not have. We take a fundamentally different approach. Instead of treating segmentation and mesh generation as two separate problems, we train a single end-to-end network that goes directly from a raw 3D medical image to a smooth, simulation-ready cardiac surface mesh. The core is a 3D Swin Transformer encoder-decoder that extracts volumetric features from CT or MRI volumes, paired with a Graph Attention Network (GAT) head that iteratively deforms a template mesh to fit the patient's cardiac boundary. We tested on the MM-WHS 2017 benchmark using both CT and MRI. Segmentation scores were competitive (Dice of 0.84 on CT, 0.83 on MRI), but the primary focus is mesh quality: mean Chamfer distance of 1.8 mm, with 95th-percentile surface distance below 5 mm. Every mesh is produced in a single forward pass -- no Marching Cubes, no smoothing filters, no manual cleanup. We argue that for cardiac digital twin pipelines, geometric fidelity and topological correctness matter more than pixel-level Dice scores. By removing the post-processing bottleneck, this approach makes patient-specific cardiac simulation substantially more accessible for clinical use.

---


### 147. [The Geometry of Phase Transitions in Generative Dynamics via Projection Caustics](https://arxiv.org/abs/2606.13191)

**<font color=#1a73e8>作者：</font>** Ryosuke Sakamoto, Kotaro Sakamoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-state generative samplers, including diffusion and flow-matching models, evolve through continuous reverse-time dynamics, yet their samples often undergo abrupt qualitative changes: trajectories commit to modes, semantic alternatives collapse, and small perturbations in narrow time windows can produce large downstream effects. This paper develops a geometric account of such phase-transition-like behaviour. We view denoising as gradient descent on a free energy landscape and show that sharp transitions arise near projection caustics, where the nearest-point projection onto the data support ceases to be unique. Motivated by this perspective, we introduce the Critical Boundary Detector (CBD), as practical diagnostics for score-direction instability. Across toy models, standard diffusion models, and latent text-to-image diffusion models, CBD localises mode commitment, predicts intervention-sensitive windows, and supports targeted control in geometrically sensitive regions. Our results connect geometry of data and dynamics of diffusion generation.

---


### 148. [WHAR Arena: Benchmarking the State of the Art in Efficient Wearable Human Activity Recognition](https://arxiv.org/abs/2606.13194)

**<font color=#1a73e8>作者：</font>** Maximilian Burzer, Tobias King, Till Riedel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has become the dominant paradigm in Wearable Human Activity Recognition (WHAR), yet progress is obscured by a comparability crisis. Results are often reported using inconsistent datasets, custom data processing, and varying evaluation protocols, making state-of-the-art claims fragile. We address this with a large-scale, open-source benchmark that integrates 30 diverse datasets under standardized processing, unified model interfaces, and a shared cross-subject evaluation protocol. Evaluating 17 representative architectures across 4760 training runs, we jointly measure predictive performance alongside on-device latency, peak memory, and model size on an Android reference device. Our results reveal that the WHAR state of the art is distributed rather than dominated by a single architecture. While CNN-HAR achieves the highest mean macro-F1, top-performing models cluster tightly, indicating contemporary architectures have converged near a predictive performance ceiling. When accounting for deployment efficiency, compact neural models, such as TinierHAR, and classical Random Forests define the practically relevant Pareto frontier, whereas larger recurrent and hybrid models incur high hardware costs without corresponding performance gains. Consequently, while predictive performance has plateaued, substantial potential for future progress remains in optimizing deployment efficiency and improving adaptation to domain shifts. We release our full framework to support transparent reuse and extension.

---


### 149. [Under What Conditions Can a Machine Become Genuinely Creative?](https://arxiv.org/abs/2606.13196)

**<font color=#1a73e8>作者：</font>** Yong Zeng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI systems can generate texts, software architectures, hypotheses, designs, and scientific workflows that appear creative. This paper asks under what conditions a machine can become genuinely creative, and how human agency can be preserved within shared cognitive and creative environments. It develops a requirement framework derived from Designics, the science of meaning-bearing intentional change. The paper argues that genuine machine creativity should not be defined by output novelty, current performance, or transient architecture alone. Instead, creativity is understood as the structural transformation of incomplete situations through recursive intervention dynamics. On this view, it depends on ten requirements: environment representation, scoped perception, conflict identification, intervention capability, consequence observation, knowledge and environment update, rescoping, local-to-global unfolding, value-based scoping, and human-AI co-living. These are organized through the three laws of Designics: perception, conflict, and capability. The paper illustrates the computational tractability of these requirements through selected cyber-physical and cyber-biological studies, including recursive element extraction, autonomous mesh generation, and neurophysiological and workload analysis. It then treats open-ended systems, automated discovery frameworks, self-modifying agents, foundation models, and agentic workflows as pressure cases: they demonstrate powerful generative means but do not by themselves establish genuine machine creativity. Finally, the paper argues that proactive AI ethics is internal to genuine machine creativity rather than an after-the-fact filter. Value-based scoping and human-AI co-living must shape how creative machines perceive environments, identify conflicts, select interventions, observe consequences, update knowledge, and rescope future action.

---


### 150. [A Minimal Model of Bounded Trade-Off Screening in Multi-Attribute Choice](https://arxiv.org/abs/2606.13201)

**<font color=#1a73e8>作者：</font>** Manisha Dubey, Anirban Sarkar, Subramanian Ramamoorthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human decision-making often involves choosing between multi-attribute alternatives, yet classical models assume fully compensatory utility aggregation despite evidence that people reject options with poor performance on critical attributes. We propose a bounded trade-off reasoning framework in which decisions are governed by a screening process that evaluates the balance between gains and losses across attributes. The model introduces a trade-off tolerance parameter that controls acceptable imbalance and can vary across contexts. Through simulation, we show that this mechanism produces preference patterns that differ from standard utility-based models and captures context-dependent variation in trade-off behavior. These results establish bounded trade-off screening as a plausible computational mechanism for multi-attribute choice and generate testable predictions for future behavioral studies.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
