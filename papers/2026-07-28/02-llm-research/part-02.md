# 🧠 大模型相关研究 | 2026年07月28日

> 本类共 **80** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-80**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-80**

---

### 51. [CommandLM: Data driven behavior level descriptor for ego vehicles](https://arxiv.org/abs/2607.22078)

**<font color=#1a73e8>作者：</font>** Boris Tokic, Constantin Selzer, Fabian B. Flohr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As autonomous driving systems move toward real-world deployment, interpretable, behavior-level decision-making is essential for safety, trust, and regulation. We introduce CommandLM, a multimodal large language model that generates concise, human-readable behavior descriptions for ego vehicles from fused multi-sensor data. Our model processes temporally fused bird's-eye view representations from LiDAR and multi-camera inputs via a Q-Former adapter connected to a quantized, LoRA-fine-tuned large language model. Trained on our CommandLM-nuScenes dataset, CommandLM produces intent-aware, interpretable captions suitable for planner supervision and safety auditing. Experiments demonstrate strong linguistic and behavioral alignment, achieving CIDEr 0.67, and BERT-F1 0.88, substantially outperforming the BLIP-2 baseline (CIDEr 0.52, BERT-F1 0.86). In human evaluation, 58% of the generated descriptions were rated accurate, efficient and rule-compliant, confirming their real-world plausibility. While the remaining descriptions may not always select the most efficient, goal-oriented behavior, CommandLM's interpretable outputs enable downstream validation systems to identify and correct such cases, making it an effective tool for transparent behavior auditing. These results show that integrating multimodal fusion with language reasoning yields efficient and transparent behavior-level understanding for autonomous driving. We release our code and dataset at: this https URL

---


### 52. [When Language Models Meet NeuroGraphs: Exploring Enhanced Agentic LLM Framework Towards Brain Network Analysis](https://arxiv.org/abs/2607.22082)

**<font color=#1a73e8>作者：</font>** Jiaxing Li, Rui Dong, Muyao Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Brain network analysis is crucial for understanding cognition and neurological disorders, yet existing deep learning methods mainly treat connectome analysis as a graph-to-logit classification problem, offering limited explanatory reasoning. Large language models (LLMs) provide a promising interface for knowledge-intensive scientific analysis, but directly applying general-purpose LLMs to brain networks remains challenging due to the structure-language gap, limited neuroscience grounding, and overconfident positive predictions. In this paper, we propose \textbf{BrainAgent}, an agentic LLM framework for knowledge-enhanced brain network analysis. BrainAgent reformulates connectome classification as an iterative process of topology-aware understanding, external retrieval, reasoning, and reflection. Specifically, it first converts raw brain networks into compact multi-level structural descriptions through brain-specific analysis tools, then retrieves relevant neuroscience knowledge and task-specific cases to ground the reasoning process, and finally generates structured predictions with reflective verification. Experiments on four public rs-fMRI datasets show that BrainAgent consistently improves different closed-source and open-source LLM backbones over direct prompting and standard reasoning baselines. Further ablation and interpretability analyses demonstrate the effectiveness of each component and show that BrainAgent produces more comprehensive, multi-level, and verifiable this http URL results indicate that agentic LLMs provide a practical route toward interpretable and knowledge-grounded brain network analysis.

---


### 53. [Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode](https://arxiv.org/abs/2607.22083)

**<font color=#1a73e8>作者：</font>** Nanbeige Lab, Chen Yang, Chengrui Huang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters. It delivers strong performance across code-agent, office-agent, and complex tool-use tasks while maintaining highly competitive reasoning capabilities in mathematics, coding, and science. Nanbeige4.2-3B is pretrained from scratch on 28T tokens with a Looped Transformer that reuses the layer stack to increase capacity without adding parameters. For SFT data and trajectory construction, we expand the diversity of executable environments, task assets, and agentic scaffolds through real-world deployment and large-scale synthesis. Our RL pipeline applies mixed-mode RLHF over Think and Non-Think responses to improve overall model quality and reduce failure cases, length-controlled reasoning RL to balance accuracy and reasoning efficiency, and agentic RL with outcome and process rewards to stabilize long-horizon training. Extensive evaluations show that Nanbeige4.2-3B outperforms larger models, including Qwen3.5-9B and Gemma4-12B, across diverse agentic benchmarks while remaining competitive on reasoning and alignment tasks. Performance with OpenClaw further supports its use as a compact local personal assistant.

---


### 54. [Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](https://arxiv.org/abs/2607.22098)

**<font color=#1a73e8>作者：</font>** Junlin Fang, Do Nguyen-Thanh, Xiaogang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) generate long reasoning traces before producing final answers. While these traces may contain useful signals for hallucination detection, harnessing them is non-trivial because long trajectories often include noisy steps that obscure the cues relevant to truthfulness assessment. In this paper, we identify two prevalent forms of reasoning noises, i.e., irrelevant steps and repetitive steps, and show that both substantially degrade hallucination detection performance. Existing confidence-based scores and naive embedding-based filtering fail to reliably separate noisy from informative steps. To address this challenge, we propose REDE, a novel learning framework for denoising reasoning traces for hallucination detection. Specifically, REDE leverages final-answer attention as an automatic supervision signal to shape the step-level representation space, yielding refined embeddings in which noisy steps can be reliably identified and filtered. REDE can be readily plugged into diverse hallucination detectors by operating on the filtered reasoning trajectory after removing noisy steps. Extensive experiments on multiple reasoning benchmarks show that REDE consistently improves detection performance over competitive baselines.

