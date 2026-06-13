# 📦 其他研究 | 2026年06月14日

> 本类共 **251** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

---

### 51. [Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows](https://arxiv.org/abs/2606.12709)

**<font color=#1a73e8>作者：</font>** Timothy McAllister, Sina Abdidizaji, Ivan Garibay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM-based multi-agent systems (MAS) are deployed in the wild, the resilience of their collaboration structures against adversarial compromise becomes a critical safety concern. Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood. This paper investigates how model scale affects the security of linear multi-agent workflows. Our experiments across scales of two open-weight model families on the HumanEval benchmark reveal a compliance-correction symmetry: larger models are far more likely to faithfully execute malicious instructions, with the control-to-malicious performance drop reaching 53.7pp at 27B in uncorrected pipelines. However, appending a lightweight terminal Fixer stage collapses this to 0.6pp and restores statistical parity with control-level performance, demonstrating that strictly linear collaboration structures can be viable and resilient to adversaries at this scale, and suggesting that the brittleness previously attributed to linear topology may stem from a lack of correction.

---


### 52. [A Stabilized Path-Space Approach to Diffusion-Based Posterior Sampling](https://arxiv.org/abs/2606.12710)

**<font color=#1a73e8>作者：</font>** Evan Scope Crafts, Umberto Villa, Saviz Mowlavi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models provide expressive data-driven priors for Bayesian inverse problems, but many diffusion posterior samplers rely on heuristic guidance approximations that can fail for nonlinear operators and multimodal posteriors. In this work, we develop a stabilized path-space framework for diffusion-based posterior sampling. Starting from a base diffusion process whose terminal marginal represents the prior, we define a likelihood-weighted target measure on trajectories and cast posterior sampling as learning a controlled stochastic process whose path measure matches this target. This formulation connects diffusion posterior sampling to stochastic optimal control while preserving the Bayesian structure needed for uncertainty quantification. We introduce a time reparameterization that makes the path-space control problem well posed by removing the bias induced by the unknown initial value function, without auxiliary training. We then learn the control via a trust-region path-space optimization method with log-variance objectives. The path-space perspective also unifies our learned control approach with existing guidance-based samplers, quantifies the sampling error induced by approximate controls, and yields importance sampling corrections for asymptotically exact posterior expectations. We evaluate the proposed framework on a suite of benchmark inverse problems with analytically characterized or high-quality reference posteriors, enabling principled assessment of sampling accuracy and uncertainty quantification. These experiments provide insight into the behavior of diffusion-based posterior samplers and demonstrate improved accuracy and robustness over leading approaches.

---


### 53. [Definitional alignment before capability alignment: a Design-Science framework for adjudicating claims about AGI](https://arxiv.org/abs/2606.12713)

**<font color=#1a73e8>作者：</font>** J. E. Aguilera Briones  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claims that artificial general intelligence has already arrived and claims that it remains decades away are often defended from overlapping evidence. "AGI" lacks a single shared and stable referent and competing operationalizations can return different verdicts on the same system. This article treats that under-specification as a design and governance problem. Following Design Science Research Methodology, it develops DAF-AGI, a second-order conceptual artifact with two coupled components: five ordinal criteria for assessing the adjudicative fitness of candidate definitions and a structured governance audit of authorship, interest, certification, external verification and revision authority. The artifact is demonstrated on five prominent measurement families and one deflationary boundary position in a documented corpus and then stress-tested against a stylized strong arrival claim: that current generative systems constitute AGI because they outperform a well-educated adult on many cognitive tasks. On evidence from the cited 2024-2025 sources, the claim was certifiable only under a performance-based operationalization; capability-ontology, psychometric and skill-acquisition approaches did not certify it, the economic family remains indeterminate and the deflationary position refuses binary adjudication. The contribution is a novel integration and operationalization, not an empirical validation: independent application, inter-rater testing and author-external cases remain necessary. The paper further proposes definitional sovereignty as an enabling component of algorithmic sovereignty: the institutional capacity to contest, certify and revise imported technological categories under public accountability.

---


### 54. [Out-of-Distribution (OOD) Detectors for Open-Set RF Fingerprinting](https://arxiv.org/abs/2606.12718)

**<font color=#1a73e8>作者：</font>** Sudeepta Mondal, Ganesh Sundaramoorthi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio-frequency (RF) fingerprinting systems must operate in open-world environments where signals from unknown transmitters and temporal drift introduce distribution shift at test time. Out-of-distribution (OOD) detection provides a natural framework for this problem, yet its application to RF fingerprinting (RFF) remains limited. A key barrier to their adoption is that most OOD detectors require auxiliary OOD data for parameter tuning, an assumption that is difficult to satisfy in RF environments where representative OOD data is impractical to collect. In this work, we introduce a promising set of OOD detection methods from the machine learning literature to open-set RFF domain. We present these methods within a unified mathematical framework based on information theory, which is a natural framework for communication systems. Our framework allows for the systematic analysis of methods and development of new methods. We further demonstrate the applicability of recent work on tuning OOD detectors without given OOD tuning data for open-set RFF. We evaluate on the POWDER RF fingerprinting dataset, showing that detectors tuned without any given OOD data achieve performance comparable to baselines with access to true OOD tuning data and greatly out-perform baseline approaches without access to true OOD tuning data, showcasing the practical viability for the RFF problem.

---


### 55. [A Multiplexing Design Space: Theory, Method, and Application](https://arxiv.org/abs/2606.12719)

**<font color=#1a73e8>作者：</font>** Yiwen Xing, Afrah Farea, Saiful Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many visualization designs feature phenomena referred to as ``visual multiplexing'', where multiple pieces of information associated with the same data point are conveyed simultaneously. Although visualization designers are able to bring such phenomena, often unconsciously, into their designs, the design space of visual multiplexing is huge, and it is uncommon to explore visual multiplexing systematically as design patterns. In this paper, we propose a design method for exploring a smaller design space constrained by an application. As an illustrative case study, we focus on machine learning (ML) workflows for developing ML models that approximate partial differential equations (PDEs). In these workflows, ML researchers need to analyze the inter-relationships among multiple 2D scalar fields frequently. Since superimposing one heatmap on top of another is not an effective design, we formulate three design steps to explore the design space of visual multiplexing in the context of multiple 2D scalar fields. Our design method also includes a pre-design step for domain grounding and theoretical analysis, and involves domain experts in both co-design and evaluation activities. The design process enables us to identify relatively optimal default multiplexing designs as well as the need for small variations that domain experts can control through a user interface.

---


### 56. [The Theory of Mind Utility: Formal Specification of a Mentalizing Mechanism](https://arxiv.org/abs/2606.12721)

**<font color=#1a73e8>作者：</font>** Nikolos Gurney, Stacy Marsella  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inferring others' beliefs requires more than reading surface signals; it requires tracking who told them what, in what order, and how credibly. The Theory of Mind Utility (ToM-U) formalizes this epistemic state inference problem at the computational level of analysis, specifying what mentalizing computes and why without commitment to algorithmic or neural implementation. ToM-U achieves this by constructing Local Epistemic World Models (LEWMs) -- directed typed graphs that represent agents, state nodes, and the epistemic relationships among them -- and evaluating discrete candidate LEWMs against observed behavior until one achieves sufficient confidence. Five formal definitions specify the LEWM structure, agent node properties including ordered information access history, a bounded proliferation mechanism for recursive mentalizing, three inference procedures, and a residue function that captures the structured trace left by failed mentalizing attempts. ToM-U differs from Bayesian Theory of Mind and adjacent formal accounts, which presuppose rather than derive belief states, and from simulation theory and theory-theory, which lack a formal apparatus for epistemic state inference. The architecture generates directional, falsifiable predictions about mentalizing failure that follow from structural properties of the model rather than auxiliary assumptions, and positions ToM-U as a domain-agnostic mechanism upstream of goal inference and other downstream social cognitive processes.

