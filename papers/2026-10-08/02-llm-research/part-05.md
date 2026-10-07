# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-303](./part-07.md)

---

### 201. [ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications](https://arxiv.org/abs/2610.08106)

**<font color=#1a73e8>作者：</font>** Langxi Huang, Pingping Zhang, Lanyun Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) advance rapidly, while conventional benchmark development lags behind, delaying investigation of newly observed capability gaps. Such investigation requires an expressive task format and an on-demand construction process: information-rich charts make chart question answering (Chart QA) suitable for probing coupled perception and reasoning. Automated Chart QA construction is intended to shorten the benchmark-development cycle by turning identified gaps into targeted samples on demand. Current methods, however, commonly separate target guidance from scratch generation: target-guided systems often require prepared data, charts, or templates, while scratch-generation systems primarily ensure artifact validity, without explicitly controlling whether newly synthesized requirements and content remain aligned with an externally specified diagnostic target. We introduce ChartBmkAgent, which turns an identified capability gap into targeted diagnostic evidence by constructing complete Chart QA samples from sparse error-taxonomy specifications. Throughout construction, a central harness governs specialized agents, requires stage-specific evidence of alignment with the original error category, and records the basis for each acceptance decision. On 300 taxonomy-wide samples, MLLM accuracies ranged from 32.7% to 84.3% with distinct category profiles, showing that generated samples reveal capability differences. Across three source-model comparisons, targeted follow-ups scored 50.0% versus 82.2% on matched controls ($p=8.96\times10^{-6}$); all six cross-model comparisons had the same direction, demonstrating targeted validation and diagnostic-data generation. Multiple evaluator models assessed whether each sample tested its specified error category; 86.4% met this criterion, providing empirical evidence of target preservation.

---


### 202. [Enhancing Diffusion Language Models with Autoregressive Post-Training Weights](https://arxiv.org/abs/2610.08108)

**<font color=#1a73e8>作者：</font>** Yiming Qin, Ke Wang, Amel Abdelraheem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) have emerged as a promising alternative to autoregressive (AR) language models, offering flexible token-update orders and parallel decoding. Recent dLLMs are often initialized from pretrained AR models before diffusion conversion in order to inherit their learned representations. After the conversion, however, they typically ignore the extensive post-training ecosystem of their AR ancestors. In this work, we show that these existing AR post-training weight updates can instead be effectively recycled to enhance diffusion models. Despite the changes by AR-to-diffusion conversion, directly adding an AR post-training weight update to a diffusion base model remains effective, bringing its performance close to that achieved by direct diffusion post-training. Notably, AR and diffusion post-training updates are nearly orthogonal in weight space, yet induce substantially more aligned representation changes in the diffusion model. Their distinct updates are also complementary: composing their weights can retain gains from both regimes and further improve the post-trained diffusion model. Based on these findings, we propose A2D, a simple training-free framework for enhancing diffusion models with existing AR post-training resources. A2D can transfer capabilities from AR post-trained models to diffusion base models, and further improve already post-trained diffusion models by composing AR and diffusion post-training updates. Across various dLLMs, including Dream, DreamReasoner, DiffuCoder, Dream-Coder, Nemotron-Labs-Diffusion, and DiffusionGemma, A2D reliably improves instruction following, mathematical reasoning, and coding with both supervised fine-tuning and reinforcement learning updates, without additional training, or inference-time computation.

---


### 203. [Do LLMs Act on What They Know? From Partner Representations to Cooperative Actions](https://arxiv.org/abs/2610.08129)

**<font color=#1a73e8>作者：</font>** Yuhwan Jeong, Jinnyeong Yang, Kuk-Jin Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperation with unfamiliar partners requires adapting to communication conventions that are not known in advance. We study this problem in a controlled Hanabi-derived environment with scripted hint generation, LLM-controlled receiving decisions, and frozen model weights. Across eight LLMs, linear probes recover intent conventions substantially more accurately than target conventions, yet receiving choices do not consistently agree with the sender's convention. We compare probe-predicted and ground-truth conventions presented either as general rules or as externally computed action recommendations. Rule statements yield modest and model-dependent changes in cooperation, whereas action translation produces larger gains on average. In a Qwen3-8B case study, matched-state statement reversals reveal much greater sensitivity to action recommendations than to rule statements. Activation transfers from oracle-action and non-oracle hint-restatement donors improve intent accuracy on both action classes, but the tested alternatives do not reliably reproduce these benefits. Together, these results distinguish convention decodability, sensitivity to convention information, and cooperative performance, and highlight limitations in turning available partner information into receiving decisions.

---


### 204. [Penalty-Framed No-Valid-Option MCQA: Analyzing LLM Abstention under Invalid Choices](https://arxiv.org/abs/2610.08153)

**<font color=#1a73e8>作者：</font>** Jinhyeok Kim, Hye-Young Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice question answering (MCQA) is commonly used to evaluate large language models under the assumption that one of the provided options is correct, typically using answer-selection accuracy. However, in real deployments, users or retrieval systems may provide invalid option sets in which none of the listed choices is correct, and selecting one of them may incur downstream cost. We study this setting as penalty-framed no-valid-option MCQA. Using the mathematics subset of MMLU-Pro, we remove the labeled correct option, allow models to either choose a remaining option or output ABSTAIN, and penalize invalid forced-choice responses. We further introduce correct-conditioned analysis, evaluating abstention only on instances that the model originally answered correctly. Experiments show that high MCQA accuracy does not fully guarantee abstention reliability: even under explicit no-valid-option-aware instructions and penalty-based scoring, models still produce invalid forced-choice responses for a subset of originally correct instances. These results show that penalty-framed no-valid-option MCQA reveals an aspect of model reliability not captured by standard answer-selection accuracy.

---


### 205. [Token-Efficient Multi-Agent Collaboration via System One-Guided Computational Division of Labor](https://arxiv.org/abs/2610.08155)

**<font color=#1a73e8>作者：</font>** Zihan Zhou, Xinzhe Hu, Hanxu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) have become a promising paradigm for complex information-seeking and reasoning tasks by enabling collaborative problem solving among specialized agents. However, existing MAS frameworks tightly couple task reasoning with coordination operations, including task selection, role assignment, message routing, and context management. As interactions grow, using powerful LLMs for these bounded control decisions introduces substantial token overhead and latency, limiting the scalability of agentic Web services. In this paper, we investigate whether coordination can be decoupled from expensive reasoning without compromising collaborative performance. We propose S1-MAS, a token-efficient multi-agent framework based on System One-guided computational division of labor. S1-MAS assigns bounded coordination decisions to lightweight System One models while reserving open-ended reasoning for capable LLM workers. Specifically, a lightweight controller selects inspection conditions, chooses subsequent tasks, and determines termination, while a compact reader retrieves condition-relevant evidence from authorized sources to support these decisions. Through a decision-evidence loop, selected tasks dynamically determine worker roles and source access, enabling adaptive collaboration without task-specific training. Extensive experiments on seven diverse benchmarks demonstrate that S1-MAS achieves superior accuracy while substantially reducing the inference cost. Across individual comparisons with AgentVerse, DyLAN, and SelfOrg on seven benchmarks, S1-MAS reduces GPT-4o token consumption by 44.9%-97.2% and measured end-to-end latency by 37.8%-93.0%. These results highlight its potential for scalable and cost-effective agentic Web applications.

---


### 206. [Symphony for Text Generation: Benchmarking Clinical Note Generation](https://arxiv.org/abs/2610.08161)

**<font color=#1a73e8>作者：</font>** Daniel Varab, Victor Petrén Bach Hansen, Asbjørn W. Helge 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ambient documentation systems are rapidly gaining adoption, yet their impact on clinical note quality remains poorly characterized. We introduce MedConv, a multilingual dataset of 300 clinical encounters in English, Danish, and German, and use it alongside the Ambient Clinical Intelligence benchmark (ACI-BENCH) to compare Corti, a clinical AI platform, with two leading, accessible ambient scribe software applications built on general-purpose AI. We present a controlled clinical evaluation framework that combines entailment metrics with LLM-judged pairwise comparisons across eight dimensions adopted from PDSQI-9. Results show that Corti's API-based text-generation infrastructure is on par with or outperforms leading commercial scribes. We further show that Corti's configurable API provides the flexibility necessary to fine-tune quality dimensions for specific documentation use cases. We present the evaluation methodology and release a dataset to support future reproducible comparison of ambient documentation systems.

---


