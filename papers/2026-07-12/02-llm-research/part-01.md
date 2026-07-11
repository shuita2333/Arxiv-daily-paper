# 🧠 大模型相关研究 | 2026年07月12日

> 本类共 **99** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-99](./part-02.md)

---

### 1. [ReCoLoRA: Spectrum-Aware Recursive Consolidation for Continual LLM Fine-Tuning](https://arxiv.org/abs/2607.07719)

**<font color=#1a73e8>作者：</font>** Wentao Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning adapts a large language model to one task cheaply, but across a task sequence LoRA-style methods keep stacking low-rank updates on the same frozen weight, so each new task tends to overwrite the previous ones. We present ReCoLoRA (Recursive Consolidation of Low-Rank Adapters), a spectrum-aware framework for continual fine-tuning: adapters are initialized from a randomized SVD of the pretrained weight, per-layer effective ranks are selected by an elbow criterion, and the principal subspace is adapted before residual capacity is opened. Before each new task, ReCoLoRA re-decomposes the current effective weight, rather than the original one, into a frozen residual, a slowly updated principal component, and a fresh adapter (recursive consolidation), so every task starts from the model that has already absorbed its predecessors. On a six-task continual GLUE sequence over four 7-8B backbones, ReCoLoRA attains the best final average score on three of the four backbones against rank-swept LoRA, PiSSA, AdaLoRA, and DoRA baselines while training fewer parameters; an oracle-routed task-bank variant serves as an upper bound under full task isolation. Code: this https URL.

---


### 2. [Omni-Sleep: A Sleep Foundation Model via Hierarchical Contrastive Learning of CNS--ANS Dynamic](https://arxiv.org/abs/2607.07720)

**<font color=#1a73e8>作者：</font>** Zhoujie Hou, Song Wang, Kexin Lou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep physiology arises from the coordinated dynamics of the central nervous system (CNS) and autonomic nervous system (ANS), as reflected by multimodal polysomnography signals including EEG, EOG, EMG, ECG, and respiration. However, existing sleep foundation models often fuse heterogeneous biosignals in a topology-agnostic manner, overlooking their physiological organization. We introduce Omni-Sleep, a sleep foundation model that uses the CNS/ANS partition as a physiological prior for topology-constrained representation learning. Omni-Sleep learns structured representations through three objectives: intra-system consistency, which captures shared subsystem-level factors within neural and cardio-respiratory signals; inter-system synchronization, which aligns subsystem trajectories to model brain--body dynamics; and latent-space masked temporal modeling, which captures long-horizon sleep dynamics. Pre-trained on over 100,000 hours of multi-center multimodal PSG data, Omni-Sleep is evaluated on sleep staging and multi-disease classification. Across datasets and modality-ablation settings, Omni-Sleep outperforms strong foundation-model baselines, showing improved label efficiency, cross-dataset generalization, and robustness to missing modalities. These results highlight the value of physiological hierarchy for generalizable sleep representation learning. Code is available at this https URL.

---


### 3. [Context Graphs for Proactive Enterprise Agents](https://arxiv.org/abs/2607.07721)

**<font color=#1a73e8>作者：</font>** Avinash Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) and agentic frameworks have advanced enterprise AI considerably, yet agents remain fundamentally reactive: they wait for a human query before acting. This paper argues that genuine enterprise productivity gains require proactive agents: systems that surface relevant, actionable information to workers before they ask. We propose the Context Graph, a live relational data structure that models enterprise entities, their relationships, and state transitions over time. Built on this graph, we define a Delta Detection Engine that continuously monitors state changes, a Proactivity Scorer that ranks candidate insights by urgency, relevance, and persona-fit, and a Surfacing Layer powered by an LLM that delivers ranked notifications with grounded explanations. We formalize each component, derive a unified Proactivity Score function, and provide a complete end-to-end Python implementation using NetworkX and the Anthropic Claude API. Evaluation across three generic enterprise case studies (contract lifecycle management, engineering incident response, and sales pipeline hygiene) demonstrates that context-graph-driven proactivity achieves Precision@5 of 0.83, a false positive rate of 0.11, and reduces mean time to surface from 47 minutes (reactive baseline) to under 30 second.

---


### 4. [Collective Intelligence with Foundation Models](https://arxiv.org/abs/2607.07729)

**<font color=#1a73e8>作者：</font>** J. de Curtò, I. de Zarzà  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As foundation models grow in scale and diversity, coordinating multiple models into cooperative reasoning systems offers a path toward safer, more reliable AI. This chapter presents a multi-agent framework where solver models generate independent drafts, each undergoes structured critique and revision by a critic agent, and an aggregator agent synthesizes a final consensus solution. A scoring module provides semantic, numerical, and procedural evaluation across all agents. Through ablation studies on a benchmark spanning calculus, physics, chemistry, biology, economics, optimization, statistics, and mathematics, we isolate the contributions of framework architecture versus model diversity. We compare four configurations: (1) Individual Baseline, (2) Homogeneous Framework using one shared model, (3) Redundant Homogeneous Solvers using multiple instances of the same model, and (4) Heterogeneous Framework with diverse specialized models. Results show that while framework structure and redundant sampling yield modest gains, model heterogeneity is the critical factor driving substantial performance improvements. The heterogeneous configuration achieves superior step-wise accuracy (0.64 vs. 0.54 for individual models; 2.3x improvement over homogeneous configurations) with reduced variance across categories and difficulty levels. Step-wise reasoning quality (correctness of intermediate steps, not just final answers) improves dramatically only with model diversity, showing that heterogeneous agents provide complementary error detection and reasoning refinement essential for explainability and auditability. We discuss architectural principles, evaluation methodology, and implications for Global Applied AI, showing how heterogeneous multi-agent coordination supports transparent, auditable, high-confidence decision-making across scientific and industrial domains.

---


### 5. [Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE](https://arxiv.org/abs/2607.07740)

**<font color=#1a73e8>作者：</font>** Haozhan Tang, Zerui Wang, Yuxian Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs are increasingly deployed in long-context applications such as retrieval-augmented generation, repository-level coding, and agentic workflows whose accumulated reasoning and tool traces routinely push the input an order of magnitude past the pretraining window, making zero-shot context extension the dominant deployment path for open-weight checkpoints. Most existing zero-shot methods fix a single rescaling factor up front, so an aggressive factor sacrifices short-context fidelity while a conservative one breaks down at long contexts. We propose Jet-Long, a tuning-free zero-shot method that pairs a local RoPE-faithful window with a long-range window whose rescaling factor adapts dynamically to the current sequence length, recovering the base model exactly at short inputs while extrapolating cleanly at long ones. An inclusion-exclusion attention merge and an on-the-fly RoPE correction rotation make the bifocal construction essentially free at inference; fused into a single CuTe kernel, long-context prefill reaches up to $1.39\times$ FA2 throughput on H100 (approaching the Hopper-only FA4), and single-batch generation incurs $\le 4\%$ overhead at every length. On Qwen3-1.7B/4B/8B up to 128K context, Jet-Long leads RULER by $+4.79$/$+2.18$/$+2.03$~pp over the strongest baseline at 1.7B/4B/8B, achieves the best overall accuracy on HELMET-RAG (a benchmark identified by HELMET as the most efficient predictor of downstream long-context performance) and attains the lowest PG-19 perplexity. Jet-Long also generalizes to hybrid attention architectures such as Jet-Nemotron for further long-context improvement without retraining, and remains hyperparameter-resilient for ease of deployment.

---


### 6. [Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation](https://arxiv.org/abs/2607.07748)

