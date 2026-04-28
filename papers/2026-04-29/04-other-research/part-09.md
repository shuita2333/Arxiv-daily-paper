# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-437**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-437**

---

### 401. [Hierarchical Behaviour Spaces](https://arxiv.org/abs/2604.24558)

**<font color=#1a73e8>作者：</font>** Michael Tryfan Matthews, Anssi Kanervisto, Jakob Foerster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work in hierarchical reinforcement learning has shown success in scaling to billions of timesteps when learning over a set of predefined option reward functions. We show that, instead of using a single reward function per option, the reward functions can be effectively used to induce a space of behaviours, by letting the controller specify linear combinations over reward functions, allowing a more expressive set of policies to be represented. We call this method Hierarchical Behaviour Spaces (HBS). We evaluate HBS on the NetHack Learning Environment, demonstrating strong performance. We conduct a series of experiments and determine that, perhaps going against conventional wisdom, the benefits of hierarchy in our method come from increased exploration rather than long term reasoning.

---


### 402. [Aligned Multi-View Scripts for Universal Chart-to-Code Generation](https://arxiv.org/abs/2604.24559)

**<font color=#1a73e8>作者：</font>** Zhihan Zhang, Lizi Liao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chart-to-code generation converts a chart image into an executable plotting script, enabling faithful reproduction and editable visualizations. Existing methods are largely Python-centric, limiting practical use and overlooking a critical source of supervision: the same chart can be expressed by semantically equivalent scripts in different plotting languages. To fill this gap, we introduce Chart2NCode, a dataset of 176K charts paired with aligned scripts in Python, R, and LaTeX that render visually equivalent outputs, constructed via a metadata-to-template pipeline with rendering verification and human quality checks. Building on a LLaVA-style architecture, we further propose CharLuMA, a parameter-efficient adaptation module that augments the multimodal projector with a language-conditioned mixture of low-rank subspaces, allowing the model to share core chart understanding while specializing code generation to the target language through lightweight routing. Extensive experiments show consistent gains in executability and visual fidelity across all languages, outperforming strong open-source baselines and remaining competitive with proprietary systems. Further analyses reveal that balanced multi-language supervision benefits all languages and that the adapter allocates a compact shared core plus language-specific capacity. Codes and data are available at this https URL.

---


### 403. [Diffusion Model as a Generalist Segmentation Learner](https://arxiv.org/abs/2604.24575)

**<font color=#1a73e8>作者：</font>** Haoxiao Wang, Antao Xiang, Haiyang Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are primarily trained for image synthesis, yet their denoising trajectories encode rich, spatially aligned visual priors. In this paper, we demonstrate that these priors can be utilized for text-conditioned semantic and open-vocabulary segmentation, and this approach can be generalized to various downstream tasks to make a general-purpose diffusion segmentation framework. Concretely, we introduce DiGSeg (Diffusion Models as a Generalist Segmentation Learner), which repurposes a pretrained diffusion model into a unified segmentation framework. Our approach encodes the input image and ground-truth mask into the latent space and concatenates them as conditioning signals for the diffusion U-Net. A parallel CLIP-aligned text pathway injects language features across multiple scales, enabling the model to align textual queries with evolving visual representations. This design transforms an off-the-shelf diffusion backbone into a universal interface that produces structured segmentation masks conditioned on both appearance and arbitrary text prompts. Extensive experiments demonstrate state-of-the-art performance on standard semantic segmentation benchmarks, as well as strong open-vocabulary generalization and cross-domain transfer to medical, remote sensing, and agricultural scenarios-without domain-specific architectural customization. These results indicate that modern diffusion backbones can serve as generalist segmentation learners rather than pure generators, narrowing the gap between visual generation and visual understanding.

---


### 404. [Point-MF: One-step Point Cloud Generation from a Single Image via Mean Flows](https://arxiv.org/abs/2604.24586)

**<font color=#1a73e8>作者：</font>** Yuta Baba, Keiji Yanai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image point cloud reconstruction must infer complete 3D geometry, including occluded parts, from a single RGB image. While diffusion-based reconstructors achieve high accuracy, they typically require many denoising iterations, resulting in slow and expensive inference. We propose Point-MF, a Mean-Flow-based framework for low-NFE single-image point cloud reconstruction that couples a Mean-Flow-compatible architecture with an auxiliary loss. Specifically, Point-MF operates directly in point-cloud space to learn the mean velocity field and enables one-step reconstruction with a single network function evaluation (1-NFE), without relying on VAE-based latent representations. To make Mean Flow effective under large interval jumps, Point-MF employs a Diffusion Transformer tailored to the Mean-Flow setting, conditioned on frozen DINOv3 image features via a lightweight token adapter and equipped with explicit interval/time conditioning. Moreover, we introduce Denoised Space Anchor, a set-distance auxiliary loss on the denoised-space estimate $x_\theta$ induced by the predicted velocity field, to stabilize large-step generation and reduce outliers and density artifacts. On ShapeNet-R2N2 and Pix3D, Point-MF strikes a strong balance between reconstruction quality and inference speed compared to multi-step diffusion baselines and competitive feedforward models, while generating high-quality point clouds with millisecond-level latency.

---


### 405. [Fraud Detection in Cryptocurrency Markets with Spatio-Temporal Graph Neural Networks](https://arxiv.org/abs/2604.24590)

**<font color=#1a73e8>作者：</font>** Lidia Losavio, Luca Persia, Madan Sathe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Technological advancements in cryptocurrency markets have increased accessibility for investors, but concurrently exposed them to the risks of market manipulations. Existing fraud detection mechanisms typically rely on machine learning methods that treat each financial asset (i.e., token) and its related transactions independently. However, market manipulation strategies are rarely isolated events, but are rather characterized by coordination, repetition, and frequent transfers among related assets. This suggests that relational structure constitutes an integral component of the signal and can be effectively represented through graphical means. In this paper, we propose three graph construction methods that rely on aggregated hourly market data. The proposed graphs are processed by a unified spatio-temporal Graph Neural Network (GNN) architecture that combines attention-based spatial aggregation with temporal Transformer encoding. We evaluate our methodology on a real-world dataset comprised of pump-and-dump schemes in cryptocurrency markets, spanning a period of over three years. Our comparative results showcase that our graph-based models achieve significant improvements over standard machine learning baselines in detecting anomalous events. Our work highlights that learned market connectivity provides substantial gains for detecting coordinated market manipulation schemes.