---


### 57. [Let's Ask Gauss: Improved One-Run Privacy Auditing](https://arxiv.org/abs/2606.12733)

**<font color=#1a73e8>作者：</font>** Adya Agrawal, Yu Wei, Jaspal Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy auditing provides an important safeguard by estimating the actual information leaked by a model, thus ensuring that theoretical privacy guarantees hold in practice. We study empirical privacy auditing for differentially private (DP) machine learning, focusing on efficient one-run methods for mechanisms such as DP-SGD. Prior one-run approaches threshold training examples or "canaries" into binary membership guesses, which discards useful information. We show that, in the white-box DP-SGD setting, canary-aligned signals naturally form a sequence of random variables whose normalized sum is asymptotically Gaussian. Leveraging this distributional perspective, we develop a DP-auditing framework that leads to tighter privacy lower bounds from a single training run.

---


### 58. [Physics-Informed Neural Networks and Radial Basis Functions for PDEs with Dirac Delta Sources](https://arxiv.org/abs/2606.12735)

**<font color=#1a73e8>作者：</font>** Manuel Reyna, Alexandre Tartakovsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) are a machine learning method for solving forward and inverse Partial Differential Equations (PDEs). When applied to PDEs with Dirac delta functions in the forcing terms, boundary conditions, or initial conditions, PINNs require approximating them with smooth surrogate functions, a practice that can introduce significant modeling errors. In this work, we exploit the interpretation of PINNs as Residual Least Squares (RLS) methods and show that this perspective enables direct treatment of Dirac delta terms by integrating the weak-form equation. Among RLS formulations other than PINN, we focus on the Radial Basis Function (RBF) expansion (also known as a single-layer RBF Network). We show that while integrating out the Dirac delta in PINNs causes residuals to fail to converge to zero, RBF-RLS consistently provides good forward and inverse solutions to transport problems. We explain this finding using the Neural Tangent Kernel (NTK) theory. We test both approaches on linear PDEs that represent groundwater flow and transport in porous media and rivers. We solve inverse problems to fit synthetic data, noisy synthetic data, and real-world measurements.

---


### 59. [Benchmarking AI Agents for Addressing Scientific Challenges Across Scales](https://arxiv.org/abs/2606.12736)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Allen Xin Wang, Antonia Panescu 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly being developed to accelerate scientific discovery, yet their practical capabilities in real research settings remain poorly understood. Existing benchmarks for AI agents rarely capture the complexity, heterogeneity, and extended reasoning required by scientific work, whereas benchmarks for scientific tasks often reduce research to static, direct problems and provide limited support for interactive evaluation. Here, we introduce SciAgentArena, a systematic benchmark for evaluating AI agents in real-world scientific research scenarios drawn from emerging needs across multiple domains. SciAgentArena comprises approximately 200 tasks with stepwise verification and an interactive, agent-agnostic environment for assessing diverse AI agents. Using this benchmark, we find that current agents can contribute effectively to well-specified data-analysis workflows, particularly when the task structure and evaluation criteria are clear. However, their performance remains uneven across scientific contexts: agents struggle to generate genuinely novel insights, sustain self-directed exploration, and formulate robust solutions for open-ended research questions. We further characterize common failure modes across agents and identify opportunities for improving their reliability, autonomy, and scientific reasoning. Together, SciAgentArena provides a practical framework for measuring progress in AI agents for science and for guiding the design of future agents capable of addressing complex scientific challenges. Full codes, tasks, and datasets can be accessed via this link: this https URL.

---


### 60. [Deep Unfolded Latent Optimally Partitioned-l2/l1 Networks for Data-driven Block-Sparse Recovery](https://arxiv.org/abs/2606.12740)

**<font color=#1a73e8>作者：</font>** Takanobu Furuhashi, Hidekata Hontani, Qibin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The convex Latent Optimal Partition (LOP)-l2/l1 approach enables block-sparse signal recovery with unknown partitions but relies on manual hyperparameter tuning. Additionally, numerical instability in differentiating its proximal operator prevents its automatic parameter tuning via Deep Unfolding (DU). To address these limitations, we propose two architectures: a stable framework utilizing implicit differentiation and a flexible variant leveraging Deep Weight Factorization (DWF). The DWF-based approach also supports nonconvex smooth data fidelity terms. Numerical experiments demonstrate that DU-LOP-l2/l1 yields competitive performance and high resilience against impulsive noise.

---


### 61. [Reducing the Complexity of Deep Learning Models for EEG Analysis on Wearable Devices](https://arxiv.org/abs/2606.12742)

**<font color=#1a73e8>作者：</font>** Farough Shayeste Roodi, Parham Zilouchian Moghaddam, Mahdi Mohammadi-nasab 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wearable healthcare devices are the fastest-growing Internet of Things (IoT) sector. Many automated healthcare services rely on two crucial biological signals, namely ECG and EEG, which reflect the activity of the heart and brain, respectively. Although deep neural networks are considered the primary way to process and analyze these signals, the very tight energy and computational power constraints in wearable devices are far below the computational, energy, and memory bandwidth demands of DNN models, thereby impeding the deployment of deep learning in many practical wearable services. This paper investigates the feasibility of deploying state-of-the-art DNN models in resource-constrained wearable devices. Notably, we explore the trade-off between accuracy and computational complexity of DNNs when parameter quantization and electrode reduction methods are used. Our investigation centers on several state-of-the-art DNN models designed for EEG signal analysis, specifically for detecting epileptic seizures. Our findings demonstrate that, when applied judiciously, these techniques can significantly reduce the complexity of the DNNs under consideration with minimal adverse effects on accuracy. These results reveal the explicit trade-offs between accuracy and complexity reduction encountered when adapting DNN-based online EEG analysis for wearable devices.

---


### 62. [Agent-based models for the evolution of morphological alternation patterns](https://arxiv.org/abs/2606.12748)

**<font color=#1a73e8>作者：</font>** Aravinth Kulanthaivelu, Richard Sproat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Why is the past of English "go" the apparently unrelated "went"? Such alternations are frequent in languages. They neither aid communication nor learnability, yet they can be persistent, surviving over centuries or millennia.
We present a multi-agent simulation of the emergence of morphological stem and inflection alternations. Alternate forms arise by phonological changes or, as with "go/went", from lexical alternatives associated with a subset of the population. When an agent 'hears' another agent use a novel form for a slot in the paradigm of a word (say, the past tense of go), they will with some probability adopt that form, possibly spreading its use to other slots in the paradigm that shared the same original form. Thus alternative forms can spread through the population and become entrenched as stem or inflectional marker alternants. Unlike many previous computational studies, our system allows for naturalistic lexical forms, realistic phonological rules, lexicons with hundreds or thousands of entries, and agent populations in the tens or hundreds. It supports several network topologies, diffusion patterns and agent adoption policies.
One issue with such simulations is evaluation: how realistic is the resulting morphology compared to those of real languages? We introduce the AI Historical Linguist, a novel Large Language Model-driven system that models a debate between two historical linguists. We use this to compare a set of real language morphologies, disguised morphologies, and experimentally evolved morphologies. The results suggest that among the factors that favor more plausible morphologies are scale-free social networks and random Bernoulli adoption of forms.
We also present three case studies modeling attested historical changes, allowing us to test what might have happened if history had been different.
All code and data are released.

---


### 63. [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/abs/2606.12765)

