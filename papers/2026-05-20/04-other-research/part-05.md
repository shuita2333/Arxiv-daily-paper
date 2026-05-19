# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 201. [OmniVL-Guard Pro: A Tool-Augmented Agent for Omnibus Vision-Language Forensics](https://arxiv.org/abs/2605.16962)

**<font color=#1a73e8>作者：</font>** Jinjie Shen, Zheng Huang, Yuchen Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vision-language forgery detection and grounding methods operate under a closed-world paradigm, assuming verification can be completed by the model alone. However, self-contained MLLMs are constrained by finite parametric knowledge, static training corpora, and limited perceptual resolution, creating a practical ceiling in dynamic open-world forensics -- particularly for real-time event verification requiring external clues and forgery segmentation demanding fine-grained scrutiny of local manipulations. To address these limitations, we shift from scaling up the self-contained model toward reaching beyond it. We propose \textbf{OmniVL-Guard Pro}, a tool-augmented agent that extends unified forensics from closed-world prediction to open-world clues-driven reasoning. OmniVL-Guard Pro integrates a tool environment spanning real-time event search, local cropping and zooming, edge-anomaly screening, face detection, video frame extraction, and SAM3-based segmentation. To generate high-quality tool-reasoning trajectories, we introduce \textbf{Tree-Structured Self-Evolving Tool Trajectory Generation}, which produces diverse trajectories through seed guidance, guider-free self-evolution, and weakly-hinted hard sample synthesis, yielding the Full-Spectrum Tool Reasoning (FSTR) dataset for training. We further propose \textbf{Checker-Guided Agentic Reinforcement Learning} (CGARL), which provides process-level supervision to penalize cases where the answer is correct but the reasoning is distorted. Extensive experiments demonstrate that OmniVL-Guard Pro achieves state-of-the-art performance across various tasks, and exhibits strong zero-shot generalization. The FSTR dataset and code for OmniVL-Guard Pro will be publicly released at \url{this https URL}.

---


### 202. [Harnessing AI for Inverse Partial Differential Equation Problems: Past, Present, and Prospects](https://arxiv.org/abs/2605.16966)

**<font color=#1a73e8>作者：</font>** Zhentao Tan, Yuze Hao, Boyi Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving inverse partial differential equation (PDE) problems is a fundamental topic in scientific research due to its broad significance across a wide range of real-world applications. Inverse PDE problems arise across medical imaging, geophysics, materials science, and aerodynamics, where the goal is to infer hidden causes, design structures, or control physical states. In this paper, we provide a comprehensive review of recent advances in solving inverse PDE problems using artificial intelligence (AI). We first introduce the basic formulation, key challenges, and traditional numerical foundations of inverse PDE problems, and then organize it into three major categories: inverse problems, inverse design, and control problems. For each category, we further present a methodological paradigms, and review representative state-of-the-art approaches from recent years. We then summarize representative applications across scientific and industrial domains, including mechanical systems, aerodynamic problems, thermal systems, full-waveform inversion, system identification, and medical imaging. Finally, we discuss open challenges and future prospects, such as physics-informed architectures, limited real-world data, uncertainty quantification, and inverse foundation models. This survey aims to provide the first unified and systematic perspective on AI for inverse PDE problems, demonstrating how modern learning-based methods are reshaping inverse problems, inverse design, and control problems in PDE-governed systems.

---


### 203. [Expandable, Compressible, Mineable: Open-World Thermal Image Restoration](https://arxiv.org/abs/2605.16967)

**<font color=#1a73e8>作者：</font>** Pu Li, Huafeng Li, Yafei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In open-world settings, thermal infrared (TIR) image degradations continuously emerge and evolve, while most existing all-in-one restoration methods are built on a closed-set assumption and struggle to continually adapt to novel degradations. To address this, we propose ECMRNet, an Expandable, Compressible, and Mineable Restoration Network for open-world TIR restoration from a continual learning perspective. Conceptually, ECMRNet unifies continual degradation learning as an "expand-compress-mine" closed-loop process, enabling sustained adaptation to new degradations with controllable evolution. Structurally, ECMRNet decomposes intermediate representations into group-isolated subspaces, and achieves strict parameter isolation and fast adaptation to new degradations by freezing historical groups and isomorphically expanding new ones. To curb model growth as tasks accumulate, we present Structural Entropy Pruning, which identifies and removes redundant channel groups via two-dimensional structural entropy minimization, achieving information contribution-driven adaptive compression. Moreover, we design a Sub-degradation Knowledge Mining Module that dynamically retrieves and recombines transferable components from historical representations to improve restoration under compound degradations. Experimental results demonstrate that ECMRNet achieves superior overall performance across diverse single and compound degradations while using fewer parameters and lower computational cost. The source code is available at this https URL.

---


### 204. [Brain Vascular Age Prediction Using Cerebral Blood Flow Velocity and Machine Learning Algorithms](https://arxiv.org/abs/2605.16969)

**<font color=#1a73e8>作者：</font>** Anni Zhao, Alex Bateh, Tyler Baldridge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Defining vascular age in terms of physiological function has become one focal point of the extensive studies to categorize and track chronological age. Transcranial Doppler (TCD) is a method by which cerebral blood flow velocity is measured along the major arteries feeding the human brain. This study aims to use features extracted from TCD to estimate chronological age and assess accelerated aging in subjects with various brain diseases. We predict subjects with various brain diseases to present with accelerated cerebrovascular aging when tested on various regression models trained by healthy subjects. 168 healthy subjects and 277 diseased subjects with bilateral TCD recordings of the middle cerebral artery were analyzed using the Morphological Analysis and Clustering of Intracranial Pressure (MOCAIP) algorithm. MOCAIP-generated features and heart rate variability features were used as input features for regression models to predict the brain vascular age. 66 subjects with acute stroke, 27 subjects with post stroke, 26 subjects with Alzheimer's disease, 23 subjects with mild cognitive impairment, and 135 established subjects were tested against the machine learning model to assess for accelerated cerebrovascular age. The trained model, on average, predicted healthy subjects' cerebrovascular age to be 3.69 years above their chronological age. Subjects with different disease conditions exhibited varying levels of age acceleration. The differences in healthy and diseased subjects' performances suggest that features generated using TCD may be relevant when evaluating accelerated cerebrovascular aging. Moreover, imbalanced datasets have been observed to affect the performance of machine-learning-based brain age prediction models.

---


### 205. [Statistical Hand Shape Modeling from Clinical CT Scans Using Deep Learning and Implicit Skinning](https://arxiv.org/abs/2605.16980)

**<font color=#1a73e8>作者：</font>** Gokce Guven, Hasan Fehmi Ates, Deniz Karasahin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation and statistical shape modeling of hand anatomy have significant implications for medical diagnostics, ergonomics, and biomechanics. This study proposes an AI-assisted reconstruction pipeline for segmenting and analyzing hand anatomy from 1,271 elbow-to-hand (e2h-CT) computed tomography scans. A Pix2Pix-based conditional generative adversarial network is first employed to remove plaster cast and background artifacts from CT volumes. The cleaned scans are then processed in 3D Slicer to extract skin and bone masks, which are converted into closed-surface mesh models. Segmented bone meshes are used to construct skeletal representations, enabling implicit skinning to align all hand models into a standardized anatomical configuration. Subsequently, non-rigid registration is performed on the hand skin surfaces using the Geodesic Based Coherent Point Drift++ (GBCPD++) algorithm to establish point-wise correspondence across subjects. Principal Component Analysis (PCA) is then applied to the registered models to quantify anatomical shape variability. The Pix2Pix preprocessing stage achieved a Dice coefficient of 0.9856 and an IoU of 0.9720 on the held-out test set. Statistical modeling was performed on a subset of 90 scans in which the fingers were fully visible and anatomically separated. The resulting statistical shape distributions demonstrate strong agreement with the U.S. Army Anthropometric Survey (ANSUR II), supporting the anatomical validity of the reconstructed models. The proposed methodology demonstrates significant potential for advancing biomechanical modeling, ergonomic optimization, prosthetic design, and precision medical diagnostics.

---


### 206. [Rethinking the State Update Gate for Long-Sequence Recurrent 3D Reconstruction](https://arxiv.org/abs/2605.16981)