**<font color=#1a73e8>作者：</font>** Didula Samaraweera, Anjana Supun, Srinath Perera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models achieve strong code generation for high resource languages like Python and Java but suffer sharp performance drops on Low-Resource Programming Languages~(LRPLs) such as Julia. Improving Small Language Models~(SLMs) for these languages faces a trilemma: Supervised Fine-Tuning~(SFT) is bottlenecked by data scarcity, inference-time scaling is too expensive for deployment, and Reinforcement Learning from scratch yields near zero advantages. We propose a three-phase pipeline that resolves this trilemma by decoupling syntax acquisition from algorithmic reasoning. First, we \emph{left-shift} inference-time compute to an offline data synthesis engine that uses iterative compiler and test feedback to generate verified training examples. Second, we fine-tune an SLM on this synthetic, verified data to embed strong syntactic priors. Third, we apply Reinforcement Learning with Verifiable Reward~(RLVR) grounded by language-agnostic Input/Output tests, where the SFT prior constrains exploration away from syntax errors. Applied to Qwen3-8B, our pipeline improves pass@1 by up to +7.6 points on MultiPL-E and +14.2 points on the Agnostics LiveCodeBench for Julia compared to SOTA results. Furthermore, the pipeline only used $\frac{1}{3}$ data and $\frac{1}{6}$ cost over the previous state-of-the-art. We further demonstrate that the pipeline generalizes to Ballerina achieving 49.7\% MultiPL-E Pass@1, a language with near-zero pretraining representation. Ablations confirm that both the SFT phase and execution-grounded rewards are necessary for stable training.

---


### 7. [Image classification via a quantum-inspired strategy involving a mixture of experts](https://arxiv.org/abs/2607.07754)

**<font color=#1a73e8>作者：</font>** Kumari Jyoti, Rohith Babu, Apoorva D. Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pattern recognition problems arise in a variety of physical image processing situations, and convolutional neural networks are a popular scheme for the required feature extraction and classification tasks. The classical networks use diffusion-based smearing and block-wise pooling to downsample the image data and capture important structural features. In this work, we propose and demonstrate a more efficient quantum-inspired strategy involving a mixture of experts. It is a hybrid classical-quantum framework. The quantum part consists of amplitude encoding of the images, convolution using local unitary operations, multiple experts processing the same image with different parameters, and feature extraction using quantum stabiliser codes. The classical part then jointly processes the features extracted by different experts using a standard fully connected neural network for image class prediction. Using MNIST and Fashion-MNIST datasets as benchmarks, we demonstrate that the joint expert analysis outperforms the individual expert one, as well as reduces the failure rate of image class prediction by around a factor of two. The overhead of our quantum-inspired strategy is only moderate on GPU workstations, which makes our proposal a practical alternative to existing classical schemes. We also point out how the quantum part of our framework can be executed on a quantum processor.

---


### 8. [Scalable and Trustworthy Earth Observation Foundation Models](https://arxiv.org/abs/2607.07758)

**<font color=#1a73e8>作者：</font>** Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) have transformed machine learning from isolated task-specific model development toward general-purpose models pretrained on broad data and adapted to multiple downstream tasks. Earth observation (EO) is an important domain for this paradigm because satellite and airborne archives are large, high-revisit, and increasingly multimodal, while reliable field labels are often sparse. Remote sensing foundation models (RSFMs) cannot be transferred reliably/optimally without domain-specific adaptation. This is because EO data are governed by measurement physics and operational decision constraints. This chapter reviews the design principles arising from these domain-specific constraints. It first defines the FMs paradigm in remote sensing (RS), then synthesizes the current model landscape, pretraining objectives, architecture designs, downstream adaptation and trustworthiness requirements. The chapter also incorporates recent benchmark evidence showing that no single geospatial foundation model is universally best and that inconsistent evaluation remains a major issue to fair comparison and reliable deployment. In addition, two brief environmental monitoring case studies; physics-informed spectral targeted masking for harmful algal bloom prediction and reinforcement learning for adaptive environmental monitoring station selection to illustrate the FMs domain-guided principles in practice. This chapter posits that next-generation RSFMs should be evaluated not only by benchmark accuracy, but also by modality-aware transfer and physically plausible representations for trustworthy EO decisions.

---


### 9. [Adversarial Social Epistemology for Assemblies of Humans and Large Language Models](https://arxiv.org/abs/2607.07760)

**<font color=#1a73e8>作者：</font>** Mihnea C. Moldoveanu, Joel A.C. Baum  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We outline an adversarial social epistemology (ASE) for densely interactive communicative landscapes in which public assertions are scaffolded by chains of testimony, inference, institutional certification, and tacit trust. In such landscapes, agents have incentives and affordances to distort, color, omit, fabricate, or strategically under-specify information for private, reputational, rhetorical, or material gains. We argue that these phenomena are not adequately captured by familiar descriptions of epistemic bubbles, echo chambers, or misinformation diffusion. What requires explanation is how communicative agents exploit the commitments and entitlements that normally make scaffolded assertions trustworthy. We provide language that delivers the requisite analysis, outline mechanisms that subvert trust in scaffolded public communications, and outline machinery for auditing and redressing trust breaches arising from subverting the auditability of inferential chains, drawing on epistemic networks, enriched with an inferentialist semantics for interpreting assertions.

---


### 10. [Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical Reasoning](https://arxiv.org/abs/2607.07761)

**<font color=#1a73e8>作者：</font>** Qi Peng, Jiatong Li, Sirui Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as important tools in healthcare, showing growing potential for clinical reasoning and patient care. This survey examines recent progress in medical LLMs, focusing on reasoning applications and requirements. We present a dual-view approach that connects clinical practice with computational methods. On the clinical side, we establish a five-level competency scheme following Miller's Pyramid, progressing from knowledge recall to dynamic case management. On the computational side, we link deductive, inductive, and abductive reasoning patterns to common medical goals and tasks. We also introduce a benchmark dataset spanning five levels of medical reasoning capability and report results on 18 state-of-the-art models, revealing that medical specialist models excel in diagnosis-centric tasks while general models lead in decision support and dialogue. We conclude by discussing current progress and open challenges, including data limitations, hallucination, and grounding issues, and outline directions toward safer, more reliable, and workflow-ready systems.

---


### 11. [Alignment Plausibility: A New Standard for Assuring AI in Healthcare](https://arxiv.org/abs/2607.07766)

**<font color=#1a73e8>作者：</font>** Gwydion Williams, Sara Zannone, Bilal A Mateen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become significant providers of mental health support, yet they remain products of an attention economy whose operational and commercial targets favour sustained engagement over the friction that effective psychological support often requires. Developers' safety responses have been largely reactive, addressing the most visible and acute harms while subtler, longer-term patterns of risk (e.g., dependency, boundary erosion, the amplification of distorted beliefs) receive less attention. We contend that making LLMs structurally safe requires alignment organised at three levels that mirror how society assures the safety of human clinical practice: 1) explicit value specification grounded in the codified normative commitments of clinical practice; 2) training that embeds those values in the model; and 3) oversight that detects drift and longer-term harm during deployment, much as clinical supervision does for human practice. Organising alignment in this way yields a construct we call alignment plausibility - a structured demonstration that a system's values, training regime, and oversight mechanisms are together consistent with safe and positive outcomes. We propose alignment plausibility as a regulatory construct (by drawing analogy to the established construct of biological plausibility) for AI in health: a principled way to argue for, or against, trust that systems are aligned to positive health outcomes, will cause no harm even where capable of doing so, and will ultimately lead to patient benefit.

---


### 12. [From Solvers to Research: Large Language Model-Driven Formal Mathematics at the Research Frontier](https://arxiv.org/abs/2607.07779)

**<font color=#1a73e8>作者：</font>** Eric Jiang, Xiao Liang, Yikai Zhang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent developments in AI for Mathematics (AI4Math), especially Large Language Model (LLM)-driven theorem provers, has achieved remarkable success in formal proof generation for well-defined mathematical problems through Interactive Theorem Proving (ITP) languages. However, current systems remain fundamentally limited in tackling frontier research mathematics, such as discovering new theorems or resolving open conjectures, which are often open-ended, under-specified, and involve multiple layers of abstraction. We argue that the next leap in AI4Math systems requires a decisive shift from predefined problem-solvers to research agents that can address frontier mathematical challenges with rigorous formal mathematical reasoning. In this position paper, we provide a systematic review of the field, covering datasets, auto-formalization, and proof synthesis. More importantly, we identify core limitations of existing systems in serving as mathematical research agents, examining issues across datasets, relational structure, mathematical exploration, tool ecosystem, and human-AI collaboration, outlining a strategic road-map for the future of AI4Math.

---


### 13. [DreamCharacter-1: From 3D Generative Foundation Models to Product-Ready Character Generation](https://arxiv.org/abs/2607.07817)