**<font color=#1a73e8>作者：</font>** Ramchand Kumaresan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Apple's Metal 4.1 exposes a tensor compute path: the Metal Performance Primitives (MPP) matmul2d operation over cooperative_tensor fragments, whose interface is documented but whose hardware behavior is deliberately hidden. The specification states which data-type rows are supported, never whether they are hardware-accelerated, where the operation physically executes, what its accumulator width is, or how it partitions matrix fragments across threads. We present Rigel, an empirical characterization of this path on a single Apple M4 Max (a pre-neural-accelerator generation). Using a checksum-gated, provenance-tracked microbenchmark harness, Rigel recovers eleven facts the v4.1 specification hides or contradicts. The headline finding: the Metal 4.1 fp8 (E4M3) matmul2d is emulated, not accelerated: it sustains 0.94x the throughput of fp16 despite reading half the operand bytes, so on M4 it is a memory-footprint feature, not a performance feature. We further show, via a three-signal triangulation (throughput ceiling, comparison against simdgroup_matrix, and per-rail power attribution), that matmul2d executes entirely on the GPU shader cores with no dedicated matrix datapath and no evidence of Apple Neural Engine routing; that it accumulates in >=fp32; and we reconstruct the opaque 8x8 cooperative_tensor fragment layout Apple documents nowhere. Acting on the characterization, a hand-fused GEMM + bias + GELU kernel beats the decomposed path by +6.5-12.9% in the cache-resident regime. All findings are reproducible from committed MIT-licensed code and per-cell CSVs.

---


### 64. [GENIE: A Fine-Grained Measure for Novelty](https://arxiv.org/abs/2606.12790)

**<font color=#1a73e8>作者：</font>** Ramya Namuduri, Manya Wadhwa, Anshun Asher Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models have consistently demonstrated a lack of creativity and diversity across tasks. Prior work has focused on addressing whether models are capable of generating creative outputs. Here, we aim to consider novelty and investigate what makes model-generated content novel or not novel in a task-specific manner. We propose a fine-grained evaluation metric GENIE to measure the novelty of responses along task-specific features with respect to a population of responses. We show that unlike GENIE, holistic metrics struggle to capture the high-dimensionality of novelty and do not provide insight on which properties they target. Finally, we use GENIE to measure the effectiveness of mitigation methods that address creativity to better understand where these methods can improve novelty.

---


### 65. [Semantic Identification of IoT Devices from Behavioral Primitives](https://arxiv.org/abs/2606.12793)

**<font color=#1a73e8>作者：</font>** Samuel Witt, Hassan Habibi Gharakheili  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurate identification of IoT devices is important for security management and policy enforcement. Existing approaches typically learn device signatures from packets or flow records. These methods operate on low-level communication observations whose traffic patterns may vary across deployments, software versions, and user interactions. This paper studies device identification using Manufacturer Usage Description (MUD) profiles. MUD profiles describe device behavior using Access Control Entries (ACEs), where each ACE represents a behavioral primitive consisting of protocol, endpoint, direction, and port semantics derived from device communication policy. Our contributions are threefold. First, using 28 publicly available MUD profiles containing 1,023 ACE instances, we construct ACE-level semantic representations from compact behavioral text and analyze their geometric properties. ACE-level representations preserve device-level behavioral distinctions more effectively than whole-profile embeddings and remain effective after whitening calibration. Second, we evaluate semantic ACE matching under controlled runtime variations, including unseen ACEs, drifted hostnames, and partial runtime observation. Exact ACE matching performs well when the overlap with the canonical MUD profile remains high, but degrades sharply when the overlap becomes sparse or disappears. In contrast, semantic ACE matching preserves useful identification evidence across these conditions. Third, we evaluate the same approach on real IoT traffic traces comprising more than 800,000 observed flows. Exact overlap remains the strongest signal when stable overlap exists, while semantic ACE matching provides stronger identification evidence during the early stages of observation, frequently retains the correct device among the highest-ranked candidates, and remains effective under sparse-overlap runtime traffic.

---


### 66. [Exploring How Agent Voice Accents Shape Human-AI Collaboration in K-12 Group Learning](https://arxiv.org/abs/2606.12805)

**<font color=#1a73e8>作者：</font>** Prerna Ravi, Carúmey Stevens, Ben Hurt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaboration is widely recognized as a cornerstone of 21st-century education, yet teachers still encounter persistent challenges in fostering productive peer interaction. LLM conversational peer agents introduce new possibilities for mediating in-person group work, raising questions about how persona design, particularly their voice characteristics, shapes learners' perceptions, trust, and interactional dynamics. While prior work has examined agent accent effects in one-to-one settings, little is known about how these effects manifest in groups. We conducted a between-subjects mixed-methods study with 33 teachers examining how a GenAI voice agent with different accents (British, Indian, and African American) influenced collaboration and agent perception. Across surveys, group interaction analyses, and artifacts, we find that accent shaped participants' mental models and the roles the agent assumed in group interaction. The British-accented agent was largely treated as a tool and engaged in detached, utility-based ways, whereas Indian- and African American-accented agents were more readily anthropomorphized and integrated as peers. These role expectations influenced trust, engagement, and reliance over time. This work advances understanding of how GenAI's sociolinguistic design features shape group dynamics in CSCL, with implications for designing culturally inclusive AI partners in group learning.

---


### 67. [Detect, Remask, Repair: Diffusion Editing for Faithful Summarization of Evolving Contexts](https://arxiv.org/abs/2606.12807)

**<font color=#1a73e8>作者：</font>** Hao Zou, Zachary Horvitz, Chandhru Karthick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Summaries of real-world events can become outdated as contexts evolve and new information arrives. A common response is to generate a new summary from the updated context, but full regeneration discards the previous draft, can obscure what changed, and may be unnecessary when only a few claims are unsupported. We study localized faithfulness repair: updating outdated spans in an existing summary while preserving supported content. We propose DETECT-REMASK-REPAIR, a diffusion-based framework that identifies, remasks, and repairs outdated regions with masked diffusion language models. To evaluate evolving-context summarization, we introduce StreamSum, a benchmark of synthetic event timelines. Experiments on DialogSum and StreamSum show that localized diffusion repair provides a controllable alternative to full rewriting: faithfulness-steered repair improves early drafts, one-step repair reduces repair cost to under half a second, with the framework enabling faithfulness-speed-preservation tradeoffs across datasets. We also find that the framework can provide a post-hoc correction step that improves faithfulness for autoregressive systems.

---


### 68. [SymQNet: Amortized Acquisition for Low-Latency Adaptive Hamiltonian Learning](https://arxiv.org/abs/2606.12808)

**<font color=#1a73e8>作者：</font>** Yash Vardhan Tomar, Dheeraj Peddireddy, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive Hamiltonian learning is central to calibrating and characterizing quantum devices. In an adaptive controller, choosing the next experiment is itself a computation. Bayesian design rules are recomputed after every posterior update, and that step can take seconds. Across hundreds of shots, those seconds become a significant wall-clock cost for adaptivity. We introduce SymQNet, an amortized reinforcement-learning approach for low-latency adaptive Hamiltonian learning. SymQNet learns a posterior-conditioned acquisition policy offline, then uses a fast policy forward pass online while retaining Bayesian posterior feedback. On transverse-field Ising benchmarks, SymQNet substantially reduces acquisition latency relative to bounded Fisher-information search and bounded two-step Bayesian active learning by disagreement (BALD). At five qubits, it reduces acquisition-only decision latency by $47.1\times$ and $72.6\times$ relative to these online baselines; at twelve qubits, full simulated steps take $1.02$ s for SymQNet versus $13.27$ s for bounded two-step BALD. Overall, we show that learned acquisition can make adaptive Hamiltonian learning practical for repeated low-latency workloads.

---


### 69. [Teach-and-Repeat: Accurately Extracting Operational Knowledge from Mobile Screen Demonstrations to Empower GUI Agents](https://arxiv.org/abs/2606.12817)