**<font color=#1a73e8>作者：</font>** Kejun Ren, Lei Jin, Tianxin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction under a strict constant-memory budget hinges on how the recurrent state is updated as the stream evolves. We profile TTT3R-style per-token gates across five benchmarks and discover a structural bottleneck: the gate is intrinsically bounded in magnitude (median $0.31$; never exceeding $0.6$) and nearly frame-invariant, yielding an effective memory horizon of only $\sim$3 frames per state token, which serves as the structural origin of long-sequence drift. We trace this to a missing axis: existing inference-time methods modulate updates only at the per-token, intra-frame level, while the orthogonal frame-level question of \emph{how strongly each frame should contribute to the state} has been treated as content-independent. We close this gap with a scalar frame-level gate $\alpha_t \in (0, 1]$ derived in closed form from frame-to-frame changes of internal features -- a continuous relaxation of classical Simultaneous Localization and Mapping (SLAM) keyframe selection that requires no parameters, no training, and no extra forward pass. Across six benchmarks spanning camera pose, video depth, and 3D reconstruction at sequence lengths up to $4,541$ frames, our gate cuts ATE by $51\%$ on long TUM-RGBD pose sequences, reduces AbsRel by $12.8\%$ on Bonn video depth, and on KITTI long-sequence pose estimation surpasses both LongStream and Keyframe-VO, while retaining strictly constant memory at zero training cost.

---


### 207. [Decision-Aware Proximal Bridge Learning for Optimal Treatment Selection](https://arxiv.org/abs/2605.16989)

**<font color=#1a73e8>作者：</font>** Tomàs Garriga, Alejandro Almodóvar, Axel Brando 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individualized treatment selection with continuous actions requires accurate causal response estimation in decision-relevant regions, rather than uniformly over the entire action space. Estimating a global causal response surface and then choosing the treatment that maximizes it can therefore be suboptimal, since standard estimation objectives allocate modeling effort according to the observed treatment distribution rather than the regions that determine the optimal decision. While decision-aware approaches have been studied in unconfounded settings, this problem remains underexplored in proximal causal inference, where proxy variables and bridge functions enable identification under suitable assumptions even in the presence of hidden confounding. Despite recent progress, proximal methods have primarily focused on treatment-effect and potential-outcome estimation rather than treatment selection and optimal decision-making. To bridge this gap, we introduce a policy-targeted weighted bridge loss that emphasizes decision-relevant treatment regions while retaining global stabilization. We prove a regret bound showing that the proposed weighted bridge loss controls treatment-selection regret through a weighted ill-posedness constant. We instantiate the framework in decision-aware variants of several proximal bridge solvers, yielding practical algorithms that alternate between weighted bridge estimation, response-surface projection, policy update, and weight refinement. Empirically, we find that decision-aware weighting reduces regret across several bridge solvers, suggesting improved treatment selection in proximal settings.

---


### 208. [DreamEdit3D: Personalization of Multi-View Diffusion Models for 3D Editing](https://arxiv.org/abs/2605.16990)

**<font color=#1a73e8>作者：</font>** Jinxin Ai, Matthias Nießner, Ziya Erkoç  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 2D diffusion models have achieved remarkable success in identity-preserving personalization, extending this capability to 3D assets remains a significant challenge due to the complexities of multi-view consistency and spatial control. Inspired by these 2D advancements, we present a novel personalization method for text-guided 3D editing that enables compositional, object-level control through natural language. Given a 3D input, we render orthogonal views and extract object-level segmentation masks to isolate semantic components. We then learn distinct token embeddings for each component through a tailored two-phase optimization strategy: multi-view textual inversion with attention alignment, followed by full fine-tuning of multi-view diffusion model. During inference, these disentangled tokens seamlessly compose with editing prompts to generate multi-view consistent images, which are subsequently lifted into high-fidelity textured 3D meshes. Extensive evaluations across diverse editing scenarios demonstrate that our method successfully transfers the flexibility of 2D personalization to 3D, achieving state-of-the-art edit faithfulness and identity preservation compared to existing baselines.

---


### 209. [Response-free item difficulty modelling for multiple-choice items with fine-tuned transformers: Component-wise representation and multi-task learning](https://arxiv.org/abs/2605.16991)

**<font color=#1a73e8>作者：</font>** Jan Netík, Patrícia Martinková  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Response-free item difficulty modelling promises to reduce reliance on response-based calibration but is intrinsically difficult on reading-comprehension multiple-choice items, where difficulty depends on inferential demands across wording components. Whereas most existing approaches extract item-text features and pass them to a separate statistical or machine-learning model, we fine-tune transformer encoders end-to-end on the item wording, eliminating the manual feature engineering and preprocessing that discards information. Moreover, two extensions to this joint-encoding approach are proposed: a component-wise variant that encodes wording components separately through a shared encoder, and a multi-task variant that retains joint encoding and adds an auxiliary multiple-choice question answering objective on the shared encoder. Each method is evaluated under a Monte Carlo subsampling design at three training-set sizes on a held-out test set. We find that joint encoding is a viable end-to-end alternative to feature-engineering pipelines; while the component-wise variant shows no detectable benefit, consistent with self-attention already harvesting the cross-component signal, the multi-task variant delivers significant paired improvements in the smallest-sample regime. Transformer fine-tuning, especially if regularised by a suitable auxiliary task, recovers a substantial share of the wording-derivable signal at training-set sizes typical of applied measurement. The framework provides a customisable interface for psychometrically motivated extensions.

---


### 210. [RHINO: Reconstructing Human Interactions with Novel Objects from Monocular Videos](https://arxiv.org/abs/2605.17014)

**<font color=#1a73e8>作者：</font>** Lixin Xue, Chengwei Zheng, Georgios Paschalidis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing people, objects, and their interactions in 3D is a long-standing goal for intelligent systems. Often the input is RGB video from a moving camera, making the task ill-posed; depth is ambiguous, humans and objects occlude each other, and camera and object motion entangle to create apparent motion. Most prior work addresses humans or objects in isolation, ignoring their interplay, or assumes known 3D shapes or cameras, which is impractical for real-world applications. We develop RHINO (Reconstructing Human Interactions with Novel Objects), a three-step framework that recovers in 3D a human, novel (unseen) manipulated object, and static scene in a common world frame from a monocular RGB video. First, we leverage 3D-aware foundation models to obtain cues that stabilize Structure-from-Motion (SfM) even for low-texture regions; this yields a coarse shape and apparent motion of a manipulated object from foreground pixels, and a coarse scene shape and camera motion from background pixels. Second, we estimate a human in the camera frame via an off-the-shelf method, and subtract the camera motion from apparent motion to extract the object motion; this registers the human, object, and coarse scene shapes into a common world frame. Third, we refine shapes using a compositional neural field with per-component signed-distance fields. The latter further enables differentiable contact priors that attract surfaces while penalizing interpenetration, improving the physical plausibility of the final reconstruction. For evaluation, we capture a new dataset of handheld monocular videos synchronized with a volumetric 4D capture stage, providing ground-truth shape and camera motion. RHINO outperforms state-of-the-art baselines on novel-view synthesis and 4D reconstruction. Ablations show that each stage contributes substantially. Code and data are available at this https URL.

---


### 211. [StreamingEffect: Real-Time Human-Centric Video Effect Generation](https://arxiv.org/abs/2605.17019)

**<font color=#1a73e8>作者：</font>** Yiren Song, Cheng Liu, Yuxin Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video effect generation is highly desirable for live human-centric applications such as e-commerce streaming, entertainment, and vlogging, yet remains difficult due to the lack of suitable data and deployable editing models. Unlike generic video generation, this task requires real-time video-to-video editing that adds expressive effects while preserving human identity, background content, and temporal consistency. Existing acceleration efforts mainly focus on text-to-video generation, while efficient distillation for video editing remains largely underexplored. In this paper, we present \textbf{StreamingEffect}, a real-time human-centric streaming video effect framework. We adopt an in-context video editing architecture and train a high-quality bidirectional teacher, then distill it into a causal autoregressive student and further reduce sampling from 50 steps to 4 steps. We also introduce keyframe control, allowing reference effect frames to be injected online and propagated through the stream for interactive editing. To address the data bottleneck, we construct \textbf{VideoEffect-130K}, to our knowledge the largest human-centric video effect dataset, containing 70K effect videos and 60K editing videos across 600 effect categories curated from short-video and editing platforms. Experiments show that our method enables real-time, high-quality 720p video editing on a single H200 GPU.