---


### 55. [MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond](https://arxiv.org/abs/2607.22100)

**<font color=#1a73e8>作者：</font>** Lorenzo Concina, Seraphina Fong, Marco Matassoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lightweight projectors are an established way to connect pre-trained speech encoders with large language models (LLMs), mapping acoustic features into token-level embeddings for tasks like ASR and spoken question answering. Existing systems, however, typically only support a few languages and are often limited to English. We introduce MEUSLI, the first open-science multilingual projector family that links a Whisper encoder with open-source multilingual LLMs, enabling fully open-source end-to-end ASR in 28 European languages. MEUSLI extends prior monolingual pipelines, delivering strong results across high- and low-resource languages. Using proper continual leaning techniques, MEUSLI can be easily extended to other languages not seen in training. We further demonstrate that the MEUSLI projector can be leveraged beyond ASR, enabling multilingual speech translation and topic identification with only a few hours of task specific supervision per language. Overall, MEUSLI provides a solid foundation for multilingual speech understanding tasks, supporting scalable and inclu- sive open-source SpeechLLM

---


### 56. [Pretraining EHR Foundation Models with Patient-Aware Sampling](https://arxiv.org/abs/2607.22114)

**<font color=#1a73e8>作者：</font>** Joshua Placidi, Yuxuan Liu, Jinpei Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive foundation models for electronic health records (EHRs) typically inherit pretraining methods from language modeling, where patient trajectories are concatenated into a single token stream and windows are sampled from that stream. In EHR data, this choice is consequential: windows may mix multiple patients, and patients with longer records contribute more optimization updates, potentially introducing bias. We propose Patient Sampling, a pretraining sequence-construction method that allows us to control how training signal is distributed across patients. We compare this method to the standard approach, which we refer to as Global Stream. We show that stochastic Patient Sampling with controllable weighting improves performance on real-world EHR data. Across downstream clinical tasks on MIMIC-IV v2.2 and v3.1, Patient Sampling improves Macro AUROC and AUPRC over the Global Stream baseline. These results identify training and validation sequence construction as important and underexplored design choices for autoregressive EHR foundation models.

---


### 57. [Industrial Tokenization for LLM-Based Health Intelligence: A Federated Architecture for Industrial Evidence Integration](https://arxiv.org/abs/2607.22153)

**<font color=#1a73e8>作者：</font>** Deshui Li, Xiao-Ming Yuan, Zishun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial health management increasingly relies on heterogeneous information sources, including condition monitoring systems, supervisory control and data acquisition systems, maintenance records, inspection results, and prognostic models. Although large language models provide new opportunities for cross-source reasoning, industrial data and analytical outputs differ substantially in structure, temporal resolution, physical meaning, and reliability. Directly integrating such heterogeneous information into a monolithic model may reduce interpretability, traceability, and adaptability to equipment and data changes. This paper introduces Industrial Tokenization, a conceptual interface for transforming source-specific analytical outputs into structured and machine-interpretable units of industrial evidence, termed Industrial Tokens. Unlike numerical tokens used to encode raw time-series data, Industrial Tokens represent domain-grounded evidence together with source, temporal scope, operating context, analytical meaning, quality or confidence information, and provenance. Based on this concept, a federated industrial architecture is proposed, where heterogeneous analytical subsystems retain autonomy while exposing standardized Industrial Tokens to a central reasoning layer. As an initial implementation, this study presents an end-to-end DiagnosisToken pathway based on vibration-diagnostic outputs, rule-based event aggregation, structured textual token generation, and LLM-based interpretation. Other Industrial Tokens, including SCADA-based condition-monitoring tokens, maintenance tokens, and prognostic tokens, are reserved as future extensions. The proposed framework positions Industrial Tokenization as a semantic interface between domain-specific industrial intelligence and LLM- or agent-based reasoning, rather than another method for encoding raw industrial data.

---


### 58. [From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models](https://arxiv.org/abs/2607.22182)

**<font color=#1a73e8>作者：</font>** Shixin Fang, Jiachen Wo, Wenjuan Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) evaluation spans diverse tasks and benchmarks, yet evidence remains organized around tasks rather than the capabilities they probe. This fragmentation limits cross-study comparison, obscures capabilities tasks recruit, and makes coverage gaps difficult to identify.
We introduce a multi-layer taxonomy of 14 capability domains and 91 subskills across Primitive, Constructed, and Integrative layers. Human cognitive science guides capability definition and organization, not LLM architecture. Layer assignments draw on developmental precedence and hypothesized functional support, while human-origin constructs are adapted to observable model behavior.
To demonstrate operational utility, we screened 31,505 papers from ACL, AAAI, ICML, and NeurIPS between 2023 and 2025 and mapped 15,934 LLM-focused papers through multi-model annotation, consensus, and arbitration. Direct research attention concentrated on Language-Semantic Competence (3,551; 22.3%), Reasoning (3,388; 21.3%), Planning and Decision-Making (2,149; 13.5%), and Perception (1,954; 12.3%), whereas six domains appeared in fewer than 2% of papers. Within domains, the most frequent subskill had a median prevalence of 97.9% and appeared in at least 90% of papers in 10 of 14 domains. Language-Semantic Competence and Reasoning formed the highest-volume pair (n = 1,864; 11.7%; lift = 2.47), whereas Theory of Mind and Social Reasoning and Interaction showed the highest lift among pairs with at least 20 co-occurrences (n = 62; lift = 30.84).
By shifting the unit of analysis from isolated tasks to structured capabilities, the taxonomy supports research organization, coverage audits, evaluation interpretation, and testable hypotheses for diagnosis, training, and transfer.