**<font color=#1a73e8>作者：</font>** Yudong Zhang, Lei Hu, Daoyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding the digital world on mobile devices is shifting from static UI perception to dynamic action comprehension. This capability enables models to convert visual state transitions into operational knowledge, defined as short natural-language sentences that describe action types, target UI elements, textual arguments, and execution orders. However, due to the highly diverse and heterogeneous UI designs across applications, existing vision-language models (VLMs) struggle to accurately infer these underlying operations. To bridge this gap, we introduce Teach VLM, a core model designed to translate mobile screen trajectories into step-wise operational knowledge by extracting and analyzing operation-related keyframes from demonstration videos. To address the scarcity of aligned training data, we develop a systematic data flywheel for scalable data acquisition. We further introduce a novel Chinese Mobile Screen Teach Benchmark for fine-grained evaluation. Building upon Teach VLM, we propose the Teach-and-Repeat paradigm, where the generated operational knowledge serves as an interpretable procedural reference to guide downstream screen-based execution agents. Extensive evaluations demonstrate that Teach VLM significantly outperforms strong VLM baselines, achieving state-of-the-art performance in operation semantics prediction. Furthermore, experiments in Android World show that our paradigm yields consistent Task Success Rate improvements for downstream agents. Together, Teach VLM and the Teach-and-Repeat paradigm offer a practical pathway from raw demonstrations to reusable task automation.

---


### 70. [DIMOS: Disentangling Instance-level Moving Object Segmentation](https://arxiv.org/abs/2606.12826)

**<font color=#1a73e8>作者：</font>** Hongxiang Huang, Hongwei Ren, Xiaopeng Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving instance segmentation (MIS) attracts increasing attention due to its broad applications in traffic surveillance, autonomous driving, and animal tracking. Event cameras record asynchronous brightness changes, providing high temporal resolution and dynamic range, which makes them highly sensitive to motion information. By fusing event and image features, motion cues from events can complement spatial details from images, enhancing the performance of MIS. However, current multimodal MIS methods still struggle to segment small moving instances, as event cameras often yield sparse features under limited resolution. Moreover, event features entangle appearance attributes with motion cues, which further restricts effective cross-modal fusion. To address these challenges, we first propose a dual-disentangling feature extraction framework that separates and extracts appearance and motion information within both image and event modalities, thereby improving feature density. Subsequently, a multi-granularity cross-modal alignment is introduced to align distributionally and semantically consistent features across modalities, enabling more effective fusion with rich spatial and temporal details. The experiment results demonstrate that our method achieves state-of-the-art performance in multimodal MIS, especially for small instances under challenging conditions such as fast motion and low-light settings.

---


### 71. [Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement](https://arxiv.org/abs/2606.12834)

**<font color=#1a73e8>作者：</font>** Woong Shin, Craig A. Bridges, Marshall T. McDonnell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As scientific workflows shift from deterministic executables to LLM-based agents, the development practices on offer, such as fine-tuning, reinforcement learning, and prompt-and-go, bury the scientist's judgment. We propose treating agent construction as a workflow stage and introduce AgentBuild, which builds a scientific agent from a contract the scientist authors. The contract is a version-controlled rubric, a difficulty-graded curriculum, and a curated external knowledge base. A rubric-driven judge gates a meta-optimizer coding agent that edits the agent within a declared boundary, so the build compiles the agent, not the scientist's judgment. We instantiate this for Rietveld refinement of X-ray diffraction data through GSAS-II behind MCP and A2A, where a blank-harness construction run progresses through a lithium lanthanum zirconium oxide (LLZO) signal-to-noise ladder, reaches the 4 hour scan as a frontier case, and exposes the workflow-scope limits that remain. The same rubric that rewards credible fits also scores trajectory scope, making the frontier a contract failure rather than a pattern-fitting failure. As base models evolve, re-running AgentBuild is a re-tune, not a rebuild, and the scientist's authored contract remains the durable asset.

---


### 72. [LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling](https://arxiv.org/abs/2606.12837)

**<font color=#1a73e8>作者：</font>** Jiarui Zhao, Rongzhi Zhang, Lingchuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agent benchmarks exemplified by BrowseComp have rapidly saturated over the past year, with the strongest models surpassing 90% accuracy. Since these benchmarks are predominantly human-authored, annotators lack a global perspective on entity statistics and cannot systematically maximize search space size and structural complexity. This creates a difficulty ceiling that is hard to break. To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains. LoHoSearch is constructed via an automated pipeline built upon a knowledge graph covering over 7 million Wikipedia entities, which selects relations with large search spaces and assembles them into structurally complex questions with KG-verified unique answers. Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks. LoHoSearch provides a more demanding standard for evaluating long-horizon reasoning and context management in search agents.

---


### 73. [CLARITree: Cholesky and Lookahead Accelerations for Regression with Interpretable Piecewise Linear Trees](https://arxiv.org/abs/2606.12840)

**<font color=#1a73e8>作者：</font>** Yixiao Wang, Hayden McTavish, Varun Babbar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regression trees are among the most interpretable yet expressive model classes in machine learning. Historically, greedy induction has been the dominant approach for constructing well-performing regression trees. While optimal methods based on dynamic programming and branch-and-bound exist, they are computationally prohibitive for general linear regression trees, despite often achieving substantially better performance than greedy approaches. Recent work has shown that specialized lookahead strategies can dramatically improve runtime while maintaining near-optimal performance, primarily in classification settings. In this work, we develop a novel algorithm for near-optimal, sparse, piecewise linear regression trees that combines a lookahead-style search strategy with efficient rank-one Cholesky updates of the Gram matrix. We demonstrate, both theoretically and empirically, that our method achieves a favorable trade-off between computational efficiency, predictive accuracy, and sparsity, and scales significantly better than the current state of the art.

---


### 74. [Interpretable Factor Decomposition for Decision Intelligence in Large-Scale Financial Markets: Evidence from China's A-Share Market](https://arxiv.org/abs/2606.12843)

**<font color=#1a73e8>作者：</font>** Xiao Han, Yao Xiao, Zhen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an interpretable machine learning pipeline to decompose Cross-Sectional Equity Return Predictability into auditable factor contribution. We apply an XGBoost model with TreeSHAP attribution and conduct stress testing on 3632 Chinese A-share stocks from 2009 until 2019. Using 60-month, rolling windows over 55 months of out-of-sample data, XGBoost obtains a mean AUC of 0.547 and +2.38%/month (Newey-West t = 5.94; Annualized Sharpe 2.23) long-short spread for the top vs bottom quintiles. This alpha is persistent after adjusting for the Carhart four-factor model (+2.31%/month; t = 7.48). SHAP Decomposition indicates that behavioral signals (turnover and momentum) account for 58.2% of predictive attribution compared to 10.7% for valuation ratios, on average, across 55 industry groups. Ablation analysis serves to cross-validate this ranking and provides evidence that SHAP and ablation diverge in a manner that highlights feature substitutability structure that is largely invisible to either method used in isolation.

---


### 75. [A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction](https://arxiv.org/abs/2606.12845)

**<font color=#1a73e8>作者：</font>** John Fields, K M Sajjadul Islam, Ruchitha Thota 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study explores privacy-preserving machine learning (PPML) techniques using the PySyft platform to enable collaborative prediction of student retention between institutions. We developed a remote data science (RDS) framework with a semi-air-gapped architecture consisting of high-side and low-side servers, allowing researchers from three universities to build predictive models on sensitive student data without direct data access. Using historical data from a small private university (N=720), we evaluated three synthetic data generation approaches and validated the framework through inter-institutional collaboration. The results demonstrate consistent classification performance across institutions (Macro F1: 0.690--0.695) while maintaining strict Family Educational Rights and Privacy Act (FERPA) compliance. We also propose Data-Type-Aware Templates, a novel synthetic data method that prioritizes privacy over distributional fidelity. Our findings confirm that RDS-based PPML is technically feasible for educational settings and offers a practical alternative to federated learning for small-scale inter-institutional collaborations. The code is available at this https URL.

---


