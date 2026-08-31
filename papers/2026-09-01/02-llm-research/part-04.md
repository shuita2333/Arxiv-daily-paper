# 🧠 大模型相关研究 | 2026年09月01日

> 本类共 **176** 篇论文：已确认 **168** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

---

### 151. [Sliding-window beats linear attention](https://arxiv.org/abs/2608.28444)

**<font color=#1a73e8>作者：</font>** Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy. Every new token costs more than the previous one. For each additional token, the keys and values must be stored in memory indefinitely, which is unsustainable.
Several alternatives have been proposed to fix the quadratic scaling problem, one of which is retrofitting LLMs to use Linear Attention. This idea has attracted a lot of attention, given its promise to solve the quadratic scaling problem with state-of-the-art performance at low cost. However, this line of research has not been properly compared to simpler baselines.
In this work, we show that Sliding Window Attention (SWA) with sinks performs as well or better than post-trained Linear Attention models. We observe this across multiple LLMs on various downstream tasks. For long-context reasoning tasks (Needle-in-a-Haystack and BABILong), SWA achieves massively higher performance (2 to 10 times higher than linear attention). SWA requires no post-training, is extremely fast, and requires low memory; therefore, making it an extremely cheap and reliable solution.
To reduce inference memory cost, we strongly recommend switching to SWA instead of post-training linear models. Linear attention models may have shown some promise, but they likely require to be trained from scratch or extensive post-training in order to even match SWA.

---


### 152. [Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning](https://arxiv.org/abs/2608.28447)

**<font color=#1a73e8>作者：</font>** Minghui Xu, Zi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current large language models (LLMs) increasingly benefit from external tool integration, especially for tasks requiring reliable computation and verification. Motivated by this, we study calculator tool calling for improving mathematical reasoning on the Countdown task. We first analyze reasoning failures and find that calculation errors account for a substantial portion of incorrect responses. We then construct supervised fine-tuning datasets to teach the model useful tool-use patterns and how to interpret returned outputs. Building on this tool-formatted policy, we apply several on-policy reinforcement learning methods, including RLOO, RLOO++, GRPO, and DAPO, using automatically verifiable final-answer rewards. To enable a more reliable evaluation, we construct a fresh 1,024-problem held-out Countdown benchmark with no exact overlap with the training data. Our results show that calculator tool integration consistently improves both SFT and RL baselines, yielding roughly 10 percentage-point gains across pass@k. Among the RL methods, Tool-DAPO achieves the strongest performance, improving pass@1 from 35.8% for Tool-SFT to 66.0%. Further analysis shows that RL encourages more effective tool use even when only final-answer rewards are provided. These findings suggest that tool integration reduces arithmetic and verification errors, while RL increases the probability of correct reasoning traces.

---


### 153. [ARC-CT: Anatomy-Routed Contrastive Vision-Language Learning for 3D Chest CT](https://arxiv.org/abs/2608.28455)

**<font color=#1a73e8>作者：</font>** Huseyin Umut Isik, Mehmet Alp Ozaydin, Sila Kurugol 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language learning uses paired chest CT volumes and radiology reports to learn abnormality classifiers without manually annotated labels. However, two characteristics of chest CT challenge conventional global contrastive learning. First, many critical abnormalities are small or anatomically localized, and pooling an en- tire volume into a single embedding may dilute their visual evidence. Second, the standard contrastive objective treats every other scan in a batch as a negative. Because many chest CTs share abnormalities, this objective incorrectly pushes co-positive pairs apart. We propose Anatomy-Routed Contrastive Learning for 3D Chest CT (ARC-CT), a region-aware framework that addresses these limitations using only la- bels extracted from reports by an LLM, with no manual annotations or bounding boxes. ARC-CT combines three components: (1) an Anato- myQFormer localizing evidence via queries constrained by automatically generated organ masks; (2) a label-Jaccard soft InfoNCE objective in- tegrating the standard one-hot target with the label-set overlap of each pair, which reduces false-negative penalties between studies that share clinical findings; and (3) an organ-level alignment loss connecting mask- pooled visual features to organ-specific report text extracted offline with a large language model. ARC-CT achieves a 0.86 mask-free macro AUC across 18 abnormalities using a compact 3D ResNet-18 backbone. Over- all, ARC-CT outperforms both comparable efficient baselines and sev- eral larger transformer models. Our code and weights are available at this https URL.