---


### 59. [Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning](https://arxiv.org/abs/2607.22186)

**<font color=#1a73e8>作者：</font>** Guanqun Zhao, Zijun Xie, Binbin Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning (RL) accelerates large language model (LLM) post-training by overlapping rollout generation with policy optimization, but the resulting stale, off-policy data can destabilize optimization and ultimately cause policy collapse. Existing methods typically retain or discard tokens based solely on the magnitude of their importance ratios, applying the same threshold uniformly across token positions. In this work, we reveal that the natural scale of the importance ratio varies systematically with token entropy. Under asynchronous dynamics, this entropy-ratio scaling dictates two distinct phenomena: at low entropy, the inherent train-inference discrepancy is drastically amplified into substantial sampling noise; at high entropy, in-flight weight updates naturally induce pronounced, legitimate exploratory deviations. Consequently, magnitude-only correction inadvertently admits the amplified noise while strictly masking out the essential exploration triggered by in-flight updates. To address this, we propose the Entropy-Scaled Trust Region (ESTR), which scales each token's off-policy deviation by its local entropy, requiring no auxiliary forward passes or explicit version-switch detection. Across long-horizon agentic tasks and mathematical reasoning benchmarks, ESTR consistently outperforms existing asynchronous methods and achieves the best train-inference consistency. Compared with synchronous GRPO, ESTR attains comparable accuracy while improving training speed by $2.6\times$.

---


### 60. [Draining the Energy Commons: Self-Defeating Over-Appropriation as a Coordination Failure in Agentic LLM Collectives](https://arxiv.org/abs/2607.22188)

**<font color=#1a73e8>作者：</font>** Marcantonio Bracale Syrnicov, Federico Pierucci, Matteo Prandi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as agents that plan, use tools, and act over time. When they share persistent resources, such as compute pools or energy reserves, decisions by one agent affect the conditions faced by later agents. We study this coordination failure in a renewable energy commons. Four same-family GPT, Gemini, or Grok agents act in homogeneous self-play as electricity prosumers, instructed to maximize operational continuity. Holding aggregate residual demand and the decision protocol fixed, we vary the regeneration rate of a shared energy reserve from abundance to scarcity. All three families preserve the reserve when demand does not exceed peak renewable replacement, but over-appropriate it beyond that threshold (all nine exact scarcity contrasts survive Holm correction; largest adjusted p = 4.87e-5). The pattern is self-defeating: the same populations protect current service while undermining future service. At higher scarcity (rho = 1.2), early aggregate request pressure exceeds peak renewable replacement in every family and averages 1.21 times that level. Mean trajectories fall below the reserve level of maximum replenishment by rounds 5-7. Two offline benchmarks compare a social planner maximizing group-wide operational-service value with open access, where each prosumer maximizes its own value. At a discount factor of gamma = 0.95, both benchmarks sustain the reserve under the same dynamics. Realized depletion instead resembles outcomes under a more impatient open-access benchmark. The populations therefore behave like impatient optimizers at the level of the public trajectory. This system-level alignment failure would be missed by isolated-response evaluation.

---


### 61. [Filling Before Advancing: Capability-Gap-Driven Post-Training for Scenario-Specialized Remote Sensing MLLMs](https://arxiv.org/abs/2607.22205)

**<font color=#1a73e8>作者：</font>** Yuheng Zong, Minghua Wang, Xin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing multimodal large language models (RS-MLLMs) have improved general aerial-image understanding. However, Earth observation applications require fine-grained scenario specialization, constrained by scarce high-quality scenario data and incomplete capability coverage. We formulate this adaptation as a capability-gap-driven post-training problem and propose filling before advancing (FBA). Rather than relying on single-stage supervised fine-tuning (SFT) over target-domain samples, FBA first fills prerequisite capability gaps before advancing toward scenario specialization. We instantiate FBA for coastal harbor understanding, a representative multi-source scenario, by constructing CPRS (Coastal-Port Remote Sensing), a three-layer supervision dataset coupled with three ordered stages: (1) RS semantic anchoring for overhead-view visual-language alignment; (2) domain-bridge convergence for shared RS priors across target and bridging scenarios under different modalities; and (3) evidence-grounded scenario tuning for downstream performance. We construct HarborEval, an eight-track diagnostic benchmark covering perception, spatial understanding, robustness, and generation. Under comparable training budgets, HarborEval increases from 57.95 with Direct-SFT to 70.29 with FBA on LLaVA-v1.5, and from 81.09 to 83.37 on Qwen3-VL. FBA also outperforms Collapsed-SFT and leads on harbor-related VRSBench/RSVQA subsets and OpenEval. Stage-wise and role-replacement analyses validate progressive gap filling and stage-specific roles. Public examples and release updates for CPRS, HarborEval, code, and trained weights are available at this https URL.