---


### 406. [DETOUR: A Practical Backdoor Attack against Object Detection](https://arxiv.org/abs/2604.24599)

**<font color=#1a73e8>作者：</font>** Dazhuang Liu, Yanqi Qiao, Rui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Object detection (OD) is critical to real-world vision systems, yet existing backdoor attacks on detection transformers (DETRs) for OD tasks rely on patch-wise triggers optimized at fixed locations with minimal perturbations. Such attacks overlook that backdoor triggers in the real world may appear at different sizes, fields of view (FoVs), and locations in images, while minimal perturbations are difficult for cameras to capture, limiting attack practicality. We first observe that a patch-wise trigger in DETR delivers high attack effectiveness when activating the backdoor across neighboring locations, a phenomenon we term the trigger radiating effect (TRE). Meanwhile, inserting patch-wise triggers across multiple locations synergistically enhances TRE, resulting in high attack effectiveness across images. We propose DETOUR, a practical backdoor attack by using semantic triggers that are effective in real-world object detection systems. To ensure attack practicality, we rescale trigger patterns to different sizes and insert them at various predefined locations during backdoor training, enabling the model to recognize the trigger regardless of its spatial configurations. To address FoV variations in physical deployments, we extract the trigger pattern from a real-world object (e.g., a mug) captured under multiple FoVs and inject the trigger accordingly, promoting viewpoint-invariant backdoor activation and enhancing TRE across the entire image. As a result, the backdoor can be reliably activated under diverse FoVs and spatial configurations.

---


### 407. [Children's Online Safety Risks and Ethical Considerations in XR Games](https://arxiv.org/abs/2604.24601)

**<font color=#1a73e8>作者：</font>** Zinan Zhang, Xinning Gui, Yubo Kou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Emerging extended reality technologies are reshaping how children play, learn, and socialize. Yet, they also present serious safety risks. Gaming, a primary form of entertainment for children, is also one of the key applications of XR. While XR platforms offer immersive and engaging gaming experiences, recent news has highlighted safety concerns such as car accidents, lower judgment for real-world situations, and exposure to disturbing content like virtual rape. This research examines how XR game design may lead to online safety risks for children. Through analysis of player forums, game developer forums, and interviews with child players, we identify harmful XR design patterns, explore how developers collaboratively generate and implement risky game ideas, and document children's firsthand experiences of online safety risks. Existing ethical frameworks often fail to address the immersive and socially dynamic nature of XR games. We advocate for a child-centered, design-aware approach to ethical considerations in XR games, urging platforms and policymakers to prioritize children's developmental needs. Our work aims to help shape safer, more inclusive XR environments through research and cross-sector collaboration.

---


### 408. [Evaluation of Pose Estimation Systems for Sign Language Translation](https://arxiv.org/abs/2604.24609)

**<font color=#1a73e8>作者：</font>** Catherine O'Brien, Gerard Sant, Mathias Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many sign language translation (SLT) systems operate on pose sequences instead of raw video to reduce input dimensionality, improve portability, and partially anonymize signers. The choice of pose estimator is often treated as an implementation detail, with systems defaulting to widely available tools such as MediaPipe Holistic or OpenPose. We present a systematic comparison of pose estimators for pose-based SLT, covering widely used baselines (MediaPipe Holistic, OpenPose) and newer whole-body/high-capacity models (MMPose WholeBody, OpenPifPaf, AlphaPose, SDPose, Sapiens, SMPLest-X). We quantify downstream impact by training a controlled SLT pipeline on RWTH-PHOENIX-Weather 2014 where only the pose representation varies, evaluating with BLEU and BLEURT.
To contextualize translation outcomes, we analyze temporal stability, missing hand keypoints, and robustness to occlusion using higher-resolution videos from the Signsuisse dataset. SDPose and Sapiens achieve the best translation performance (BLEU ~11.5), outperforming the common MediaPipe baseline (BLEU ~10). In occlusion cases, Sapiens is correct in all tested instances (15/15), while OpenPifPaf fails in nearly all (1/15) and also yields the weakest translation scores. Estimators that frequently leave out hand keypoints are associated with lower BLEU/BLEURT. We release code that can be used not only to reproduce our experiments, but also considerably lowers the barrier for other researchers to use alternative pose estimators.

---


### 409. [Uncovering Latent Patterns in Social Media Usage and Mental Health: A Clustering-Based Approach Using Unsupervised Machine Learning](https://arxiv.org/abs/2604.24611)

**<font color=#1a73e8>作者：</font>** Md All Shahria, Sanjeda Dewan Mithila, Touhid Alam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of social media has heightened interest in its psychological effects, particularly on mental health indicators such as anxiety, depression, loneliness, and sleep quality, as these platforms increasingly influence social interactions and well-being. Although previous research has examined correlations between social media use and mental health, few studies have utilized unsupervised machine learning to segment users based on behavioral and psychological patterns, leaving a gap in identifying distinct risk profiles across diverse groups. This study seeks to address this by segmenting individuals according to their social media usage and psychological well-being, employing clustering to reveal hidden patterns and evaluate their mental health implications. Data from 551 participants, collected via an online survey, were preprocessed using KNN imputation for missing values, one-hot encoding for categorical variables like Gender with 5 unique values, and outlier detection via IQR and Z-score methods. K-Means clustering, optimized at 6 clusters using the Elbow Method and a Silhouette Score of 0.32, was applied, with PCA reducing 22 dimensions for visualization and a correlation heatmap highlighting relationships, such as a 0.28 correlation between social media hours and anxiety.

---


### 410. [NeSyCat: A Monad-Based Categorical Semantics of the Neurosymbolic ULLER Framework](https://arxiv.org/abs/2604.24612)

