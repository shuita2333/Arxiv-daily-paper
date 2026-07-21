# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-386](./part-08.md)

---

### 301. [Artificial Intelligence for Understanding and Managing Transportation Behavior in Sustainable Smart Cities](https://arxiv.org/abs/2607.17694)

**<font color=#1a73e8>作者：</font>** Junbiao Pang, Muhammad Ayub Sabir, Fatima Ashraf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban transportation systems generate heterogeneous data, yet these data do not automatically become actionable management intelligence. This chapter adopts a behavior-centered perspective on artificial intelligence (AI), treating mobility records and passenger-generated text as behavioral evidence rather than behavioral truth. It examines four directions: bus arrival prediction for service reliability, taxi mobility pattern discovery for demand analysis and planning, abnormal behavior detection for accountable regulatory support, and passenger-perceived risk mining for service improvement. These directions are integrated through a closed-loop framework linking data input, behavior representation, AI inference, decision support, public value, and governance feedback. The chapter identifies data quality, privacy, fairness, interpretability, uncertainty, transferability, and human accountability as essential conditions for deployment. It thereby establishes a unified pathway from behavioral evidence to operational, planning, regulatory, and passenger-service decisions.

---


### 302. [ProEvent: An Event-centric Benchmark for Proactive Agents](https://arxiv.org/abs/2607.17701)

**<font color=#1a73e8>作者：</font>** Guanzhen Li, Liangming Pan, Leye Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive agents are expected to anticipate user needs and provide autonomous assistance by perceiving environmental context without explicit instructions. A fundamental capability of such agents is to identify and track users' upcoming events, enabling continuous and event-specific assistance. For example, by recording the time and location of a planned hike, an agent can deliver weather reminders in advance or provide navigation support before departure. However, existing works on proactive agents largely overlook event-centric assistance, and the open-ended nature of proactive assistance poses challenges for reliable evaluation.
To bridge these gaps, we introduce ProEvent, the first event-centric benchmark designed to assess an agent's ability to proactively maintain a user's timetable based on ongoing instant messaging chats. ProEvent provides synthesized yet realistic chats that consider the dynamic interaction among users, concurrent chat threads, and noise in the real world, and evaluates proactive agents on response timing, single-step response correctness, and multi-step response correctness. Experiments on eight LLMs and pipelines reveal that current agents frequently overact and struggle with event cancellation. Notably, even GPT-5.1 only reacts correctly in 26.7% of scenarios. Further qualitative analysis reveals fundamental limitations of current LLMs as proactive agents, particularly in detecting implicit events and reasoning from the user's first-person perspective.

---


### 303. [AEGIS: Awareness-Enhanced Guidance for Iterative Safeguard](https://arxiv.org/abs/2607.17713)

**<font color=#1a73e8>作者：</font>** Kyungwon Park, Sangmin Lee, Heejae Chon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Span-level rationales are often assumed to improve controllability in text detoxification, but it remains unclear when such guidance helps and when it introduces trade-offs. We present Awareness-Enhanced Guidance for Iterative Safeguard (AEGIS) as an exploratory framework for studying span-guided multilingual detoxification across English, Mandarin Chinese, and Korean. AEGIS combines span-level detector outputs with frozen generator backbones, allowing harmful spans, intensity labels, and target attributes to be provided as structured guidance during rewriting. Rather than claiming state-of-the-art detoxification performance, we analyze how span guidance affects the balance between toxicity reduction and meaning preservation across generator families, model scales, and languages. Our results suggest that span-guided detoxification is conditionally useful: explicit rationales change the trade-off between toxicity reduction and meaning preservation, but their effects depend strongly on the generator backbone and the linguistic context. These findings highlight both the promise and the limitations of span-level control signals for multilingual detoxification.

---


### 304. [PC-Seg: Progressive Cross-View Consistency for 3D OCT Segmentation from Sparse 2D Annotations](https://arxiv.org/abs/2607.17718)

**<font color=#1a73e8>作者：</font>** Tsubasa Konno, Takahiro Ninomiya, Yukun Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric segmentation of optical coherence tomography (OCT) images is essential for diagnosing ocular diseases but requires labor-intensive voxel-wise annotations. While semi-supervised learning (SSL) can reduce annotation costs, most existing methods process data slice by slice and fail to exploit the inherent 3D spatial context. We propose PC-Seg, a progressive cross-view consistency framework that learns high-accuracy 3D segmentation models from sparse 2D annotations. Unlike conventional multi-view approaches, PC-Seg uses a single 2D model to learn cross-view consistency from standard B-scans and orthogonal slices, thereby generating reliable volumetric pseudo-labels. These pseudo-labels are then distilled into a 3D model, followed by a co-training stage in which the 2D and 3D models mutually refine each other through ensemble pseudo-labeling. Experiments on the MSHC and Duke DME datasets demonstrate that PC-Seg achieves accuracy comparable to fully supervised learning while using labels for only about 0.7% of the training data, outperforming state-of-the-art semi-supervised and retinal layer segmentation methods. Our code is publicly available at this https URL.

---


### 305. [DA-Fusion: Deformable Attention-Based RGB-D Fusion Transformer for Unseen Object Instance Segmentation](https://arxiv.org/abs/2607.17754)

**<font color=#1a73e8>作者：</font>** Yesol Park, Hye-Jung Yoon, Juno Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In logistics automation, precise segmentation of unseen objects is crucial for efficient robotic manipulation in cluttered environments. Tasks such as bin-picking and shelf-picking require robust perception to handle occlusions, varying object shapes, and complex spatial arrangements. Traditional RGB-based methods tend to over-segment objects due to their reliance on texture, while depth-based methods often under-segment by focusing primarily on geometric features. To address these limitations, we propose DA-Fusion, a deformable attention-based RGB-D fusion Transformer designed for unseen object instance segmentation. DA-Fusion effectively combines the strengths of both RGB and depth data, enhancing segmentation accuracy in cluttered and multi-layered object environments. We also introduce the Object Clutter Bin Dataset (OCBD), a benchmark dataset specifically tailored for evaluating bin-picking scenarios in top-down views. Extensive evaluations demonstrate that DA-Fusion outperforms state-of-the-art methods across diverse environments, making it particularly suited for real-world logistics tasks.

---


### 306. [Generalize and Guide: Decomposing Rewards for Few-Shot Inverse Reinforcement Learning](https://arxiv.org/abs/2607.17760)

**<font color=#1a73e8>作者：</font>** Ziyi Liu, Grace Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL) provides a powerful framework for learning from demonstrations. However, real-world tasks often exhibit substantial natural variations (e.g., picking up mugs with varying shapes), making it impractical to collect demonstrations that fully specify a new task under every possible scenario. In practice, while demonstrations for the target task are limited, it is often easier to obtain datasets of heterogeneous but related behaviors. This motivates the problem of few-shot IRL with multi-task demonstrations (FM-IRL), where an agent must learn a new task with substantial variations from only a limited number of target-task demonstrations, together with sufficient demonstrations of related tasks and online agent experience. To do so, we must both recover the expert distribution of the new task and provide guidance when the agent deviates from it. We introduce Multitask discriminator Proximity-Guided IRL (MPG), which learns two complementary reward components: (1) a generalizable discriminator that transfers shared structure across related tasks to identify expert behavior in a new task, and (2) a proximity function that measures how far a state deviates from expert behavior and provides corrective guidance during exploration. We demonstrate the effectiveness of our method on multiple challenging navigation and manipulation tasks under significant variations (e.g., object configurations, table layouts, and initial robot poses), achieving an average success rate of 81.2%, outperforming the strongest per-task baseline by an average of 24.7 percentage points.

---


### 307. [When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation](https://arxiv.org/abs/2607.17766)