---


### 154. [Stranger, Fan, or Peer? A Systematic Study on the Role of Interlocutor in Persona-Based Dialogue Generation](https://arxiv.org/abs/2608.28467)

**<font color=#1a73e8>作者：</font>** Daniela Occhipinti, Malvina Nissim, Marco Guerini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona-based dialogue systems are usually conditioned on speaker biography, but dialogues involve at least two participants, and who has access to whose biography can vary across training, inference, and evaluation. Prior work often neglected these aspects, obscuring mechanisms that only appear when biography visibility is toggled separately across training, inference, and evaluation, a three-stage factorisation that prior work has largely treated as a single factor. We study this factorisation on a dataset of dialogues paired with speaker's biographies, varying whether the target and interlocutor speakers see each other's biographies during training and inference, and using an LLM as a judge to perform author identification. We find that (i) training-time visibility, more than inference-time visibility, determines whether models express persona traits through dialogue or fall back on copying biographical text (a known problem/phenomenon in persona-based generation); (ii) models trained with interlocutor-biography visibility copy less target-biographical text than models trained without it, while changing visibility only at inference time has a less consistent effect; and (iii) under asymmetric disclosure, where only the interlocutor sees the target biography, target content leaks into interlocutor turns more often, and dialogues containing such traces are easier for the judge to identify, especially when interlocutor turns are visible. These results suggest that biography leakage into generated turns is an artefact of how interlocutor visibility is configured across training and inference, and separating the three stages is necessary.

---


### 155. [COVER: Identifiable Evaluation of Coalition Routing](https://arxiv.org/abs/2608.28475)

**<font color=#1a73e8>作者：</font>** Raghul Sugumar, Amrit Gopinath  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a multi-agent system changes its team, it also changes the messages and final answer it produces, so an end-to-end accuracy gap does not by itself identify a routing effect. We introduce method, an evaluation contract that fixes a public information boundary, downstream stack G, and finite legal team family before outcomes are generated. Complete coverage identifies exact finite-benchmark oracle regret conditional on that stack. For any finite collection of frozen policies, executing the union of their distinct selected teams is the minimal assumption-free support for every pairwise policy contrast, though not for absolute oracle regret. Two controlled tables with source-ID-disjoint splits test the instrument. On MuSiQue-12, a pre-specified privileged positive control improves regret from 0.532 to 0.402; a later public-interface control reaches 0.424 versus 0.554 but is retrospective. On HotpotQA-4, a pre-specified public direct scorer improves regret from 0.313 to 0.110. In fixed-stack Llama execution, verified route regret improves by 0.190, while the raw-answer gain is 0.010 with an interval crossing zero. A five-family ToolSandbox variant-shift validation exhaustively evaluates 16 declared teams on 14 untouched task variants (224/224 valid rows): the declared-family oracle reaches 0.768 safe-evidence completion, while the prospectively frozen router gets 0.637 (regret 0.131), failing the predeclared 0.10 criterion. A later retrospective comparator reaches 0.655, matching all-workers with 4.57 versus 5.00 workers on average. Thus COVER exposes selection headroom without manufacturing a routing win. A crossed-stack diagnostic shows absolute scores depend on G but finds no detectable router-by-finalizer interaction. COVER is an auditable measurement methodology, not a claim of stack-invariant or universal agent-routing superiority.

---


### 156. [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](https://arxiv.org/abs/2608.28476)

**<font color=#1a73e8>作者：</font>** Zhuoshi Pan, Qizhi Pei, Junru Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks require large language models (LLMs) to iteratively retrieve, integrate, and maintain dispersed information across multi-turn interactions, but preserving all interaction histories leads to a continuously growing working context. Recent proactive context management methods allow models to edit their own working context with specialized tools, yet they still face three key limitations: (1) a limited toolset restricted to search, deletion, and summarization, with no support for global planning, long-term memory, and adaptive compression; (2) inefficient exploration that treats context management actions uniformly despite their heterogeneous impacts on final outcomes; and (3) coarse-grained credit assignment that assigns the final trajectory-level reward to all intermediate context editing actions during RL. To bridge these gaps, we introduce ContextPilot, a proactive context management framework for long-horizon agentic reasoning. Our approach systematically augments the toolset with planning, long-term memory, and soft context offloading tools. We further propose an RL method tailored for context management, which uses context and entropy variation to identify critical editing decisions for branch sampling and estimates action-level advantages from all branched trajectories that pass through the corresponding context editing action. Experiments on long-context QA and deep search tasks show that ContextPilot achieves stronger performance with a more compact working context, consistently outperforming existing baselines across various base models and benchmarks. Code is available at this https URL.