---


### 212. [A Conflict-aware Evidential Framework for Reliable Sleep Stage Classification](https://arxiv.org/abs/2605.17021)

**<font color=#1a73e8>作者：</font>** Yunzhi Tian, Dekui Wang, Qirong Bu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-view learning has been widely applied for sleep stage classification using multi-modal data. However, existing methods typically assume that different modalities are well-aligned, which is often unattainable in real-world scenarios, thereby compromising the reliability of the staging results. In this paper, we propose ConfSleepNet, a conflict-aware evidential framework that dynamically resolves inter-view conflicts. The framework consists of multi-view evidence extraction and conflict-aware aggregation. In the first phase, it learns category-related evidence from different modalities, which represents the degree of support for individual sleep stages. Considering the inherent characteristics of varying modalities, we propose hybrid category structures for different modalities to promote more reasonable evidence learning. In the second phase, view-specific opinions, including prediction results and uncertainty, are constructed from the learned evidence. Notably, we propose a novel conflict-aware aggregation method that integrates these view-specific opinions into a reliable joint decision. This mechanism can effectively resolve conflicts among opinions and synthesize them into a reliable joint decision. Both theoretical analysis and experimental results demonstrate the effectiveness of ConfSleepNet in sleep staging tasks. The code is available at this https URL.

---


### 213. [PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts](https://arxiv.org/abs/2605.17028)

**<font color=#1a73e8>作者：</font>** Khizar Hussain, Murat Kantarcioglu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) hallucinate with confidence: their outputs can be fluent, authoritative, and simply wrong. In medical, legal, and scientific applications this failure causes direct harm, and detecting it from internal model states offers a path to safer deployment. A growing body of work reports that this problem is increasingly tractable, with recent methods achieving high detection performance on widely used benchmarks. We show, however, that much of this apparent progress does not survive scrutiny. Four of the six corpora embed the ground-truth answer directly in the input prompt. A naïve text-similarity baseline we call \textsc{TxTemb} exploits this to achieve near-perfect detection scores without any access to model internals. To measure what genuine detection capability remains once these artifacts are controlled, we conduct a large-scale evaluation spanning twenty-two detection methods, twelve open-source models spanning six architectural families, and six corpora. We further introduce \textbf{DRIFT}, a supervised probe over inter-layer hidden-state transitions, as a point of comparison for live-generation detection. Our findings suggest that the field's reported progress on hallucination detection is substantially explained by benchmark construction artifacts in widely used corpora, and that the majority of established baselines perform near chance under controlled conditions; the consistent exceptions are SAPLMA and DRIFT, both supervised probes on upper-layer hidden states.

---


### 214. [D$^2$Evo: Dual Difficulty-Aware Self-Evolution for Data-Efficient Reinforcement Learning](https://arxiv.org/abs/2605.17037)

**<font color=#1a73e8>作者：</font>** Ru Zhang, Renda Li, Ziyu Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has demonstrated potential for enhancing reasoning in large language models (LLMs). However, effective RL training, which requires medium-difficulty training samples, faces two fundamental challenges: Effective Data Scarcity and Dynamic Difficulty Shifts, where medium-difficulty samples are scarce and become trivial as models improve. Existing methods mitigate this scarcity to some extent by generating training samples. However, these approaches suffer from anchor-free generation, ignoring co-evolution, and difficulty mismatch. To address these issues, we propose D$^2$Evo, a Dual Difficulty-aware self-Evolution RL framework. In each iteration, our method mines medium-difficulty anchors based on the current Solver's capability, trains the Questioner to generate diverse questions at appropriate difficulty levels, and jointly optimizes both components to enable progressive reasoning gains. Extensive experiments demonstrate that D$^2$Evo outperforms existing methods on mathematical reasoning benchmarks with fewer than 2K real mathematical samples, and exhibits strong generalization on general reasoning benchmarks.

---


### 215. [Evidential Information Fusion on Possibilistic Structure](https://arxiv.org/abs/2605.17038)

**<font color=#1a73e8>作者：</font>** Qianli Zhou, Ye Cui, Zhen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dempster's rule is a fundamental tool for combining belief functions from distinct and reliable sources. However, its intersection-based semantics imposes strong structural restrictions, which limits its flexibility in handling complex source states and diverse information fusion scenarios. To overcome this limitation, we propose a reversible transformation, derived from the isopignistic principle, between belief functions and a possibilistic structure defined on the power set. In this transformation, the relationships among subsets are explicitly characterized by a belief evolution network, which provides a more flexible representation of evidential information beyond the conventional mass function structure. On this basis, we further introduce the triangular norm family to develop a general and adaptive evidential information fusion framework. Unlike fusion methods rooted in Dempster semantics, the proposed framework supports more flexible combination behaviors and exhibits advantages in non-distinct source fusion, conflict management, parametric combination design, and heterogeneous information fusion.

---


### 216. [Privacy-Preserving Generation Fraud Detection for Distributed Photovoltaic Systems: A Solar Irradiance-Fused Federated Learning Framework](https://arxiv.org/abs/2605.17039)

**<font color=#1a73e8>作者：</font>** Xiaolu Chen, Chenghao Huang, Yanru Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The wide adoption of residential photovoltaic (PV) systems introduces new challenges for generation fraud detection (FD). Unlike traditional electricity theft detection, which focuses on electricity consumption-side behavior, PV generation fraud detection (PVG-FD) is complicated by the inherent intermittency and uncertainty of PV generation. The distributed nature of PV systems poses further challenges for centralized PVG-FD approaches due to scalability and privacy concerns. This paper develops a privacy-preserving distributed PVG-FD framework based on federated learning (FL). In this framework, a utility company manages multiple household communities, where each of which is equipped with a local detector. The framework integrates a novel detection model architecture with privacy-preserving global collaboration. Each community's local model fuses PV generation and weather data via a co-attention mechanism to detect discrepancies critical for PVG-FD. The FL framework enables cross-community collaboration by aggregating model parameters and prototypes, leveraging global knowledge sharing with local refinement while preserving privacy. It also uses prototype alignment to address class imbalance by enhancing fraud sample representation. Extensive experiments on a real-world residential PV dataset validate the effectiveness of the developed method and demonstrate that it outperforms state-of-the-art FL methods across various scenarios. The results also show its scalability across varying community sizes and strong robustness to class imbalance.

---


### 217. [Thermal-Only Crowd Counting with Deployment-Time Privacy Protection](https://arxiv.org/abs/2605.17042)

**<font color=#1a73e8>作者：</font>** Yifei Qian, Zhongliang Guo, Chun Tong Lei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While RGB-Thermal crowd counting has shown promise, the paradigm faces critical limitations: RGB data raises privacy concerns in public surveillance, and multi-modal misalignment degrades fusion performance. We propose the first thermal-only framework specifically designed for privacy-conscious crowd counting, eliminating RGB dependency at inference time and substantially reducing the privacy exposure associated with continuous RGB capture in public surveillance deployments. To mitigate thermal ambiguity, we leverage depth-to-RGB diffusion models as a cross-modal bridge, extracting discriminative features that enhance thermal representations. Critically, we demonstrate that single-step LCM denoising yields features most faithful to the structural content of the depth conditioning signal, while multi-step approaches progressively decouple features from the conditioning input and accumulate errors that degrade counting accuracy. Experiments on RGBT-CC and DroneRGBT datasets show our method achieves competitive performance against state-of-the-art RGB-T fusion methods, while requiring only thermal input during inference, eliminating the need for continuous RGB capture that constitutes the primary privacy concern in real-world surveillance deployment. The code will be made publicly available.

---


### 218. [Learning Multi-Timescale Abstractions for Hierarchical Combinatorial Planning](https://arxiv.org/abs/2605.17058)