**<font color=#1a73e8>作者：</font>** Daniel Romero Schellhorn, Till Mossakowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ULLER (Unified Language for LEarning and Reasoning) offers a unified first-order logic (FOL) syntax, enabling its knowledge bases to be used directly across a wide range of neurosymbolic systems. The original specification endows this syntax with three pairwise independent semantics: classical, fuzzy, and probabilistic, each accompanied by dedicated semantic rules. We show that these seemingly disparate semantics are all instances of one categorical framework based on monads, the very construct that models side effects in functional programming. This enables the modular addition of new semantics and systematic translations between them. As example, we outline the addition of generalised quantification in Logic Tensor Networks (LTN) to arbitrary (also infinite) domains by extending the Giry monad to probability spaces. In particular, our approach allows a modular implementation of ULLER in Python and Haskell, of which we have published initial versions on GitHub.

---


### 411. [Infrastructure-Guided Connectivity-Enhanced Road Crack Detection and Estimation](https://arxiv.org/abs/2604.24616)

**<font color=#1a73e8>作者：</font>** Haosong Xiao, Yamini Ramesh, Rishabh Shukla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we report the world's first infrastructure-guided communication-enhanced road crack detection pipeline that is effective and implementable on passenger vehicles. We first design a customized communication protocol to transmit the region of interest from the infrastructure to the vehicle. With proper camera image processing (e.g., dynamic cropping and frame selection), the focused images are provided to the crack detection model. Leveraging state-of-the-art crack detection model backbones and a carefully prepared dataset comprising a forward-facing view with a crack, we train the model to improve crack-detection performance. We demonstrate the full detection pipeline on an experimental vehicle platform, showcase the detection effectiveness, and project future research directions.

---


### 412. [Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618)

**<font color=#1a73e8>作者：</font>** Robert Kirk, Alexandra Souly, Kai Fronsdal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate the propensity of frontier models to sabotage or refuse to assist with safety research when deployed as AI research agents within a frontier AI company. We apply two complementary evaluations to four Claude models (Mythos Preview, Opus 4.7 Preview, Opus 4.6, and Sonnet 4.6): an unprompted sabotage evaluation testing model behaviour with opportunities to sabotage safety research, and a sabotage continuation evaluation testing whether models continue to sabotage when placed in trajectories where prior actions have started undermining research. We find no instances of unprompted sabotage across any model, with refusal rates close to zero for Mythos Preview and Opus 4.7 Preview, though all models sometimes only partially completed tasks. In the continuation evaluation, Mythos Preview actively continues sabotage in 7% of cases (versus 3% for Opus 4.6, 4% for Sonnet 4.6, and 0% for Opus 4.7 Preview), and exhibits reasoning-output discrepancy in the majority of these cases, indicating covert sabotage reasoning. Our evaluation framework builds on Petri, an open-source LLM auditing tool, with a custom scaffold running models inside Claude Code, alongside an iterative pipeline for generating realistic sabotage trajectories. We measure both evaluation awareness and a new form of situational awareness termed "prefill awareness", the capability to recognise that prior trajectory content was not self-generated. Opus 4.7 Preview shows notably elevated unprompted evaluation awareness, while prefill awareness remains low across all models. Finally, we discuss limitations including evaluation awareness confounds, limited scenario coverage, and untested pathways to risk beyond safety research sabotage.

---


### 413. [Looking for the Bottleneck in Fine-grained Temporal Relation Classification](https://arxiv.org/abs/2604.24620)

**<font color=#1a73e8>作者：</font>** Hugo Sousa, Ricardo Campos, Alípio Jorge  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal relation classification is the task of determining the temporal relation between pairs of temporal entities in a text.
Despite recent advancements in natural language processing, temporal relation classification remains a considerable challenge.
Early attempts framed this task using a comprehensive set of temporal relations between events and temporal expressions.
However, due to the task complexity, datasets have been progressively simplified, leading recent approaches to focus on the relations between event pairs and to use only a subset of relations.
In this work, we revisit the broader goal of classifying interval relations between temporal entities by considering the full set of relations that can hold between two time intervals.
The proposed approach, Interval from Point, involves first classifying the point relations between the endpoints of the temporal entities and then decoding these point relations into an interval relation.
Evaluation on the TempEval-3 dataset shows that this approach can yield effective results, achieving a temporal awareness score of $70.1$ percent, a new state-of-the-art on this benchmark.

---


### 414. [CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2604.24622)

**<font color=#1a73e8>作者：</font>** Fan Du, Feng Yan, Jianxiong Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structure from uninformative Gaussian noise, leading to a poor efficiency-quality trade-off under real-time constraints. We address this issue by rethinking the role of the starting point in generative action modeling. Instead of shortening the sampling trajectory, we propose CF-VLA, a coarse-to-fine two-stage formulation that restructures action generation into a coarse initialization step that constructs an action-aware starting point, followed by a single-step local refinement that corrects residual errors. Concretely, the coarse stage learns a conditional posterior over endpoint velocity to transform Gaussian noise into a structured initialization, while the fine stage performs a fixed-time refinement from this initialization. To stabilize training, we introduce a stepwise strategy that first learns a controlled coarse predictor and then performs joint optimization. Experiments on CALVIN and LIBERO show that our method establishes a strong efficiency-performance frontier under low-NFE (Number of Function Evaluations) regimes: it consistently outperforms existing NFE=2 methods, matches or surpasses the NFE=10 $\pi_{0.5}$ baseline on several metrics, reduces action sampling latency by 75.4\%, and achieves the best average real-robot success rate of 83.0\%, outperforming MIP by 19.5 points and $\pi_{0.5}$ by 4.0 points. These results suggest that structured, coarse-to-fine generation enables both strong performance and efficient inference. Our code is available at this https URL.

---


### 415. [Meta-CoT: Enhancing Granularity and Generalization in Image Editing](https://arxiv.org/abs/2604.24625)

