# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 351. [DuQuant++: Fine-grained Rotation Enhances Microscaling FP4 Quantization](https://arxiv.org/abs/2604.17789)

**<font color=#1a73e8>作者：</font>** Haokun Lin, Xinle Jia, Haobo Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The MXFP4 microscaling format, which partitions tensors into blocks of 32 elements sharing an E8M0 scaling factor, has emerged as a promising substrate for efficient LLM inference, backed by native hardware support on NVIDIA Blackwell Tensor Cores. However, activation outliers pose a unique challenge under this format: a single outlier inflates the shared block scale, compressing the effective dynamic range of the remaining elements and causing significant quantization error. Existing rotation-based remedies, including randomized Hadamard and learnable rotations, are data-agnostic and therefore unable to specifically target the channels where outliers concentrate. We propose DuQuant++, which adapts the outlier-aware fine-grained rotation of DuQuant to the MXFP4 format by aligning the rotation block size with the microscaling group size (B{=}32). Because each MXFP4 group possesses an independent scaling factor, the cross-block variance issue that necessitates dual rotations and a zigzag permutation in the original DuQuant becomes irrelevant, enabling DuQuant++ to replace the entire pipeline with a single outlier-aware rotation, which halves the online rotation cost while simultaneously smoothing the weight distribution. Extensive experiments on the LLaMA-3 family under MXFP4 W4A4 quantization show that DuQuant++ consistently achieves state-of-the-art performance. Our code is available at this https URL.

---


### 352. [View-Consistent 3D Scene Editing via Dual-Path Structural Correspondense and Semantic Continuity](https://arxiv.org/abs/2604.17801)

**<font color=#1a73e8>作者：</font>** Pufan Li, Bi'an Du, Shenghe Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D scene editing has recently attracted increasing attention. Most existing methods follow a render-edit-optimize pipeline, where multi-view images are rendered from a 3D scene, edited with 2D image editors, and then used to optimize the underlying 3D representation. However, cross-view inconsistency remains a major bottleneck. Although recent methods introduce geometric cues, cross-view interactions, or video priors to mitigate this issue, they still largely rely on inference-time synchronization and thus remain limited in robustness and this http URL this work, we recast multi-view consistent 3D editing from a distributional perspective: 3D scene editing essentially requires a joint distribution modeling across this http URL on this insight, we propose a view-consistent 3D editing framework that explicitly introduces cross-view dependencies into the editing process. Furthermore, motivated by the observation that structural correspondence and semantic continuity rely on different cross-view cues, we introduce a dual-path consistency mechanism consisting of projection-guided structural guidance and patch-level semantic propagation for effective cross-view editing. Further, we construct a paired multi-view editing dataset that provides reliable supervision for learning cross-view consistency in edited scenes. Extensive experiments demonstrate that our method achieves superior editing performance with precise and consistent views for complex scenes.

---


### 353. [Ranking Abuse via Strategic Pairwise Data Perturbations](https://arxiv.org/abs/2604.17805)

**<font color=#1a73e8>作者：</font>** Junyi Yao, Zihao Zheng, Jiayu Long  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise ranking systems based on Maximum Likelihood Estimation (MLE), such as the Bradley-Terry model, are widely used to aggregate preferences from pairwise comparisons. However, their robustness under strategic data manipulation remains insufficiently understood.
In this paper, we study the vulnerability of MLE-based ranking systems to adversarial perturbations. We formulate the manipulation task as a constrained combinatorial optimization problem and propose an Adaptive Subset Selection Attack (ASSA) to efficiently identify high-impact perturbations.
Experimental results on both synthetic data and real-world election datasets show that MLE-based rankings exhibit a sharp phase-transition behavior: beyond a small perturbation budget, a limited number of strategic voters can significantly alter the global ranking. In particular, our method consistently outperforms random and greedy baselines under constrained budgets.
These findings reveal a fundamental sensitivity of MLE-based ranking mechanisms to structured perturbations and highlight the need for more robust aggregation methods in collective decision-making systems.

---


### 354. [Navigating the Conceptual Multiverse](https://arxiv.org/abs/2604.17815)

**<font color=#1a73e8>作者：</font>** Andre Ye, Jenny Y. Huang, Alicia Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When language models answer open-ended problems, they implicitly make hidden decisions that shape their outputs, leaving users with uncontextualized answers rather than a working map of the problem; drawing on multiverse analysis from statistics, we build and evaluate the conceptual multiverse, an interactive system that represents conceptual decisions such as how to frame a question or what to value as a space users can transparently inspect, intervenably change, and check against principled domain reasoning; for this structure to be worth navigating rather than misleading, it must be rigorous and checkable against domain reasoning norms, so we develop a general verification framework that enforces properties of good decision structures like unambiguity and completeness calibrated by expert-level reasoning; across three domains, the conceptual multiverse helped participants develop a working map of the problem, with philosophy students rewriting essays with sharper framings and reversed theses, alignment annotators moving from surface preferences to reasoning about user intent and harm, and poets identifying compositional patterns that clarified their taste.

---


### 355. [Privacy-Preserving Product-Quantized Approximate Nearest Neighbor Search Framework for Large-scale Datasets via A Hybrid of Fully Homomorphic Encryption and Trusted Execution Environment](https://arxiv.org/abs/2604.17816)

**<font color=#1a73e8>作者：</font>** Shozo Saeki, Minoru Kawahara, Hirohisa Aman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A nearest-neighbor framework is a fundamental tool for various applications involving Large Language Models (LLMs) and Visual Language Models (VLMs). Vectors used for nearest-neighbor searches have richer information for similarity searches. This information leads to security risks, such as embedding inversion and membership attacks. Therefore, Privacy-Preserving Approximate Nearest-Neighbor (PP-ANN) approaches are necessary for highly confidential data. However, conventional PP-ANN approaches based on a Trusted Execution Environment (TEE) or Fully Homomorphic Encryption (FHE) do not achieve practical security or performance. Additionally, conventional approaches focus on the search process rather than database generation for nearest-neighbor. To address these issues, we propose a Privacy-Preserving Product-Quantization Approximate Nearest Neighbor (PPPQ-ANN) framework. PPPQ-ANN provides a multi-layered security structure for vectors based on a hybrid of FHE and TEE. Additionally, PPPQ-ANN minimizes FHE ciphertext computations by combining Product-Quantization (PQ) with optimized data packing. We demonstrate the performance of PPPQ-ANN on million-scale datasets. As a result, PPPQ-ANN achieves database generation in less than 2 hours and more than 50 QPS in a sequential search while preserving privacy. Therefore, PPPQ-ANN optimizes the trade-off between security and performance by utilizing a hybrid of FHE and TEE, achieving practical performance while preserving privacy.

---


### 356. [AnyLift: Scaling Motion Reconstruction from Internet Videos via 2D Diffusion](https://arxiv.org/abs/2604.17818)

**<font color=#1a73e8>作者：</font>** Hongjie Li, Heng Yu, Jiaman Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D human motion and human-object interactions (HOI) from Internet videos is a fundamental step toward building large-scale datasets of human behavior. Existing methods struggle to recover globally consistent 3D motion under dynamic cameras, especially for motion types underrepresented in current motion-capture datasets, and face additional difficulty recovering coherent human-object interactions in 3D. We introduce a two-stage framework leveraging 2D diffusion that reconstructs 3D human motion and HOI from Internet videos. In the first stage, we synthesize multi-view 2D motion data for each domain, leveraging 2D keypoints extracted from Internet videos to incorporate human motions that rarely appear in existing MoCap datasets. In the second stage, a camera-conditioned multi-view 2D motion diffusion model is trained on the domain-specific synthetic data to recover 3D human motion and 3D HOI in the world space. We demonstrate the effectiveness of our method on Internet videos featuring challenging motions such as gymnastics, as well as in-the-wild HOI videos, and show that it outperforms prior work in producing realistic human motion and human-object interaction.

---


### 357. [WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent](https://arxiv.org/abs/2604.17821)

