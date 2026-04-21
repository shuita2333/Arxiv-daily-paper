# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 201. [Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification](https://arxiv.org/abs/2604.17112)

**<font color=#1a73e8>作者：</font>** Kimia Hamidieh, Veronika Thost, Walter Gerych 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce confident yet incorrect responses, and uncertainty quantification is one potential solution to more robust usage. Recent works routinely rely on self-consistency to estimate aleatoric uncertainty (AU), yet this proxy collapses when models are overconfident and produce the same incorrect answer across samples. We analyze this regime and show that cross-model semantic disagreement is higher on incorrect answers precisely when AU is low. Motivated by this, we introduce an epistemic uncertainty (EU) term that operates in the black-box access setting: EU uses only generated text from a small, scale-matched ensemble and is computed as the gap between inter-model and intra-model sequence-semantic similarity. We then define total uncertainty (TU) as the sum of AU and EU. In a comprehensive study across five 7-9B instruction-tuned models and ten long-form tasks, TU improves ranking calibration and selective abstention relative to AU, and EU reliably flags confident failures where AU is low. We further characterize when EU is most useful via agreement and complementarity diagnostics.

---


### 202. [Inference-Time Temporal Probability Smoothing for Stable Video Segmentation with SAM2 under Weak Prompts](https://arxiv.org/abs/2604.17115)

**<font color=#1a73e8>作者：</font>** Dawar Jyoti Deka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video segmentation models such as SAM2 have demonstrated strong generalization across diverse visual domains. However, under weak user supervision, for example, when sparse point prompts are provided on a single frame, their predictions often suffer from temporal instability, including flickering boundaries, object dropout, and inconsistent object extents across frames. These issues limit their reliability in downstream video understanding and control applications.
In this paper, we propose an inference-time temporal probability smoothing method that improves the temporal stability of SAM2-based video segmentation without retraining or architectural modification. Our approach operates directly on per-frame segmentation probability maps and leverages optical-flow-based motion warping together with pixel-wise uncertainty estimates derived from segmentation entropy, and forward-backwards flow consistency. These signals are used to adaptively blend current-frame predictions with motion-aligned historical estimates, yielding temporally coherent segmentation outputs under weak prompts.
We evaluate the proposed method on four diverse video sequences using a comprehensive set of frame-wise and temporal stability metrics, including motion-compensated IoU, boundary consistency, object persistence, and area volatility. Experimental results demonstrate consistent improvements in temporal stability over vanilla SAM2 inference while preserving spatial accuracy. The proposed framework is lightweight, model-agnostic, and well-suited for real-time, interactive video segmentation.

---


### 203. [The Topological Trouble With Transformers](https://arxiv.org/abs/2604.17121)

**<font color=#1a73e8>作者：</font>** Michael C. Mozer, Shoaib Ahmed Siddiqui, Rosanne Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers encode structure in sequences via an expanding contextual history. However, their purely feedforward architecture fundamentally limits dynamic state tracking. State tracking -- the iterative updating of latent variables reflecting an evolving environment -- involves inherently sequential dependencies that feedforward networks struggle to maintain. Consequently, feedforward models push evolving state representations deeper into their layer stack with each new input step, rendering information inaccessible in shallow layers and ultimately exhausting the model's depth. While this depth limit can be bypassed by dynamic depth models and by explicit or latent thinking that externalizes state representations, these solutions are computationally and memory inefficient. In this article, we argue that temporally extended cognition requires refocusing from explicit thought traces to implicit activation dynamics via recurrent architectures. We introduce a taxonomy of recurrent and continuous-thought transformer architectures, categorizing them by their recurrence axis (depth versus step) and their ratio of input tokens to recurrence steps. Finally, we outline promising research directions, including enhanced state-space models and coarse-grained recurrence, to better integrate state tracking into modern foundation models.

---


### 204. [CASCADE: A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems](https://arxiv.org/abs/2604.17125)

**<font color=#1a73e8>作者：</font>** İpek Abasıkeleş Turgut, Edip Gümüş  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model Context Protocol (MCP) is a rapidly adopted standard for defining and invoking external tools in LLM applications. The multi-layered architecture of MCP introduces new attack surfaces such as tool poisoning, in addition to traditional prompt injection. Existing defense systems suffer from limitations including high false positive rates, API dependency, or white-box access requirements. In this study, we propose CASCADE, a three-tiered cascaded defense architecture for MCP-based systems: (i) Layer 1 performs fast pre-filtering using regex, phrase weighting, and entropy analysis; (ii) Layer 2 conducts semantic analysis via BGE embedding with an Ollama Llama3 fallback mechanism; (iii) Layer 3 applies pattern-based output filtering. Evaluation on a dataset of 5,000 samples yielded 95.85% precision, 6.06% false positive rate, 61.05% recall, and 74.59% F1-score. Analysis across 31 attack types categorized into 6 tiers revealed high detection rates for data exfiltration (91.5%) and prompt injection (84.2%), while semantic attack (52.5%) and tool poisoning (59.9%) categories showed potential for improvement. A key advantage of CASCADE over existing solutions is its fully local operation, requiring no external API calls

---


### 205. [Prompt Sensitivity in Vision-Language Grounding: How Small Changes in Wording Affect Object Detection](https://arxiv.org/abs/2604.17126)

**<font color=#1a73e8>作者：</font>** Dawar Jyoti Deka, Amit Sethi, Syed Mohammad Ali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models enable open-vocabulary object grounding through natural language queries, under the implicit assumption that semantically equivalent descriptions yield consistent outputs. We examine this assumption using a controlled pipeline combining DETR for object proposals with CLIP for language-conditioned selection on 263 COCO val2017 images. We find that overlapping prompts such as "a person," "a human," and "a pedestrian" frequently select different instances, with mean instability of 2.11 distinct selections across six prompts. PCA analysis shows this variability is structured and directional, not random. Prompt ensembling does not improve quality and often shifts selections toward generic regions. We further show that text embedding proximity explains only 34% of grounding disagreement (r = -0.58), confirming that instability arises from the argmax selection mechanism rather than text-level distances alone.

---


### 206. [The Privacy Placebo: Diagnosing Consent Burden through Performative Scrolling](https://arxiv.org/abs/2604.17129)

**<font color=#1a73e8>作者：</font>** Haoze Guo, Ziqi Wei  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While consent banners and privacy policies invite users to read and choose, many choices are shaped by repeated, low-yield interaction routines rather than deliberation. This paper studies performative scrolling: slow, low-information interaction that can signal attention to consent without substantially improving understanding. We present the Performative Scrolling Index (PSI), a reproducible interface-audit metric for measuring pre-choice burden before a meaningful non-accepting alternative becomes visible and actionable. PSI decomposes burden into four observable components: distance, time, focus loops, and hidden reveals. In this paper, PSI is the primary burden metric, while companion signals such as AAI, CSI, and divergence are used as secondary interpretive audit aids rather than standalone validated scales. We also provide a least-effort audit protocol, design-side invariants, a worked example, and a medium-scale live deployment across desktop and mobile conditions under pointer and keyboard traversal policies. Together, these analyses show how structural choices such as offscreen alternatives, fragmented disclosure, and staged modal flows can increase pre-choice friction without improving meaningful control. PSI is not a measure of comprehension or legal sufficiency; rather, it is a diagnostic of interface-side burden intended to support reproducible audits and redesigns.

---


### 207. [If Only My CGM Could Speak: A Privacy-Preserving Agent for Question Answering over Continuous Glucose Data](https://arxiv.org/abs/2604.17133)

**<font color=#1a73e8>作者：</font>** Yanjun Cui, Ali Emami, Temiloluwa Prioleau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitors (CGMs) used in diabetes care collect rich personal health data that could improve day-to-day self-management. However, current patient platforms only offer static summaries which do not support inquisitive user queries. Large language models (LLMs) could enable free-form inquiries about continuous glucose data, but deploying them over sensitive health records raises privacy and accuracy concerns. In this paper, we present CGM-Agent, a privacy-preserving framework for question answering over personal glucose data. In our design, the LLM serves purely as a reasoning engine that selects analytical functions. All computation occurs locally, and personal health data never leaves the user's device. For evaluation, we construct a benchmark of 4,180 questions combining parameterized question templates with real user queries and ground truth derived from deterministic program execution. Evaluating 6 leading LLMs, we find that top models achieve 94\% value accuracy on synthetic queries and 88\% on ambiguous real-world queries. Errors stem primarily from intent and temporal ambiguity rather than computational failures. Additionally, lightweight models achieve competitive performance in our agent design, suggesting opportunities for low-cost deployment. We release our code and benchmark to support future work on trustworthy health agents.