### 207. [The Failure Is in the Readout: Fine-Grained Emotion Recognition Benchmarks Measure Elicitation, Not Perception](https://arxiv.org/abs/2610.08162)

**<font color=#1a73e8>作者：</font>** Tobias Hallmen, Fabian Deuser, Robin-Nico Kampa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained emotion recognition supports therapy tools and social robots, but it needs facial data, which raises privacy and data-protection concerns. EmoNet-Face-HQ answers that with generated portraits, expert-rated over a $40$-category taxonomy far finer than the usual six to eight basic emotions. Under the protocol it ships with, vision-language models (VLMs) score poorly on that taxonomy, and the benchmark concludes that a dedicated fine-tuned model is necessary: Empathic-Insight-Face (EIF; Small/Large). We show that off-the-shelf VLMs match or beat that fine-tuned model when the answer is not generated but read from the logits, as one binary query per category. We keep the benchmark's images, taxonomy and ratings, and change only how the answer is read. Experts agree at $\kappa_w = 0.468$ on the five categories they measure most reliably. Generatively, no interval among eleven open-weight VLMs lies entirely above that anchor ($\kappa_w=0.268$-$0.486$). Under verification all eleven clear it, each of them significantly better at $\kappa_w=0.507$-$0.586$. Three also significantly beat EIF sitting at $\kappa_w = 0.551$ (Small; $0.534$ Large). The gain comes from the graded probability and not from asking a yes/no question: as a control, thresholding those same probabilities to yes/no costs 142% of the average gains and drops binarization below generative elicitation to $\kappa_w=0.254$-$0.423$. A replication on real photographs (FACES) is weaker and mixed: of the ten models that pass a validity gate, six gain, three are neutral to positive and one is negative, so the effect is not confined to synthetic data.

---


### 208. [Align, Then Correct: Training-Free Two-Stage Low-Rank Compensation for Extremely Quantized Large Language Models](https://arxiv.org/abs/2610.08164)

**<font color=#1a73e8>作者：</font>** Seobin Song, Geonho Lee, Janghwan Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank quantization error compensation (LQEC) recovers the accuracy lost under aggressive weight quantization by attaching a closed-form rank-$r$ adapter beside each frozen quantized weight, without any training. We show that existing compensators are limited by two shared simplifications. They calibrate symmetrically, evaluating the full-precision and compensated weights on the same activation, which yields a compensation target that is inherently high-rank -- so a fixed rank budget captures only a small fraction of it. And they minimize only the second-order term of the loss, although the compensated model is not stationary: a first-order descent direction larger than the applied compensation itself remains in every layer, and no reconstruction objective can absorb it. We propose a two-stage closed-form framework that removes both simplifications. Stage 1 aligns each layer's output with the full-precision model under a Fisher-weighted asymmetric objective, concentrating the rank budget on a rank-compressible target. Stage 2 re-measures statistics on the compensated model and applies a rank-constrained natural-gradient step that absorbs the remaining first-order signal. Every adapter is the result of a single truncated SVD; backward passes serve only to collect statistics. At 2 bits under QuIP#, our method reduces WikiText-2 perplexity from 12.43 to 10.26 on Qwen3-8B and from 21.11 to 13.22 on Qwen3-4B. On the held-out C4 corpus, it recovers 51% and 84% of the gap to FP16, versus 31% and 63% for the strongest baseline, with consistent gains in the seven-task zero-shot average, at higher bit-widths, and under a distinct quantizer.

---


### 209. [Visual Orchestration Tax in Agentic VLM Pipelines: Auditing and Certifying Visual Evidence Reuse](https://arxiv.org/abs/2610.08170)

**<font color=#1a73e8>作者：</font>** Lingteng Zeng  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic VLM pipelines increasingly pass the same static visual evidence through multiple specialist agents and tools. This design creates an orchestration-level redundancy mode: semantically unchanged images are repeatedly reconstructed as image-conditioned requests at the VLM API boundary. We call this phenomenon visual orchestration tax and develop a measurement-to-certification framework for visual evidence reuse in agentic VLM pipelines. The audit side defines $\mathrm{M1}_{\mathrm{trace}}$ to count raw visual-evidence touches and M2 to measure structural touch redundancy, with query-level distributions, bootstrap confidence intervals, and paired quality tests. Across SeeingEye and MAMMQA on chart, document, general-VQA, and multi-modal-QA tasks, audits reveal 66.8-75.6% visual-evidence touch redundancy, and every audited query exceeds the predefined gate. The certification side introduces SharedVisCache, a contract-aware evidence reuse hook keyed by image content, preprocessing fingerprint, and encoder assumptions. On SeeingEye, contract validation certifies 75.0-75.5% repeated touches as reusable while preserving 350/350 output strings and $\Delta\mathrm{M5}{=}0$. At the physical layer, certified hits reduce $F_{\mathrm{vision}}$ from 800 to 200 in ChartQA-200 trace replay and from 200 to 50 inside live SeeingEye translator-stage physical integration, preserving 800/800 replay strings and 200/200 integrated call outputs. The results position visual reuse as a measurable, behavior-preserving property of agent orchestration and define an agent-layer contract that makes backend prefix or token reuse semantically interpretable.

---


### 210. [Finding the Heads and the Neurons Responsible for Network Information Retrieval in Language Models](https://arxiv.org/abs/2610.08200)

**<font color=#1a73e8>作者：</font>** Abdul Kadir, Md Mohasin Hossain, Daniel Sonntag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask whether specific attention heads, and more finely specific neurons inside those heads, are responsible for recognizing that a language model's context contains network infrastructure information (a hostname paired with its IP address), and whether that responsibility can be validated causally rather than by correlation alone. At the head level the answer is yes, across five models spanning three architecture families: in every model, a small set of heads (1 to 9 out of 128 to 1152 candidates), found by causal ablation screening and tested for selectivity against matched negative and context-free controls, supports a detector with 99.5--100\% held-out accuracy. We then ask whether a head's responsibility concentrates into one neuron or stays spread across its dimensions; this is model-specific. In one model, the top head's signal concentrates into a single neuron, found independently by both a causal intervention and a correlational ranking, which agree exactly (AUC = 1.000, matching the full head). In another, the single clean head works as a whole (AUC = 1.000) but the best causally ranked neuron inside it does not (AUC = 0.665), so the responsibility there is spread across the head. The remaining three models fall in between. On an independent dataset collected by a different institution (reverse-DNS records rather than the discovery data), every model's full-head detector flags 100\% of positive records; the single-neuron versions transfer less reliably, and in one model score below chance. Causal head-finding for a specific network-information entity works across models and architectures; how far that finding can be pushed down to individual neurons varies, and needs to be checked for each model.

---


### 211. [STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty](https://arxiv.org/abs/2610.08208)

**<font color=#1a73e8>作者：</font>** Nina Nusbaumer, Iria de-Dios-Flores, Corentin Bel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce STRUCTURALCOST, a self-paced reading dataset of 475 participants and 40,800 observations isolating the processing cost of long-distance subject-verb dependency resolution. We replicate a low-powered psycholinguistic finding at NLP scale, namely that human reading times at the main verb increase with dependency length, driven by syntactic embedding beyond linear distance. Different language models -- spanning n-gram models, SSMs, and transformers -- partially mirror this graded difficulty profile, yet underestimate the integration cost humans incur, with a gap that persists across architectures and model sizes. This suggests these models capture the predictive component of human processing but not the full integration cost that working memory imposes. STRUCTURALCOST provides data needed to drive progress toward evaluating the cognitive plausibility of language models.

---


### 212. [Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?](https://arxiv.org/abs/2610.08215)

**<font color=#1a73e8>作者：</font>** Yibo Li, Jinhang Qiu, Zhi Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from experience is essential for LLM agents to adapt to unfamiliar and dynmaic environments. Evaluating this ability is therefore important for understanding how effectively agents acquire and use new knowledge. Existing benchmarks have sought to evaluate this ability, but they primarily evaluate tasks whose rules are provided in the instructions or already familiar to pretrained models, making it difficult to distinguish learning from interactions from reasoning with existing knowledge. To address this, we introduce Learn2Play Bench, a benchmark of newly designed text-based games, whose rules are novel or counterintuitive, requiring agents to acquire knowledge through interaction rather than rely solely on pretrained knowledge. These games provide reproducible feedback and automatic scoring, enabling controlled evaluation of learning across repeated attempts. We also vary game instances to test whether agents can apply what they have learned to new situations. Therefore, we evaluate how backbone models, self-evolving methods, and agent harnesses affect agents' learning ability, revealing three findings: (1) Experience retention: Retaining complete records of actions and feedback can support more effective learning than summarizing these experiences into rules or strategies. (2) Human agent gap: Top-performing human players achieve higher peak scores than the evaluated agents. Human explore more varied strategies, and repeat actions less. (3) Harness matters: With the backbone fixed, changing the harness can improve performance while reducing estimated inference cost. Together, these findings provide insights into how LLM agents learn from experience and suggest directions for future work to improve their learning ability. Project website: this https URL