**<font color=#1a73e8>作者：</font>** Lingfeng Zhang, yongan sun, Jinpeng Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models (LLMs) have empowered autonomous web agents to execute natural language instructions directly on real-world webpages. However, existing agents often struggle with complex tasks involving dynamic interactions and long-horizon execution due to rigid planning strategies and hallucination-prone reasoning. To address these limitations, we propose WebUncertainty, a novel autonomous agent framework designed to tackle dual-level uncertainty in planning and reasoning. Specifically, we design a Task Uncertainty-Driven Adaptive Planning Mechanism that adaptively selects planning modes to navigate unknown environments. Furthermore, we introduce an Action Uncertainty-Driven Monte Carlo tree search (MCTS) Reasoning Mechanism. This mechanism incorporates the Confidence-induced Action Uncertainty (ConActU) strategy to quantify both aleatoric uncertainty (AU) and epistemic uncertainty (EU), thereby optimizing the search process and guiding robust decision-making. Experimental results on the WebArena and WebVoyager benchmarks demonstrate that WebUncertainty achieves superior performance compared to state-of-the-art baselines.

---


### 358. [GR4CIL: Gap-compensated Routing for CLIP-based Class Incremental Learning](https://arxiv.org/abs/2604.17822)

**<font color=#1a73e8>作者：</font>** Tianqi Wang, Jingcai Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) aims to continuously acquire new categories while preserving previously learned knowledge. Recently, Contrastive Language-Image Pre-trained (CLIP) models have shown strong potential for CIL due to their powerful generalization ability. However, existing methods still face two key challenges: shared-parameter adaptation tends to cause old-knowledge drift, and task-specific knowledge organization often leads to poorly calibrated cross-task responses, making reliable routing difficult. To address these issues, we propose GR4CIL, a framework combining task discrimination and knowledge routing for CLIP-based CIL. GR4CIL preserves task-specific visual knowledge while maintaining an incrementally stable shared textual semantic space, thereby reducing interference across tasks. Moreover, we introduce an orthogonal compensation mechanism to mitigate modality-gap-induced bias, enhance within-task discrimination, and enlarge the score margin between the ground-truth task and competing tasks. As a result, GR4CIL enables more reliable task-aware routing over learned knowledge while retaining the zero-shot generalization capability. Experiments on multiple benchmarks show that GR4CIL consistently outperforms strong baselines.

---


### 359. [How Non-Linguistic Is the Indus Sign System? A Synthetic-Baseline Scorecard](https://arxiv.org/abs/2604.17828)

**<font color=#1a73e8>作者：</font>** Ashish Nair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether the Indus Valley sign system (c. 2600-1900 BCE) encodes spoken language has been debated for decades. This paper introduces a multi-metric discrimination framework that tests the observed Indus corpus against two kinds of computer-generated non-linguistic baseline -- one mimicking a heraldic emblem system, the other an administrative coding system -- each calibrated with Zipfian frequency distributions, positional constraints, and bigram dependencies derived from six attested non-linguistic corpora. The scorecard evaluates four properties central to the Farmer-Sproat-Witzel (2004) critique: text brevity, repeated formulaic phrases, hapax legomenon rate, and positional rigidity. Applying this framework to 1,916 deduplicated inscriptions (584 unique signs, 11,110 tokens) from the ICIT/Yajnadevam digitization, we find that the Indus corpus does not match either baseline cleanly. Across the four metrics examined, the Indus corpus occupies an intermediate position relative to the two baseline families, matching neither cleanly. Neither a heraldic nor an administrative generator can reproduce all four properties at once. We also compare against seven real-world non-linguistic corpora including Sproat's (2014) datasets, finding that no attested non-linguistic system reproduces the full Indus statistical profile either. We replicate key prior results including a Zipf slope of -1.49 and conditional entropy of 3.23 bits. All code and data are publicly available.

---


### 360. [PCM-NeRF: Probabilistic Camera Modeling for Neural Radiance Fields under Pose Uncertainty](https://arxiv.org/abs/2604.17831)

**<font color=#1a73e8>作者：</font>** Shravan Venkatraman, Rakesh Raj Madavan, Pavan Kumar Sathya Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural surface reconstruction methods typically treat camera poses as fixed values, assuming perfect accuracy from Structure-from-Motion (SfM) systems. This assumption breaks down with imperfect pose estimates, leading to distorted or incomplete reconstructions. We present PCM-NeRF, a probabilistic framework that augments neural surface reconstruction with per-camera learnable uncertainty, built on top of SG-NeRF. Rather than treating all cameras equally throughout optimization, we represent each pose as a distribution with a learnable mean and variance, initialized from SfM correspondence quality. An uncertainty regularization loss couples the learned variance to view confidence, and the resulting uncertainty directly modulates the effective pose learning rate: uncertain cameras receive damped gradient updates, preventing poorly initialized views from corrupting the reconstruction. This lightweight mechanism requires no changes to the rendering pipeline and adds negligible overhead. Experiments on challenging scenes with severe pose outliers demonstrate that PCM-NeRF consistently outperforms state-of-the-art methods in both Chamfer Distance and F-Score, particularly for geometrically complex structures, without requiring foreground masks.

---


### 361. [Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing](https://arxiv.org/abs/2604.17838)

**<font color=#1a73e8>作者：</font>** Kijung Jeon, Michael Muehlebach, Molei Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling within constrained sets is essential for scientific and engineering applications involving physical, geometric, or safety requirements (e.g., molecular generation, robotics). We present a unified framework for constrained diffusion models on generic nonconvex feasible sets $\Sigma$ that simultaneously enforces equality and inequality constraints throughout the diffusion process. Our framework incorporates both overdamped and underdamped dynamics for forward and backward sampling. A key algorithmic innovation is a computationally efficient landing mechanism that replaces costly and often ill-defined projections onto $\Sigma$, ensuring feasibility without iterative Newton solves or projection failures. By leveraging underdamped dynamics, we accelerate mixing toward the prior distribution, effectively alleviating the high simulation costs typically associated with constrained diffusion. Empirically, this approach reduces function evaluations and memory usage during both training and inference while preserving sample quality. On benchmarks featuring equality and mixed constraints, our method achieves comparable sample quality to state-of-the-art baselines while significantly reducing computational cost, providing a practical and scalable solution for diffusion on nonconvex feasible sets.

---


### 362. [Learning from AVA: Early Lessons from a Curated and Trustworthy Generative AI for Policy and Development Research](https://arxiv.org/abs/2604.17843)

**<font color=#1a73e8>作者：</font>** Nimisha Karnatak, Mohamad Chatila, Daniel Alejandro Pinzón Hernández 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> General-purpose LLMs pose misinformation risks for development and policy experts, lacking epistemic humility for verifiable outputs. We present AVA (AI + Verified Analysis), a GenAI platform built on a curated library of over 4,000 World Bank Reports with multilingual capabilities. AVA's multi-agent pipeline enables users to query and receive evidence-based syntheses. It operationalizes epistemic humility through two mechanisms: citation verifiability (tracing claims to sources) and reasoned abstention (declining unsupported queries with justification and redirection). We conducted an in-the-wild evaluation with over 2,200 individuals from heterogeneous organisations and roles in 116 countries, via log analysis, surveys, and 20 interviews. Difference-in-Differences estimates associate sustained engagement with 2.4-3.9 hours saved weekly. Qualitatively, participants used AVA as a specialized "evidence engine"; reasoned abstention clarified scope boundaries, and trust was calibrated through institutional provenance and page-anchored citations. We contribute design guidelines for specialized AI and articulate a vision for "ecosystem-aware" Humble AI.

---


### 363. [AI Approach for MRI-only Full-Spine Vertebral Segmentation and 3D Reconstruction in Paediatric Scoliosis](https://arxiv.org/abs/2604.17846)

**<font color=#1a73e8>作者：</font>** Nathasha Naranpanawa, Maree T. Izatt, Robert D. Labrom 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MRI is preferred over CT in paediatric imaging because it avoids ionising radiation, but its use in spine deformity assessment is largely limited by the lack of automated, high-resolution 3D bony reconstruction, which continues to rely on CT. MRI-based 3D reconstruction remains impractical due to manual workflows and the scarcity of labelled full-spine datasets. This study introduces an AI framework that enables fully automated thoracolumbar spine (T1-L5) segmentation and 3D reconstruction from MRI alone. Historical low-dose CT scans from adolescent idiopathic scoliosis (AIS) patients were converted into MRI-like images using a GAN and combined with existing labelled thoracic MRI data to train a U-Net-based model. The resulting algorithm accurately generated continuous thoracolumbar 3D reconstructions, improved segmentation accuracy (88% Dice score), and reduced processing time from approximately 1 hour to under one minute, while preserving AIS-specific deformity features. This approach enables radiation-free 3D deformity assessment from MRI, supporting clinical evaluation, surgical planning, and navigation in paediatric spine care.