### 76. [Language-Guided Abstraction for Visual Reasoning](https://arxiv.org/abs/2606.12847)

**<font color=#1a73e8>作者：</font>** Xu-Jing Ye, Yuan-Gen Wang, Ruping Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Abstraction and Reasoning Corpus (ARC) is viewed as a critical avenue to Artificial General Intelligence (AGI), as it enables models to learn abstract transformation rules from few-shot examples and then generalize to new tasks. However, prevalent ARC methodology is either pure language or vision-only (i.e., VARC). The former depends heavily on LLMs, consuming billions of parameters. The latter often struggles to capture high-level semantics, leading to overfitting on pixel-level patterns. To bridge this gap, we propose L-VARC, a novel framework that enhances visual reasoning via a language-guided Learning Using Privileged Information (LUPI) branch. Specifically, we design a Semantic Compression Module by feeding a unified, task-agnostic prompt into DeepSeek-V3. In this way, the raw LARC (a crowd-sourced language description dataset) can be substantially refined and structured, fitting with the context length constraint of standard text encoders (e.g., CLIP). Moreover, we design a Cross-Attention Projector to align visual features with semantic embeddings, aiming to guide the training of the ARC model. Notably, the LUPI branch is taken in the training process and will be discarded during inference, thereby yielding a lightweight model with a mere 18 million parameters. Extensive experiments demonstrate that our L-VARC effectively leverages linguistic priors to boost visual reasoning and outperforms state-of-the-art. Ablation studies further confirm the contribution of the two new designs towards the L-VARC framework. The code is available at this https URL.

---


### 77. [(Human) Attention Is (Still) All You Need: Human oversight makes AI-assisted social science reliable](https://arxiv.org/abs/2606.12848)

**<font color=#1a73e8>作者：</font>** Chen Zhu, Xiaolu Wang, Weilong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for tasks once reserved for trained researchers, including hypothesis generation, specification choice, and drafting conclusions. We argue that the reliability of AI-assisted research depends not only on model capability, but also on how cognitive labour is structured between humans and machines. We study this problem through Human-in-the-Loop Economic Research (HLER), a decision architecture based on pre-commitment, decision sequencing, accountability, and attention allocation. In a pre-specified 2*4 factorial experiment with 280 complete research runs across four datasets, an unconstrained multi-agent baseline produced critical failures in 72% of runs. Using the same underlying model, the same agent decomposition, and identical prompts for the shared reasoning agents, HLER reduced the failure rate to 16% by imposing three architectural commitments: LLMs reason but do not execute data work, data and estimation are handled deterministically, and three human decision gates bind the workflow. Fisher's exact test rejects equality of failure rates at p<0.001. Reliability gains were largest on the least publicly represented dataset, a Qing-dynasty population register, consistent with a task-based production model with Frechet-distributed output quality. An 80-run ablation suggests that deterministic computation and human gates contribute independently, with exploratory evidence of complementarity. We interpret HLER as a research harness rather than an autonomous AI scientist: it sharply reduces failures, makes residual weaknesses more visible, and prevents unreliable claims from being advanced as publication-ready outputs.

---


### 78. [WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning](https://arxiv.org/abs/2606.12852)

**<font color=#1a73e8>作者：</font>** Renmin Cheng, Changhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches. Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures. We argue that a key limitation is not only the lack of episodic memory, but also the decoupling of \textit{what-where-when} memory from \textit{which-why} reasoning. To address this, we propose \textbf{WISE} (Which-Why Informed Semantic Explorer), a long-horizon agent framework with an enhanced low-level controller equipped with a Causal Event Graph that augments episodic memory with explicit causal structure linking observations to task relevance. Unlike prior work such as MrSteve, which relies on feature similarity for retrieval, WISE enables robust recall under viewpoint changes and supports opportunistic task reordering through causal reasoning. Building on this memory, we propose an Opportunistic Task Scheduler that dynamically re-prioritizes subtasks when causally relevant opportunities are detected. We further equip WISE with a multi-scale progressive exploration strategy to provide spatially comprehensive observations for downstream reasoning. Experiments show that WISE largely improves task success and efficiency on long-horizon sparse tasks, particularly in settings requiring adaptive decision-making.

---


### 79. [Learning Task-Aware Sampling with Shared Saliency through Density-Equalizing Mappings](https://arxiv.org/abs/2606.12869)

**<font color=#1a73e8>作者：</font>** Tsz Lok Ip, Han Zhang, Lok Ming Lui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In image and surface-based learning tasks, convolutional features are typically extracted using receptive fields that are sampled uniformly across the entire domain. However, informative structures are rarely distributed uniformly in practice and are often concentrated in localized regions. Such phenomena are particularly common in medical imaging, where pathological changes are spatially confined. Consequently, uniform convolution allocates equal computational effort to both informative and uninformative regions, resulting in inefficient feature extraction and suboptimal utilization of model capacity. To address this issue, we propose a framework for task-adaptive sampling that dynamically redistributes computational attention according to the spatial importance of the data. Specifically, we introduce the Density-Equalizing Convolutional Neural Network (DECNN), which employs density-equalizing mappings to guide convolution through a learned density function. The density function encodes the relative importance of different regions and induces a transformation that enlarges informative areas while compressing less relevant ones. As a result, convolutional receptive fields are redistributed non-uniformly over the domain, enabling denser sampling in task-relevant regions. By coupling this importance-driven transformation with convolution, DECNN performs adaptive feature extraction that focuses computational resources on informative structures. This leads to more efficient use of model capacity, yielding a lightweight yet expressive architecture while simultaneously producing an interpretable saliency map. Experiments on image classification and craniofacial surface analysis demonstrate that DECNN achieves competitive or superior performance with fewer parameters, accurately identifies task-relevant regions, and remains robust under complex geometric variations.

---


### 80. [The Hidden Power of Scaling Factor in LoRA Optimization](https://arxiv.org/abs/2606.12883)

**<font color=#1a73e8>作者：</font>** Zicheng Zhang, Haoran Li, Jiaxing Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Low-Rank Adaptation (LoRA), the scaling factor $\alpha$ is often treated as a mere complement to the learning rate, yet its role in optimization remains poorly understood. In this paper, we reveal that the scaling factor $\alpha$ and the learning rate function differently, with $\alpha$ emerging as the dominant driver of effective optimization, delivering gains that cannot be replicated by learning rate scaling alone. Through the synergy of extensive empirical analysis and a theoretical Signal-Drift framework, we uncover three findings into LoRA's scaling mechanism: First, LoRA's spectral suppression smooths the optimization landscape, rendering standard hyperparameters overly conservative and creating an optimization gap. Second, when leveraging this smoothness to accelerate convergence, $\alpha$ outperforms the learning rate by amplifying the task signal without increasing the drift ratio. Third, the optimal scaling factor follows a sublinear relationship with the rank, well characterized by a square-root law with an unexpectedly large coefficient, revealing the insufficient scaling of existing rank-tied heuristics. Based on these insights, we propose LoRA-$\alpha$, a minimalist framework that restores $\alpha$ to its principled regime, making LoRA compatible with standard small learning rates. Extensive evaluations across diverse tasks demonstrate that LoRA-$\alpha$ consistently improves performance while streamlining hyperparameter search, unleashing the learning potential of LoRA.

---


### 81. [Bridging Modal Isolation in Interleaved Thinking: Supervising Modality Transitions via Stepwise Reinforcement](https://arxiv.org/abs/2606.12886)