---


### 208. [RoIt-XMASA: Multi-Domain Multilingual Sentiment Analysis Dataset for Romanian and Italian](https://arxiv.org/abs/2604.17134)

**<font color=#1a73e8>作者：</font>** Andrei-Marius Avram, Aureliu Valentin Antonie, Cosmin-Mircea Croitoru 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present RoIt-XMASA, a multilingual dataset that extends the Cross-lingual Multi-domain Amazon Sentiment Analysis to Italian and Romanian, comprising 36,000 labeled reviews across three domains (books, movies, and music) and 202,141 unlabeled samples. To address cross-lingual and cross-domain challenges, we propose a multi-target adversarial training framework that employs loss reversal with meta-learned coefficients to dynamically balance sentiment discrimination with domain and language invariance. XLM-R achieves an F1-score of 66.23% with our approach, outperforming the baseline by 4.64%. Few-shot evaluation shows that Llama-3.1-8B achieves 58.43% F1-score, revealing a meaningful trade-off between the efficiency of prompting-based approaches and the higher performance of task-specific fine-tuning.

---


### 209. [OptiMVMap: Offline Vectorized Map Construction via Optimal Multi-vehicle Perspectives](https://arxiv.org/abs/2604.17135)

**<font color=#1a73e8>作者：</font>** Zedong Dan, Zijie Wang, Wei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Offline vectorized maps constitute critical infrastructure for high-precision autonomous driving and mapping services. Existing approaches rely predominantly on single ego-vehicle trajectories, which fundamentally suffer from viewpoint insufficiency: while memory-based methods extend observation time by aggregating ego-trajectory frames, they lack the spatial diversity needed to reveal occluded regions. Incorporating views from surrounding vehicles offers complementary perspectives, yet naive fusion introduces three key challenges: computational cost from large candidate pools, redundancy from near-collinear viewpoints, and noise from pose errors and occlusion artifacts.
We present OptiMVMap, which reformulates multi-vehicle mapping as a select-then-fuse problem to address these challenges systematically. An Optimal Vehicle Selection (OVS) module strategically identifies a compact subset of helpers that maximally reduce ego-centric uncertainty in occluded regions, addressing computation and redundancy challenges. Cross-Vehicle Attention (CVA) and Semantic-aware Noise Filter (SNF) then perform pose-tolerant alignment and artifact suppression before BEV-level fusion, addressing the noise challenge. This targeted pipeline yields more complete and topologically faithful maps with substantially fewer views than indiscriminate aggregation. On nuScenes and Argoverse2, OptiMVMap improves MapTRv2 by +10.5 mAP and +9.3 mAP, respectively, and surpasses memory-augmented baselines MVMap and HRMapNet by +6.2 mAP and +3.8 mAP on nuScenes. These results demonstrate that uncertainty-guided selection of helper vehicles is essential for efficient and accurate multi-vehicle vectorized mapping. The code is released at this https URL.

---


### 210. [BOIL: Learning Environment Personalized Information](https://arxiv.org/abs/2604.17137)

**<font color=#1a73e8>作者：</font>** Rohan Patil, Henrik I. Christensen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Navigating complex environments poses challenges for multi-agent systems, requiring efficient extraction of insights from limited information. In this paper, we introduce the Blackbox Oracle Information Learning (BOIL) process, a scalable solution for extracting valuable insights from the environment structure. Leveraging the Pagerank algorithm and common information maximization, BOIL facilitates the extraction of information to guide long-term agent behavior applicable to problems such as coverage, patrolling, and stochastic reachability. Through experiments, we demonstrate the efficacy of BOIL in generating strategy distributions conducive to improved performance over extended time horizons, surpassing heuristic approaches in complex environments.

---


### 211. [Local Inconsistency Resolution: The Interplay between Attention and Control in Probabilistic Models](https://arxiv.org/abs/2604.17140)

**<font color=#1a73e8>作者：</font>** Oliver E. Richardson, Mandana Samiei, Mehran Shakerinava 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a generic algorithm for learning and approximate inference with an intuitive epistemic interpretation: iteratively focus on a subset of the model and resolve inconsistencies using the parameters under control. This framework, which we call Local Inconsistency Resolution (LIR) is built upon Probabilistic Dependency Graphs (PDGs), which provide a flexible representational foundation capable of capturing inconsistent beliefs. We show how LIR unifies and generalizes a wide variety of important algorithms in the literature, including the Expectation-Maximization (EM) algorithm, belief propagation, adversarial training, GANs, and GFlowNets. In the last case, LIR actually suggests a more natural loss, which we demonstrate improves GFlowNet convergence. Each method can be recovered as a specific instance of LIR by choosing a procedure to direct focus (attention and control). We implement this algorithm for discrete PDGs and study its properties on synthetically generated PDGs, comparing its behavior to the global optimization semantics of the full PDG.

---


### 212. [SeekerGym: A Benchmark for Reliable Information Seeking](https://arxiv.org/abs/2604.17143)

**<font color=#1a73e8>作者：</font>** Remy Kim, Minseung Lee, Shuo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their substantial successes, AI agents continue to face fundamental challenges in terms of trustworthiness. Consider deep research agents, tasked with searching for information relevant to a given topic-while AI agents can perform effective information retrieval, there is little guarantee regarding the completeness of this information. Gaps in retrieved information can leave biases that mislead users even if the information they are given is correct and relevant. We introduce SeekerGym, a benchmark designed to evaluate the completeness of information retrieved by AI agents. In addition, SeekerGym also measures how well agents quantify their uncertainty in the completeness of their information; if an agent fails to retrieve all relevant information, it is useful for it to at least quantify how much might be missing. At a high level, each task in SeekerGym is a document (e.g., a Wikipedia article), and the AI agent must issue queries to retrieve passages from that document. Intuitively, the document comprehensively covers a topic, so the ability to retrieve its sections directly measures completeness of information retrieval. In addition to Wikipedia, we also consider machine learning survey papers, where the goal is to retrieve relevant sections of a survey paper. We benchmark several models and algorithms; the best approaches retrieve 42.5% of passages on Wikipedia and 29.2% on ML Surveys, leaving substantial room for improvement.

---


### 213. [ScenarioControl: Vision-Language Controllable Vectorized Latent Scenario Generation](https://arxiv.org/abs/2604.17147)

**<font color=#1a73e8>作者：</font>** Lili Gao, Yanbo Xu, William Koch 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ScenarioControl, the first vision-language control mechanism for learned driving scenario generation. Given a text prompt or an input image, Scenario-Control synthesizes diverse, realistic 3D scenario rollouts - including map, 3D boxes of reactive actors over time, pedestrians, driving infrastructure, and ego camera observations. The method generates scenes in a vectorized latent space that represents road structure and dynamic agents jointly. To connect multimodal control with sparse vectorized scene elements, we propose a cross-global control mechanism that integrates crossattention with a lightweight global-context branch, enabling fine-grained control over road layout and traffic conditions while preserving realism. The method produces temporally consistent scenario rollouts from the perspectives different actors in the scene, supporting long-horizon continuation of driving scenarios. To facilitate training and evaluation, we release a dataset with text annotations aligned to vectorized map structures. Extensive experiments validate that the control adherence and fidelity of ScenarioControl compare favorable to all tested methods across all experiments. Project webpage: this https URL

---


### 214. [From Legal Text to Executable Decision Models: Evaluating Structured Representations for Legal Decision Model Generation](https://arxiv.org/abs/2604.17153)