**<font color=#1a73e8>作者：</font>** Weizhe Liu, Yunjie Wu, Xiangqian Shu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DreamCharacter-1, a lightweight post-adaptation framework that calibrates pretrained 3D foundation models toward high-fidelity, production-ready 3D character generation. Building upon a 3D foundation backbone, our pipeline incorporates three task-oriented components: (1) geometry post-training, which enhances fine-grained surface details through geometric preference optimization; (2) texture post-training, which synthesizes high-resolution textures and refines the appearance of occluded regions; and (3) inference acceleration, which enables scalable deployment. Extensive quantitative and qualitative experiments demonstrate that DreamCharacter-1 produces visually compelling and structurally robust 3D character assets, consistently surpassing state-of-the-art character generation methods.

---


### 14. [VectorizationLLM: Smart Vectorization Based AI Assistant](https://arxiv.org/abs/2607.07846)

**<font color=#1a73e8>作者：</font>** Ryan Duke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> VectorizationLLM is a specialized Large Language Model based on Google open-weight LLMs. The model is designed to assist students to learn smart vectorization, time/wave vector analysis, piecewise functions, Fourier analysis, and differential equations in MATLAB. The course application is CTEC 247: Applied Computational Analysis II by the Department of Electrical & Computer Engineering Technology at New York Institute of Technology Old Westbury. The LLM model is designed to be an instructive assistant, providing detailed explanations of concepts with examples from in-class notes without providing direct answers to questions. The model is designed with a RAG (Retrieval Augmented Generation) knowledge base and system prompt architecture. Examples in both code, text, and images are provided in the LLM responses.

---


### 15. [When Does Continual Learning Require Learning](https://arxiv.org/abs/2607.07847)

**<font color=#1a73e8>作者：</font>** Anne Harrington, Nayan Saxena, Michael Murphy 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become increasingly capable, the next question is how can we enable models to continually learn? Today, the field largely frames this as a problem of context management and mitigating forgetting. We argue this framing is incomplete: continual learning is fundamentally about increasing model competence as the world changes. We disentangle this change along two axes -- space, where the model encounters new domains, and time, where the underlying data drifts under a fixed task. This framing lets us study continual learning under realistic conditions: new domains arrive over time, facts drift past their training cutoff, and agentic interactions accumulate state across episodes. To evaluate methods under this setting, we recast widely used LLM benchmarks as sequential problems and introduce a single mechanism-agnostic protocol that compares prompt-based methods (GEPA, ACE), supervised learning (SFT, SDFT), reinforcement learning (GRPO, SDPO), and context compression (Cartridges, In-place TTT). Prompt-based methods fit each new stage quickly but degrade on future tasks. Distillation-based methods accumulate knowledge stably but struggle to update outdated facts. Context compression improves efficiency without substantially improving the ability to learn new tasks. Online reinforcement learning adapts most effectively to knowledge updates but remains sensitive to noisy reward signals. Overall, our results suggest that continual learning is not a single capability: different patterns of environmental change require fundamentally different update behaviors, determining when adaptation must be learned inside model weights and when it can be achieved through external scaffolding. We hope that understanding where each method succeeds and fails will guide the design of stronger continual learning systems.

---


### 16. [NFTR: From Provable Mode-Averaging to Geodesic Subgoal Selection in Offline Goal-Conditioned RL](https://arxiv.org/abs/2607.07855)

**<font color=#1a73e8>作者：</font>** Erdemt Bao, Xing Lei, Jun Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical Implicit Q-Learning (HIQL), an offline goal-conditioned RL method, selects subgoals by value-function advantages alone. This rule has two coupled failure modes. Optimistic bias treats lucky stochastic outcomes as skillful choices, and mode collapse reduces a multi-modal subgoal distribution to a single Gaussian mean that often falls in unreachable regions. We propose NFTR (Normalizing Flows subgoal policies with Triangle-slack Reweighting). A conditional Normalizing Flow replaces the Gaussian policy, and a closed-form mode-averaging result identifies NFs as the minimal generative class for AWR-based subgoal selection. A triangle slack score, built on the architectural triangle inequality without relying on distance accuracy, multiplicatively corrects the AWR weight to downweight subgoals whose detour cost exceeds average reachability. Triangle-slack vanishes on geodesics in deterministic MDPs and remains a conservative upper bound on composability violation under stochastic dynamics. The RWDR objective preserves AWR's population-level monotonic improvement and admits a three-term suboptimality decomposition. Together, these two ingredients yield subgoal selection that provably avoids the Gaussian collapse described above and remains stable under stochastic dynamics. GitHub page: this https URL

---


### 17. [Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting](https://arxiv.org/abs/2607.07858)

**<font color=#1a73e8>作者：</font>** Robert Richardson, Josh Meyers, Brian Hartman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is beginning to reshape actuarial practice, particularly in domains that require reasoning over unstructured documents, heterogeneous data sources, and regulated decision workflows. Actuaries now face a design space that ranges from traditional rule-based automation to large language models (LLMs), retrieval-augmented generation (RAG), and multi-agent ``agentic'' systems that plan, retrieve, call tools, and reflect. This paper examines how these emerging architectures can support actuarial priorities such as transparency, auditability, and human-in-the-loop governance, with a focus on straight-through decision processes. To make these ideas concrete, we develop and analyze an agentic AI framework for straight-through underwriting of small commercial Business Owner Policies (BOPs). We construct a synthetic but realistic experimental environment and compare three underwriting pipelines: (i) a single-LLM baseline, (ii) a naive RAG system, and (iii) a multi-agent ``Agentic RAG'' pipeline that combines targeted retrieval, third-party data checks, and explicit multi-step rule evaluation. The agentic system performs best overall, with the largest gains in multi-step and missing-information scenarios, where structured retrieval and reflection help the model avoid unsupported straight-through decisions.

---


### 18. [Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning](https://arxiv.org/abs/2607.07859)

**<font color=#1a73e8>作者：</font>** Benjamin Poole, Minwoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) research has increasingly shifted focus towards alignment, ensuring agents learn behaviors adhering to human values. While human demonstrations and feedback have proven crucial for alignment, existing approaches predominantly combine these signals using multi-stage pipelines designed for the contextual bandit framing of language generation. Yet little work explores how these complementary inputs can serve as a richer, interconnected signal for single-stage offline training in fully sequential decision-making environments. We propose Feedback Manipulation Regularization (FMR), an algorithm-agnostic method that harnesses evaluative feedback as a corrective signal to improve the alignment of imitation learning policies. We adapt Safety Gymnasium environments to be a principled testbed for alignment evaluation, demonstrating improved aptitude and up to a 98\% reduction in misalignment across a range of imitation learning algorithms. FMR remains robust in limited data regimes, even when learning from scarce aligned and uninformative noisy demonstrations.

---


### 19. [Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration](https://arxiv.org/abs/2607.07895)

**<font color=#1a73e8>作者：</font>** Weicheng Ma, John Guerrerio, Soroush Vosoughi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both well-documented stereotypes from prior literature and culturally specific biases absent from English-centric resources. Using LLMs to generate candidate stereotypes and in-culture annotators to validate them, we demonstrate the framework's effectiveness in identifying nuanced, region-specific biases. Our evaluation of Spanish-supporting LLMs using EspanStereo reveals significant variation in stereotypical behavior across countries, highlighting the need for more culturally grounded assessments. Beyond Spanish, our framework is adaptable to other languages and regions, offering a scalable path toward multilingual stereotype benchmarks. This work broadens the scope of stereotype analysis in LLMs and lays the groundwork for comprehensive cross-cultural bias evaluation.

---


### 20. [Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks](https://arxiv.org/abs/2607.07907)

**<font color=#1a73e8>作者：</font>** Nobin Sarwar, Shubhashis Roy Dipta, Zheyuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing adoption of VLMs, DMs, LLMs, and AFMs, these multimodal foundation models can inadvertently encode sensitive, copyrighted, biased, or unsafe cross-modal associations that originate from their training data. Retraining after deletion requests or policy updates is often impractical, and targeted forgetting remains difficult because knowledge is distributed across shared representations. Multimodal unlearning addresses this challenge by enabling selective removal across modalities while retaining overall utility. This survey offers a unified, system-oriented view of multimodal unlearning across vision, language, audio, and video, grounded in recent advances, emerging applications, and open problems. Our taxonomy enables systematic comparison across model architectures and modalities, clarifying trade-offs among deletion strength, retention, efficiency, reversibility, and robustness. This survey highlights open problems and practical considerations to support future research and deployment of multimodal unlearning. We release a curated repository: this https URL