**<font color=#1a73e8>作者：</font>** Zeyu Yang, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extra context is valuable for simultaneous speech translation of technical talks, but injecting the entire document context into every streaming segment is often too coarse. Through diagnostic experiments, we find that context gains mainly come from paper-specific terminology recovery rather than uniform semantic enhancement. We therefore propose EGTA, an Evidence-Grounded Terminology Adaptation framework that builds a document terminology memory, selects compact candidate terms conditioned on the current streaming state, and adapts ASR/speech-side and decoder-side decision spaces using only the selected terms. EGTA can be instantiated in cascaded, end-to-end, and generation-only SimulST settings without full-model fine-tuning. We evaluate EGTA on an ACL technical-talk SimulST evaluation suite consisting of MCIF-dev and ACL60/60-dev. On MCIF-dev, EGTA-RG improves BLEU by +1.05/+0.59, XCOMET-XL by +0.019/+0.006, named-entity recall by +79\%/+73\% relative, and acronym recall by +0.099/+0.171 on En$\rightarrow$Zh and En$\rightarrow$De. Across MCIF-dev latency settings, EGTA consistently improves XCOMET-XL, named-entity recall, and acronym recall. External validation on ACL60/60-dev further shows consistent terminology-recall gains without additional fine-tuning. Shuffled-memory controls and activation audits provide evidence that the improvements are tied to paper-specific evidence alignment rather than generic context prompting.

---


### 308. [To Blend In, First Decouple: Rethinking Camouflage Image Generation via Context-Decoupled Representations](https://arxiv.org/abs/2607.17768)

**<font color=#1a73e8>作者：</font>** Wenzhuang Wang, Yifan Zhao, Mingcan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflage image generation (CIG) focuses on generating visually concealed objects that seamlessly blend into their backgrounds. Existing methods typically follow either background-guided paradigms that adapt object appearance via style transfer, or foreground-guided strategies that outpaint surrounding regions conditioned on object features. However, they still suffer from appearance discrepancy and background artifacts. We attribute these limitations to cross-context representation leakage, where object and background cues are entangled in a coupled conditional space, resulting in ambiguous control and degraded camouflage fidelity. To tackle this, we propose a new context-decoupled generative paradigm, termed CamoDreamer, which aims to isolate contextual conditional guidance and explicitly decouple latent camouflage features into coordinated object and background control streams. First, a Contrast-aware Contextual Bridge is designed to model cross-context discrepancies and construct contrast-aware dual conditional guidance. Second, Context-Decoupled Assimilation Streams are employed to separate generative interactions conditioned on the dual guidance, while facilitating background rendering with target-aware cues in the latent space. Finally, a Frequency-Adaptive Contextual Blend module integrates complementary high-frequency textures and low-frequency structures from decoupled features to improve holistic coherence. Extensive experiments demonstrate that CamoDreamer consistently outperforms existing methods with a substantial margin, while maintaining a relatively lightweight design.

---


### 309. [Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence](https://arxiv.org/abs/2607.17770)

**<font color=#1a73e8>作者：</font>** Katarzyna Filus, Sebastian Pokuciński  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Within Explainable Artificial Intelligence, mechanistic interpretability uses Sparse Autoencoders (SAEs) to extract more interpretable features from neural representations. However, assessing their monosemanticity, and thus explanation quality, remains challenging. Existing metrics require external concept labels or depend on pretrained embedding models, making them sensitive to encoder's geometry. We introduce the Tversky Monosemanticity Score (TMS), a label-free metric that operationalizes monosemanticity as activation-set coherence of binarized SAE latents, and does not require external embedding encoders. We evaluate TMS on SAEs trained on features from pretrained vision and vision-language models (DINOv3, CLIP, BLIP2), two common SAE regimes (TopK, BatchTopK), multiple sparsity levels, and expansion factors. Our results show that TMS is less affected by encoder anisotropy than its embedding-based alternative, while remaining aligned with established monosemanticity indicators. TMS also reveals distinct SAE training dynamics across base models. Moreover, under encoder anisotropy, TMS provides a stronger indication of probe-based concept deletion effectiveness, while being competitive otherwise.

---


### 310. [CDIS: Cross-Dimensional Class-Agnostic 3D Instance Segmentation via 2D Mask Tracking and 3D-2D Projection Merging](https://arxiv.org/abs/2607.17778)

**<font color=#1a73e8>作者：</font>** Juno Kim, Hye-Jung Yoon, Yesol Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-agnostic 3D instance segmentation is critical for robotic systems operating in unknown environments, enabling perception of previously unseen objects for reliable manipulation and navigation. Existing approaches typically project per-frame 2D instance masks into 3D and merge them, which often breaks object identities across time and yields fragmented 3D instances. We introduce Cross-Dimensional Class-Agnostic 3D Instance Segmentation (CDIS), a zero-shot framework that explicitly tracks 2D instance masks across frames and associates them with 3D superpoints, creating a feedback loop between 2D and 3D. This cross-dimensional reasoning links temporally stable 2D tracks with spatially coherent 3D regions, producing globally consistent 3D instance labels without any 3D-specific training. Experiments on benchmark datasets demonstrate that CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods, while remaining efficient and scalable to diverse real-world environments.

---


### 311. [Dynamic Defense Profiling Enables Cognitive Jailbreak of Text-to-Image Models](https://arxiv.org/abs/2607.17779)

**<font color=#1a73e8>作者：</font>** Dongdong Yang, Deyue Zhang, Zhao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) generative models have achieved remarkable progress in synthesizing high-quality visual content, yet they remain vulnerable to adversarial misuse, particularly in generating Not-Safe-For-Work (NSFW) images. Most existing jailbreak attacks primarily rely on heuristic prompt engineering or black-box optimization, treating model feedback as a binary signal (success or failure). This coarse-grained paradigm overlooks the rich information embedded in diverse failure modes, such as textual refusal, visual blocking, and semantic sanitization, resulting in inefficient exploration and severe semantic collapse.
In this paper, we propose MIND, a cognitive jailbreak framework that reframes adversarial prompt generation as a belief-state inference problem over latent defense mechanisms. Instead of blindly searching for bypass prompts, MIND actively models the target system's latent defense mechanisms by interpreting multi-modal feedback as high-density signals. Specifically, the framework integrates three core components: (1) a Multi-modal Judge for fine-grained feedback decomposition, (2) a Defense Profiler for iterative belief updating, and (3) a Meta-Memory module for retrieving historically effective attack strategies. These components are unified within a reasoning-driven evolutionary optimization process, enabling adaptive and semantically consistent jailbreak generation. Extensive experiments on the I2P benchmark demonstrate the effectiveness of MIND. Under six representative pre-processing and post-processing defense settings applied to the Stable Diffusion v1.5 model, MIND achieves an Attack Success Rate (ASR) of 95.62%, significantly outperforming existing methods. Additionally, the effectiveness of the proposed framework is validated across four widely used commercial T2I systems, achieving the highest ASR of 91.58% on Wan-2.5.

---


### 312. [Feature Attribution-Based Explainability Analysis of Deep Learning Models in Predictive Process Monitoring](https://arxiv.org/abs/2607.17783)

**<font color=#1a73e8>作者：</font>** Kseniya Sahatova, Rafael Seidi Oyamada, Xuefei Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive process monitoring supports the optimization and control of operational business processes by forecasting the future state or outcome of ongoing cases. While deep neural networks have achieved strong performance for these tasks by modeling sequential dependencies in event logs, their black-box nature limits trust and practical adoption. Feature attribution methods are often used to address this, but applying them directly poses a dilemma: event-level attributions impose high computational complexity for long traces, while explanations based on aggregated trace representations often fail to capture the underlying control-flow dynamics. To address this issue, we propose a local post-hoc explainability method for deep neural networks in outcome prediction. The method relies on a control-flow-aware segmentation algorithm that partitions a trace into meaningful segments and supports the computation of segment-level SHAP explanations. This makes it possible to identify which parts of a trace influence a prediction and which change points steer the case toward the predicted outcome. We assess the proposed segmentation method on a synthetic dataset with known process logic, where meaningful change points can be explicitly verified, and we demonstrate its usefulness on real-world event logs from a loan application process and an administrative process of a Dutch municipality.

---


### 313. [Medical Imaging Fusing Vision Transformer: Laryngeal Cancer Screening with Explanation](https://arxiv.org/abs/2607.17789)

**<font color=#1a73e8>作者：</font>** Haiyang Wang, Luca Mainardi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early and timely screening of laryngeal cancer is crucial for improving clinical outcomes. In recent years, NBI endoscopy has become a standard diagnostic tool for the detection of laryngeal lesions. However, its effective use requires well-trained clinicians and the procedure is time-consuming and subject to interobserver variability. In this context, the application of artificial intelligence (AI) offers a promising solution to support clinical decision-making. In this work, we proposed applying transformer and attention mechanism for analyzing the narrow band imaging and distinguish benign and malignant lesions. Results show it has good classification performance with F1 (82.72%), accuracy(82.33%). In addition, the result of laryngeal cancer screening is explainable for clinicians. The explainability is utilizing the state of art segmentation method (MedSAM) to provide the useful pathological information area for clinicians. The proposed methodology fusing classification and segmentation provides a translating on laryngeal cancer screening.