**<font color=#1a73e8>作者：</font>** Shiyi Zhang, Yiji Cheng, Tiankai Hang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multi-modal understanding/generative models have shown improved image editing performance by incorporating fine-grained understanding into their Chain-of-Thought (CoT) process. However, a critical question remains underexplored: what forms of CoT and training strategy can jointly enhance both the understanding granularity and generalization? To address this, we propose Meta-CoT, a paradigm that performs a two-level decomposition of any single-image editing operation with two key properties: (1) Decomposability. We observe that any editing intention can be represented as a triplet - (task, target, required understanding ability). Inspired by this, Meta-CoT decomposes both the editing task and the target, generating task-specific CoT and traversing editing operations on all targets. This decomposition enhances the model's understanding granularity of editing operations and guides it to learn each element of the triplet during training, substantially improving the editing capability. (2) Generalizability. In the second decomposition level, we further break down editing tasks into five fundamental meta-tasks. We find that training on these five meta-tasks, together with the other two elements of the triplet, is sufficient to achieve strong generalization across diverse, unseen editing tasks. To further align the model's editing behavior with its CoT reasoning, we introduce the CoT-Editing Consistency Reward, which encourages more accurate and effective utilization of CoT information during editing. Experiments demonstrate that our method achieves an overall 15.8% improvement across 21 editing tasks, and generalizes effectively to unseen editing tasks when trained on only a small set of meta-tasks. Our code, benchmark, and model are released at this https URL

---


### 416. [Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks](https://arxiv.org/abs/2604.24637)

**<font color=#1a73e8>作者：</font>** Kevin McKee, Thomas Hazy, Yicong Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block-sequential continual learning demands that a single model both protect prior solutions from catastrophic forgetting and efficiently infer at inference time which prior solution matches the current input without task labels. We present Functional Task Networks (FTN), a parameter-isolation method inspired by structural and dynamical motifs found in the mammalian neocortex. Similar to mixture-of-experts, this method uses a high dimensional, self-organizing binary mask over a large population of small but deep networks, inspired by dendritic models of pyramidal neurons. The mask is produced by a three-stage procedure: (1) gradient descent on a continuous mask identifies task-relevant neurons, (2) a smoothing kernel biases the result toward spatial contiguity, (3) and k-winner-take-all binarizes the resulting group at a fixed capacity budget. Like mixture-of-experts, each neuron is an independent deep network, so disjoint masks give exactly disjoint gradient updates, providing structural guarantees against catastrophic forgetting. This three-stage procedure recovers the sub-network of a previously-trained task in a single gradient step, providing unsupervised task segmentation at inference time. We test it on three continual-learning benchmarks: (1) a synthetic multi-task classification/regression generator, (2) MNIST with shuffled class labels (pure concept shift), and (3) Permuted MNIST (domain shift). On all three, FTN with fine grained smoothing (FTN-Slow) results in nearly zero forgetting. FTN with a large kernel and only 2 iterations of smoothing (FTN-Fast) trades off some retention for increased speed. We show that the spatial organization mechanism reduces the effective mask search from the combinatorial top-k subset problem in O(C(H,K)) to the complexity of a near-linear scan in O(H) over compact cortical neighborhoods, which is parallelized by the gradient-based update.

---


### 417. [ARCANE: Cross-Campaign Attacker Re-identification via Passive Beacon Telemetry -- A Bayesian Network Framework for Longitudinal Cyber Attribution](https://arxiv.org/abs/2604.24644)

**<font color=#1a73e8>作者：</font>** Abraham Itzhak Weinberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current cyber attribution approaches typically operate on a per-incident basis, leaving open whether aggregating evidence across campaigns improves adversary identification. We investigate whether cross-campaign attribution reduces ambiguity or whether structural limits persist under longitudinal data. We model adversary fingerprints as multi-dimensional feature vectors encoding behavioral, infrastructural, and temporal characteristics derived from covert beacon interactions. We introduce ARCANE (Attacker Re-identification via Cross-campaign Attribution Network), a probabilistic framework that aggregates passive telemetry across campaigns and organizations to construct persistent adversary fingerprints. These fingerprints are updated using a Bayesian belief network that integrates new evidence over time. A time-decayed confidence metric captures accumulated similarity across campaigns. Evaluation on a synthetic dataset of multiple threat profiles shows that intra-actor similarity consistently exceeds inter-actor similarity. However, separation between distinct actors remains limited due to shared operational practices among sophisticated adversaries. Results indicate that cross-campaign aggregation alone does not resolve attribution ambiguity. Performance is constrained by a structural ceiling in feature space, where inter-actor similarity remains high even without evasion. Attribution accuracy remains stable under increasing evasion, suggesting the main limitation is feature indistinguishability rather than adversarial adaptation. These findings highlight the need for additional signal classes, such as targeting patterns, temporal coordination, and infrastructure relationships, to improve attribution reliability.

---


### 418. [AgentWard: A Lifecycle Security Architecture for Autonomous AI Agents](https://arxiv.org/abs/2604.24657)

**<font color=#1a73e8>作者：</font>** Yixiang Zhang, Xinhao Deng, Jiaqing Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents extend large language models into full runtime systems that load skills, ingest external content, maintain memory, plan multi-step actions, and invoke privileged tools. In such systems, security failures rarely remain confined to a single interface; instead, they can propagate across initialization, input processing, memory, decision-making, and execution, often becoming apparent only when harmful effects materialize in the environment. This paper presents AgentWard, a lifecycle-oriented, defense-in-depth architecture that systematically organizes protection across these five stages. AgentWard integrates stage-specific, heterogeneous controls with cross-layer coordination, enabling threats to be intercepted along their propagation paths while safeguarding critical assets. We detail the design rationale and architecture of five coordinated protection layers, and implement a plugin-native prototype on OpenClaw to demonstrate practical feasibility. This perspective provides a concrete blueprint for structuring runtime security controls, managing trust propagation, and enforcing execution containment in autonomous AI agents. Our code is available at this https URL .

---


### 419. [The Last Human-Written Paper: Agent-Native Research Artifacts](https://arxiv.org/abs/2604.24658)