---


### 213. [OSFP4: Joint Optimization of Diagonal Smoothing and Block Scales for NVFP4 Quantization](https://arxiv.org/abs/2610.08231)

**<font color=#1a73e8>作者：</font>** Neriah Ben David, Ori Meir, Or Ordentlich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> NVFP4 is an attractive datatype for large language model (LLM) inference, offering compact storage and native tensor-core acceleration. However, preserving accuracy using NVFP4 requires careful quantization. In this work we develop a novel quantization scheme called Optimized Smoothing and Scaling for NVFP4 (OSFP4). For each linear projection it uses a diagonal smoothing matrix whose entries are optimized to minimize the squared matrix-product quantization error under NVFP4, taking into account the rounding procedure that is used (either round-to-nearest, or GPTQ-style successive interference cancellation). This requires performing joint optimization on the smoothing entries as well as the block scales, which is facilitated by analyzing a multiplicative-dither FP4 quantizer instead of the fixed deterministic one. Experiments show that OSFP4 achieves the highest average accuracy among the evaluated competitors in the corresponding quantization settings, while retaining approximately 94-97\% of vendor NVFP4 prefill throughput on the measured workloads. Our code is available in this https URL

---


### 214. [LeanPlan: Optimal Planning with LLM-Generated Heuristics and Admissibility Proofs](https://arxiv.org/abs/2610.08246)

**<font color=#1a73e8>作者：</font>** André G. Pereira, Augusto B. Corrêa, Felipe Meneguzzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier large language models (LLMs) can generate heuristic functions that guide search to achieve state-of-the-art performance in satisficing planning, where any plan is acceptable. However, these heuristics are not guaranteed to be admissible and can lead to suboptimal plans. We introduce LeanPlan, the first planning system that finds optimal plans with LLM-generated heuristics whose admissibility is machine-checked. Given a domain description and training tasks, an agentic loop uses planner feedback to iteratively improve a reusable domain-specific heuristic, its admissibility proof and the required domain assumptions. LeanPlan implements the heuristic, its proof and an efficient planner with machine-checked grounding and search in Lean 4. We evaluate LeanPlan on ten domains from the International Planning Competition and three new domains, using test tasks with up to 57 times as many objects as the training tasks. With GPT-5.6 Sol in the agentic loop, we successfully generate heuristics and admissibility proofs for all these domains. With the resulting heuristics, LeanPlan usually expands fewer states than the state-of-the-art Scorpion planner and solves more tasks overall.

---


### 215. [MASC: A Multi-Agent Self-Calibration Framework with Latent Construct Alignment for Consistent Client Role-Playing in Psychological Counseling](https://arxiv.org/abs/2610.08250)

**<font color=#1a73e8>作者：</font>** Shixin Peng, Kun Jiang, Jiaxing Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to simulate clients for counselor training and psychological counseling research, but reliable simulation requires clients to remain psychologically coherent across extended interactions. Existing role-playing methods largely rely on static profile prompts and may exhibit persona drift, unrealistic cooperativeness, or inconsistent psychological states, communicative actions, and emotions. Existing evaluations also lack a unified testbed for both stable client characteristics and evolving psychological dynamics. We propose MASC, a Multi-Agent Self-Calibration framework with latent construct alignment for consistent client role-playing in psychological counseling. MASC combines construct-guided generation, collaborative refinement, consistency verification, and memory-based revision in a closed calibration loop that detects and corrects inconsistencies as dialogue unfolds. We further introduce CRPC-Bench, a benchmark covering session-level profile information and Big-Five personality traits, as well as turn-level psychological state, communicative action, and emotion expression. CRPC-Bench contains 38 motivational interviewing client profiles augmented with personality and emotion annotations. Experiments show that MASC outperforms existing methods across profile, personality, receptivity, and turn-level consistency, with the heterogeneous configuration achieving the strongest overall performance. MASC and CRPC-Bench provide a unified foundation for developing and evaluating psychologically coherent client simulations for AI-assisted counseling research and training.

---


### 216. [zkLLMPoT: Efficient Zero Knowledge Proof of Training for Large Language Models](https://arxiv.org/abs/2610.08258)

**<font color=#1a73e8>作者：</font>** Junkai Liang, Zhanpeng Guo, Pengfei Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Auditing the claimed outcomes of large language model (LLM) training is challenging when model weights and training data are private, while cryptographically proving the full training process is prohibitively expensive at Transformer scale. We present zkLLMPoT, a zero-knowledge framework that certifies auditor-defined properties of a trained checkpoint through forward evaluation rather than verification of its optimization trajectory. zkLLMPoT includes 2 phases: 1) The trainer fixes the architecture and the model weights are committed. Then the auditor selects challenge sequences, preventing the trainer from modifying the checkpoint in response to the audit data. 2) Then the trainer proves the objective value attained by the committed model on those sequences. This formulation makes the certification cost independent of the number of training iterations, without revealing model weights or requiring access to private training data. We build on sumcheck- and lookup-based arguments to certify Transformer computations, while supporting next-token loss and task-specific audit objectives. Across four model families, operator-level benchmarks yield proving times of 41-59 seconds for 1.1-1.5B-parameter models and 131 seconds at 13B for the covered operators, with verification below half a second at a sequence length of 512.

---


### 217. [Memory Depth and Reconstructed Context Width: A Controlled Evaluation of Hierarchical Retrieval](https://arxiv.org/abs/2610.08300)

**<font color=#1a73e8>作者：</font>** Michael Andreev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational memory is becoming an integral component of modern LLM systems. Proposed architectures group records by topics and events, construct hierarchies and graphs, and connect facts through causal and temporal relations. We experimentally study the interaction between two memory parameters: structural depth and the width of context supplied to the answer model. Using EverMemBench, we evaluate depths D1-D4, core budgets of 1,024/2,048/4,096 tokens, and additional Production and Oracle conditions up to the full archive. Increasing width from 1K to 4K improves Accuracy by 10.11-17.98 percentage points, whereas increasing depth provides no monotonic gain. Beyond 8-16K, Production performance reaches a plateau while tokens per correct answer continue to increase; Oracle preserves quality on full archives of 68-71K tokens. These results motivate further investigation of large, coherent context blocks instead of progressively deeper memory structures.

---


### 218. [Language Unalignability: Why Some Concepts Resist Cross-Cultural Benchmark Evaluation](https://arxiv.org/abs/2610.08303)

**<font color=#1a73e8>作者：</font>** Shu-Kai Hsieh, Da-Chen Lian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluation of multilingual Large Language Models (LLMs) rests on an implicit Translation-Isomorphism Assumption (TIA): that semantic structures across languages are congruent and mutually mappable without loss of information. We argue that this assumption is not merely violated in practice, but ill-posed in principle for a typologically identifiable class of concepts, including pragmatic markers, honorifics, and diachronically stratified terms. We formalize this failure using a usage-cloud framework, representing concepts as point sets of contextualized embeddings. We define $\alpha$-unalignability as the impossibility of any mapping that simultaneously preserves lexical faithfulness (centroid correspondence) and structural faithfulness (local neighborhood topology). We provide three layers of evidence. Behaviorally, we show that FLORES-200 translation failures are predicted by language family and resource class but not by script, and that LOBSTER reasoning scores vary by family. Mechanistically, we report a Representation-Intervention Gap (RIG) in a nine-model case study on Yami: the models' activations encode a regularity along which Yami groups with other low-resource and Austronesian languages, yet interventions on language-specific neurons show no demonstrated advantage over random masks: the regularity is visible but not usable by this intervention. Finally, we operationalize these findings into a multidimensional diagnostic profile: Cycle-Consistency, Pragmatic-Load Disagreement, Manifold-Curvature Mismatch, and RIG. We argue that collapsing cultural competence into a single scalar incentivizes "probabilistic flattening," and that recognizing the unalignable class is a precondition for AI that respects, rather than erases, cultural divergence. This suggests that multilingual alignment is not a single well-defined objective, but a set of mutually incompatible projections.