**<font color=#1a73e8>作者：</font>** David Graus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transforming legal text into executable decision logic is a longstanding challenge in legal informatics. With the rise of LLMs, this task has gained renewed interest, but remains challenging due to requiring extensive manual coding and evaluation. We use a unique real-world dataset that pairs production-grade decision models with legal text from the Dutch Environment and Planning Act. These models power the Omgevingsloket government platform, where citizens check permit requirements for environmental activities. We study whether intermediate structured representations can improve LLM-based generation of executable decision models from legal text. We compare four input conditions: raw legal text, text enriched with semantic role labels, text enriched with input and output constraints, and text enriched with both. We evaluate along two dimensions: structural evaluation, through similarity to gold decision models with graph kernels and graphs' descriptive statistics, and outcome evaluation, through functional equivalence by executing models on pre-configured test scenarios. Our findings show that I/O constraints provide the dominant improvement (+37-54% similarity over baseline), while semantic role labels show modest improvements. Outcome evaluation shows that generated models match the gold standard on 51-53% of test scenarios, even though generated models are typically smaller and simpler. We find LLMs eliminate redundant pass-through logic that comprises up to 45-55% of nodes. Importantly, structural similarity and outcome equivalence are complementary: structural similarity does not guarantee outcome equivalence, and vice versa. To facilitate reproducibility, we publicly release our dataset of 95 production decision models with associated legal text and all experimental code.

---


### 215. [Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155)

**<font color=#1a73e8>作者：</font>** Daniel Lieber, Alexander Mock, Nils Wandel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has recently become one of the most popular frameworks for photorealistic 3D scene reconstruction and rendering. While current rasterizers allow for efficient mappings of 3D Gaussian splats onto 2D camera views, this work focuses on mapping 2D image information (e.g. color, neural features or segmentation masks) efficiently back onto an existing scene of Gaussian splats. This 'opposite' direction enables applications ranging from scene relighting and stylization to 3D semantic segmentation, but also introduces challenges, such as view-dependent colorization and occlusion handling.
Our approach tackles these challenges using the normal equation to solve a visibility-weighted least squares problem for every Gaussian and can be implemented efficiently with existing differentiable rasterizers. We demonstrate the effectiveness of our approach on scene relighting, feature enrichment and 3D semantic segmentation tasks, achieving up to an order of magnitude speedup compared to gradient descent-based baselines.

---


### 216. [Uncertainty Quantification in PINNs for Turbulent Flows: Bayesian Inference and Repulsive Ensembles](https://arxiv.org/abs/2604.17156)

**<font color=#1a73e8>作者：</font>** Khemraj Shukla, Zongren Zou, Theo Kaeufer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have emerged as a promising framework for solving inverse problems governed by partial differential equations (PDEs), including the reconstruction of turbulent flow fields from sparse data. However, most existing PINN formulations are deterministic and do not provide reliable quantification of epistemic uncertainty, which is critical for ill-posed problems such as data-driven Reynolds-averaged Navier-Stokes (RANS) modeling. In this work, we develop and systematically evaluate a set of probabilistic extensions of PINNs for uncertainty quantification in turbulence modeling. The proposed framework combines (i) Bayesian PINNs with Hamiltonian Monte Carlo sampling and a tempered multi-component likelihood, (ii) Monte Carlo dropout, and (iii) repulsive deep ensembles that enforce diversity in function space. Particular emphasis is placed on the role of ensemble diversity and likelihood tempering in improving uncertainty calibration for PDE-constrained inverse problems. The methods are assessed on a hierarchy of test cases, including the Van der Pol oscillator and turbulent flow past a circular cylinder at Reynolds numbers Re=3,900 (direct numerical simulation data) and Re = 10,000 (experimental particle image velocimetry data). The results demonstrate that Bayesian PINNs provide the most consistent uncertainty estimates across all inferred quantities, while function-space repulsive ensembles offer a computationally efficient approximation with competitive accuracy for primary flow variables. These findings provide quantitative insight into the trade-offs between accuracy, computational cost, and uncertainty calibration in physics-informed learning, and offer practical guidance for uncertainty quantification in data-driven turbulence modeling.

---


### 217. [Lightweight Cybersickness Detection based on User-Specific Eye and Head Tracking Data in Virtual Reality](https://arxiv.org/abs/2604.17158)

**<font color=#1a73e8>作者：</font>** Yijun Wang, Mihai Bâce, Maria Torres Vega  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The occurrence of cybersickness in virtual reality (VR) significantly impairs users' perception and sense of immersion. Therefore, timely detection of cybersickness and the application of appropriate intervention strategies are crucial for enhancing the user experience. However, existing cybersickness detection methods often suffer from issues such as poor detection reliability across different levels of cybersickness and unnecessary model complexity. Furthermore, while cybersickness exhibits significant inter-user variability, most existing approaches aggregate all data from users and lack user-specific solutions. In this paper, we investigate a lightweight approach for cybersickness detection incorporating an ensemble learning model and user-specific eye and head tracking data. Our experiments using the open-source dataset Simulation 2021 demonstrate that feature engineering and training set construction are critical for determining detection performance. Models trained with data from similar-content segments achieve the best results, attaining detection accuracies of 93% in the cross-user setting and 88% in the user-personalized setting, using only 23-dimensional eye and head features. Moreover, by using user-specific data, well-tuned ensemble learning models with shorter training and inference times can be feasibly applied to real-world cybersickness detection, offering superior time efficiency and outstanding detection performance. This work offers useful evidence toward the development of lightweight and user-adaptive cybersickness detection models for VR applications.

---


### 218. [PPEDCRF: Dynamic-CRF-Guided Selective Perturbation for Background-Based Location Privacy in Video Sequences](https://arxiv.org/abs/2604.17163)

**<font color=#1a73e8>作者：</font>** Bo Ma, Weiqi Yan, Jinsong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose PPEDCRF, a calibrated selective perturbation framework that protects \emph{background-based location privacy} in released video frames against gallery-based retrieval attackers. Even after GPS metadata are stripped, an adversary can geolocate a frame by matching its background visual cues to geo-tagged reference imagery; PPEDCRF mitigates this threat by estimating location-sensitive background regions with a dynamic conditional random field (DCRF), rescaling perturbation strength with a normalized control penalty (NCP), and injecting Gaussian noise only inside the inferred regions via a DP-style calibration rule.
On a controlled paired-scene retrieval benchmark with eight attacker backbones and three noise seeds, PPEDCRF reduces ResNet18 Top-1 retrieval accuracy from 0.667 to $0.361\pm0.127$ at $\sigma_0=8$ while preserving $36.14\,$dB PSNR -- an ${\approx}6\,$dB quality advantage over global Gaussian noise. Transfer across the eight-backbone seed-averaged benchmark is broadly supportive (23 of 24 backbone-gallery cells show negative $\Delta$), while appendix-scale confirmation identifies MixVPR as a remaining adverse-transfer exception. Matched-operating-point analysis shows that PPEDCRF and global Gaussian noise converge in Top-1 privacy at equal utility, so the practical benefit is spatially concentrated perturbation that preserves higher visual quality at any given noise scale rather than stronger matched-utility privacy. Code: this https URL

---


### 219. [Decentralised Trust and Security Mechanisms for IoT Networks at the Edge: A Comprehensive Review](https://arxiv.org/abs/2604.17179)

**<font color=#1a73e8>作者：</font>** Khandoker Ashik Uz Zaman, Mahdi H. Miraz, Mohammed N. M. Ali  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> INTRODUCTION: The proliferation of the amalgamation of IoT and edge computing has increased the demand for decentralised trust and security mechanisms capable of operating across heterogeneous and resource-limited devices. Approaches such as federated learning, Zero Trust architectures, lightweight blockchain and distributed neural models offer alternatives to centralised control. OBJECTIVES: This review examines various state-of-the-art decentralised mechanisms and evaluates their effectiveness in terms of securing IoT networks at the edge. METHODS: Thirty recent studies were analysed to compare how decentralised architectures establish trust, support secure communication and enable intrusion and anomaly detection. Frameworks, such as DFGL-LZTA, SecFedDNN and COSIER were assessed. RESULTS: Decentralised designs enhance privacy, reduce single points of failure and improve adaptive threat response, though challenges remain in scalability, efficiency and interoperability. CONCLUSION: The study identifies key considerations and future research needs for building secure and resilient trust-aware IoT edge ecosystems.

---


### 220. [Beyond Overlap Metrics: Rewarding Reasoning and Preferences for Faithful Multi-Role Dialogue Summarization](https://arxiv.org/abs/2604.17188)