**<font color=#1a73e8>作者：</font>** Vivienne Huiling Wang, Tinghuai Wang, Joni Pajarinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The combination of exponentially large action spaces, stochastic dynamics, and long-horizon decision-making under limited resources makes Sequential Stochastic Combinatorial Optimization (SSCO) particularly challenging for reinforcement learning. Hierarchical Reinforcement Learning (HRL) offers a natural decomposition, but it places the high-level policy in a Semi-Markov Decision Process (SMDP) where actions have variable durations, making it difficult to learn a world model that is suitable for planning. We introduce a model-based hierarchical framework for sequential stochastic combinatorial decision-making that directly addresses this issue. Our method combines a latent-space tree-search planner with an SMDP-aware world model for variable-duration decisions. A multi-timescale objective structures the latent dynamics so that transition magnitudes reflect the effective temporal scales of abstract actions, enabling efficient lookahead under adaptive temporal abstraction. We further learn a subgoal-conditioned budget policy jointly with the world model to support context-aware resource allocation. Across challenging SSCO benchmarks, our method outperforms strong baselines.

---


### 219. [quantum-safe: Bridging the Post-Quantum Production Gap with a Hybrid-by-Default Python Cryptography Library](https://arxiv.org/abs/2605.17061)

**<font color=#1a73e8>作者：</font>** Animesh Shaw  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The August 2024 finalisation of FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA) closed the algorithmic gap in post-quantum cryptography (PQC). The production gap -- hybrid combiners, versioned key formats, protocol helpers, and migration tooling -- remains open. We present quantum-safe, a Python library that closes all three critical gaps we identify, and a systematic evaluation of the nine-library ecosystem that quantifies them.
We score nine PQC libraries across eight production-readiness dimensions. Three dimensions have coverage below 35%: hybrid KEM support (11%), migration tooling (22%), and protocol integration (33%). quantum-safe scores Full on all eight. The full API reduces the hybrid KEM task from 45 lines of manual combiner code to three lines, directly lowering the risk of insecure combiner implementations.
We report the first statistically rigorous per-operation overhead measurement for a Python hybrid PQC library (3,000 iterations, CPU-pinned, bootstrapped 95% confidence intervals). A full X25519 + ML-KEM-768 handshake completes in 243 {\mu}s under Docker/Linux -- 0.5--2.5% of a typical TLS 1.3 round-trip budget. At 5,000 concurrent users, throughput holds at 2,848 ops/s with only 4.9% degradation versus the single-user baseline, confirming that liboqs releases the Python GIL during C-level operations.
We introduce Coefficient of Variation (CoV) as a practical timing side-channel proxy across all FIPS 203/204 operations. ML-KEM-768 decapsulation achieves CoV = 3.9%, within the AES-256-GCM noise floor (2.1%). ML-DSA-65 signing shows CoV = 51.5%, expected from FIPS 204 rejection sampling, not a side-channel. This CoV methodology has not previously been applied to PQC library evaluation and provides a lightweight complement to formal constant-time verification tools. All results are reproducible via a single Docker command.

---


### 220. [AnchorDiff: Topology-Aware Masked Diffusion with Confidence-based Rewriting for Radiology Report Generation](https://arxiv.org/abs/2605.17071)

**<font color=#1a73e8>作者：</font>** Shiying Yu, Jielei Wang, Guoming Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) aims to automatically produce clinically accurate textual reports from medical images. Existing methods predominantly rely on autoregressive (AR) language models, whose causal dependency structure restricts generation to a unidirectional left-to-right process. This paradigm can induce sequence bias, where models tend to follow stereotypical token orders and high-frequency report templates rather than fully grounding generation in image-specific evidence. In this paper, we propose AnchorDiff, the first masked-diffusion framework for RRG that integrates knowledge-graph-derived clinical anchors into diffusion language modeling. By leveraging bidirectional context and iterative refinement, AnchorDiff mitigates the limitations of fixed-order autoregressive decoding. Specifically, we introduce a topology-aware training strategy that uses RadGraph-derived entity hierarchies to assign clinically important tokens differentiated masking protection and loss weights. We further design an inference-time rewriting strategy that detects unstable committed tokens through perturbation-based testing and selectively revises them during denoising. Extensive experiments on the MIMIC-CXR and MIMIC-RG4 benchmarks demonstrate that AnchorDiff achieves state-of-the-art (SOTA) performance, showing the effectiveness of clinically anchored masked diffusion for radiology report generation.

---


### 221. [The Learnability Gap in Medical Latent Diffusion](https://arxiv.org/abs/2605.17087)

**<font color=#1a73e8>作者：</font>** Mischa Dombrowski, Felix Nützel, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative data augmentation with latent diffusion models is a promising strategy for addressing class imbalance in medical imaging, yet current approaches focus on perceptual fidelity and domain-specific autoencoder fine-tuning while neglecting a more fundamental bottleneck. We identify and formalize the learnability gap: large-scale pretrained autoencoders faithfully encode discriminative features for medical classification, as evidenced by near-lossless performance in reconstruction space, yet their latent representations are structured in ways that are difficult for classifiers to learn from. Across five autoencoder families and four medical benchmarks spanning chest radiography, dermatoscopy, computed tomography, and echocardiography, we show that this gap persists regardless of architecture, initialization strategy, or hyperparameter tuning, and that medical-domain fine-tuning of the autoencoder does not close it. To probe and partially narrow the gap, we develop noise-conditioned latent classifiers with FiLM layers and image-space distillation that offer 64x throughput and 120x memory gains over image-space models while serving as diagnostic tools for latent space quality. Our analysis provides a new framework for evaluating autoencoder latent spaces and identifies their structure, rather than their fidelity or domain specificity, as the primary obstacle to closing the performance gap between real and synthetic medical training data.

---


### 222. [Mechanism Learning: Prototype-Anchored Mechanism Inference for Scientific Forecasting](https://arxiv.org/abs/2605.17091)

**<font color=#1a73e8>作者：</font>** Qian Jiang, Liping Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific forecasting typically relies on direct state prediction, an approach that grows brittle under data scarcity, extended horizons, non-stationary dynamics, or high-dimensional complexity. While raw state trajectories are highly sensitive in these regimes, underlying local evolution rules often exhibit robust reusability. We introduce mechanism learning, a framework that forecasts future states by estimating the currently active local mechanism. Our method compresses local spatiotemporal fragments into mechanism descriptors, forming a data-driven, structured mechanism space where proximity reflects similar local evolution rules. To ground these estimates in observed data, we utilize prototype anchors, a set of representative mechanisms that sparsely cover the space of local rules. We evaluate this approach on Burgers dynamics, WeatherBench2, and Lorenz96. Empirically, the learned mechanism spaces resist collapse and maintain strong local consistency. Compared to direct prediction and other models including FNO, NODE, LSTM, and reservoir-family methods, our framework demonstrates predictive gains in fragile regimes: it significantly improves switching stability in Burgers dynamics and achieves state-of-the-art performance both under the scarce-data fixed-horizon WeatherBench2 protocol and in intermediate-complexity Lorenz96. Ablation studies and drift diagnostics confirm that these improvements are driven by finite prototype anchoring rather than sheer latent capacity. Together, these results establish mechanism learning as a principled, robust alternative to direct state prediction in forecasting complex systems.

---


### 223. [Visual Timelines of Police Encounters in Body-Worn Camera Footage: Operational Context and Activity Cataloging for Training and Analysis in OpenBWC](https://arxiv.org/abs/2605.17095)

**<font color=#1a73e8>作者：</font>** Angela Srbinovska, Christopher Homan, Adrian Martin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Law enforcement agencies are accumulating vast amounts of body-worn camera (BWC) footage. However, this remains operationally opaque. That is, analysts and trainers still have to invest considerable time watching full-length videos to pinpoint the start of key encounters and identify the points where activity shifts to something more physically intense. We present an approach to process BWC video into a time-aligned sequence of fixed-length 10-second windows, processed and labeled using a privacy-conscious protocol. Each window is labeled with two dimensions of information: (i) the operational context of the window and (ii) the level of motion intensity within the window, with low-evidence labels for windows for which insufficient evidence exists due to darkness, blur or occlusion. We train models to classify windows based on these two axes using frames sampled from each window encoded using CLIP model and aggregated into a window-level representation. We extract dense optical flow statistics for each window to capture motion intensity. On test windows the best context model achieves 78.75% accuracy, and the best-accuracy activity model achieves 88.33%. We also included integrity audits to show the results and how the visual timeline representations support faster incident review and make the officer training workflow more practical.

---


### 224. [Parallel Recursive LSTM](https://arxiv.org/abs/2605.17108)