---


### 219. [CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs via Knowledge Consolidation and Decoupling](https://arxiv.org/abs/2610.08312)

**<font color=#1a73e8>作者：</font>** Maoqi Liu, Quan Fang, Yufei He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) is essential for Large Language Models (LLMs) to sequentially adapt to evolving tasks. To mitigate catastrophic forgetting, recent advances implement low-rank adaptation with orthogonal projections (e.g., O-LoRA) to isolate task parameters. However, we reveal that such strict geometric constraints trigger an "Orthogonality Dilemma": rigid parameter isolation impedes the transfer and accumulation of shared representations across semantically related tasks. In this work, we propose a new replay-free method, called Consolidation and Decoupling LoRA (CoDe-LoRA), for CL of LLMs. CoDe-LoRA disentangles the learning process into Consolidating Universal Knowledge and Decoupling Task-Specific Knowledge. To achieve this, CoDe-LoRA leverages an adaptive null space projection mechanism and semantic routing to balance knowledge accumulation with task-specific adaptation. Experimental results across four backbones and three CL benchmarks show that CoDe-LoRA achieves the best average accuracy. Our code is available at this https URL.

---


### 220. [SCOPE: Certified Theorem Proving with a Language Model as the Policy Planner](https://arxiv.org/abs/2610.08319)

**<font color=#1a73e8>作者：</font>** Hanchao Zhou, Jialei Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In proof assistants such as Lean, a generated proof must pass machine compilation checks, so evaluation needs no human scoring. Direct generation fails on multi-step numeric propositions: a proof is valid only if every content integer is correct, so the pass rate is bounded by the k-th power of the per-integer accuracy. Controlled corruption across 2,617 reference proofs confirms this power law. SCOPE (State-Conditioned Operator Planning and Execution) enforces the natural division of labor: the model plans over an operator vocabulary, a symbolic engine executes the numerics, and a compiler renders the proof. On a 218-problem suite it certifies 191/218 (87.6%) with a 135M backbone; the 7B DeepSeek-Prover-V1.5-RL certifies 18/218 at 27.5 times the tokens and 37.5 times the wall-clock, and DeepSeek-Prover-V2-7B certifies zero on a bidirectional dual suite. Multi-step thinking costs 6.12 discrete decision actions per problem and produces no natural-language thinking text. Replacing the lagged engine state in the decision frame with the current one lifts the pass rate from 117/218 to 191/218, while up-weighting the chain-end loss hurts. On the public Lean-Workbook library, 2,132 of 3,536 gradeable admissible problems certify (60.29%) with zero regression on the main suite. All readings come from a version-frozen review with independent rechecks and reverse verification. Restricting free generation and keeping decision-time information visible is a more direct route than enlarging the model.

---


### 221. [MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation](https://arxiv.org/abs/2610.08327)

**<font color=#1a73e8>作者：</font>** Xilin Dang, Weilin Ruan, Xue Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise in medical question answering and clinical reasoning, yet their improvement remains constrained by static parametric knowledge and costly expert supervision. Self-evolving agents offer a promising alternative by enabling models to improve through iterative task generation and problem-solving. However, most existing self-evolving methods are designed for easily verifiable domains such as mathematics and coding, where solutions can be checked by exact answers or executable programs. Medical reasoning is fundamentally different: it is open-ended, knowledge-intensive, and often only partially verifiable. We present MedZERO, a self-evolving framework for open-ended medical reasoning. MedZERO couples an Examiner that generates frontier medical question-option pairs with a Reasoner that solves them through evidence-grounded multi-turn reasoning with external knowledge tools. To support reliable, continual improvement, MedZERO adopts controlled knowledge accumulation, which maintains temporary exploratory knowledge and curated persistent knowledge in reasoning. We evaluate MedZERO on five public medical reasoning benchmarks using 4B- and 8B-scale base models under open-ended evaluation. Across all settings, MedZERO consistently outperforms the underlying base models and prior self-evolving baselines, achieving up to 13.7 average accuracy-point gains over the next-best self-evolving baseline.

---


### 222. [MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization](https://arxiv.org/abs/2610.08330)

**<font color=#1a73e8>作者：</font>** Hun Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proprietary Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet aligning their outputs with diverse user preferences remains challenging. Existing personalization approaches for black-box LLMs often rely on user-specific scoring heads, causing the number of personalized parameters to grow linearly with the number of users and requiring additional adaptation for unseen users. To address these limitations, we propose Mixture-of-Facets (MoF), a scalable personalization framework for black-box LLMs that models user preferences as compositions of shared latent preference facets rather than dedicated user-specific parameters. MoF performs personalization through history-conditioned routing over shared facet heads, enabling personalization for users unseen during training without additional parameter updates. Across diverse personalization tasks, MoF delivers stronger personalization performance while maintaining a more scalable and parameter-efficient design than prior approaches. Additional analysis indicates strong generalization to unseen users.

---


### 223. [Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box Vision Language Models for Autonomous Driving](https://arxiv.org/abs/2610.08331)

**<font color=#1a73e8>作者：</font>** Heyam Bin Jahlan Areej Alhothali Abeer Alhothali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Vision Language Models (VLMs) into sensitive systems introduces critical safety vulnerabilities that remain unexplored in exist studies. While adversarial attack robustness has been extensively studied for image-based models, the susceptibility of VLMs to temporally-aware adversarial attacks against video in driving context poses a distinct and under examined threat. In this paper, we introduce novel adversarial attack against video targeting VLM models used for autonomous driving scenes named Spatial Temporal Coherence Adversarial Attack (STCA). Our attack comprise from three stages: modalities expansion, Spatial attack, and STCA attack. In modalities expansion, we propose caption-guided frame selection method in order to ensure that adversarial perturbation target the most semantically significant frames. this http URL spatial attack, we craft effective perturbation and preserve high similarity. Then the perturbed video generated fed into STCA stage that disrupt cross-frame temporal coherence using motion guided mask. Our method operate under black box threat model against victim target VLMs, relying solely on transferability from white-box surrogate this http URL conduct our experiments on the BDD100K and nuScenes autonomous driving datasets across three VLM models: Video LLaVA-7B, Qwen2.5-VL-7B, and Dolphin. Experimental results demonstrate spatial attack achieves an ASR with high SSIM. Our finding reveal that existing video language model, remain highly susceptible to adversarial attack in autonomous driving scenarios, underscoring the urgent need for robust defense for VLM models.

---


### 224. [DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models](https://arxiv.org/abs/2610.08341)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Changbai Li, Linlin Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent training-free pruning approaches for Multimodal Large Language Models (MLLMs) effectively cut computational overhead by exploiting visual redundancy or text-vision attention. However, they frequently suffer from semantic degradation due to their task-agnostic design or unreliable attention estimates. Based on our empirical analysis, we have found that this issue arises because salient tokens in shallow layers persistently suppress emerging semantic ones through numerical inertia, leading to premature discarding of signals crucial for deep reasoning. To address the aforementioned issue, from the task-oriented aspects, we first reformulate training-free pruning as a minimization of the distortion in the final task loss and derive a tractable, token-wise upper bound to serve as a surrogate objective. Specifically, this formulation inherently reveals a previously neglected inter-layer term that accounts for gradients across layers. Accordingly, for the implementation, we propose DIPrune, a rank-based framework that employs a dual importance scoring mechanism to jointly optimize intra-layer static feature saliency and inter-layer dynamic semantic evolution. Extensive experiments on LLaVA and Qwen-VL demonstrate that DIPrune consistently achieves state-of-the-art results.

---


### 225. [Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations](https://arxiv.org/abs/2610.08364)

