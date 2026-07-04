# 📦 其他研究 | 2026年07月05日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

---

### 251. [Extreme Adaptive Transformer for Time Series Forecasting](https://arxiv.org/abs/2607.02437)

**<font color=#1a73e8>作者：</font>** Sanjeev Shrestha, Hui Liu, Yifan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting remains challenging when the underlying data contain rare but critical extreme events. This issue is particularly important in hydrologic forecasting, where streamflow distributions are often highly skewed and extreme peaks can have substantial impacts on flood monitoring, water resource management, and early warning systems. Although Transformer-based forecasting models have achieved strong performance by modeling long-range temporal dependencies, they typically treat all time points uniformly and may therefore underrepresent rare extreme patterns. In this paper, we propose the Extreme-Adaptive Transformer (Exformer), a forecasting framework designed to explicitly model temporal dependencies involving both normal and extreme events. Exformer introduces an extreme-adaptive attention mechanism composed of three sparse components: Local, Stride, and Extreme. The Local and Stride components capture short-term and periodic temporal dependencies, respectively, while the Extreme component selectively models event-aware dependencies between normal and extreme streamflow patterns. Experiments on four real-world hydrologic streamflow datasets show that Exformer achieves superior 3-day forecasting performance compared with state-of-the-art baselines. Our findings demonstrate that explicitly incorporating extreme-aware attention improves the forecasting capacity of Transformer models on imbalanced time series with rare but consequential events.

---


### 252. [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440)

**<font color=#1a73e8>作者：</font>** Zhilin Wang, Han Song, Runzhe Zhan 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly expected to improve executable policies through feedback, yet existing evaluations often collapse this process into a final score or confound it with open-ended software-engineering progress. We introduce Autonomous Policy Evolution, a controlled evaluation setting in which a harness-model agent repeatedly edits an executable policy system under a fixed interaction budget. We instantiate this setting in EvoPolicyGym, a benchmark built from compact interactive RL environments that evaluates how agents iteratively improve explored policies. On the EvoPolicyGym suite, GPT-5.5 achieves the strongest aggregate rank score and top-two performance on all 16 environments. Beyond leaderboard results, EvoPolicyGym also provides trajectory-level diagnostics that distinguish how agents allocate budget, convert feedback into parametric tuning. These analyses show that strong autonomous policy evolution depends not only on isolated task wins, but on discovering task-appropriate mechanisms and refining policies under bounded feedback.

---


### 253. [Understanding the Robustness of Distributed Self-Supervised Learning Frameworks Against Non-IID Data](https://arxiv.org/abs/2607.02447)

**<font color=#1a73e8>作者：</font>** Xuanyu Chen, Nan Yang, Shuai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research has introduced distributed self-supervised learning (D-SSL) approaches to leverage vast amounts of unlabeled decentralized data. However, D-SSL faces the critical challenge of data heterogeneity, and there is limited theoretical understanding of how different D-SSL frameworks respond to this challenge. To fill this gap, we present a rigorous theoretical analysis of the robustness of D-SSL frameworks under non-IID (non-independent and identically distributed) settings. Our results show that pre-training with Masked Image Modeling (MIM) is inherently more robust to heterogeneous data than Contrastive Learning (CL), and that the robustness of decentralized SSL increases with average network connectivity, implying that federated learning (FL) is no less robust than decentralized learning (DecL). These findings provide a solid theoretical foundation for guiding the design of future D-SSL algorithms. To further illustrate the practical implications of our theory, we introduce MAR loss, a refinement of the MIM objective with local-to-global alignment regularization. Extensive experiments across model architectures and distributed settings validate our theoretical insights, and additionally confirm the effectiveness of MAR loss as an application of our analysis.

---


### 254. [SoK: A Taxonomy for Cybersecurity Incident Response Influence Factors](https://arxiv.org/abs/2607.02451)

**<font color=#1a73e8>作者：</font>** Thomas Biege, Marius Brockhoff, Jonas Kaspereit 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity incident response has emerged as a critical area of interest for both researchers and practitioners. The corpus of literature on cybersecurity incident response is expanding, yet a unified framework for systematically organizing the accumulated knowledge remains absent. The aspects of incident response span multiple domains, including technology, human-computer interaction, organizational theory, and human factors. A comprehensive, integrative perspective on these factors can enable researchers to identify underexplored areas and more effectively target their empirical and theoretical investigations. Our study systematizes the factors that influence organizational preparedness for and response to cybersecurity incidents. Through a systematic review of academic literature (n = 417) and non-scientific publications (n = 40), we derived the "Cybersecurity Incident Response Influencing Factor Taxonomy" (\textit{CIR-IF Taxonomy}). Existing empirical findings were classified within this taxonomy, providing a comprehensive and up-to-date overview of knowledge from the period 1999 to mid-2024. The taxonomy categories were systematically compared with seven established scientific frameworks and with the \textit{NIST Cyber Security Framework} elements referenced in the \textit{NIST Special Publication 800-61r3} incident response profile. The results of this comparison show that the \textit{CIR-IF Taxonomy} delivers a richer, more rigorous, and more systematically organized view of the factors that drive and shape incident response.