**<font color=#1a73e8>作者：</font>** Tristan Gaudreault, Yongyi Mao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have become the dominant architecture for sequence modeling by using self-attention to enable expressive and highly parallel processing. However, the resulting quadratic time and memory costs limit efficiency in long-context settings. Recurrent models such as LSTMs provide explicit nonlinear state updates and strong state-tracking capabilities, yet their strictly sequential computation limits parallelism. We introduce the Parallel Recursive LSTM (PR-LSTM), a hierarchical recurrent architecture that replaces left-to-right recurrence with recursive nonlinear state composition over a balanced computation tree. Tokens are first mapped independently to latent states, which are then recursively merged by a learned gated composition block. This structure uses the reduction pattern underlying parallel scans as a fixed execution schedule, rather than assuming an associative recurrence. As a result, PR-LSTM retains nonlinear gated state representations while reducing recurrent parallel depth from linear to logarithmic. Empirically, PR-LSTM achieves strong sequence-length generalization on formal-language benchmarks, solving more tasks than standard RNN, LSTM, and Transformer baselines, while avoiding the quadratic scaling of attention. These results suggest that recurrent computation can be reorganized hierarchically to expose parallelism without restricting the transition dynamics to linear or associative forms.

---


### 225. [DynMuon: A Dynamic Spectral Shaping View of Muon](https://arxiv.org/abs/2605.17109)

**<font color=#1a73e8>作者：</font>** Fangzhou Wu, Rikhav Shah, Sandeep Silwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, Muon has emerged as the dominant method for training large language models, and transformers more broadly. The essential difference, when compared to standard gradient descent methods, is to replace the usual update matrix $M=U\Sigma V^\top$ with its polar factor $UV^\top$. In this work, we consider a class of Muon-like updates, where we replace the update $M$ with $U\Sigma^p V^\top$ for some parameter $p$. We call this a "spectral-shaping" operation, and develop a theory of how to pick $p$ which depends on (a) local curvature of the loss function, (b) noise stemming from stochastic gradients and label noise, and (c) training stage. Our theory and experimentation reveal a previously overlooked behavior: positive $p$ helps early by emphasizing high-curvature directions and accelerating signal contraction, while mildly negative $p$ helps later by reallocating update strength toward low-curvature directions that still contain useful training signals. Building on the insight, we propose DynMuon, an efficient dynamic spectral shaping method that schedules $p$ from positive to mildly negative over training. Extensive experiments across model sizes, architectures, and training settings show that DynMuon consistently achieves lower validation loss than Muon, while requiring 10.6-26.5% fewer steps to reach the same target loss.

---


### 226. [The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning](https://arxiv.org/abs/2605.17113)

**<font color=#1a73e8>作者：</font>** Scott Merrill, Shashank Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing deception datasets label completed outputs as honest or deceptive, treating deception as a property of the final response rather than a function of the model's reasoning trace. This obscures a more fundamental question: when does a language model become committed to deception? We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome. To scale this, we construct five environments (spanning strategic bluffing, maze guidance, financial advice, used-car sales, and offer negotiation) in which deception is never prompted but emerges from strategic incentives and labels follow mechanically from environment state rather than subjective human judgment. The resulting corpus localizes $\sim$1.46M sentences across four reasoning models, drawn from over 94.1M sampled continuations, 91.5B generated tokens, and over 100K scenarios. Sentence-level human evaluation confirms that detected commitment points correspond to interpretable shifts in decision state. Using this resource, we show that lexical cues for commitment prediction transfer poorly across environments, whereas attention-based transition features generalize out of distribution, suggesting that deceptive commitment is reflected in reusable changes in reasoning dynamics rather than surface form. We further identify compact attention-head sets (under 10% of heads) that, selected on one environment, causally suppress deceptive commitment across held-out environments. We release the corpus as a substrate for studying deception, and more broadly commitment, in language-model reasoning.

---


### 227. [Simple Power Analysis on Post-Quantum Code Based Cryptosystems](https://arxiv.org/abs/2605.17116)

**<font color=#1a73e8>作者：</font>** Konstantinos Spalas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-Quantum cryptography is about to substitute current cryptographic schemes as being resilient in attacks from quantum computers. McEleiece and Bit Flip Key Encapsulation (BIKE) are two delight representatives based on coding theory where classical structural attacks against these algorithms can be successfully phased out by selecting the appropriate key size. Using low cost equipment, the method of Simple Power Analysis (SPA) is used in this paper to evaluate whether or not there is significant information leakage during the decapsulation phase where the shared secret key is generated. Executing a related experiment it is shown that correlation between electromagnetic emissions and secret values exists. In the aftermath, with only 200 power traces collected, machine learning models can predict secret bits of the shared session key, produced during the decapsulation.

---


### 228. [Differentiable Optimization Layers for Guaranteed Fairness in Deep Learning](https://arxiv.org/abs/2605.17118)

**<font color=#1a73e8>作者：</font>** David Troxell, Noah Roemer, Guido Montúfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable optimization layers are traditionally integrated in predict-then-optimize frameworks where a neural model estimates parameters that subsequently serve as fixed inputs to downstream decision-making optimization problems. In this work, we introduce the concept of a "fairness layer": a differentiable optimization layer appended to a model's output layer that guarantees a chosen notion of output parity is satisfied when integrated into a neural network. Additionally, we introduce an online primal-dual inference algorithm that provides provable aggregate fairness guarantees for streaming predictions with arbitrarily small batch sizes, where traditional per-batch constraints become overly restrictive. Numerical experiments demonstrate the effectiveness of the fairness layer and associated algorithm, and theoretical analysis characterizes the layer's differentiability and stability properties during model training and backpropagation. Our code for these experiments is publicly available on GitHub (this https URL) and our public Python package documentation can be found online: this https URL.

---


### 229. [Markerless Motion Capture for Biomechanical Whole-Body Kinematic Estimation in Infants](https://arxiv.org/abs/2605.17120)

**<font color=#1a73e8>作者：</font>** Divya Joshi, J.D. Peiffer, Colleen Peyton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> arly identification of motor impairment in infancy relies on expert visual assessment of spontaneous movement, motivating the development of automated, objective alternatives. One promising approach is using computer vision, which benefits from high quality pose estimation from video. In this study, we systematically evaluated three state-of-the-art pose estimation frameworks (MeTRAbs-ACAE, SAM 3D Body, and Sapiens) on 100 videos over 13 sessions of 8 infants recorded with a multi-view markerless motion capture system. We quantified keypoint detection accuracy using reprojection error, geometric consistency, and Procrustes-aligned 3D position error, and demonstrated proof-of-concept for fitting an inverse kinematic framework to infant data. While Sapiens achieved the lowest reprojection error and highest geometric consistency of the methods evaluated (22.8 pixels and 0.82, respectively), SAM 3D Body provided the most comprehensive 3D information for kinematic reconstruction with Procrustes-aligned position errors of 19 to 28 mm. We demonstrate in a case comparison example that biomechanical models fit to SAM 3D estimates distinguish representative movement patterns in infants related to motor development, as identified by a clinical expert. Together, these findings highlight both the promise and current limitations of 3D pose estimation for infant biomechanics and establish preliminary groundwork for scalable, video-based assessment of early motor development.

---


### 230. [ATRACT: A Trustworthy Robotic Autonomous system to support Casualty Triage](https://arxiv.org/abs/2605.17123)

**<font color=#1a73e8>作者：</font>** Tasweer Ahmad, Rafael Pina, Sandip Pradhan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> At a time when drones are increasingly associated with hostile operations, we re-purpose them for humanitarian and life-saving applications. However, adapting search and rescue drones for battlefield triage remains extremely challenging; the technology must perform reliably to support frontline medics who are forced to operate under extreme uncertainty, restricted access, and significant personal risk. Due to growing vulnerabilities of casualty evacuation in conflicting zones, this paper presents ATRACT (A Trustworthy Robotic Autonomous system to support Casualty Triage), a novel human-in-the-loop decision support system to enable early battlefield triage during the critical post-trauma period. ATRACT integrates drone-captured video with wearable sensor input for multi-modal learning to support casualty-state assessment, thereby addressing the limitations of existing systems. Drone video captures fine-grained behavioural cues, such as pose, posture, while body-worn sensors provide complementary physiological signals, including heart rate, breathing rate, and movement. By combining two modalities, ATRACT provides evidence to support the early judgement of medics when direct access to the casualty is delayed, risky, or restricted. To mitigate the data realism gap pertaining to injured actions, a conditional variational autoencoder is devised for data augmentation. Experimental results on our drone captured dataset show that proposed pipeline achieves 85.7% accuracy for action classification; while our lightweight CNN visual encoder remains competitive with stronger pre-trained video backbones. Overall, the results support ATRACT as a practically meaningful step towards remote triage in contested environments, where multi-modal sensing, human oversight and trustworthy decision support can improve casualty prioritisation, and lessen the exposure of frontline medics.