---


### 157. [Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge](https://arxiv.org/abs/2608.28478)

**<font color=#1a73e8>作者：</font>** Zhuoshi Pan, Junru Lu, Yan Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual question answering (QA) typically assumes a single canonical answer, obscuring whether large language models (LLMs) retain divergent accounts of long-tail facts. To address this gap, we introduce ElephantBench, a closed-book knowledge probe comprising 1,094 questions generated through an auditable graph-based pipeline. The pipeline retrieves related documents from a low-exposure web corpus, identifies naturally occurring disagreements, and converts them into multi-account QA records. Each answer is verified against the originating documents and authoritative public web sources and is then reviewed by human annotators. Across 32 models, even the strongest model recovers both accounts on only 52.4% of questions, while on nearly all remaining questions it recalls one account but omits the other. Scaling model size and inference-time reasoning improve recall but do not eliminate this incompleteness. Corpus analysis further shows that exposure imbalance favors the dominant account, whereas greater minority-side exposure is associated with more complete recall. These findings establish ElephantBench as a reproducible knowledge probe for diagnosing epistemic myopia in parametric memory. More broadly, our graph-based benchmark construction pipeline provides an efficient and scalable way to turn long-tail corpora into source-traceable knowledge probes, supporting efforts to evaluate and advance the epistemic rigour of next-generation LLMs. Code is available at this https URL.

---


### 158. [NL2AGBench: Benchmarking LLM Auto-Formalization for AlphaGeometry](https://arxiv.org/abs/2608.28481)

**<font color=#1a73e8>作者：</font>** Samuel Xiao, Judy Song, Rory Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have demonstrated strong capabilities in natural language understanding and mathematical reasoning. However, their ability to translate informal mathematical problems into formal representations remains underexplored. This limitation is particularly important for neuro-symbolic geometry systems such as AlphaGeometry, whose theorem-proving engine requires inputs in a specialized domain-specific language (DSL). Although AlphaGeometry achieves near-IMO gold-medalist performance, manually converting natural-language problems into its formal syntax remains a significant usability bottleneck. To address this challenge, we introduce the Natural Language to AlphaGeometry Benchmark (NL2AGBench), which evaluates LLMs in translating English geometry problems into AlphaGeometry-compatible formal representations. NL2AGBench uses execution-based verification within AlphaGeometry to assess translation quality rather than relying solely on textual similarity. We evaluate ten state-of-the-art open- and closed-source LLMs across multiple parameter scales and analyze executable translation accuracy, syntactic correctness, and error characteristics. Our experiments reveal a substantial performance gap between closed- and open-source models: leading closed-source models achieve executable translation rates above 80%, while even the largest open-source models struggle to consistently preserve geometric constraints and produce valid formalizations. We introduce an error taxonomy distinguishing syntax and logic errors and investigate mitigation strategies, including few-shot prompting, fine-tuning, and human-guided hinting, which yield measurable improvements across multiple model families.

---


### 159. [How Proper Scoring Rules Shape LLM Forecasting](https://arxiv.org/abs/2608.28482)

**<font color=#1a73e8>作者：</font>** Benjamin Turtel, Paul Wilczewski, Kris Skotheim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper evaluates how reward function choice shapes the performance and behavior of LLM forecasters. We compare five proper scoring rules as training objectives for binary forecasts of resolved real-world events. Although the rules share the same theoretical incentive for truthful probability reporting, the resulting models differ in calibration, probability use, and estimated profiles of bias, information, and noise, with smaller differences in aggregate accuracy and discrimination. The Brier-trained model has the lowest observed Brier score and highest AUC-ROC, while the log-trained model has the highest observed log score and lowest calibration error. Models with similar aggregate performance also reach that performance through different combinations of bias, information, and noise. Proper scoring rules therefore need not behave interchangeably as training objectives. Reward choice may shape not only how well an LLM forecasts, but how its forecasting errors are structured. Each condition uses a single seed, so some differences may reflect training stochasticity.