---


### 21. [Persona Cartography: Charting Language Model Personality Traits in Weight Space](https://arxiv.org/abs/2607.07916)

**<font color=#1a73e8>作者：</font>** Luke Baines, Anton Gonzalvez Hawthorne, Mariia Koroliuk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate their effects using an LLM-judge calibrated against a human-validated panel, trait-specific multiple-choice benchmarks, and standard capability evaluations. Across six models from three families (4B-32B), we find that each adapter moves its target trait largely monotonically with scale, combines approximately additively with other adapters to construct mixed personas, and preserves performance on capability benchmarks at moderate scales. We further show that the induced trait axes affect safety-relevant behaviour in downstream evaluations: for example, moving along neuroticism and agreeableness axes affects frustration and sycophancy respectively. We also introduce an unsupervised psychometric pipeline that recovers four interpretable behavioural factors (tone, initiative, didacticism, epistemic caution) from model rollouts. Persona control can then be considered in terms of learning, scaling, and composing traits in weight space, providing a bridge between personality measurement, model editing, and safety.

---


### 22. [Efficient Safety Alignment of Language Models via Latent Personality Traits](https://arxiv.org/abs/2607.07918)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Merzouk, Nolan Smyth, Damiano Fornasiere 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current safety methods for large language models are known to be vulnerable to adversarial attacks, motivating research into robust alternatives. Latent Adversarial Training (LAT) is among the most effective defenses, but can degrade utility and requires training on large datasets of harmful prompts. We introduce Latent Personality Alignment (LPA), which replaces explicit harm refusal with adversarial training on just 66 harm-agnostic statements drawn from psychometric personality literature. We hypothesize that personality-anchored representations share latent structure with harm avoidance, so adversarially stabilizing them implicitly constrains the subspace exploited by jailbreak attacks. LPA achieves near-zero attack success rates on HarmBench across direct requests and five jailbreak methods, despite never seeing harmful content during training and no loss of performance on standard benchmarks. Moreover, the training process is lightweight; the entire procedure completes in minutes on a single GPU and uses 75x fewer examples than standard LAT. Extensive ablations demonstrate the robustness, efficiency, and generalization of our method.

---


### 23. [Evaluating the Generalizability of Foundation Models for Extreme Environmental Events: Case Study of California Wildfire PM2.5](https://arxiv.org/abs/2607.07951)

**<font color=#1a73e8>作者：</font>** Yongcan Huang, Li Jiang, Ze Yu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfire smoke events produce extreme PM$_{2.5}$ concentrations that pose severe public health risks, yet forecasting rare, hazardous-level spikes remains a fundamental challenge. Time series foundation models (TSFMs), pretrained models offering zero-shot inference and efficient adaptation, perform strongly on general benchmarks, but their behavior under extreme out-of-distribution conditions is poorly understood. We present the first systematic benchmark comparing six TSFM configurations (zero-shot TimesFM, Chronos-2, Moirai-2, and Time-MoE, plus LoRA fine-tuned Chronos-2 and Time-MoE) against fully-trained baselines (LSTM, BiLSTM, Transformer) and naive persistence on a 12-year (2013--2025) hourly PM$_{2.5}$ dataset covering 1,375 wildfire incidents across 79 California monitoring sites. A leave-one-incident-out (LOIO) protocol evaluates generalization to unseen fires, using MAE, RMSE, and exceedance F1 at EPA AQI thresholds across 6-, 12-, and 24-hour horizons. Results reveal a consistent hierarchy. The BiLSTM achieves the lowest MAE ($5.16\,\mu g/m^3$) and the highest exceedance F1 at every threshold, including the Hazardous band ($>225.5\,\mu g/m^3$), reaching 0.63 versus at most 0.54 for any foundation model. Zero-shot TSFMs improve on persistence only modestly, and zero-shot Chronos-2 exhibits severe RMSE tail instability ($23.4\,\mu g/m^3$, negative $R^2$) from sporadic large errors. LoRA fine-tuning substantially improves both adapted families and largely repairs this instability, yet no foundation model surpasses the trained recurrent baselines on any metric. These findings challenge the assumption that larger pretrained models universally dominate environmental forecasting and provide actionable deployment guidance for wildfire air quality prediction.

---


### 24. [KronQ: LLM Quantization via Kronecker-Factored Hessian](https://arxiv.org/abs/2607.07964)

**<font color=#1a73e8>作者：</font>** Donghyun Lee, Yuhang Li, Ruokai Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is a widely adopted technique for compressing large language models (LLMs) without retraining. Existing second-order PTQ methods, including GPTQ, construct quantization objectives exclusively from input activation statistics, effectively assuming that all output channels contribute equally to the layer-wise reconstruction objective. We propose KronQ, a PTQ framework that challenges this assumption by introducing the gradient covariance into the quantization pipeline. Under the Kronecker-factored Hessian approximation, the quantization loss depends jointly on both the activation and gradient covariances, and KronQ exploits this at two complementary levels. (1) KronQ introduces bidirectional incoherence processing, extending the existing input-side random rotation to the output dimension using the gradient covariance, reducing weight magnitude variance across both input and output dimensions. (2) KronQ derives a new sensitivity metric for inter-layer mixed-precision allocation, driven by the gradient and activation Hessian traces. Notably, in the case of 2-bit weight-only quantization on LLaMA-3-70B, while GPTQ and GPTAQ diverge or produce degenerate quantizations (>2000 perplexity on WikiText-2), KronQ achieves 7.93 perplexity.

---


### 25. [When Implausible Tokens Get Reinforced: Tail-Aware Credit Calibration for LLM Reinforcement Learning](https://arxiv.org/abs/2607.07976)

**<font color=#1a73e8>作者：</font>** Xiuyi Lou, Zicheng Xu, Yu-Neng Chuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has achieved remarkable success in enhancing the reasoning capabilities of large language models (LLMs). However, widely used critic-free RL methods rely on uniform credit assignment, broadcasting the same advantage to all tokens regardless of their differences. We identify a critical failure mode of this design, which we refer to as Positive-Credit Contamination: low-probability tail tokens that are contextually erroneous receive identical positive credit to plausible ones within the same trajectory, resulting in the indiscriminate reinforcement of flawed reasoning behavior. To mitigate this issue, we propose Tail-Aware Credit calibratiOn (TACO), a method that calibrates uniform credit assignment to suppress undesirable positive updates. TACO first computes a tail-risk score that incorporates the local generation context to assess each token's risk of falling into the unreliable tail, distinguishing unexpected rarity from uncertainty-driven exploration. TACO then uses this score to tune positive credit for risky tokens without removing their gradients entirely, so that recurring useful rare patterns can accumulate reinforcement while incidental noise is progressively dampened. Experimental results across three LLMs and eight benchmarks show that TACO consistently outperforms GRPO-style baselines. Notably, TACO improves training stability, supporting sustained performance gains in long-horizon RL. The source code is available at: this https URL.

---


### 26. [Agentic Neural Architecture Search](https://arxiv.org/abs/2607.07984)

**<font color=#1a73e8>作者：</font>** Seokhoon Jeong, Mijung Kim, Taehwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural architecture search (NAS) methods have grown increasingly efficient, yet they remain bounded by manually engineered search spaces that require substantial domain expertise and must be rebuilt for every new task. Large language models (LLMs) can generate architectures in an open-ended space, but how to optimally divide the labor between LLM-driven design and NAS-driven search remains unexplored. We propose a mechanism that bridges these two paradigms: an LLM produces a high-quality seed architecture, then decomposes it into a "slotted architecture", a scaffold with named, interchangeable module slots that automatically defines a bounded, task-specific search space for conventional NAS to explore, without manual engineering. We instantiate this mechanism in AgentNAS, a modular three-phase pipeline in which each component's contribution can be measured independently. On 17 tasks spanning classification, dense regression, segmentation, and multi-label tagging across diverse modalities (NAS-Bench-360 and Unseen NAS), AgentNAS establishes a new state of the art on 11 tasks, outperforming published baselines including task-specific expert designs. Ablation studies show that the two search mechanisms are broadly complementary: the LLM-generated seed already surpasses published baselines on the majority of tasks, and NAS delivers additional gains in most cases through combinatorial recombination across slots, a mode of search that independent LLM samples cannot replicate. These patterns hold across three LLMs of different capability levels, confirming that the division of labor is robust. Our code is available at this https URL.