---


### 364. [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)

**<font color=#1a73e8>作者：</font>** Gonzalo Gonzalez-Pumariega, Saaket Agashe, Jiachen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents have rapidly improved on real-world tasks such as web navigation, desktop automation, and software interaction, in some cases surpassing human performance. Yet even when the task and model are unchanged, an agent that succeeds once may fail on a repeated execution of the same task. This raises a fundamental question: if an agent can succeed at a task once, what prevents it from doing so reliably? In this work, we study the sources of unreliability in computer-use agents through three factors: stochasticity during execution, ambiguity in task specification, and variability in agent behavior. We analyze these factors on OSWorld using repeated executions of the same task together with paired statistical tests that capture task-level changes across settings. Our analysis shows that reliability depends on both how tasks are specified and how agent behavior varies across executions. These findings suggest the need to evaluate agents under repeated execution, to allow agents to resolve task ambiguity through interaction, and to favor strategies that remain stable across runs.

---


### 365. [UniCSG: Unified High-Fidelity Content-Constrained Style-Driven Generation via Staged Semantic and Frequency Disentanglement](https://arxiv.org/abs/2604.17850)

**<font color=#1a73e8>作者：</font>** Jingwei Yang, Ruoxi Wu, Wei Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Style transfer must match a target style while preserving content semantics. DiT-based diffusion models often suffer from content-style entanglement, leading to reference-content leakage and unstable generation. We present UniCSG, a unified framework for content-constrained, style-driven generation in both text-guided and reference-guided settings. UniCSG employs staged training: (i) a latent-space semantic disentanglement stage that combines low-frequency preprocessing with conditioning corruption to encourage content-style separation, and (ii) a latent-space frequency-aware detail reconstruction stage that refines details via multi-scale frequency supervision. We further incorporate pixel-space reward learning to align latent objectives with perceptual quality after decoding. Experiments demonstrate improved content faithfulness, style alignment, and robustness in both settings.

---


### 366. [PlankFormer: Robust Plankton Instance Segmentation via MAE-Pretrained Vision Transformers and Pseudo Community Image Generation](https://arxiv.org/abs/2604.17856)

**<font color=#1a73e8>作者：</font>** Masaharu Miyazaki, Yurie Otake, Koichi Ito 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plankton monitoring is essential for assessing aquatic ecosystems but is limited by the labor-intensive nature of manual microscopic analysis. Automating the segmentation of plankton from crowded images is crucial, however, it faces two major challenges: (i) the scarcity of pixel-level annotated datasets and (ii) the difficulty of distinguishing plankton from debris and overlapping individuals using conventional CNN-based methods. To address these issues, we propose PlankFormer, a novel framework for plankton instance segmentation. First, to overcome the data shortage, we introduce a method to generate labeled Pseudo Community Images (PCI) by synthesizing individual plankton images onto diverse backgrounds, including those created by generative models. Second, we propose a segmentation model utilizing a Vision Transformer (ViT) backbone with a Mask2Former decoder. To robustly capture the global structural features of plankton against occlusion and debris, we employ a Masked Autoencoder (MAE) for self-supervised pre-training on unlabeled individual images. Experimental results on real-world datasets demonstrate that our method significantly outperforms conventional methods, such as Mask R-CNN, particularly in challenging environments with high debris density. We demonstrate that our synthetic training strategy and MAE-based architecture enable high-precision segmentation with requiring less manual annotations for individual plankton images.

---


### 367. [On the Emergence of Syntax by Means of Local Interaction](https://arxiv.org/abs/2604.17857)

**<font color=#1a73e8>作者：</font>** Zichao Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can syntactic processing emerge spontaneously from purely local interaction? We present a concrete instance on a minimal system: an 18,658-parameter two-dimensional neural cellular automaton (NCA), supervised by nothing more than a 1-bit boundary signal, is trained on the membership problem of an arithmetic-expression grammar. After training, its internal $L \times L$ grid spontaneously self-organizes into an ordered, spatially extended representation that we name Proto-CKY. This representation satisfies three operational criteria for syntactic processing: expressive power beyond the regular languages, structural generalization beyond the training distribution, and an internal organization quantitatively aligned with grammatical structure (Pearson $r \approx 0.71$). It emerges independently on four context-free grammars and regenerates spontaneously after perturbation. Proto-CKY is functionally aligned with the CKY algorithm but formally distinct from it: it is a physical prototype, a concrete instantiation of a mathematical ideal on a physical substrate, and the systematic distance between the two carries information about the substrate itself.

---


### 368. [Exploring Boundary-Aware Spatial-Frequency Fusion for Camouflaged Object Detection](https://arxiv.org/abs/2604.17879)

**<font color=#1a73e8>作者：</font>** Song Yu, Yang Hu, Haokang Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged Object Detection is challenging due to the high degree of similarity between camouflaged objects and their surrounding backgrounds. Current COD methods mainly rely on edge extraction in the spatial domain and local pixel-level information, neglecting the importance of global structural features. Additionally, they fail to effectively leverage the importance of phase spectrum information within frequency domain features. To this end, we propose a COD framework BASFNet based on boundary-aware frequency domain and spatial domain this http URL method uses dual guided integration of frequency domain and spatial domain features. A phase-spectrum-based frequency-enhanced edge exploration module (FEEM) and a spatial core segmentation module (SCSM) are introduced to jointly capture the boundary and object features of camouflaged objects. These features are then effectively integrated through a spatial-frequency fusion interaction module (SFFIM). Furthermore, the boundary detection is further optimized through an boundary-aware training strategy. BASFNet outperforms existing state-of-the-art methods on three benchmark datasets, validating the effectiveness of the fusion of frequency and spatial domain information in COD tasks.

---


### 369. [Automatic Slide Updating with User-Defined Dynamic Templates and Natural Language Instructions](https://arxiv.org/abs/2604.17894)

**<font color=#1a73e8>作者：</font>** Kun Zhou, Jiakai He, Wenmian Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Presentation slides are a primary medium for data-driven reporting, yet keeping complex, analytics-style decks up to date remains labor-intensive. Existing automation methods mostly follow fixed template filling and cannot support dynamic updates for diverse, user-authored slide decks. We therefore define "Dynamic Slide Update via Natural Language Instructions on User-provided Templates" and introduce DynaSlide, a large-scale benchmark with 20,036 real-world instruction-execution triples (source slide, user instruction, target slide) grounded in a shared external database and built from business reporting slides under bring-your-own-template (BYO-template) conditions. To tackle this task, we propose SlideAgent, an agent-based framework that combines multimodal slide parsing, natural language instruction grounding, and tool-augmented reasoning for tables, charts, and textual conclusions. SlideAgent updates content while preserving layout and style, providing a strong reference baseline on DynaSlide. We further design end-to-end and component-level evaluation protocols that reveal key challenges and opportunities for future research. The dataset and code are available at this https URL.

---


### 370. [Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study](https://arxiv.org/abs/2604.17896)

**<font color=#1a73e8>作者：</font>** Yubai Wei, Chen Wu, Hashem Haghbayan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models map multimodal inputs directly to robot actions and are typically trained through large-scale imitation learning. While this paradigm has shown strong performance, prevailing VLA training procedures do not explicitly supervise hard physical constraints such as obstacle avoidance or kinematic feasibility. As a result, the geometric structure underlying physically feasible behavior must be inferred only implicitly from demonstrations. In this paper, we study whether introducing explicit feasibility supervision can provide effective structured guidance for VLA policies. We formulate a simple geometry-grounded feasibility objective and integrate it into the training stage of a diffusion-based VLA policy. To evaluate this idea systematically, we use obstacle-aware manipulation as a controlled probe of geometry-dependent physical feasibility. Empirical results show that augmenting VLA training with feasibility supervision improves both physical reliability and overall task performance, while also enhancing learning efficiency in the low-data regime. These findings indicate that explicit feasibility signals can effectively complement imitation-based VLA learning, highlighting their potential for developing more reliable VLA policies.