---


### 255. [Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks](https://arxiv.org/abs/2607.02453)

**<font color=#1a73e8>作者：</font>** Xi Zhang, Papi Menon, Vivian Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Since ChatGPT's launch in November 2022, open-source agentic frameworks have proliferated, making framework selection important for engineering teams while obscured by popularity signals such as GitHub stars. This paper analyzes 15 major open-source AI agent framework repositories from late 2022 to early 2026, using 808,042 stars, 73,997 pull requests, 86,241 commits, and 987,330 user profiles to assess ecosystem health across awareness, adoption, and retention. Three findings emerge. First, headline popularity is unreliable. Star counts reflect hype cycles and inorganic activity. AutoGPT gained 111,967 stars in one month but converted fewer than 9 contributors per 1,000 stars, defined as contributor density in this research, compared with LangChain's 41. Lower-profile frameworks such as Pydantic-AI show higher contributor density, indicating deeper adoption. Second, mapping awareness against adoption shows that visibility and engagement diverge. MetaGPT and LangFlow have contributor density ratios below 5 even with their high visibility. Openai-agents-python's limited contributor base suggests institutional backing alone does not ensure community depth. By analyzing cross-framework contribution, we discover that LangChain functions as a shared infrastructure, attracting 82.5% of cross-ecosystem contributors. Third, retention drops most steeply in the first 30 days of initial contribution and stabilizes near 90 days. Overall, ecosystem health is better measured by contributor density, cross-ecosystem engagement, and retention than by stars alone. These metrics offer teams a more robust basis for framework evaluation.

---


### 256. [OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers](https://arxiv.org/abs/2607.02461)

**<font color=#1a73e8>作者：</font>** Donghyun Lee, Jitesh Chavan, Duy Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in a normalized, rotated basis. In this basis, a randomized permuted block-Hadamard (RPBH) rotation concentrates each coordinate around one fixed, known marginal regardless of the input, so a single Lloyd-Max codebook serves all timesteps, prompts, and layers of a given input dimension. We extend the same quantizer to weight rows offline, absorbing the rotation into the weights so that it cancels inside each linear layer and only a forward rotation on the activations remains at runtime. The same recipe transfers from image to video with no per-modality tuning. Across FLUX.1, Z-Image-Turbo, Wan 2.1, and CogVideoX, it sets the state of the art for PTQ at several low-bit settings. It also pushes PTQ of image diffusion transformers to W2A4 with usable generation quality.

---


### 257. [Audio-Based Understanding of Audiobook Narration Appeal](https://arxiv.org/abs/2607.02473)

**<font color=#1a73e8>作者：</font>** Shahar Elisha, Mariano Beguerisse-Díaz, Emmanouil Benetos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narration is central to the audiobook listening experience, shaping how listeners engage with and understand the content. This work explores how narration qualities shape an audiobook's appeal, noting that their effects can vary by genre, title, and audience. We extract vocal and acoustic features (e.g., tone, pace, loudness) from LibriVox using pre-trained audio models and analyse their relationship with consumption data (specifically, view-rate) and their interplay with genre and title. Despite limited consumption data, we find that acoustic information alone has a robust association with appeal, even after accounting for title effects. We further validate these findings using more nuanced proprietary engagement metrics. To our knowledge, this is the first systematic computational study linking narration qualities, genre, title, and audiobook consumption, highlighting the potential of data-driven insights to improve audiobook personalisation and narrator casting.

---


### 258. [Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning](https://arxiv.org/abs/2607.02484)