---


### 160. [LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment](https://arxiv.org/abs/2608.28490)

**<font color=#1a73e8>作者：</font>** Jingjing Nie, Jiawei Guo, Krishna Meda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software and systems security workflows are typically procedural: analysts inspect heterogeneous artifacts, form hypotheses, invoke tools, interpret outputs, and revise plans. Large language model (LLM)-based agents, which can plan, use tools, retain state, and revise actions across multi-step workflows, are being rapidly adopted to automate this work. Given the consequences of delegating security decisions to autonomous systems, understanding how such agents are built, used, and assessed is crucial. Yet to this date, there remains a lack of systematic understanding of what has been done and how far we are in this field: the term "agent" is applied inconsistently, applications differ sharply in risk, and assessment protocols are often incomparable. To gain a comprehensive and coherent view of this area hence inform relevant future research, this paper provides a systematic literature review of the (1) technical approaches, including agent architecture, perception, memory, reasoning and planning, action space, orchestration, and self-improvement, (2) applications, with respect to the security tasks served, and (3) assessment, including the datasets, outcome and trajectory metrics, safety measures, and baselines considered, over the peer-reviewed literature spanning the emergence of this area (2023--2026). Our synthesis reveals a field that has built agents able to act but not yet agents whose authority is bounded or whose behavior is auditable. In addition to knowledge systematization, we also extend our insights into the limitations of and challenges faced by current approach, application, and assessment designs, which shed light on potentially promising future research directions.

---


### 161. [Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve LLM Machine Translation](https://arxiv.org/abs/2608.28496)

**<font color=#1a73e8>作者：</font>** Di Wu, Sergey Troshin, Christof Monz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Two forms of test-time scaling for Large Language Models (LLMs) have emerged as effective and widely adopted paradigms: sequential, in which later answer attempts depend on earlier ones, and parallel, such as i.i.d. sampling with reranking. In this study, we investigate their properties in translation. First, our study shows that sequential sampling has a higher performance ceiling, providing a more diverse and effective pool of samples, particularly under smaller sampling budgets. Second, we interrogate the nature of test-time scaling through a multidimensional manual analysis. Human analysis of the Best-of-$N$ translations demonstrates that sequential sampling substantially improves translation fluency and naturalness, but can degrade accuracy when inference budgets are large. Finally, we suggest an explanation of the mechanism through which sequential scaling improves machine translation. Our controlled analysis partially attributes the success of sequential self-improvement to the model's access to a larger target-side context. Ablation experiments on sequential sampling demonstrate its robustness across different sampling temperatures, while also revealing sensitivity to context construction, suggesting directions for future improvement.

---


### 162. [Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration and External Control](https://arxiv.org/abs/2608.28502)

**<font color=#1a73e8>作者：</font>** Jun Wen Leong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents arbitrate among instructions from system prompts, users, memory, and tools, but this arbitration cannot be assumed to enforce trust boundaries. We identify a recognition-enforcement gap: source-format features (role-template position, channel metadata, formatting cues) are linearly decodable from model activations, and models can explicitly identify forged authority when prompted, yet some configurations still produce the conflicting tool call. We use "recognition" in this specific decodable-source-format-plus-verbalized-detection sense; crossed-probe controls show it is not a unified abstract trust representation. The gap is not an immutable property of model weights. Restrictive policies and diverse prompts can eliminate execution on the same models, while permissive configurations and particular prompt-model pairs yield deterministic failures. Across a fleet evaluation (authority spoofing: 46 model endpoints across 6 vendors including open-weight; memory conflict: 48 models), average execution under diverse novel attacks is 1.21% [0.5-2.1%] (model-clustered CI over 14,294 spoofed trials from 29 models), but vulnerability is concentrated in reproducible cells and shifts across deployment windows (up to 47pp within-window per-fingerprint range). Prompt-layer defenses likewise fail to generalize across models and adaptive formulations. We therefore treat model self-arbitration as a capability rather than a security boundary and implement an external reference monitor combining authenticated source routing with capability-gated tool execution. It deterministically rejects all tested forged, tampered, replayed, and unsigned requests while preserving legitimate operations. A separate adaptive red-team found one implementation flaw (a since-patched clock-skew admission), not a cryptographic bypass. Secure agents require external enforcement, not merely better recognition.