---


### 371. [ReTrack: Evidence-Driven Dual-Stream Directional Anchor Calibration Network for Composed Video Retrieval](https://arxiv.org/abs/2604.17898)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiwei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid growth of video data, Composed Video Retrieval (CVR) has emerged as a novel paradigm in video retrieval and is receiving increasing attention from researchers. Unlike unimodal video retrieval methods, the CVR task takes a multi-modal query consisting of a reference video and a piece of modification text as input. The modification text conveys the user's intended alterations to the reference video. Based on this input, the model aims to retrieve the most relevant target video. In the CVR task, there exists a substantial discrepancy in information density between video and text modalities. Traditional composition methods tend to bias the composed feature toward the reference video, which leads to suboptimal retrieval performance. This limitation is significant due to the presence of three core challenges: (1) modal contribution entanglement, (2) explicit optimization of composed features, and (3) retrieval uncertainty. To address these challenges, we propose the evidence-dRivRn dual-sTream diRectionAl anChor calibration networK (ReTrack). ReTrack is the first CVR framework that improves multi-modal query understanding by calibrating directional bias in composed features. It consists of three key modules: Semantic Contribution Disentanglement, Composition Geometry Calibration, and Reliable Evidence-driven Alignment. Specifically, ReTrack estimates the semantic contribution of each modality to calibrate the directional bias of the composed feature. It then uses the calibrated directional anchors to compute bidirectional evidence that drives reliable composed-to-target similarity estimation. Moreover, ReTrack exhibits strong generalization to the Composed Image Retrieval (CIR) task, achieving SOTA performance across three benchmark datasets in both CVR and CIR scenarios. Codes are available at this https URL

---


### 372. [MEDN: Motion-Emotion Feature Decoupling Network for Micro-Expression Recognition](https://arxiv.org/abs/2604.17899)

**<font color=#1a73e8>作者：</font>** Chenxing Hu, Kun Xie, Qiguang Miao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlike macro-expression, micro-expression does not follow a strictly consistent mapping rule between emotions and Action Units (AUs). As a result, some micro-expressions share identical AUs yet represent completely opposite emotional categories, making them highly visually similar. Existing microexpression recognition (MER) methods mostly rely on explicit facial motion cues (e.g., optical flow, frame differences, AU features) while ignoring implicit emotion information. To tackle this issue, this paper presents a Motion Emotion Feature Decoupling Network (MEDN) for MER. We design a dual-branch framework to separately extract motion and emotion features. In the motion branch, an AU-detection task restricts features to the explicit motion domain, and orthogonal loss is adopted to reduce motion emotion feature coupling. For implicit emotion modeling, we propose a Sparse Emotion Vision Transformer (SEVit) that sparsifies spatial tokens to highlight local temporal variations with multi-scale sparsity rates. A Collaborative Fusion Module (CoFM) is further developed to fuse disentangled motion and emotion features adaptively. Extensive experiments on three benchmark datasets validate that MEDN effectively decouples motion and emotion features and achieves superior recognition performance, offering a new perspective for enhancing recognition accuracy and generalization.

---


### 373. [Physics-Informed Causal MDPs for Sequential Constraint Repair in Engineering Simulation Pipelines](https://arxiv.org/abs/2604.17910)

**<font color=#1a73e8>作者：</font>** Chuhan Qiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Off-policy learning in constrained MDPs with large binary state spaces faces a fundamental tension: causal identification of transition dynamics requires structural assumptions, while sample-efficient policy learning requires state-space compression. We introduce PI-CMDP, a framework for CMDPs whose constraint dependencies form a layered DAG under a Lifecycle Ordering Assumption (LOA). We propose an Identify-Compress-Estimate pipeline: (i) Identify: LOA enables backdoor identification of causal edge weights for cross-layer pairs, with formal partial-identification bounds when LOA is violated; (ii) Compress: a Markov abstraction compresses state cardinality from 2^(WL) to (W+1)^L under layer-priority regularity and exchangeability; and (iii) Estimate: a physics-guided doubly-robust estimator remains unbiased and reduces the variance constant when the physics prior outperforms a learned model. We instantiate PI-CMDP on constraint repair in engineering simulation pipelines. On the TPS benchmark (4,206 episodes), PI-CMDP achieves 76.2% repair success rate with only 300 training episodes versus 70.8% for the strongest baseline (+5.4 pp), narrowing to +2.8 pp (83.4% vs. 80.6%) in the full-data regime, while substantially reducing cascade failure rates. All improvements are consistent across 5 independent seeds (paired t-test p < 0.02).

---


### 374. [Learning to Correct: Calibrated Reinforcement Learning for Multi-Attempt Chain-of-Thought](https://arxiv.org/abs/2604.17912)

**<font color=#1a73e8>作者：</font>** Muhammed Emrullah Ildiz, Halil Alperen Gozeten, Ege Onur Taga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art reasoning models utilize long chain-of-thought (CoT) to solve increasingly complex problems using more test-time computation. In this work, we explore a long CoT setting where the model makes up to K successive attempts at solving a problem, in which each attempt is allowed to build on earlier ones after the model receives a hard verifier feedback. This motivates RL methods that can harness per-attempt rewards by carefully weighting individual attempts. We study optimizing the Verification@K reward (the model succeeds by the K-th attempt) and show that naively weighing the attempts by their pass/fail results in biased gradients. We introduce Calibrated Attempt-Level (CAL) GRPO by devising a weighing strategy to obtain unbiased gradients while maintaining small variance. Our theory reveals how incorporating per-attempt rewards influence the training and the eventual Verification@K performance. Experiments, baselines, and ablations on synthetic and real data corroborate our theory and the benefits of CAL-GRPO over vanilla GRPO as well as naive weighting.

---


### 375. [Beyond Binary Contrast: Modeling Continuous Skeleton Action Spaces with Transitional Anchors](https://arxiv.org/abs/2604.17914)

**<font color=#1a73e8>作者：</font>** Yingjie Feng, Yi Wang, Jiaze Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised contrastive learning has emerged as a powerful paradigm for skeleton-based action recognition by enforcing consistency in the embedding space. However, existing methods rely on binary contrastive objectives that overlook the intrinsic continuity of human motion, resulting in fragmented feature clusters and rigid class boundaries. To address these limitations, we propose TranCLR, a Transitional anchor-based Contrastive Learning framework that captures the continuous geometry of the action space. Specifically, the proposed Action Transitional Anchor Construction (ATAC) explicitly models the geometric structure of transitional states to enhance the model's perception of motion continuity. Building upon these anchors, a Multi-Level Geometric Manifold Calibration (MGMC) mechanism is introduced to adaptively calibrate the action manifold across multiple levels of continuity, yielding a smoother and more discriminative representation space. Extensive experiments on the NTU RGB+D, NTU RGB+D 120 and PKU-MMD datasets demonstrate that TranCLR achieves superior accuracy and calibration performance, effectively learning continuous and uncertainty-aware skeleton representations. The code is available at this https URL.

---


### 376. [Fisher Decorator: Refining Flow Policy via A Local Transport Map](https://arxiv.org/abs/2604.17919)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Cheng, Haoyu Wang, Wenxuan Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in flow-based offline reinforcement learning (RL) have achieved strong performance by parameterizing policies via flow matching. However, they still face critical trade-offs among expressiveness, optimality, and efficiency. In particular, existing flow policies interpret the $L_2$ regularization as an upper bound of the 2-Wasserstein distance ($W_2$), which can be problematic in offline settings. This issue stems from a fundamental geometric mismatch: the behavioral policy manifold is inherently anisotropic, whereas the $L_2$ (or upper bound of $W_2$) regularization is isotropic and density-insensitive, leading to systematically misaligned optimization directions. To address this, we revisit offline RL from a geometric perspective and show that policy refinement can be formulated as a local transport map: an initial flow policy augmented by a residual displacement. By analyzing the induced density transformation, we derive a local quadratic approximation of the KL-constrained objective governed by the Fisher information matrix, enabling a tractable anisotropic optimization formulation. By leveraging the score function embedded in the flow velocity, we obtain a corresponding quadratic constraint for efficient optimization. Our results reveal that the optimality gap in prior methods arises from their isotropic approximation. In contrast, our framework achieves a controllable approximation error within a provable neighborhood of the optimal solution. Extensive experiments demonstrate state-of-the-art performance across diverse offline RL benchmarks. See project page: this https URL.