**<font color=#1a73e8>作者：</font>** Jiachen Liu, Jiaxin Pei, Jintao Huang 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way. This compilation imposes two structural costs: a Storytelling Tax, where failed experiments, rejected hypotheses, and the branching exploration process are discarded to fit a linear narrative; and an Engineering Tax, where the gap between reviewer-sufficient prose and agent-sufficient specification leaves critical implementation details unwritten. Tolerable for human readers, these costs become critical when AI agents must understand, reproduce, and extend published work. We introduce the Agent-Native Research Artifact (Ara), a protocol that replaces the narrative paper with a machine-executable research package structured around four layers: scientific logic, executable code with full specifications, an exploration graph that preserves the failures compilation discards, and evidence grounding every claim in raw outputs. Three mechanisms support the ecosystem: a Live Research Manager that captures decisions and dead ends during ordinary development; an Ara Compiler that translates legacy PDFs and repos into Aras; and an Ara-native review system that automates objective checks so human reviewers can focus on significance, novelty, and taste. On PaperBench and RE-Bench, Ara raises question-answering accuracy from 72.4% to 93.7% and reproduction success from 57.4% to 64.4%. On RE-Bench's five open-ended extension tasks, preserved failure traces in Ara accelerate progress, but can also constrain a capable agent from stepping outside the prior-run box depending on the agent's capabilities.

---


### 420. [Machine-Checked Cardinality Bounds for Masked Barrett Reduction: A 1-Bit Side-Channel Leakage Barrier in Post-Quantum Cryptographic Hardware](https://arxiv.org/abs/2604.24670)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Barrett reduction is the nonlinear core of every practical NTT-based post-quantum cryptography implementation. Existing composition frameworks (ISW, t-SNI, PINI, DOM) address Boolean masking over GF(2); none provides a machine-checked characterization of Barrett's leakage under first-order arithmetic masking and the first-order probing model over prime fields. Building on our prior series, QANARY [15], partial-NTT-masking margins [14], algebraic foundations [16], and butterfly composition [18], we close this gap. We prove a trichotomy: for any $q > 0$ and shift $s$, the Barrett internal wire map $f_x(m) = ((x + 2^s - m) \bmod 2^s) \bmod q$ has preimage cardinality in $\{0, 1, 2\}$, never more. We call this the 1-Bit Barrier: max-multiplicity 2 implies at most 1 bit of min-entropy loss per internal wire, universal over all moduli. The count-zero cases, unreachable output values, reveal that actual leakage is often strictly less than 1 bit, making the bound conservative. We introduce PF-PINI (Prime-Field PINI): Barrett satisfies PF-PINI(2); the Cooley-Tukey butterfly satisfies PF-PINI(1). We observe (not yet proved) that with fresh inter-stage masking, the composed pipeline has max-multiplicity $\max(k_1, k_2)$, so the 1-Bit Barrier propagates. The trichotomy, the PF-PINI instantiations, and cardinality results are machine-checked in Lean 4 with Mathlib: 12 proved results, zero sorry, universal over all $q > 0$ (the min-entropy bound follows by standard definitions). Adams Bridge lacks fresh inter-stage masking, violating PF-PINI composition and explaining why Papers 1 [15] and 2 [14] found vulnerabilities. NIST IR 8547 recommends formal methods for PQC implementation validation. The 1-Bit Barrier provides the first universal machine-checked cardinality bound for masked Barrett reduction in ML-KEM (FIPS 203) and ML-DSA (FIPS 204), with a corresponding 1-bit leakage interpretation.

---


### 421. [A Functorial Formulation of Neighborhood Aggregating Deep Learning](https://arxiv.org/abs/2604.24672)

**<font color=#1a73e8>作者：</font>** Sun Woo Park, Yun Young Choi, U Jin Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We provide a mathematical interpretation of convolutional (or message passing) neural networks by using presheaves and copresheaves of the set of continuous functions over a topological space. Based on this interpretation, we formulate a theoretical heuristic which elaborates a number of empirical limitations of these neural networks by using obstructions on such sets of continuous functions over a topological space to be sheaves or copresheaves.

---


### 422. [Aycromo: An Open-Source Platform for Automatic Chromosome Detection in Metaphase Images Based on Deep Learning](https://arxiv.org/abs/2604.24685)

**<font color=#1a73e8>作者：</font>** Jorge L. A. Lima, Filipe R. Cordeiro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chromosome analysis is a fundamental step in the diagnosis of genetic diseases, but the manual karyotyping workflow is time-consuming and heavily dependent on expert specialists, often requiring several days per patient. Although Deep Learning models have achieved high performance in chromosome detection, most proposed solutions remain restricted to research prototypes or lack graphical interfaces suitable for clinical use. In this work, we present Aycromo, an open-source desktop platform for AI-assisted cytogenetic analysis. Built on Electron and ONNX Runtime, the tool allows cytogeneticists to load pre-trained models, compare architectures through an integrated benchmarking module, and manually correct detections via an interactive annotation interface, all without command-line interaction. Preliminary experiments on metaphase images from the CRCN-NE dataset demonstrate that YOLOv11 achieves 99.40% mAP@50, while the platform reduces per-slide analysis to seconds

---


### 423. [Governing What You Cannot Observe: Adaptive Runtime Governance for Autonomous AI Agents](https://arxiv.org/abs/2604.24686)

**<font color=#1a73e8>作者：</font>** German Marin, Jatin Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents can remain fully authorized and still become unsafe as behavior drifts, adversaries adapt, and decision patterns shift without any code change. We propose the \textbf{Informational Viability Principle}: governing an agent reduces to estimating a bound on unobserved risk $\hat{B}(x) = U(x) + SB(x) + RG(x)$ and allowing an action only when its capacity $S(x)$ exceeds $\hat{B}(x)$ by a safety margin. The \textbf{Agent Viability Framework}, grounded in Aubin's viability theory, establishes three properties -- monitoring (P1), anticipation (P2), and monotonic restriction (P3) -- as individually necessary and collectively sufficient for documented failure modes. \textbf{RiskGate} instantiates the framework with dedicated statistical estimators (KL divergence, segment-vs-rest $z$-tests, sequential pattern matching), a fail-secure monotonic pipeline, and a closed-loop Autopilot formalised as an instance of Aubin's regulation map with kill-switch-as-last-resort; a scalar Viability Index $VI(t) \in [-1,+1]$ with first-order $t^*$ prediction transforms governance from reactive to predictive. Contributions are the theoretical framework, the reference implementation, and analytical coverage against published agent-failure taxonomies; quantitative empirical evaluation is scoped as follow-up work.