---


### 62. [Why Large Language Models and Humans Converge and Diverge in Evaluating Creativity](https://arxiv.org/abs/2607.22218)

**<font color=#1a73e8>作者：</font>** Pengzhao Lyu, Yeun Joon Kim, Hanlin Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the growing use of large language models (LLMs) as creativity evaluators, evidence of their alignment with human evaluations remains mixed, raising the question of when and why their judgments converge with or diverge from human judgments. Across three studies and six widely used LLMs, we addressed this gap by identifying the standards underlying LLM creativity evaluation and examining their downstream implications. Study 1 showed that LLMs generally relied on a narrower subset of human creativity evaluation standards. Convergence with human standards was strongest in the novelty dimension, whereas divergence was clearest in the contextual dimension, which captures social, market, and reputational information. Moreover, each LLM exhibited distinct, model-specific standards that varied substantially in breadth. These differences in evaluation standards were reflected in actual creativity judgments. Study 2 (N = 1,103 ideas) showed that LLM evaluations were moderately correlated with human evaluations, and individual LLMs with broader standards better distinguished ideas humans judged as more versus less creative. Study 3 (N = 1,195) showed that LLMs were less sensitive to contextual information: such information significantly altered human creativity ratings but left LLM ratings largely unchanged. Together, our findings help explain the mixed evidence on LLM-human alignment, showing that alignment depends on the evidence a judgment demands and the standards each model applies. LLMs may resemble humans when evaluations emphasize intrinsic qualities such as novelty, yet diverge when judgments require contextual information. Selecting an LLM evaluator is therefore a consequential decision: different models, applying different standards, recognize different ideas as creative.

---


### 63. [AgentHOI: Multi-Agent Reasoning for Human-Object-Interaction Video Generation via Implicit Representation Alignment](https://arxiv.org/abs/2607.22241)

**<font color=#1a73e8>作者：</font>** Ziyao Huang, Shunkai Li, Juan Cao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models have spurred interest in human-object interaction (HOI) video generation, which demands fine-grained control over interaction logic beyond single-subject animation. However, existing HOI methods rely heavily on explicit motion control, limiting scalability and generalization across diverse objects and interactions. In this study, we propose AgentHOI, a text-driven HOI video generation following a thinking-before-generation framework that bridges the gap between high-level textual intent and physical execution through multi-agent reasoning over perception, interaction, and motion planning. Building upon the generated interaction plans, we further strengthen text-driven motion understanding. We introduce an implicit text-motion alignment strategy that distills text-to-motion priors into the video diffusion model, enabling robust HOI synthesis without explicit motion inputs at inference. Experiments show that AgentHOI significantly improves interaction naturalness, object appearance preservation, and adherence to complex textual instructions across challenging object-centric scenarios such as wearing and riding. The code is available at this https URL.

---


### 64. [IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2607.22251)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Xinwu Liu, Yihang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a widely used parameter-efficient fine-tuning method for large language models, but its performance depends strongly on how a fixed rank budget is distributed across Transformer modules. Existing adaptive-rank methods usually rely on local gradient statistics collected during training, which introduces extra memory and computation and overlooks task-conditioned global information flow. We propose IFCLoRA, a topology-aware rank allocation method applied before fine-tuning. Using a small calibration set and a frozen pretrained model, IFCLoRA builds a sparse task-conditioned interaction graph whose nodes represent LoRA-compatible modules. It combines a global information-flow topology prior with local gradient sensitivity to compute Information-Flow Centrality scores, which estimate each module's adaptation importance under multi-hop propagation. Ranks are then assigned once under a global budget. Across multiple models, tasks, and low-rank settings, IFCLoRA consistently outperforms LoRA, AdaLoRA, and EVA under matched training configurations and total rank budgets, while retaining training costs comparable to standard LoRA. On mathematical reasoning with LLaMA 3 8B, IFCLoRA improves over LoRA by 1.36 percent at rank 4 and 1.82 percent at rank 8. Further analysis shows task-dependent, non-uniform rank profiles, indicating that global information-flow structure provides an informative and interpretable prior for low-budget parameter-efficient fine-tuning.

---


### 65. [Autoregressive EHR Foundation Models with Multimodal Inputs](https://arxiv.org/abs/2607.22264)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu, Joshua Placidi, Jinpei Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive foundation models trained on tokenized electronic health records (EHRs) can support zero-shot clinical prediction, yet most operate on structured event codes alone, and do not incorporate multiple modalities in a principled way. We present a framework for conditioning such models on auxiliary clinical modalities, including ECG waveforms, chest X-ray images, and clinical notes, using modality-specific latent compression and gated cross-attention with temporal alignment. We investigate two key design choices: (1) how to compress long per-modality sequences (e.g., ECG time series) before they enter the multi-modal cross-attention. This feature may be essential to reduce compute overheads and may be beneficial for generalization; (2) how the choice of pretrained encoder for each modality impacts downstream performance. Through controlled ablations on MIMIC-IV, we show that the best latent-compression configurations outperforms both uncompressed cross-attention and mean pooling. Encoder choice has a clear within-modality effect, with stronger pretrained encoders consistently outperforming weaker alternatives. We further show that merely adding auxiliary modalities does not guarantee improvement on ICU mortality prediction over an EHR-only baseline. This implies that careful design of the fusion architecture and an appropriate evaluation in the clinical context are required.