**<font color=#1a73e8>作者：</font>** Toby D. Pilditch, Konstantinos Voudouris, Alexandra Abbas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI evaluations increasingly use open-ended, agentic, long-horizon tasks whose transcripts can span hundreds of pages of outputs and actions from complex multi-agent networks. The observability envelop-the range of what evaluators can reliably infer about an agent's behaviours-is therefore narrowing. Language model assistants can help classify and interpret agent behaviour but also afford human evaluators significant analytical degrees of freedom, threatening the reproducibility and auditability of language-model-based transcript analysis. Transect is an open source package built on Inspect Scout to help evaluators understand how a long agent run unfolded, identify behaviour worth investigating, and check interpretations against the transcript. Users specify task context and behavioural vocabulary in a reusable evaluation-family configuration, with judge models and analysis settings supplied separately. Transect's navigable reports align recorded events, token use, sub-agent activity, and model-generated behavioural labels on a common turn-based timeline. Reviewers can quickly grasp a run's narrative, trace any label or event to its source turns, and export the underlying data tables for cross-run analysis. We demonstrate the workflow on an AI R&D evaluation that generated almost 13 million tokens, dividing the agents' work into behavioural phases aligned with research-skill classifications, sub-agent delegations and interactions, and token use. The combined view shows a focus on operational work and manuscript production, with little evidence of a sustained hypothesis generation stage-arguably a necessary component for high-quality scientific outputs. Transect's flexible, customisable transcript-analysis pipeline will enable evaluators to keep pace with longer, more complex, more frequent AI evaluations while supporting scientific rigour, transparency, and reproducibility.

---


### 226. [A Stevens's Power Law Check-up of GPT-5.5's Image-Based Visualization Reading](https://arxiv.org/abs/2610.08365)

**<font color=#1a73e8>作者：</font>** Kaichun Yang, Jian Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We adapt Stevens's power law to measure the innate ability of AI models to read visualizations, which can reveal the built-in perceptual mechanisms of algorithmic models. In our pilot study, models see no legend. A model first views a reference visual representation and estimates its magnitude, then estimates the magnitude of each subsequent image of the same representation relative to that reference. Our evaluation of twelve visual variables makes how algorithmic models read visual encodings measurable, comparable with human perception, and more interpretable to humans.

---


### 227. [Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering](https://arxiv.org/abs/2610.08388)

**<font color=#1a73e8>作者：</font>** Yang Hong, Yajun Yang, Xin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities in question answering, yet they still frequently suffer from hallucinations on knowledge-intensive tasks. Knowledge graphs (KGs) provide LLMs with structured, interpretable, and updatable factual grounding, making them a promising external knowledge source for reliable reasoning. However, existing LLM-guided graph reasoning methods typically rely on hop-wise greedy or beam-style pruning during evidence retrieval. Such local decision processes are inherently myopic: evidence that appears weak near the source may become crucial only after deeper graph context is explored, causing answer-critical branches to be discarded prematurely and making the reasoning chain difficult to recover. To address this limitation, we propose Foresight-over-Graph (FoG), a foresight-aware evidence retrieval framework for knowledge base question answering (KBQA). FoG iteratively constructs a question-relevant evidence subgraph and uses far-to-near feedback to guide path exploration, and maintains a compact memory subgraph to support continued exploration. Extensive experiments on widely used KBQA benchmarks demonstrate that FoG achieves state-of-the-art performance, with a particularly large improvement of 16.58% in Hit on CWQ, while also reducing LLM calls and token usage. Our code is available at this https URL .

---


### 228. [UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.08398)

**<font color=#1a73e8>作者：</font>** Taojie Zhu, Jing Jin, Yuan Xia 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation from multiple teachers combines expertise from different domains in a single student, but conflicting gradients can hinder this integration. Gradient corrections directly constrain parameter updates under plain SGD. With optimizers such as AdamW, however, momentum, adaptive scaling, and weight decay can turn a corrected gradient into an update that increases a domain loss to first order. To address this gap, we propose Update Projection for Multi-Teacher On-Policy Distillation (UP-MOPD). UP-MOPD lets the original mixed gradient update the optimizer state and generate a candidate displacement, then projects only violating candidates before they are committed to the parameters. The projection gives the unique feasible update closest to the candidate in Euclidean distance. In experiments combining medical and general domains, UP-MOPD improves IFEval-loose accuracy late in training by 2.96 points over vanilla M-OPD. It achieves an average score of 60.03 across eight metrics, compared with 59.00 for gradient projection and 59.15 for update rejection. On a public benchmark covering mathematics, code, and instruction following, it achieves the best average across six tasks (32.67), leads on LiveCodeBench v5, and ties for the best IFEval this http URL results support projecting optimizer updates to reduce interference between domains.

---


### 229. [GeoPID: Decomposing and Steering Visual Information in Vision-Language Models](https://arxiv.org/abs/2610.08401)

**<font color=#1a73e8>作者：</font>** Seulgi Kim, Zhixiong Zhang, Xinwei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent vision-language models (VLMs) have shown outstanding performance across diverse applications, they tend to under-use visual information and over-rely on textual context. In this work, we propose \textsc{GeoPID}, a training-free framework that analyzes multimodal information within VLMs from a geometric perspective. \textsc{GeoPID} decomposes information into Redundant, Modality-Unique, and Synergistic components through the geometric relationships between visual and textual representation subspaces. Through an extensive analysis across 22 VLMs and 14 benchmarks, we confirm that correct predictions exhibit stronger vision-unique components when questions strongly require visual grounding. Building on this geometric analysis, we introduce a targeted intervention technique that selectively amplifies visual representations along the vision-unique subspace during inference. As a result, visual grounding capabilities were enhanced without any additional model parameter updates, achieving an average relative accuracy gain of 7.63\%.

---


### 230. [VETTA: Coordinating Turn- and Token-Level Credit Assignment for Multi-Turn LLM Agents](https://arxiv.org/abs/2610.08402)

**<font color=#1a73e8>作者：</font>** Jiaju Chen, Min Yang, Jinghua Piao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn LLM agents often receive sparse task feedback across several interactions, while generating each response token by token. This creates two related credit-assignment questions: which responses helped achieve the outcome, and which generation decisions mattered within each response? Existing methods typically focus on only one level: turn-level methods evaluate complete responses but do not distinguish the decisions within them; token-level methods can propagate feedback across turns but do not explicitly model credit for each response. These complementary limitations motivate learning credit at both levels and coordinating it in a single policy update. We introduce VETTA, a credit assignment method that jointly learns turn- and token-level values through separate heads on a shared lightweight critic. VETTA computes advantages along both temporal sequences and combines each turn advantage with a within-response-centered token residual for PPO updates. Furthermore, to reduce value-learning cost, the critic retains only early Transformer blocks from the pretrained checkpoint used to initialize the actor. On two challenging agent benchmarks, ALFWorld and WebShop, VETTA improves success rates over PPO by 37.5% and 22.3%, respectively, with Qwen2.5-1.5B-Instruct and achieves success rates of 95.5% and 76.0%, respectively, with Qwen2.5-7B-Instruct. Critic-depth comparisons further show strong task performance with substantially lower critic-side computation. These results suggest that a compact shared critic can coordinate turn- and token-level credit to improve agent performance while keeping value estimation efficient. Code is available at this https URL.

---


### 231. [SSR: Sparse Segment Reduction for Ternary GEMM Acceleration](https://arxiv.org/abs/2610.08403)

**<font color=#1a73e8>作者：</font>** Adeline Pittet, Shien Zhu, Valérie Verdan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware. Ternary LLMs mitigate these demands through weight quantization via ternary values, achieving significant compression often with 50-90% sparsity. However, existing approaches have limitations: methods optimized for ternary weights, such as BitNet, redundant segment reduction (RSR), and its improved version RSR++, do not exploit sparsity structures, while conventional sparse formats neglect ternary characteristics, foregoing dual optimization opportunities.
In this paper, we introduce Sparse Segment Reduction (SSR), a ternary matrix multiplication method designed to accelerate the inference of ternary LLMs and general Ternary Weight Networks (TWNs). SSR has a dedicated optimized ternary data format and an algorithm that systematically exploits sparsity patterns through computation trees that scale with the sparsity. SSR provides theoretical gains with asymptotically faster inference than RSR++ for sparsity above 50%, while practical evaluations reveal performance improvements across all sparsity levels. Evaluation results show that SSR achieves 2.1-11.3x speedup over RSR++ on ternary GEMM with 45-95% sparsity. Furthermore, SSR achieves 3.5-6.3x end-to-end speedup and 4.9% of memory saving over RSR++ on the Llama-3 1B model inference.

---


### 232. [Case-Level Verification in Scanner-LLM Cascades: Overcoming the Alert Aggregation Bottleneck to Expand the FRR-TPR Trade-off Space](https://arxiv.org/abs/2610.08406)