---


### 163. [Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration](https://arxiv.org/abs/2608.28511)

**<font color=#1a73e8>作者：</font>** Simeng Sun, Roger Waleffe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When training Mixture-of-Experts (MoE) language models with expert parallelism, all-to-all token dispatch and combine collectives can consume a substantial fraction of end-to-end training time. In this work, we study communication-efficient MoE models (CE-MoE), in which we adopt a heterogeneous layer pattern that decouples token-mixing and channel-mixing depth. Compared to conventional models which interleave MoE layers after each token-mixing layer (e.g., attention, Mamba-2), CE-MoE models concentrate expert capacity in a select few routed MoE layers, while maintaining depth by adding additional token-mixing and dense-FFN layers. Across a scaling ladder from 2B to 31.5B total parameters, under matched total and activated parameters, CE-MoE models consistently reduce training cost while matching validation loss and downstream benchmarks with full-MoE baselines. At the 31.5B scale, CE-MoE uses 33.3\% fewer GPU-hours while improving average downstream score and inference throughput.

---


### 164. [InstructMesh: Selective Refinement of Generative 3D Models for Fabrication](https://arxiv.org/abs/2608.28534)

**<font color=#1a73e8>作者：</font>** Faraz Faruqi, Ahmed Katary, Demircan Tas 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.

---


### 165. [An Enclosed Mode Is a Gauge Choice: Topology Relative to Reach in Certified Code World Models](https://arxiv.org/abs/2608.28541)

**<font color=#1a73e8>作者：</font>** Javier Aguilar Martín  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A code world model accepted by a sampling gate can be exactly right on everything the gate can see and arbitrarily wrong beyond it. We characterize what a certified model can know, and what its errors can cost, when the omission is an annular freeze mode enclosing an unreachable interior. The gate quotient makes the question precise: acceptance-with-certainty determines the model exactly on the reachable query set; beyond reach is gauge. On a minimal ring instrument we prove the extreme case (a wrong-topology filled-disc artifact unfalsifiable by any sampling gate and bitwise harmless at play) and measure, with LLM synthesis across three model families, how one knob (a channel of width gamma) walks the same artifact through three regimes: unfalsifiable-and-harmless, falsifiable-and-costly, and instantly falsified. Three principles organize the empirics. First, danger is topology relative to reach: a channel the planner can use collapses the blind model's exploitation (play cost 1.09 to ~0 over a knee at gamma ~ 0.1), while a hidden channel with the same first Betti number keeps it at full strength (1.12). Second, repair is parameter-bound and sensor-bound: no family recovers the region from outside evidence; from inside, models pose the right topology but cannot pin its parameters, and the posed topology tracks the guiding persistent-homology summary's wrong beta_1 (a sensor with a measured geometric resolution limit), not the truth. Third, mitigation must match the error's dimension and direction: point fences fail against the one-dimensional boundary, a dimension-matched persisted fence collapses exploitation to a two-lesson transient (0.999 to 0.058), and the dual freedom certificate collapses the invented-mode failure symmetrically (1.769 to 0.029). In n dimensions the shell makes misidentification near-certain while the danger stays fully exploitable: the two axes are independent.

---


### 166. [DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging](https://arxiv.org/abs/2608.28547)

**<font color=#1a73e8>作者：</font>** Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\%$ of total parameters).

---


### 167. [A Formal Limitation on Learning Human Language From Textual Corpora](https://arxiv.org/abs/2608.28560)