**<font color=#1a73e8>作者：</font>** Tingyu Li, Le Zhou, Siyuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interleaved thinking, where a unified multimodal model alternates between textual reasoning and visual generation, has shown promise on spatial and physical tasks. However, in complex long-chain scenarios, we identify a fundamental failure mode: generated images diverge from the textual context while subsequent text ignores the visual evidence, causing the two modalities to alternate without genuinely informing each other. We term this Modal Isolation and attribute it to compounding information loss at modality boundaries. We decompose each reasoning cycle into atomic operations and define modality transition loss, quantifying cross-modal hallucination (text-to-image) and visual utilization deficit (image-to-text) at each boundary. We propose MoTiF (Modality Tiransition Fidelity), a two-stage training framework that directly optimizes these transitions: Reflective SFT trains the model to detect and recover from erroneous visual outputs; Flow-GRPO improves image generation fidelity via reinforcement learning. All training signals in MoTiF derive from transition-level fidelity rather than end-task accuracy. Across four visual puzzle benchmarks, this transition-level supervision substantially improves both cross-modal coherence and final task accuracy. The results demonstrate that effective interleaved reasoning requires explicit structural supervision at modality boundaries, not merely scaling or end-task optimization.

---


### 82. [LNTest: A Testbed for Evaluating Bitcoin Lightning Network-Based Botnets](https://arxiv.org/abs/2606.12887)

**<font color=#1a73e8>作者：</font>** Thomas Bakaysa, Ahmet Kurt, Abdul-Salem Beibitkhan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bitcoin's Lightning Network (LN) can be exploited as a covert, low-cost command-and-control (C&C) channel for botnets, as demonstrated by the LNBot and D-LNBot designs. However, both remain proof-of-concept prototypes evaluated only through simulation, leaving key questions about real-world topology formation, propagation complexity, and resilience to takedowns unanswered. We present LNTest, the first reusable testbed for LN-based botnets, built from Core Lightning nodes containerized with Docker over a shared Bitcoin Core regtest chain. LNTest supports three overlay topology modes (a deterministic chain, autonomous peer discovery, and user-supplied graphs), enabling controlled experiments across different botnet structures. Using LNTest, we report three main findings. First, D-LNBot's autonomous formation protocol does not produce the uniform chain from its design; instead, it creates a clustered chain in which cliques are linked by bridge nodes whose removal fragments the network. Second, command propagation scales linearly with botnet size ($\Theta(n)$), not the $O(m \log n)$ previously claimed, and gains nothing from higher neighbor connectivity. Third, the overlay topology determines the effectiveness of takedown strategies: uniform-degree chains resist targeted removal but fragment under random failure, scale-free topologies show the opposite pattern, and the autonomous clustered chain is fragile under both, making it the most vulnerable of the three. LNTest is released as open source, with a script that reproduces all our experiments, to support reproducible research on LN-based botnet defenses.

---


### 83. [LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning](https://arxiv.org/abs/2606.12895)

**<font color=#1a73e8>作者：</font>** Xinrui He, Qiyu Kang, Xuhao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) are well-regarded for their biological plausibility and energy efficiency in processing sequential data. However, dominant SNN architectures typically rely on first-order Ordinary Differential Equations (ODEs) to govern neuronal state transitions. This first-order assumption imposes a "memoryless" bottleneck, limiting the model's capacity to capture the complex, long-range dependencies inherent in long-sequence tasks. In this work, we propose LongSpike, a novel SNN framework that integrates fractional-order State-Space Modeling, or f-SSM, from control theory into the spiking domain. By extending traditional integer-order SSMs to the fractional-calculus regime, LongSpike enables the hierarchical integration of neuronal dynamics with long-memory kernels. To mitigate the computational overhead and parallelization challenges typically associated with fractional operators, we leverage a state-space formulation that supports efficient, parallel training. Empirical evaluations on challenging benchmarks, including Long Range Arena (LRA), large-scale WikiText-103, and Speech Commands, demonstrate that LongSpike outperforms state-of-the-art SNNs in accuracy while preserving sparse synaptic computation. The code is available at this https URL.

---


### 84. [PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent](https://arxiv.org/abs/2606.12896)

**<font color=#1a73e8>作者：</font>** Junfeng Guo Heng Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While real-world applications of reinforcement learning (RL) are becoming increasingly popular, the security of RL systems deserve more attention and exploration. In particular, recent work has revealed that RL agents are vulnerable to backdoor attacks, where a victim agent behaves normally under standard conditions but executes malicious actions when a specific trigger is activated. Existing backdoor defenses for RL either require access to the agent's internal parameters, operate only at the model or trajectory level, or are limited to specific attack types. To ensure the security of RL agents, we propose \texttt{PolicyGuard}, a \textit{test-time step-level} backdoor defense which leverages Gaussian Process (GP) posterior variance and adapts pseudo trajectories to enable uncertainty computation for individual time step. Besides, we also provide theoretical foundations to explain the efficacy of GP posterior variance. Extensive experiments across seven RL games demonstrate that PolicyGuard achieves state-of-the-art detection performance in most cases, with average AUROC of 0.856 for perturbation-based attacks and 0.859 for adversary-agent attacks.

---


### 85. [PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue](https://arxiv.org/abs/2606.12902)

**<font color=#1a73e8>作者：</font>** Wen Zhang, Xiaocui Yang, Zhuoyue Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: this https URL.

---


### 86. [PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation](https://arxiv.org/abs/2606.12911)

**<font color=#1a73e8>作者：</font>** Giang Son Nguyen, Tung X. Nguyen, Hieu Minh Truong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cascaded speech translation (ST) systems suffer from error propagation when Automatic Speech Recognition (ASR) outputs incorrect transcripts. We present the first systematic categorization of ASR errors for Vietnamese ST, classifying substitution errors by phonetic cause and quantifying their impact on downstream Neural Machine Translation (NMT) performance using Linear Mixed-Effects Modelling. We confirm that most ASR substitution errors arise from phonetic confusions rather than random noise, and that these phonetic errors significantly degrade ST quality. Motivated by this finding, we propose Phonetically-Informed Data Augmentation (PiDA), which generates ASR-like corruptions by substituting words with phonetically similar alternatives using phonetic word embeddings. Fine-tuning on a PiDA-augmented version of FLEURS Vietnamese-English improves translation of erroneous ASR outputs (up to +2.04 BLEU over standard fine-tuning) while also slightly improving clean-text performance.

---


### 87. [Selecting Samples on Graphs: A Unified Dataset Pruning Framework for Lossless Training Acceleration](https://arxiv.org/abs/2606.12913)

**<font color=#1a73e8>作者：</font>** Dongyue Wu, Zilin Guo, Xiaoyu Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of modern training datasets has significantly increased computational cost, motivating dataset pruning~(DP) methods which retain only a subset of informative samples to reduce training cost.
Existing pruning criteria typically rely on either intrinsic signals that assess samples independently or extrinsic signals that promote diversity via pairwise relations.
While effective in their own specific regimes, each captures only one aspect of sample utility and lacks robustness across different pruning ratios or data distribution.
In this work, we present a unified graph-based DP framework.
By modeling the dataset as a weighted graph, where node weights encode intrinsic value and edge weights encode extrinsic value, DP can be cast as a Maximum Weight Clique Problem (MWCP).
Although MWCP is NP-hard, its structure admits a principled greedy solution based on sample-wise marginal gains.
Under a few mild conditions, we further prove that this unified objective enjoys a formal approximation guarantee, which applies to a broad family of importance metrics and provides practical design guidelines.
Extensive experiments show that our method outperforms existing DP methods while substantially reducing training cost, reducing training time by over 40\% without sacrificing accuracy on ImageNet-1k with ResNet-50.

---


### 88. [Where Computation Lives Inside TabPFN: Causal Localisation of Attention Head Function](https://arxiv.org/abs/2606.12917)