---


### 314. [ReViV: Reconstructing the Viewer and the View in 4D from Monocular Egocentric Video](https://arxiv.org/abs/2607.17790)

**<font color=#1a73e8>作者：</font>** Xiaozhong Lyu, Gen Li, Zhiyin Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric devices, such as wearable front-facing cameras, provide a unique perspective for capturing the continuous interaction between a human viewer and the surrounding environment. A holistic and efficient multimodal model capable of reconstructing this 4D representation is therefore highly desirable. However, existing approaches often rely on auxiliary inputs such as pre-computed camera trajectories, treat scene perception and human ego-motion modeling as separate problems despite their strong interdependency, and suffer from slow inference time. To address these limitations, we present ReViV, the first unified framework for holistic egocentric 4D reconstruction that extracts both viewer and view dynamics from a single monocular RGB video. We formulate the task as learning the full joint probability distribution over multimodal signals, including RGB video, camera trajectory, gaze direction, full-body motion, hand motion, and depth. Powered by a Masked Generative Egocentric Transformer, ReViV operates within a single feed-forward architecture to simultaneously reconstruct the temporally consistent 4D reconstruction across the viewer and the view with fast inference speed. Extensive experiments on diverse benchmarks, including HoloAssist, HOT3D, ARCTIC, Aria Digital Twin, and TACO, demonstrate that ReViV achieves state-of-the-art accuracy and efficiency across holistic ego-body, hand, and gaze reconstruction, camera tracking, while maintaining highly competitive egocentric depth estimation without relying on heavy task-specific priors. Code and models are fully open-sourced: this https URL.

---


### 315. [Financial Audit Assistance using Misinformation Detection and Explanation](https://arxiv.org/abs/2607.17797)

**<font color=#1a73e8>作者：</font>** Kshitij Madhav Jadhav, Sushodhan Vaishampayan, Manoj Apte 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial statements (FS) such as Balance Sheet (BS), Income Statement (IS) and Cash-flow Statement (CS) summarize the annual financial performance of a company. FS are widely used for evaluating corporate governance, credit appraisal, risk analysis, validate taxation, make investment decisions etc. Financial auditing is a complex and knowledge-intensive discipline whose one important aim is ensuring integrity, accuracy, fairness and absence of material misstatement in the published FS. Given the importance of FS, there are incentives to hide, omit or falsify information to misrepresent the true financial health of the company; e.g., reduce tax liabilities, or increase investor confidence. Given the complex, time-consuming and expertise-dependent nature of auditing, auditors would benefit from an AI-assisted system that automatically detects instances of misinformation in the given FS and identify likely sources of this misinformation in the financial data. In this paper, we present unsupervised techniques to identify misinformation in FS, and also generate explanations as to the financial variables that are likely sources of misinformation. The auditor can then explore in more detail the associated data sources and business processes to validate these suggestions. A crucial feature of our approach is the use of past corpus of FS and associated audit reports to generate insights, which help in providing assistance. We demonstrate the efficacy of these techniques on a large corpus of 11,460 FS over 5 years and associated audit reports. This paper integrates and adds more novel contributions over the previously reported research (Shinde et al., 2022)\cite{SVAP22}, (Vaishampayan et al., 2022)\cite{VSPP22}, (Pawar et al., 2023)\cite{PAPV23}, which we have used as the foundation for our AI-assisted Auditor Assistance system.

---


### 316. [Toward Optimal Adenovirus Detection Using YOLO26](https://arxiv.org/abs/2607.17799)

**<font color=#1a73e8>作者：</font>** Olivier Rukundo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study systematically benchmarks different data augmentation setups across YOLO26 model size variants to determine the most effective setup for adenovirus detection in TEM images. The benchmarked setups include NAS, GAS, GMAS and DAS, all evaluated under identical training conditions. The adenovirus dataset, selected from the published TEM virus dataset, was re-annotated by leveraging adenovirus particle positions to generate YOLO-compatible bounding box annotations. The experimental results demonstrated the impact of the benchmarked data augmentation setups on adenovirus detection with YOLO26 and indicated the most effective data augmentation setup.

---


### 317. [The Concept of Representation in ML: Beyond Plato and Aristotle](https://arxiv.org/abs/2607.17800)

**<font color=#1a73e8>作者：</font>** Gilad Landau, Aviv Keren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation is a central concept in modern machine learning, where it usually refers to internal encodings that support learning and generalization. As models scale and their capabilities become increasingly human-level, this representational language sometimes shifts from an engineering context into the more philosophically loaded domain of mental representation. We argue that this is the case for recent claims about the convergence of representational properties across different AI models. In particular, we assess the arguments developed in The Platonic Representation Hypothesis, according to which this convergence is driven by a unified structure of reality. We examine this claim by introducing arguments and ideas from debates about mental representation in the philosophy of mind. We argue that these philosophical resources can clarify what is at stake in such claims, explain why alignment evidence alone is insufficient for strong metaphysical conclusions, and suggest directions for future research.

---


### 318. [FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803)

**<font color=#1a73e8>作者：</font>** Ziyao Wang, Yuqi Li, Wenxing Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Projector-camera (ProCams) systems achieve active scene perception and controllable appearance manipulation via structured illumination, serving as a core infrastructure for spatial augmented reality, projection mapping, and surface reflectance acquisition. Existing inverse-rendering methods for ProCams deliver high-fidelity results but rely on time-consuming per-scene optimization, while mainstream feed-forward 3D reconstruction models produce baked appearance that cannot adapt to spatially varying projector illumination.
To resolve this accuracy-efficiency trade-off, we propose FF-ProCams, a Feed-Forward 3D Gaussian inverse-rendering framework for ProCams. A hybrid Mamba2-Transformer encoder aggregates cross-view geometric and photometric cues from sparse multi-view observations, and lightweight heads predict a relightable Gaussian representation in a single forward pass. We further design a projector-aware differentiable renderer to synthesize camera observations under arbitrary active illumination and ProCams poses. To enable feed-forward training, we construct a large-scale synthetic ProCams dataset covering diverse object geometries and surface materials. Experiments show FF-ProCams achieves high-fidelity projector-aware rendering, generalizes to unseen patterns, and supports novel projector-camera poses. Using only 8 input views, it outperforms optimization-based baselines with 297 views while reducing test-time reconstruction to 0.13 seconds (a three-to-five-order-of-magnitude speedup). The code and data are available at this https URL.

---


### 319. [Residual Observability and Attack Detectability in Encrypted OPC UA Traffic](https://arxiv.org/abs/2607.17809)

**<font color=#1a73e8>作者：</font>** Song Son Ha, Florian Foerster, Henry Beuster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> OPC Unified Architecture (OPC UA) encryption conceals application-layer semantics and restricts intrusion detection to residual communication structure. Although machine learning-based intrusion detection systems (IDSs) can detect attacks in encrypted OPC UA traffic, the relationship between residual structural observability and attack detectability remains insufficiently understood. This paper presents an explanatory framework combining a structural observability profile, the Structural Leakage Score (SLS), controlled within-family and cross-family comparisons, phase-specific analysis, and dimension-ablation analysis. Jensen--Shannon divergence is used to characterize transport, temporal, and protocol-lifecycle dimensions, while the SLS summarizes the residual structural magnitude. Evaluation on an industrial private 5G testbed covers four attack families with progressively reduced nominal activity. SLS generally tracks within-family recall trends but does not reproduce cross-family detectability ordering. Interpreting these mismatches also requires temporal prevalence, inter-burst persistence, predictive utility, unique contribution, and redundancy. The framework complements conventional IDS metrics by relating detection outcomes to the magnitude, temporal distribution, and predictive role of observable structural evidence.

---


### 320. [Vis2Reg: Visibility-Aware Landmark-Free Geometric 3D--2D Registration for Liver Laparoscopy](https://arxiv.org/abs/2607.17810)