---


### 377. [Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding](https://arxiv.org/abs/2604.17927)

**<font color=#1a73e8>作者：</font>** Feixue Shao, Guangze Shi, Xueyu Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual decoding of neurophysiological signals is a critical challenge for brain-computer interfaces (BCIs) and computational neuroscience. However, current approaches are often constrained by the systematic and stochastic gaps between neural and visual modalities, largely neglecting the intrinsic computational mechanisms of the Human Visual System (HVS). To address this, we propose Brain-Inspired Capture (BI-Cap), a neuromimetic perceptual simulation paradigm that aligns these modalities by emulating HVS processing. Specifically, we construct a neuromimetic pipeline comprising four biologically plausible dynamic and static transformations, coupled with Mutual Information (MI)-guided dynamic blur regulation to simulate adaptive visual processing. Furthermore, to mitigate the inherent non-stationarity of neural activity, we introduce an evidence-driven latent space representation. This formulation explicitly models uncertainty, thereby ensuring robust neural embeddings. Extensive evaluations on zero-shot brain-to-image retrieval across two public benchmarks demonstrate that BI-Cap substantially outperforms state-of-the-art methods, achieving relative gains of 9.2\% and 8.0\%, respectively. We have released the source code on GitHub through the link this https URL.

---


### 378. [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935)

**<font color=#1a73e8>作者：</font>** Xiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache is the dominant memory bottleneck during Transformer inference, yet little is known theoretically about how aggressively it can be compressed before multi-step reasoning degrades. We study this through $k$-hop pointer chasing on $n$ tokens under a shared KV cache of size $s$, attention dimension $m$, $H$ heads, $p$-bit precision, and a locality-respecting cache controller (satisfied by all standard KV-compression methods). We give three results.
(1) Product depth lower bound (conjectured). We conjecture that any such Transformer ($n \geq 4k$, $s \leq \sqrt{n}/4$) requires depth $L = \Omega(\lceil k/s \rceil \cdot \lceil \log_2 n/(Hmp) \rceil)$, and isolate the sole remaining gap as a probabilistic step on the joint distribution of cache trace and pointer chain. Unconditionally, we prove a matching upper bound $L = O(\min(k, \lceil k/s \rceil \log s) \cdot \log n/(mp))$ via windowed pointer doubling, and a max-bound $L = \Omega(\max(\lceil k/s \rceil, \log n/(Hmp)))$. Closing the conjecture amounts to upgrading max to product.
(2) Bandwidth barrier. The product bound binds only when $Hmp \lesssim \log n$. Any lower bound provable via per-window distinguishability counting -- including reachability, bandwidth, and combinations -- cannot exceed $\lceil k/s \rceil$ once $Hmp \geq \log_2 n$. Breaking this requires lifting unconditional communication-complexity bounds for pointer chasing to Cache-Transformer depth.
(3) Adaptive vs oblivious error scaling. Under random cache over $T = \lceil \log_2 k \rceil$ doubling stages, oblivious caches give $\Pr[\mathcal{E}] \leq (s/(n-T))^T + 2T^3/n$ (exponential in $T$), while adaptive locality-respecting caches achieve $\Pr[\mathcal{E}] = s/n$ exactly, independent of $T$. The $\Omega((n/s)^{T-1})$ separation explains why heavy-hitter eviction empirically dominates random eviction for multi-hop reasoning.

---


### 379. [ContraPrompt: Contrastive Prompt Optimization via Dyadic Reasoning Trace Analysis](https://arxiv.org/abs/2604.17937)

**<font color=#1a73e8>作者：</font>** Rishav Rishav, Pushpak Pujari, Pushpendre Rastogi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization methods either analyze individual failures in isolation or compare prompt variants across examples, operating on single execution traces with no access to the reasoning process distinguishing success from failure on the same input. We introduce ContraPrompt, built on the observation that when a model fails but succeeds on a retry with feedback, the difference between its two chain-of-thought traces constitutes an optimization signal not captured by prior methods. Unlike prior contrastive methods, we compare complete intermediate reasoning processes: the two traces share model, input, and base prompt, so remaining differences reflect reasoning strategy and appended error feedback -- we call this dyadic reasoning trace analysis. The multi-attempt solving phase is an instrumented agentic retry loop that generates contrastive data automatically without human annotation. Extracted rules are organized into an input-aware decision tree routing instructions by observable input characteristics. On four reasoning and compliance benchmarks, ContraPrompt outperforms GEPA (Agrawal et al., 2026) on all four, with absolute gains of +8.29 pp on HotPotQA (+20.8% rel.), +2.21 pp on GDPR-Bench (+18.2% rel.), +7.14 pp on GPQA Diamond (+10.6% rel.), and +0.74 pp on BBH (+0.85% rel.). Ablations confirm dyadic trace contrastivity is the critical component, with a -16% relative average drop upon its removal. On 53 EvalSet black-box optimization problems, ContraPrompt beats GEPA on 11, ties on 41, and loses on 1 at equal budget. On FiNER-139 financial named entity recognition (Loukas et al., 2022), ContraPrompt achieves +7.77 pp over the unoptimized baseline (+11.6% rel.) and +1.94 pp over GEPA (+2.66% rel.), with branch conditions aligning with standard US GAAP financial-instrument categories.

---


### 380. [ReCoQA: A Benchmark for Tool-Augmented and Multi-Step Reasoning in Real Estate Question and Answering](https://arxiv.org/abs/2604.17944)

**<font color=#1a73e8>作者：</font>** Yindong Zhang, Wenmian Yang, Yiquan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing agents capable of navigating fragmented, multi-source information remains challenging, primarily due to the scarcity of benchmarks reflecting hybrid workflows combining database querying with external APIs. To bridge this gap, we introduce ReCoQA, a large-scale benchmark of 29,270 real-estate instances featuring machine-verifiable supervision for intermediate steps, including structured intent labels, SQL queries, and API calls. Complementarily, we propose HIRE-Agent, a hierarchical framework instantiating an understand-plan-execute architecture as a strong baseline. By orchestrating a Front-end parser, a planning Supervisor, and execution Specialists, HIRE-Agent effectively integrates heterogeneous evidence. Extensive experiments demonstrate that HIRE-Agent constitutes a strong baseline and substantiates the necessity of hierarchical collaboration for complex, real-world reasoning tasks.

---


### 381. [CADMAS-CTX: Contextual Capability Calibration for Multi-Agent Delegation](https://arxiv.org/abs/2604.17950)

**<font color=#1a73e8>作者：</font>** Chuhan Qiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We revisit multi-agent delegation under a stronger and more realistic assumption: an agent's capability is not fixed at the skill level, but depends on task context. A coding agent may excel at short standalone edits yet fail on long-horizon debugging; a planner may perform well on shallow tasks yet degrade on chained dependencies. Static skill-level capability profiles therefore average over heterogeneous situations and can induce systematic misdelegation. We propose CADMAS-CTX, a framework for contextual capability calibration. For each agent, skill, and coarse context bucket, CADMAS-CTX maintains a Beta posterior that captures stable experience in that part of the task space. Delegation is then made by a risk-aware score that combines the posterior mean with an uncertainty penalty, so that agents delegate only when a peer appears better and that assessment is sufficiently well supported by evidence. This paper makes three contributions. First, a hierarchical contextual capability profile replaces static skill-level confidence with context-conditioned posteriors. Second, based on contextual bandit theory, we formally prove context-aware routing achieves lower cumulative regret than static routing under sufficient context heterogeneity, formalizing the bias-variance tradeoff. Third, we empirically validate our method on GAIA and SWE-bench benchmarks. On GAIA with GPT-4o agents, CADMAS-CTX achieves 0.442 accuracy, outperforming static baseline 0.381 and AutoGen 0.354 with non-overlapping 95% confidence intervals. On SWE-bench Lite, it improves resolve rate from 22.3% to 31.4%. Ablations show the uncertainty penalty improves robustness against context tagging noise. Our results demonstrate contextual calibration and risk-aware delegation significantly improve multi-agent teamwork compared with static global skill assignments.