**<font color=#1a73e8>作者：</font>** Hao Sun, Yibin Yao, Chaohai Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dynamic Application Security Testing (DAST) scanners achieve high recall but also produce a large number of false positives, resulting in substantial manual triage costs. Large Language Models (LLMs), when used for independent detection, achieve extremely high recall (95.4%-100%) but also exhibit prohibitively high false positive rates (49.6%-85.0%), precluding their use as standalone replacements for scanners. A natural solution is a two-stage cascade consisting of scanner detection followed by LLM verification. However, a verification-granularity issue that has long been overlooked in practice creates a structural bottleneck: alert aggregation binds multiple true and false cases into a shared decision unit, such that removing a false positive inevitably eliminates true positives aggregated within the same alert group. This creates a trade-off bottleneck between the False-positive Reduction Rate (FRR) and the True-positive Rate (TPR). We formalize this bottleneck by showing that the alert-level false-positive set is a subset of the case-level false-positive set, and introduce a Case-Level, per-case verification strategy that shifts the decision granularity from the alert level to the instance level, independently replaying HTTP requests and making an independent determination for each detected case. Evaluation on the dual testbeds of Damn Vulnerable Web Application (DVWA) and WebGoat shows that the empirically best Alert-Level operating point achieves FRR=42.86% (TPR=51.7%). The Case-Level Baseline achieves FRR=47.6%, an improvement of 4.7 percentage points (+4.7 pp), while the Case-Focused Evidence Verification Prompt (CEV-Prompt) increases TPR from 55.2% to 62.1% at the same FRR.

---


### 233. [Knowing When Not to Answer: Cross-Domain and Multi-Turn Generalization of Latent Underspecification Signals](https://arxiv.org/abs/2610.08413)

**<font color=#1a73e8>作者：</font>** Jerzy Kamiński, Ilya Galyukshev, Artem Kuznetsov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models routinely answer questions that cannot be answered from the information given, and in dialogue they answer before enough has been said. Unanswerability is linearly decodable from hidden states, but it is unclear which of its forms share a representation and whether the signal is useful in dialogue. We contribute a turn-labeled multi-turn benchmark (423 conversations, 1,661 labeled turn-states) and an evaluation harness with a simulated user who answers clarifying questions, and use them with six datasets and six open-weight LLMs to test how far probes for unanswerability carry. Probes transfer robustly between datasets that share a ground of unanswerability: missing information in math (AUROC 0.77-0.97) and in a passage (SQuAD 2.0<->MuSiQue, 0.77-0.90). Probes for epistemic "known-unknowns" transfer poorly to math, but this separation weakens under lexical controls and changes with layer and coordinate system, so it remains unresolved. Single-turn probes fail zero-shot to detect when a conversation becomes answerable; in-structure probes recover it, but no better than a bag-of-words classifier. A gate on the calibrated probe, with no model fine-tuning, fires on underspecified turns far more precisely than chance, and its end-task success comes within 0.08 of a gate given the true labels. Yet across four models it does not reliably beat vanilla generation or prompted consolidation. The remaining gap lies mostly in how models use a clarification, not in detection.

---


### 234. [Image Bitstream Fine-grained Understanding for Privacy-Friendly AIoT](https://arxiv.org/abs/2610.08414)

**<font color=#1a73e8>作者：</font>** Zhen Yu, Wenyang Liu, Kejun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image Bitstream Fine-grained Understanding (IBFU) aims to directly perform fine-grained classification and semantic description generation from encoded image byte sequences. In contrast to conventional pixel-domain visual understanding, IBFU conducts semantic analysis without fully decoding images into the pixel domain. Since pixel-level visual content is not explicitly reconstructed during inference, this paradigm reduces visual exposure within the processing pipeline and suits privacy-friendly Artificial Intelligence of Things (AIoT) applications. In this paper, we propose Bitstream Fine-grained Generator (BFG), a novel foundation model tailored for IBFU. BFG consists of two main components: a Bitstream Semantic Encoder (BSeE) and a Fine-grained Semantic Generator (FSeG). BSeE directly models semantic representations from encoded image bitstreams without explicit pixel reconstruction, while FSeG transforms the extracted bitstream semantics into detailed natural-language descriptions through autoregressive generation. To train BFG and comprehensively evaluate IBFU in practical AIoT scenarios, where image bitstreams may suffer corruption during transmission and storage, we construct a large-scale Corrupted-bitstream Fine-grained Understanding dataset (CFU-D), containing both intact bitstreams and corrupted variants across multiple corruption types and severity levels. Experiments show that BFG maintains stable fine-grained caption generation under bitstream corruption. For example, the performance only has slight change from 0.6339 to 0.6077 in terms of average CIDEr score on Stanford Dogs Caption dataset, while vision-language models, such as Qwen-VL-Chat, BLIP-2, GLM, Gemini, and GPT suffer severe performance decrease. This paper provides a practical paradigm for privacy-friendly fine-grained understanding in AIoT.

---


### 235. [EMHO: EMbodied Agent Harness Optimization via Experience Traces](https://arxiv.org/abs/2610.08432)

**<font color=#1a73e8>作者：</font>** Hyun Jung Lee, Jungtaek Kim, Jongwon Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving embodied agents often focuses on optimizing the underlying model through training, while the surrounding agent harness that controls planning, context, and tool use is typically engineered. We ask whether this harness can instead improve itself directly from experience traces under sparse environmental feedback. We propose EMbodied Agent Harness Optimization (EMHO), a self-evolving framework that keeps the embodied model frozen and iteratively revises its harness by analyzing execution trajectories and prior harness history. EMHO optimizes beyond skills or recovery prompts, modifying how the agent monitors progress, uses vision tools, grounds observations, and responds to failures. To support multiple subtasks with a single harness, we introduce EMHO-Merge, which addresses trade-offs in jointly optimizing a single shared harness across subtasks by using episode-level gains and losses to guide evidence-supported refinement of when and how revised behaviors are applied. We evaluate EMHO on EmbodiedBench across navigation and manipulation tasks, and EMHO consistently improves task success for both Qwen 9B and 27B models. Qualitative analysis shows that EMHO goes beyond recovering from failures and unproductive actions to reshape how the embodied agent interprets and interacts with its environment.

---


### 236. [AssemState: Manual and Physical-State-Guided Reasoning for Zero-shot Furniture Assembly](https://arxiv.org/abs/2610.08446)

**<font color=#1a73e8>作者：</font>** Zhiyuan Qi, Jierui Li, Yifan Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made significant progress in visual understanding, but precise 3D spatial reasoning integrated with physical environment remains difficult. Furniture assembly requires not only recovering step-level operations from diagrammatic manuals, but also translating semantic attachment relations into 6D pose updates that enable parts to physically interact with the environment and previously assembled components. To study this problem, we propose AssemState, a zero-shot framework for manual and physical-state-guided furniture assembly. It firstly employs anchor-guided boundary assembly states to decompose manual pages into single-part operations and recover an assembly-tree. Then, it uses iterative after-state feedback refinement to guide successive (SE(3)) updates and corrections, and validates their physical plausibility through simulation-based release tests. Experiments show that compared with the strongest prior baseline, AssemState improves F1 from 38.58\% to 62.80\% and Tree Exact Match from 28.24\% to 53.92\% for assembly-tree recovery. On 243 independently evaluated part-level operations, our proposed iterative refinement improves judge-accepted operations from 0 to 5.3\% and reduces mean Chamfer distance from 5.4111 to 1.7744. However, visually plausible candidate poses may still suffer from collision, floating, mirror-orientation errors, incomplete seating, and wrong-side attachment. These results show that AssemState improves operation-structure recovery and selected local pose metrics, while MLLMs remain limited for spatial relationship reasoning.

---


### 237. [Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability](https://arxiv.org/abs/2610.08448)

**<font color=#1a73e8>作者：</font>** Bingxi Hou, Guochao Jiang, Guofeng Quan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) trains a student on its own generations using teacher feedback. With different tokenizers, comparing teacher and student predictions requires alignment at both sequence and vocabulary levels. In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1 groups already cover most student-generated tokens despite substantial vocabulary mismatch. On responses sampled from the students before distillation, the shared vocabulary retains nearly all teacher and student probability mass at strictly aligned positions on average. Restricting reverse KL to a student-selected top-16 subset of the shared vocabulary at each strict position achieves accuracy comparable to full shared-vocabulary OPD, outperforming the evaluated cross-tokenizer baselines. Adding mean squared error supervision on span log-probabilities in mismatch groups gives complete supervision coverage, yet reduces accuracy. At checkpoints from training with only the strict loss, the span gradients show weak or negative directional agreement with the strict gradients and grow in magnitude relative to them. These diagnostics may help explain the accuracy drop from adding span supervision. Our findings motivate a shift from maximizing alignment coverage to prioritizing supervision reliability: compact supervision at strict positions can be more effective than broader coverage that introduces weakly aligned or conflicting training signals.