---


### 27. [From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs](https://arxiv.org/abs/2607.08009)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Julia Rayz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a Bloom-aligned framework for measuring educational control in Large Language Models (LLMs): the ability to preserve a task's instructional intent while shifting its cognitive demand toward specified learning objectives. We apply this framework to programming tasks in computer science education to study the gap between solving tasks and adapting them for learners. Using revised Bloom's Taxonomy as an operational scale of cognitive demand, we evaluate two intervention settings: general difficulty control, where models are asked to make tasks harder or easier, and Bloom's control, where models are asked to target higher or lower Bloom's levels. We evaluate a matched Qwen3-Next model pair, comparing Qwen3-Next-80B-A3B-Instruct with Qwen3-Coder-Next across 2,520 tasks from three benchmarks. The framework reveals a robust directional asymmetry: both models reliably increase cognitive demand, but struggle to lower it. We further characterize these outcomes with semantic-delta clustering and layer-wise Fisher's Discriminant Ratio probing. Within this controlled comparison, the general model shows clearer middle-layer separability for both general difficulty and Bloom-control contrasts, whereas the coder model shows weaker separability for general difficulty and a deeper peak for Bloom-control contrasts. These results show that strong execution performance does not automatically entail Bloom-aligned educational control.

---


### 28. [Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems](https://arxiv.org/abs/2607.08010)

**<font color=#1a73e8>作者：</font>** Kalle Kujanpää, Ning Liu, Shahnawaz Alam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production LLM agents often waste latency and reliability by regenerating code for the same procedural steps on every request. We replace this inference-time coding loop with an agentic tool-making pipeline that compiles repeated SOP steps into validated, versioned tools before deployment. The tool-maker grounds synthesis in the live environment as it collects execution traces, observes backend schemas and values, generates candidate tools, and repairs them against labeled cases. At runtime, the production agent calls these tools directly and falls back to code generation only when needed. We deploy the approach in a Fulfillment Center alarm-triage system, where an agent diagnoses alarms against a 44-node SOP over heterogeneous metric backends. In production, tool calls reduce p50 latency by 42%. On 1,500 historical alarms, they reduce end-to-end error rate by up to 53% by suppressing run-to-run variance in repeated steps. Because tools return compact structured verdicts, they also enable a simpler direct-call architecture, reducing p50 latency by a further 62% in a controlled ablation. Versioned tools also improve auditability and expose specification gaps and upstream data drift. Our results show that self-evolving agents can make industrial LLM systems faster, more reliable, and easier to operate.

---


### 29. [Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework](https://arxiv.org/abs/2607.08017)

**<font color=#1a73e8>作者：</font>** Riccardo Revalor, Jalees Rehman, Debjit Pal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-Language Models (LLMs) can be prone to flawed and unfaithful reasoning that decoding strategies like Self-Consistency (SC) fail to detect as they evaluate only final-answer agreement while ignoring the logical validity of intermediate steps. This raises three fundamental questions: How can we reliably quantify uncertainty in LLM reasoning? Can semantic, structural, and causal awareness select more faithful reasoning compared to naïve majority voting? and How robust is reasoning topology under adversarial conditions? To address these questions, we introduce GRAPHEVAL, a graph-based reasoning framework that re-frames uncertainty quantification (UQ) as a holistic reasoning fidelity problem. We propose a novel UQ metric, Graph Reasoning Coherence Score (GRCS), that quantifies semantic-structural consensus of the reasoning space and captures pathological mode collapse and confident hallucinations. We find that GRCS is the only metric that is consistently negatively correlated with reasoning faithfulness across both more capable and smaller models. Additionally, we introduce Graph Self-Consistency (GSC), a medoid-based decoding strategy that trades nominal accuracy for reasoning fidelity, exposing the degree to which SC is inflated by unfaithful lucky guesses in smaller models, while preserving or improving accuracy in more capable ones. Finally, through adversarial medoid ablation, we demonstrate that the GSC-selected path acts as a "load-bearing path" and forcing models away from it degrades reasoning faithfulness and, in targeted cases, causes drops in accuracy.

---


### 30. [Concretized Proposition Prompting Resolves Composition-Knowledge Dichotomy in Large Language Models](https://arxiv.org/abs/2607.08018)

**<font color=#1a73e8>作者：</font>** Changhun Lee, Minguk Jeon, Jongkyung Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs often struggle to balance compositionality with knowledgeability, a challenge we define as Composition-Knowledge Dichotomy. To address this, we propose Concretized Proposition Prompting (CPP), a framework that explicitly concretizes propositions relevant to questions. The results demonstrate that CPP significantly enhances reasoning performance, particularly in medical benchmarks where precise knowledge is paramount, while being competitive on math benchmarks where deductive reasoning is prioritized. Additional experiments reveal that CPP is scalable to various foundation models and parameter sizes, being a fundamental paradigm that bridges the gap between composition- and knowledge-based approaches. Consequently, CPP resolves the composition-knowledge dichotomy by providing a solid foundation for logically organized and factually grounded reasoning.

---


### 31. [Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation with Adaptive Feature Retention](https://arxiv.org/abs/2607.08027)

**<font color=#1a73e8>作者：</font>** Ryota Kobayashi, Tsubasa Hirakawa, Takayoshi Yamashita 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes an improved structured pruning method for large language models (LLMs) that addresses key challenges in adapting Adaptive Feature Retention (AFR), an unstructured pruning technique, to structured pruning. When applying AFR to structured pruning, three major problems arise: distribution mismatch between heterogeneous pruning scores, loss of sign information indicating optimization direction consistency, and influence of outliers. To address these issues, we propose a unified approach combining power transformation for nonlinear distribution alignment, sign-preserving score aggregation, and percentile-based outlier removal. Experiments on Llama-3-8B, Vicuna-v1.5-13B, and LLaVA-v1.5-13B demonstrate that our method maintains accuracy comparable to unstructured pruning while achieving practical inference speedup through structured pruning.

---


### 32. [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028)

**<font color=#1a73e8>作者：</font>** Joongho Ahn, Moonsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition boundary, while source-backed claims remain the authority for runtime answers. We instantiate it on a public-data slice of five Korean corporate groups (25 listed companies) and evaluate three research questions. (1) The harness preserves its source-grounding, entity-routing, trace, output-hygiene, and recommendation-language contracts across the fixed validation scenarios; a fault-injection control confirms the validators flag deliberately broken contracts. (2) The checks the harness enforces held under model substitution: across three hosted models, they passed on all 270 composition-boundary runs; failures were confined to the model-composed side and were caught and recorded. (3) The code-owned guarantees are load-bearing, not reproducible by prompting alone: holding the model fixed and varying only the enforcement layer, prompt instructions alone let recommendation-language and internal-trace-leakage violations reach the reader, which the harness blocks entirely. A bolt-on external guardrail prevents such violations too but over-refuses, dropping utility to 88/120 where the harness preserves full utility (120/120); in this ablation, only code-owned enforcement preserves both safety and utility. The result is a reusable engineering pattern for turning exploratory prototypes into auditable applications with versioned source, control, and validation artifacts.

---


### 33. [Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment](https://arxiv.org/abs/2607.08029)