**<font color=#1a73e8>作者：</font>** Xiaoyong Mei, Tingting Zuo, Da Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-role dialogue summarization requires modeling complex interactions among multiple speakers while preserving role-specific information and factual consistency. However, most existing methods optimize for automatic metrics such as ROUGE and BERTScore, which favor surface-level imitation of references rather than genuine gains in faithfulness or alignment with human preferences. We propose a novel framework that couples explicit cognitive-style reasoning with reward-based optimization for multi-role dialogue summarization. Our method first distills structured reasoning traces (e.g., step-by-step inferences and intermediate reflections) from a large teacher model and uses them as auxiliary supervision to initialize a reasoning-aware summarizer via staged supervised fine-tuning. It then applies GRPO with a dual-principle reward that blends metric-based signals with human-aligned criteria targeting key information coverage, implicit inference, factual faithfulness, and conciseness. Experiments on multilingual multi-role dialogue benchmarks show that our method matches strong baselines on ROUGE and BERTScore. Specifically, results on CSDS confirm the framework's stability in semantic consistency, while in-depth analysis on SAMSum demonstrates clear gains in factual faithfulness and model-based preference alignment. These findings underscore the value of reasoning-aware and preference-aware training for reliable dialogue summarization. Checkpoints and datasets are available at this https URL.

---


### 221. [DreamShot: Personalized Storyboard Synthesis with Video Diffusion Prior](https://arxiv.org/abs/2604.17195)

**<font color=#1a73e8>作者：</font>** Junjia Huang, Binbin Yang, Pengxiang Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Storyboard synthesis plays a crucial role in visual storytelling, aiming to generate coherent shot sequences that visually narrate cinematic events with consistent characters, scenes, and transitions. However, existing approaches are mostly adapted from text-to-image diffusion models, which struggle to maintain long-range temporal coherence, consistent character identities, and narrative flow across multiple shots. In this paper, we introduce DreamShot, a video generative model based storyboard framework that fully exploits powerful video diffusion priors for controllable multi-shot synthesis. DreamShot supports both Text-to-Shot and Reference-to-Shot generation, as well as story continuation conditioned on previous frames, enabling flexible and context-aware storyboard generation. By leveraging the spatial-temporal consistency inherent in video generative models, DreamShot produces visually and semantically coherent sequences with improved narrative fidelity and character continuity. Furthermore, DreamShot incorporates a multi-reference role conditioning module that accepts multiple character reference images and enforces identity alignment via a Role-Attention Consistency Loss, explicitly constraining attention between reference and generated roles. Extensive experiments demonstrate that DreamShot achieves superior scene coherence, role consistency, and generation efficiency compared to state-of-the-art text-to-image storyboard models, establishing a new direction toward controllable video model-driven visual storytelling.

---


### 222. [Learning to Control Summaries with Score Ranking](https://arxiv.org/abs/2604.17197)

**<font color=#1a73e8>作者：</font>** Hongye Liu, Liang Ding, Ricardo Henao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in summarization research focus on improving summary quality across multiple criteria, such as completeness, conciseness, and faithfulness, by jointly optimizing these dimensions. However, these efforts largely overlook the challenge of controlling summary generation with respect to individual criteria, especially in the presence of their inherent trade-offs. For example, enhancing conciseness can compromise completeness, and vice versa. In this work, we address this gap by proposing a loss function that aligns model outputs with fine-grained, model-based evaluation scores (e.g., from FineSurE), enabling both improvement in summary quality and dimension-specific control. Our approach improves the overall quality of summaries while maintaining the ability to selectively prioritize one criterion over others. Experiments on three pretrained models (LLaMA, Qwen, and Mistral) demonstrate that our method achieves performance comparable to state-of-the-art summarizers, while uniquely offering strong controllability over individual quality dimensions.

---


### 223. [Calibrating Model-Based Evaluation Metrics for Summarization](https://arxiv.org/abs/2604.17200)

**<font color=#1a73e8>作者：</font>** Hongye Liu, Dhanajit Brahma, Ricardo Henao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in summary evaluation are based on model-based metrics to assess quality dimensions, such as completeness, conciseness, and faithfulness. However, these methods often require large language models, and predicted scores are frequently miscalibrated, limiting their reliability. Moreover, evaluating the average quality across different summaries for a single document typically requires access to multiple reference summaries. Here, we propose a general framework that generates individual and average proxy scores without relying on reference summaries, human annotations, or expensive model-based metrics. We also propose group isotonic regression binning (GIRB), a calibration method that adjusts the raw predictions to better align with ground-truth evaluation metrics. While we focus on continuous-value scenarios, such as summarization, the method is applicable to discrete-value tasks, such as question answering. Experiments on seven datasets demonstrate that our approach consistently outperforms existing baselines.

---


### 224. [CDSA-Net:Collaborative Decoupling of Vascular Structure and Background for High-Fidelity Coronary Digital Subtraction Angiography](https://arxiv.org/abs/2604.17208)

**<font color=#1a73e8>作者：</font>** Si Li, Chen-Kai Hu, Zhenhuan Lyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital subtraction angiography (DSA) in coronary imaging is fundamentally challenged by physiological motion, forcing reliance on raw angiograms cluttered with anatomical noise. Existing deep learning methods often produced images with two critical clinically unacceptable flaws: persistent boundary artifacts and a loss of native tissue grayscale fidelity that undermined diagnostic confidence. We propose a novel framework termed as CDSA-Net that for the first time explicitly decouples and jointly optimizes vascular structure preservation and realistic background restoration. CDSA-Net introduces two core innovations: (i) A hierarchical geometric prior guidance (HGPG) mechanism, embedded in our coronary structure extraction network (CSENet). It synergistically combines integrated geometric prior (IGP) with gated spatial modulation (GSM) and centerline-aware topology (CAT) loss supervision, ensuring structural continuity. (ii) An adaptive noise module (ANM) within our coronary background restoration network (CBResNet). Unlike standard restoration, ANM uniquely models the stochastic nature of clinical X-ray noise, bridging the domain gap to enable seamless background intensity estimation and the complete elimination of boundary artifacts. The final subtraction is obtained by removing the restored background from the raw angiogram. Quantitatively, it significantly outperformed state-of-the-art methods in vascular intensity correlation and perceptual quality. A 25.6% improvement in morphology assessment efficiency and a 42.9% gain in hemodynamic evaluation speed set a new benchmark for utility in interventional cardiology, while maintaining diagnostic results consistent with raw angiograms. The project code is available at this https URL.

---


### 225. [EmbodiedHead: Real-Time Listening and Speaking Avatar for Conversational Agents](https://arxiv.org/abs/2604.17211)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Kaiyuan Shen, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present EmbodiedHead, a speech-driven talking-head framework that equips LLMs with real-time visual avatars for conversation. A practical embodied avatar must achieve real-time generation, unified listening-speaking behavior, and high rendered visual quality simultaneously. Our framework couples the first Rectified-Flow Diffusion Transformer (DiT) for this task with a differentiable renderer, enabling diverse, high-fidelity generation in as few as four sampling steps. Prior listening-speaking methods rely on dual-stream audio, introducing an interlocutor look-ahead dependency incompatible with causal user--LLM interaction. We instead adopt a single-stream interface with explicit per-frame listening-speaking state conditioning and a Streaming Audio Scheduler, suppressing spurious mouth motion during listening while enabling seamless turn-taking. A two-stage training scheme of coefficient-space pretraining and joint image-domain refinement further closes the gap between motion-level supervision and rendered quality. Extensive experiments demonstrate state-of-the-art visual quality and motion fidelity in both speaking and listening scenarios.

---


### 226. [Region-Affinity Attention for Whole-Slide Breast Cancer Classification in Deep Ultraviolet Imaging](https://arxiv.org/abs/2604.17222)

**<font color=#1a73e8>作者：</font>** Nagur Shareef Shaik, Teja Krishna Cherukuri, Dong Hye Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer diagnosis demands rapid and precise tools, yet traditional histopathological methods often fall short in intra-operative settings. Deep Ultraviolet (DUV) fluorescence imaging emerges as a transformative approach, offering high-contrast, label-free visualization of whole-slide images (WSIs) with unprecedented detail, surpassing conventional hematoxylin and eosin (H&E) staining in speed and resolution. However, existing deep learning methods for breast cancer classification, predominantly patch-based, fragment spatial context and incur significant preprocessing overhead, limiting their clinical utility. Moreover, standard attention mechanisms, such as Spatial, Squeeze-and-Excitation, Global Context and Guided Context Gating, fail to fully exploit the rich, multi-scale regional relationships inherent in DUV-WSI data, often prioritizing generic feature recalibration over diagnostic specificity. This study introduces a novel Region-Affinity Attention mechanism tailored for DUV-WSI breast cancer classification, processing entire slides without patching to preserve spatial integrity. By modeling local neighbor distances and constructing a full affinity matrix, our method dynamically highlights diagnostically relevant regions, augmented by a contrastive loss to enhance feature discriminability. Evaluated on a dataset of 136 DUV-WSI samples, our approach achieves an accuracy of 92.67 +/- 0.73% and an AUC of 95.97%, outperforming existing attention methods.

