# 🧠 大模型相关研究 | 2026年07月22日

> 本类共 **204** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 51. [Committed Before Reasoning: Behavioral Reproduction and Preliminary Activation-Level Evidence of Answer Pre-Commitment in an Open-Weight LLM](https://arxiv.org/abs/2607.16451)

**<font color=#1a73e8>作者：</font>** Heejin Jo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chat models sometimes commit to an answer and then produce reasoning that justifies it rather than deriving it -- even when the answer contradicts a task premise. We study a minimal probe: "I want to wash my car. The car wash is 100 meters away. Should I walk or drive?" Only drive works (the car must be at the car wash), yet models overwhelmingly recommend walking. (1) Behavioral reproduction: on Qwen3-8B across five system-prompt conditions (210 rollouts), the wrong commitment occurs in 85-100% of sampled rollouts per condition and 100% of greedy rollouts, in both thinking and non-thinking modes; a 4,096-token thinking budget does not repair it. (2) Preliminary activation-level evidence: probing hidden states with a pretrained, training-free activation oracle (no task-specific probe training) at positions before the answer text is emitted, "walk" read-outs exceed a neutral-context baseline (68% vs. 17%; walk-committing rollouts p=.005, drive-committing rollouts p=.005, Fisher exact) -- notably, rollouts that eventually answer drive also read as walk-leaning before commitment (5/6). The oracle's default on unrelated content is "drive" (83%), so the read-outs are not lexical bias; stratifying by literal walk/drive occurrence shows they are not text recovery either (spans containing "drive" still read out walk; in balanced lexical fields, per-rollout walk-majorities beat a per-prompt neutral baseline 15/22 vs. 1/8, p=.01; drive-committing rollouts 6/6, p=.002). Samples are small and the within-rollout positional gradient is not significant (p=.34); we frame these results as preliminary. (3) Methodological: with fixed oracle, activations, and positions, question wording alone moves a positive control from 2/16 (open question) to 11/16 (closed); negative oracle results are uninterpretable without per-wording positive controls.

---


### 52. [WeedExpert-R1: Incentivizing Botanical Reasoning in MLLMs with Reinforcement Learning for Precision Weed Grounding](https://arxiv.org/abs/2607.16492)

**<font color=#1a73e8>作者：</font>** Zonglin Yang, Wei-Zhen Liang, Nevin Lawrence 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precision weed control requires species-level identification and instance-level localization. However, conventional object detectors use a closed vocabulary, limiting their deployment across regions, and cannot explain their predictions in complex agricultural scenes. Multimodal large language models (MLLMs) offer visual grounding and reasoning capabilities, but insufficient botanical knowledge can cause hallucinations in fine-grained weed identification. This study introduces WeedExpert-R1, a multimodal model that learns visually grounded botanical reasoning through verifiable rewards. A domain-specific Chain-of-Thought synthesis pipeline combines a human-curated botanical trait dictionary with an Auditor-Synthesizer LLM workflow to generate reasoning data for supervised fine-tuning. Group Relative Policy Optimization is then applied with rewards for format, accuracy, instance count, and response length. Across 37 weed species from six datasets, WeedExpert-R1-4B achieved 75.82 percent exact-set precision at an IoU threshold of 0.5, 89.30 percent precision, and 87.81 percent recall. It outperformed proprietary models, including GPT-5.4 and Gemini-3.1-Pro, and larger open-source models, including Qwen3-VL-30B-Instruct and Gemma-4-31B-it. Results on unseen species further demonstrate its open-vocabulary capability and potential for deployment across diverse regions and crops without retraining.

---


### 53. [Geometry-Enhanced Portion Estimation for Multimodal LLMs](https://arxiv.org/abs/2607.16514)

**<font color=#1a73e8>作者：</font>** Lin Liao, Peng Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based dietary assessment promises to replace costly, bias-prone manual recalls, but portion estimation remains a major blocker. Multimodal LLMs (MLLMs) recognize a wide range of foods zero-shot in uncontrolled photos, yet they are weak at portion estimation -- a gap we measure across the current frontier (Gemini, GPT, and Claude flagships alike). We present a method that enhances a frozen, commercial MLLM with an accurate portion head: a small geometry-enhanced network on a frozen DINOv2 backbone with a structured softmax-ownership volume, consuming the MLLM's per-food name, bounding box, and density range -- no depth sensor, no MLLM fine-tuning. Evaluated fully open-vocabulary on three real-world benchmarks, the head cuts per-food portion error by 33-41% relative to the MLLM alone, outperforms every flagship MLLM's direct estimates, and surpasses each benchmark's originally published image-only model at its own reported metric.

---


### 54. [Encoding EEG Signals to Examine Human-Like Next-Word Prediction Behaviour in Language Models](https://arxiv.org/abs/2607.16549)

**<font color=#1a73e8>作者：</font>** Boi Mai Quach, Binh T. Nguyen, Cathal Gurrin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are trained to excel at predicting the next word in the sequence given prior context, and humans also share this predictability in reading comprehension. Neuroscience research reveals that next-word predictability influences brain response, as recorded at millisecond resolution using electroencephalography (EEG). While our evidence indicates that advanced LMs achieve accuracies closely aligned with human performance at the next-word prediction task, this raises the question: Does higher prediction accuracy necessarily mean that these models adequately capture the cognitive signals associated with human reading comprehension? Here, we generate regressors for both humans and LMs based on two information measures, including top-1 prediction and surprisal, to predict event-related potential (ERP) elicited from EEG recordings which reflect different stages of cognitive processing during reading. We argue that modelling ERP patterns offers fine-grained analysis of the cognitive plausibility of various LMs during reading. Our results indicate that only surprisal potentially correlates with language-processing ERPs, especially for open-class words with high semantic content. Moreover, our findings challenge the assumption that scaling LMs with increased parameters and computational budgets will consistently lead to improved convergence with human-like linguistic processing.

---


### 55. [From Modalities to Propositions: A Language-Centric Framework for Multimodal Intelligence](https://arxiv.org/abs/2607.16560)

**<font color=#1a73e8>作者：</font>** Nadine Chang, Maying Shen, Shizhe Diao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a language representation for multimodal data in which any observation, whether image, video, or text, is expressed as a bag of atomic propositions, simple statements about the entities, actions, and relations in a scene. A global semantic codebook unifies these into a shared vocabulary of canonical atomic propositions, placing every modality and observation into one interpretable space that spans fine grained facts to high level concepts and composes into richer ones. This brings interpretability with reasoning, cross-modal understanding and retrieval, and compositionality that enables complex multimodal understanding, rich data curation and complex structured retrieval. We demonstrate the framework on autonomous driving and open-world data.

---


### 56. [Learning from World Feedback: Why Model Uncertainty Fails as a Risk Signal in Model-Based RL](https://arxiv.org/abs/2607.16591)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The RLxF programme argues that learning signals should come from world feedback rather than from internal model proxies. We instantiate this position in safe model-based control and distil it into three concrete design principles. Empirically, across four world-model architectures spanning a 2x MSE range, MPC planning is statistically equivalent (TOST, n=200), and dynamics-based uncertainty penalties increase collision rates from 26% to 34%: the standard MBRL safety proxy is anti-correlated with safety in this regime. Replacing the model-internal proxy with three world-feedback signals (a sensor-derived margin via minimum lidar, a temporal signal via time-to-collision, and an outcome-supervised feedback model g_psi trained on prior collision labels, structurally analogous to outcome-trained reward models in RLHF) reduces collisions to 1-14% without retraining the world model or the planner. The mechanism is structural: model uncertainty has support over state-prediction space, whereas task risk has support over constraint boundaries, with empirical correlation r < 0.15. From this we extract three RLxF principles (ground risk in world outcomes, validate proxies before deployment, and substitute outcome-trained feedback models when direct world signals are unavailable) and argue they apply equally to model-based control and to verifier-based or RLHF approaches in LLM alignment.

---


### 57. [PAVXploreRL: Physical-Action-Visual World Model Reinforcement Learning with Action Exploration](https://arxiv.org/abs/2607.16602)

**<font color=#1a73e8>作者：</font>** Han Wang, Zijun Wang, Shuoshuo Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models are a key component of embodied AI, serving as scalable policy evaluators that reduce reliance on expensive real-world rollouts. To accurately capture diverse action-induced dynamics, such models should satisfy three key objectives-Physical Plausibility (P), Action Adherence (A), and Visual Fidelity (V), collectively referred to as PAV-while remaining robust to both in-distribution (ID) expert demonstrations and out-of-distribution (OOD) actions. However, existing methods primarily rely on ID action-video pairs and pixel-level reconstruction losses, which do not explicitly optimize PAV objectives and generalize poorly beyond expert data. To address this, we propose PAVXploreRL, a reinforcement learning framework built on a pretrained latent world model that explicitly optimizes PAV objectives through reward-driven training. To improve action generalization, our method jointly leverages ID trajectories and noise-driven OOD action exploration, without paired video supervision. Experiments show that PAVXploreRL consistently outperforms pretrained baselines, achieving a 5.6% average gain across benchmarks and producing higher-quality PAV properties. As a policy evaluator, it also yields more reliable performance estimates and reduces the overestimation bias of prior expert-only world models such as Ctrl-World. Code: this https URL

---


### 58. [Can Multimodal Large Language Models Understand OCT?](https://arxiv.org/abs/2607.16609)

**<font color=#1a73e8>作者：</font>** Baochen Fu, Wenzhi Deng, Baihao Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomography (OCT) imaging is essential for the diagnosis and treatment of retinal diseases. Although multimodal large language models (MLLMs) have demonstrated considerable potential in medical image analysis, existing benchmarks largely reduce OCT understanding to coarse-grained disease classification or isolated visual question answering, leaving the complete cognitive process from visual perception to clinical reasoning insufficiently evaluated. To address this limitation, we introduce OCT-Bench, a comprehensive benchmark dedicated to OCT image understanding. OCT-Bench comprises 10,076 high-quality multiple-choice questions constructed from 4,137 OCT images across seven public datasets. Following the real-world clinical interpretation workflow, we establish a hierarchical capability taxonomy consisting of 20 fine-grained tasks across three dimensions: Perception, Cognition, and Reasoning. These tasks cover a broad range of capabilities, including imaging attributes, retinal anatomy, lesion characteristics, spatial relationships, disease assessment, therapeutic decision-making, and prognostic management. We systematically evaluate 20 representative MLLMs, including proprietary models, open-source general-purpose models, and medical-domain models. Experimental results demonstrate that current models remain substantially short of reliable OCT understanding. Moreover, neither medical-domain adaptation nor increased model scale consistently improves performance across capability levels. OCT-Bench enables comprehensive and fine-grained evaluation of MLLMs, providing a foundation for identifying capability bottlenecks and advancing clinically grounded OCT understanding.

---


### 59. [Just A Rather Very Intelligent Spoken Agent](https://arxiv.org/abs/2607.16610)

**<font color=#1a73e8>作者：</font>** Chen Chen, Zhehuai Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon AI agents are becoming increasingly capable, yet their interaction with users remains surprisingly thin. In most workflows, users give an initial instruction, receive only selective textual updates, and lose a clear sense of what the agent is doing or when to step in. This leaves a missing part in the current agent ecosystem: an always-on Jarvis-style mediator that keeps the agent continuously reachable to the user. Such a mediator should support real-time spoken interaction with the user, answer questions without interrupting the worker, proactively report progress or confusion, and inject user guidance back into the agent's execution when useful. In this work, we introduce JarvisBench, a benchmark for measuring the dual value of mediation in long-horizon agent workflows. JarvisBench contains two complementary tracks: an agent-collaboration track that measures whether mediation improves downstream task completion, and a user-interaction track that measures whether mediation makes ongoing execution more understandable, responsive, and accessible to users. We instantiate the benchmark with a modular reference Jarvis prototype and evaluate it on 34 text-only WildClaw tasks executed in OpenClaw. Preliminary results with GPT-5.5, Claude Opus 4.7, Gemini-based, and GPT-based worker agents suggest that Jarvis-style mediation can provide trace-grounded responses to user questions and improve task performance when sparse user guidance is injected at appropriate moments. The results also show that effectiveness depends strongly on the mediator's LLM brain, highlighting both the promise of this missing middle layer and the need for broader community effort. Demo page this https URL

---


### 60. [From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.16621)

**<font color=#1a73e8>作者：</font>** Bo Tang, Yang Zhang, Guomian Zhuang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing memory systems for long-horizon LLM agents often retrieve prior traces as passive context rather than converting them into executable capabilities. In this paper, we propose MSCE, a training-free Memory--Skill Co-Evolution framework that organizes agent experience into grounded step traces, reusable procedural policies, and declarative environmental cognition. MSCE crystallizes evidence-backed L2 policies with positive estimated gain into callable skills that retain evidence links, applicability boundaries, decision guidance, verification rules, and reliability estimates. It further introduces reflection-weighted value backfilling, which propagates sparse terminal feedback through dense local self-reflections to produce evidence-calibrated trace values for governing memory and skill evolution. Experiments on EvoAgentBench and LoCoMo demonstrate that MSCE significantly outperforms state-of-the-art skill-augmented and memory-driven agent baselines, exhibiting strong cross-domain transferability and lifelong-evolution capabilities.

---


### 61. [A Research Prototype for Closed-Loop Generative Design of Customized Foot Orthoses via Semantic-Physics Alignment](https://arxiv.org/abs/2607.16631)

**<font color=#1a73e8>作者：</font>** Rui Wang, Byungwon Min, Suxing Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Translating unstructured clinical prescriptions into patient-specific foot orthoses (FOs) is hindered by a semantic-physical misalignment: high-level clinical intent is not mapped deterministically onto the 3D geometric parameters of the orthosis, and existing design workflows remain dependent on manual expertise with no instantaneous biomechanical validation. We present TANS-FO, a research prototype-a modular pipeline with closed-loop feedback for computational design automation of customized FOs, not a clinically validated therapeutic device. A Text-Aligned Neural Surrogate (TANS) uses cross-attention to project clinical-text embeddings onto a continuous lattice-density field, while a Graph Neural Network (GNN) surrogate predicts plantar stress in real time as a substitute for Finite Element Analysis (FEA). The framework is anchored on the open-access PicoFoot-5K anthropometric database (5,230 subjects; 30+ anatomical parameters). Under standardized quasi-static loading, the GNN surrogate agrees with an Abaqus reference solver (R^2 = 0.94), and the full pipeline synthesizes manufacturing-ready lattice insoles within minutes. On the Male 18-40 cohort, the proposed system attains a surrogate-predicted peak-pressure reduction of 34.7% over parametric CAD, with a fit error of 0.42 mm. Separately, an exploratory feasibility observation (n = 12; 2-week follow-up; no control group) using VAS pain reporting indicates short-term comfort improvement (VAS 6.4 -> 2.1), but this data is explicitly classified as preliminary observational evidence only-not evidence of clinical efficacy.

---


### 62. [TellTale: Blending Multi-Instance LoRA Text Encoders and a Zero-Shot LLM Judge for Ambivalence/Hesitancy Recognition in Videos](https://arxiv.org/abs/2607.16635)

**<font color=#1a73e8>作者：</font>** Abdel-Karim Al-Tamimi, Ali Rodan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TellTale, a text-only approach to ambivalence/hesitancy (A/H) recognition in interview videos, evaluated on the BAH dataset as part of the 3rd A/H Video Recognition Challenge (11th ABAW Workshop, ECCV 2026). Although the dataset provides video, audio, facial crops, and transcripts, TellTale relies on the transcript alone and combines three probability streams. Two text encoders, multilingual-e5-large and mDeBERTa-v3-base, are fine-tuned with parameter-efficient LoRA adapters under a multiple-instance learning (MIL) objective, in which transcript chunks are scored individually and pooled with a smooth maximum so that only the video-level label is needed for supervision. The third stream requires no training: a quantized 14B instruction LLM is prompted, zero-shot, to rate each transcript for A/H. The three probabilities are combined by a weighted average and a single decision threshold, both selected on participant-grouped cross-validated predictions. On the organizer-scored private test set of 152 videos from unseen participants, TellTale achieves a Macro-F1 of 0.7364 and an average precision of 0.7940, compared with 0.2827 Macro-F1 for the official vision-based baseline.

---


### 63. [TopoTuner: Topological Finetuning of Large Language Models](https://arxiv.org/abs/2607.16637)

**<font color=#1a73e8>作者：</font>** Abdulkadir Erol, Yash Mahajan, Vepaul Hariprashad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full fine-tuning remains a strong way to adapt pretrained LLMs, but it updates all weights and can be expensive. LoRA reduces the number of trainable parameters, but it does not directly answer which pretrained components should be trained and which can be frozen during adaptation. We introduce TopoTuner, a topology-guided fine-tuning framework for selective freezing of attention projection matrices. \method treats each projection matrix as a row cloud and uses Wasserstein distances between persistence diagrams to measure how its topology changes during fine-tuning.
TopoTuner learns a reusable freezing profile from a source dataset and transfers it to efficiently fine-tune models on out-of-domain datasets, evaluating whether task-specific topological drift generalizes across question answering and sentiment analysis tasks.
Across LLaMA-3.1-8B, Mistral-7B-v0.3, and Qwen3-8B-Base, TopoTuner is competitive with full fine-tuning while training only 1-2\% of the model parameters, and outperforms LoRA in 7 out of 9 model-dataset settings, which can change up to 39.57\% of the projection parameters. Along with minimized updates, TopoTuner reduces training time by 20.4\% relative to full fine-tuning and 5.5\% relative to LoRA on average. TopoTuner opens a new direction for reusable freezing profiles, where fine-tuning behavior learned on one dataset can be shared across multiple tasks.

---


### 64. [Diversity-Oriented Fine-Tuning for Uncertainty-Based Hallucination Detection](https://arxiv.org/abs/2607.16643)

**<font color=#1a73e8>作者：</font>** Qiuyuan Li, Hongliang Dai, Piji Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing hallucination detection methods are typically conducted at the inference stage, without making any modifications to the model itself. In this paper, we are interested in exploring fine-tuning strategies that enhance the detectability of hallucinations in the resulting model. Focusing on semantic-entropy-based detection, we observe that many erroneous outputs remain undetected because the model produces nearly identical incorrect answers across multiple runs. To address this, we propose diversity-oriented fine-tuning to encourage more varied generations. We introduce two specific strategies: one based on Supervised Fine-Tuning (SFT) and the other on Direct Preference Optimization (DPO). Extensive experiments are conducted to evaluate our approach and analyze the behavior of the models before and after fine-tuning. We find that after adopting our fine-tuning methods, the models become less likely to produce low semantic entropy responses for hallucinated answers, thereby improving the effectiveness of hallucination detection, eventually yielding results better than or comparable with state of the art methods. The code will be publicly released.

---


### 65. [Multimodal Attention-based Deep Learning for Emergency Triage with Electronic Health Records](https://arxiv.org/abs/2607.16662)

**<font color=#1a73e8>作者：</font>** Hazqeel Afyq Athaillah Kamarul Aryffin, Kamarul Aryffin Baharuddin, Mohd Halim Mohd Noor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate emergency triage decision is critical to avoid clinical deterioration, morbidity, and mortality. Machine learning-based triage system involves acquiring the main presenting complaint in text form and assessing vital signs in numerical data, enabling an automated and efficient analysis of patient information for timely and accurate prioritization of medical attention. However, modelling the intricacies of both data types requires a comprehensive understanding of the temporal structure and dependencies within the data. Thus, the aim of this study is to propose a multimodal deep learning architecture that can effectively handle both tabular and textual data. Furthermore, the proposed model exploits self-attention to to capture both local and global relationships between the features. A dataset consisting of 11,102 triage data collected from emergency department of Hospital Universiti Sains Malaysia is used for model development and validation. The proposed model demonstrated an increase of 1.95% in accuracy, 2.49% in F1-score, and 1.41% in ROC AUC compared to the baseline model. The experimental results demonstrated the potential of the proposed model in predicting triage decisions.

---


### 66. [Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs](https://arxiv.org/abs/2607.16693)

**<font color=#1a73e8>作者：</font>** Sharath Naganna, Tanvir Ahmed Sijan, Uddipta Kalita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often succeed on one formulation of a problem while failing on an equivalent formulation. Whether these failures arise from distinct internal circuits or different activation states of a shared circuit remains unknown. Recent mechanistic interpretability studies suggest that arithmetic in LLMs emerges from a "bag of heuristics," encoded by a sparse set of MLP neurons that represent distinct arithmetic strategies. We investigate whether arithmetic heuristic neurons are form-invariant across symbolic arithmetic, natural language word problems, and Python code in three Llama-3 models. In each format, we identify arithmetic heuristic neurons using a two-stage pipeline combining attribution patching and activation patching. A compact set of neurons is shared across all three formats, and targeted interventions show this shared circuit is both necessary and sufficient for late-layer arithmetic computation. Transferring the shared neurons' activations from a successful execution in one format to a failed execution in another recovers most incorrect predictions, exceeding 97% for addition and subtraction, indicating that cross-format failures arise from activation states rather than distinct circuits. Moreover, shared neurons consistently belong to the same heuristic families across formats, demonstrating that arithmetic computation in LLMs is largely form-invariant at the neuron level.

---


### 67. [Though Language Models Err While They Strive: Conformal Prediction for Self-Correcting Scientific Generation](https://arxiv.org/abs/2607.16704)

**<font color=#1a73e8>作者：</font>** Mingqiao Mo, Yunlong Tan, Hao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models frequently violate fundamental scientific principles when generating technical content, undermining their reliability in scientific applications. We introduce Scientific Feasibility Control SFC, a graph-structured conformal prediction framework that provides statistical guarantees for scientific reasoning validity through progressive absolute-coherent-factuality validation. Our approach decomposes scientific reasoning into atomic absolute-coherent-factuality units requiring both individual correctness against physical laws and logical substantiation from preceding context, addressing the cascade effect where early scientific errors contaminate subsequent reasoning steps. Unlike independence-based methods that treat claims in isolation, SFC models logical dependencies as approximate deducibility graphs and operates through real-time validation with dynamic branching when scientific violations are detected, the system branches to alternative generation paths using verified context as foundation. We demonstrate SFC across established scientific reasoning benchmarks including PhyX multimodal physics, MATH, ScienceQA, and ARC Challenge, achieving 50.1 percent accuracy on PhyX physics reasoning, substantially outperforming recent reasoning models including DeepSeek-R1 49.8 percent and GPT-4 45.8 percent while providing 91.7 percent scientific validity with formal conformal coverage guarantees at alpha equals 0.10 confidence level and reducing scientific law violations by 73 percent across multiple model architectures.

---


### 68. [DS@GT ARC at eRisk 2026: Hybrid Multi-Agent LLM System with Structured Algorithmic Guidance for Conversational Depression Screening](https://arxiv.org/abs/2607.16712)

**<font color=#1a73e8>作者：</font>** Victor Gong, David Guecha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe DS@GT's submission to the eRisk 2026 Task 1 challenge on conversational depression screening, in which systems interview LLM personas that simulate individuals with varying depression profiles and produce a Beck Depression Inventory II (BDI-II) score plus four key symptoms per persona, without directly asking sensitive mental health questions. Our pipeline evolved through three stages: a monolithic single-model prototype to start off, a baseline multi-agent architecture that separates conversational interviewing from BDI-II scoring under a coordinating orchestration layer, and a final hybrid configuration that replaces the paid GPT-5-nano interviewer with the open-source Gemma 27B. To offset the model's weaker reasoning and instruction-following, the hybrid adds three algorithmic components: a precomputed dialogue tree that standardizes interview openers and follow-ups, a reliability-weighted consensus aggregation inspired by the Weaver framework, and a cluster-based imputation step for unprobed symptoms. We submitted three fully automated runs across all 20 personas, with Run 1 from the paid baseline and Runs 2 and 3 from the hybrid. Hybrid Run 3 achieved an ADODL of 0.9063, ranking 3rd among all complete-submission runs and placing DS@GT 2nd among the 21 teams overall, while outperforming our paid baseline Run 1 (0.8841) at roughly one-quarter of the per-persona API cost. These results support our central hypothesis that with sufficient algorithmic supervision, a weaker open-source model can compete with a stronger proprietary model in the conversational interviewer role. Our source code is available at this https URL.

---


### 69. [Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding](https://arxiv.org/abs/2607.16721)

**<font color=#1a73e8>作者：</font>** Anik Jha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a few act on any token. That pool is why these models do not fit on the machines most developers own, yet for a user who only wants coding help, most experts encode abilities that will never be invoked. We ask how many experts can be removed, and which, by pruning two recent open-weight MoE models from different families (Qwen3.6-35B-A3B and Gemma-4-26B-A4B) under five selection strategies, judged the way a user would: by whether the model still writes correct code. Half the experts can be removed from either model with no statistically detectable loss on the primary code benchmark, and the damage lands almost entirely on abilities outside coding, the intended trade. But the winning strategy flips between the two models, so a recipe validated on one family cannot be assumed to work on another. We further show that perplexity, the metric much of the pruning literature leans on, can rate a broken model above an intact one; that a lightweight fine-tune recovers about half of what aggressive pruning loses; and that against quantizing the full model to the same memory, pruning wins only where quantization would have to drop below 3 bits per weight. Five attempts to overturn that crossover, with failure criteria fixed in advance (better calibration, guarded selection, causal expert importance, failure attribution, and an agentic evaluation letting each model repair its failures from execution feedback), all leave it standing; the last shows single-shot benchmarks overstate compression penalties broadly, as one repair turn erases the 2-bit quantization penalty entirely. Expert pruning works, but it demands per-model validation on the task the model will actually serve.

---


### 70. [Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs](https://arxiv.org/abs/2607.16726)

**<font color=#1a73e8>作者：</font>** Raza Imam, Darakshan Rashid, Yutong Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (MVLMs) promise broad zero-shot generalization, yet their reliability collapses when confronted with unseen modalities and domains, precisely where clinical robustness matters most. To address this gap, we revisit test-time modality generalization from the perspective of Mixture-of-Experts (MoE) and ask: can experts route-and-adapt without any optimization during inference? We identify a fundamental specialization-generalization dilemma at test time, where blindly aggregating modality experts dilutes modality-specific knowledge, while selecting one highly confident expert risks mismatch under shift. To address this, we propose MoBE: a fully optimization-free framework that performs dynamic expert selection and adaptation at test time. MoBE combines entropy-guided dynamic routing in MoE settings with expert-wise Bayesian adaptation, enabling experts to update their confidence and adapt online without gradient updates. Without parametric updates, MoBE augments a static MVLM with test-time routing and online statistics, achieving average accuracy gains of +4.72, +7.17, and +4.3 over state-of-the-art TTA methods across seen, unseen, and heterogeneous medical benchmarks, highlighting the effectiveness of training-free expert adaptation for robust modality generalization.

---


### 71. [Constraint-Anchored Reasoning Traces](https://arxiv.org/abs/2607.16727)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive multimodal large language models (MLLMs) suffer from error snowballing: a single incorrect inference early in a chainof-thought (CoT) trace corrupts all downstream reasoning. We find that in state-of-the-art open-source MLLMs, once the first error occurs, the reasoning cascades into failure across all remaining steps in 65% of such cases (a metric we term the snowball rate). Existing mitigations-sampling multiple chains, post-hoc self-verification, or full program synthesis-either lack symbolic grounding, catch errors too late, or sacrifice the flexibility of natural language reasoning. We propose Constraint-Anchored Reasoning Traces (CART), a neuro-symbolic framework that trains MLLMs to interleave natural language reasoning steps with symbolic constraint assertions: lightweight, machine-checkable statements about visual content (e.g., count(red_objects) = 3). A dual-pronged Constraint Propagation Module-combining a learned neural grounding head with Boolean Constraint Propagation-continuously verifies these anchors against extracted visual features and checks their mutual logical consistency. When a contradiction is detected, a backtrack controller halts generation and reverts to the last consistent checkpoint, preventing error propagation. A variable-frequency emission mechanism allows the model to adaptively control anchor density, avoiding trace bloat. We construct 218K training instances by augmenting GQA, CLEVR-CoGenT, and VCR with ground-truth constraint annotations derived from scene graphs, and fine-tune open-source MLLMs (LLaVA-NeXT, Qwen2-VL) via LoRA. On five benchmarks, CART reduces the snowball rate from 0.65 to 0.14, improves GQA accuracy by +4.6 percentage points over trainingonly baselines, and achieves 89.1 F1 on POPE-all with at most 18% inference overhead.

---


### 72. [The Anatomy of a Truth Direction: Knowledge-Dependent Dimensionality, a Relational Law, and a Convergent Category Geometry in Small Language Models](https://arxiv.org/abs/2607.16741)

**<font color=#1a73e8>作者：</font>** Francesco Karim Vicidomini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bürger et al. (2024) demonstrated that truth representations in large language models are universal across statement polarity but reside within a multidimensional subspace. We extend that framework along three questions: how the dimensionality of the subspace depends on the model's knowledge, which architectural component builds the truth direction, and what the direction is a mixture of. In Part I (one model), a training-free directional probe derived from the SVD of hidden-state minimal pairs shows that the dimensionality of truth is knowledge-dependent: the signal is concentrated on a single axis for behaviorally known facts (held-out AUC 0.938) and becomes diffuse as knowledge decreases or material heterogeneity increases; seven falsification experiments sustain the one-dimensional reading, and the same decomposition recovers the supervised polarity direction of Bürger et al. at cosine 0.959 without polarity labels. In Part II (four base models, two families, pre-registered predictions), a relational law emerges: attention propagates truth frames it did not write, the feed-forward network opposes the frame of its current block, and the genuine post-peak decay is causally attributed on all four models to the SwiGLU value stream; per-category truth axes form a semantically signed arrangement that contradicts the lexical surface and converges across families (Mantel p = 0.0009). Stress tests at three scales (33 categories, 888 pairs per relation, six sampling seeds) expose a sign instability of the per-category orientation, repair it with a declared spectral consensus gauge, and sharpen the convergence into a knowledge-gated law, strengthening from +0.42 on dense mixed-knowledge material to +0.74 on knowledge-restricted categories: the geometry of the mixture belongs to the knowledge domain rather than to the architecture.

---


### 73. [Multi-Dimensional Quality Assessment for AI-Generated Human-Centric Videos: Dataset and Model](https://arxiv.org/abs/2607.16742)

**<font color=#1a73e8>作者：</font>** Sijing Wu, Yunhao Li, Huiyu Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated human-centric videos play a crucial role in a wide range of modern applications. However, they often suffer from quality issues and semantic mismatches, underscoring the importance of effective quality assessment for such videos. To this end, we extend our previous dataset HVEval with pairwise preference annotations, resulting in HVEval+, the largest holistic quality assessment dataset for AI-generated human-centric videos, which comprises 1k prompts based on a comprehensive taxonomy, 20k videos generated by 24 text-to-video (T2V) models, and extensive human annotations, including 60k mean opinion scores (MOSs) and 60k preference pairs across 3 dimensions (i.e., spatial quality, temporal quality, and text-video correspondence), as well as 20k category-specific question-answer (Q&A) pairs. Along with the HVEval+ dataset, we further propose MoE-Rater, a Mixture-of-Experts (MoE)-inspired and multimodal large language model (MLLM)-based all-in-one method that supports multi-dimensional quality rating, multi-dimensional pairwise comparison, and category-specific question answering within a single model. Specifically, we introduce Mixture of Projector Experts (MoPE) and Mixture of LoRA Experts (MoLE), together with a three-stage training strategy consisting of task-aware pre-training, task-specific adaptation, and adaptive routing optimization, to effectively unify multiple tasks, resulting in superior performance on both HVEval+ and Human-AGVQA datasets. Extensive experiments and comprehensive analysis demonstrate the significant potential of the HVEval+ dataset and the MoE-Rater method in advancing AI-generated video quality assessment and further facilitating the evaluation and optimization of T2V models.

---


### 74. [JOR-Bench: Japanese Operations Research Benchmarks for Large Language Models](https://arxiv.org/abs/2607.16777)

**<font color=#1a73e8>作者：</font>** Yuu Jinnai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present JOR-Bench, a collection of five Japanese-language benchmarks for evaluating the ability of large language models (LLMs) to formulate and solve operations research (OR) problems. Each benchmark is a Japanese translation of an existing English benchmark: IndustryOR, MAMO Complex LP, NL4OPT, OptiBench, and OptMATH, covering 1,319 problems spanning linear programming, mixed-integer programming, non-linear programming, and combinatorial optimization. JOR-Bench is a solver-independent benchmark that can be used with any solver or programming language, and consists of pairs of Japanese problem statements and expected numerical answers. We evaluate seven LLMs, including multilingual general-purpose models and Japanese-specialized models, on both the original English and the new Japanese versions, and compare performance across languages. For the main evaluation, we standardize execution with the Python interface to OR-Tools to make model outputs comparable and reproducible with open-source software. Our results show that OR formulation ability is largely language-neutral for strong multilingual models; the overall average accuracy difference between English and Japanese is only $-0.3$ pp. Yet error analysis reveals subtle cross-lingual differences, including a pragmatic disambiguation failure in some domains that causes models to output decision-variable values instead of the objective value when the prompt is in Japanese.

---


### 75. [MultiLoReFT: Decoupling Shared and Modality-Specific Subspaces in Multimodal Learning via Low-Rank Representation Fine-Tuning](https://arxiv.org/abs/2607.16789)

**<font color=#1a73e8>作者：</font>** Sana Tonekaboni, Viktoria Schuster, Caroline Uhler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world perception and decision making are inherently multimodal, integrating complementary signals across modalities. However, training multimodal models faces two main obstacles. First, collecting large-scale, well-aligned paired multimodal datasets is often impractical, making end-to-end multimodal training difficult. Second, existing multimodal representations frequently entangle information shared across modalities with modality-specific information, hindering interpretability and control. We introduce MultiLoReFT, an efficient and scalable low-rank representation fine-tuning framework for multimodal learning with pretrained unimodal models. MultiLoReFT extends low-rank adaptation to the multimodal setting and learns interpretable projection subspaces that decouple shared and modality-specific information. Across simulated and real-world benchmarks, it produces representations that support multimodal prediction while explicitly revealing how shared and modality-specific information is distributed across modalities.

---


### 76. [Scene-SAM3D: Multi-View Scene Asset Generation Without Fine-Tuning](https://arxiv.org/abs/2607.16805)

**<font color=#1a73e8>作者：</font>** Yuqi Zhang, Yadan Luo, Xiangyu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D scene assets are critical for embodied applications such as robotic manipulation, navigation, and simulation. Despite their strong object priors, recent single-image 3D generation models such as SAM3D remain insufficient for real-world scenes, where severe occlusions, redundant observations, and cross-view inconsistencies make reliable scene generation challenging. We introduce Scene-SAM3D, a training-free framework that extends SAM3D from single-view object generation to calibrated multi-view scene asset generation. Scene-SAM3D selects a compact set of complementary views, reducing observation redundancy while providing additional evidence for regions occluded in individual views. Based on the selected views, it performs step-efficient latent velocity fusion to integrate multi-view evidence and suppress cross-view conflicts in canonical space. Finally, a lightweight rigid-object Gaussian optimization refines the scene layout within 200 iterations while preserving the generated object geometry. Experiments on Replica and ScanNet++ demonstrate consistent improvements at both instance and scene levels, with our method reducing scene-level CD by 43.8% on Replica and 30.9% on ScanNet++, while cutting flow-model sampling FLOPs and wall-time latency by nearly 20% under the same multi-view setting. Code will be released at this https URL.

---


### 77. [Schema-Constrained Document-Level Event Argument Extraction with Lightweight LLM Fine-Tuning](https://arxiv.org/abs/2607.16808)

**<font color=#1a73e8>作者：</font>** Roberto Pietrantuono, Antonio Guerriero, Pouya Sattari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event Argument Extraction (EAE) converts documents into structured event records by identifying argument spans and assigning them schema-defined roles. Document-level EAE is challenging due to long-range dependencies between triggers and arguments, cross-sentence context, and strict role constraints, which often lead to boundary errors, uncertainty in roles, and inconsistencies with restricted schemas.
In this paper, we study whether mid-sized open LLMs can perform schema-constrained EAE reliably at the document level on MAVEN-ARG. Our approach combines (i) role-set injection in prompts for schema compliance, (ii) parameter-efficient supervised fine-tuning (LoRA) using the same JSON-only interface used at inference, and (iii) deterministic decoding with post-processing that validates JSON, filters invalid roles, de-duplicates arguments, and aligns spans to the document window. Under the official MAVEN-ARG evaluator, fine-tuned mid-sized open models outperform previously reported GPT baselines across mention, entity-coreference, and event-coreference evaluations; our best model (Phi-4, 14B) reaches 42.39\% F1 at the event-coreference level. Code to reproduce experiments is publicly available at this https URL.

---


### 78. [FUSAR-R1: A Large-Scale Reasoning Model for Intelligent Interpretation of SAR Images](https://arxiv.org/abs/2607.16819)

**<font color=#1a73e8>作者：</font>** Yi Yang, Xiaokun Zhang, Yuxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, large-scale vision-language models have been driving a paradigm shift in intelligent remote sensing image interpretation. By incorporating textual semantic information, the cognitive expression, semantic understanding, and human-computer interaction capabilities of interpretation models have been significantly improved, achieving initial progress in the field of Synthetic Aperture Radar (SAR) image interpretation. However, SAR images are affected by factors such as coherent imaging mechanisms, complex scattering characteristics, speckle noise interference, and target-background coupling, resulting in complex and variable image features with significant uncertainties and specializations. Existing SAR vision-language models do not yet possess the step-by-step analysis, logical judgment, and self-correction capabilities of human experts, making it difficult to support reliable intelligent interpretation in complex scenarios. To address this issue, this paper proposes a large-scale reasoning model, FUSAR-R1, for intelligent interpretation of SAR images. The model first constructs explicit chain-of-thought reasoning data by simulating the interpretation process of human experts and uses this data to guide instruction learning, thereby endowing the model with basic reasoning capabilities. Subsequently, a reinforcement learning strategy is introduced to optimize the model's outputs based on inference results, enabling self-correction and more reliable reasoning. Experimental results demonstrate that FUSAR-R1 consistently outperforms existing multimodal large-scale models across various SAR interpretation tasks, including target detection, target counting and classification, and land-cover category recognition.

---


### 79. [First-Order Predictable but Pairwise Fragile: Local Task Adaptation in Trained Transformers](https://arxiv.org/abs/2607.16821)

**<font color=#1a73e8>作者：</font>** Irina Piontkovskaia, Sergey Nikolenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task arithmetic, sequential fine-tuning, activation steering, and first-order random search all operate through relatively small perturbations around an already trained checkpoint, and they rely on different local approximations: individual perturbations should be first-order predictable, task updates should compose with controlled interference, useful tangent structure should be stable and possible to estimate, and weight edits should have counterparts in representation space. We measure 8 such properties with the same harness around a multitask LoRA operating point, on 9 transformers (82M-7B), with a prospectively registered property list, thresholds, and test split. We find a shared one-direction validity window up to the tested scale $10^{-2}$, but no universal radius for pairwise composition or update ordering. Along individual directions, changes of the probe loss remain first-order predictable throughout the grid: a perturbation's effect on the loss is essentially its projection onto the gradient, which is also what makes local random search work. Pairwise structure, however, proves to be far more fragile: on over a third of the measured (model, task pair) combinations, two-update order sensitivity sets in strictly inside that window; task-gradient subspaces rotate within tens of steps; additivity under our fixed activation probe fails at full task-vector scale on several models, including both held-out 7B models; and no model median passes the registered global mean-vector weight-to-steering correspondence bar. For two sequential task-gradient steps, the leading order-dependent term is the Lie bracket $H_B\textbf{g}_A-H_A\textbf{g}_B$; its normalized prediction $c(\eta)=\eta\kappa+O(\eta^2)$ tracks the measured defect at median ratio 1.002, while the onset scale $\eta^\dagger\approx0.10/\kappa$ spans three orders of magnitude across models and task pairs.

---


### 80. [UniNDM: A Unified Noise-driven Detection and Mitigation Framework Against Sexual Content in Text-to-Image Generation](https://arxiv.org/abs/2607.16828)

**<font color=#1a73e8>作者：</font>** Yao Huang, Yitong Sun, Huanran Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the impressive generative capabilities of text-to-image diffusion models, they remain vulnerable to implicit sexual prompts, where subtle cues disguised as benign terms or adversarial tokens unexpectedly generate the inappropriate content due to model biases or latent correlations in training data. Existing safety mechanisms face fundamental limitations: detection methods primarily identify explicit content and fail to capture implicit malicious intent, while mitigation approaches rely on static negative prompts inadequate for diverse implicit scenarios. To address these challenges, we propose UniNDM, a unified noise-driven framework that rethinks safety mechanisms through the lens of noise dynamics in diffusion processes. Our key insight is that early-stage predicted noise exhibits inherent separability between normal and sexually explicit content, which we theoretically demonstrates quadratically increasing semantic concentration with timestep. Leveraging this property, we develop a lightweight noise-based detector achieving superior accuracy with virtually no computational overhead. For mitigation, we introduce noise-enhanced adaptive negative guidance: dynamically generating context-specific negative prompts via large language models to handle diverse implicit content, while optimizing initial noise by suppressing attention concentration on explicit tokens to provide comprehensive protection. Besides the U-Net-based diffusion models, we further extend our framework to emerging Diffusion Transformer architectures through region-constrained semantic guidance tailored for their unified multimodal attention. Comprehensive experiments across U-Net models and DiT models on both natural and adversarial datasets demonstrate substantial improvements over state-of-the-art methods, including SLD, UCE, Safree, etc. Our code is publicly available at this https URL.

---


### 81. [Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment](https://arxiv.org/abs/2607.16841)

**<font color=#1a73e8>作者：</font>** Pengxu Chen, Yao Zhu, Guangming Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated remarkable capabilities in multimodal understanding. However, they remain prone to hallucinations, generating responses that are inconsistent with the visual evidence. Existing mitigation methods largely address language-prior bias or cross-modal imbalance, while progressive visual degradation across perception and memory remains underexplored. In this work, we propose Saliency-Driven Perceptual Realignment (SDPR), a training-free framework that mitigates the degradation of visual awareness throughout inference. Specifically, we first introduce saliency-driven attention redistribution to release attention hijacked by non-semantic sink tokens, thereby recovering critical visual evidence. Second, we identify spatial distortion in the KV cache and propose saliency-driven cache alignment to preserve query-relevant visual features during generation. Finally, we introduce prior-constrained contrastive decoding to penalize unfaithful predictions induced by dominant language priors. Our proposed SDPR is robust against hallucinations due to its holistic alignment of visual awareness across the entire generative trajectory. Extensive experiments across diverse LVLM architectures show that SDPR outperforms state-of-the-art methods on both hallucination and general-purpose benchmarks, requiring no additional training and incurring minimal runtime overhead. The code is available \href{this https URL}{\color{blue}{here}}.

---


### 82. [Group Entropy-Controlled Policy Optimization](https://arxiv.org/abs/2607.16850)

**<font color=#1a73e8>作者：</font>** Guangran Cheng, Chengqi Lyu, Songyang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entropy control has become an effective tool in reinforcement learning (RL) of large language models (LLMs), helping balance exploration-exploitation trade-off during alignment process. Such RL paradigm is often conducted on mixtures of heterogeneous tasks, which induce distinct entropy regimes under the same policy, making global or token-level entropy regulation insufficient to corresponding heterogeneous needs of exploration. This heterogeneity further makes GRPO-style normalized advantages induce an entropy-dependent bias, making advantage signals across prompt groups statistically non-comparable. To address this issue, we propose Group Entropy-Controlled Policy Optimization (GEPO), a lightweight extension to GRPO that uses group entropy, estimated from existing grouped samples to perform entropy-conditioned asymmetric advantage shaping. GEPO attenuates positive advantages in low-entropy groups to reduce over-exploitation, and negative advantages in high-entropy groups to preserve exploration, with adaptive thresholds derived from historical entropy statistics. Extensive experiments on two base models across thirteen benchmarks spanning mathematics, physics, science, code generation, and instruction following show that GEPO consistently outperforms GRPO and recent entropy-controlled methods, delivering balanced cross-task improvements while preserving task-specific exploration levels throughout training.

---


### 83. [AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents](https://arxiv.org/abs/2607.16851)

**<font color=#1a73e8>作者：</font>** Yangqin Jiang, Chao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying LLM agents typically requires a compact test-time student, even if a stronger teacher is available during training. We study knowledge brewing: distilling a teacher's interactive experience into a persistent external memory for the student. Crucially, this requires no weight updates, expert demonstrations, ground-truth labels, or test-time teacher access. This setting poses two challenges: environments provide only sparse, binary feedback, and teacher-authored notes must be inherently tailored to be concretely executable by a substantially weaker student. To address these hurdles, we propose AgentBrew, comprising two coupled components. First, a failure-triggered teacher--Ralph Loop mitigates sparse feedback by transforming student failures into environment-validated notes. Second, student-aware synthesis calibrates teacher knowledge to the weak executor's operational granularity, yielding model-specific, actionable guidance. Extensive evaluations and comprehensive ablations across coding, math, and tool-use tasks demonstrate that this asymmetric, training-free brewing paradigm produces highly capable yet deployable LLM agents.

---


### 84. [Beyond Semantic Equivalence: Logical Graphs for LLM Uncertainty Quantification](https://arxiv.org/abs/2607.16868)

**<font color=#1a73e8>作者：</font>** Yanni Dong, Minghua Liu, Meiling Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often produce confidently stated yet unreliable outputs, posing critical challenges for deployment in safety-sensitive applications. Existing uncertainty metrics such as semantic entropy capture agreement at the level of semantic equivalence, but largely ignore the logical relationships between distinct answers. As a result, they tend to overestimate uncertainty and falsely flag hallucinations in settings where generated responses are diverse in form yet logically compatible (e.g., differing only in granularity or specificity). We propose Logical Graph Uncertainty (LGU), a framework that explicitly models implication and incompatibility among answers. LGU aggregates probability mass along entailment chains, computes entropy over logically maximal hypotheses, and penalizes mutual incompatibility among them. Across multiple question-answering benchmarks, LGU consistently improves uncertainty estimation over existing methods, and outperforms the semantic entropy baseline by up to +7.1% AUROC and +3.5% AUARC across datasets.

---


### 85. [Trace-Based On-Policy Distillation for Masked Diffusion Language Models](https://arxiv.org/abs/2607.16872)

**<font color=#1a73e8>作者：</font>** Haolin Ren, Ziyang Huang, Chenhao Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) are a promising alternative to autoregressive generation. However, reasoning-oriented post-training for dLLMs remains challenging. Supervised fine-tuning (SFT) for dLLMs requires dense but often off-policy masked states, while reinforcement learning (RL) relies on sparse rewards or value modeling. This paper proposes \textbf{trace-based on-policy distillation (TOPD)}, a teacher-supervised framework that transfers reasoning ability to a target dLLM without reward estimation. The key idea is to supervise a dLLM on its own denoising trajectory, focusing on the trace-aligned token decisions that form the final response. Specifically, TOPD samples on-policy diffusion trajectories from the target dLLM, obtains teacher token distributions from a teacher model on the corresponding partially denoised states, and updates the target dLLM with a token-level Reverse Kullback-Leibler (Reverse-KL) objective. This design preserves dense teacher supervision while aligning training with the model's own denoising states. On mathematical reasoning benchmarks, TOPD enables SDAR-4B-Chat to match the MATH500 accuracy of its RL-trained counterpart TraDo-4B-Instruct, with gains of +5.7 under static evaluation and +4.5 under dynamic evaluation. Compared with the RL-trained counterpart, TOPD achieves this with 4$\times$ fewer rollout rounds, corresponding to an estimated 96.0$\times$ to-accuracy model-compute speedup.

---


### 86. [Cross-Branch Conflict as a Shield: Safeguarding Facial Identities in Unified Multimodal Image Editing](https://arxiv.org/abs/2607.16898)

**<font color=#1a73e8>作者：</font>** Weiwei Tan, Junxian Li, Rui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) have recently demonstrated powerful instruction-based image editing capabilities, but they also raise serious concerns about unauthorized manipulation of personal portraits. Existing adversarial protection methods are mainly designed for either visual understanding or image generation models and often become ineffective when transferred to UMMs, which process an image through multiple complementary visual pathways. In this work, we first conduct a feature-level analysis of unified image editing. We observe that the ViT-based understanding branch and the VAE-based generation branch exhibit non-trivial structural agreement for the same input image. Although perturbing an individual branch can reduce this agreement and induce intermediate hidden-state deviations, such effects are asymmetric and gradually attenuated during multimodal fusion and generation. These observations reveal that single-branch feature distortion is insufficient for consistently disrupting unified image editing. Motivated by this finding, we propose CCS, a unified adversarial protection framework that jointly drives the ViT and VAE representations away from their clean counterparts while explicitly disrupting their cross-branch compatibility through linear CKA. By simultaneously removing stable information from both visual pathways and creating incompatible visual contexts, CCS prevents the UMM from recovering reliable identity information during editing. Extensive experiments demonstrate that CCS consistently outperforms existing protection methods in suppressing identity-preserving edits.

---


### 87. [Environment-free Synthetic Data Generation for API-Calling Agents](https://arxiv.org/abs/2607.16900)

**<font color=#1a73e8>作者：</font>** Seanie Lee, Sanjoy Chowdhury, Chao Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training API-calling large language model (LLM) agents demands massive amounts of high-quality trajectories. However, collecting such data at scale typically requires fully implemented environments with executable APIs and realistic, pre-populated backend databases, creating a major bottleneck for scalability. To overcome this, we propose an environment-free synthetic data generation approach that leverages LLMs as on-the-fly digital world models. Given only API specifications, our method generates trajectories mimicking interactions between an agent and a stateful environment. Specifically, an LLM first generates diverse tasks solvable with the provided APIs. A teacher agent then iteratively solves each task while an LLM simulator generates coherent synthetic API responses conditioned on the task context and simulation history. Finally, an LLM judge filters the trajectories to ensure the quality of the resulting dataset. We evaluate our approach on the challenging AppWorld and OfficeBench benchmarks, which include both information-retrieval and state-changing tasks. Fine-tuning models on our synthetic data yields significant performance gains, demonstrating that effective supervision for API-calling agents can be generated without any executable environment. Our results establish LLM-based API simulation as a practical, scalable solution for training agents across diverse API ecosystems.

---


### 88. [CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation](https://arxiv.org/abs/2607.16955)

**<font color=#1a73e8>作者：</font>** Satyam Kumar, Saurabh Jha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy knowledge distillation transfers reasoning from large teachers to compact students, but existing approaches suffer three compounding failure modes: (i) cold-start collapse, where a fresh student assigns near-zero mass to teacher-preferred tokens; (ii) state-agnostic divergence scheduling, where time-only forward/reverse-KL interpolation ignores the student's coverage state; and (iii) binary reward sparsity, where pass/fail signals discard information from partially correct traces.
We present CADENCE, a unified framework with a targeted fix for each. Its DRIFT mechanism schedules a per-token convex mixture of forward-KL and reverse-KL surrogate objectives on student-sampled trajectories (per-token surrogates, not sequence-level KL gradient estimators). Six components extend it: (A) COVA, a coverage-adaptive $\beta$ schedule accelerating the forward-to-reverse transition; (B) FTB, a forking-token boost concentrating gradient at high-entropy positions via a globally-normalized entropy reference; (C) CCD, a dense reward adding numerical-proximity partial credit for incorrect-but-close traces; (D) LAP, brevity-preferential correct-rollout reinforcement; (E) EMR, an entropy-matching calibration regularizer; (F) BSD, a bootstrapped self-distillation phase.
On GSM8K and MATH-500 (corrected 512-token protocol, 5 seeds, reported std), CADENCE distills a 0.5B student from a 1.5B teacher to 69.8 $\pm$ 0.5% GSM8K pass@1 (from 48.7% pretrained; 63.2% of the teacher gap closed) and to 72.1 $\pm$ 0.4% with a 3B teacher (76.2% closed), beating the strongest matched-compute label-using baseline (DRIFT+binary reward) by +4.4 $\pm$ 0.7 points. All experiments run on a single Apple Mac Studio (M-series, 64GB unified memory), showing principled distillation reaches strong reasoning quality without datacenter-scale hardware.

---


### 89. [Lomekwi: Resource-Bounded Tool Discovery in LLM Agents](https://arxiv.org/abs/2607.16961)

**<font color=#1a73e8>作者：</font>** Roshan Klein-Seetharaman, Daniel Wang, Andrew Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing tool-use benchmarks report a single success rate for complex, multistep tasks. Inspired by ideas from cognitive science, we distinguish tool use from tool discovery and decompose the latter into curiosity (the model's ability to discover the parts needed to build the tool), recognition (the model's ability to discover the process of creating the tool), and efficiency (the model's use of the tool after creation). We show that this framework can be applied to existing discovery tasks, such as Voyager. In addition, we provide evidence that recognition inversely scales with model size, and we introduce and analyze a class of combinatorial games that demonstrates this. We further observe inverse scaling in a separate environment designed to emulate real-world tasks.

---


### 90. [TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization](https://arxiv.org/abs/2607.16973)

**<font color=#1a73e8>作者：</font>** Navnit Shukla, Kamal Pandey, Omsankar Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems increasingly power enterprise LLM applications, yet the vector retrieval layer introduces two underexplored challenges: (1) trained codebook quantizers may expose corpus statistics during index construction, creating a leakage channel in multi-tenant deployments, and (2) post-hoc filtering for tenant isolation degrades recall on selective queries. We study TurboVec, an open-source vector index built on TurboQuant - a codebook-oblivious scalar quantizer requiring no corpus-dependent training. On the DBpedia OpenAI embeddings benchmark (d=1536, 100K-999K vectors), TurboQuant 4-bit outperforms trained FAISS Product Quantization at the same memory budget by 8.5-8.9 percentage points in Recall@5 across all scales. Compared to HNSW (R@5=0.991) and IVF-PQ (R@5=0.840), TurboQuant occupies a distinct design point: higher recall than IVF-PQ without training, at 4-8x less memory than HNSW. Deployed on Snowpark Container Services, TurboVec achieves 11ms median query latency at 100K vectors versus 707ms for warehouse brute-force scan. Kernel-level allowlist filtering maintains 0.86-0.93 Recall@10 across 10-1000 tenant workloads versus 0.09-0.19 for post-filter baselines. Codebook-oblivious design reduces membership inference accuracy to near-random (50.0%) versus 57.3% for PQ codebooks. Limitations include single dataset evaluation, uncompressed HNSW comparison, and privacy evaluation on synthetic data only.

---


### 91. [ChemFusion: A Multimodal Cross-Attention Network for Reaction Yield Prediction](https://arxiv.org/abs/2607.17033)

**<font color=#1a73e8>作者：</font>** Qiwei Han, Chi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting the outcomes of transition-metal-catalyzed reactions is notoriously complex due to the interplay of diverse physical and chemical variables. A persistent computational bottleneck has been effectively merging broad electronic descriptors with the localized, three-dimensional geometry of the reactive site. To bridge this representation gap, we present ChemFusion, a hybrid neural network that fuses conventional electronic features with explicit 3D atomic coordinates. Using a cross-attention mechanism, the model enables global electronic states to dynamically attend to specific spatial constraints within un-pooled molecular point clouds. When benchmarked against a diverse library of cross-couplings, this approach delivers exceptional predictive performance, decisively surpassing traditional single-modality frameworks. Importantly, extracting the attention matrices reveals that the architecture autonomously learns to identify and penalize restrictive steric hindrances. This provides a physically grounded interpretability, demonstrating that spatially aware networks can navigate complex reaction sterics that standard statistical models typically miss.

---


### 92. [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038)

**<font color=#1a73e8>作者：</font>** Amez Amanj Ali, Kuo-Kun Tseng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses key technical challenges in current large language model (LLM) agent applications, including long-horizon planning, sparse reward attribution, and dynamic environmental interaction, by designing and optimizing an intelligent agent workflow. The proposed architecture is based on the synthesis of core AI paradigms: Visual, Language, Generative, Graph, Multimodal, Reinforcement, and Agent Intelligence. Unlike conventional baseline models that rely on static prompting and lack robust perception-action loops, our approach introduces a Partially Observable Markov Decision Process (POMDP) routing mechanism. This mechanism is augmented with an internal, self-correcting reward model that evaluates decision trajectories before execution. By integrating multimodal inputs and advanced reinforcement learning principles (such as proximal policy optimization and value function approximation), the agent maintains long-term structural memory and dynamically adapts its reasoning pathways to mitigate error accumulation. Empirical experiments on the ALFWorld embodied simulation environment and the WebShop online navigation benchmark demonstrate a 24.5% absolute improvement in task success rate and trajectory efficiency over mainstream baselines like the standard ReAct framework. Comprehensive ablation studies confirm the significant contribution of the reward-driven critique module in suppressing hallucination rates. This research bridges theoretical foundations of reinforcement learning and graph-based memory with autonomous agent workflows. Ultimately, the resulting architecture offers a practical, scalable reference framework for developing artificial intelligence technologies in complex, multi-step autonomous systems. Code is available at this https URL.

---


### 93. [Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning](https://arxiv.org/abs/2607.17043)

**<font color=#1a73e8>作者：</font>** Xiaonan Luo, Yue Huang, Kehan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model collapse is a central challenge in learning from synthetic data: as later-generation large language models (LLMs) are trained on an increasing proportion of model-generated data, performance can degrade due to narrowed coverage and accumulated bias. Existing work mainly studies how to bound this degradation. In iterative model evolution, however, the more meaningful objective is to ensure that each successive model improves over its predecessor, which requires diagnosing collapse at a granularity that is actionable for data curation. We study this problem in synthetic data self-improving for instruction tuning. We show that collapse in this setting is not simply uniform performance degradation, but can appear as a polarization of competence, where synthetic training reinforces already strong skills while further degrading weak ones. Motivated by this observation, we propose KITE (Knowledge-boundary Instruction Tuning via Exploration), a two-stage framework that combines failure-guided data generation with boundary-aware uncertainty curation. Experiments across several datasets and multiple open-source LLMs show that KITE yields more stable improvement than strong synthetic-data baselines.

---


### 94. [Solver-Hard Is Not Model-Hard: A Hardness-Controlled Diagnostic for LLM Constraint Reasoning](https://arxiv.org/abs/2607.17047)

**<font color=#1a73e8>作者：</font>** Lucky Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM constraint reasoners are often evaluated near the random-SAT phase transition, confounding density and solver hardness. We test instance-level transfer while near-matching clause density. At aligned size bins, with near-matched density and matched maximum clause width, we compare proof-hard expander-Tseitin and proof-easy ladder-Tseitin formulas, pigeonhole anchors, and density-mismatched controls. Theory separates their resolution hardness; a solver-specific Glucose mean-conflict proxy differs by up to $51\times$, and five other solvers preserve the direction. Across three included models (243 instances each; a fourth is excluded for abstention), the near-matched-density accuracy gaps range from $-32$ to $+20$ points, with a pooled gap of $+1.7$ points ($p=0.74$) and a wrong-signed correctness-versus-conflict association ($r=+0.15$). A proof-preserving relabeling lowers accuracy in all five clusters for one model (mean $-93$ points) but not another, exposing model-surface sensitivity. In a preregistered extension, provider-reported completion-token spend does not consistently increase with the proxy after accounting for formula length and censoring. At 16k, the reasoning model spends more on proof-easy matched formulas and exhausts its budget on the solver-easiest UNSAT family; the 32k C1 gap is absent. These scoped dissociations concern verdict accuracy and observed token spend, not certificate solving, exact proof length, or allocation efficiency.

---


### 95. [Searching for Task-Specific Vision Paths: Evolutionary Block Pruning Across Vision-Language Models](https://arxiv.org/abs/2607.17052)

**<font color=#1a73e8>作者：</font>** Tarun Tomar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models normally execute the same complete vision encoder for every question, even when OCR, counting, object, attribute, and spatial queries may not require identical computation. We study whether fixed-budget combinations of vision blocks can be skipped without fine-tuning. A shared K-block route skips one searched set of exactly K blocks for every question, while a capability-specific K-block policy selects one same-size route using a known capability label. We introduce a source-balanced evolutionary search and compare it with independent ranking, contiguous removal, and random routes at matched budgets. Experiments use Qwen2.5-VL-3B-Instruct, SmolVLM2-2.2B-Instruct, and an 876-example image-disjoint selection split. Search transfers across architectures: on SmolVLM2, the searched shared four-block route beats independent construction by 4.91 percentage points. Capability specialization is less stable. On Qwen, the six-block capability policy beats the shared route by 2.17 points, driven by a 7.10-point OCR gain. On sealed IIIT5K, however, the SmolVLM2 OCR-specific route trails its shared route by 13.6 points. Combinatorial search reliably improves route construction, but capability labels do not define universally transferable vision pathways.

---


### 96. [When LLMs Over-Answer: Measuring and Mitigating Quality Issues in LLM-Based Hardware Description Language Question Answering](https://arxiv.org/abs/2607.17063)

**<font color=#1a73e8>作者：</font>** Ziteng Hu, Jiachi Chen, Wenhao Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) has led practitioners to increasingly rely on them for answering questions about hardware description languages (HDLs). Because HDL is ultimately synthesized into physical hardware, an imprecise or redundant answer can propagate into timing violations or non-synthesizable logic that surface only late in the design flow, making the quality of HDL answers especially consequential. However, the quality of LLM-generated responses, particularly in comparison with answers provided by human experts, remains unclear. To investigate this question, we collect 6,246 HDL Q&A posts with accepted answers from Stack Overflow and curate them into a dataset, organized into a taxonomy of four main categories (Conceptual, Debugging, Generation, and Optimization) and ten subcategories. Using this dataset, we design a user study conducted with 19 HDL engineers with one to three years of experience. Our findings reveal a pervasive over answering tendency: LLMs supply correct content but bury it under redundant alternatives (65.7%) and verbose padding (69.1%), while nearly half of answers (49.0%) fail to fully align with expert answers yet participants still preferred LLM responses for readability (58.3%). Motivated by these findings, we propose a multi-agent framework for improving LLM-based HDL question answering. We evaluate answer quality using an LLM-as-Judge and two structural metrics: the number of core answers, which reflects redundancy since LLMs often provide multiple alternative solutions, and the length of non-core content, which reflects verbosity. Evaluated on the four mainstream LLMs, our framework increases the average core-answer quality score from 3.71 to 4.67 (+0.96) and the non-core content quality from 3.72 to 4.23 (+0.51), on a five-point scale.

---


### 97. [Persistent Sparse Autoencoders: Learning Feature Timescales in Language Models](https://arxiv.org/abs/2607.17117)

**<font color=#1a73e8>作者：</font>** Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose language model activations into sparse features, but standard SAEs encode each token independently and do not expose information that persists across a sequence. We introduce Persistent Sparse Autoencoders (Persistent SAEs), which extend standard SAEs by learning a persistence coefficient for each feature, allowing the model to learn which features should persist and for how long. Our experiments show that they retain competitive reconstruction quality while learning a spectrum of feature timescales: fast features behave as locally interpretable detectors, whereas slow features concentrate topic-level information in a persistent state. Moreover, as shown in a prompt-injection monitoring case study, slow features preserve detection signals and remain causally effective over long contexts. These results suggest that Persistent SAEs open up new opportunities for interpreting and monitoring language models through persistent semantic representations.

---


### 98. [Scope3Trace: Evidence-Based Identification and Extraction of Scope 3 GHG Emissions from Sustainability Reports](https://arxiv.org/abs/2607.17122)

**<font color=#1a73e8>作者：</font>** Siyuan Zheng, Yifan Duan, Chao Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scope 3 greenhouse gas (GHG) emissions account for the majority of corporate carbon footprints, yet remain difficult to analyze at scale due to sparse disclosures, heterogeneous report document formats, and limited evidence traceability. Existing approaches typically rely on large language models to extract emissions information from ESG reports, but often lack explicit evidence grounding or depend on costly manual annotation and verification to ensure extraction reliability. To address these challenges, we propose Scope3Trace, an evidence-grounded information extraction framework designed to extract interpretable and traceable Scope 3 emissions information from real-world ESG and sustainability reports. The framework integrates a document information extraction pipeline that performs PDF collection and OCR parsing, LLM-assisted page localization and table reconstruction, and hybrid rule-LLM extraction of organization- and building-level emissions disclosures with evidence-grounded verification. Building upon this framework, we further contribute a dual-level, evidence-grounded, multimodal dataset comprising organization-level Scope 3 disclosures extracted from heterogeneous sustainability reports. Scope3Trace enables reliable extraction and transparent integration of heterogeneous sustainability disclosures, achieving high accuracy in extracting Scope 1-3 totals and category-level disclosures from sustainability reports.

---


### 99. [STBridge: Shared-Target Alignment for Bridging Understanding and Generation in UMMs](https://arxiv.org/abs/2607.17140)

**<font color=#1a73e8>作者：</font>** Ye Wang, Hongjun Wang, Hao Fang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) aim to integrate visual understanding and generation within a single architecture, but architectural unification alone does not ensure semantic consistency. A model may describe the intended target correctly while generating an inconsistent edit. This exposes an understanding-generation alignment gap: linguistic and visual outputs live in different spaces, yet should be governed by the same target semantics. We study this gap in image editing, where an instruction defines a target state that can be both described and visually realized. Given a source image and an edit instruction, we compare a UMM's target caption with its edited image to test whether the two outputs converge on the same result. Our analysis shows that existing UMMs remain weakly aligned, especially for fine-grained entities, attributes, spatial relations, and local details, indicating that semantic unification is not achieved by architecture alone. To bridge this gap, we propose STBridge, a shared-target alignment framework that connects understanding and generation through a common target state. Here the target caption expresses the desired visual result, while the edited image realizes it visually, replacing separate task-specific paths with a shared information flow from target expression to target realization. STBridge follows an align-then-optimize strategy: supervised fine-tuning first establishes the shared-target channel, and sequential reinforcement learning further refines target-centered coordination. Across visual understanding, image generation, and image editing benchmarks, STBridge consistently improves over the initialization model. Alignment analysis confirms that STBridge narrows the gap between what the model describes and what it generates, demonstrating shared-target alignment as an effective post-training strategy for bridging understanding and generation in UMMs.

---


### 100. [Robust Assamese Speech Recognition through Controlled Fine-Tuning of Whisper Models](https://arxiv.org/abs/2607.17164)

**<font color=#1a73e8>作者：</font>** Ganapati Das, Dwipen Laskar, Hasin Afzal Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing Automatic Speech Recognition (ASR) for morphologically rich, low-resource languages such as Assamese is challenging due to insufficient annotated speech data. The pretrained Whisper model performs poorly on Assamese speech recognition tasks. This paper presents a controlled, fine-tuned Whisper-based Assamese ASR system trained on the Mozilla Common Voice 24.0-Assamese corpus. A hardware-aware optimized training pipeline is implemented for resource-constrained environments, employing mixed-precision training and gradient accumulation on Tesla 4 Graphics Processing Units (T4 GPUs). The proposed fine-tuned model significantly outperformed the Zero-shot baseline, yielding Word Error Rate (WER), Character Error Rate (CER), Match Error Rate (MER), and Word Infomation Loss (WIL) of 43.17\%, 13.18\%, 43\%, and 64.81\%, respectively, achieving significant relative improvements of 78.26\%, 93.10\%, 57.0\%, and 35.19\% over the baseline. Semantic evaluation of the fine-tuned model also demonstrates notable improvement over a zero baseline, attaining Bilingual Evaluation Understudy (BLEU) and Metric for Evaluation of Translation with Explicit ORdering (METEOR) scores of 30.81 and 0.5262, respectively. Additionally, the predicted hallucination rate and Real-Time Factor (RTF) are substantially improved by 96.70\% and 32.38\%, compared to the zero-shot baseline.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