**<font color=#1a73e8>作者：</font>** Jiaming Feng, Xukun Zhang, Shahid Farid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D--2D liver registration, which aligns preoperative 3D models to partial, view-dependent intraoperative surface observations, is critical for AR-guided laparoscopic surgery but remains challenging due to severe occlusion, limited visibility, and the lack of 3D ground-truth supervision. Existing landmark-free approaches perform partial-to-complete geometric alignment, yet robust self-supervision under extreme partial visibility remains difficult. We propose Vis2Reg, a visibility-aware registration framework that explicitly constrains deformation using mask-consistent visible regions. We introduce a visibility-aware self-supervision that derives a visible-domain 3D supervision signal from intraoperative masks, enabled by differentiable point rasterization and mask-guided back-projection. This formulation improves robustness under severe occlusion while maintaining fully self-supervised learning. Vis2Reg combines a robust geometric rigid initialization module with an implicit neural deformation field for stable alignment. Vis2Reg achieves a Dice score of 92.6\% and a Chamfer Distance of 1.43 mm on real intraoperative datasets, with 111 ms per-frame inference time, demonstrating both accuracy and practical efficiency.

---


### 321. [ESCUCHA: A Spanish Speech Benchmark for Heterogeneous Acoustic Conditions](https://arxiv.org/abs/2607.17812)

**<font color=#1a73e8>作者：</font>** Fernando López, Ana Ayala, Guillermo Segovia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large audio language models (LALMs) advance, robust evaluation frameworks have become essential. In this context, Spanish speech understanding under realistic acoustic conditions has received particularly little attention. We introduce ESCUCHA, the first Spanish speech understanding benchmark designed to evaluate LALMs across heterogeneous acoustic conditions and reasoning abilities. ESCUCHA comprises 1,000 human-curated questions paired with audio, totaling 162.9 hours sourced directly ``from the wild'' rather than drawn from existing datasets, with durations ranging from a few seconds to over 80 minutes. The benchmark emphasizes reasoning, spanning 9 perceptual and 10 reasoning categories, and it captures linguistic diversity through multiple Spanish accents and non-normative speech. ESCUCHA further includes multi-audio questions, spoken questions, and audio instructions, and it flags which questions support open-ended evaluation. Benchmarking several state-of-the-art multimodal and speech models reveals substantial performance gaps relative to trained humans.

---


### 322. [PRiSM: Prototype Regularization for Few-Shot VLMs](https://arxiv.org/abs/2607.17820)

**<font color=#1a73e8>作者：</font>** Ghassen Baklouti, Omprakash Chakraborty, Jose Dolz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free few-shot adaptation methods have gained significant attention recently in the context of Vision-language Models (VLMs). Yet, current benchmarks rely on strong assumptions about the statistics of the adaptation data, e.g., class balance. We question these simplifying assumptions and introduce a more realistic benchmark that varies both the levels of class balance and the effective number of classes in few-shot tasks via Dirichlet sampling. Surprisingly, under our setting, we observe substantial drops in the performances of state-of-the-art methods, more so when the number of labeled samples increases. To mitigate this, we introduce PRiSM, a class-prototype regularization that can be deployed as a plug and play module on top of any existing baseline method, significantly improving performances. Our method optimizes a novel multi-term loss, which includes a regularizer maximizing inter-class pairwise distances, along with additional terms promoting support-feature alignment and fidelity to the baseline prototypes. Furthermore, we introduce an effective and computationally efficient block Majorize-Minimize optimizer for our objective. More specifically, we derive a valid blockwise Lipschitz constant (i.e., a bound on the Hessian's spectral norm), which can be computed efficiently via the Gershgorin circle theorem. Extensive experiments show that PRiSM improves several training-free baselines, with large gains when dealing with severe class imbalance and high numbers of classes.

---


### 323. [Phasor Attention: Mean Root Square Normalization for Phase Manifold Preservation](https://arxiv.org/abs/2607.17822)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Root Mean Square Normalization has become the de facto standard for accelerating modern sequence models, its reliance on the quadratic accumulation of independent scalars ($\sum x^2$) inherently triggers outlier-induced numerical instability, gradient starvation, and anisotropic phase distortion. We introduce Mean Root Square Normalization (MRSNorm). By structurally pairing channels into 2D phasors, MRSNorm mathematically inverts the traditional scaling paradigm: it computes the localized $L_2$ magnitudes (Root Square) before aggregating them via a global $L_1$ average (Mean).
This operational inversion strictly constrains activations to a phasor manifold, preserving conformal invariance. By sharing a single affine weight across phasor components, MRSNorm halves the total number of learnable parameters, proving that unconstrained spatial scaling in standard norms is a harmful redundancy. We analytically demonstrate that this geometric constraint yields a built-in, trigonometric gradient clipper governed by the Pythagorean identity, unconditionally equalizing the local gradient norm to ensure Gradient Homogeneity.
Empirical evaluations on a ResNet with CIFAR-100 show that despite halved parameters, MRSNorm provides critical structural stability under rigorous stress tests. Under extreme hyperparameter settings where standard normalizations suffer from gradient divergence, MRSNorm successfully prevents numerical explosion and secures stable optimization trajectories. Our findings propose a fundamental paradigm shift toward phasor-based deep representation learning. The implementation of MRSNorm is available at Appendix C.

---


### 324. [Theoretical Foundations of $\max$@$k$ Reinforcement Learning](https://arxiv.org/abs/2607.17823)

**<font color=#1a73e8>作者：</font>** Riccardo Poiani, Martino Bernasconi, Andrea Celli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning is a cornerstone technique for modern large reasoning models. Usually, for difficult tasks such as code generation and theorem proving, the agent is evaluated by generating $K$ responses rather than sampling a single response, and performance is then measured using a retry-aware metric such as $\max$@$k$. Despite their practical importance, the theoretical foundations of learning under such criteria remain limited. In this work, we provide a theoretical study of the $\max$@$k$ learning problem in finite-horizon reinforcement learning. We show that optimizing the $\max$@$k$ objectives is fundamentally different from standard expected-return maximization. In particular, we prove that Markovian policies are in general insufficient, identify a compact state augmentation that restores optimality, and explicitly characterize the performance gap that can arise between history-dependent and non-history-dependent policies. Moreover, we show that learning $\max$@$k$-optimal policies is statistically harder than standard reinforcement learning and provide an efficient algorithm that achieves the optimal sample complexity rate.

---


### 325. [I wanted it to feel more personal: Customization of social AI as AI individualism in practice](https://arxiv.org/abs/2607.17826)

**<font color=#1a73e8>作者：</font>** Marita Skjuve, Anna Grøndal Larsen, Asbjørn Følstad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite the growing availability of customizable social artificial intelligence (AI), such as ChatGPT, Grok, and this http URL, we know little about how users actively shape social AI to reflect their personal preferences. This study examines why and how users (N = 169) customize social AI through the lens of the newly developed concept of AI individualism. Through reflexive thematic analysis of open-ended responses, we identified several motivations for customization, including (1) enhanced pragmatic support, (2) emotional support or companionship, (3) trust and reliability, (4) pushback, (5) a tailored degree of human likeness, (6) creativity or playfulness, and (7) having the AI function as an extension of the self. In line with the concept of AI individualism, our findings show that, for many users, customization is a co-creative process between the human and the AI that is perceived as strengthening support, autonomy, ownership, and engagement, potentially contributing to a closer and more personal relationship. Through customization users may come to view social AI as a personalized social resource that increases their sense of individualism, freedom, and control. We discuss how these perceptions may foster pseudo-autonomy, whereby customization creates an illusion of individual control over powerful social AI systems.

---


### 326. [Consistent Feature Transport for Image Relighting](https://arxiv.org/abs/2607.17833)

**<font color=#1a73e8>作者：</font>** Bohan Zhang, Huanwei Liang, Yuhan He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image relighting modifies illumination while preserving non-lighting content such as identity and geometry. Existing diffusion-based methods often suffer from unstable illumination changes or inconsistent content preservation under complex lighting, as they lack an explicit mechanism to learn feature transformations between images. We reformulate relighting as an illumination feature transport problem and introduce Consistent Feature Transport (CFT), a training principle that explicitly enforces illumination-consistent transport between source and target image distributions. Built upon rectified flow, CFT jointly models noise-to-image generation and illumination-consistent source-to-target transport through trajectory-level supervision. This dual-transport formulation encourages isolation of illumination-specific variations while preserving content-aligned features. To support complex lighting scenarios, we construct a large-scale portrait relighting dataset with diverse relighting effects. Experiments show consistent improvements over existing state-of-the-art relighting approaches and demonstrate that CFT can generalize to other editing tasks, including style transfer. Code is available at this https URL.