---


### 238. [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents](https://arxiv.org/abs/2610.08452)

**<font color=#1a73e8>作者：</font>** Lasse B. Strand, Robert Jakob, Kevin O'Sullivan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is a widely used approach for grounding large language models (LLMs) in external knowledge. However, configuring a pipeline is an expensive hyperparameter optimization problem over many interacting choices, from chunking and embedding model to reranking and generation. Existing optimizers, from greedy search to Bayesian optimization, reduce each trial to an aggregate score and search without modeling why a configuration performed as it did, even though the retrieved chunks already provide evidence about whether each failure occurred during retrieval or after it. We introduce Agentic AutoRAG, an LLM-agent optimizer for multi-objective RAG hyperparameter optimization with retrieval-versus-generation failure attribution. It proposes configurations scored on a frozen exam from the corpus: after each trial a Diagnoser attributes each failed question to retrieval or generation, and a Proposer, grounded in a knowledge base of model rankings and pricing, selects the next configuration, weighing accuracy against cost to trace a Pareto frontier. On three multi-hop QA benchmarks it reaches higher LLM-judge accuracy than every baseline we compare, and within its first 10 trials it matches or beats the statistical baselines' full 30-trial judge accuracy. In its cost-aware mode on a real-world healthcare corpus it reaches a median exam accuracy of 77%, above the strongest baseline's 71.5%, at about 58% of that baseline's cost per query, and it matches that 71.5% at about 22% of the cost.

---


### 239. [UNREAL: Unifying Retrieval and Long-Context with a Single Model](https://arxiv.org/abs/2610.08463)

**<font color=#1a73e8>作者：</font>** Edan Kinderman, Elad Hoffer, Yochai Blau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales, from a single long prompt to an entire corpus. We ask whether a single model-internal mechanism can select evidence across this range. We introduce UNifying REtrieval And Long-Context with a Single Model (UNREAL), a model-native evidence selection framework to span corpus retrieval and long-context inference. UNREAL encodes chunks and derives retrieval queries directly from the frozen LLM's internal representations. It adds fewer than 500K trainable parameters and leaves the backbone unchanged. On a 3B-token, 21M-chunk Wikipedia index, all four dense and hybrid UNREAL backbones outperform state-of-the-art retriever-reranker systems. The best model raises recall from 49.1% to 73.2% on HotpotQA, from 31.7% to 60.1% on 2WikiMultiHopQA, and from 8.8% to 14.4% on MuSiQue. Applied to long-context tasks, the same selection mechanism removes distractors before generation, raising NoLiMa accuracy from 1.0% to 24.83% at its maximum context length of 128K tokens, and LV-Eval's F1 score from 49.97% to 54.66% at 256K. UNREAL also reduces FLOPs and time-to-first-token relative to full-context inference from roughly 32K tokens onward, with larger gains as context grows. Together, these results establish model-internal evidence selection as a common foundation for corpus retrieval and evidence-sparse long-context inference.

---


### 240. [Knee3DVLM: Dual-Sequence Full-Volume Vision-Language Modeling for Comprehensive Knee MRI Assessment](https://arxiv.org/abs/2610.08482)

**<font color=#1a73e8>作者：</font>** Maryam Baizhigitova, Andrew Seohwan Yu, Po-Hao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly being applied to three-dimensional medical imaging, but their application to knee MRI remains limited, particularly for interpreting the complementary sequences used in clinical practice. We introduce Knee3DVLM, a sequence-aware VLM that uses full-volume DESS and fluid-sensitive TSE MRI to predict 57 anatomically resolved binary diagnostic targets derived from the MRI Osteoarthritis Knee Score (MOAKS) for structured reporting. We evaluated DESS-only, TSE-only, and paired DESS-TSE configurations using subject-disjoint Osteoarthritis Initiative partitions. In a held-out cohort of 1,074 examinations, the fused model achieved 72.98% average accuracy, 71.17% balanced accuracy, 78.96% mean ROC-AUC, and 78.74% macro ROC-AUC, the highest values among the three configurations. In a secondary multiclass analysis aligned with the released 3DReasonKnee cohort, Knee3DVLM was numerically higher than the strongest reported 3DReasonKnee configuration across five pathology categories. These findings support dual-sequence full-volume modeling for comprehensive knee MRI assessment.

---


### 241. [Language-model ratings of depression reflect the rater more than the patient](https://arxiv.org/abs/2610.08501)

**<font color=#1a73e8>作者：</font>** Baihan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver operating characteristic curve (AUC) >= 0.70 disagreed on screening decisions for 40% of participants, on average. Average over-rating governed how many were flagged, yet equal-capacity raters chose differently for about one participant in five. A locked analysis of 86 new interviews reproduced the main pre-registered findings. Exploratory recalibration with 40 labelled participants raised accuracy from about 60% to 75% and halved disagreement, leaving one participant in five decided differently. Calibration repaired much of the rater dependence without securing agreement about individuals.

---


### 242. [Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions](https://arxiv.org/abs/2610.08513)

**<font color=#1a73e8>作者：</font>** Dennis Fucci, Andrea Bacciu, Dong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from Wikipedia Talk pages across five languages spanning two language families: Germanic (German, English) and Romance (Spanish, French, Italian), paired with personas derived from real user communities and encompassing sociodemographic attributes, self-descriptions, and behaviorally grounded interaction traits. Using Wiki-Talkie, we evaluate agent interactional behavior on a next-turn generation task across various persona conditioning strategies. Our evaluation assesses whether agents collectively reproduce the distributional behavioral patterns observed in human discussions. Results show that user's comment history exemplifying interaction behavior consistently outperforms explicit persona information. In addition, models systematically underproduce negative or extreme sentiments, while over producing references and suggestions, revealing biases toward agreeableness and positivity. Crucially, these patterns hold robustly across languages, with small cross-lingual differences.

---


### 243. [How Much Evidence Should a Coding Agent's Self-Correction Carry? Adaptive Dirichlet Evidence for Self-Distillation](https://arxiv.org/abs/2610.08514)

**<font color=#1a73e8>作者：</font>** Yunbo Long, Guangya Hao, Yuhan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Execution feedback lets coding agents revise programs and learn from their own corrections. A correction's learning weight should reflect both the transitions supported by its executions and the amount of evidence behind that support. We introduce Effective-Evidence Self-Distillation (EESD), which represents these quantities separately. Normalized execution relevance determines relative transition support and an effective pseudo-count mass; a Dirichlet posterior then produces an uncertainty-penalized weight for KL-anchored correction learning. Under a symmetric prior, changing mass preserves category ordering, and effective mass yields a supervised coefficient bounded by its matched fixed-mass counterpart. Across four model-domain history sweeps, increasing visible observations from one to eight reduces future-outcome NLL by 55.0-59.3%. At eight observations, effective mass achieves lower NLL than fixed mass in all four comparisons. In the primary matched DeepSeek/RunBugRun study, argmax predictions agree on all 3,000 examples, with the largest NLL gain under concentrated relevance. After one correction-learning round, DeepSeek/CodeARC all-tests Pass@1 increases from 15.0% to 20.4%, with a paired 95% source-bootstrap interval of [+2.8, +8.0] percentage points. The twelve-setting downstream evaluation establishes the model-domain scope of this update. These results show how separating evidence support from evidence mass changes probability estimation and correction learning in coding agents.

---


### 244. [How Bregman Divergences Shape Shampoo](https://arxiv.org/abs/2610.08534)

**<font color=#1a73e8>作者：</font>** Bing Liu, Wenjie Zhou, Chengcheng Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the principles behind Shampoo has recently guided the development of more effective neural network optimizers. These methods learn a preconditioner by optimizing the Frobenius or Kullback-Leibler (KL) divergence against the gradient second moment. In this work, we investigate how the choice of divergence shapes preconditioning, which remains unclear and blocks further improvements. To do so, we develop a unified Bregman divergence framework that connects all popular divergences, allowing us to study them jointly. Through empirical spectral analysis of gradient second moments, we examine how divergence choice shapes Kronecker approximation and interacts with finite-sample error in preconditioning. We find that some divergences can better compensate for finite-sample underestimation of the empirical second moment, helping explain the differing behavior of their corresponding Shampoo variants. We further validate this explanation through GPT-2 pretraining experiments. By connecting divergence choice to practical training behavior, we believe our framework provides principled guidance for understanding the foundations of, and further improving, Shampoo.