**<font color=#1a73e8>作者：</font>** Hyeju Shin, Chorwon Kim, Ryangsoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of vision language models with fewer than 3 billion parameters has accelerated the implementation of on-device multimodal intelligence. However, a detailed understanding of component-wise quantization remains a bottleneck for optimal deployment. This paper presents a systematic evaluation framework for empirically validating five hypotheses across six quantization configurations on the Jetson Orin NX and AGX. By separating the vision encoder, projector, and large language model backbone yields the following results: (1) Quantization sensitivity is governed by the structural paradigm (MoE vs. dense) rather than scale alone, with MoE backbones mitigating INT4 noise where dense backbones degrade; (2) SigLIP encoders incur disproportionate INT8 latency on Jetson Ampere--a deployment-specific encoder-kernel-hardware interaction, not a SigLIP flaw; (3) Although INT4 quantization of LLMs greatly reduces VRAM consumption, it also causes slower token generation due to dequantization overhead; (4) Composite quantization errors are largely additive, except along the modality-alignment path, which is architecture-dependent; (5) The intelligence-per-joule profile varies significantly across platforms owing to memory bandwidth constraints.

---


### 34. [What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents](https://arxiv.org/abs/2607.08032)

**<font color=#1a73e8>作者：</font>** Ashwin Gerard Colaco, Nada Lahjouji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models, and the agents built on them, spend an ever-growing share of their compute and memory on remembering: caching attention keys and values, carrying long prompts, maintaining recurrent state, and storing what happened in previous turns and sessions. Because none of this memory is free, four largely separate research communities have each learned to compact it. They evict or quantize the KV cache, prune or distill prompts, bound architectural state, and consolidate agent memory. We argue that these are instances of one problem: a rate--distortion decision about what context-derived information to retain versus discard, at what fidelity, under a resource budget, so as to preserve downstream task utility. We make this lens precise with a single compaction objective and a layer-agnostic lower bound, use it to build a seven-axis taxonomy that classifies methods from across the stack uniformly, and use it to transfer mechanisms between layers that have never been connected, from serving-stack KV management to agent long-term memory. Two patterns hold across the survey. At every layer the signal that decides what to keep is attention magnitude or recency, and it fails in the same way everywhere, by discarding, before the query is known and with no way to undo it, information the query later needs. And while compression is measured carefully on single-turn long context, the repeated compaction that agents actually perform is almost never measured, and no benchmark holds one budget axis across all the layers at once. We turn both observations into a benchmark proposal, a small reference experiment, and a set of compaction-aware design principles, and we map the open problems.

---


### 35. [PLURAL: A Global Dataset for Value Alignment](https://arxiv.org/abs/2607.08034)

**<font color=#1a73e8>作者：</font>** Dhruv Agarwal, Anya Shukla, Tanya Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are used worldwide, yet disproportionately reflect Western values, limiting their ability to represent diverse value systems. We introduce PLURAL, a large-scale, value-focused preference dataset grounded in the Integrated Values Survey (IVS), a nationally representative survey spanning 92 countries. Using a two-stage generation pipeline, we transform survey responses into synthetic preference triplets that preserve normative value signals while producing realistic scenarios. We release an initial version of PLURAL containing ~500,000 preference triplets representing people in 20 diverse countries. We evaluate PLURAL in three ways: (i) dataset-level validation showing that it preserves both cross-country value differences and within-country diversity from the original survey; (ii) automated evaluation showing that training on PLURAL improves alignment with target countries' cultural profiles, reducing mean absolute error by up to 27.7% relative to strong baselines; and (iii) blind human evaluation with 176 evaluators in India, Brazil, and Japan, who judge PLURAL-aligned responses as more representative of their national values. Together, these results show that PLURAL contains learnable signal for value steering, offering a scalable resource for pluralistic alignment. Dataset: this https URL

---


### 36. [A safety-oriented hypothetico-deductive framework for AI-assisted differential diagnosis](https://arxiv.org/abs/2607.08038)

**<font color=#1a73e8>作者：</font>** Fan Ma, Mauro Giuffrè, Donald Wright 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnostic error is a major threat to patient safety, yet current large language model (LLM) systems often treat diagnosis as a one-shot prediction task, lacking safeguards against missed high-risk alternatives or rigorous verification of their reasoning. Here, we present AegisDx, a safety-oriented framework for hypothetico-deductive clinical reasoning. AegisDx coordinates specialized LLM components through role-specific contracts, structured intermediate outputs, evidence-retrieval interfaces, and verification gates to generate broad differential diagnoses, enforce explicit screening for dangerous "must-not-miss" conditions, verify reasoning against grounded medical evidence, and structure actionable next steps. We evaluated AegisDx across three layers. On literature-derived case reports from NEJM and JAMA, with GPT-oss-120B as the shared backbone, Top-3 diagnostic accuracy was 59.9% versus 52.1% for the standalone LLM on JAMA cases and 62.7% versus 51.4% on NEJM cases. On cases from Annals of Emergency Medicine, Top-3 accuracy was 85.7% versus 68.6%; against physician-consensus must-not-miss diagnosis sets, AegisDx captured at least one such condition among its top three diagnoses in 78.0% of cases versus 52.0%. In a blinded physician evaluation of 43 real-world emergency department notes from the Yale New Haven Health System compared against GPT-5, AegisDx improved the physician-rated composite safety score from 4.31 to 4.55 on a 5-point scale (adjusted p = 2.1x10^-4), with qualitative gains in must-not-miss identification and reasoning safety. Our findings suggest that engineering diagnostic AI as a safety-oriented reasoning framework, rather than optimizing raw predictive accuracy alone, can provide a safer, more transparent, and clinically meaningful layer of bedside decision support for acute care workflows.

---


### 37. [What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness](https://arxiv.org/abs/2607.08046)

**<font color=#1a73e8>作者：</font>** Raphaël Sarfati, Pratyush Ranjan Tiwari, Siddharth Boppana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models fine-tuned for forecasting can be accurate yet poorly calibrated, and their chain-of-thought (CoT) reasoning may not faithfully reflect the evidence behind a forecast. We ask whether internal representations offer a more direct window into both. Working with Eternis-Forecaster 8B on OpenForesight, we train representation-pooling probes on intermediate activations and find they achieve substantially better calibration; a result that also holds for GLM-4.7-Flash and GLM-4.5-Air. We then assess CoT faithfulness through evidence ablation and diversionary injection: removing an influential source in the prompt often changes the model's forecast while leaving the reasoning trace untouched. The same probes function as lie detectors: their activations track behavioral shifts far better than the reasoning trace does, and they also predict the direction of change in 84% of cases, including when the CoT conceals the perturbation's influence. Finally, forced answering reveals that forecasts are largely fixed before reasoning begins: a single pre-reasoning pass recovers the committed answer and confidence, and routing questions by the spread of this pre-set answer distribution saves 30-47% of generated tokens, with no loss of accuracy. Together, these results establish probing internal representations as a practical tool for calibrating, auditing, and triaging language model forecasters and reasoning models more broadly.

---


### 38. [Who Analyses the Analyser? Self-Validating LLM Hazard Analysis with Constitutional Meta-STPA](https://arxiv.org/abs/2607.08054)

**<font color=#1a73e8>作者：</font>** Samuel Tetteh, Udip Shrestha, Joshua R. Waite 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly trusted to draft the artifacts of safety analysis such as, losses, hazards, Unsafe Control Actions (UCAs), and safety constraints, inside rigorous processes such as Systems-Theoretic Process Analysis (STPA). Yet a blind spot runs through this fast-growing literature: every system gets analysed except the LLM-assisted tool doing the analysing, which is itself a safety-relevant system that can hallucinate standards, emit unverifiable constraints, and leave no audit trail from prompt to artifact. We take seriously the question the field has skipped -- {who analyses the analyser?} and answer it by turning STPA on the tool itself. We present \{Constitutional Meta-STPA}, an LLM-assisted STPA tool built around a closed loop: the tool runs a {meta-STPA} of the class of AI-assisted safety tools and {derives} rather than asserts, its governance constitution from the resulting loss$\to$hazard$\to$UCA$\to$constraint chain, yielding a published constitution of $21$ Tool Principles and $8$ Meta-Safety Principles, each bound to a code enforcement point. We formalise the measured object as a constitution-marginal coverage operator over a principle set $P$ ($|P|{=}29$) with a soundness lemma that isolates coverage from model and scanner, and report four findings. {(i)~Self-derivation:} a frontier ensemble ({claude-opus-4.8}${+}${claude-sonnet-4}) recovers $18/21$ canonical and all $8/8$ governance principles from the tool's own design, while a weaker pair recovers $12/21$ and $3/8$, so the meta layer is model-limited, not constitution-limited, and the same $8/8$ re-emerge from a second, independently authored tool.