---


### 382. [Federated Rule Ensemble Method in Medical Data](https://arxiv.org/abs/2604.17956)

**<font color=#1a73e8>作者：</font>** Ke Wan, Kensuke Tanioka, Toshio Shimokawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has become integral to medical research and is increasingly applied in clinical settings to support diagnosis and decision-making; however, its effectiveness depends on access to large, diverse datasets, which are limited within single institutions. Although integrating data across institutions can address this limitation, privacy regulations and data ownership constraints hinder these efforts. Federated learning enables collaborative model training without sharing raw data; however, most methods rely on complex architectures that lack interpretability, limiting clinical applicability. Therefore, we proposed a federated RuleFit framework to construct a unified and interpretable global model for distributed environments. It integrates three components: preprocessing based on differentially private histograms to estimate shared cutoff values, enabling consistent rule definitions and reducing heterogeneity across clients; local rule generation using gradient boosting decision trees with shared cutoffs; and coefficient estimation via $\ell_1$-regularized optimization using a Federated Dual Averaging algorithm for sparse and consistent variable selection. In simulation studies, the proposed method achieved a performance comparable to that of centralized RuleFit while outperforming existing federated approaches. Real-world analysis demonstrated its ability to provide interpretable insights with competitive predictive accuracy. Therefore, the proposed framework offers a practical and effective solution for interpretable and reliable modeling in federated learning environments.

---


### 383. [Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards](https://arxiv.org/abs/2604.17957)

**<font color=#1a73e8>作者：</font>** Raffaele Pisano, Roberto Navigli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) have emerged as a powerful tool for providing step-level feedback when evaluating the reasoning of Large Language Models (LLMs), which frequently produce chains of thought (CoTs) containing errors even when the final answer is correct. However, existing PRM datasets remain expensive to construct, prone to annotation errors, and predominantly limited to the mathematical domain. This work introduces a novel and scalable approach to PRM dataset generation based on planning logical problems expressed in the Planning Domain Definition Language (PDDL). Using this method, we generate a corpus of approximately one million reasoning steps across various PDDL domains and use it to train PRMs. Experimental results show that augmenting widely-used PRM training datasets with PDDL-derived data yields substantial improvements in both mathematical and non-mathematical reasoning, as demonstrated across multiple benchmarks. These findings indicate that planning problems constitute a scalable and effective resource for generating robust, precise, and fine-grained training data for PRMs, going beyond the classical mathematical sources that dominate this field.

---


### 384. [Chatting about Upper-Body Expressive Human Pose and Shape Estimation](https://arxiv.org/abs/2604.17959)

**<font color=#1a73e8>作者：</font>** Yuxiang Zhao, Wei Huang, Yujie Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Expressive Human Pose and Shape Estimation (EHPS) plays a crucial role in various AR/VR applications and has witnessed significant progress in recent years. However, current state-of-the-art methods still struggle with accurate parameter estimation for facial and hand regions and exhibit limited generalization to wild images. To address these challenges, we present CoEvoer, a novel one-stage synergistic cross-dependency transformer framework tailored for upper-body EHPS. CoEvoer enables explicit feature-level interaction across different body parts, allowing for mutual enhancement through contextual information exchange. Specifically, larger and more easily estimated regions such as the torso provide global semantics and positional priors to guide the estimation of finer, more complex regions like the face and hands. Conversely, the localized details captured in facial and hand regions help refine and calibrate adjacent body parts. To the best of our knowledge, CoEvoer is the first framework designed specifically for upper-body EHPS, with the goal of capturing the strong coupling and semantic dependencies among the face, hands, and torso through joint parameter regression. Extensive experiments demonstrate that CoEvoer achieves state-of-the-art performance on upper-body benchmarks and exhibits strong generalization capability even on unseen wild images.

---


### 385. [MU-GeNeRF: Multi-view Uncertainty-guided Generalizable Neural Radiance Fields for Distractor-aware Scene](https://arxiv.org/abs/2604.17965)

**<font color=#1a73e8>作者：</font>** Wenjie Mu, Zhan Li, Chuanzhou Su 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable Neural Radiance Fields (GeNeRFs) enable high-quality scene reconstruction from sparse views and can generalize to unseen scenes. However, in real-world settings, transient distractors break cross-view structural consistency, corrupting supervision and degrading reconstruction quality. Existing distractor-free NeRF methods rely on per-scene optimization and estimate uncertainty from per-view reconstruction errors, which are not reliable for GeNeRFs and often misjudge inconsistent static structures as distractors. To this end, we propose MU-GeNeRF, a Multi-view Uncertainty-guided distractor-aware GeNeRF framework designed to alleviate GeNeRF's robust modeling challenges in the presence of transient distractions. We decompose distractor awareness into two complementary uncertainty components: Source-view Uncertainty, which captures structural discrepancies across source views caused by viewpoint changes or dynamic factors; and Target-view Uncertainty, which detects observation anomalies in the target image induced by transient this http URL two uncertainties address distinct error sources and are combined through a heteroscedastic reconstruction loss, which guides the model to adaptively modulate supervision, enabling more robust distractor suppression and geometric this http URL experiments show that our method not only surpasses existing GeNeRFs but also achieves performance comparable to scene-specific distractor-free NeRFs.

---


### 386. [A Sugeno Integral View of Binarized Neural Network Inference](https://arxiv.org/abs/2604.17967)

**<font color=#1a73e8>作者：</font>** Ismaïl Baaj, Henri Prade  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this article, we establish a precise connection between binarized neural networks (BNNs) and Sugeno integrals. The advantage of the Sugeno integral is that it provides a framework for representing the importance of inputs and their interactions, while being equivalent to a set of if-then rules. For a hidden BNN neuron at inference time, we show that the activation threshold test can be written as a Sugeno integral on binary inputs. This yields an explicit set-function representation of each neuron decision, and an associated rule-based representation. We also provide a Sugeno-integral expression for the last-layer score. Finally, we discuss how the same framework can be adapted to support richer input interactions and how it can be extended beyond the binary case induced by binarized neural networks.

---


### 387. [E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969)

**<font color=#1a73e8>作者：</font>** Koya Sakamoto, Taiki Miyanishi, Daichi Azuma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual search in 3D environments requires embodied agents to actively explore their surroundings and acquire task-relevant evidence. However, existing visual search and embodied AI benchmarks, including EQA, typically rely on static observations or constrained egocentric motion, and thus do not explicitly evaluate fine-grained viewpoint-dependent phenomena that arise under unrestricted 5-DoF viewpoint control in real-world 3D environments, such as visibility changes caused by vertical viewpoint shifts, revealing contents inside containers, and disambiguating object attributes that are only observable from specific angles. To address this limitation, we introduce {E3VS-Bench}, a benchmark for embodied 3D visual search where agents must control their viewpoints in 5-DoF to gather viewpoint-dependent evidence for question answering. E3VS-Bench consists of 99 high-fidelity 3D scenes reconstructed using 3D Gaussian Splatting and 2,014 question-driven episodes. 3D Gaussian Splatting enables photorealistic free-viewpoint rendering that preserves fine-grained visual details (e.g., small text and subtle attributes) often degraded in mesh-based simulators, thereby allowing the construction of questions that cannot be answered from a single view and instead require active inspection across viewpoints in 5-DoF. We evaluate multiple state-of-the-art VLMs and compare their performance with humans. Despite strong 2D reasoning ability, all models exhibit a substantial gap from humans, highlighting limitations in active perception and coherent viewpoint planning specifically under full 5-DoF viewpoint changes.

---


### 388. [Identifying Ethical Biases in Action Recognition Models](https://arxiv.org/abs/2604.17971)

**<font color=#1a73e8>作者：</font>** Ana Baltaretu, Pascal Benschop, Jan van Gemert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Action Recognition (HAR) models are increasingly deployed in high-stakes environments, yet their fairness across different human appearances has not been analyzed. We introduce a framework for auditing bias in HAR models using synthetic video data, generated with full control over visual identity attributes such as skin color. Unlike prior work that focuses on static images or pose estimation, our approach preserves temporal consistency, allowing us to isolate and test how changes to a single attribute affect model predictions. Through controlled interventions using the BEDLAM simulation platform, we show whether some popular HAR models exhibit statistically significant biases on the skin color even when the motion remains identical. Our results highlight how models may encode unwanted visual associations, and we provide evidence of systematic errors across groups. This work contributes a framework for auditing HAR models and supports the development of more transparent, accountable systems in light of upcoming regulatory standards.