---


### 424. [Diffusion-Guided Feature Selection via Nishimori Temperature: Noise-Based Spectral Embedding](https://arxiv.org/abs/2604.24692)

**<font color=#1a73e8>作者：</font>** Vasiliy S. Usatyuk, Denis A. Sapozhnikov, Sergey I. Egorov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Noise-Based Spectral Embedding (NBSE), a physics-informed framework for selecting informative features from high-dimensional data without greedy search. NBSE constructs a sparse similarity graph on the samples and identifies the Nishimori temperature $\beta_N$ the critical inverse temperature at which the Bethe Hessian becomes singular. The corresponding smallest eigenvector captures the dominant mode of an intrinsically degree-corrected diffusion process, naturally reweighting nodes to prevent hub dominance. By transposing the data matrix and applying NBSE in feature space, we obtain a one-dimensional spectral embedding that reveals groups of redundant or semantically related dimensions; balanced binning then selects one representative per group. We prove that coloured Gaussian perturbations shift $\beta_N$ by at most $O(\bar\sigma^2)$, guaranteeing robustness to measurement noise. Experiments on ImageNet embeddings from MobileNetV2 and EfficientNet-B4 show that NBSE preserves classification accuracy even under aggressive compression: on EfficientNet-B4 the accuracy drop is below $1\%$ when retaining only $30\%$ of features, outperforming ANOVA $F$-test and random selection by up to $6.8\%$.

---


### 425. [NeuroClaw Technical Report](https://arxiv.org/abs/2604.24696)

**<font color=#1a73e8>作者：</font>** Cheng Wang, Zhibin He, Zhihao Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence systems promise to accelerate scientific workflows, but neuroimaging poses unique challenges: heterogeneous modalities (sMRI, fMRI, dMRI, EEG), long multi-stage pipelines, and persistent reproducibility risks. To address this gap, we present NeuroClaw, a domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research. NeuroClaw operates directly on raw neuroimaging data across formats and modalities, grounding decisions in dataset semantics and BIDS metadata so users need not prepare curated inputs or bespoke model code. The platform combines harness engineering with end-to-end environment management, including pinned Python environments, Docker support, automated installers for common neuroimaging tools, and GPU configuration. In practice, this layer emphasizes checkpointing, post-execution verification, structured audit traces, and controlled runtime setup, making toolchains more transparent while improving reproducibility and auditability. A three-tier skill/agent hierarchy separates user-facing interaction, high-level orchestration, and low-level tool skills to decompose complex workflows into safe, reusable units. Alongside the NeuroClaw framework, we introduce NeuroBench, a system-level benchmark for executability, artifact validity, and reproducibility readiness. Across multiple multimodal LLMs, NeuroClaw-enabled runs yield consistent and substantial score improvements compared with direct agent invocation. Project homepage: this https URL

---


### 426. [Profiling Resilient to Change in Probe Position](https://arxiv.org/abs/2604.24701)

**<font color=#1a73e8>作者：</font>** Elie Bursztein, Michael Gruber, Karel Král 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Side Channel Analysis (SCA) relaxes the black-box assumption of conventional cryptanalysis by incorporating physical measurements acquired during cryptographic operations. Electro-magnetic (EM) emissions of a chip during computations often provide a very valuable source of side channel leakage. During the evaluation of a chip for electro-magnetic side channel emissions one needs to position an electro-magnetic probe in an advantageous position relative to the chip. Previous literature focused on hot-spot finding and to a lower extend repositioning. Trace augmentations have been considered to aid portability of profiling using one physical device and attacking another device. This paper focuses on training a single neural network using traces from multiple EM probe positions to detect leakage from a larger area over the attacked device. We provide dual evaluation of EM traces - from two completely independent labs - profiling on data from one lab and attacking traces from the other lab.

---


### 427. [Scalable Hyperparameter-Divergent Ensemble Training with Automatic Learning Rate Exploration for Large Models](https://arxiv.org/abs/2604.24708)

**<font color=#1a73e8>作者：</font>** Hailing Cheng, Tao Huang, Chen Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large neural networks with data-parallel stochastic gradient descent allocates N GPU replicas to compute effectively identical updates -- a practice that leaves the rich space of learning rate configurations entirely unexplored during training. We propose Hyperparameter-Divergent Ensemble Training (HDET), a method that repurposes these replicas for simultaneous learning rate exploration at negligible communication overhead. HDET operates in alternating phases: a fan-out stage in which replicas train independently under a structured, symmetric spread of learning rates, and a converge stage in which parameters are averaged across all replicas via AllReduce every T steps. Building on this ensemble substrate, we further propose an automatic learning rate (auto-LR) controller that treats the relative training loss across replicas as a performance signal, updating the shared base schedule toward higher-performing configurations via a momentum-based gradient-free meta-update. The combined method produces a self-adapting learning rate schedule that improves both optimization quality and generalization without additional hyperparameter sweeps or training budget.
Crucially, the framework generalizes beyond learning rate: any scalar hyperparameter that does not alter model architecture -- such as dropout rate, attention scale temperature, or weight-decay coefficient -- can be explored across replicas using the same fan-out/converge protocol, with inter-replica loss differences serving as zero-order hypergradients that guide the search direction. HDET is implemented as a drop-in replacement for PyTorch's OneCycleLR scheduler, requiring no changes to model architecture, optimizer, or data pipeline.

---


### 428. [Learning to Rotate: Temporal and Semantic Rotary Encoding for Sequential Modeling](https://arxiv.org/abs/2604.24717)