**<font color=#1a73e8>作者：</font>** Emily Cheng, Ryan Cotterell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a listener recover what a speaker means from the form of an utterance alone? We answer this question information-theoretically, and for a listener given by any featurizer of text, including the hidden states of contemporary large language models. Modeling language use as a joint distribution over meanings, contexts, and utterances, we derive upper bounds on the probability that a decoder recovers a speaker's intended meaning from a representation of the utterance. The bounds are governed by the uncertainty that form leaves about meaning, which splits into an irreducible part and a part that only (extralinguistic) context, but never the utterance alone, can resolve. Because these quantities are intrinsic to language, no representation, however much text or supervision produced it, can surpass them; the bounds hold whether the space of meanings is discrete or continuous. Experiments on artificial languages, Mandarin zero-pronoun resolution, and color reference provide empirical evidence in support of the theory.

---


### 168. [GeBDA: Building Damage Assessment as Text-Based Sequence Prediction](https://arxiv.org/abs/2608.28567)

**<font color=#1a73e8>作者：</font>** Olivier Dietrich, Krishna Sapkota, Konrad Schindler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventionally, Building Damage Assessment (BDA) is tackled either with dedicated network architectures or by fine-tuning geospatial image foundation models. In this work, we ask whether a general-purpose Vision-Language Model (VLM) can localize buildings and grade their damage through autoregressive sequence generation alone. We cast BDA as predicting a variable-length set of bounding boxes, each specified by its coordinates and a damage label. Our preliminary implementation, based on the open Gemma model, achieves promising damage mapping results from only bi-temporal satellite images and a suitable text prompt.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 169. [WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcement Learning](https://arxiv.org/abs/2608.27508)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Han, Tianwen Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents trained with reinforcement learning (RL) have showcased strong environment learning capabilities on mobile platforms. However, RL typically demands extensive real-environment interactions, leading to high resource costs and instability, especially in GUI scenarios. To address these, we propose WM-R1, the first reinforcement learning framework that trains mobile GUI agents with world models instead of real environments. Specifically, world models serve as the source of state transitions during all rollouts, replacing the real Android environment within the training loop. WM-R1 also embeds world models directly into the thinking process, enabling agents to reason about the consequences of candidate actions before committing to the final action. Crucially, WM-R1 eliminates the need for real-environment interaction, supports massively parallelized and step-level granularized trajectory generation grounded in world models, and introduces a multi-dimensional rule-based reward that jointly optimizes task success, trajectory efficiency, and world model utilization. For efficient training, we curate a high-quality dataset of 2000 challenging tasks. Experiments on Android mobile benchmarks demonstrate that WM-R1-trained agents significantly outperform GRPO-only baselines and inference-time simulation methods. Code is available at this https URL .

---


### 170. [Leveraging a Foundation Model for the EEG-Based Diagnosis of Alzheimer's Disease](https://arxiv.org/abs/2608.27719)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maggie Lin, Chung-Lin Hou, Tzyy-Ping Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological heterogeneity in Alzheimer's Disease (AD) poses a critical diagnostic challenge, particularly for traditional linear methods that fail to capture non-linear neural dynamics. To address this, we propose a diagnostic framework utilizing the Large Brain Model (LaBraM), pretrained on over 2,500 hours of EEG data. By integrating these high-dimensional latent embeddings with a non-linear Random Forest classifier, our approach effectively isolates robust disease markers. Under a rigorous subject-independent 5-fold cross-validation protocol, the method achieves an ROC-AUC of 89.36% +/- 3.49%, PR AUC of 81.45% +/- 4.43%, and Balanced Accuracy of 82.44% +/- 4.34% in distinguishing dementia patients from healthy controls. Notably, this performance uses only 8-second EEG segments, surpassing traditional spectral baselines, including band-power and parameterized oscillatory features (FOOOF). Post-hoc occlusion analysis confirms the model captures clinically validated biomarkers, specifically occipital-frontal Alpha and Theta rhythm degradation. Additional neurophysiological alignment analysis demonstrated that higher LaBraM-predicted dementia probability significantly correlated with worse cognitive performance, greater clinical severity, increased theta and alpha relative power, and higher aperiodic exponent. These findings demonstrate that deep latent representations extract clinically relevant signatures from noisy signals, enabling precise, rapid, and data-efficient diagnosis.

---