---


### 227. [LASER: Low-Rank Activation SVD for Efficient Recursion](https://arxiv.org/abs/2604.17224)

**<font color=#1a73e8>作者：</font>** Ege Çakar, Ketan Ali Raghu, Lia Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive architectures such as Tiny Recursive Models (TRMs) perform implicit reasoning through iterative latent computation, yet the geometric structure of these reasoning trajectories remains poorly understood. We investigate the activation manifold of TRMs during recursive unrolling and find that activations occupy an effectively linear, low-dimensional subspace whose principal directions can be tracked dynamically with cheap power iterations. This suggests that weight-sharing concentrates iterative computation along a small number of dominant eigendirections, and we find that this concentration varies sharply across computational sites. We exploit this structure through LASER (Low-Rank Activation SVD for Efficient Recursion), a dynamic compression framework that maintains an evolving low-rank basis via matrix-free subspace tracking with a fidelity-triggered reset mechanism, achieving ${\sim}60\%$ activation memory savings with no statistically significant accuracy degradation. Our analysis raises questions about how recursive architectures allocate representational capacity during implicit reasoning, and whether this concentration can be exploited to improve the efficiency and stability of latent computation.

---


### 228. [A Multi-Agent Approach for Claim Verification from Tabular Data Documents](https://arxiv.org/abs/2604.17225)

**<font color=#1a73e8>作者：</font>** Rudra Ranajee Saha, Laks V. S. Lakshmanan, Raymond T. Ng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a novel approach for claim verification from tabular data documents. Recent LLM-based approaches either employ complex pretraining/fine-tuning or decompose verification into subtasks, often lacking comprehensive explanations and generalizability. To address these limitations, we propose a Multi-Agentic framework for Claim verification (MACE) consisting of three specialized agents: Planner, Executor, and Verifier. Instead of elaborate finetuning, each agent employs a zero-shot Chain-of-Thought setup to perform its tasks. MACE produces interpretable verification traces, with the Planner generating explicit reasoning strategies, the Executor providing detailed computation steps, and the Verifier validating the logic. Experiments demonstrate that MACE achieves state-of-the-art (SOTA) performance on two datasets and performs on par with the best models on two others, while achieving 80--100\% of best performance with substantially smaller models: 27--92B parameters versus 235B. This combination of competitive performance, memory efficiency, and transparent reasoning highlights our framework's effectiveness.

---


### 229. [Revisiting Auxiliary Losses for Conditional Depth Routing: An Empirical Study](https://arxiv.org/abs/2604.17228)

**<font color=#1a73e8>作者：</font>** Qingwei Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional depth execution routes a subset of tokens through a lightweight cheap FFN while the remainder execute the standard full FFN at each controlled layer. The central difficulty is gate training: the gate decision must propagate through many layers before it influences the language modeling (LM) loss, so the resulting gradients are weak and noisy. Auxiliary losses are commonly stacked to stabilise training, yet the interactions among them -- particularly between a predictive auxiliary and explicit score supervision -- have not been systematically compared under controlled conditions.
We evaluate two gate designs under a 157.5M-parameter decoder-only model with controller-only training, 50% full-path budget, and 3-seed runs on a fineweb-edu subset. The MLP gate (G1) maps the current hidden state to a utility score; the JEPA-guided gate (G3) adds an action-conditional predictor that forecasts, in a low-dimensional latent space, the outcome of executing full vs. cheap per token, aligned against a fixed target head. Under the standard recipe with oracle-style utility regression and pairwise rank supervision (util/rank), G3 improves early-to-mid optimisation over G1 in 3/3 seeds (lower avg LM, faster threshold hits, ~10.3x lower grad norms), with 20k-step endpoint LM within a 0.005 heuristic reference.
A key finding (ablation A3): jointly removing util/rank improves best/avg LM and threshold-hit speed in 3/3 seeds for both gates, and the early-to-mid advantage of G3 over G1 disappears. We trace this to an off-policy oracle label that assumes all subsequent layers execute full, whereas gated execution routes only a fraction through full -- making util/rank net-negative under the current recipe. Removing util/rank also cuts the training FLOPs proxy from ~1.53x to ~1.07x full-only (2.87h to 1.75h on a V100-32GB, ~39%). Conclusions are scoped to the studied regime.

---


### 230. [Yanasse: Finding New Proofs from Deep Vision's Analogies, Part 1](https://arxiv.org/abs/2604.17229)

**<font color=#1a73e8>作者：</font>** Alexandre Linhares  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Project Yanasse presents a method for discovering new proofs of theorems in one area of mathematics by transferring proof strategy patterns (e.g., Lean 4 tactic invocation patterns) from a structurally distant area. The system extracts tactic usage distributions across 27 top-level areas of Mathlib (217,133 proof states), computes z-scores to identify tactics that are heavily used in a source area but rare or absent in a target area, matches source and target proof states via GPU-accelerated NP-hard analogy (running on a MacBook Air via Apple's MPS backend), and then asks an AI reasoning agent to semantically adapt--not symbol-substitute--the source tactics invocation pattern to the target theorem. In this first part of the study, the method is applied to the pair Probability -> Representation Theory, producing 4 Lean-verified new proofs out of 10 attempts (40%). The proofs compile with zero sorry declarations. The key finding is that tactic schemas decompose into a head (domain-gated, rarely transfers) and a modifier (domain-general, often transfers): filter upwards's head fails in representation theory (no Filter structure), but its [LIST] with {\omega} modifier transfers cleanly as ext1 + simp [LIST] + rfl. Crucially, the underlying matching engine--deep vision this http URL--is entirely domain independent: the same optimization code for an NP-hard matching that matches chess positions by analogy matches Lean proof states by analogy, without knowing which domain it is processing. Only a relation extractor is domain-specific.

---


### 231. [Fringe Projection Based Vision Pipeline for Autonomous Hard Drive Disassembly](https://arxiv.org/abs/2604.17231)

**<font color=#1a73e8>作者：</font>** Badrinath Balasubramaniam, Vignesh Suresh, Benjamin Metcalf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unrecovered e-waste represents a significant economic loss. Hard disk drives (HDDs) comprise a valuable e-waste stream necessitating robotic disassembly. Automating the disassembly of HDDs requires holistic 3D sensing, scene understanding, and fastener localization, however current methods are fragmented, lack robust 3D sensing, and lack fastener localization. We propose an autonomous vision pipeline which performs 3D sensing using a Fringe Projection Profilometry (FPP) module, with selective triggering of a depth completion module where FPP fails, and integrates this module with a lightweight, real-time instance segmentation network for scene understanding and critical component localization. By utilizing the same FPP camera-projector system for both our depth sensing and component localization modules, our depth maps and derived 3D geometry are inherently pixel-wise aligned with the segmentation masks without registration, providing an advantage over RGB-D perception systems common in industrial sensing. We optimize both our trained depth completion and instance segmentation networks for deployment-oriented inference. The proposed system achieves a box mAP@50 of 0.960 and mask mAP@50 of 0.957 for instance segmentation, while the selected depth completion configuration with the Depth Anything V2 Base backbone achieves an RMSE of 2.317 mm and MAE of 1.836 mm; the Platter Facing learned inference stack achieved a combined latency of 12.86 ms and a throughput of 77.7 Frames Per Second (FPS) on the evaluation workstation. Finally, we adopt a sim-to-real transfer learning approach to augment our physical dataset. The proposed perception pipeline provides both high-fidelity semantic and spatial data which can be valuable for downstream robotic disassembly. The synthetic dataset developed for HDD instance segmentation will be made publicly available.

---