---


### 245. [RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models](https://arxiv.org/abs/2610.08539)

**<font color=#1a73e8>作者：</font>** Dongchen Si, Di Wang, Mingzhen Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing scene classification is a fundamental task in Earth observation and geospatial analysis. Existing approaches mainly follow three paradigms: task-specific visual classification, vision-language similarity matching, and autoregressive multimodal generation. However, visual classifiers rely on predefined label spaces, CLIP-based methods perform recognition through static image-text alignment, and multimodal large language models (MLLMs) introduce unnecessary token-level generation for classification tasks with explicit candidate categories. To address these limitations, we propose RSJEV, a one-pass multimodal decision framework for remote sensing scene classification. Unlike conventional MLLMs that formulate classification as autoregressive text generation, RSJEV reformulates scene classification as a candidate-conditioned multimodal discriminative decision process, where visual representations, task instructions, and candidate category semantics are jointly modeled. Specifically, we introduce a OnePass Decider that extracts multimodal decision states and directly estimates category probabilities within the candidate category space, eliminating autoregressive decoding while preserving vision-language interactions. Extensive experiments on three widely used remote sensing scene classification benchmarks, including UC Merced, AID, and NWPU-RESISC45, demonstrate that RSJEV achieves superior classification performance compared with representative CNN-, Transformer-, Mamba-, CLIP-, and MLLM-based methods. Moreover, RSJEV significantly reduces inference costs and achieves a better accuracy-efficiency trade-off with only a compact 0.8B-parameter model. These results demonstrate the effectiveness of state-conditioned multimodal decision making for efficient remote sensing image understanding. The code will be available at this https URL.

---


### 246. [Toward Alignment Scaling Laws: A Framework and First Preregistered Measurements](https://arxiv.org/abs/2610.08540)

**<font color=#1a73e8>作者：</font>** Jeremy Canale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether alignment gets easier or harder as models grow is often argued from isolated findings, as if alignment were one property. We treat it as a family of measurable scaling relations: for each risk category r, the alignment burden needed to hold a fixed safety target is modeled as B_r(N)=a_rN^alpha_r, with N a capability proxy; against a budget proportional to N, scaling helps if alpha_r<1, keeps pace if alpha_r~1, and accumulates alignment debt if alpha_r>1. We give three operationalizations of burden and distinguish observed, audited and true alignment. A toy model, in which corrections consume capability headroom, makes the consequences explicit. We prove that the largest exponent among corrected risks, not an average, sets the long-run regime; that above 1 any policy holding headroom above a floor must grow super-exponentially; that, for burdens that are positive mixtures of power laws, fits on small models underestimate large-scale exponents; and that an audit that uncovers hidden failures without false positives never underestimates true alignment. We propose a pre-registrable protocol and apply reduced versions of it twice. A preregistered reanalysis of public adversarial-training data for Pythia classifiers finds that the compute needed to bring attack success under 10% grows as N^0.60. A preregistered pilot on Qwen2.5 0.5B-72B finds exponents of -0.05 for truthfulness and 0.48 for stated dispositions (both scaling helps under its reduced rule, though local slopes approach 1 at the top; replicated on Qwen3 0.6B-14B), while sycophancy (0.89, or 0.83 with two seeds added at 72B) and a planted backdoor are undetermined: the backdoor is removed quickly when its trigger is known but survives blind safety training at four of five sizes. We release four browser games that play these laws (this http URL). We make no claim about which regime holds for current frontier models.

---


### 247. [How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing](https://arxiv.org/abs/2610.08544)

**<font color=#1a73e8>作者：</font>** Pranjal Garg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input already gives away, and the same score can mean different things on different data. We propose reading every probe score against two reference points: a floor, what a declared set of simple inputs already predicts, and a ceiling, what the full input can predict. The gap between them, the headroom, is the range in which a probe can show that a model computes something beyond the simple inputs. We prove that headroom vanishes in two ways: the target stops depending on a hidden variable the model must infer, or the input stops revealing it. We test this on transformers trained for in-context meta-analysis, which must infer the hidden heterogeneity between studies to weight them correctly, and where both reference points are known. Under distribution shift, probe scores fall and prediction error rises $12$--$15\times$, yet the model recovers a similar share of the headroom, indicating that the data lost information, not the representation. We then analyze the real models. The single-cell foundation model scGPT encodes biological variability only partially. We also revisit four influential LLM probing studies, which claim that models represent geography, the state of an Othello board, truth, and the demographics of their users. Against a floor computed from the input text alone, some of these claims hold, while others are largely explained by the text itself.

---


### 248. [Latent space bias directions in LLMs capture confidence, not fairness](https://arxiv.org/abs/2610.08559)

**<font color=#1a73e8>作者：</font>** Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activations of anti-biased and biased prompts, and evaluate it as a steering intervention across bias and general knowledge benchmarks. We find that this direction is dominated by model confidence, pointing from regions of high to low-probability tokens in activation space rather than encoding a meaningful representation of model bias. Steering along it does reduce measured bias, but this is a consequence of reducing model confidence: on QA benchmarks we find that this steering drives the model to abstain from answering, with a side effect of improving fairness metrics. Our experiments show that model confidence is the dominant separating factor between biased and anti-biased prompts in hidden space, indicating that isolating a linear representation of bias which is disentangled from model confidence is difficult and steering-based debiasing results should be interpreted with care. In short, steering appears to reduce bias, not by correcting the model's underlying preferences, but by making it less confident, even on tasks unrelated to bias.

---


### 249. [Have I Seen Enough? Frozen Video-Language Models Encode Evidence Readiness](https://arxiv.org/abs/2610.08560)

**<font color=#1a73e8>作者：</font>** Dan Ben-Ami, Kobi Cohen, Chaim Baskin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video-language models must decide not only what to answer, but whether the evidence needed for the current question has arrived. Existing systems learn that decision as a separate trigger; we ask whether an unmodified model already computes it. We show that frozen VideoLLMs carry a linearly readable evidence-readiness signal, labelled from timestamped evidence rather than from model output. It decodes in all seven models of a shared byte-identical evaluation (AUROC 0.733-0.905 under the strictest not-ready sampling, where a fitted clock is near chance), and a probe fitted without any of a benchmark family's footage still reads that family. It is question-conditioned: on byte-identical windows, changing only the question reverses the readout on 66.1% of pairs, while every question-blind control is at chance by construction. The model can answer incorrectly and still encode readiness: AUROC remains 0.722 among wrong answers. Readiness also beats uncertainty estimators and their supervised combination on latency-matched answer selection, and tracks independent human judgments more closely than confidence. Released streaming triggers are also linear readouts, yet a trained trigger read on its own base model's activations is approximately orthogonal to readiness and decodes it far less accurately than a probe. We turn the readout into Readiness Gating, an answer-timing policy that improves accuracy by up to +9.75 pp at matched video duration with negligible computational overhead. How much it gains varies with the accuracy headroom the task makes available: across 26 configurations the gain tracks that headroom, and an intervention that moves it over identical pixels moves the gain with it.

---


### 250. [Reinforcement Learning for Hierarchical Reasoning Rewards: Minimax-Optimal Rates with Transformers](https://arxiv.org/abs/2610.08561)

**<font color=#1a73e8>作者：</font>** Naoki Nishikawa, Taiji Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a standard tool for post-training language models on reasoning tasks, where the policy is updated by reward feedback while exploring the space of responses. Despite its empirical success, theoretical understanding of RL post-training remains limited, in particular of why on-policy exploration combined with a neural reward model is effective. In this paper, we address this question by modeling the reward as a hierarchical function on the response space: the reward consists of infinitely many local components, each of which becomes relevant only after the preceding ones have been resolved. We show that a natural Transformer-based actor--critic algorithm, which alternates between sampling from the current KL-regularized policy, fitting a Transformer critic to the observed rewards, and updating the policy, achieves the minimax optimal rates in the query budget and in the regularization strength up to logarithmic factors, and is minimax optimal for a fixed number of prompts. In contrast, we prove that sampling from the fixed reference distribution, as in offline reward modeling, can limit regret decay to a logarithmic rate. These results show that on-policy exploration progressively zooms in on the region where the reward is concentrated, and quantify its benefit for RL post-training.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-303](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