### 171. [Learning from Hard Prompts: Difficulty-aware Advantage Amplification in Dynamic Sampling](https://arxiv.org/abs/2608.27982)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Siyuan Gan, Yuhan Li, Xiran Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) is a prominent variant of Group Relative Policy Optimization (GRPO). DAPO introduces several improvements over GRPO. Among these, Dynamic Sampling contributes the most to DAPO's accuracy gains relative to GRPO. To improve accuracy, Dynamic Sampling enhances training stability by eliminating zero policy gradients from zero advantages. Specifically, it avoids such zero gradients by filtering out prompts where sampled responses are either entirely correct or incorrect. However, our theoretical analysis shows that Dynamic Sampling decrease training efficiency as it cannot effectively utilize hard-to-sample correct responses on hard prompts. Formally, it asymmetrically amplifies the advantages of distinct responses to the same prompts. On hard prompts, incorrect responses undergo greater amplification than correct ones. This leads the model to avoid generating the observed incorrect responses rather than capitalizing on the hard-to-sample correct ones on hard prompts, resulting in low training efficiency. To improve training efficiency, we propose Direct Advantage Amplification (DAA), which amplifies the advantages of hard-to-sample correct responses on hard prompts, as obtained by Dynamic Sampling. This ensures that, when Dynamic Sampling is used, these hard-to-sample responses can be effectively capitalized on, implying higher training efficiency. By integrating DAA into DAPO, we obtain Difficulty-aware Advantage Amplification Policy Optimization (DA3PO), which is implemented with fewer than 30 lines of code from DAPO. Experiments show that DA3PO significantly outperforms GRPO and other classical GRPO variants.

---


### 172. [A Controlled Audit of Architectural Complexity in Uncertainty-Aware Multi-Organ Ultrasound Classification](https://arxiv.org/abs/2608.28063)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Song, Pengbo Sun, Shichang Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-organ ultrasound classifiers increasingly combine attention, mixture-of-experts routing, uncertainty gating, and evidential deep learning (EDL) objectives to address heterogeneous anatomy and acquisition. Yet a plausible design rationale does not by itself establish that an added component improves the trained system. We contribute a controlled complexity-audit framework, applied to the deployment decision between the maximal evidential candidate Full-EDL and simpler alternatives. Six candidates were evaluated on the primary dataset and three in an internal replication, using ten matched seeds, frozen image-level partitions, capacity- and optimisation-aware comparisons, symmetric temperature scaling, paired decision rules, and a separate out-of-distribution (OOD) veto. Retaining Full-EDL did not establish a reliable macro-F1 gain on either dataset, while the simplified alternatives remained inconclusive under the non-inferiority margin. Simple cross-entropy with temperature scaling (Simple-CE+TS) met the calibrated negative log-likelihood criterion on both datasets and showed favourable selective-risk ordering. The raw calibration advantage of evidential training disappeared after temperature scaling and did not recur on the second dataset. The gate had negligible observable influence at the audited checkpoints, and deleting the Full-only chain revealed no stable task or calibrated-loss benefit. Simple-CE nevertheless triggered the OOD veto against the fetal probe but not the lung probe, precluding an unconditional OOD-safety claim. We therefore selected Simple-CE+TS for the evaluated in-distribution objective while retaining Full-EDL as the maximal reference. Components should earn retention through functional and retraining-based evidence, and calibration and distribution-shift reliability should be evaluated separately.

---


### 173. [FinExam-10K: When Retrieval Helps Financial Reasoning?](https://arxiv.org/abs/2608.28155)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yan Lin, Jingyu Sun, Zhongliang Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Professional financial examinations require models to combine domain knowledge, calculation, and judgment, yet no benchmark covers the full CFA and FRM structure under one protocol. We introduce FinExam-10K, to our knowledge the largest reported English benchmark for this setting, with 10,198 expert-reannotated questions spanning CFA Levels I-III and FRM Parts I-II. We release 5,110 questions and sequester 5,088 for a quarterly maintained leaderboard. To separate coverage from local answerability, we report a 10,198-item Full-Coverage Track and a 7,625-item Context-Complete Reasoning Track, which is the primary basis for claims about reasoning from the supplied record. Across 17 models, the best accuracy is 85.29% overall. On the frozen Hard band, the best score is 34.68% on the Full-Coverage Track and 54.57% on the 372 context-complete items. All 17 models share 47 context-complete failures. Function-RAG and FunctionGraph-RAG rescue hundreds of errors but also overturn many correct answers, producing little or negative net gain. A gate trained only on public data decides from the question and initial response when FunctionGraph-RAG should run. On the 5,088 held-out items, the gate invokes FunctionGraph-RAG for 7.9% of questions and improves accuracy from 70.83% to 71.23% (p = .0446).