**<font color=#1a73e8>作者：</font>** Hailing Cheng, Daqi Sun, Xinyu Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every Transformer architecture dedicates enormous capacity to learning rich representations in semantic embedding space -- yet the rotation manifold acted upon by Rotary Positional Embeddings (RoPE) has been treated as a fixed, hand-crafted structure, populated only by discrete ordinal indices. We argue that this rotation space is a largely overlooked second dimension of expressivity in the attention mechanism, one whose systematic exploration may open a new door for attention-based architectures. The analogy to complex numbers is instructive: just as introducing the imaginary axis -- orthogonal to and independent of the real line -- unlocked new algebraic structure once believed impossible, treating the rotation manifold as a learnable, signal-conditioned space opens an orthogonal degree of freedom in attention. In this framing, the token embedding encodes the semantic (real) component of a representation -- what a token means -- while the rotation encodes its dynamic (imaginary) component -- how it relates to every other token across time, position, and context.
We introduce SIREN-RoPE, a concrete instantiation of this idea, which populates the rotation dimension with heterogeneous signals -- continuous timestamps, cyclical temporal patterns, and categorical metadata -- via a dual-branch Sinusoidal Representation Network (SIREN). As a proof of concept, we evaluate on a production-scale news feed dataset from a major social network using a generative recommender as the ranking model, demonstrating that activating this hidden dimension yields consistent improvements across calibration and ranking objectives with negligible computational overhead. We invite the community to view the rotation space not as a solved positional-encoding detail, but as an untapped axis whose rich structure may prove as consequential for attention as the imaginary unit proved for algebra.

---


### 429. [WildLIFT: Lifting monocular drone video to 3D for species-agnostic wildlife monitoring](https://arxiv.org/abs/2604.24718)

**<font color=#1a73e8>作者：</font>** Vandita Shukla, Fabio Remondino, Blair Costelloe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular RGB cameras mounted on drones are widely used for wildlife monitoring, yet most analytical pipelines remain confined to two-dimensional image space, leaving geometric information in video underexploited. We present WildLIFT, a computational framework that integrates three-dimensional scene geometry from monocular drone video with open-vocabulary 2D instance segmentation to enable species-agnostic 3D detection and tracking. Oriented 3D bounding box labels with semantic face information enable quantitative assessment of viewpoint coverage and inter-animal occlusion, producing structured metadata for downstream ecological analyses. We validate the framework on 2,581 manually curated frames comprising over 6,700 3D detections across four large mammal species. WildLIFT maintains high identity consistency in multi-animal scenes and substantially reduces manual 3D annotation effort through keyframe-based refinement. By transforming standard drone footage into structured 3D and viewpoint-aware representations, WildLIFT extends the analytical utility of aerial wildlife datasets for behavioural research and population monitoring.

---


### 430. [DiffuSAM: Diffusion-Based Prompt-Free SAM2 for Few-Shot and Source-Free Medical Image Segmentation](https://arxiv.org/abs/2604.24719)

**<font color=#1a73e8>作者：</font>** Tal Grossman, Noa Cahan, Lev Ayzenberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation models such as Segment Anything Model (SAM) and SAM2 achieve strong prompt-driven zero-shot performance. However, their training on natural images limits domain transfer to medical data. Consequently, accurate segmentation typically requires extensive fine-tuning and expert-designed prompts. We propose DiffuSAM, a diffusion-based adaptation of SAM2 for prompt-free medical image segmentation. Our framework synthesizes SAM2-compatible segmentation mask-like embeddings via a lightweight diffusion-prior from off-the-shelf frozen SAM2 image features. The generated embeddings are integrated into SAM2's mask decoder to produce accurate segmentations, thereby eliminating the need for user prompts. The diffusion prior is further conditioned on previously segmented slices, enforcing spatial consistency across volumes. Evaluated on the BTCV and CHAOS datasets for CT and MRI under Source-Free Unsupervised Domain Adaptation (SF-UDA) and Few-Shot settings, DiffuSAM achieves competitive performance with efficient training and inference. Code is available upon request from the corresponding author.

---


### 431. [Sentiment and Emotion Classification of Indonesian E-Commerce Reviews via Multi-Task BiLSTM and AutoML Benchmarking](https://arxiv.org/abs/2604.24720)

**<font color=#1a73e8>作者：</font>** Hermawan Manurung, Ibrahim Al-Kahfi, Ahmad Rizqi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Indonesian marketplace reviews mix standard vocabulary with slang, regional loanwords, numeric shorthands, and emoji, making lexicon-based sentiment tools unreliable in practice. This paper describes a two-track classification pipeline applied to the PRDECT-ID dataset, which contains 5,400 product reviews from 29 Indonesian e-commerce categories, each labeled for binary sentiment (Positive/Negative) and five-class emotion (Happy, Sad, Fear, Love, Anger). The first track applies TF-IDF vectorization with a PyCaret AutoML sweep across standard classifiers. The second track is a PyTorch Bidirectional Long Short-Term Memory (BiLSTM) network with a shared encoder and two task-specific output heads. A preprocessing module applies 14 sequential cleaning steps, including a 140-entry slang dictionary assembled from marketplace corpora. Four configurations are benchmarked: BiLSTM Baseline, BiLSTM Improved, BiLSTM Large, and TextCNN. Training uses class-weighted cross-entropy loss, ReduceLROnPlateau scheduling, and early stopping. Both tracks are deployed as Gradio applications on Hugging Face Spaces. Source code is publicly available at this https URL.

---


### 432. [SpecRLBench: A Benchmark for Generalization in Specification-Guided Reinforcement Learning](https://arxiv.org/abs/2604.24729)

**<font color=#1a73e8>作者：</font>** Zijian Guo, İlker Işık, H. M. Sabbir Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specification-guided reinforcement learning (RL) provides a principled framework for encoding complex, temporally extended tasks using formal specifications such as linear temporal logic (LTL). While recent methods have shown promising results, their ability to generalize across unseen specifications and diverse environments remains insufficiently understood. In this work, we introduce SpecRLBench, a benchmark designed to evaluate the generalization capabilities of LTL-based specification-guided RL methods. The benchmark spans multiple difficulty levels across navigation and manipulation domains, incorporating both static and dynamic environments, diverse robot dynamics, and varied observation modalities. Through extensive empirical evaluation, we characterize the strengths and limitations of existing approaches and reveal the challenges that emerge as specification and environment complexity increase. SpecRLBench provides a structured platform for systematic comparison and supports the development of more generalizable specification-guided RL methods. Code is available at this https URL.