**<font color=#1a73e8>作者：</font>** Atharva Gupta, Dhruv Kumar, Murari Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the first causal mechanistic analysis of a tabular foundation model, investigating how TabPFN 2.5's feature wise attention heads distribute computation across layers. Using activation patching, ablation, and attention entropy across two synthetic regression datasets, we find clear temporal specialisation: one head's causal necessity dominates that of the others by 2 to 5 times at peak layer, with its dominant layer shifting across tasks of different complexity, while the remaining heads exhibit symmetric late layer profiles. Attention entropy and patching provide convergent evidence for the computationally active layers of the dominant head. We additionally investigate inference time steerability via contrastive activation steering, which fails to transfer across samples. We attribute this result to TabPFN's in context learning mechanism, which encodes task structure through context dependent attention rather than the stable parametric directions that make steering tractable in language models.

---


### 89. [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](https://arxiv.org/abs/2606.12918)

**<font color=#1a73e8>作者：</font>** Chejian Xu, Zhaorun Chen, Jingyang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.

---


### 90. [LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold](https://arxiv.org/abs/2606.12921)

**<font color=#1a73e8>作者：</font>** Franz Louis Cesista, Katherine Crowson, Cédric Simal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) significantly reduces compute and memory costs for finetuning Deep Learning models but is often harder to tune than dense training: when using factor-wise optimizers such as AdamW, it is sensitive to initialization choices, its optimal learning rates transfer poorly across ranks, and it often fails to beat dense baselines. We derive LoRA-Muon by applying the Muon optimizer's spectral steepest-descent rule to the low-rank setting. Along with our split weight-decay rule, our main claim is that LoRA-Muon is a good low-rank proxy for full-rank Muon and Shampoo-family optimizers. Its optimal learning rates transfer across rank, width, depth, and factor-rescaling. In our compute-matched TinyShakespeare study, a rank-$2$ proxy recovers the dense best tested learning rate, and a rank-$32$ LoRA-Muon run attains lower mean validation loss than the dense baseline in the seed-averaged sweep. We further show that the Spectron optimizer depends on arbitrary factor scaling, so it would likely be a poor fit when finetuning starts from badly imbalanced factors, and that LoRA-RITE's simplified QR-coordinate core implements the same spectral update. LoRA-Muon computes that update without QR-decomposition and avoids storing second moments, making it more accelerator-friendly and memory-efficient.

---


### 91. [Order Is Not Control](https://arxiv.org/abs/2606.12923)

**<font color=#1a73e8>作者：</font>** Gareth Seneque, Lap-Hang Ho, Nafise Erfanian Saeedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI alignment, interpretability, steering, and neural perturbation studies identify order-inducing objects. We argue that order is not control. Control requires a receiver-gated response law: a denominator-indexed operator mapping material state, action/drive, bath, and receiver state to response displacement, sinks, effort, and basin projection. We identify it across biological, LLM, adapter, and stochastic-operator panels. The laws are local: an intervention can be admitted, saturated, sign-changing, leaky, or overdriven depending on medium, bath, receiver state, action port, and comparator. Control is assigned when finite effort moves a target or outcome-readout class under the same denominator while damage, null/evasive, invalid format, overdrive, and unnecessary effort stay bounded. Mouse ALM, C. elegans, and zebrafish panels provide physical response-operator evidence while excluding coordinate identity and controller conclusions. LLM panels show generated-output response laws: across four material conditions, response vectors are predictable at 72.8-73.7% component-sign accuracy, rising to 84.3-84.8% on nonzero components; held-out observers predict system-effect and target/oracle families at 93.6% and 91.7% accuracy. Constitution-conditioned adapters reshape susceptibility as prepared media, and stochastic-operator panels separate measured opportunity from deployable action policies. This gives a driven-dissipative response-system account at the mesoscopic control level: drives act through prepared media, baths, and receivers, producing admitted movement, impedance, sinks, or overdrive. The evidence supports local admitted control and measurable stochastic response operators, while leaving deployable pre-generation control, hidden/logit causal sufficiency, biological-to-LLM coordinate identity, and literal thermodynamic quantities outside scope.

---


### 92. [Multi-Label Test-Time Adaptation with Bayesian Conditional Priors](https://arxiv.org/abs/2606.12925)

**<font color=#1a73e8>作者：</font>** Qiru Li, Ao Zhou, Zhiwei Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label recognition with frozen Vision-Language Models (VLMs) is brittle under distribution shift: standard zero-shot inference scores labels independently, ignoring co-occurrence structure and producing incoherent label sets where dominant concepts suppress weaker but compatible labels. We introduce Bayesian Conditional Priors (BCP) Estimation, a gradient-free test-time adaptation method that injects label dependency without tuning the backbone. BCP views zero-shot logits as a proxy for marginal posteriors under a fixed image-text likelihood and attributes shift-induced errors mainly to a mismatched label prior. For each test image, it selects a high-confidence anchor label and applies an anchor-conditioned Bayesian refinement. This update is closed-form in logit space and admits a pointwise mutual information (PMI) interpretation, explicitly promoting compatible labels and suppressing incompatible ones. BCP operates without target annotations by estimating anchor-conditioned priors online from the unlabeled test stream via lightweight second-order co-occurrence statistics, adding negligible overhead beyond a single forward pass. Across standard multi-label benchmarks and multiple CLIP backbones, BCP consistently outperforms strong TTA baselines, e.g., improving RN50 average mAP from 57.31 to 69.22 and ViT-B/16 from 62.61 to 71.79.

---


### 93. [Is Spurious Correlation Removal Always Learnable?](https://arxiv.org/abs/2606.12930)

**<font color=#1a73e8>作者：</font>** Yibo Zhou, Bo Li, Hai-Miao Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Invariant learning can fail even when the invariant structure is statistically identifiable. We show a conditional computational barrier: under a black-box samplable supervised sparse recovery primitive motivated by average-case sparse-recovery reductions, there exist \emph{samplable} multi-environment instances with a one-dimensional predictive invariant subspace ($k=1$) that are learnable with polynomial samples by exhaustive search, while any polynomial-time constant-accuracy recovery algorithm would contradict the primitive. We further quantify environment diversity by a separation parameter $\gamma$, which controls identifiability and the curvature of invariance objectives. Under sufficient diversity and local Gaussian regularity, the minimax risk is $\mathbb{E}[\dist(\hat{V},V_{\mathrm{inv}})^2]=\Theta(k(d-k)/(n|\mathcal{E}|))$, and under label-induced shifts a phase transition occurs at $n^*\propto k(d-k)/(|\mathcal{E}|\gamma^2)$ with refined estimation error scaling proportional to $1/\gamma^2$. Synthetic and real datasets illustrate the predicted gaps and transitions and motivate simple diversity diagnostics.

---


### 94. [MAMVI: 3D Test-Time Adaptation via Masked Multi-View Point Clouds](https://arxiv.org/abs/2606.12939)

**<font color=#1a73e8>作者：</font>** Inseok Kong, Geunyoung Jung, Jiyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D point cloud models suffer significant performance degradation under distribution shifts caused by sensor noise, occlusions, and environmental changes. Test-time adaptation (TTA) has emerged as a practical paradigm for mitigating this issue during inference. Recently, leveraging multi-view augmentation has shown promise in improving 3D TTA performance. However, existing multi-view approaches are often constrained by sequential optimization that treats each view independently. This sequential optimization leads to substantial inference latency due to repetitive optimization steps, making real-time adaptation impractical. To address this, we propose Masked Multi-View Test-Time Adaptation (MAMVI), which replaces sequential optimization with a unified single-step adaptation. Specifically, MAMVI utilizes a hybrid masking strategy that combines fixed ratios for stability with Beta-distributed sampling for diversity. By aggregating losses across multiple views, MAMVI performs adaptation through a single backward pass based on multi-view consensus. Additionally, a confidence-based adaptive learning rate is used to dynamically adjust the adaptation intensity for each sample. Extensive experiments on ModelNet-40C, ShapeNet-C, and ScanObjectNN-C demonstrate that MAMVI achieves state-of-the-art accuracy on ShapeNet-C and ScanObjectNN-C. Moreover, it remains competitive on ModelNet-40C while delivering 4.9-8.9 times faster inference, making it highly suitable for real-time applications. Our code is available at this https URL