---


### 327. [Measuring and Improving Complex-Atomic Answer Consistency in Endoscopic VQA](https://arxiv.org/abs/2607.17834)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Cheng Zhao, Guanghui Yue  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endoscopic visual question answering (VQA) increasingly asks complex questions that combine several endoscopic answer components rather than isolated factual queries. Such complex answers may be scored as correct even when the same model fails on associated atomic questions. We introduce EndoCA, a paired complex-atomic answer consistency benchmark for evaluating whether complex answers remain consistent with same-image atomic answers. EndoCA contains two suites: EndoCA-Core evaluates compact question-complexity patterns commonly seen in practical endoscopic VQA, and EndoCA-Diagnostic supports controlled analysis across increasing question complexity. We evaluate 11 VLMs spanning open, medical, endoscopy-adapted, and closed-source models on EndoCA. Some VLMs achieve high complex-answer accuracy, yet their atomic-answer accuracy and complex-atomic answer consistency remain substantially lower. To reduce this complex-atomic inconsistency, we introduce Atomic-Support Reconciliation (ASR), a training-free mechanism that uses model-generated atomic answers as contextual premises for answer revision and consistency-guided selective answering. On four selected publicly available models, ASR-Revise improves paired complex-atomic correctness with modest changes in complex-answer accuracy, while ASR-Selective improves accuracy on answered cases by allowing the model to abstain from less reliable cases. Together, EndoCA and ASR provide a consistency-aware benchmark and a training-free mechanism for answer reconciliation and selective answering in endoscopic VQA.

---


### 328. [CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842)

**<font color=#1a73e8>作者：</font>** Tingjia Zhang, Bo Chen, Shengzhong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in 3D Gaussian Splatting (3DGS) have advanced neural rendering with high fidelity and speed. However, its performance degrades significantly in large-scale scenes due to the computational burden of tile-based rasterization. Existing optimization efforts either require costly scene re-training or focus on narrow aspects of the pipeline, overlooking critical inefficiencies in real-world deployments. Through a comprehensive analysis, we identify three primary sources of redundancy and low GPU utilization: redundant inter-frame pre-processing, viewpoint-based occlusion redundancy, and severe tile-level load imbalance. To address these issues, we propose CaT-GS, a novel and efficient 3DGS rendering pipeline. CaT-GS introduces a speculative multi-frame preprocessing method to eliminate redundant computations across consecutive frames, and an inter-frame caching mechanism to eliminate viewpoint redundant rendering stages. Furthermore, it refactors rasterization tasks with a dedicated kernel to mitigate tile load imbalance, significantly boosting GPU utilization. Extensive experiments demonstrate that CaT-GS achieves a speedup of up to 10 times over the original 3DGS and up to 70% over previous state-of-the-art methods, establishing a new benchmark for high-fidelity, real-time rendering of large-scale scenes.

---


### 329. [Mobius Learning: Cyclic Depth Folding in Transformers](https://arxiv.org/abs/2607.17843)

**<font color=#1a73e8>作者：</font>** Tongtian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models organize computation along an ordered depth axis, where shallow and deep blocks often develop distinct representational roles. We challenge the conventional view that these roles must remain tied to a block's position in the ordered sequence. We introduce Mobius Learning, a training architecture based on cyclic depth folding, in which different data streams follow cyclically shifted block orders. The same block group is therefore applied early in the block sequence for some data streams and late for others, so it is optimized in both shallow and deep roles, a phenomenon we call depth-role superposition. Surprisingly, in four-worker experiments with a modded GPT-2 small (124M) model trained on 2.5B FineWeb tokens using Muon, Mobius Learning achieves lower validation loss than a fixed-order looped Transformer at larger numbers of Transformer block-sequence passes. This counterintuitive result shows that a block group need not remain confined to one fixed shallow or deep role within the block sequence and opens a new design space based on cyclic depth folding. Crucially, this structure makes Mobius Learning particularly well suited to memory-constrained distributed training: raw training data remain local, while each worker stores one block group rather than the complete Transformer block stack.

---


### 330. [AlphaOracle: Oracle bone script decipherment via human-workflow-inspired deep learning](https://arxiv.org/abs/2607.17849)

**<font color=#1a73e8>作者：</font>** Yuliang Liu, Haisu Guan, Pengjie Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Approximately 3,000 of the 4,500 oracle bone script (OBS) characters remain undeciphered due to fragmentary inscriptions and sparse evidence. Current AI approaches fail to replicate expert workflows that integrate form analysis, contextual semantics, and philological reasoning. We introduce AlphaOracle, a human-workflow-inspired framework that systematizes OBS decipherment using the largest digitized corpus to date. Its multi-stage pipeline comprises: (i) rubbing parsing; (ii) radical-based morphological analysis with diachronic modeling; (iii) contextual retrieval with semantic alignment; and (iv) philological validation against classical sources. Each stage generates explicit, confidence-weighted evidence chains, culminating in interpretable reports for scholarly verification. Across multiple test characters, AlphaOracle's readings strongly agreed with expert interpretations. In a study of 86 domain specialists, it reduced analysis time by 64% and 79% of participants rated it highly useful. Notably, AlphaOracle resolves the character "Lao" as a toponymic or clan designation, offering concrete revisions to Shang administrative and social interpretations. These results suggest that computational methods aligned with philological practice can facilitate OBS research and provide a conceptual reference for studies of other undeciphered scripts.

---


### 331. [A Hardware-oriented Approach for Efficient Bayesian Inference Computation and Deployment](https://arxiv.org/abs/2607.17855)

**<font color=#1a73e8>作者：</font>** Nikola Pižurica, Matteo Risso, Nikola Milović 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian inference provides a principled foundation for reasoning under uncertainty, but its computational cost hinders deployment on resource-constrained edge devices. In this paper, we present a hardware-oriented methodology for accelerating discrete Bayesian inference on commercial off-the-shelf embedded GPUs. We identify that the latency of a broad class of variational message-passing algorithms is dominated by tensor contractions. Our approach restructures the memory layout of these operations using two complementary merging strategies that produce compact, regularly-shaped primitives better suited for efficient GPU execution. We then introduce optional sparse array representations and a tensor-clustering scheme to reduce the memory footprint. We instantiate the methodology and produce optimized variants of three message-passing algorithms for Hidden Markov Models (HMMs), namely variational filtering, variational message passing, and marginal message passing. Furthermore, we complement this with a machine-learning-based autotuner that automatically selects the best-performing algorithmic variant for a given generative model specification. Benchmarked on an NVIDIA Jetson Orin AGX across 770 randomly sampled realistic Partially Observable Markov Decision Process (POMDP) configurations, our implementations achieve speedups of up to 5x, with typical gains of 2-2.5x, while producing numerically identical outputs to the baseline implementations.

---


### 332. [Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory](https://arxiv.org/abs/2607.17879)

**<font color=#1a73e8>作者：</font>** Ganesh Senrayan, Moyuru Yamada, Ishan Jindal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning. However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores. We propose Exploratory-Assimilating Reflection (EAR), a framework for high initial retrieval performance and sample-efficient adaptation. EAR combines two mechanisms: Exploratory Reflection, which performs iterative search to bootstrap retrieval and collect useful experiences for each query, and Assimilating Reflection, which replays these experiences from an Experience Buffer to refine a global reranker more efficiently than methods relying only on immediate rewards. Experiments show that EAR improves retrieval by up to 17.9% over the baseline retriever on two long-term dialogue benchmarks. We also show that EAR is highly sample-efficient and robust to noisy feedback.

---


### 333. [Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI](https://arxiv.org/abs/2607.17883)