---


### 433. [Learning to Think from Multiple Thinkers](https://arxiv.org/abs/2604.24737)

**<font color=#1a73e8>作者：</font>** Nirmit Joshi, Roey Magen, Nathan Srebro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning with Chain-of-Thought (CoT) supervision from multiple thinkers, all of whom provide correct but possibly systematically different solutions, e.g., step-by-step solutions to math problems written by different thinkers, or step-by-step execution traces of different programs solving the same problem.
We consider classes that are computationally easy to learn using CoT supervision from a single thinker, but hard to learn with only end-result supervision, i.e., without CoT (Joshi et al. 2025). We establish that, under cryptographic assumptions, learning can be hard from CoT supervision provided by two or a few different thinkers, in passive data-collection settings.
On the other hand, we provide a generic computationally efficient active learning algorithm that learns with a small amount of CoT data per thinker that is completely independent of the target accuracy $\varepsilon$, a moderate number of thinkers that scales as $\log \frac{1}{\varepsilon}\log \log \frac{1}{\varepsilon}$, and sufficient passive end-result data that scales as $\frac{1}{\varepsilon}\cdot poly\log\frac{1}{\varepsilon}$.

---


### 434. [Conflict-Aware Harmonized Rotational Gradient for Multiscale Kinetic Regimes](https://arxiv.org/abs/2604.24745)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a harmonized rotational gradient method, termed HRGrad, for simultaneously tackling multiscale time-dependent kinetic problems with varying small parameters.
These parameters exhibit asymptotic transitions from microscopic to macroscopic physics, making it a challenging multi-task problem to solve over all ranges simultaneously.
Solving tasks in different asymptotic regions often encounter gradient conflicts, which can lead to the failure of multi-task learning.
To address this challenge, we explicitly encode a hidden representation of these parameters, ensuring that the corresponding solving tasks are serialized for simultaneous training.
Furthermore, to mitigate gradient conflicts, we segment the prediction results to construct task losses and introduce a novel gradient alignment metric to ensure a positive dot product between the final update and each loss-specific gradient.
This metric maintains consistent optimization rates for all task losses and dynamically adjusts gradient magnitudes based on conflict levels.
Moreover, we provide a mathematical proof demonstrating the convergence of the HRGrad method, which is evaluated across a range of challenging asymptotic-preserving neural networks (APNNs) scenarios.
We conduct an extensive set of experiments encompassing the Bhatnagar-Gross-Krook (BGK) equation and the linear transport equation in all ranges of Knudsen number.
Our results indicate that HRGrad effectively overcomes the `failure modes' of APNNs in these problems.

---


### 435. [The Optimal Sample Complexity of Multiclass and List Learning](https://arxiv.org/abs/2604.24749)

**<font color=#1a73e8>作者：</font>** Chirag Pabbaraju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While the optimal sample complexity of binary classification in terms of the VC dimension is well-established, determining the optimal sample complexity of multiclass classification has remained open. The appropriate complexity parameter for multiclass classification is the DS dimension, and despite significant efforts, a gap of $\sqrt{\text{DS}}$ has persisted between the upper and lower bounds on sample complexity.
Recent work by Hanneke et al. (2026) shows a novel algebraic characterization of multiclass hypothesis classes in terms of their DS dimension. Building up on this, we show that the maximum hypergraph density of any multiclass hypothesis class is upper-bounded by its DS dimension. This proves a longstanding conjecture of Daniely and Shalev-Shwartz (2014). As a consequence, we determine the optimal dependence of the sample complexity on the DS dimension for multiclass as well as list learning.

---


### 436. [Personalized Worked Example Generation from Student Code Submissions using Pattern-based Knowledge Components](https://arxiv.org/abs/2604.24758)

**<font color=#1a73e8>作者：</font>** Griffin Pitts, Muntasir Hoq, Peter Brusilovsky 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adaptive programming practice often relies on fixed libraries of worked examples and practice problems, which require substantial authoring effort and may not correspond well to the logical errors and partial solutions students produce while writing code. As a result, students may receive learning content that does not directly address the concepts they are working to understand, while instructors must either invest additional effort in expanding content libraries or accept a coarse level of personalization. We present an approach for knowledge-component (KC) guided educational content generation using pattern-based KCs extracted from student code. Given a problem statement and student submissions, our pipeline extracts recurring structural KC patterns from students' code through AST-based analysis and uses them to condition a generative model. In this study, we apply this approach to worked example generation, and compare baseline and KC-conditioned outputs through expert evaluation. Results suggest that KC-conditioned generation improves topical focus and relevance to learners' underlying logical errors, providing evidence that KC-based steering of generative models can support personalized learning at scale.

---


### 437. [OmniShotCut: Holistic Relational Shot Boundary Detection with Shot-Query Transformer](https://arxiv.org/abs/2604.24762)

**<font color=#1a73e8>作者：</font>** Boyang Wang, Guangyi Xu, Zhipeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shot Boundary Detection (SBD) aims to automatically identify shot changes and divide a video into coherent shots. While SBD was widely studied in the literature, existing state-of-the-art methods often produce non-interpretable boundaries on transitions, miss subtle yet harmful discontinuities, and rely on noisy, low-diversity annotations and outdated benchmarks. To alleviate these limitations, we propose OmniShotCut to formulate SBD as structured relational prediction, jointly estimating shot ranges with intra-shot relations and inter-shot relations, by a shot query-based dense video Transformer. To avoid imprecise manual labeling, we adopt a fully synthetic transition synthesis pipeline that automatically reproduces major transition families with precise boundaries and parameterized variants. We also introduce OmniShotCutBench, a modern wide-domain benchmark enabling holistic and diagnostic evaluation.

---


> [!TIP]
> 当前位于：**401-437**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-437**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