### 232. [Breaking Euston: Recovering Private Inputs from Secure Inference by Exploiting Subspace Leakage](https://arxiv.org/abs/2604.17238)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhao, Fengwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the 47th IEEE Symposium on Security and Privacy (IEEE S&P 2026), Gao et al. proposed an efficient and user-friendly secure transformer inference framework, namely Euston. In Euston, a singular value decomposition-based matrix transmission protocol is designed to efficiently transmit input matrices, reducing communication bandwidth by approximately 2.8 times. In this manuscript, we show that this transmission protocol introduces subspace leakage of random masks, enabling the model owner to recover private samples easily. We further validate the effectiveness of the recovery attack through simple experiments on image and language datasets, highlighting a fundamental privacy risk of the protocol design.

---


### 233. [Safe and Policy-Compliant Multi-Agent Orchestration for Enterprise AI](https://arxiv.org/abs/2604.17240)

**<font color=#1a73e8>作者：</font>** Vinil Pasupuleti, Shyalendar Reddy Allala, Siva Rama Krishna Varma Bayyavarapu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI systems increasingly deploy multiple intelligent agents across mission-critical workflows that must satisfy hard policy constraints, bounded risk exposure, and comprehensive auditability (SOX, HIPAA, GDPR). Existing coordination methods - cooperative MARL, consensus protocols, and centralized planners - optimize expected reward while treating constraints implicitly. This paper introduces CAMCO (Constraint-Aware Multi-Agent Cognitive Orchestration), a runtime coordination layer that models multi-agent decision-making as a constrained optimization problem. CAMCO integrates three mechanisms: (i) a constraint projection engine enforcing policy-feasible actions via convex projection, (ii) adaptive risk-weighted Lagrangian utility shaping, and (iii) an iterative negotiation protocol with provably bounded convergence. Unlike training-time constrained RL, CAMCO operates as deployment-time middleware compatible with any agent architecture, with policy predicates designed for direct integration with production engines such as OPA. Evaluation across three enterprise scenarios - including comparison against a constrained Lagrangian MARL baseline - demonstrates zero policy violations, risk exposure below threshold (mean ratio 0.71), 92-97% utility retention, and mean convergence in 2.4 iterations.

---


### 234. [Seeing Isn't Believing: Mitigating Belief Inertia via Active Intervention in Embodied Agents](https://arxiv.org/abs/2604.17252)

**<font color=#1a73e8>作者：</font>** Hanlin Wang, Chak Tou Leong, Jian Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models (LLMs) have enabled agents to tackle complex embodied tasks through environmental interaction. However, these agents still make suboptimal decisions and perform ineffective actions, as they often overlook critical environmental feedback that differs from their internal beliefs. Through a formal probing analysis, we characterize this as belief inertia, a phenomenon where agents stubbornly adhere to prior beliefs despite explicit observations. To address this, we advocate active belief intervention, moving from passive understanding to active management. We introduce the Estimate-Verify-Update (EVU) mechanism, which empowers agents to predict expected outcomes, verify them against observations through explicit reasoning, and actively update prior beliefs based on the verification evidence. EVU is designed as a unified intervention mechanism that generates textual belief states explicitly, and can be integrated into both prompting-based and training-based agent reasoning methods. Extensive experiments across three embodied benchmarks demonstrate that EVU consistently yields substantial gains in task success rates. Further analyses validate that our approach effectively mitigates belief inertia, advancing the development of more robust embodied agents. Our code is available at this https URL.

---


### 235. [A Unified Compliance Aggregator Framework for Automated Multi-Tool Security Assessment of Linux Systems](https://arxiv.org/abs/2604.17256)

**<font color=#1a73e8>作者：</font>** Sheldon Paul, Izzat Alsmadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Assessing the security posture of modern computing systems typically requires the use of multiple specialized tools. These tools focus on different aspects such as configuration compliance, file integrity, and vulnerability exposure, and their outputs are often difficult to interpret collectively. This paper introduces the Unified Compliance Aggregator (UCA), a framework that integrates several open-source security tools into a single composite score representing overall system security. The proposed framework combines outputs from Lynis, OpenSCAP (STIG and CIS profiles), AIDE, Tripwire, and Nmap NSE. A normalization process converts heterogeneous outputs into a consistent 0 to 100 scale, followed by weighted aggregation. We also introduce a logarithmic scoring model for file integrity measurements to address limitations observed in prior linear approaches. Experiments were conducted on Ubuntu 22.04 across different hardening levels and environments. Results show consistent improvement in composite scores as systems are hardened, while also revealing contrasting behavior between compliance and file integrity tools. Two case studies, a basic web server and a DVWA-based system illustrate how the framework can be applied in practical scenarios.

---


### 236. [REZE: Representation Regularization for Domain-adaptive Text Embedding Pre-finetuning](https://arxiv.org/abs/2604.17257)

**<font color=#1a73e8>作者：</font>** Seungmin Lee, Jeonghwan Lee, Hyunkuk Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent text embedding models are often adapted to specialized domains via contrastive pre-finetuning (PFT) on a naive collection of scattered, heterogeneous tasks. However, this approach often introduces task-induced bias alongside domain knowledge, leading to uncontrolled representation shifts that distort the pretrained embedding geometry and cause substantial performance degradation. To address this issue, we propose REZE}, a representation regularization framework that explicitly controls representation shift during embedding pre-finetuning. REZE operates on the relations of anchor-positive pairs and decomposes them in an eigenspace. It then measures task-wise dispersion along each eigencomponent to identify task-variant directions and applies adaptive soft-shrinkage to suppress task-induced noise while preserving task-invariant semantic structure, without inference-time overhead. Experiments across multiple embedding backbones and specialized benchmarks show that REZE outperforms standard pre-finetuning and isotropy-oriented post-hoc regularization in most settings, remaining stable where existing PFT variants collapse. Embedding space analyses further confirm that REZE induces controlled shifts aligned with the original embedding manifold, underscoring representation shift control as a key principle for robust embedding pre-finetuning under heterogeneous supervision.

---


### 237. [Rethinking Meeting Effectiveness: A Benchmark and Framework for Temporal Fine-grained Automatic Meeting Effectiveness Evaluation](https://arxiv.org/abs/2604.17260)

**<font color=#1a73e8>作者：</font>** Yihang Li, Chenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating meeting effectiveness is crucial for improving organizational productivity. Current approaches rely on post-hoc surveys that yield a single coarse-grained score for an entire meeting. The reliance on manual assessment is inherently limited in scalability, cost, and reproducibility. Moreover, a single score fails to capture the dynamic nature of collaborative discussions. We propose a new paradigm for evaluating meeting effectiveness centered on novel criteria and temporal fine-grained approach. We define effectiveness as the rate of objective achievement over time and assess it for individual topical segments within a meeting. To support this task, we introduce the AMI Meeting Effectiveness (AMI-ME) dataset, a new meta-evaluation dataset containing 2,459 human-annotated segments from 130 AMI Corpus meetings. We also develop an automatic effectiveness evaluation framework that uses a Large Language Model (LLM) as a judge to score each segment's effectiveness relative to the overall meeting objectives. Through substantial experiments, we establish a comprehensive benchmark for this new task and evaluate the framework's generalizability across distinct meeting types, ranging from business scenarios to unstructured discussions. Furthermore, we benchmark end-to-end performance starting from raw speech to measure the capabilities of a complete system. Our results validate the framework's effectiveness and provide strong baselines to facilitate future research in meeting analysis and multi-party dialogue. Our dataset and code will be publicly available. The AMI-ME dataset and the Automatic Evaluation Framework are available at: this URL.

---


### 238. [Fractal Characterization of Low-Correlation Signals in AI-Generated Image Detection](https://arxiv.org/abs/2604.17268)

**<font color=#1a73e8>作者：</font>** Wenwei Xie, Jie Yin, Lu Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated imagery has reached near-photorealistic fidelity, yet this technology poses significant threats to information security and societal trust. Existing deepfake detection methods often exhibit limited robustness in open-world scenarios. To address this limitation, this paper investigates intrinsic discrepancies between synthetic and authentic images from a signal-level perspective. Our analysis reveals that low-correlation signals serve as distinctive markers for differentiating AI-generated imagery from real photographs. Building on this insight, we introduce a novel method for quantifying these signals based on fractal theory. By analyzing the fractal characteristics of low-correlation signals, our method effectively captures the subtle statistical anomalies inherent to the synthesis process. Extensive experimental results demonstrate the method's robustness and superior detection performance. This work emphasizes the need to shift research focus to a new signal-level direction for deepfake detection. Theoretically, this proposed approach is not limited to face image identification but can be applied to all AI-generated image detection tasks. This study provides a new research direction for deepfake detection.