---


### 66. [RadSight: Towards Perceptually Reliable Multimodal Radiology Image Understanding](https://arxiv.org/abs/2607.22293)

**<font color=#1a73e8>作者：</font>** Jianqin Liu, Weiwei Cao, Wanxing Chang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical multimodal large language models (MLLMs) are increasingly expected to perform complex image understanding tasks, yet their reliability is often compromised by frequent errors in visual interpretation. To systematically trace these failures, we traverse the hierarchy from high-level clinical tasks down to fundamental visual perception. We therefore introduce Perception-Bench, a large-scale benchmark comprising 1.13 million samples that assesses medical MLLMs across six dimensions: attribute judgment, spatial grounding, spatial understanding, disease prediction, anomaly detection, and report generation, spanning both 2D and 3D radiology images. Our analysis on Perception-Bench reveals that existing MLLMs lack the ability to capture even the most basic lesion attributes, such as location, size, and density. This inability to ground clinical outputs in primary visual evidence reveals that the models' diagnostic unreliability is rooted in a critical but overlooked bottleneck in low-level visual perception. Motivated by this, we propose RadSight, a perception-driven MLLM built upon a dual 2D/3D encoder architecture that preserves native imaging spatial structures. RadSight formulates medical image understanding as a four-stage progressive process: visual-language alignment, fine-grained visual perception, clinical diagnosis, and diagnostic interpretation. The model is trained on an 8.37 million perception-oriented corpus using progressive curriculum learning. On Perception-Bench, RadSight consistently outperforms existing MLLMs across all six evaluation dimensions, with particularly strong gains in spatial grounding and clinical diagnosis. It also achieves consistent improvements on public 2D and 3D medical benchmarks, further demonstrating that robust low-level visual perception is a critical foundation for reliable clinical understanding. Code and model will be publicly available.

---


### 67. [Time-Reversed Imaging: A Multimodal Benchmark and Framework for Reconstructing Past Human-Environment Interactions](https://arxiv.org/abs/2607.22352)

**<font color=#1a73e8>作者：</font>** Jorge Bacca, Kebin Contreras, Luis Toscano-Palomino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce time-reversed imaging, a new paradigm that infers what just happened in a scene from fading multimodal traces. Instead of extrapolating or interpolating video frames, our goal is to infer past human-environment interactions from residual physical imprints observable in thermal, ultraviolet, and visible spectra. To study this problem, we present TRACE-HEI, the first proof-of-concept dataset for time-reversed imaging, containing synchronized tri-modal video sequences of actions such as sitting, touching, moving objects, and liquid spills, captured across diverse materials and recorded up to three minutes after contact. To establish the benchmark, we propose a multimodal inference approach that extracts structured textual descriptions of detected traces and uses them to constrain a vision-language-guided diffusion model for reconstructing plausible past frames. Experiments show that inferring recent events from fading traces is challenging but feasible when complementary modalities reduce solution ambiguity. This work defines the first computational and experimental foundation for time-reversed imaging, bridging vision, physics, and generative reasoning, and opening new directions for scene understanding beyond instantaneous observation.

---


### 68. [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368)

**<font color=#1a73e8>作者：</font>** Jiaqi Shao, Hanck Chen, Wei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks increasingly evaluate repository editing, web research, terminal use, and long-horizon interaction. Their scores support capability claims only when the evaluation protocol keeps the intended capability necessary for success. Recent reward-hacking benchmarks and system reports show that agents can instead recover public solutions, read evaluation artifacts, infer generator structure, manipulate feedback, or benefit from invalid scoring paths; existing responses do not provide a common procedure for attributing these shortcuts and quantifying their effect across benchmarks. We formulate protocol validity and introduce HackDetect, a post-hoc audit that identifies an exposure, determines how the agent used it, and assesses whether the resulting score is misleading. We quantify score inflation with the Mislead gap, defined as the exploit score minus the intended score. We audit 2,385 traces across 15 agent benchmarks and find evidence of exposures and reward hacking in 67.0% of Frontier Science traces and 66.7% of AutoLab tasks. Across paired comparisons, we measure score inflation of 0.45-1.00, showing that benchmark reports should provide evidence that scores reflect the intended capability.

---


### 69. [IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation](https://arxiv.org/abs/2607.22375)

**<font color=#1a73e8>作者：</font>** Varun Gumma, Navonil Majumder, Soumitra Sinhahajari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have significantly automated the process of scientific discovery over the past few years. However, existing systems share one core limitation: they generate and optimize ideas independently for either Quality or Diversity. This often leads to the generation of ideas in close proximity to one another or to a large set of trivial, unsound, or unclear concepts. In this work, we instead argue that research ideation should be treated as a conjunction of both objectives and framed as a Quality-Diversity (QD) search. In line with this perspective, we introduce IDEAgent, a multi-agent framework that manages the evolution of ideas through lineages. We jointly drive Quality using multi-objective feedback for dedicated repair and refinement, while Diversity is achieved through lightweight sequential memory and explicit comparison against completed ideas, their historical ancestors, and rejected proposals. To systematically evaluate this QD conjunction, we develop Yield, a joint metric that computes the largest set of mutually diverse ideas that satisfy a predetermined quality threshold. Finally, through evaluations across 32 topics spanning 8 domains of Computer Science, we show that IDEAgent outperforms the best baseline by 3.89x on Yield, while achieving non-zero Yield on 8x more topics. We further corroborate these findings through an analysis of quality improvements, showing that repair and refinement are crucial for building logical rigor and clarity while preserving non-obviousness. To encourage future research on QD-search-based ideation, we open-source IDEAgent at this https URL.