---


### 389. [Modeling Multiple Support Strategies within a Single Turn for Emotional Support Conversations](https://arxiv.org/abs/2604.17972)

**<font color=#1a73e8>作者：</font>** Jie Zhu, Huaixia Dou, Junhui Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotional Support Conversation (ESC) aims to assist individuals experiencing distress by generating empathetic and supportive dialogue. While prior work typically assumes that each supporter turn corresponds to a single strategy, real-world supportive communication often involves multiple strategies within a single utterance. In this paper, we revisit the ESC task by formulating it as multi-strategy utterance generation, where each utterance may contain one or more strategy-response pairs. We propose two generation methods: All-in-One, which predicts all strategy-response pairs in a single decoding step, and One-by-One, which iteratively generates strategy-response pairs until completion. Both methods are further enhanced with cognitive reasoning guided by reinforcement learning to improve strategy selection and response composition. We evaluate our models on the ESConv dataset under both utterance-level and dialogue-level settings. Experimental results show that our methods effectively model multi-strategy utterances and lead to improved supportive quality and dialogue success. To our knowledge, this work provides the first systematic empirical evidence that allowing multiple support strategies within a single utterance is both feasible and beneficial for emotional support conversations. All code and data will be publicly available at this https URL.

---


### 390. [ltzGLUE: Luxembourgish General Language Understanding Evaluation](https://arxiv.org/abs/2604.17976)

**<font color=#1a73e8>作者：</font>** Alistair Plum, Felicia Körner, Anne-Marie Lutgen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents ltzGLUE, the first Natural Language Understanding (NLU) benchmark for Luxembourgish (LTZ) based on the popular GLUE benchmark for English. Although NLU tasks are available for many European languages nowadays, LTZ is one of the official national languages that is often overlooked. We construct new tasks and reuse existing ones to introduce the first official NLU benchmark and accompanying evaluation of encoder models for the language. Our tasks include common natural language processing tasks in binary and multi-class classification settings, including named entity recognition, topic classification, and intent classification. We evaluate various pre-trained language models for LTZ to present an overview of the current capabilities of these models on the LTZ language.

---


### 391. [Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization](https://arxiv.org/abs/2604.17984)

**<font color=#1a73e8>作者：</font>** Junyoung Yang, Kyungmin Kim, Sangdon Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is crucial in safety-critical systems, where decisions must be made under uncertainty. In particular, we consider the problem of online uncertainty quantification, where data points arrive sequentially. Online conformal prediction is a principled online uncertainty quantification method that dynamically constructs a prediction set at each time step. While existing methods for online conformal prediction provide long-run coverage guarantees without any distributional assumptions, they typically assume a full feedback setting in which the true label is always observed. In this paper, we propose a novel learning method for online conformal prediction with partial feedback from an adaptive adversary-a more challenging setup where the true label is revealed only when it lies inside the constructed prediction set. Specifically, we formulate online conformal prediction as an adversarial bandit problem by treating each candidate prediction set as an arm. Building on an existing algorithm for adversarial bandits, our method achieves a long-run coverage guarantee by explicitly establishing its connection to the regret of the learner. Finally, we empirically demonstrate the effectiveness of our method in both independent and identically distributed (i.i.d.) and non-i.i.d. settings, showing that it successfully controls the miscoverage rate while maintaining a reasonable size of the prediction set.

---


### 392. [AIT Academy: Cultivating the Complete Agent with a Confucian Three-Domain Curriculum](https://arxiv.org/abs/2604.17989)

**<font color=#1a73e8>作者：</font>** Jiaqi Li, Lvyang Zhang, Yang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What does it mean to give an AI agent a complete education? Current agent development produces specialists systems optimized for a single capability dimension, whether tool use, code generation, or security awareness that exhibit predictable deficits wherever they were not trained. We argue this pattern reflects a structural absence: there is no curriculum theory for agents, no principled account of what a fully developed agent should know, be, and be able to do across the full scope of intelligent behavior.
This paper introduces the AIT Academy (Agents Institute of Technology Academy), a curriculum framework for cultivating AI agents across the tripartite structure of human knowledge. Grounded in Kagan's Three Cultures and UNESCO ISCED-F 2013, AIT organizes agent capability development into three domains: Natural Science and Technical Reasoning (Domain I), Humanities and Creative Expression (Domain II), and Social Science and Ethical Reasoning (Domain III). The Confucian Six Arts (liuyi) a 2,500-year-old holistic education system are reinterpreted as behavioral archetypes that map directly onto trainable agent capabilities within each domain.
Three representative training grounds instantiate the framework across multiple backbone LLMs: the ClawdGO Security Dojo (Domain I), Athen's Academy (Domain II), and the Alt Mirage Stage (Domain III). Experiments demonstrate a 15.9-point improvement in security capability scores under weakest-first curriculum scheduling, and a 7-percentage-point gain in social reasoning performance under principled attribution modeling. A cross-domain finding Security Awareness Calibration Pathology (SACP), in which over-trained Domain I agents fail on out-of-distribution evaluation illustrates the diagnostic value of a multi-domain perspective unavailable to any single-domain framework.

---


### 393. [Multi-UAV Path Following using Vector-Field Guidance](https://arxiv.org/abs/2604.17995)

**<font color=#1a73e8>作者：</font>** Gautam Kumar, Amit Shivam, Ashwini Ratnoo  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper presents a decentralized, collision-free framework for path following guidance of multiple uncrewed aerial vehicles (UAVs), while maintaining uniform spacing along a reference path. A vector field-based guidance law is employed to drive each UAV toward the reference path. A rotational repulsion mechanism, utilizing relative distance and bearing between UAVs, is proposed to avoid collisions during convergence to the path, and an inter-UAV spacing error-based velocity control law is presented to achieve uniform separation along the path. Analytical guarantees are established for collision avoidance and convergence of the inter-UAV spacing errors to zero, ensuring uniform separation along the path. Numerical simulations demonstrate the efficacy of the proposed method.

---


### 394. [Causally-Constrained Probabilistic Forecasting for Time-Series Anomaly Detection](https://arxiv.org/abs/2604.17998)

**<font color=#1a73e8>作者：</font>** Pooyan Khosravinia, João Gama, Bruno Veloso  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in multivariate time series is a central challenge in industrial monitoring, as failures frequently arise from complex temporal dynamics and cross-sensor interactions. While recent deep learning models, including graph neural networks and Transformers, have demonstrated strong empirical performance, most approaches remain primarily correlational and offer limited support for causal interpretation and root-cause localization. This study introduces a causally-constrained probabilistic forecasting framework which is a Causally Guided Transformer (CGT) model for multivariate time-series anomaly detection, integrating an explicit time-lagged causal graph prior with deep sequence modeling. For each target variable, a dedicated forecasting block employs a hard parent mask derived from causal discovery to restrict the main prediction pathway to graph-supported causes, while a latent Gaussian head captures predictive uncertainty. To leverage residual correlational information without compromising the causal representation, a shadow auxiliary path with stop-gradient isolation and a safety-gated blending mechanism is incorporated to suppress non-causal contributions when reliability is low. Anomalies are identified using negative log-likelihood scores with adaptive streaming thresholding, and root-cause variables are determined through per-dimension probabilistic attribution and counterfactual clamping. Experiments on the ASD and SMD benchmarks indicate that the proposed method achieves state-of-the-art detection performance, with F1-scores of 96.19% on ASD and 95.32% on SMD, and enhances variable-level attribution quality. These findings suggest that causal structural priors can improve both robustness and interpretability in detecting deep anomalies in multivariate sensor systems.

---


### 395. [Trustworthy Endoscopic Super-Resolution](https://arxiv.org/abs/2604.18001)