---


### 239. [What Security and Privacy Transparency Users Need from Consumer-Facing Generative AI](https://arxiv.org/abs/2604.17270)

**<font color=#1a73e8>作者：</font>** Jiaxun Cao, Yu Dong, Chunxi Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users increasingly rely on consumer-facing generative AI (GenAI) for tasks ranging from everyday needs to sensitive use cases. Yet, it remains unclear whether and how existing security and privacy (S&P) communications in GenAI tools shape users' adoption decisions and subsequent experiences. Understanding how users seek, interpret, and evaluate S&P information is critical for designing usable transparency that users can trust and act on. We conducted semi-structured interviews and design sessions with 21 U.S. GenAI users. We find that available S&P information rarely drove initial adoption in practice, as participants often perceived it as incomplete, ineffective, or lacking credibility. Instead, they relied on rough proxies, such as popularity, to infer S&P practices. After adoption, uncertainty about S&P practices constrained participants' willingness to use GenAI tools, particularly in high-stakes contexts, and, in some cases, contributed to discontinued use. Participants therefore called for transparency that supports decision-making and use, including trustworthy information (e.g., independent evaluations) and usable interfaces (e.g., on-demand disclosure). We synthesize participants' desired design practices into five dimensions to facilitate systematic future investigation into best practices. We conclude with recommendations for researchers, designers, and policymakers to improve S&P transparency in consumer-facing GenAI.

---


### 240. [The Continuity Layer: Why Intelligence Needs an Architecture for What It Carries Forward](https://arxiv.org/abs/2604.17273)

**<font color=#1a73e8>作者：</font>** Samuel Sameer Tanguturi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The most important architectural problem in AI is not the size of the model but the absence of a layer that carries forward what the model has come to understand. Sessions end. Context windows fill. Memory APIs return flat facts that the model has to reinterpret from scratch on every read. The result is intelligence that is powerful per session and amnesiac across time. This position paper argues that the layer which fixes this, the continuity layer, is the most consequential piece of infrastructure the field has not yet built, and that the engineering work to build it has begun in public. The formal evaluation framework for the property described here is the ATANT benchmark (arXiv:2604.06710), published separately with evaluation results on a 250-story corpus; a companion paper (arXiv:2604.10981) positions this framework against existing memory, long-context, and agentic-memory benchmarks. The paper defines continuity as a system property with seven required characteristics, distinct from memory and from retrieval; describes a storage primitive (Decomposed Trace Convergence Memory) whose write-time decomposition and read-time reconstruction produce that property; maps the engineering architecture to the theological pattern of kenosis and the symbolic pattern of Alpha and Omega, and argues this mapping is structural rather than metaphorical; proposes a four-layer development arc from external SDK to hardware node to long-horizon human infrastructure; examines why the physics limits now constraining the model layer make the continuity layer newly consequential; and argues that the governance architecture (privacy implemented as physics rather than policy, founder-controlled class shares on non-negotiable architectural commitments) is inseparable from the product itself.

---


### 241. [Fully Analog Resonant Recurrent Neural Network via Metacircuit](https://arxiv.org/abs/2604.17277)

**<font color=#1a73e8>作者：</font>** Zixin Zhou, Tianxi Jiang, Menglong Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical neural networks offer a transformative route to edge intelligence, providing superior inference speed and energy efficiency compared to conventional digital architectures. However, realizing scalable, end-to-end, fully analog recurrent neural networks for temporal information processing remains challenging due to the difficulty of faithfully mapping trained network models onto physical hardware. Here we present a fully analog resonant recurrent neural network (R$^2$NN) implemented via a metacircuit architecture composed of coupled electrical local resonators. A reformulated mechanical-electrical analogy establishes a direct mapping between the R$^2$NN model and metacircuit elements, enabling accurate physical implementation of trained neural network parameters. By integrating jointly trainable global resistive coupling and local resonances, which generate effective frequency-dependent negative resistances, the architecture shapes an impedance landscape that steers currents along frequency-selective pathways. This mechanism enables direct extraction of discriminative spectral features, facilitating real-time temporal classification of raw analog inputs while bypassing analog-to-digital conversion. We demonstrate the cross-domain versatility of this framework using integrated hardware for tactile perception, speech recognition, and condition monitoring. This work establishes a scalable, fully analog paradigm for intelligent temporal processing and paves the way for low-latency, resource-efficient physical neural hardware for edge intelligence.

---


### 242. [MedPRMBench: A Fine-grained Benchmark for Process Reward Models in Medical Reasoning](https://arxiv.org/abs/2604.17282)

**<font color=#1a73e8>作者：</font>** Lingyan Wu, Xiang Zheng, Weiqi Zhai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process-Level Reward Models (PRMs) are essential for guiding complex reasoning in large language models, yet existing PRM benchmarks cover only general domains such as mathematics, failing to address medical reasoning -- which is uniquely characterized by safety criticality, knowledge intensity, and diverse error patterns. Without a reliable medical PRM evaluation framework, we cannot quantify models' error detection capabilities in clinical reasoning, leaving their safety in real-world healthcare applications unverified. We propose MedPRMBench, the first process-level reward model benchmark for the medical domain. Built through a three-phase pipeline based on Clinical Reasoning Blueprints (CRBs), MedPRMBench systematically generates high-quality evaluation data from seven medical QA sources, covering 14 fine-grained error types across three categories (Simplicity, Soundness, and Sensitivity) with the first 4-level severity grading system to quantify clinical impact. The benchmark comprises 6{,}500 questions with 13{,}000 reasoning chains and 113{,}910 step-level labels, plus 6{,}879 questions for training. Our medical PRM baseline achieves an 87.1\% overall PRMScore -- substantially surpassing all baselines -- and serves as a plug-and-play verifier that improves downstream medical QA accuracy by 3.2--6.7 percentage points. Systematic evaluation spanning proprietary frontier models, open-source reasoning models, and medical-specialized models reveals critical weaknesses in current models' medical reasoning error detection capabilities, providing clear directions for future PRM improvement.

---


### 243. [HorizonBench: Long-Horizon Personalization with Evolving Preferences](https://arxiv.org/abs/2604.17283)

**<font color=#1a73e8>作者：</font>** Shuyue Stella Li, Bhargavi Paranjape, Kerem Oktar 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User preferences evolve across months of interaction, and tracking them requires inferring when a stated preference has been changed by a subsequent life event. We define this problem as long-horizon personalization and observe that progress on it is limited by data availability and measurement, with no existing resource providing both naturalistic long-horizon interactions and the ground-truth provenance needed to diagnose why models fail. We introduce a data generator that produces conversations from a structured mental state graph, yielding ground-truth provenance for every preference change across 6-month timelines, and from it construct HorizonBench, a benchmark of 4,245 items from 360 simulated users with 6-month conversation histories averaging ~4,300 turns and ~163K tokens. HorizonBench provides a testbed for long-context modeling, memory-augmented architectures, theory-of-mind reasoning, and user modeling. Across 25 frontier models, the best model reaches 52.8% and most score at or below the 20% chance baseline. When these models err on evolved preferences, over a third of the time they select the user's originally stated value without tracking the updated user state. This belief-update failure persists across context lengths and expression explicitness levels, identifying state-tracking capability as the primary bottleneck for long-horizon personalization.

---


### 244. [HalluClear: Diagnosing, Evaluating and Mitigating Hallucinations in GUI Agents](https://arxiv.org/abs/2604.17284)