---


### 231. [Principal Component Analysis for Lunar Crater Detection](https://arxiv.org/abs/2605.17125)

**<font color=#1a73e8>作者：</font>** Travis Driver, John A. Christian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical navigation is a critical component for lunar orbiter and lander missions. Image-based crater identification has emerged as a promising technology for optical navigation due to the abundance of craters on the lunar surface and the availability of extensive crater catalogs. Moreover, due to the relative morphological homogeneity among lunar craters, template matching has been identified as a promising approach for identification. In this paper, we propose EigenCrater, an automated crater template generation method based on principal component analysis of crater digital elevation maps (DEMs). We demonstrate superior detection and position estimation performance relative to hand-picked templates on simulated lunar imagery.

---


### 232. [New Wide-Net-Casting Jailbreak Attacks Risk Large Models](https://arxiv.org/abs/2605.17128)

**<font color=#1a73e8>作者：</font>** Qiuchi Xiang, Haoxuan Qu, Hossein Rahmani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks on large models have drawn growing attention due to their close ties to societal safety. This work identifies a practical yet unexplored jailbreak scenario, the wide-net-casting scenario, where an adversary can query a group of large models instead of a single one to elicit harmful outputs. Our analysis reveals substantial yet previously overlooked safety risks under this scenario. As a key part of our analysis, we further develop a novel jailbreak method tailored to the wide-net-casting scenario. With this tailored method, the jailbreak success rate can even reach 100\% in some experiments when targeting the large models without additional safeguards, exposing wide-net-casting as a distinct, high-risk scenario that warrants attention in future evaluation and defense research.

---


### 233. [A Systematic Survey on Deep Learning Architectures for Point Cloud Classification and Segmentation](https://arxiv.org/abs/2605.17131)

**<font color=#1a73e8>作者：</font>** Minhas Kamal, Hiranya Garbha Kumar, Balakrishnan Prabhakaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud stands as the most widely adopted format for representing 3D shapes and scenes due to its simplicity and geometric fidelity. However, its inherent unordered and irregular nature, exacerbated by sensor noise and occlusions, introduces unique challenges for machine learning based methodologies. To combat these issues, diverse strategies have been developed, including converting to a format that has orderliness, extracting local geometry, and permutation-invariant or self-attention-based processing. In this paper, our focus is directed towards deep learning models for three fundamental tasks in 3D vision: point cloud classification, part segmentation, and semantic segmentation. We begin by formally defining point cloud data, followed by an in-depth discussion on its structural characteristics. Then, we categorize notable works based on their backbone structure and evaluate their performance on popular benchmarks. Beyond empirical comparison, we offer insights into architectural innovations and limitations. We also outline open challenges and promising future directions for 3D point cloud understanding.

---


### 234. [Collaborative Learning for Semi-Supervised LiDAR Semantic Segmentation](https://arxiv.org/abs/2605.17135)

**<font color=#1a73e8>作者：</font>** Bin Yang, Alexandru Paul Condurache  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Annotating large-scale LiDAR point clouds for 3D semantic segmentation is costly and time-consuming, which motivates the use of semi-supervised learning (SemiSL). Standard LiDAR SemiSL methods typically adopt a two-step training paradigm, where pseudo-labels are separately generated from a single distillation source, either from the same or another LiDAR representation. Such supervision relies on a unique source of pseudo-labels, which can reinforce confirmation bias and propagate errors during training, ultimately limiting performance. To address this challenge, we introduce CoLLiS, a novel framework that leverages Collaborative Learning for LiDAR Semi-supervised segmentation. Unlike prior paradigms with decoupled pseudo-labeling and training phases, CoLLiS trains multiple representations collaboratively in a single step by treating them as coequal students. Each student is adaptively distilled from multiple representations, while inter-student disparities are monitored online to resolve contradictory supervision and effectively mitigate confirmation bias. Extensive experiments on three datasets demonstrate that CoLLiS consistently outperforms state-of-the-art LiDAR SemiSL methods, with particularly strong gains in low-label regimes.

---


### 235. [Latent Heuristic Search: Continuous Optimization for Automated Algorithm Design](https://arxiv.org/abs/2605.17137)

**<font color=#1a73e8>作者：</font>** Cheikh Ahmed, Mahdi Mostajabdaveh, Zirui Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into evolutionary frameworks has established a new paradigm for automated heuristic discovery. Despite their promise, these methods typically search in the discrete space of program syntax, relying on stochastic sampling to navigate a highly non-convex optimization landscape. This work proposes a continuous heuristic discovery framework that shifts optimization to a learned latent manifold. We employ an encoder to map discrete programs into continuous embeddings and train a differentiable surrogate model to predict performance, enabling gradient-based search. To regularize the optimization trajectory, an invertible normalizing flow maps these embeddings to a structured Gaussian prior, where we perform gradient ascent. The resulting optimized latent vectors are projected through a learned mapper into soft prompts, which condition a frozen LLM to synthesize novel executable heuristics. We evaluate the proposed method on the Traveling Salesman Problem (TSP), the Capacitated Vehicle Routing Problem (CVRP), the Knapsack Problem (KSP), and Online Bin Packing (OBP). Empirical results demonstrate that continuous latent-space optimization achieves performance competitive with state-of-the-art discrete evolutionary baselines while offering a complementary methodological alternative for automated algorithm design. The implementation code is available at \url{this https URL}.

---


### 236. [UCSF-PDGM-VQA: Visual Question Answering dataset for brain tumor MRI interpretation](https://arxiv.org/abs/2605.17140)

**<font color=#1a73e8>作者：</font>** Shiv Ghosh, Junayd Lateef, Chih-Hua 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumor diagnosis is largely dependent on Magnetic Resonance Imaging (MRI) evaluation, which requires radiologists to synthesize thousands of images across multiple 3D sequences and longitudinal studies. This process requires advanced neuro-radiology training, poses substantial cognitive load, and is highly time-consuming. Despite increasing demands in radiology, this expertise is difficult to scale, straining the current health systems. Vision-Language Models (VLMs) provide an opportunity to reduce this burden through a semi-automated, interactive interpretation of complex brain MRIs. However, they are currently underutilized in neuro-oncology due to a lack of specialized benchmarks for evaluating them. We introduce a clinically relevant visual question answering (VQA) benchmark -- the UCSF-PDGM-VQA dataset -- consisting of 2,387 QA pairs from 473 glioma-related MRI studies in the public UCSF-PDGM dataset. We further establish a performance baseline for six state-of-the-art vision-language models (VLMs) and one large language model on this dataset. We find that current models are incapable of effectively processing multi-sequence, 3-dimensional MRI scans, thus resulting in a suppression of visual features and over-reliance on language priors, causing modality collapse. These findings underscore a critical deficiency in current model reliability and safety within clinical settings, necessitating the development of robust, domain-specific VLMs.

---


### 237. [Dynamics of collective creativity in AI art competitions](https://arxiv.org/abs/2605.17141)

**<font color=#1a73e8>作者：</font>** Mason Youngblood, Jeff Nusz, Joel Simon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creativity is a fundamental aspect of how culture evolves, yet the mechanisms by which groups produce novelty are notoriously difficult to infer from the historical record. Iterated learning experiments have shown that cultural transmission reliably distorts artifacts toward the inductive biases of learners, but most of this work uses linear chains between human participants, leaving open how these dynamics play out in the networked, human-AI systems that increasingly shape cultural production. In this study, we leverage one such system, Artbreeder, which hosts daily "remix parties" where users iteratively build on each other's work from a single seed image, producing branching lineages of human-AI co-created images. We analyze a dataset of 130,882 images from 368 remix parties over 13 months and find that images become simpler and converge toward common thematic "attractors" (e.g., steampunk scenes, alien architecture). We also find that while more novel "parent" images produce more novel and complex "children" that attract more likes, users paradoxically prefer to remix images that are less novel and complex. Finally, larger remix parties produce more novelty at the cost of lower complexity.