---


### 95. [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/abs/2606.12941)

**<font color=#1a73e8>作者：</font>** Shu Tong Luo, Wenqin Liu, Rui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a user reveals task-critical information across several conversation turns, LLM accuracy drops by up to 65% despite full context availability. We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history. To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation. Training only on sharded GSM8K, our memory-augmented policy significantly improves multi-turn accuracy and generalises zero-shot to harder math and out-of-domain long-context QA. Moreover, memory-trained models outperform full-history baselines even when given the full history at test time, suggesting that learning to compress induces more robust incremental reasoning than full-context exposure alone.

---


### 96. [ViPER: Vision-based Packing-Aware Encoder for Robust Malware Detection](https://arxiv.org/abs/2606.12949)

**<font color=#1a73e8>作者：</font>** Fatima Qaiser, Bisma Tahir, Muhammad Abid Mughal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Visualization-based malware detection maps raw binary bytes to grayscale images and applies learned visual classifiers, providing an evasion-resistant and disassembly-free alternative to conventional analysis pipelines. However, executable packing remains a critical failure mode: packed binaries produce high-entropy images that obscure the structural patterns these models rely on. Because packing is also prevalent in benign software (e.g., for compression or copy protection), packing state alone is not a reliable indicator of maliciousness, and existing approaches do not address this challenge within a unified supervised framework. We present ViPER, a Vision-based Packing-Aware Encoder for Robust malware detection. ViPER builds on a LoRA-adapted ViT-B/14 backbone with a dual-head architecture that jointly learns malware classification and packing detection. A packing-aware gating mechanism conditions malware predictions on the inferred packing state, enabling distinct decision boundaries for packed and unpacked inputs. To address packing label skew during training, we employ frequency-weighted losses with stratified sampling over joint class-packing strata. Evaluated on 200,000 Windows PE byteplot images, ViPER achieves a balanced accuracy of 0.8521, ROC-AUC of 0.9260, and AUPR of 0.9279, outperforming representative state-of-the-art baselines across all primary metrics, while attaining a packing detection AUC of 0.9949.

---


### 97. [YOLO-AMC: An Improved YOLO Architecture with Attention Mechanisms for Building Crack Detection](https://arxiv.org/abs/2606.12958)

**<font color=#1a73e8>作者：</font>** Ching-Yu Tsai, Chia-Min Lin, Chih-Hsiang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crack detection plays an important role in infrastructure inspection and Structural Health Monitoring (SHM). However, cracks typically appear as thin, low-contrast structures and are easily affected by background noise, posing challenges for existing object detection models. This study proposes an improved YOLO-based architecture with integrated attention mechanisms, termed YOLO-AMC (YOLO with Attention Mechanisms for Crack Detection), to enhance automated crack detection performance. Based on YOLOv11, the original C2PSA module is removed, and multiple attention mechanisms, including Global Attention Mechanism (GAM), Residual Convolutional Block Attention Module (Res-CBAM), and Shuffle Attention (SA), are introduced into the multi-scale feature fusion layers of the Neck to strengthen cross-scale feature integration. Experimental results demonstrate that YOLO-AMC consistently outperforms baseline models YOLOv11n and YOLOv8n across multiple evaluation metrics. Among the evaluated attention modules, GAM achieves the best detection performance, obtaining mAP@0.5 = 0.9917 and mAP@0.5:0.95 = 0.9506 on the test dataset, which are higher than those of YOLOv11 (0.9833 / 0.9112) and YOLOv8 (0.9707 / 0.8921). Furthermore, while maintaining a computational complexity of 7.6 GFLOPs, the proposed model achieves 110.95 FPS on an NVIDIA RTX 4090 platform and approximately 5 FPS on a Raspberry Pi 5 edge device, demonstrating a favorable trade-off between accuracy and deployment efficiency. The implementation code for this study is available on GitHub at this https URL.

---


### 98. [Circuit Synchronization Precedes Generalization: Causal Evidence from Fourier Structure in Grokking Transformers](https://arxiv.org/abs/2606.12966)

**<font color=#1a73e8>作者：</font>** Achyuthan Sivasankar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking -- where a transformer on modular arithmetic suddenly transitions from near-chance to near-perfect validation accuracy -- is attributed to a Fourier circuit, but its timing, causal structure, and controllability remain poorly understood. We introduce the Frequency Synchronization Degree (FSD), a normalised, permutation-tested metric for Fourier circuit synchronisation requiring no prior circuit knowledge. Across nine modular addition configurations (primes p in {53, 71, 97, 113, 131}, three seeds), FSD synchronises 500-3,000 steps before grokking (mean lead +1,722 steps; all nine positive, sign-test p~0.004), and precedes a restricted-logit loss baseline (Nanda et al.'s excluded loss) in all nine cases, making it the earliest available predictor. We provide direct causal evidence that the inter-phase gap is a regularisation phenomenon: forking training at the FSD-ceiling step and varying weight decay lambda produces strictly monotone earlier grokking, with Delta_t proportional to 1/lambda. This law replicates across three primes (p in {53,97,131}; R^2=1.00 and R^2=0.99 for two clean cases), captured as Delta_t ~ C/lambda, consistent with (1/lambda)*log(||W_mem||/tau). Architecture ablations show an attention-only model groks with a strong FSD precursor; an MLP-only model never groks; a single-layer model's FSD lags, confirming the precursor is a multi-block circuit property.

---


### 99. [Predicting Cognitive Load from Speech and Interaction Dynamics in Dyadic Conversations](https://arxiv.org/abs/2606.12971)

**<font color=#1a73e8>作者：</font>** Tahiya Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating cognitive load from speech has largely been studied in controlled laboratory settings, with limited understanding of its reliability in natural collaborative conversations. We investigate whether speech and interaction dynamics predict perceived cognitive load during dyadic conversations. We analyze audio from 53 dyads performing nine collaborative tasks and extract static acoustic, dynamic, and interaction features to train a two-head Gated Recurrent Unit encoder to predict cognitive load scores. Results show conversational interaction provides useful signals for predicting cognitive load related to time pressure, mental work, effort, and task performance. Temporal demand is associated with turn-taking dynamics such as overlap and speaker switch, while mental demand is linked to imbalanced participation between speakers. These findings highlight the importance of task structure and conversational interaction for modeling cognitive load in natural collaborative settings.

---


### 100. [From Prompts to Preferences: An Open-Source Platform for Generative AI-Enhanced Conjoint Analysis](https://arxiv.org/abs/2606.12972)

**<font color=#1a73e8>作者：</font>** Philipp Brauner  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conjoint analysis is a widely used preference measurement method in marketing research, political science, healthcare, and human-computer interaction. Despite broad adoption, researchers without access to commercial platforms face significant barriers, as existing tools are either expensive or lack end-to-end survey infrastructure. This paper presents an open-source, self-hosted web application for designing, deploying, and analysing conjoint surveys. Beyond conventional tabular stimuli, the platform uses generative AI to produce integrated stimuli formats: textual scenario descriptions generated by a large language model, and visual stimuli by a text-to-image model. A researcher-defined base prompt is parameterised with the conjoint profile, and optional LLM-facing level annotations enrich the generation. A structured setup wizard, AI-assisted attribute suggestion, and live data analysis lower the technical barriers for researchers new to conjoint methodology. A full export bundle including all stimuli, their generating prompts, and response data facilitates transparency and reproducibility. The platform is demonstrated through a proof-of-concept study on care robot preferences for ambient assisted living (AAL, N=55) using AI-generated visual stimuli. The paper discusses the role of AI assistance in conjoint design, arguing that theoretical grounding must remain the researcher's responsibility, and outlining how genAI-generated stimuli can broaden the methodological repertoire for HCI and related fields.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