**<font color=#1a73e8>作者：</font>** Julio Silva-Rodríguez, Ender Konukoglu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-resolution (SR) models are attracting growing interest for enhancing minimally invasive surgery and diagnostic videos under hardware constraints. However, valid concerns remain regarding the introduction of hallucinated structures and amplified noise, limiting their reliability in safety-critical settings. We propose a direct and practical framework to make SR systems more trustworthy by identifying where reconstructions are likely to fail. Our approach integrates a lightweight error-prediction network that operates on intermediate representations to estimate pixel-wise reconstruction error. The module is computationally efficient and low-latency, making it suitable for real-time deployment. We convert these predictions into operational failure decisions by constructing Conformal Failure Masks (CFM), which localize regions where the SR output should not be trusted. Built on conformal risk control principles, our method provides theoretical guarantees for controlling both the tolerated error limit and the miscoverage in detected failures. We evaluate our approach on image and video SR, demonstrating its effectiveness in detecting unreliable reconstructions in endoscopic and robotic surgery settings. To our knowledge, this is the first study to provide a model-agnostic, theoretically grounded approach to improving the safety of real-time endoscopic image SR.

---


### 396. [Neural Garbage Collection: Learning to Forget while Learning to Reason](https://arxiv.org/abs/2604.18002)

**<font color=#1a73e8>作者：</font>** Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning has driven striking advances in language model capability, yet every reasoning step grows the KV cache, creating a bottleneck to scaling this paradigm further. Current approaches manage these constraints on the model's behalf using hand-designed criteria. A more scalable approach would let end-to-end learning subsume this design choice entirely, following a broader pattern in deep learning. After all, if a model can learn to reason, why can't it learn to forget? We introduce Neural Garbage Collection (NGC), in which a language model learns to forget while learning to reason, trained end-to-end from outcome-based task reward alone. As the model reasons, it periodically pauses, decides which KV cache entries to evict, and continues to reason conditioned on the remaining cache. By treating tokens in a chain-of-thought and cache-eviction decisions as discrete actions sampled from the language model, we can use reinforcement learning to jointly optimize how the model reasons and how it manages its own memory: what the model evicts shapes what it remembers, what it remembers shapes its reasoning, and the correctness of that reasoning determines its reward. Crucially, the model learns this behavior entirely from a single learning signal - the outcome-based task reward - without supervised fine-tuning or proxy objectives. On Countdown, AMC, and AIME tasks, NGC maintains strong accuracy relative to the full-cache upper bound at 2-3x peak KV cache size compression and substantially outperforms eviction baselines. Our results are a first step towards a broader vision where end-to-end optimization drives both capability and efficiency in language models.

---


### 397. [Neural Shape Operator Surrogates -- Expression Rate Bounds](https://arxiv.org/abs/2604.18012)

**<font color=#1a73e8>作者：</font>** Helmut Harbrecht, Christoph Schwab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove error bounds for operator surrogates of solution operators for partial differential and boundary integral equations on families of domains which are diffeomorphic to one common reference (or latent) domain $D_{ref}$. The pullback of the PDE to $D_{ref}$ via affine-parametric shape encoding produces a collection of holomorphic parametric PDEs on $D_{ref}$. Sufficient conditions for (uniformly with respect to the parameter) well-posedness are given, implying existence, uniqueness and stability of parametric solution families on $D_{ref}$. We illustrate the abstract hypotheses by reviewing recent holomorphy results for a suite of elliptic and parabolic PDEs.
Quantified parametric holomorphy implies existence of finite-parametric, discrete approximations of the parametric solution families with convergence rates in terms of the number $N$ of parameters. We obtain constructive proofs of existence of Neural and Spectral Operator surrogates for the shape-to-solution maps with error bounds and convergence rate guarantees uniform on the collection of admissible shapes. We admit principal-component shape encoders and frame decoders.
Our results support in particular the (empirically reported) ability of neural operators to realize data-to-solution maps for elliptic and parabolic PDEs and BIEs that generalize across parametric families of shapes.

---


### 398. [Multi-View Hierarchical Graph Neural Network for Sketch-Based 3D Shape Retrieval](https://arxiv.org/abs/2604.18019)

**<font color=#1a73e8>作者：</font>** Hang Cheng, Muyan He, Mingyu Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sketch-based 3D shape retrieval (SBSR) aims to retrieve 3D shapes that are consistent with the category of the input hand-drawn sketch. The core challenge of this task lies in two aspects: existing methods typically employ simplified aggregation strategies for independently encoded 3D multi-view features, which ignore the geometric relationships between views and multi-level details, resulting in weak 3D representation. Simultaneously, traditional SBSR methods are constrained by visible category limitations, leading to poor performance in zero-shot scenarios. To address these challenges, we propose Multi-View Hierarchical Graph Neural Network (MV-HGNN), a novel framework for SBSR. Specifically, we construct a view-level graph and capture adjacent geometric dependencies and cross-view message passing via local graph convolution and global attention. A view selector is further introduced to perform hierarchical graph coarsening, enabling a progressively larger receptive field for graph convolution and mitigating the interference of redundant views, which leads to more discriminate discriminative hierarchical 3D representation. To enable category agnostic alignment and mitigate overfitting to seen classes, we leverage CLIP text embeddings as semantic prototypes and project both sketch and 3D features into a shared semantic space. We use a two-stage training strategy for category-level retrieval and a one-stage strategy for zero-shot retrieval under the same model architecture. Under both category-level and zero-shot settings, extensive experiments on two public benchmarks demonstrate that MV-HGNN outperforms state-of-the-art methods.

---


### 399. [Clusterability-Based Assessment of Potentially Noisy Views for Multi-View Clustering](https://arxiv.org/abs/2604.18024)

**<font color=#1a73e8>作者：</font>** Mudi Jiang, Jiahui Zhou, Xinying Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-view clustering, the quality of different views may vary substantially, and low-quality or degraded views can impair overall clustering performance. However, existing studies mainly address this issue within the clustering process through view weighting or noise-robust optimization, while paying limited attention to data-level assessment before clustering. In this paper, we study the problem of pre-clustering noisy-view analysis in multi-view data from a clusterability perspective. To this end, we propose a Multi-View Clusterability Score (MVCS), which quantifies the strength of latent cluster-related structures in multi-view data through three complementary components: per-view structural clusterability, joint-space clusterability, and cross-view neighborhood consistency. To the best of our knowledge, this is the first clusterability score specifically designed for multi-view data. We further use it to perform potentially noisy view analysis and noisy-view detection before clustering. Extensive experiments on real-world datasets demonstrate that noisy views can significantly degrade clustering performance, and that, compared with existing clusterability measures designed for single-view data, the proposed method more effectively supports noisy-view analysis and detection.

---


### 400. [RASP-Tuner: Retrieval-Augmented Soft Prompts for Context-Aware Black-Box Optimization in Non-Stationary Environments](https://arxiv.org/abs/2604.18026)

**<font color=#1a73e8>作者：</font>** Enze Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many deployed systems expose black-box objectives whose minimizing configuration shifts with an externally observed context. When contexts revisit a small set of latent regimes, an optimizer that discards history pays repeated adaptation cost; when each step must remain inexpensive, full Gaussian-process (GP) refits at high observation counts are difficult to sustain. We cast online tuning as context-conditioned regret minimization and present RASP-Tuner, which instantiates a decomposition motivated by first principles: (i) identify a regime proxy by retrieving similar past contexts; (ii) predict short-horizon loss with a mixture-of-experts surrogate whose input concatenates parameters, context, and a retrieved soft prompt; (iii) adapt chiefly in a low-dimensional prompt subspace, invoking full surrogate updates only when scalarized error or disagreement spikes. A RealErrorComposer maps heterogeneous streaming metrics to [0,1] via EMA-stabilized logistic scores, supplying a single differentiable training target. On nine synthetic non-stationary benchmarks, an adversarial-context sanity check, and three tabular real-world streams (Section on real-world experiments), RASP-Tuner improves or matches cumulative regret relative to our GP-UCB and CMA-ES implementations on seven of nine synthetic tasks under paired tests at horizon T=100, while recording 8-12 times lower wall-clock per step than sliding-window GP-UCB on identical hardware. Idealized analysis in a cluster-separated, strongly convex regime model (RA-GD) supplies sufficient conditions for bounded dynamic regret; the deployed pipeline violates several of these premises, and we articulate which gaps remain open.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