**<font color=#1a73e8>作者：</font>** Xuehui Wang, Xuankun Yang, Wei Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is a crucial strategy for accelerating VLMs by compressing redundant image patches, yet existing methods often fail to preserve critical cues under dense instructions and fine-grained queries. In this paper, we investigate this failure and identify two underlying bottlenecks: the widespread dispersion of textual noise that corrupts dense cross-modal scoring, and the feature fragmentation inherent to standard token selection. To address these issues, we propose Entropy-Aware Dense Pruning (EADP), a framework that reformulates pruning as a structured compression problem. EADP first leverages statistical entropy to quantify and filter out textual noise, yielding a robust, fine-grained instruction relevance score. Subsequently, instead of naive Top-K selection, EADP casts token selection as a submodular maximization problem with a spatial prior, explicitly ensuring a holistic and non-redundant visual representation. Extensive experiments demonstrate that EADP improves the accuracy-efficiency trade-off of VLMs, robustly preserving fine-grained visual cues under strict token budgets while achieving SoTA performance on challenging multimodal benchmarks.

---


### 259. [GeoMix: Descriptor-Free Visual Localization via Global Context and Multi-Detector Training](https://arxiv.org/abs/2607.02486)

**<font color=#1a73e8>作者：</font>** Yejun Zhang, Xinjue Wang, Zihan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Descriptor-free visual localization eliminates high-dimensional descriptor storage, preserves scene privacy, and simplifies map maintenance, yet its accuracy still lags far behind descriptor-based pipelines. We identify this gap to insufficient geometric discriminability in geometry-only matching. Without visual appearance, current methods underutilize local geometry cues, lack the global context among keypoints, and overfit to a single keypoint detector. We further observe that descriptor-free matching naturally enables multi-detector training, as heterogeneous keypoints can be optimized in a shared geometry-only space without aligning descriptor spaces. Building on these insights, we propose GeoMix, a descriptor-free 2D-3D matching framework that strengthens geometric discriminability at three levels. Locally, directional and distance-aware embeddings enrich neighborhood aggregation with fine-grained spatial structure. Globally, learnable context nodes aggregate and redistribute scene-wide information via cross-attention to resolve ambiguities beyond local receptive fields. At the training level, Mix-Training exploits this detector-agnostic geometry space to learn representations across multiple keypoint detectors. Extensive experiments on MegaDepth, Cambridge Landmarks, 7Scenes, and Aachen Day-Night show that GeoMix sets a new state of the art among descriptor-free methods, reducing 75th-percentile rotation error by 89\% and translation error by up to 90\% over the previous best, while generalizing zero-shot to unseen detectors and narrowing the gap to descriptor-based pipelines. Code is available at $\href{this https URL}{\text{this links}}$.

---


### 260. [Towards Robustness against Typographic Attack with Training-free Concept Localization](https://arxiv.org/abs/2607.02494)

**<font color=#1a73e8>作者：</font>** Bohan Liu, Wenqian Ye, Guangzhi Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Models trained via Contrastive Language-Image Pretraining (CLIP) serve as the foundational vision encoders for most modern Large Vision Language Models (LVLMs). Despite their widespread adoption, CLIP models exhibit a critical yet underexplored failure mode: irrelevant text appearing within images confounds visual representations, biasing them toward lexical meaning rather than true visual semantics. This robustness issue, commonly described as a Typographic Attack (TA), exposes a vulnerability that poses a significant risk to safety-critical applications such as autonomous driving. To achieve interpretable and effective robustness against TA, we propose a novel, training-free mechanistic interpretability method. Our method provides sampling-based interpretations of hidden state representations and quantitatively attributes semantic versus lexical focus to individual attention heads. Through probabilistic analysis and circuit mining, we isolate specific Vision Transformer (ViT) components that disproportionately encode lexical information, thereby identifying the mechanistic source of TA. We further show that simple interventions applied directly to the identified circuits, without any additional training, can substantially improve robustness against Typographic Attacks in object classification. These interventions, such as selective adjustment of attention weights, also outperform both supervised and training-free defense methods. Our experiments demonstrate that applying the proposed intervention to the vision encoders of several state-of-the-art LVLMs yields substantial gains in Visual Question Answering accuracy under Typographic Attack interference on RIO-Bench. These results confirm both the efficacy and the generalizability of our mechanistic approach. Code is released at this https URL.

---


### 261. [Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials](https://arxiv.org/abs/2607.02499)

**<font color=#1a73e8>作者：</font>** Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning interatomic potentials (MLIPs) have become a hallmark of AI for scientific simulation. While efforts on new architectures and datasets have led to increasingly accurate and general models, the choice of optimizer for training has largely remained unexplored, defaulting to Adam and its variants in the community. Here, we implement and systematically compare a class of recently proposed matrix-structured optimizers, including Muon, SOAP, and the hybrid SOAP-Muon, for training NequIP and Allegro MLIP models. We find that these optimizers can substantially outperform Adam in both convergence speed and final accuracy. SOAP and SOAP-Muon emerge as robust and consistently strong methods, while Muon only provides partial gains relative to Adam. The improvements are particularly pronounced under partial force supervision. Our results indicate that optimizer choice is an overlooked yet impactful design axis for MLIPs.