**<font color=#1a73e8>作者：</font>** Chao Jin, Wenkui Yang, Hao Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While progress in GUI agents has been largely driven by industrial-scale training, ungrounded hallucinations often trigger cascading failures in real-world this http URL general VLM domains, the GUI agent field lacks a hallucination-focused suite for fine-grained diagnosis, reliable evaluation, and targeted this http URL bridge this gap, we introduce HalluClear, a comprehensive suite for hallucination mitigation in GUI agents as a complement to computation-intensive scaling. HalluClear comprises: (1) a GUI-specific hallucination taxonomy derived from empirical failure analysis; (2) a calibrated three-stage evaluation workflow which enhances VLM-as-a-judge reliability via expert-annotated benchmarking and ensemble credibility estimation; and (3) a mitigation scheme based on closed-loop structured reasoning, enabling lightweight continual post-training with cold-start initialization for both generalist and GUI-specialist agents. Experiments across representative agents and public benchmarks demonstrate that post-training on only 9K samples within our suite can significantly reduce hallucinations, thereby improving grounding and action fidelity, offering a compute-efficient pathway to robust GUI automation.

---


### 245. [Depth Adaptive Efficient Visual Autoregressive Modeling](https://arxiv.org/abs/2604.17286)

**<font color=#1a73e8>作者：</font>** Chunliang Li, Tianze Cao, Sanyuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive (VAR) modeling inefficiently applies a fixed computational depth to each position when generating high-resolution images. While existing methods accelerate inference by pruning tokens using frequency maps, their binary hard-pruning approach is fundamentally limited and fails to improve quality even with better frequency estimation. Observing that VAR models possess significant depth redundancy, we propose a paradigm shift from pruning entire tokens to adaptively allocating per-token computational depth. To this end, we introduce DepthVAR, a training-free framework that dynamically allocates computation. It integrates an adaptive depth scheduler, which assigns computational depth via a cyclic rotated schedule for balanced, non-static refinement, with a dynamic inference process that translates these depths into layer-major masks, selectively applies transformer blocks, and blends the resulting codes to ensure each token's influence is proportional to its processing depth. Extensive experiments show that DepthVAR achieves 2.3$\times$-3.1$\times$ acceleration with minimal quality loss, offering a competitive compute-performance trade-off compared to existing hard-pruning approaches. Code is available at this https URL

---


### 246. [Spectral Forensics of Diffusion Attention Graphs for Copy-Move Forgery Detection](https://arxiv.org/abs/2604.17287)

**<font color=#1a73e8>作者：</font>** H. M. Shadman Tabib, Tasriad Ahmed Tias, Nafis Tahmid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Copy-move forgery, where a region within an image is duplicated to hide or fabricate content, remains a persistent threat to visual media integrity. We introduce GraphSpecForge, a training-free framework that detects copy-move forgery by analysing the spectral structure of attention graphs from a pretrained Stable Diffusion U-Net. Our central insight is that copy-move manipulation induces approximate subgraph duplication in the self-attention graph, leading to measurable spectral redistribution in the normalized graph Laplacian. We formalise this link with perturbation-based arguments and build an image-level anomaly detector using Wasserstein distances between per-image Laplacian spectra and an authentic reference distribution. We evaluate GraphSpecForge on four copy-move benchmarks without forgery-specific retraining. On RecodAI-LUC (5,128 images), our best configuration achieves AUROC = 0.606 (95% CI: 0.580-0.638; permutation p = 0.005), and the normalized Laplacian outperforms raw attention spectra by +0.057 AUROC. On MICC-F220, CoMoFoD, and COVERAGE, the same pipeline attains AUROCs of 0.752, 0.774, and 0.673, respectively; on CoMoFoD it also reaches AUPRC = 0.833, balanced accuracy = 0.712, MCC = 0.499, and TPR@1%FPR = 32.5%. Additional ablation and falsification experiments confirm the signal's specificity and sensitivity to manipulation strength, while null-graph controls rule out trivial-statistic explanations.

---


### 247. [Probabilistic Programs of Thought](https://arxiv.org/abs/2604.17290)

**<font color=#1a73e8>作者：</font>** Poorva Garg, Renato Lui Geh, Daniel Israel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are widely used for code generation and mathematical reasoning tasks where they are required to generate structured output. They either need to reason about code, generate code for a given specification, or reason using programs of thought. The typical approach to code generation is to prompt the model and generate samples until an appropriate program is obtained. Within this process, sampling $n$ programs from the language model requires $n$ GPU compute-intensive generations which becomes prohibitively expensive for larger values of $n$. In this work, we address this limitation by exposing the LLM's distribution within the generated programs themselves. We propose a novel test-time framework we dub probabilistic programs of thought to obtain more samples from the model with fewer LLM generations. Given a program generated by a model and the associated next-token probabilities, we build a probabilistic program that compactly represents exponentially many deterministic programs. Since performing probabilistic reasoning in this probabilistic program is much cheaper, our approach allows sampling new programs without any additional GPU compute and little CPU overhead. We instantiate our approach on benchmarks for code generation, code understanding and mathematical reasoning and report improvements in performance with fewer generations from the LLM.

---


### 248. [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](https://arxiv.org/abs/2604.17297)

**<font color=#1a73e8>作者：</font>** Yangsong Lan, Hongliang Dai, Piji Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long Chain-of-Thought (CoT) reasoning is pivotal for the success of recent reasoning models but suffers from high computational overhead and latency. While prior works attempt to compress CoT via external compressor, they often fail to align with the model's internal reasoning dynamics, resulting in the loss of critical logical steps. This paper presents \textbf{C}ompressing \textbf{R}edundancy in Chain-of-Thought via \textbf{I}ntrinsic \textbf{S}aliency \textbf{P}runing (\textbf{CRISP}), a framework that compresses CoT by exploiting the model's intrinsic saliency. Our analysis reveals a distinct phenomenon: the reasoning termination token \texttt{[object Object]} acts as an information anchor, where its attention pattern effectively demarcates essential reasoning from redundancy. Based on this finding, we design a policy that utilizes these intrinsic attention signals to guide atomic compression operations. In contrast to coarse-grained pruning strategies, CRISP strategically distills the reasoning chain to maximize information density while preserving logical coherence. Empirical results across various backbone models and mathematical datasets demonstrate that CRISP achieves a 50-60% reduction in token count without compromising accuracy, effectively mitigating the efficiency bottleneck of long-context reasoning. We open-source our implementation to facilitate further research in efficient reasoning.

---


### 249. [Frequency-guided Multi-level Reasoning for Scene Graph Generation in Video](https://arxiv.org/abs/2604.17298)

**<font color=#1a73e8>作者：</font>** Chenxing Li, Yiping Duan, Xiaoming Tao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Scene Graph Generation aims to obtain structured semantic representations of objects and their relationships in videos for high-level understanding. However, existing methods still have limitations in handling long-tail distributions. This paper proposes the Frequency-guided Relational Multi-level Reasoning (FReMuRe) model, which enhances the modeling ability of long-tail relationships from a mechanism perspective. We introduce relation-specific branches to deal gradient conflicts, yielding more balanced and tail-aware learning. And we design a frequency-aware dual-branch predicate embedding network to model high-frequency and low-frequency relationships separately and improve the recall rate of tail classes through gated fusion. Meanwhile, we propose two types of interchangeable relation classification heads: Bayesian Head for uncertainty estimation and new Gaussian Mixture Model Head to enhance intra-class diversity. Experimental results show that FReMuRe significantly improves the recall rate of long-tail relationships and overall reasoning robustness on the Action Genome dataset.

---


### 250. [Efficient Test-Time Scaling via Temporal Reasoning Aggregation](https://arxiv.org/abs/2604.17304)

**<font color=#1a73e8>作者：</font>** Jiakun Li, Xingwei He, Kefan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves the reasoning performance of large language models but often results in token-inefficient overthinking, where models continue reasoning beyond what is necessary for a correct answer. Existing dynamic early-exit methods typically rely on single-step confidence signals, which are often unreliable for detecting reasoning convergence in multi-step settings. To mitigate this limitation, we propose TRACE, a training-free framework for efficient test-time scaling that determines when to terminate reasoning based on temporal aggregation of multi-step evidence rather than instantaneous signals. TRACE detects reasoning convergence over time by aggregating two complementary signals across recent reasoning steps: answer consistency, capturing the persistence of predicted answers, and confidence trajectory, modeling the temporal evolution of model confidence. Benefiting from these two factors, TRACE can accurately determine whether the reasoning process has converged, thereby promptly halting inference and effectively avoiding redundant reasoning steps. Extensive experiments on multiple challenging benchmarks show that TRACE reduces reasoning token usage by 25-30% on average while maintaining accuracy within 1-2% of full-length reasoning, consistently outperforming existing dynamic reasoning methods.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