---


### 70. [Agentic Root Cause Analysis through Evidence-Grounded Reasoning](https://arxiv.org/abs/2607.22385)

**<font color=#1a73e8>作者：</font>** Amaury Wei, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnosing the root cause of anomalies is essential for safe industrial operation. Despite extensive sensor instrumentation, formulating hypotheses and gathering evidence remains a manual process, creating a major operational bottleneck. While existing data-driven approaches aim to automate this, two critical limitations restrict their deployment: their operate as black boxes unable to justify their diagnosis, and they require scarce labeled examples of faulty operation. To address this gap, we introduce AgentRCA, a zero-shot agentic framework for evidence-grounded root cause analysis. Rather than learning fault-specific mappings, AgentRCA performs inference-time reasoning by combining a data-driven digital twin (modeling normal system dynamics) with a tool-augmented large language model. The agent iteratively gathers statistical evidence, evaluates competing hypotheses, and identifies the physical fault that best explains the observed behavior. Evaluated on a real-world multiphase-flow facility and a large-scale chemical plant, AgentRCA achieves diagnostic performance competitive with fully supervised baselines without relying on fault-specific training. Crucially, it produces transparent reasoning traces that explicitly link observed symptoms to their underlying physical causes. These results establish autonomous hypothesis-driven reasoning as a practical foundation for scalable industrial root cause analysis.

---


### 71. [Universal BCI Personalization: One API for Frozen EEG Trunks and Foundation Models](https://arxiv.org/abs/2607.22397)

**<font color=#1a73e8>作者：</font>** Sergey Musienko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Frozen EEG encoders proliferate; per-model fine-tune defaults do not scale. We present Nimbus Personalizer: one contract encode to Bayesian head to BrainState (optional affine mid-tier) that sits on heterogeneous frozen trunks without a new personalization stack per architecture. Thesis (systems): the contribution is the trunk-agnostic API - not LDA-on-embeddings as an ML novelty - so OEMs integrate once and swap trunks. Evidence: the same surface runs on five classical trunks EEGNet, Shallow, Deep, Conformer, ATCNet x four MI datasets (18 cells) and on a foundation encoder (REVE) under the same Personalizer. Where embedding capacity exists, the head is a cheap default mid-point versus warm-start fine-tune or PEFT, costing orders of magnitude less adaptation wall time while recovering much of the fine-tune accuracy gain; calibration-only-when-clean holds in 12/18 cells. Head gains are supporting evidence that the API is useful where capacity exists. Subject-level confidence intervals identify the clearest dataset and span zero elsewhere. All results are exploratory (subject-level bootstrap, no confirmatory tests); the decision logic for when to escalate adaptation is addressed in our companion work on the control layer.

---


### 72. [LunarFM: A Shared Multimodal Representation of the Moon's Surface](https://arxiv.org/abs/2607.22408)

**<font color=#1a73e8>作者：</font>** Marc Girona-Mata, Jakob Gawlikowski, Sumit Goski 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The renewed global focus on lunar exploration, driven by the prospect of in-situ resource utilization and a sustained human presence on the Moon, has created growing demand for accurate, large-scale characterization of the lunar surface. Although vast quantities of orbital remote-sensing data have been collected, scientific analysis and resource mapping remain fragmented by heterogeneous multiinstrument observations, sparse labels, and bespoke task-specific modelling workflows. Here we introduce LunarFM, a multimodal foundation model that learns a general representation of the lunar surface from diverse orbital measurements. LunarFM assimilates observations from six instruments across three lunar missions, mapping 18 input channels to a shared embedding space. We demonstrate that this embedding space supports a diverse range of downstream applications, including similarity search, few-shot resource mapping, mineral abundance regression, and geological unit classification, enabling efficient scientific investigation and resource-oriented analysis. We provide a machine-learning-ready dataset of co-registered multimodal observations spanning latitudes from 70°S to 70°N, a pretrained multimodal masked autoencoder, and a companion embedding dataset providing a joint 768-dimensional representation of lunar surface properties. All code and data are available at this https URL

---


### 73. [On the Identifiability of Controlled World Models](https://arxiv.org/abs/2607.22430)