---


### 174. [EXPOSE: Explainable and Domain-Robust Embeddings from Pathology Vision Foundation Models using Sparse Autoencoders](https://arxiv.org/abs/2608.28191)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anja Witte, Maximilian Lennartz, Jan Baumbach 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) are widely used in computational pathology but remain sensitive to domain shifts arising from variations in staining, tissue preparation, and scanner hardware. A key limitation is that VFM embeddings entangle biological with domain-specific information, hindering cross-domain generalization. We propose Explainable Probing of Cross-Domain Sparse Embeddings (EXPOSE), a framework that uses Sparse Autoencoders (SAEs) as an explainable bottleneck to identify and suppress domain-specific components in VFM embeddings. We train a sparse representation of VFM features, use a linear classifier to identify domain-specific latent dimensions, and mask these features prior to downstream relapse prediction without retraining the backbone model. Experiments on a large prostate cancer dataset with multiple acquisition domains show that SAE features capture both domain- and task-specific information, which are partially disentangled in the latent space. Removing domain-specific features improves cross-domain performance and increases embedding robustness as measured by the Domain Robustness Index (DoRI). Code is available at this https URL .

---


### 175. [Explainable Diabetic Retinopathy Classification Using Vision Foundation Models](https://arxiv.org/abs/2608.28207)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Abhishek Verma, Anila Krishna, Abhishek Gajanan Bankar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy (DR) is a major cause of preventable blindness, creating a need for accurate and trustworthy automated screening. This study investigates an explainable DR classification framework using vision foundation models and multiple transfer learning strategies. Three backbones, DINOv2, CLIP, and Vision Transformer (ViT), were evaluated using full fine-tuning, linear probing, and Low-Rank Adaptation (LoRA). Models were trained and internally evaluated on the ODIR dataset and externally evaluated on APTOS to assess generalization. DINOv2-LoRA achieved the highest internal AUROC of 0.758, while DINOv2 full fine-tuning and ViT full fine-tuning achieved the highest external AUROC of 0.920. Calibration was further assessed using reliability analysis after isotonic regression. For explainability, Grad-CAM and HiResCAM were evaluated against expert-annotated lesion masks from the IDRiD dataset using Dice, Intersection over Union (IoU), and Pointing Game metrics. The results demonstrate that foundation models, particularly DINOv2, can provide strong predictive performance, while LoRA offers a parameter-efficient alternative to full fine-tuning. Quantitative evaluation of explanation maps further supports the assessment of whether model attention corresponds to clinically relevant retinal lesions.

---


### 176. [Efficient Online Continual Foundation Model Fine-Tuning for Predictive Process Monitoring](https://arxiv.org/abs/2608.28237)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sjoerd van Straten, Marwan Hassani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Process Monitoring (PPM) models are increasingly deployed in dynamic environments where concept drift causes the underlying process distribution to shift over time. While recent work has moved toward online continual learning, existing methods train compact, task-specific networks entirely from scratch, leaving a persistent cold-start problem. Foundation Models (FMs) offer a compelling solution to this problem, but their continual fine-tuning in the process mining domain remains unexplored. We propose COMPASS (Continual Online foundation Model-based PPM with Adaptive SubSpaces), the first framework for online continual fine-tuning of FMs for PPM. COMPASS adapts loss-plateau drift detection to autonomously identify task boundaries in event streams and maintains a unified knowledge subspace including both pre-trained and task-specific directions. We evaluate our approach on nine event streams covering synthetic and real-world concept drift scenarios, across task-free and task-aware settings with multiple backbones and with consistent hyperparameter tuning across all methods. Our approach outperforms three SOTA non-FM competitors and two update strategy baselines, with particularly strong gains on streams exhibiting recurrent drift and complex, long-running cases, while incurring acceptable computational overhead compared to the non-FM competitors.

---


> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