**<font color=#1a73e8>作者：</font>** Bogdan Raduta, Horia Velicu, Alexandru Preda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprises will not deploy AI agents they cannot trust, and the most-cited reason for distrust is hallucination: confident, fluent output that is simply not true. The common response is to wait for a model that does not hallucinate. We argue that this is the wrong target. Large language models are, by construction, capable of generating unsupported text, and no amount of scale removes the possibility; a faithfulness judge bolted onto a raw model catches some errors but still ships others, and even well-curated retrieval pipelines have been shown to fabricate citations. We reframe the goal: "zero hallucination" is not a property a model possesses but a property a system enforces. We present HALO (Hallucination-Aware Layered Oversight), an assurance architecture which treats hallucination as a containable failure mode rather than an eliminable one. HALO composes six layers of defense: grounded generation over retrieved, approved content; constrained, deterministic execution that bounds where the model can err; multi-signal verification that scores every output for groundedness and hallucination using both an LLM judge and evidence-based checks against the source text; calibrated abstention, so the system declines rather than guesses when grounding is insufficient; total traceability of every retrieval, tool call, and generation; and continuous oversight that detects drift, alerts on threshold breaches, and closes the loop by regenerating and statistically validating improved agents. We detail each layer, give particular attention to evidence-based confidence (which verifies extractions against the source document rather than trusting the model's self-reported certainty), and illustrate the architecture on a regulated claims-extraction workload

---


### 334. [Rate-Distortion Function for Encrypted Traffic Side-Channel Defense](https://arxiv.org/abs/2607.17889)

**<font color=#1a73e8>作者：</font>** Guangjie Liu, Guang Cheng, Weiwei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Parameter selection for encrypted traffic defense has long relied on empirical tuning, yet the fundamental question -- \emph{given a QoS cost budget $D$, how low can the leakage rate go under sustained observation?} -- lacks a provable, computable baseline. Taking the semantic label sequence $X^n$ as the source, the defended feature sequence $Y^n$ as the observation, and Wasserstein-1 distance as the defense cost, we define the \emph{side-channel rate-distortion function} $R^{\mathrm{sc}}(D)$ within the stationary memoryless defense class $\Theta_{\mathrm{iid}}$ and provide its complete characterization. We prove that $R^{\mathrm{sc}}(D)$ is monotone decreasing, convex, and continuous, with exact endpoints; the optimal defense has an exponential-tilting (Boltzmann) structure governed by KKT conditions; and the curve constitutes the exact Pareto frontier within $\Theta_{\mathrm{iid}}$. For binary equal-prior tasks, $D_{\max} = \tfrac{1}{2}W_1(P_0,P_1)$ via Kantorovich--Rubinstein duality. On real-world website-fingerprinting defenses, the framework locates Front ($\Delta_{\mathrm{gap}}{=}0.028$\,bits), WTF-PAD ($0.034$\,bits), and TrafficSliver ($0.124$\,bits) above the theoretical curve, quantifying their suboptimality gaps.

---


### 335. [Locality-Aware Density Control for Efficient Gaussian-based Image Representation](https://arxiv.org/abs/2607.17896)

**<font color=#1a73e8>作者：</font>** Jiacong Chen, Qingyu Mao, Xiandong Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 2D Gaussian Splatting is an attractive direction for image representation due to its explicit formulation, fast rasterization, and favorable decoding efficiency. The representation quality of this paradigm depends on the proper allocation of Gaussian capacity to the demanding regions. However, existing methods fail to allocate Gaussian capacity efficiently during optimization: under-reconstructed content is often refined in a fragmented pixel-wise manner, while neighboring optimized Gaussians with similar attributes are redundantly retained. This inefficiency motivates the need for a density control framework that jointly addresses insufficient allocation in under-reconstructed regions and redundant allocation in over-reconstructed regions. Our key insight is that this framework should exploit two complementary forms of locality: the local continuity of reconstruction errors in image space for improved Gaussian allocation, and the local similarity of neighboring Gaussians in Gaussian space for redundant elimination. Based on this insight, we propose Locality-Aware Density Control (LocoADC), a plug-and-play framework that improves Gaussian capacity utilization through Region-wise Gaussian Densification (RGD) and Similarity-Driven Gaussian Merging (SDGM) strategies, together with a local color consistency constraint for more reliable merging. Extensive experiments on diverse datasets show that LocoADC consistently improves multiple baselines by enabling more effective local Gaussian allocation, including a 2.93 dB PSNR gain over GI on the CLIC dataset under the same 30k Gaussian budget. Code is available at: \textit{this https URL}.

---


### 336. [Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss](https://arxiv.org/abs/2607.17914)

**<font color=#1a73e8>作者：</font>** Kemal Devrim Kafadar, Eren Özaltun, Mahmud Efnan Şanlı 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Robust multi-agent coordination relies heavily on inter-agent communication, which is frequently disrupted by physical and environmental constraints in real-world deployments. To maintain operation during these intermittent communication failures, agents can employ internal prediction models to estimate missing shared state information. However, predictors trained with standard reconstruction objectives treat all transitions equally. In a Reinforcement Learning context, this forces the model to waste capacity learning stochastic exploration noise and the outdated dynamics of suboptimal policies. In this paper, we propose a value-aware extension of Multi-Agent Observation Sharing under Communication Dropout (MARO) to patch communication gaps; we refer to this method as Value-Aware MARO. By dynamically weighting the predictor's loss function using advantage estimates derived from the underlying actor-critic architecture, our objective explicitly couples the predictor's learning process to the policy's evolution. This formulation focuses the model's capacity on the intentional, high-return dynamics actively reinforced by the agents. We evaluate our framework on several tasks within the Multi-Agent Particle Environment under varying communication reliability levels. Experimental results demonstrate that our approach maintains performance under declining communication reliability, particularly below 40%. While our method performs comparably in tasks where the baseline already maintains high coordination, our value-aware weighting effectively prevents the performance collapse observed in the standard predictor during high-attrition scenarios. In these environments, our method achieves an average improvement in mean returns of more than 20% and reduces performance variance by a mean of 64.7% compared to the standard unweighted baseline.

---


### 337. [PEARL: Auditable Repair for Scientific Reasoning Graph Extraction](https://arxiv.org/abs/2607.17917)

**<font color=#1a73e8>作者：</font>** Bohan Su, Pengze Li, Yuchen Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific Reasoning Graph Extraction (SRGE) aims to recover explicit links among observations, evidence, intermediate claims, and paper-level conclusions. LLMs can produce graph-like scientific explanations, but their outputs often mix malformed syntax, drifting edge labels, incorrectly oriented roots, and weak source anchors. We propose PEARL (Peircean Extraction via Abstraction and Repair Layer), a training-free framework that turns noisy LLM graph responses into auditable reasoning graphs and repairs them toward strict semantic validity. PEARL first materializes explicit graph content under a closed Peircean schema, then uses matched evidence-grounded judge feedback to repair rejected edge types, local inference steps, and terminal roots while preserving an audit trail. On five 70-paper model archives from ARCHE, a benchmark for latent reasoning-chain extraction, PEARL raises strict gate passes from 0/350 for the LLM baseline to 300/350, with average REA improving from 0.339 to 0.906. The graphs provide a reliability layer for research-agent and AI scientist workflows that need inspectable reasoning traces rather than unconstrained graph regeneration. Code and audit artifacts are available at this https URL .

---


### 338. [PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks](https://arxiv.org/abs/2607.17922)

**<font color=#1a73e8>作者：</font>** Wen Qiu, Zhiqiang He, Wei Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most reinforcement learning controllers for these networks assume stationary conditions, and the few that handle change react to the external environment while leaving the network's internal state unexamined. We show that sustained non-stationarity damages this internal state directly: as objectives shift, neurons progressively fall dormant and the shared policy loses the capacity to learn. The obvious remedy, resetting dormant neurons, is unsafe under shared-parameter multi-agent training: many neurons that appear inactive are still receiving strong training gradients, and whether a neuron appears dormant depends on which agent's observations it processes. PRIME (Plasticity Recovery In Multi-agent Environments) therefore verifies both directions before intervening. Extending the bidirectional Silent Neuron framework to cooperative multi-agent reinforcement learning, it aggregates activation and gradient statistics over the full team batch, reads the backward signal from the gradient the training loss has already deposited , not from a hand-crafted proxy, and reinitializes only neurons that are simultaneously activation-dormant and gradient-silent. Useful representations are preserved while learning capacity is restored. On a phase-switching UAV emergency communication simulator, PRIME improves interquartile mean return by 24.9\% over MAPPO and holds dormant neuron fractions at 10--20\% versus 40--45\%; ablations attribute the gains to the gradient signal and team-level aggregation rather than to the specific reset operator. A dynamic regret bound shows that the perturbation cost scales with the small silent-subspace dimension rather than the full parameter count.