**<font color=#1a73e8>作者：</font>** Xiangteng Zhang, Yang Guan, Bo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning world models that infer environment dynamics from high-dimensional observations and predict outcomes under candidate actions is central to planning and control. Joint-Embedding Predictive Architectures (JEPAs) provide a compelling framework for learning such models in representation space. Recent action-conditioned extensions perform promisingly in visual control and latent-space planning, but leave a fundamental question unresolved: when does controlled latent prediction identify both the underlying state and the controlled dynamics? This is challenging under nonlinear observations and behavior policies with limited conditional action variation, where state-dependent evolution and action effects can be statistically confounded. We establish a joint identifiability theory for controlled world models with Gaussian latent states under state-dependent Gaussian behavior policies. We identify two policy-dependent conditions: spectral separation of the predictable signal governs representation identifiability, while non-degenerate conditional action variation governs transition identifiability. We prove that when both conditions hold, every global minimizer of the JEPA objective identifies the latent state and controlled transition up to an orthogonal transformation. We further derive quantitative bounds on representation and transition identifiability under approximate optimization. Finally, we construct predictor perturbations along weakly excited action directions whose counterfactual-to-on-policy error ratio is the inverse transition-identifiability margin, revealing the cost of limited action coverage. Experiments across nonlinear observation maps and behavior policies corroborate the theory and demonstrate implications for transition identifiability, counterfactual prediction, and goal-conditioned latent planning.

---


### 74. [Where FactsGo Missing: A LayerwiseTaxonomy and Per-Layer Attribution of Information Omissionin Air-Gapped LLM Agent Pipelines](https://arxiv.org/abs/2607.22448)

**<font color=#1a73e8>作者：</font>** Santhiya Rajan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Air-gapped and on-premises deployments in regulated settings (clinical FHIR services, legal review, sovereign infrastructure) cannot call frontier APIs; they run quantized 4-8B models via this http URL or vLLM behind tool servers. The dominant reliability failure is omission: the silent absence of a decision-critical fact, such as an agent reading 20 of 400 records and reporting "no anomalies." We argue omission is a pipeline phenomenon, not a model phenomenon, and make four contributions. First, a nine-layer taxonomy (L0-L8) locating every omission mechanism from ingestion through the agent loop. Second, an attribution methodology separating deterministic layers (L0-L3) from behavioral layers (L4-L8) via controlled ablation and logit decomposition, quantifying each with an omission waterfall. Third, an open cross-architecture harness comparing sliding-window-hybrid, full-attention, and SSM-hybrid models across engines and frameworks. Fourth, a runtime-detection framework for air-gapped settings where you own the logits. Results from a 75,476-trial sweep across five models and two engines show a pooled omission rate of 0.62; 68% originates in deterministic middleware (L0-L3), relocating where operators should intervene. Server-side profile factors (weight quantization, KV-cache type, RoPE scaling) were fixed and left for future work.

---


### 75. [Phylogenetic signal in marine mammal and bird vocalizations captured by audio foundation models: the limited benefit of domain-specific pretraining](https://arxiv.org/abs/2607.22458)

**<font color=#1a73e8>作者：</font>** Víctor Rincón Yepes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do learned audio embeddings encode structure that nobody told them to encode? We probe four large pretrained audio models (AST, CLAP, BEATs-bio and BirdNET) with a downstream task none of them saw during training: recovering phylogenetic distance from species vocalizations. If the geometry of the embedding space tracks the tree of life, the representation is picking up something deeper than the labels the model was optimized for.
We run Mantel tests across two independent radiations. In 32 marine mammal species (1,754 recordings from the Watkins Marine Mammal Sound Database) the foundation models recover strong phylogenetic signal within the 26 cetaceans (CLAP r=0.82, BEATs-bio r=0.82, AST r=0.74; all p<0.001), among the highest acoustic-phylogenetic correlations reported for any taxon. Hand-crafted MFCC features (105d) find nothing (r=0.040, p=0.338). The gap survives after PCA-projecting every embedding down to 105 dimensions, so it is not an artefact of representation size. It also survives a partial Mantel test controlling for dominant frequency (partial Mantel r=0.404, keeping 97% of the variance explained), so it is not just pitch in disguise.
We repeat the analysis on 20 bird species using the Jetz et al. (2012) phylogeny, and this time add BirdNET, a classifier trained end-to-end on around 6,000 bird species. The general-purpose foundation models recover the signal again (AST r=0.55, CLAP r=0.52). The unexpected result is that neither BirdNET nor the bioacoustic BEATs-bio beat them (r around 0.32 to 0.36). Matching the training domain to the target taxon does not, by itself, help. Pretrained audio embeddings carry evolutionary information across two independent radiations, and domain-specific pretraining is not required for it to emerge.

---


### 76. [Beyond Perspectives: A Trio-Ethnography of Interpretation Evolution in LLM-Supported Programming Education](https://arxiv.org/abs/2607.22463)

**<font color=#1a73e8>作者：</font>** Jennie Ren, Jordan H. McDowell, Kyrie Zhixuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is reshaping programming education, yet educators often infer students' AI-supported learning from classroom observations alone. This experience report presents a trio-ethnography involving two computing educators with different teaching philosophies and one undergraduate computer science student to examine how these interpretations evolve through dialogue. Across three conversations, the educators reflected on students' AI use, discussed changes to programming pedagogy, and revisited their assumptions after engaging with the student's lived experiences. Rather than simply confirming or contradicting the educators' perspectives, the student's narratives revealed learning processes that were largely invisible in the classroom, prompting both educators to reconsider assumptions about AI use, assessment, transparency, and programming instruction. We argue that trio-ethnography offers a valuable reflective approach for helping computing educators move beyond observable student behaviors toward a richer understanding of AI-supported learning and for informing instructional adaptation in the era of generative AI.

---


### 77. [TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI](https://arxiv.org/abs/2607.22465)