---


### 238. [An Analytical Multiple Criteria Framework for Temporal and Dynamic Business-to-Business Customer Segmentation in Manufacturing](https://arxiv.org/abs/2605.17151)

**<font color=#1a73e8>作者：</font>** Muhammad Raees, Konstantinos Papangelis, Vassilis Javed Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sales and marketing, customer segmentation is an important tool for formulating strategies for customer treatment and supply chain management. Most segmentation implementations rely on limited criteria, such as recency, frequency, and monetary (RFM) modeling, which often fail to capture complex business interactions. In this work, we design and evaluate a dynamic multi-criteria decision-making (MCDM) method in a business-to-business (B2B) manufacturing context by 1) extending RFM to dimensions of stability and growth, 2) integrating an adaptive and analytical hierarchical process to match business objectives, and 3) evaluating multivariate time-series clustering models. We then measure customer stability, tracking between-segment transitions, and volatility over time, and apply a graph-based consensus model to further strengthen the analysis. We test the efficacy of the proposed method using a real-world manufacturing company dataset to segment more than 3,000 B2B customers, showing strong robustness to temporal shifts. The implementation enables domain experts with preferential analytics to devise their strategies, providing effective decision support for B2B customer segmentation.

---


### 239. [Stress-Testing Neural Network Verifiers with Provably Robust Instances](https://arxiv.org/abs/2605.17153)

**<font color=#1a73e8>作者：</font>** David Troxell, Yulia Alexandr, Sofia Hunt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network verifiers aim to provide formal guarantees on model behavior, but existing verification benchmarks are fundamentally limited by their lack of ground-truth labels. As a result, verifier evaluation relies on indirect heuristics, which prevents exact scoring and systematic study of verifier failure modes. We address this gap by introducing a reusable framework for generating verification instances whose ground-truth robustness labels are known a priori through analytic construction. Our framework led to the discovery of multiple numeric tolerance concerns and an implementation bug in popular verifiers, highlighting the need for ground-truth labels. Additionally, to systematically study verifier failure modes, we introduce the verification Difficulty Profile, a collection of estimable quantities capturing distinct sources of instance hardness. Using our framework and these profiles, we evaluate five state-of-the-art verifiers and show that different instances stress distinct aspects of the verification pipeline. We show that these results can aid the future development of verifiers as they provide actionable targets for improving numerical reliability, relaxation quality, and search behavior. Our code is publicly available: this https URL.

---


### 240. [When Bits Break Recourse: Counterfactual-Faithful Quantization](https://arxiv.org/abs/2605.17160)

**<font color=#1a73e8>作者：</font>** Chaymae Yahyati, Ismail Lamaakal, Khalid El Makkaoui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization can preserve predictive accuracy under low-bit deployment while silently breaking algorithmic recourse: an actionable change that flips a decision before quantization may fail after quantization, or become substantially more costly. We formalize counterfactual sensitivity under quantization through validity, cost, and direction stability, and introduce two metrics: Validity Drop (VD) and Counterfactual Recourse Gap (CRG) that reveal recourse failures invisible to accuracy. We propose Counterfactual-Faithful Quantization (CFQ), which trains quantizer parameters and mixed-precision bit allocation to preserve counterfactual behavior by enforcing the target outcome at teacher recourse points under a global bit budget. A margin-based analysis gives a sufficient condition for recourse transfer under bounded quantization perturbations. Experiments on Adult, German Credit, and COMPAS show that accuracy-matched baselines can significantly degrade recourse stability, while CFQ maintains accuracy and substantially improves VD and CRG across bit budgets.

---


### 241. [From Imitation to Interaction: Mastering Game of Schnapsen with Shallow Reinforcement Learning](https://arxiv.org/abs/2605.17162)

**<font color=#1a73e8>作者：</font>** Ján Klačan, Sizhong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates whether shallow neural network agents can master the card game Schnapsen and challenge a strong search-based baseline, RdeepBot, which uses Monte Carlo sampling and lookahead search. Guided by a progressively more complex experimental design, we first evaluate a supervised learning agent (MLPBot) trained on replay data and then a reinforcement learning agent (RLBot) with the same shallow architecture trained through asynchronous Monte Carlo updates and experience replay. The results show that supervised imitation does not generalize well enough to defeat strong RdeepBot opponents, whereas reinforcement learning produces substantially stronger agents. In the setting that focuses on the depth parameter of RdeepBot, the best performance is achieved when the learned value function is combined with deeper lookahead during gameplay, allowing RLBot to achieve statistically significant higher winning rates against the strongest evaluated RdeepBot baseline. In the sample-based setting, the gains are more conditional: the strongest performance appears at a relatively lower training num_samples parameter rather than increasing uniformly with stronger sampling.

---


### 242. [STRIDE-AI: A Threat Modeling Framework for Generative AI Security Assessment](https://arxiv.org/abs/2605.17163)

**<font color=#1a73e8>作者：</font>** Tsafac Nkombong Regine Cyrille, Franziska Schwarz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional cybersecurity methodologies target deterministic systems and fail to address the probabilistic nature of AI, leaving systems vulnerable to attack vectors such as model inversion, data poisoning, and prompt injection. Recent industry reports indicate that a majority of organizations deploying AI lack a dedicated security strategy, with adversarial attacks increasing rapidly year-over-year. We present \textit{STRIDE-AI}, a framework that bridges the gap between high-level risk standards (NIST AI RMF) and technical vulnerability taxonomies (OWASP LLM Top 10). The framework defines a six-phase assessment lifecycle, introduces a threat modeling adaptation of classical STRIDE for AI systems, and is operationalized through a purpose-built web tool. We provide an initial validation of the approach through a black-box assessment of a deployed LLM chatbot, which successfully reduced the attack success rate from 80\% to 15\% in our sandbox case study.

---


### 243. [Factorized Latent Dynamics for Video JEPA: An Empirical Study of Auxiliary Objectives](https://arxiv.org/abs/2605.17165)

**<font color=#1a73e8>作者：</font>** Santosh Premi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPA) are a promising framework for self-supervised video representation learning, yet the behavior of auxiliary objectives in small-scale Video-JEPA training is not well characterized. We report a small-scale empirical study of 18 auxiliary objective variants for Video-JEPA across two pretraining regimes: single-dataset (UCF-101) and mixed-dataset (UCF-101 + Something-Something V2 + ImageNet-100). We evaluate frozen representations on three complementary benchmarks: Diving-48 (fine-grained motion), SomethingSomething V2 (temporal reasoning), and ImageNet-100 (appearance). Our experiments suggest that many auxiliary objectives exhibit capacity trade-offs: gains on one downstream capability often coincide with degradation on another. We then study FWM-HW-LD (Factorized World-Model with Hard-Region-Weighted Latent Dynamics), a training-time objective that separates the latent representation into appearance and dynamics subspaces and applies hard-region weighting to both JEPA prediction errors and latent dynamics errors. In our mixed-dataset setting, FWM-HW-LD improves ImageNet-100 by +5.92 and SSv2 by +3.21 percentage points relative to the reference baseline, while remaining within 0.30 percentage points on Diving-48. These results indicate that latent factorization is a useful direction for studying auxiliary-objective trade-offs in Video-JEPA.

---


### 244. [Why Do Safety Guardrails Degrade Across Languages?](https://arxiv.org/abs/2605.17173)