---


### 339. [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](https://arxiv.org/abs/2607.17924)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Sen Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL). A central design question is how many neighboring agents\footnote{In this paper, "neighbors" refer not only to physical proximity but also to agents whose actions influence one another.} to aggregate in order to effectively utilize global information for cooperation. This decision must be made along two dimensions: in the advantage (which agents' rewards contribute to the credit signal) and in the ratio (which agents' likelihood ratios form the clipped importance weight). Existing methods occupy scattered, underexplored points on these two axes: IPPO treats both separately; MAPPO pairs a team-level advantage with per-agent ratios; HAPPO employs sequential ratios with per-agent advantages; and single-agent reductions operating on factorized joint policies aggregate both into fully joint products. We formalize these two design choices as support matrices $\SA$ and $\SR$, and prove a canonical structure: the expected multi-agent policy optimization objective depends on the pair $(\SA,\SR)$ only through their matrix product $\tS=\SR\SA$. This yields two key consequences: (i) Redundancy: the two support matrices are interchangeable with respect to the signal, meaning neither aggregation pattern is inherently superior.(ii) Variance Ordering: the advantage aggregates rewards as a sum (additive variance with an interior bias-variance optimum at the coupling neighborhood), whereas the ratio aggregates likelihood ratios as a product (multiplicative variance that grows exponentially with support size, with no accompanying bias reduction). The resulting design principle is unambiguous: aggregate neighbors in the advantage, sized to the coupling neighborhood, and keep the ratio per-agent.

---


### 340. [MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors](https://arxiv.org/abs/2607.17938)

**<font color=#1a73e8>作者：</font>** Denis Fatykhoph, Timur Akhtyamov, Konstantin Pakulev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classical image correspondence is solved at the level of sparse keypoints or dense pixels, but the systems that consume these matches - object-level mapping, topological navigation, scene-graph maintenance - reason about whole objects. Recent work narrows this gap by matchng directly at the level of instance segments: a class-agnostic segmenter partitions each image, and per-segment descriptors are obtained by pooling features from large 3D foundation models over the masks. We build on this segment-level matching paradigm and propose three learned matching heads: a LightGlue-style attention head with DoubleSoftmax scoring on frozen MASt3R descriptors; a DPT-style multi-scale fusion module that exposes layered spatial detail from the VGGT foundation model before pooling; and - as our main contribution - a multi-view extension that performs joint self-attention over segments drawn from several views at once, recovering transitive correspondences that strictly pairwise matchers cannot reach. Under a stratified zero-shot protocol on Replica and Virtual KITTI 2 with controlled viewpoint baselines from 0 deg to 180 deg, the LightGlue-style head improves over a parameter-free Sinkhorn matcher on the same MASt3R backbone by +4.85 AUPRC on Replica and +25.9 AUPRC on Virtual KITTI 2. Dropped into the RoboHop topological navigation pipeline on the Habitat-Matterport 3D (HM3D) Instance Image Navigation benchmark without retraining, our multi-view variant raises success rate from 50% to 70%, and our LightGlue-style head raises SPL from 45.7 to 59.1.

---


### 341. [The Art of Not Forgetting](https://arxiv.org/abs/2607.17944)

**<font color=#1a73e8>作者：</font>** Ashmith Atmuri, Akshay Kumar, Yashaswini Rao Bhogarajula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce CMP (Cognitive Memory Primitive), an architecture that represents inputs as sparse relational codes, stores them in a two-tier competitive memory, and learns entirely through local, gradient-free updates, with no backpropagation anywhere in the network. We use this architecture to test a specific hypothesis: that catastrophic forgetting, usually treated as a training-time defect to be patched with replay or regularization, is instead a structural consequence of how backpropagation assigns credit and that a learning rule that is local and sparse by construction should resist it without a patch. On a controlled domain-incremental protocol across 15 text domains, three-seed replicated, CMP's backward transfer is 15-19x better than a matched-size Transformer trained with online EWC, and the result survives a domain-order control (reported as a range, +0.24 to +0.44, rather than a single figure). We report this alongside a real, substantial accuracy gap versus the Transformer baseline, a null result on a recognized vision benchmark, and a diagnosed, unresolved failure attempting to combine this architecture with a separate mechanism that improves raw accuracy, disclosed because an honest negative result is more useful than an omitted one. The central claim is narrow and falsifiable: local, sparse, non-backpropagation learning measurably resists catastrophic forgetting better than backpropagation with its standard fix, under conditions we state precisely.

---


### 342. [The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed Behavior in AI Systems](https://arxiv.org/abs/2607.17947)

**<font color=#1a73e8>作者：</font>** Samuel Presgraves  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing AI measurement frameworks quantify cognitive capability, task automation, or catastrophic risk, but none measure autonomous agency: the extent to which a system behaves in a self-directed way. A system can saturate capability benchmarks while remaining entirely reactive, acting only when prompted and ceasing all activity when a task completes. We introduce the Autonomous Agency Scale (AAS), a behavioral framework that scores AI systems on a 0-5 lexicon across seven dimensions of agency: cognitive autonomy, temporal persistence, environmental agency, social agency, creative agency, self-awareness, and goal formation, each operationalized by falsifiable threshold tests. Every dimension is scored in two temporal bands: an Active band covering engaged, user-initiated activity, and an Ambient band covering idle periods. Ambient Level 4 is gated by the Idle-Gap Test, a counterfactual criterion (remove all triggers and observe whether internally derived activity persists) that separates self-direction from scheduled rule-following. We apply the scale to six contemporary systems spanning task agents (Claude Code, Manus, Hermes), consumer assistants (ChatGPT, Siri), and a persistent companion architecture (Airi). The two-band profile quantifies a boundary that single-score frameworks conflate: task agents reach Active composites of 2.3-2.4 while scoring 0.6-1.9 Ambient, with every idle-period behavior attributable to user-configured schedules, whereas the companion architecture, evaluated longitudinally, is the only assessed system whose idle-period behavior survives trigger removal. We discuss limitations, including single-rater provenance, developer-evaluator bias on the longitudinal assessment, and the partially operationalized self-direction boundary in the Active band.

---


### 343. [RT-SHCUA: Real-Time Self-Hosted Computer-Use Agent for UAV Control](https://arxiv.org/abs/2607.17951)

**<font color=#1a73e8>作者：</font>** Di Lu, Bo Zhang, Xiyuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Natural-language control offers a promising interface for unmanned aerial vehicles (UAVs), but directly applying self-hosted computer-use agents (SHCUAs) to UAV control introduces a structural mismatch. SHCUAs are designed for interactive host-side tool use, where delayed agent iterations are often acceptable. UAV control, however, is coupled with continuously changing physical states, strict timing constraints, safety risks, and security accountability. A stale, unauthorized, or tampered agent decision may therefore lead to unsafe or untraceable vehicle behavior.
This paper proposes a real-time and security-oriented restructuring of SHCUA-based UAV control. Instead of allowing an SHCUA to directly issue flight commands, we transform its outputs into contract-bound UAV skill invocations with explicit timing, state, authority, fallback, and evidence semantics. Based on this abstraction, we design an architecture that separates semantic reasoning from onboard execution and security/safety enforcement. Slow cloud or edge reasoning is used for mission understanding, while onboard components validate and dispatch only timely, authorized, and state-consistent skills. Security-critical enforcement points can be protected by TEE-style or microcontroller isolation mechanisms without moving the full language agent or high-frequency flight-control loop into trusted components. Prototype evaluation shows that RT-SHCUA maintains bounded task-level responsiveness while supporting degraded handling, trusted admission, and auditable evidence preservation for SHCUA-mediated UAV actions.

---


### 344. [Topological Signatures of Context-Level Reliability in TabPFN](https://arxiv.org/abs/2607.17962)