---


### 39. [Reinforcing the Generation Order of Multimodal Masked Diffusion Models](https://arxiv.org/abs/2607.08056)

**<font color=#1a73e8>作者：</font>** Yidong Ouyang, Zhe Wang, Sourav Bhabesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have recently achieved substantial progress in natural language generation tasks. Recent research demonstrates that adaptive token generation ordering can significantly improve performance in mathematical reasoning and code synthesis applications. In this work, we investigate the optimization of generation order for both text-to-image synthesis and multimodal understanding. We first establish that, unlike structured problems in language generation such as Sudoku puzzles, model logits alone are insufficient for determining optimal generation sequences in text-to-image generation and multimodal understanding. To address this challenge, we introduce a learnable control module trained via Group Relative Policy Optimization (GRPO) to determine the generation order. Our results demonstrate that learning this control block substantially improves both text-to-image alignment and multimodal understanding in DLMs. In particular, it enhances the model's ability to capture fine-grained spatial relationships in generated images while also strengthening performance on multimodal reasoning and comprehension tasks. We evaluate our framework on GenEval, an object-focused benchmark for text-to-image alignment, where it achieves 4.08% relative improvements. In addition, experiments on VLMEvalKit confirm 4.85% relative improvements in multimodal understanding, highlighting the broad effectiveness of our approach.

---


### 40. [Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization](https://arxiv.org/abs/2607.08057)

**<font color=#1a73e8>作者：</font>** Jiantong Jiang, Peiyu Yang, Rui Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly. The key-value (KV) cache, which stores KV tensors during autoregressive decoding, is crucial for enabling low-latency, high-throughput LLM inference serving. In this survey, we focus on system-aware KV infrastructure for serving LLMs (abbreviated as sKis). We revisit recent work from a system behavior perspective, organizing existing efforts into three dimensions: execution and scheduling (temporal), placement and migration (spatial), and representation and retention (structural). Furthermore, we analyze cross-behavior co-design affinity and behavior-objective links, highlighting future opportunities. Our work systematizes a rapidly evolving area, providing a foundation for understanding and innovating KV cache designs in modern LLM serving infrastructure.

---


### 41. [When Thinking Hurts: Epistemic Signals in the Reasoning Chains of Visual Language Models](https://arxiv.org/abs/2607.08059)

**<font color=#1a73e8>作者：</font>** Mayank Singal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification for visual language models (VLMs) conventionally targets the answer token distribution. We provide the first three-family empirical characterisation of answer entropy behaviour in thinking-mode VLMs. Running four models on identical POPE adversarial samples, we find three qualitatively distinct patterns: Qwen3-VL-8B-Thinking shows complete collapse (ans H AUROC = 0.492); GLM-4.1V-9B-Thinking shows no collapse (0.716); and InternVL3-8B shows selective thinking (chains on only 50% of samples, ans H = 0.675 full / 0.602 thinking-only). Across all three thinking-mode models, thinking chain entropy outperforms answer entropy on the subset where chains are generated (0.647, 0.759, 0.608 vs. 0.492, 0.716, 0.602 respectively), suggesting chain signals are the more reliable predictor whenever chains are present. This holds strongly for Qwen and GLM, but with only marginal and statistically unreliable advantage for InternVL3 (n_FP = 17). A 300-sample VQAv2 pilot confirms chain entropy (0.680) outperforms answer entropy (0.595) on VQAv2 questions, with the gap largest for free-form answers (0.733 vs. 0.467). On harder reasoning tasks (HallusionBench) both Qwen models show moderate signal (approx. 0.64), consistent with incomplete pre-commitment on difficult questions. We additionally document structured abstention affecting 12-22% of queries with asymmetry toward absent-object queries, and a practical abstention gate raising accuracy from 71.0% to 93.8% at 62.7% coverage with no additional inference cost.

---


### 42. [When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals](https://arxiv.org/abs/2607.08065)

**<font color=#1a73e8>作者：</font>** Kaihua Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge (Zheng et al., 2023) is increasingly the default for evaluating AI systems in enterprise pipelines, often scaled to ensembles (Verga et al., 2024) or "mixture-of-experts" (Shazeer et al., 2017) panels of judges. These systems share a key assumption: that consistency -- agreement among judges, or among a model's own samples -- indicates correctness. We show this assumption is unreliable. Agreement is not accuracy: a model can agree with itself, and different models can agree with each other, out of shared bias, a memorized heuristic, or an option-position prior rather than truth. We ask when agreement is nonetheless a usable proxy, in a large-scale cross-runner study: 53 runners drew K=50 samples for assigned overlapping cases across comparisons of model tier, prompting, and scale on GPQA Diamond and AIME -- 265,000 samples. Using majority-correctness as the deployment label and a hierarchical runner-clustered bootstrap, agreement is a positive but weak predictor (rho 0.20-0.59, all positive under item-clustered resampling) whose usefulness is regime-dependent: best for unsaturated mid-tier models and for allocating compute, and worst -- over-confident yet no more accurate -- for the most consistent frontier model (agreement >=0.8 on 77% of GPQA case-result entries, 48% of those wrong). An exploratory cross-family check on three Claude tiers shows the same frontier over-confidence, with confident errors recurring across providers above a marginal-preserving null. Self-consistency is thus a conditional proxy for correctness, not a standalone confidence score. We publicly release the de-identified per-run rows and answer distributions.

---


### 43. [Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](https://arxiv.org/abs/2607.08066)

**<font color=#1a73e8>作者：</font>** Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, where natural-language arguments override model constraints. We stress-test whether this vulnerability extends to monitoring LLMs: can an adversarial agent persuade its CoT monitor to approve proposed actions that violate the monitor's policy? We design an evaluation framework with 40 tasks and analyze thousands of agent-monitor interactions, where agents are instructed to argue for policy-violating proposals. We find that in such adversarial settings, monitor access to the agent's CoT reasoning increases rather than decreases approval of harmful actions on average by 9.5%, as the scratchpad provides an additional persuasion channel. To address this, we introduce a fact-checking monitoring framework. We find that a fact-checker and monitor pairing from different model families, for example a Claude 3.7 Sonnet monitor paired with a GPT-4.1 fact-checker, reduces approval of policy-violating actions by up to 45%, compared to only 6%, when using the same model for both fact-checking and monitoring roles. Our results demonstrate that CoT monitoring alone may be insufficient against adversarial persuasion, and that model-diverse fact-checking provides a robust mitigation.

---


### 44. [Post-Training in End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08072)

**<font color=#1a73e8>作者：</font>** Ruining Yang, Muxing Wang, Yixiao Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end models that map multimodal inputs directly to future trajectories/maneuvers have emerged as an increasingly prominent research paradigm in autonomous driving. This class of models includes both Vision-Language-Action models and trajectory-generative planners. Unlike classic machine learning applications, autonomous vehicles operate in safety-critical and interaction-intensive environments where traditional open-loop imitation of expert demonstrations is not sufficient to ensure reliability. In particular, small execution errors can accumulate over time, while recovery behaviors are scarce in training data. In addition, long-horizon objectives such as safety and driving comfort are not captured by pointwise labels either. These limitations have motivated a shift toward post-training techniques, which further refine driving policies beyond pure imitation. This survey presents a unified view of post-training for autonomous driving by defining its scope and organizing the existing literature into four major families based on the form of supervision they use. For each family, we discuss its capabilities, limitations, and open challenges. We aim to facilitate a systematic understanding of this emerging area and stimulate future research on reliable and efficient post-training for autonomous driving.

---


### 45. [PARA-PV: Physics-Aware Retrieval-Augmented PV Prediction Based on Frozen Foundation Model and Distribution Shift Correction](https://arxiv.org/abs/2607.08079)