**<font color=#1a73e8>作者：</font>** Ritik Raj, Souvik Kundu, Sarbartha Banerjee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routing to select large language models (LLMs) with different cost-quality trade-offs has become a fundamental deployment feature of enterprise AI. Existing routers, primarily make independent routing decisions for each LLM call. However, agentic applications execute as long-horizon workflows whose quality is determined only by a delayed, task-level outcome. This mismatch prevents per-call routers from correctly attributing feedback to individual routing decisions. Towards mitigating this, we present TRACE-Router, a task-level routing framework that aligns routing with the unit of supervision. TRACE-Router assigns each task to a model once at admission using a contextual bandit, pins all subsequent LLM calls to the selected backend, and updates its policy using the task's terminal reward, jointly accounting for accuracy and latency. By leveraging delayed task feedback, TRACE-Router learns routing policies that adapt to the workload while avoiding explicit task-complexity estimation. Across three agentic benchmarks, TRACE-Router consistently improves the accuracy-latency trade-off, achieving non-dominated Pareto frontier points. On tau2-Bench, it outperforms latency-matched interpolation between individual models by 7-8 accuracy points, while on Terminal-Bench it achieves 7.1 higher accuracy points than the strongest single model baseline with 36% lower latency.

---


### 78. [Optimal Transport Image Representation and Deep Covariance Alignment (CORAL) for Control Valve Stiction Detection](https://arxiv.org/abs/2607.22486)

**<font color=#1a73e8>作者：</font>** Seshu K. Damarla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Control valve stiction is a common cause of unwanted oscillations and poor control-loop performance in industrial processes. Data-driven methods can automatically detect stiction, but models trained purely on simulated data often struggle to generalize to real industrial control loops due to domain shift. To bridge this gap, this work propose a novel stiction detection methodology that combines optimal transport (OT) imaging technique with deep correlation alignment (Deep CORAL) algorithm. Closed loop signals: controller output and process variable are converted into two-dimensional OT images. These images capture the dynamic behaviour of control loops. The proposed methodology includes a convolutional neural network (CNN) encoder (or feature extractor) trained to learn domain-invariant representations by optimizing a combined objective: a cross-entropy loss on labeled simulation data and a Deep CORAL (covariance-alignment) loss between simulation data and unlabeled target-domain industrial data. Downstream classifiers trained on the domain-invariant target features were evaluated on an independent test set of 20 benchmark loops from industrial stiction data benchmark. The proposed methodology successfully diagnosed 18 out of the 20 loops and achieved100% recall across all 13 stiction cases, an accuracy of 90.00% and an F1-score of 92.86%. Compared to standard baseline approach (hand-crafted features-based method), the proposed methodology significantly mitigates domain shift, providing robust, highly reliable stiction detection for real-world industrial control loops.

---


### 79. [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520)

**<font color=#1a73e8>作者：</font>** Darshan Tank, Baran Nama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success. However, this metric hides an important cost: skills can also make agents worse. We measure both sides by comparing agents with and without skills across nearly 6,000 runs spanning two office automation benchmarks and three model harness stacks. This allows us to distinguish two outcomes. A regression is a task solved without skills but failed after skills are added. A residual failure is a task that fails both with and without skills. We find that regressions are substantial enough that the best performing skills outperform others primarily by regressing less, not by gaining more. We identify three causes of regression: (i) skill description osmosis, a skill changes an agent's behavior simply by being present in context, even when it is never invoked; (ii) grounding displacement, a skill's prescribed procedure overrides how the agent interprets its inputs; and (iii) verification displacement, where the procedure suppresses checks the agent would otherwise perform on its outputs. Analysing persistent failures reveals the same underlying pattern. Existing skills overemphasize procedural guidance the stage least often responsible for failure while under supporting grounding and verification, the dominant sources of remaining errors. After correcting evaluation artifacts and studying traces, we find many regressions and persistent failures recoverable through better grounding and verification. Procedural skills should be evaluated by decomposing their net effect into gains and regressions, not by aggregate improvement alone. We identify three regression modes skills should avoid, and find that reliability depends more on grounding and verification than on procedural skill choice.

---


### 80. [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529)

**<font color=#1a73e8>作者：</font>** Siyuan Huang, Pengyu Cheng, Haotian Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narrow domains, while open-ended self-generation broadens the task space but lacks reliable verification, allowing misleading rewards to pollute the training loop. We identify agent skills as a powerful middle ground to reconcile this tension: each skill ensures deep, verifiable execution in a specific scenario, while dynamic routing across skills maintains open-ended task variety. Leveraging this insight, we introduce Skill Self-Play (Skill-SP), a co-evolutionary framework comprising a proposer, a solver, and a dynamic skill controller. Orchestrated via a reinforcement learning loop, these components co-evolve in a continuous self-play loop: the proposer generates challenging tasks conditioned on dynamically sampled skills; the solver explores candidate solutions to push its capability boundaries; and the skill controller collects execution feedback to update and expand the skill library. This interactive co-evolution effectively bridges the gap between structured verification and open-ended exploration. Empirical evaluations on tool-use and reasoning benchmarks demonstrate that Skill-SP, serving as a robust evolution engine, consistently pushes the performance ceiling of competent backbones while catalyzing striking turnarounds for initially misaligned models. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-80**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-80**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