---


### 262. [DemoPSD: Disagreement-Modulated Policy Self-Distillation](https://arxiv.org/abs/2607.02502)

**<font color=#1a73e8>作者：</font>** Yunhe Li, Hao Shi, Wenhao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamental issue: *privileged information leakage*, where the student encodes answer-dependent shortcuts that are unavailable at test time. We introduce **DemoPSD**, a novel framework that resolves such problems through the idea of *selective adoption of teacher guidance*. Instead of fitting the full teacher distribution, DemoPSD steers the student toward a *reverse-KL barycenter target*, a weighted geometric combination of the teacher and student distributions, that naturally balances learning from the teacher with preserving the student's own reasoning capacity. We measure the difference between their distributions and use such a discrepancy to adaptively control the blending at each token position. We provably show that DemoPSD achieves **(1)** *leakage attenuation*, i.e., effective mitigation of privileged information leakage; and **(2)** *exploration preservation*, i.e., preservation of exploration capacity under dense token-level distillation. Extensive experiments on SciKnowEval across four scientific fields show that DemoPSD outperforms both GRPO and SDPO while maintaining higher training entropy and robustly generalizing to out-of-distribution GPQA benchmarks.

---


### 263. [From SRA to Self-Flow: Data Augmentation or Self-Supervision?](https://arxiv.org/abs/2607.02508)

**<font color=#1a73e8>作者：</font>** Dengyang Jiang, Mengmeng Wang, Harry Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different noise levels, where cleaner tokens help infer noisier ones. In this work, we revisit this explanation and ask whether the gain instead comes from data augmentation along the noise dimension. To disentangle these factors, we introduce Attention Separation, which preserves the same dual-timestep input as Self-Flow while blocking attention between tokens assigned to different noise levels. Surprisingly, removing such interaction does not degrade performance and can even improve it, suggesting that the improvement from SRA to Self-Flow mainly comes from data augmentation. Furthermore,We show that Attention Separation itself provides an augmentation effect by splitting a single image into multiple effective training parts to expand the training data. Based on these observations, we combine self-representation alignment with dual-timestep and attention-separation augmentation, and demonstrate the effectiveness of this design on ImageNet.

---


### 264. [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514)

**<font color=#1a73e8>作者：</font>** Josh Hills, Ida Caspary, Asa Cooper Stickland  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterative VibeCoding, a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task. Our benchmark includes two task families: CLI tools and Flask web services, across 20 total task variations. We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. No single monitor is robust to both: which strategy evades best (success while evading the monitor) depends on the monitor type, so a defender cannot close off both gradual and non-gradual attacks with any one monitor. High evasion (>= 65%) generalizes across model attack agent backends (Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5), confirming this is a property of the persistent-state attack surface rather than a single model's capability. Evasion also remains high across state-of-the-art monitor models and the gap between gradual and non-gradual evasion widens for more capable models. We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. On both task families, it detects gradual attacks substantially better than diff monitors that merely see more accumulated history. Combining this stronger monitor with trajectory monitors in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%.

---


### 265. [PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation](https://arxiv.org/abs/2607.02515)

**<font color=#1a73e8>作者：</font>** Haofei Xu, Rundi Wu, Philipp Henzler 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre-trained DINOv3. Unlike existing latent diffusion approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers. Despite its simplicity, our approach surpasses complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives. Notably, it produces sharper geometric structure and is more robust in highly ambiguous regions, such as transparent objects.

---


### 266. [WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory](https://arxiv.org/abs/2607.02517)

**<font color=#1a73e8>作者：</font>** Hanlin Wang, Hao Ouyang, Qiuyu Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present WorldDirector, a highly controllable video world model framework designed for persistent dynamic object memory and unrestricted viewpoint exploration. Unlike existing world models that entangle physical dynamics with pixel rendering and rely on continuous visual observation to sustain motion, our framework explicitly decouples semantic motion orchestration from visual generation. By leveraging an LLM to coordinate 3D trajectories with camera movements and subsequently employing these orchestrated trajectories as control signals for video generation, our approach ensures strict physical logic and appearance stability, successfully preserving the exact visual identities of dynamic entities even when they re-enter the scene after prolonged periods out of view. Experimental results demonstrate that our method supports the synthesis of complex and extended events with unprecedented controllability and persistent dynamic object memory. Project Page: this https URL

---


> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