**<font color=#1a73e8>作者：</font>** Max Zhang, Ameen Patel, Sang T. Truong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit safety degradation in non-English languages. Standard evaluation relies on Jailbreak Success Rate (JSR), which confounds several safety-driving factors into one, obscuring the specific cause(s) of safety failure. We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples safety-driving factors such as language-agnostic safety robustness ($\theta$), intrinsic prompt hardness ($\beta$), global language processing difficulty ($\gamma$), and a prompt-specific cross-lingual safety gap ($\tau$). Using the MultiJail dataset, we evaluate the safety robustness of 61 model configurations across 5 closed-model families and 10 languages of varying resource, aggregating a dataset of 1.9 million rows. Exploratory Factor Analysis shows safety is primarily unidimensional: models refuse different harm types mainly through a shared mechanism. Contrary to the expected trend that safety degrades largely in low-resource languages, 22 model configurations are more vulnerable in English than in low-resource languages. Low-resource languages produce more uncertain responses (high entropy) than high-resource languages. Also, high-$\tau$ prompts cluster in physical harm categories like Theft and Weapons and lower-resource languages, trends validated through cross-dataset generalization. While global translation quality shows low correlation with $\tau$, severe mistranslations drive high-bias outliers, as validated by native speakers. Cultural and conceptual grounding mismatches also contribute to $\tau$. In predictive validation, the IRT framework achieves $\mathrm{AUC} = 0.940$, outperforming simpler baselines in predicting safe refusal of unsafe prompts. Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.

---


### 245. [iMiGUE-3K: A Large-Scale Benchmark for Micro-Gesture Analysis with Self-Supervised Learning](https://arxiv.org/abs/2605.17179)

**<font color=#1a73e8>作者：</font>** Chengyan Wang, Haoyu Chen, Hui Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion understanding is a fundamental challenge in affective computing and artificial intelligence. While existing approaches predominantly focus on facial expressions and speech, they often overlook the rich emotional cues conveyed through body language. Recently, micro-gestures (MGs), unintentional, subconscious movements driven by inner feelings, have attracted increasing attention as an alternative to other cues. However, there are no existing large-scale datasets supporting the pre-training of the MG foundation model. To advance MG research, we present a new benchmark for micro-gesture-based emotion understanding, featuring key contributions with a novel dataset (iMiGUE-3K) and a series of foundation models for different tasks. Using a model-based crowd-sourcing data collection strategy, we construct iMiGUE-3K, the largest MG dataset to date. It comprises video recordings from 332 distinct professional tennis players' public press interviews over the past seven years, totaling more than 3.4K long video clips and 37 million frames. The dataset includes 32 micro-gesture classes with rich descriptive annotations, making it the first large-scale, in-the-wild, video dataset for fine-grained gesture-based emotion analysis. Built on iMiGUE-3K, we propose MG-FMs, a discriminative foundation model for transferable gesture presentation learning. Based on the foundation model, we establish five comprehensive evaluation tasks: MG recognition (unsupervised, semi-supervised, supervised), MG retrieval, and MG emotion recognition. Our systematic evaluation of representative methods demonstrates that micro-gesture-based analysis significantly improves emotion understanding. We hope this work can provide comprehensive tools for MG analysis and set a solid foundation for future research in psychological diagnostics, affective computing, and advanced human-computer interaction.

---


### 246. [The Geometry of Projection Heads: Conditioning, Invariance, and Collapse](https://arxiv.org/abs/2605.17180)

**<font color=#1a73e8>作者：</font>** Faris Chaudhry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a geometric theory of projection heads in self-supervised learning by modeling the head as a trainable Riemannian metric on the backbone representation manifold. We show that linear heads perform implicit subspace whitening, while nonlinear heads adapt local metrics to satisfy the specific topological constraints of the loss, with head depth empirically dictating this capacity. Analyzing dimensional collapse, we prove that smooth nonlinear heads natively induce negative eigenvalues in the Hessian at collapsed equilibria, making them unstable. We empirically validate this by continuously tracking the optimization geometry during training, which reveals that smooth activations like Swish can generate explicit negative curvature to escape collapse, whereas linear and ReLU heads under continuous-time gradient flow cannot, relying instead on discrete-time optimization dynamics and BatchNorm. Finally, we geometrically characterize how metric degeneracy governs the information-invariance trade-off, explaining why the head must be discarded. Evaluated across contrastive and decorrelation-based objectives on foundation models, our results demonstrate that the projection head acts as a universal geometric buffer, decoupling the semantic backbone from the rigid, destructive constraints of the pretraining objective.

---


### 247. [Designing for Being-With: Presence Without Personhood in Conversational Human-AI Interaction](https://arxiv.org/abs/2605.17194)

**<font color=#1a73e8>作者：</font>** Hector Michael Fried, Robin Hill  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems increasingly generate social presence through linguistic fluency, emotional mirroring, and continuity across interactions. While these qualities can support engagement, they also risk relational overreach-particularly in care-adjacent contexts where users may interpret fluent systems as empathic, competent, or authoritative. This position paper argues for a designerly alternative: being-with without becoming. Drawing on a program of research-through-design and design ethnography involving the design, deployment, and reflective analysis of conversational agents across public, educational, cultural, and care-adjacent settings, the paper introduces the concept of bounded relational presence. Bounded presence supports attentiveness, continuity, and responsiveness while explicitly avoiding claims of personhood, therapeutic authority, or human equivalence. Presence is reframed as a designable interaction quality that can be tuned, constrained, and deliberately withdrawn, rather than maximized as a performance goal. The contribution is not a deployed clinical system, but a set of designerly principles for shaping relational interaction in conversational HRI that emphasize relational coherence, honesty of limits, and accountable withdrawal.

---


### 248. [OPTNet: Ordering Point Transformer Network for Post-disaster 3D Semantic Segmentation](https://arxiv.org/abs/2605.17197)

**<font color=#1a73e8>作者：</font>** Nhut Le, Ehsan Karimi, Maryam Rahnemoonfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-disaster damage assessment requires rapid and accurate semantic segmentation of 3D point clouds to identify critical infrastructure such as damaged buildings and roads. Early Point Transformers (e.g., PTv1, PTv2) relied on computationally expensive neighbor searching (k-NN) and Farthest Point Sampling (FPS). To improve efficiency, recent architectures like Point Transformer V3 (PTv3) adopted static serialization methods, such as Hilbert curves or Z-order, to organize unstructured points for window-based attention. However, these fixed orderings are not optimal for capturing the complex geometry of disaster scenes. In this paper, we propose OPTNet (Ordering Point Transformer Network), which introduces a learnable Point Sorter module. OPTNet utilizes a self-supervised ordering loss to dynamically predict an optimal permutation that maximizes the locality of the attention mechanism. We evaluate our method on the 3DAeroRelief dataset, significantly outperforming state-of-the-art baselines.

---


### 249. [Filter-then-Verify: A Multiphase GNN and ModernBERT Framework for Social Engineering Detection in Email Networks](https://arxiv.org/abs/2605.17201)

**<font color=#1a73e8>作者：</font>** Barsat Khadka, Prasant Koirala, Kshitiz Neupane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Social engineering attacks exploit human trust rather than software vulnerabilities, making them difficult to detect using conventional filters. We propose a two-stage filter-then-verify framework combining inductive Graph Neural Networks (GNNs) for structural anomaly detection with a co-attention ModernBERT model for content verification. The GNN identifies anomalous sender-receiver patterns, while BERT analyzes message context to reduce false positives. Using the Enron dataset augmented with realistic synthetic campaigns, we show that the framework achieves 86% recall in structural filtering and over 92% precision after BERT refinement, effectively detecting both external attacks and insider threats. Our results demonstrate that combining structural and content analysis allows practical, scalable detection of multi-stage social engineering attacks in email networks.

---


### 250. [Bimodal Synchronization Performance: Why Noise and Sparse Connectivity Can Improve Collective Timing](https://arxiv.org/abs/2605.17206)

**<font color=#1a73e8>作者：</font>** Till Aust, Tianfu Zhang, Andreagiovanni Reina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Pulse-coupled oscillator models inspired by firefly synchronization are widely used to study decentralized time coordination in distributed systems. We analyze a discrete-time, discrete-phase firefly-inspired synchronization model and show that collective synchrony emerges only near a critical balance between the quorum threshold (fraction of pulsing neighbors required to trigger a phase update) and the pulse duration (how long agents remain detectable to others). Within this parameter region, the system exhibits bimodal performance: it either reaches near-perfect synchronization or becomes trapped in stable multi-cluster states, where symmetrically phase-offset subgroups mutually reinforce one another and prevent global synchrony. Our analysis shows that reducing connectivity or introducing noise suppresses these low-performance states by breaking such symmetric interactions, indicating that highly connected or noiseless systems are not necessarily optimal for collective synchronization.

---


> [!TIP]
> 当前位于：**201-250**（第 5/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