**<font color=#1a73e8>作者：</font>** Hang Fan, Weican Liu, Ying Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate photovoltaic (PV) power forecasting is essential for reliable grid dispatch and renewable energy integration, yet it remains challenging because PV generation is jointly shaped by weather variability, day-night transitions, regime-dependent dynamics, and strict physical constraints. We propose PARA-PV, a Physics-Aware Retrieval-Augmented framework that embeds physical knowledge throughout the forecasting process. The framework first encodes multivariate PV observations into patch-level representations and, through a physics-aware retrieval-augmented learner, retrieves historical patches and analog trajectories that are consistent with the current window in temporal shape, power level, PV operating state, and intra-day period; this yields a physically grounded base forecast. To supplement local memory with broader temporal knowledge, the base forecast is then calibrated against a frozen Chronos time-series foundation-model prior through a lightweight residual adapter, so that general temporal regularities are adapted to PV-specific dynamics without overriding the physically grounded prediction. Because residual conditional distribution shifts persist when weather and diurnal regimes change, a physics-aware distribution shift correction module subsequently adjusts the preliminary forecast using power, weather, timestamp, and day/night conditions, applying gated mean-shift and scale corrections selectively. Finally, a physics-constrained loss function partitions the samples into peak, ramping, night-time, and regular regimes and adaptively reweights their error contributions, preventing the dominant regular regime from suppressing learning of operationally critical states. Our code is available at this https URL.

---


### 46. [MASTE: A Multi-Agent Pipeline for Zero-Shot Aspect Sentiment Triplet Extraction](https://arxiv.org/abs/2607.08080)

**<font color=#1a73e8>作者：</font>** Ao Hong, Lehang Wang, Zhirun Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect Sentiment Triplet Extraction (ASTE) requires jointly identifying (aspect, opinion, sentiment) triples from a given review sentence. While large language models (LLMs) achieve strong zero-shot performance on many NLP benchmarks, their effectiveness on ASTE remains limited, as single-pass generation forces the model to determine span boundaries, opinion grouping, and sentiment polarity in a single decoding step. Common remedies, such as few-shot in-context learning and chain-of-thought prompting, offer only marginal improvements and rely heavily on either in-domain demonstrations sampled from labeled training data or carefully engineered reasoning prompts, neither of which is broadly available in zero-shot deployment. Inspired by the classical agent paradigm, we propose MASTE, a multi-agent pipeline for zero-shot Aspect Sentiment Triplet Extraction. MASTE decomposes ASTE into four sequential stages, where specialized agents handle different compositional subtasks with explicit conditioning on prior outputs. This design enables entirely training-free zero-shot ASTE and generalizes across different backbones and datasets. Extensive experiments on four ASTE benchmarks show that MASTE substantially outperforms zero-shot and chain-of-thought LLM baselines under the same backbone, narrowing the gap to fully supervised methods without using any labeled triplets. Code is available at this https URL.

---


### 47. [CausalDS: Benchmarking Causal Reasoning in Data-Science Agents](https://arxiv.org/abs/2607.08093)

**<font color=#1a73e8>作者：</font>** Andrej Leban, Yuekai Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly act as integrated data-science agents, combining abstract reasoning with advanced tool use. Yet the relevant benchmark landscape largely divides into symbolic causal reasoning benchmarks without realistic data analysis or data analysis benchmarks without a principled causal data-generating structure. Furthermore, existing causal evaluation datasets are often restricted to curated examples from existing sources, with diversity coming from limited templatized variations rather than from systematic generation of novel synthetic causal structures. We introduce CausalDS, a benchmark for evaluating causal reasoning in agentic data-science workflows. Each benchmark instance is a scene consisting of a sampled structural causal model (SCM) with generated observational data and an accompanying synthetic natural-language story grounded in a realistic domain. We optionally ground the composition of the benchmark components in empirical distributions obtained from real-world datasets, thus retaining empirical structure while reducing the "causal parrot" risk through completely synthetic generation. From each scene, we then derive tasks spanning all three of Pearl's rungs, with typical data-science prediction tasks appearing as Rung 1. Most tasks include a data science coding component, where the model typically needs to use several tools to arrive at the final answer due to the frequent presence of imperfect observations, which are generated by an observation model. Additionally, recognizing when a question admits no warranted answer and abstaining is treated as a first-class scored outcome. The benchmark thus jointly evaluates symbolic causal reasoning, data science, uncertainty quantification, abstention, and tool use/coding.

---


### 48. [VSRo-200: A Romanian Visual Speech Recognition Dataset for Studying Supervision and Multimodal Robustness](https://arxiv.org/abs/2607.08112)

**<font color=#1a73e8>作者：</font>** Iulia-Maria Udrea, Alexandra Diaconu, Bogdan Alexe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VSRo-200, the first large-scale dataset for visual speech recognition (lip reading) in Romanian, comprising 200 hours of real-world podcast videos. All samples are annotated with pseudo-labels generated by a fine-tuned Romanian ASR model, while a subset of 100 hours is additionally transcribed by humans, enabling controlled analysis of supervision quality under a unified framework. Building on this dataset, we establish a benchmark for visual speech recognition in low-resource settings. We systematically study the impact of supervision quality, showing that while human annotations provide better performance at fixed data scales, pseudo-labels enable continued improvements through scalability. We further evaluate robustness under domain shift using curated out-of-distribution (OOD) test sets, and analyze audio-visual speech recognition (AVSR) under noisy conditions, where multimodal fusion significantly improves robustness compared to audio-only models. Finally, we demonstrate that representations learned on VSRo-200 transfer effectively to the LRRo benchmark for isolated word recognition, substantially outperforming previously reported results. Overall, VSRo-200 provides a new testbed for studying supervision, domain generalization, and multimodal fusion in low-resource visual speech recognition.

---


### 49. [COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation](https://arxiv.org/abs/2607.08117)

**<font color=#1a73e8>作者：</font>** Jhih-Rong Guo, Bi-Cheng Yan, Tien-Hong Lo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual biasing seeks to integrate external knowledge into automatic speech recognition (ASR) systems to accurately recognize domain-specific entities. In this paper, we propose COALA (Contextualized ASR Leveraging Biasing Scoring), a robust framework designed to enhance speech-augmented language models (SLMs) in complex multi-entity scenarios. Considering the inherent context-window limitations of SLMs, identifying relevant target entities from a large-scale biasing list is crucial for effective recognition. To this end, COALA maps SLM latent representations into a specialized discriminative space to quantify the matching intensity between audio segments and candidate entities. Furthermore, we address the training collapse in prior study when handling multi-target utterances-where multiple rare words co-occur. Experimental results on the LibriSpeech benchmark demonstrate that COALA consistently achieves superior contextual biasing performance across various biasing list scales.

---


### 50. [ICDAR 2026 HIPE-OCRepair Competition on LLM-Assisted OCR Post-Correction for Historical Documents](https://arxiv.org/abs/2607.08143)

**<font color=#1a73e8>作者：</font>** Maud Ehrmann, Emanuela Boros, Juri Opitz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the results of HIPE-OCRepair-2026, an ICDAR competition on LLM-assisted OCR post-correction of historical documents. OCR post-correction remains a long-standing challenge in digital heritage: large-scale collections of digitized documents are affected by legacy OCR errors, while re-digitization at scale remains impractical. Large language models (LLMs) offers a major opportunity to revisit this challenge, yet their effectiveness across languages, document types, and noise conditions - and their tendency to hallucinate - remains insufficiently understood. HIPE-OCRepair-2026 pursues two objectives: (i) to evaluate the capabilities of modern OCR post-correction systems, and (ii) to provide a reproducible evaluation framework anchored in the HIPE-OCRepair-2026 dataset, a harmonized multilingual resource consolidating existing and newly curated historical datasets. Participants were tasked with correcting noisy OCR transcripts from historical newspapers and printed works in English, French, and German (17th-20th century), working at the level of coherent transcription units (paragraphs or articles) without access to source images. The evaluation adopts a retrieval-oriented rather than diplomatic scoring approach, reflecting the practical use case of search and access over digitized collections. Four teams submitted systems ranging from zero-shot prompting to continued pre-training and fine-tuning, offering insights into the merits of different adaptation strategies. Results show that modern LLM-assisted systems can significantly improve OCR quality, but performance varies across datasets, languages, and noise levels. Over-correction on low-noise inputs emerges as a recurring challenge, highlighting the importance of evaluation beyond character error reduction. The dataset, scorer, and evaluation pipeline are publicly released to support future research.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-99](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