**<font color=#1a73e8>作者：</font>** James Hu, Mahdi Ghelichi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TabPFN is a transformer-based foundation model for tabular prediction that performs inference without task-specific training by conditioning on a support set and query inputs. Despite its strong empirical performance, its internal behavior on structurally difficult tabular geometries remains poorly understood. We study this behavior using zigzag persistent homology, treating TabPFN layer representations as evolving point clouds. We construct a controlled benchmark of synthetic tabular tasks with known true probabilities and varied intrinsic topology, including warped circles, tori, spheres, Hopf links, trefoil knots, and Swiss rolls. Across these tasks, we find that the topology of TabPFN's internal representation geometry is strongly associated with dataset-level reliability; for example, the zeroth homology group $H_0$ fragmentation count correlates positively with mean absolute residual across controlled tasks, and this association strengthens in a high-resolution warped circle case study at large sample size. Harder geometries induce a dual topological signature: increased $H_1$ loop activity and increased $H_0$ fragmentation, while the $H_1$ persistence becomes shorter-lived. These descriptors correlate with Bayes error, mean absolute residuals, and overconfidence. Our results suggest that zigzag persistence diagnoses the reliability of the inferred in-context task geometry and provides a context-level view of when TabPFN operates in topologically stressed regimes.

---


### 345. [Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting](https://arxiv.org/abs/2607.17965)

**<font color=#1a73e8>作者：</font>** Chengbo Wang, Guozheng Ma, Jinhong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) employs Gaussian primitives for explicit scene representation, facilitating real-time, high-fidelity reconstruction and novel view synthesis of complex scenes. However, the explicit modeling inherent in 3DGS introduces a gradient bias during optimization, rendering its non-convex optimization process highly susceptible to convergence toward local suboptimal solutions. This constitutes a fundamental limitation in 3DGS optimization, which we term the Blur Trap. To address this limitation, we integrate simple explicit exploration into the 3DGS optimization framework. First, through rigorous mathematical analysis of the 3DGS optimization formulation, we identify the underlying optimization bias responsible for the Blur Trap and categorize it into two distinct subtypes: the Far-Side Blur Trap and the Near-Side Blur Trap. Subsequently, we propose two highly straightforward exploration strategies (Random Seeding and Random Splitting) to mitigate the far-side and near-side blur traps, respectively. Experimental validation demonstrates that the incorporation of these exploration operators effectively and complementarily overcome the Blur Trap, achieving high-quality rendering performance across multiple datasets. Project page: this https URL

---


### 346. [Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement](https://arxiv.org/abs/2607.17967)

**<font color=#1a73e8>作者：</font>** Lingyu Kong, Ruicheng Li, Ruicheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular geometry estimation has recently achieved impressive performance across diverse scenes. However, state-of-the-art models still face notable distortion in local 3D structure, especially in fine details, like thin structures and small objects. We attribute this limitation to an architectural mismatch: most current models decode 3D geometry within a 2D parameterization, where feature interactions are governed by image-plane proximity rather than true 3D spatial relationships. This inadvertently mixes features from geometrically distant surfaces, resulting in over-smoothed geometry particularly around thin or elongated structure. In this paper, we propose a fine-detail monocular geometry estimation with Self-Guided Sparse 3D Refinement (SSR) that lifts monocular geometry modeling from 2D image space to 3D space for high-fidelity metric-scale point maps. Our model lifts the coarse point map from a foundation base model onto a sparse voxel shell and refines it via SSR. The SSR employs sparse convolutions that aggregate features based on 3D spatial locality, avoiding feature mixing across depth discontinuities. Extensive experiments on diverse datasets demonstrate that our method significantly outperforms existing approaches in recovering fine detailed 3D geometry across both quantitative metrics and qualitative visualizations.

---


### 347. [DiFA: Inference-Time Forward-Process Alignment for Diffusion Models](https://arxiv.org/abs/2607.17972)

**<font color=#1a73e8>作者：</font>** Shigui Li, Delu Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The prevailing inference framework for diffusion models formulates generation fundamentally as a problem of numerical integration. This perspective casts the model as an exact estimator, neglecting the inherent statistical uncertainty of the denoising process. In this work, we propose Forward-Process Aligned Diffusion prediction (\textbf{DiFA}), a training-free framework that reframes inference-time data prediction refinement as a sequential state estimation problem. Rather than reusing past outputs solely for numerical integration, DiFA treats iterative data predictions along the reverse trajectory as correlated observations to build a forward-aligned temporal consensus. Inspired by Kalman filtering, this consensus aggregates historical predictions according to structural consistency and noise-level compatibility. To counteract the over-smoothing tendency of temporal consensus, we introduce a deviation guidance mechanism to adaptively preserve residual details. Empirically, DiFA yields significant improvements on CIFAR-10 and ImageNet across the evaluated metrics, including FID, IS, and FD-DINOv2, demonstrating that aligning inference with the forward statistical structure substantially improves generative fidelity.

---


### 348. [Information-Based Exploration via Random Features for Reinforcement Learning](https://arxiv.org/abs/2607.17981)

**<font color=#1a73e8>作者：</font>** Waris Radji, Odalric-Ambrym Maillard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning has enabled classical exploration strategies to be extended to deep Reinforcement Learning (RL), but often makes algorithms more complex and theoretical guarantees harder to establish. We introduce Random Feature Information Gain (RFIG), grounded in Bayesian kernel methods theory, which uses random Fourier features to approximate information gain and compute exploration bonuses in non-countable spaces. We provide error bounds on information gain approximation and avoid the black-box aspects of neural network-based uncertainty estimation, for optimism-based exploration. We present practical details that make RFIG scalable to deep RL scenarios, enabling smooth integration into standard deep RL algorithms. Experimental evaluation across diverse control and navigation tasks demonstrates that RFIG achieves competitive performance with well-established deep exploration methods while offering superior theoretical interpretation.

---


### 349. [Keyframe-Anchored Identity Preservation for Sequential-Action Video Generation](https://arxiv.org/abs/2607.17985)

**<font color=#1a73e8>作者：</font>** Zhenjie Liu, Binyan Chen, Hao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving text-to-video generation aims to synthesize a video that accurately follows a textual description while maintaining the recognizability of a user-specified subject throughout. The IPVG26 challenge extends this framework from a single holistic prompt to a temporally structured specification. The model additionally receives a sequence of timestamped action captions and must render the subject performing these actions in the specified order. This temporal structure presents a challenge not encountered in previous identity-preserving generation tasks, as the subject must continuously perform a scripted sequence of distinct actions while maintaining a consistent identity. However, end-to-end video generators are prone to appearance drift as motion accumulates and the depicted actions change. We address this challenge with a training-free, three-stage pipeline framework. An action-aware prompt polishment stage first rewrites the inputs into image-generation prompts that specify the terminal state of each action. An identity-preserving generation stage then produces the keyframe sequence by conditioning each frame jointly on the reference identity and its predecessor, thereby decoupling time-invariant appearance from time-varying pose. Finally, an identity-aware inference enhancement stage synthesizes the intermediate segments using multi-reference guidance and identity-driven noise searching, both of which reinforce identity fidelity during sampling. Our method ranked third on the official Track 2 leaderboard, demonstrating competitive performance and strong generality.

---


### 350. [Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?](https://arxiv.org/abs/2607.17986)

**<font color=#1a73e8>作者：</font>** Yimeng Chen, Nathanaël Denis, Roberto Di Pietro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-hosted AI agents read and write their own memory and configuration files to function. An agent may get compromised via corruption of its own state -- a compromise realized via legitimate OS system call invocation. We refer to this class of threats as self-state attacks. In this paper, we investigate the OS resilience to this class of attacks. Formally, we characterize a four-axis attack space (Target, Mechanism, Granularity, Temporal); investigate the structural limits of prevention, detection, and recovery; and introduce a workload-conditioned view of detectability. To instantiate the framework, we collect live activity traces from a representative self-hosted agent running across distinct workload profiles, and realize the attack space as a 23-cell matrix, 43 concrete operations on real self-state files, and injected into those traces. We then evaluate both canonical and workload-conditioned defense strategies. The empirical results show that a layered defense stack (access-control prevention on the instruction and configuration layers, workload-conditioned detection on the memory layer, and periodic backup for recovery) is effective on most attack cells while a small residual attack surface remains structurally indistinguishable at the OS level. These findings suggest that against the newly established class of self-state attacks, OS-level defense needs to be reconsidered, potentially opening new research directions in the field.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
