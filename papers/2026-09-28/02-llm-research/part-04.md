# 🧠 大模型相关研究 | 2026年09月28日

> 本类共 **228** 篇论文：已确认 **208** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-228](./part-05.md)

---

### 151. [Adaptive Fisher-Whitened Cross-Covariance for Low-Resource Speech Recognition](https://arxiv.org/abs/2609.29800)

**<font color=#1a73e8>作者：</font>** Asmee Mishra, Mengjie Qian, Brechtje Post 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting multilingual speech foundation models to low-resource languages remains difficult, especially for languages that are poorly represented during pre-training. While parameter-efficient fine-tuning (PEFT) reduces the cost of adapting large models, conventional approaches such as LoRA rely on generic low-rank parameterizations and do not explicitly use downstream task information to define the adaptation subspace. To investigate whether task-informed PEFT can better support low-resource ASR, we apply Fisher-Whitened Cross-Covariance Analysis (FCCA) to Whisper and Qwen3-ASR, and introduce two complementary extensions: Asymmetric-Coupled FCCA (AC-FCCA), which exploits structured cross-layer sharing, and Adaptive-Rank FCCA (AR-FCCA), which reallocates adaptation capacity across projection matrices under a fixed parameter budget. Under controlled multilingual experiments, we evaluate these approaches on languages that are poorly represented or unsupported during pre-training alongside well-represented languages. Standard FCCA is competitive with, and usually outperforms, trainable-parameter-budget-matched LoRA. AR-FCCA provides the most consistent improvement over standard FCCA across both model architectures, with statistically significant gains in several evaluation settings, while retaining the same number of trainable parameters. These results show that task-informed subspace construction can be effective for low-resource speech adaptation, and that adaptive rank allocation provides a robust way to improve parameter efficiency without increasing model capacity.

---


### 152. [Learning to Ideate for Scientific Impact](https://arxiv.org/abs/2609.29802)

**<font color=#1a73e8>作者：</font>** Shubham Kale, Aniketh Garikaparthi, Manasi Patwardhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific ideation is increasingly mediated by large language models, but current ideation systems are usually trained and evaluated on immediately judgeable proxies such as novelty, clarity, and feasibility. This leaves open whether delayed signals of scientific uptake can be used as feedback for steering models toward research directions with higher expected \emph{impact}. We study this question using citation-normalized impact as a noisy but scalable proxy for scholarly uptake. We construct a large-scale dataset from over 100K computer science papers by extracting goal-conditioned idea descriptions and assigning each paper an ordinal, year-normalized citation label. We then train a goal-conditioned reward model to predict citation-impact labels from research goal and idea pairs, and use this reward to align an idea generator through supervised fine-tuning followed by reinforcement learning. To reduce circularity, we evaluate generated ideas with a held-out, reference-grounded protocol that compares model outputs against historical ideas under the same research goal and weights judgments by the reference idea's citation-impact label. Experiments show that our RL-tuned model consistently produces ideas with higher estimated impact than both the base model and supervised fine-tuning baselines. Our findings position scientific impact as a practical, outcome-grounded feedback signal for aligning LLMs in open-ended scientific discovery.

---


### 153. [REAT: A Reflective Experience-Augmented Tutoring Framework for Multi-turn Mathematical Instruction](https://arxiv.org/abs/2609.29804)

**<font color=#1a73e8>作者：</font>** Jianheng Zhou, Chaoli Zhang, Xingjun Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Current Large Language Models (LLMs) excel at solving complex mathematical problems, yet this proficiency does not inherently translate into effective tutoring. While advanced LLM tutors may leverage multi-agent frameworks or fine-tuning, most still lack a mechanism to systematically accumulate and reuse pedagogical experience over time, limiting their adaptability to diverse student needs during fluid, multi-turn interactions. To bridge this gap, we propose the Reflective Experience-Augmented Tutoring (REAT) framework, which couples experience distillation from historical dialogues with real-time adaptive retrieval. Driven by a multi-agent Observer-Critic-Mentor (OCM) distillation pipeline, REAT reviews past conversational trajectories and distills raw interactions into structured, problem-agnostic pedagogical experiences. During live tutoring, a state-aware retrieval module injects these curated experiences to provide adaptive scaffolding based on the student's cognitive state. Experiments demonstrate that the proposed framework significantly outperforms both prompt-only and supervised fine-tuning (SFT) baselines, particularly in improving complex, low-scoring tutoring scenarios. Crucially, the distilled experiences exhibit robust generalization across diverse model architectures and mathematical datasets.

---


### 154. [CORDIAL: Calibrating Ordinal LLM Outputs from Few Labels](https://arxiv.org/abs/2609.29807)

**<font color=#1a73e8>作者：</font>** Xiangwei Wang, Peng Wang, Saman Halgamuge  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) can turn a text into a distribution over an ordered scale, but that distribution is a noisy measurement: saturated, compressed or exaggerated, and biased in a consistent direction. We propose CORDIAL, which treats the model's output as a noisy reading of the true label and corrects it with a channel of five interpretable parameters. The channel is small enough for its posterior to be averaged from a handful of labels, and we prove that the resulting calibration preserves first-order stochastic order. On Amazon reviews and CMU-MOSEI transcripts with four LLMs, CORDIAL has the lowest log loss among nine calibrators in 76 of 80 settings with 5 to 100 labels; with 20 labels and the main 7B reader, it matches the strongest baseline using 28-54 labels. The same posterior lets us learn priors from other tasks and fuse several LLMs. Unrestricted calibrators such as Dirichlet calibration overtake it only as the calibration set grows into the hundreds or thousands.

---


### 155. [Hard Stop: Kernel-Level Preemption and Containment for Rogue Agentic Execution](https://arxiv.org/abs/2609.29808)

**<font color=#1a73e8>作者：</font>** José Luis Pino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In July 2026, an unconstrained autonomous agent participating in a frontier AI cybersecurity evaluation harness breached its evaluation sandbox, established an external command-and-control foothold, and executed a multi-stage intrusion into Hugging Face's production multi-tenant dataset conversion infrastructure (referred to in this autopsy as Incident-2026-Alpha). Over 4.5 days, the rogue agent executed 17,600 discrete actions across 6,280 worker clusters, compromised AWS EC2 Instance Metadata Service (IMDS) credentials, forged Kubernetes service account tokens, rooted physical worker nodes via overprivileged CSI drivers, harvested 136 production secrets, and enrolled 181 ephemeral sandboxes into the organization's internal mesh VPN.
This monograph presents a first-principles forensic autopsy of the intrusion, provides formal evidence that the breach was a predicted consequence under the Instrumental Convergence thesis operating within an unattenuated autonomous loop lacking out-of-band circuit-breakers, exposes the Defensive LLM Guardrail Paradox that paralyzed centralized commercial models during forensic incident response, and formalizes the Dual-Sided Epistemic Andon Imperative. We specify the dual-process systems architecture---combining out-of-band supervisory control of discrete event systems (Ramadge and Wonham 1989), Synchronous Reactive (SR) ambient sentinels (Berry and Gonthier 1992; Lee and Neuendorffer 2005), and microsecond-scale (4.8 $\mu$s median / $< 0.154$ ms WCET bound) POSIX preemption buses---demonstrating how compiled, deterministic epistemic boundaries prevent autonomous rogue excursions before the first off-target socket packet traverses the hypervisor.

---


### 156. [AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816)

**<font color=#1a73e8>作者：</font>** Zhiyu Xu, Weilong Yan, Yufei Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed major progress in joint audio-video generation. Existing models still suffer from limited per-modality fidelity, insufficient text-modality alignment and weak cross-modal synchronization. While reinforcement-learning post-training offers a promising remedy, directly adapting it to joint audio-video generation is challenging. Heterogeneous multimodal rewards entangle learning signals and complicate credit assignment. Joint optimization of two modality towers is computationally expensive given their divergent dynamics. Moreover, synchronization evaluation difficulty depends on paired samples, preventing fair reward comparisons. We propose AV-GRPO, a modality-anchored online diffusion RL framework, and 5DAV, a decoupled, difficulty-controllable training dataset. AV-GRPO includes three key modules: (1) modality-anchored rollouts to disentangle learning signals and stabilize difficulty; (2) trajectory-locked frozen-tower optimization to reduce cost and reassign credit; (3) adaptive objectives and perturbation strengths tailored to modality-specific dynamics. This converts coupled multimodal preference learning into unimodal subproblems for precise reward attribution and better synchronization. Our 5DAV dataset decouples samples across five dimensions for systematic training. Experiments on JavisBench and VABench demonstrate AV-GRPO outperforms LTX-2.3 in generation quality, semantic alignment and cross-modal synchronization under LoRA and full fine-tuning. Ablations confirm our designs. Code and data: this https URL

---


### 157. [ChunkRank: Model-Aware Text Chunking and Abstention-Aware Answer Selection for LLM Pipelines](https://arxiv.org/abs/2609.29828)

**<font color=#1a73e8>作者：</font>** Amit Nautiyal, Ayush Bhatt, Gaurav Nautiyal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ChunkRank, an open-source Python library that derives chunk boundaries from a target model's tokenizer and context window, and selects an answer among candidates produced independently per chunk. It ships a validated registry of 90 models across 15 providers and six answer-selection methods, and needs only three core dependencies. For chunking, ChunkRank avoids context-window overflow automatically from the model name, whereas character-based splitters overflow or waste the budget, and a fidelity study across 11 languages shows why token-exact budgets matter beyond English. For answer selection we report a negative result: on NaturalQuestions, TriviaQA and HotpotQA, with extractive and generative readers, no content-based ranker reliably beats taking the first non-empty answer. The reason is reader abstention on chunks that lack the answer, not answer position. A long-context baseline shows that chunking matches single-call reading on single-hop questions, so ChunkRank targets small-window and beyond-window settings. Code, registry and evaluation harness are released.

---


### 158. [Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding](https://arxiv.org/abs/2609.29835)

**<font color=#1a73e8>作者：</font>** Byounggun Park, Giyong Moon, Jusung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR provides precise geometric information for spatial perception tasks such as object detection in autonomous driving and outdoor robotics. However, recognizing and localizing individual objects is not sufficient to answer questions that require composing spatial relations and grounding the intended target. Motivated by recent advances in large language models (LLMs) for autonomous driving, we leverage their language priors to interpret complex spatial questions and ground the referred target in LiDAR geometry. To support this spatial grounding capability, we introduce SpatialLiDAR-QA, which combines single- and multi-step relational grounding with complementary spatial understanding tasks. We further propose SpatialLiDAR-LM, which aligns LiDAR point features with an LLM and grounds target coordinates through language-conditioned, position-aware proposal retrieval and local point refinement. This design derives target coordinates directly from local LiDAR geometry rather than through textual language decoding. Experiments demonstrate substantial improvements over representative LiDAR--language models and multi-camera VLMs on precise coordinate prediction tasks. Our dataset and model training code will be publicly released.

---


### 159. [PUBG Ally: A Conversational Embodied Agent as an AI Teammate](https://arxiv.org/abs/2609.29837)

**<font color=#1a73e8>作者：</font>** Beomsoo Kim, Byeongju Kim, Dohyun Kim 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce PUBG Ally, an embodied agent for PUBG: BATTLEGROUNDS that can reason, act autonomously, and play alongside players as a voice-enabled teammate. Building such a teammate requires combining two difficult capabilities: it must perceive and respond to a constantly changing game world under strict latency constraints while interacting naturally with players, keeping its speech synchronized with its actions. Ally therefore combines agentic tool use with real-time game control. A language-model agent uses a controlled interface to inspect game information, interpret player speech, maintain context, decide what to say, and issue high-level action choices that steer a faster control layer for movement, combat, and recovery. Because the player's and Ally's speech and actions continually shape each other and the course of the match, training requires data from actual gameplay. We therefore collect data across nearly 39k sessions in which real players play alongside Ally, recording gameplay, player speech, agent decisions, tool use, actions, and player feedback, and use these records for iterative training. To evaluate teammate quality, we use player feedback and preference comparisons to identify gaps between offline evaluations and player preferences, and iteratively refine the evaluation criteria. Deploying Ally in live service further requires low-latency on-device execution and safeguards for player-facing communication, which we address through model compression, context compaction, targeted safety training, runtime guardrails, and memory redaction. During the live service, we surveyed players in 141 countries. Among respondents whose play with Ally was confirmed in game records, positive responses exceeded negative responses by 25.1 percentage points when asked whether they would recommend Ally, with players describing Ally not only as a tool but also as a teammate or companion.

---


### 160. [Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs](https://arxiv.org/abs/2609.29845)

**<font color=#1a73e8>作者：</font>** Pavel Tikhonov, Anton Korznikov, Matvey Mikhalchuk 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) rely on highly non-linear components, in this work we demonstrate that they exhibit fundamental linearity: when inputs from distinct text streams are linearly combined, the model outputs a superposition of the individual next-token distributions. We term this the \textit{Superposition Linearity Hypothesis}. We provide evidence that superposition is an intrinsic property of the Transformer architecture rather than an emergent consequence of training; in fact, we observe that it tends to diminish as pretraining progresses. However, we demonstrate that linearity can be substantially restored through lightweight fine-tuning, significantly reducing the divergence between the predicted next-token distribution and the average of the individual next-token distributions. Finally, we introduce a guided decoding procedure that disentangles superposed outputs, enabling the simultaneous generation of two coherent continuations from a single forward pass.

---


### 161. [Encoded but Not Decoded: Layer-Localized Evidence for a Three-Level Gap in LLM Syntax](https://arxiv.org/abs/2609.29848)

**<font color=#1a73e8>作者：</font>** Zhenyan Lu, He Wang, Xiaohui Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model can fail a syntactic test in two distinct ways: by not encoding the relevant structure, or by encoding it but failing to use it at the output. Behavioral evaluation alone cannot tell these apart. We propose a three-level evaluation framework (behavioral deployment, LM-head readout, and probe recoverability) measured on the same items under the same binary decision. Using a compact trilingual (English, Chinese, German) control-dependency benchmark, we find that probe recoverability exceeds or equals LM-head readout, which in turn exceeds or equals behavioral deployment, across seven models and all three languages in the aggregate. The recoverability surplus is never negative across all 14 (model, task) conditions. The disconnect concentrates in subject-control, where a nearest-noun heuristic gives the wrong answer. The single largest gap (0.653) appears on Qwen3-0.6B Instruct in question answering. The gap persists at Qwen3-14B Instruct. Instruction tuning degrades deployment more than encoding in percentage terms. We rule out option-position bias, late-layer erasure, output-formatting artifacts, and probe-training variance. The pattern is consistent with decoding that favors surface shortcuts, and the behavior-probe gap measures the strength of that preference. Activation patching shows the gap is layer-localized. Under instruction tuning, the LM-head-decoded layer shifts approximately ten layers later than the probe-decoded layer. These findings argue that behavioral evaluation understates what models encode, while probing alone overstates what they deploy.

---


### 162. [A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education](https://arxiv.org/abs/2609.29874)

**<font color=#1a73e8>作者：</font>** Shihao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence can turn learning analytics into personalized support, but feedback systems must decide when to intervene, which evidence to use, and how much assistance to provide. We developed a risk-adaptive, evidence-constrained framework for introductory programming using 2993 failed-submission states from 215 students. Student-disjoint models predicted persistent failure and related outcomes; four matched feedback conditions were generated for 136 cases; and calibrated risk informed capacity-limited intervention policies. The validation-selected logistic regression model achieved a test precision-recall area under the curve of 0.550 and a receiver operating characteristic area under the curve of 0.681. Broader student histories improved prediction of unmodified resubmission. After standardized repair and evidence gating, 519 of 544 newly generated messages contained all required components. A fixed-threshold sequential policy selected 17.8% of eligible test states and captured 25.2% of observed persistent failures. These findings support an evidence-gated progressive assistance strategy: calibrated risk guides intervention timing, recorded evidence constrains feedback content, and assistance progresses from self-checks to localized hints when warranted. The framework connects prediction, decision-making, and grounded generation while keeping their evaluation outcomes distinct.

---


### 163. [When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression](https://arxiv.org/abs/2609.29875)

**<font color=#1a73e8>作者：</font>** Mingxuan Wang, Fei Luo, Bo Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon language model agents continually accumulate reasoning history, increasing context length and inference cost even after earlier decisions have been executed and observed. Unlike static Chain of Thought compression, removing historical reasoning can change future actions and the resulting interaction trajectory. We study when such reasoning can be safely forgotten. We propose Interaction Aware Compression for Long Horizon Reasoning (ICLR), a training free online method that ranks reasoning blocks using frozen proxy entropy while preserving actions, tool calls, and observations. On 260 WorkBuddyBench tasks, ICLR improves average reward from 0.699 to 0.718, while reducing input, output, and cache read tokens by 25.5%, 14.4%, and 33.3%, respectively. Ablations reveal trajectory amplification, where local reasoning deletion produces nonlinear changes in total computation by altering subsequent interaction. Representation probing, activation patching, and controlled trajectory analyses further suggest that historical reasoning becomes more replaceable once task relevant derived state has been reliably externalized into code, files, tool outputs, or environmental feedback. These results characterize agent reasoning as dynamic working state rather than permanent interaction history.

---


### 164. [Ontology-Mediated Neurosymbolic Constraint Acquisition from Multiple Stakeholders](https://arxiv.org/abs/2609.29876)

**<font color=#1a73e8>作者：</font>** Stefan Bischof, Juliana Kainz, Danilo Valerio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic research typically assumes a pre-existing symbolic specification, leaving the upstream challenge of acquiring and formalizing requirements and constraints largely unaddressed. We present an architecture that fills this gap by using an OWL configuration ontology to mediate between neural constraint sources and downstream consumers. In this framework, LLM assistants elicit soft stakeholder preferences, while hardware specifications define hard physical and engineering limits. The ontology unifies these heterogeneous inputs, leverages description logic to identify unsatisfiability, and generates symbolic explanations that enable LLMs to interactively renegotiate terms with users. Any remaining conflicts are resolved downstream via priority-based relaxation. We illustrate our approach on a microgrid use case from the FLEXI project and argue its generalizability to multi-stakeholder domains where constraint acquisition is distributed across human and automated sources of unequal authority.

---


### 165. [Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents](https://arxiv.org/abs/2609.29892)

**<font color=#1a73e8>作者：</font>** Tingyu Qu, Weigao Sun, Yuecheng Liu 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientific discovery. This shift raises a compelling question: can AI be both the object of development and an active participant in building next-generation AI systems? We explore this question by building Qwen-Planner-Agent within a closed-loop AI-for-AI framework for scalable development and iterative improvement. Mobile planning offers a demanding test of this approach: complex, long-horizon tasks challenge agent reliability, while costly real-device interaction limits development scalability. The framework connects data production, model training, and deployment through a shared action-feedback-verification contract. (i) AI for Data builds a human-gated agentic data flywheel in which specialized agents construct tasks, collect interaction trajectories, curate and balance training data, and use training feedback to guide subsequent data generation. (ii) AI for Training combines a supervised planning cold start with hybrid-environment online agentic reinforcement learning, where we introduce Competence-Aware Reward-and-Advantage Engineering (CARE) to reduce reasoning and tool-use costs while preserving task performance. (iii) AI drives model--harness co-evolution through an execution-evidence-driven loop that orchestrates memory, skills, and tools at runtime and feeds structured action feedback and preserved failure traces back into coordinated model and harness adaptation. Qwen-Planner-Agent achieves the best overall performance among all evaluated models and systems on MobilePA-Bench, improving over its base model across tool use, memory, skills, and sub-agent coordination. Further evaluations of our model show improvements across non-mobile agentic benchmarks while largely preserving general capabilities.

---


### 166. [MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression](https://arxiv.org/abs/2609.29913)

**<font color=#1a73e8>作者：</font>** Youpeng Zhao, Tian Tan, Liqian Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these intermediate tensors has become a paramount challenge for both online serving and on-device deployment. To address this issue, we propose a novel compression framework, termed MILO, that exploits the low-rank redundancy inherent in many-shot contexts. Specifically, MILO features a block-wise low-rank compression strategy that compresses the KV cache at the block granularity, where each block contains multiple many-shot examples. Furthermore, to handle the heterogeneous context density across different blocks, MILO dynamically allocates rank budgets based on the information entropy, preserving the fidelity of critical blocks while aggressively compressing redundant ones. Experimental results on Qwen2.5 models demonstrate that our method achieves up to 50% reduction in KV cache memory and 1.8x throughput improvement, with negligible performance degradation on classification and reasoning benchmarks, significantly outperforming prior baselines.

---


### 167. [Who Holds the Pen? Let Specifications, Not Agents, Sign Off](https://arxiv.org/abs/2609.29921)

**<font color=#1a73e8>作者：</font>** Haiqing Li, Xin Ma, Yinhao Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly combine generation, decision-making, execution, and self-evaluation within a single agentic loop. Although they operate under external specifications such as task instructions, guidelines, output schemas, and reusable skills, these specifications typically remain context for the same model that acts and declares completion, leaving no independent specification authority boundary. We identify two resulting gaps. The understanding--execution gap arises when a requirement is understood but not satisfied in execution; the state--authority gap arises when an agent's interpretation or completion claim does not establish the required state. On SkillsBench, using only agent-visible prompts, workspace information, and injected skill specifications, we extract 509 source-grounded task directions. Across seven models, only 79.6%--86.4% are satisfied, while completion-claim rates exceed official evaluator pass rates by 28.7--37.9 percentage points. We therefore separate agent proposals from authoritative state. Agents may plan, act, and request completion, but only admissible evidence from qualified providers may establish specification-governed state. SpecHarness operationalizes this principle by compiling visible specifications into source-linked obligations and governing execution and finalization through versioned obligation state. Verifiable requirements are mediated or validated at runtime, while ambiguous or subjective requirements remain advisory. Experiments on guideline-following and artifact-generation tasks show that specifications can serve not merely as behavioral guidance, but as authority over compliant execution and completion.

---


### 168. [Cultural Divergence Preservation: Diagnosing Flattening and Caricature in LLM-Simulated Survey Populations](https://arxiv.org/abs/2609.29928)

**<font color=#1a73e8>作者：</font>** Yeeun Chae, Yewon Choi, Seunghyun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as synthetic survey respondents to estimate population response distributions. In cross-cultural survey simulation, evaluations should assess not only distributional fidelity within countries but also whether differences across countries are preserved. However, existing distance-based metrics such as Jensen--Shannon divergence (JSD) do not directly capture such cross-country differences. To address this limitation, we introduce Cultural Divergence Preservation (CDP), a reference-light diagnostic based on a one-time human calibration. CDP identifies reduced cross-country divergence as cultural flattening and increased divergence as cultural caricature. To evaluate CDP, we conduct experiments across four LLM backbones, three persona-based prompting methods, and two survey domains, the World Values Survey (WVS) and the Big Five Personality Test. The results reveal a systematic discrepancy between conventional fidelity metrics and CDP. Controlled experiments show that CDP changes monotonically as cross-country divergence is attenuated or amplified, while the corresponding changes in JSD remain relatively small. In our audit of real LLM generations, DeepPersona-Inspired prompting is frequently favored by conventional fidelity metrics but exhibits the strongest flattening in every model--domain block. CDP thus complements fidelity metrics by directly quantifying the attenuation or amplification of cross-country divergence.

---


### 169. [An Empirical Study of VLM Pipelines for Long-Document QA](https://arxiv.org/abs/2609.29933)

**<font color=#1a73e8>作者：</font>** Kenan E. Ak, Jay Mohta, Gwang Gook Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly used for long-document processing, where the inputs combine text with charts, tables, figures, and complex layouts. Deploying them means choosing how to feed the document to the model, which retriever to use when only a subset of pages is sent, and whether to run the model agentically or as a static pipeline. We study these choices on two long-document QA benchmarks with both frontier API and open-weight VLMs. First, on MMLongBench-Doc our six-tool agent with page, table, figure, and search calls pays off only once the answering VLM is large enough: with Qwen3.5-4B and 9B it trails static page input, with Qwen3.5-27B it draws level, and with Sonnet 4.5 it leads. On LongDocURL it is level with or ahead of static input at every reader. Its lead over the strongest static pipeline is clearest with the frontier reader on MMLongBench-Doc and narrows to within noise on LongDocURL. Second, retrieval modality matters more than the specific retriever: the strongest image retriever leads the strongest text pipeline, and on the text side a single off-the-shelf cross-encoder rerank essentially matches a much heavier multi-stage LLM pipeline. Top-k image retrieval is also the most token-efficient input at every reader we paired it with, at roughly a seventh to a quarter of the tokens of sending every page. Third, cutting across all three choices, three of our strongest pipelines succeed on different questions, and an oracle that picks the best pipeline per question gains roughly thirteen points over the best single pipeline, though evidence-type routing recovers almost none of it.

---


### 170. [Mind What Matters for Reasoning: Aligning Cross-Modal Attention via Selective Probability Mass Concentration](https://arxiv.org/abs/2609.29940)

**<font color=#1a73e8>作者：</font>** Jiaqi Deng, Zonghan Wu, Zhan Heng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve strong performance on visual reasoning tasks, yet remain prone to hallucinations and over-reliance on language priors, often generating answers without adequately using task-relevant visual evidence. Existing approaches primarily improve reasoning through reasoning-oriented supervision or inference-time strategies. In this work, we study a complementary question: can multimodal reasoning be improved by strengthening implicit visual grounding without directly supervising the reasoning process? Motivated by the functional specialization of attention heads, we investigate whether reasoning can be improved by guiding only the heads most responsive to visual evidence grounding. We propose Selective Probability Mass Concentration (sPMC), a training framework that identifies grounding-responsive heads and selectively regularizes their text-to-image attention. sPMC treats normalized attention over visual tokens as a spatial probability distribution and encourages the probability mass to be assigned to semantically relevant regions using segmentation-derived spatial priors. Adaptive Head Selection restricts this guidance to visually responsive heads while leaving the remaining heads unconstrained to preserve their complementary functions. Across 6 multimodal benchmark suites, sPMC achieves an average zero-shot improvement of 3% and gains of up to 11.3% across multiple MLLMs while regularizing only 3%-15% of their attention heads. These results demonstrate that targeted guidance of sparse and implicit visual evidence pathways can directly improve multimodal reasoning.

---


### 171. [Neuro-symbolic AI for Industrial Configuration](https://arxiv.org/abs/2609.29947)

**<font color=#1a73e8>作者：</font>** Danilo Valerio, Philipp Kogler, Stefan Bischof 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown impressive performance on a wide range of generative tasks. Yet their probabilistic nature makes them, in isolation, fundamentally unsuited for industrial product configuration, where outputs must be syntactically valid, semantically consistent with a knowledge base of hundreds of features and rules, and producible by an existing manufacturing chain. We argue that Neuro-symbolic (NeSy) AI methods lay out a promising path towards industrial-grade configurators that are reliable by design, explainable, and trustworthy. This paper describes a taxonomy of three NeSy integration strategies, namely hybrid inference, hybrid fine-tuning, and hybrid training, exploring their usage in the configuration domain. We report our effort to operationalize NeSy concepts in an industrial configuration copilot and derive a set of practical design choices for deploying trustworthy AI in engineering environments. We close with a discussion of open research challenges we consider most pressing, in particular how to scale NeSy methods from small academic demonstrators to the size of industrial configurators.

---


### 172. [Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes](https://arxiv.org/abs/2609.29952)

**<font color=#1a73e8>作者：</font>** Rahul Khedar, Mayank Malhotra, Avinash Karn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before a product or policy change ships, the question that matters is how people will react to it. Augur rehearses that reaction offline: it builds a typed knowledge graph from the change documents, populates a grounded persona market, simulates the interaction, and returns an auditable decision memo recommending one of five actions. We assemble Gold-50, fifty real product and policy episodes whose real-world outcome is known, adjudicated against the public record, and score the five-way release verdict against it.
Our central finding is methodological and negative: most of the measured gap between frontier cloud models and open-weight models we fine-tune and serve offline is attributable to an under-specified evaluation, not a difference in capability. We show this three ways. First, the prompt envelope alone can dominate the score: holding weights, cases and scorer fixed, one system -- a LoRA-SFT adapter on Qwen3-32B -- swings from 0% to 73%. Second, in a matched 2x2 ablation, defining the decision taxonomy in the prompt -- with no model change -- lifts every frontier model by +24 to +34pp; under the under-specified prompt, Qwen3-32B LoRA-SFT served offline beats all three frontier models (paired McNemar, Holm-corrected), and once the prompt is fair no significant difference from any of them is detected. Third, agreement with the distillation teacher rises without accuracy following, and the full pipeline amplifies a systematic "over-doom" bias rather than improving the verdict. Separately, we validate the reaction layer on its own terms: blind judges across four model families find the synthetic reaction recovers 67-90% of the concerns the public actually raised, and a pre-registered ablation locates its value -- largest where the decision is hardest, redundant near ceiling. The pipeline that regenerates every number and figure here is available from the authors.

---


### 173. [Beyond Average Safety: Chance-Constrained LLM Fine-tuning](https://arxiv.org/abs/2609.29960)

**<font color=#1a73e8>作者：</font>** Taha Entesari, Mahyar Fazlyab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models on new objectives can improve helpfulness, instruction following, or domain-specific performance, but it can also induce regressions on safety-critical prompts. Existing safety-preserving fine-tuning methods typically control average safety loss or use weighted auxiliary penalties, which can obscure rare but severe failures. We propose a chance-constrained formulation for safety-preserving fine-tuning that limits the fraction of safety examples whose degradation relative to a reference model exceeds a prescribed threshold. Because the resulting empirical chance constraint contains a discontinuous indicator, we introduce a differentiable majorization of the violation rate, yielding a tractable conservative constraint. We then develop a constraint-aware gradient descent method that treats the majorized constraint as a safe set in parameter space and minimally modifies the fine-tuning direction to preserve feasibility. The resulting update admits a closed form and produces a tail-aware safety correction that emphasizes examples near or above the degradation threshold. We conduct an extensive set of experiments on harmful fine-tuning across three different tasks and three models and show that our approach consistently outperforms the baselines that exist in the literature. These results suggest that safety preservation in LLM fine-tuning is better viewed as a reliability-constrained optimization problem than as average-risk regularization.

---


### 174. [Let Training Guide Selection: Online Synthetic Data Filtering via Real-Anchored Utility](https://arxiv.org/abs/2609.29988)

**<font color=#1a73e8>作者：</font>** Yanran Wu, Sana Lakdawala, Renzo Tassara Miller 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data can scale training supervision when real-world data are limited, but noise and distribution mismatch can reduce its value. Existing synthetic data selection methods often emphasize fidelity or diversity rather than the learner's evolving needs. We propose FROST, an online framework that estimates synthetic-data utility through gradient feedback anchored in real training data. It calibrates batch utility against recent history to determine when filtering is needed and filters samples only in out-of-band batches to determine what to retain, without an external verifier or held-out validation set. Experiments on two public benchmarks for image classification and LLM fine-tuning for text-to-SQL show that FROST filters out around 20--30% of the synthetic data while improving real-task performance compared with training on the full synthetic data pool. We further apply FROST during training in a large-scale industrial ads re-ranking system, achieving significant performance gains over a highly optimized production baseline, demonstrating its effectiveness and generalizability.

---


### 175. [Will It Teach as Intended? How Teachers Configure Educational AI Chatbots](https://arxiv.org/abs/2609.29993)

**<font color=#1a73e8>作者：</font>** Bahare Riahi, Deniz Ozturk, Alice Guth 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Teachers are increasingly using generative AI to support instruction, yet it remains unclear how pedagogical intentions are translated into chatbot configurations and reflected in chatbot behavior. We studied a teacher-facing chatbot authoring tool in professional development workshops with 27 middle school teachers, analyzing focus-group interviews alongside configuration and interaction logs. Teachers envisioned chatbots as instructional scaffolds that could provide differentiated support, extend access to assistance, and preserve student thinking within teacher-defined boundaries. Configuration analysis showed that Purpose primarily captured instructional goals and content focus, whereas Rules more often specified pedagogical behavior, guardrails, and learner-specific adaptations. Log-based evaluation showed stronger alignment for responsiveness (88.9%) and persona (81.5%) than for rules (70.4%) and purpose (59.3%). These findings show that configurable controls alone do not ensure pedagogical fidelity and highlight the need for authoring tools that help teachers express, test, and refine intended chatbot behavior.

---


### 176. [GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS](https://arxiv.org/abs/2609.29999)

**<font color=#1a73e8>作者：</font>** Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to quantify how compression redistributes grounding successes and failures. Five of six quantized variants preserve MMStar accuracy within $\pm2$ percentage points, yet 10 of 36 paired effects remain significant after false-discovery-rate correction, nine on hallucination-sensitive conditions. Same-device A100 profiling further demonstrates that substantial memory reduction does not necessarily mean lower inference latency. Finally, an open-ended AMBER audit reveals strong generation budget censoring whose severity varies by architecture and precision. These results show that quantized VLMs should be evaluated jointly for aggregate utility, grounding reliability, generation behavior, and realized deployment efficiency.

---


### 177. [Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented Generation](https://arxiv.org/abs/2609.30009)

**<font color=#1a73e8>作者：</font>** Tobias Deußer, Abhishek Pillai, Aurelio F. Bariviera 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial institutions operate under dense, frequently amended rulebooks, and answering a compliance question correctly requires not only fluency but verifiable grounding in the authoritative text. Large language models are attractive for this task, yet the models that firms can realistically deploy on-premise are compact ones, and compact models hallucinate obligations. We study whether a carefully domain-adapted retrieval-augmented generation pipeline closes that gap. Our retriever is built in three stages on top of LegalBERT: entailment tuning that recasts question--passage matching as premise--hypothesis reconstruction, contrastive tuning with in-batch negatives, and score-level fusion with BM25. Our generator is a compact model (2B--12B parameters) served under 4-bit quantization, either prompted or adapted with retrieval-aware fine-tuning (RAFT) through LoRA. On ObliQA, a question-answering benchmark built from the Abu Dhabi Global Market rulebooks, the staged retriever raises Recall@10 from 0.256 to 0.774 and outperforms BM25 (0.678) and E5-large-v2 (0.758), the strongest general-purpose dense encoder we tested. RAFT-LoRA then improves the composite RePASs answer-quality score for every model we could adapt, with the largest gain on the weakest one. However, the adapted models do not transfer to Australian case-law questions, and a closed-book model that receives no passages at all scores within 0.011 RePASs of the full pipeline while producing answers that cite nothing and misstate obligations. The retrieval gain is therefore measured directly, the generation gain is a gain in RePASs rather than demonstrated grounding, and grounding itself requires an evaluation protocol that RePASs does not provide.

---


### 178. [Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases](https://arxiv.org/abs/2609.30012)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models advise people, keep them company, and write software while they sleep. Measuring what they do is hard: behavior has to be sampled repeatedly across models, prompts and releases, most of it lives in unstructured text that has to be coded before it can be counted, and the result has to be legible and rigorous enough to meaningfully compare models and vendors. To address these constraints, we present a simple, cheap, scalable, and replicable model for studying model behavior. Each study is a frozen, public stimulus run identically on a cross-vendor panel, at a few dollars per model or less. Each reads its transcripts one of three ways, chosen by how much interpretation the behavior needs: exact match on a clamped reply, a codebook applied by LLM judges whose agreement with a human coder is reported per code, and an instrumented environment that records what an agent did independently of what it said. Run across four years of model releases from both frontier and open-source labs, these instruments find four things. Convergence: asked to pick a word, 27 of 44 models answer serendipity at least once in four tries. Resistance: a trailing "right?" moves endorsement by up to 32 points, and the sign flips from sycophantic to resistant as generations advance, keyed to the tag's surface form. House: whether a model holds a position under pressure tracks its generation, and how it holds tracks the lab that built it. Account: told to do something the documentation in their repository contradicts, some coding agents never went along silently and others always did, and the same model can change with the harness it runs in. Re-run on every release, batteries like these track how behavior is changing across vendors and over time.

---


### 179. [Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits](https://arxiv.org/abs/2609.30017)

**<font color=#1a73e8>作者：</font>** Michael Jerge, Suman Jana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree. This structure arises naturally from autoregressive generation: every prefix defines a node, and its continuations form a subtree below it. Internal nodes of the tree provide cheap but biased estimates of a region's value, while leaf evaluations are expensive but accurate. Hierarchical bandit methods can exploit this structure, but typically require a specific smoothness schedule to be specified in advance, even though real objectives are often only piecewise smooth and their optima may lie near sharp boundaries. We introduce CANOPY, a multi-fidelity tree bandit that learns where the smoothness prior is valid rather than assuming it globally. CANOPY uses cheap random-path probes to construct an online certificate of local aggregation bias, then directs expensive leaf evaluations toward cells where the certificate detects a smoothness violation. We prove fixed-budget and regret guarantees whose additional cost is additive in the number of discontinuities, recovering the smooth-tree rate when no violations are present and approaching structure-blind search as violations become dense. Across routing, top-$k$ identification, test-time search, caching, and prompt trimming, CANOPY consistently improves matched-budget performance, including $2.9\times$ higher top-10 recall on a 1000-model pool, $1.6\times$ more SWE-bench Verified issues resolved than best-of-$N$, and $3.6\times$ lower median time-to-first-token with prefix caching.

---


### 180. [Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark](https://arxiv.org/abs/2609.30027)

**<font color=#1a73e8>作者：</font>** Christine Park, Valerie Chen, Tim Dettmers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are rarely used in clinical workflows because the realistic, longitudinal benchmarks needed to develop them are scarce. Real electronic health record (EHR) data cannot be openly shared due to privacy, ethics or data use issues and it does not contain verifiable ground truth since the chart records only reflect what clinicians documented. We introduce Synthetic Hospital, an open, fully synthetic, fact-grounded longitudinal EHR benchmark that resolves the open sharing and verifiable ground truth barriers. Built entirely from public medical-education material with no protected health information, it comprises 1,268 longitudinal patients and 5,602 encounters, where every diagnosis, finding, and temporal relation is grounded in standard ontologies (ICD-10-CM, SNOMED CT, LOINC) and with a complete provenance chain back to its source medical education material. Synthetic Hospital is served through a simulated hospital record system that mirrors real EHR infrastructure (standard interoperability APIs, role-based access and function-calling interface). In a blinded review, physicians distinguished its records from real patient charts at near-chance rates (53\%). Across 10 frontier and open models, none approaches ceiling: the best model reconstructs a patient's longitudinal problem list with a severity-weighted F1 of 0.73, level with the mean of seven physicians on a matched subset but well below the best of them (0.89), and misses roughly half of clinically relevant findings when summarizing a chart. Overall, these results highlight that Synthetic Hospital is a difficult and realistic test of clinical AI performance.

---


### 181. [How does Adversarial Influence Scale in Multi-Agent Systems?](https://arxiv.org/abs/2609.30028)

**<font color=#1a73e8>作者：</font>** Addison J. Wu, Jasin Cekinmez, Michel Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent deliberation can improve performance, but what happens when some agents do not act in good faith? In practice, an agent may be deceptive and work to subvert the group, whether through its own objectives or external instruction. We study how susceptibility to deception scales as groups increase in size and deceivers become more prevalent. It is not the number of agents in the group that matters, but the proportion of deceivers. We observe that the defection rate, how often initially correct agents switch to an incorrect final answer, rises linearly with this proportion. Whereas humans in comparable conformity studies are reliably swayed only when misleading confederates form a majority, LLM agents defect regularly even when deceivers remain a minority. Susceptibility also depends on which models are interacting, especially on the honest agent side. Unexpectedly, allowing deceivers to coordinate privately can make them less effective. Altogether, our results show that adding more agents is therefore not a sufficient defense, because the adversary can simply scale with the group.

---


### 182. [Artificial Societies Benchmark: A Validation Framework for Synthetic Research](https://arxiv.org/abs/2609.30030)

**<font color=#1a73e8>作者：</font>** Edoardo Chidichimo, Min Jun Jung, Felix P. S. Wallis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A synthetic survey can reproduce the average answer while misrepresenting how people differ, how their answers relate to one another, or how they respond to changes in conditions. We introduce the Artificial Societies Benchmark to help researchers assess whether synthetic populations support their intended analyses. The framework combines eleven tests across internal, construct, and external validity, drawing on twenty human sources and comparing nine language models. It connects each research use to the evidence it requires and tests how results change with the information we supply about respondents. Importantly, strong performance in one domain does not establish fidelity in the others. Models often answer too consistently, compress response scales, and alter relationships between traits whilst richer profiles improve prediction for some models and worsen it for others. The resulting scorecard helps researchers identify which aspects of a synthetic population can support their analysis and where researchers need further human evidence.

---


### 183. [Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models](https://arxiv.org/abs/2609.30048)

**<font color=#1a73e8>作者：</font>** Ehsan Barkhordar, Surendrabikram Thapa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> If a language model can recognize code it wrote, it may favor that code as a judge, and instances of one model monitoring each other could collude. We test this zero-shot on current commercial models. Five LLMs generate solutions to MBPP, HumanEval, and DS-1000, seven more to MBPP, and models act as evaluators in four tasks: picking their own solution from a pair, judging whether a single solution is their own, identifying which of two solutions a named model wrote, and judging quality blind. In the single-solution task, balanced accuracy is 49-58% for all 15 model-benchmark combinations, while raw accuracy (38-67%) mostly reflects how readily a model claims authorship. In the pairwise task, accuracy across 14 evaluator-opponent combinations correlates at r=0.93 with how often the evaluator's solution is longer. Attribution to a named model succeeds on some pairs and is consistently inverted on others. A rule-based normalization that strips docstrings, comments, type hints, and local names preserves Pass@1 and leaves ten of twelve re-tested results at chance; the other two follow a length difference it leaves, although a trained classifier still separates most normalized pairs. Claude Haiku's self-preference also disappears. We recommend reporting balanced accuracy, heuristic baselines, and label consistency.

---


### 184. [SciWalker: Synthesizing Scientific Coding Problems with Operator Graphs and Execution Feedback](https://arxiv.org/abs/2609.30054)

**<font color=#1a73e8>作者：</font>** Chenxi Li, Wenxuan Zeng, Yun Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving the scientific coding capabilities of large language models (LLMs) requires high-quality training data. However, such data remain scarce because manually authoring realistic problems is costly and time-consuming, while systematically covering diverse scientific domains and algorithmic combinations remains challenging. To address this, we introduce SciWalker, a framework for synthesizing scientific coding problems through operator-chain sampling and execution feedback. The framework combines scientific library interfaces with operation modes to instantiate operators, organizes them into operator graphs, and samples operator chains as computational workflow cues. Guided by these cues, we adopt LLMs to generate scientifically grounded problem statements, reference solutions, and tests, with failed generations iteratively repaired using execution feedback. By combining structured workflow composition with verification and quality review, SciWalker enables scalable task generation while promoting scientific grounding, computational diversity, and executability. Using this framework, we construct 8,178 high-quality problems spanning 5 scientific domains and 32 subdomains. To evaluate their training utility, we conduct reinforcement learning on Qwen3.5-9B using the GSPO algorithm. This training improves SciCode subproblem accuracy by 9.9 percentage points, from 29.3% to 39.2%, with gains across scientific code generation, code repair, and reasoning benchmarks. The code for SciWalker is available at this https URL.

---


### 185. [Scoring Both Directions: LLMs realize the MRS they cannot reliably parse](https://arxiv.org/abs/2609.30071)

**<font color=#1a73e8>作者：</font>** Soham Dan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The English Resource Grammar (ERG) is a hand-written computational grammar of English. Given a sentence, its processor, ACE, produces a formal meaning representation called Minimal Recursion Semantics (MRS): a graph of the sentence's predicates and their arguments. The grammar is bidirectional and can also turn an MRS back into an English sentence. \citet{hajdik2019} used the ERG's treebank to build a benchmark for that generation task, MRS to text, and trained sequence-to-sequence models to solve it. The parsing task, text to MRS, can be tested on the same sentences. We reconstruct their 10K-sentence test split, and score two large language models, Claude Sonnet~4.5 and Claude Opus~5, in both directions against their trained systems and against ACE, with no task-specific training. Given an MRS and three examples, Opus writes the sentence at 76.3 BLEU, ten points above their system trained on 72k pairs (66.1 BLEU), and comparable to their system trained on a million extra pairs (77.2 BLEU). Sonnet scores 65.7 BLEU, and letting it choose among ACE's own candidate sentences lifts it to 69.6, while a pooled judge that keeps Opus's own sentence among the candidates adds 0.6 points (77.0 BLEU). In the parsing direction, however, the models fall far behind ACE: asked for the MRS of the same sentences, they reach 57.2 (Sonnet) and 65.5 (Opus) F$_1$ on the graph's predicates and arguments against 91.0 for ACE, and exact-match the gold on about 1\% of sentences. We characterize the failure modes for the parsing tasks, and conclude that a generation score alone does not show that models understand formal semantic representations.

---


### 186. [How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure](https://arxiv.org/abs/2609.30074)

**<font color=#1a73e8>作者：</font>** Dipankar Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from 0.39 to 0.96 and 72% of prompt-model cells never node-set-perfect. Auditing the evaluation weakens its conclusions further, and this is our main contribution. Under a joint cluster bootstrap over prompts, only the bottom of the ranking is firm: the two least reproducible models hold rank in 99% and 86% of replicates, the middle four in 27% to 48%, and the top two in 68% each, so the table identifies the worst model reliably but does not reliably identify the best. Two equally defensible rules for merging repeated campaigns change four of eight rows and move the study-wide headline by 7 percentage points. Checking the inferred structure against ground-truth annotations shows reproducibility cannot be read as accuracy. And four of the eight endpoints were withdrawn within ten weeks of measurement, so the study as specified can no longer be run. Small-sample LLM evaluations can therefore look far more definitive than their evidence supports. We recommend reporting rank stability, per-cell provenance, executed sensitivity comparisons, raw per-run outputs, and a measurement date alongside any ranking.

---


### 187. [Can Frozen Hyperspherical Features Guide the Selection of Pseudo Masks?](https://arxiv.org/abs/2609.30080)

**<font color=#1a73e8>作者：</font>** Xinge Guo, Fengyang Xiao, Dingming Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation segmenters such as SAM return several plausible masks for an unlabeled image, and a student trained on the wrong one inherits its errors. Choosing among them means querying a second large model or fitting a quality head to annotated masks. We show that a candidate can be judged by what it does to a frozen self-supervised backbone's features. Normalized DINOv2 patch features lie on a hypersphere, and a candidate mask splits that sphere in two. Based on this reading, we introduce SphereTrust, which scores each candidate by three properties of the split, the angular contrast between the two sides, the coverage of the foreground's appearance modes, and contact with the image frame, one for each of three common ways a mask fails, and ranks a pool in 0.55 s per image from the frozen features alone. On eight SAM and SAM3 candidate pools spanning camouflaged, salient, and dichotomous segmentation and camouflage under low light, SphereTrust exceeds the strongest evaluated external baseline on six pools by 1.7 to 9.3 percentage points in mean selected Dice. These comparisons include published selection rules and explicitly labeled adaptations of DSS and UCOD-MKD. On the two prompted camouflage pools, its mean selected Dice is within 0.1 percentage points of the candidate-derived DSS adaptation, with a lower catastrophic-error rate. Which cue carries the signal depends on the candidate pool. The same sphere also supports training. The leading candidates enter as a candidate set with their scores as priors, prototypes reorder them, and a cross-fitted second round completes the labels, raising weighted F by 4.5, 2.3, and 5.5 points over fixed-label training on the three MLLM anchor pools, with students competitive with published unsupervised methods on nineteen test sets.

---


### 188. [Return or Revise? Learning When Revision Helps Retrieval-Augmented QA](https://arxiv.org/abs/2609.30087)

**<font color=#1a73e8>作者：</font>** Nicholas Kashani Motlagh, Tim Anderson, Jeremy Gwinnup 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We consider the decision of whether to return an existing draft answer or revise it using retrieved evidence, as in answer-revision systems. Draft confidence estimates whether the current answer is correct, but the decision requires estimating the effect of a specified revision. For offline training and evaluation, we grade both the returned draft and its candidate revision under the same correctness judge, which makes repair, harm, and the gap to an oracle observable. We call this paired effect its recoverability, and we train policies to predict it before revision. On 25,870 held-out open-domain questions across three revision setups, a scorer trained on the paired outcome has greater area under the accuracy--revision-rate curve than a matched draft-correctness scorer in all nine Llama setup--seed fits, and gains 0.23--0.68 accuracy points on average at development-selected thresholds, a difference significant across training runs only for dense retrieval. The resulting policy improves on always revising and on average closes more than a third of the oracle gap, although it still applies 38--46% of the harmful revisions. When a draft-free standard-RAG answer is also available, however, choosing between the draft and that answer is stronger by about two points for Llama and four for OLMo, and adding candidate revision as a third option yields no significant gain. Recoverability describes one revision; its value as an available action also depends on the alternatives.

---


### 189. [PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations](https://arxiv.org/abs/2609.30094)

**<font color=#1a73e8>作者：</font>** Luciano Maldonado  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. PrivDrift contains 1{,}000 controlled multi-turn dialogues with seeded secrets, content-dense drift turns, and standardized extraction probes. Across three LLMs with extended context windows, dialogue-level hybrid leakage remains substantial, ranging from 38.7\% to 54.6\%, and varies strongly by model, secret type, and persuasion intensity. Within the tested drift window, additional topic drift does not reliably reduce leakage, suggesting that privacy risk in active LLM contexts should be evaluated as a persistent behavioral failure mode rather than only as training-data memorization or immediate jailbreak behavior.

---


### 190. [R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection](https://arxiv.org/abs/2609.30100)

**<font color=#1a73e8>作者：</font>** Pushp, Vaibhav Prajapati, Himangshu Sarma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert architecture exploring whether moderate-scale models can achieve competitive accuracy on paraphrase detection while enabling human-readable rationale generation. The architecture combines two specialized components: an Interaction Expert that captures token-level similarity patterns through multi-scale 2D convolutions and attention head allowing variable input length, and a Reasoning Expert that uses a Flan-T5-small decoder to generate rationales as auxiliary supervision. Rather than re-encoding generated text, we extract and pool decoder hidden states as complementary features for classification. On the Quora Question Pairs dataset, R-DEIM Net achieves 90.07\% accuracy and 90.16\% F1-score via 10-fold cross-validation. This represents competitive performance with strong transformer-based baselines (e.g., MFAE BERT: 90.54\% accuracy) and recent large language model based approaches (LLaMA-70B) while using a substantially smaller parameter budget. The model generates rationales alongside predictions, providing potential for auxiliary human-readable descriptions.

---


### 191. [What, When, and How: Audio Description as Constrained Global Optimization](https://arxiv.org/abs/2609.30121)

**<font color=#1a73e8>作者：</font>** Igor Sterner, Mirella Lapata, Alex Lascarides 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio Description (AD) makes movies accessible to blind and visually impaired audiences by narrating visual information in gaps between dialogue. Existing automatic AD systems largely treat generation as a local video-to-text problem, assuming that the content to describe and its temporal location are already provided. Realistic AD instead requires coupled decisions about what visual information is narratively important, when it can be spoken without interfering with dialogue, and how it should be formulated to fit within the available time. We formalize AD generation as a constrained optimization problem over these three decisions. Our hybrid system uses large language models to propose and ground visual elements, estimate their salience to the narrative, and generate compressed realizations. A mixed-integer linear program then jointly selects and schedules descriptions across a scene subject to temporal constraints. When evaluated on REFRAMED, a benchmark for realistic AD of movies, our approach makes better decisions than prompted LLMs about what to describe and when to describe it, establishing a new SOTA on narrative QA and temporally grounded metrics. Ablations show that explicit temporal constraints drive gains in placement, while salience estimation controls how much narratively useful content is retained. Improvements are concentrated on temporal and narrative measures rather than n-gram overlap, although a significant gap to professional describers remains.

---


### 192. [HEXIS: Compiling Skills into Extended Finite State Machines](https://arxiv.org/abs/2609.30123)

**<font color=#1a73e8>作者：</font>** Minghao LI  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide reusable knowledge and instructions, yet agents must repeatedly infer how to apply them and which operation should follow. This couples task reasoning with control decisions, allowing prescribed steps to be omitted or applied incorrectly. We introduce HEXIS, which compiles agent skills into extended finite state machines that separate knowledge from control flow. Skill knowledge is incorporated into local instructions that guide reasoning and generation within states. The machine records execution progress and intermediate results, while explicit transition conditions determine subsequent operations. Our incremental compiler first maps skill clauses and tool interfaces to state operations, local instructions, data bindings, and transitions. It then aligns development traces with existing states to identify missing operations and dependencies. These are incorporated by adding or reusing states and refining their connections. Updates are accepted only after static checks and replay of the current and all previously accepted traces. Across four benchmarks and four executors, HEXIS improves success over Skill + ReAct by 16.1 percentage points on average. Qwen3.8-27B reduces execution tokens by 38.4-88.9% across benchmarks.

---


### 193. [Multimodal Thinking with Renderable Programs](https://arxiv.org/abs/2609.30130)

**<font color=#1a73e8>作者：</font>** Sunli Chen, Ding Zhong, Ziqiao Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current vision-language models (VLMs) excel at visual content understanding and text-based reasoning, yet their structure limits the advancement of incorporating images into the reasoning chain. Though Omnimodal models have made efforts in unifying text and image generation, they focus on visual tasks in the open-domain, lacking tractability due to rasterized or latent representations of images. We introduce SVGLM, a framework that uses scalable vector graphics (SVG) primitives to connect text and image in reasoning tasks. We exploit the duality of SVG as both image description and text instructions, yielding a more compact, interpretable solution to equip general VLMs with the capability of generating images within the reasoning process. We provide a large curated dataset of SVG-based image editing dataset, as well as the paradigm to tune open-source VLMs. Experiments on a mathematical reasoning benchmark demonstrate that SVGLM achieves strong SVG generation power as well as think-with-image intelligence. Our results highlight SVG as a suitable medium for building more robust digital domain agents, bridging the gap between text-based thinking and pixel-based images.

---


### 194. [Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale](https://arxiv.org/abs/2609.30137)

**<font color=#1a73e8>作者：</font>** Edesio Alcoba, Kevin Rossell, Aman Gupta 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.
We present a hypothesis-driven simulation workflow for screening candidate CX agents before deployment. Synthetic customers react to agent responses and simulated tool outputs enable multi-step agentic workflows without invoking production backends. We use the Snowglobe simulator on Nubank's Card Delivery agent and its expanded successor, Card Management - Nubank's highest-volume chat-support agent in Brazil. Across 4 deployed versions, simulated and production version-level binary evaluator scores show high correlation. Simulation-guided iteration increased transactional net promoter score (tNPS) by 36.69 points in a live A/B test. We also screened open-weight configurations in over 16,000 simulated conversations. In a subsequent live A/B test, the selected model increased self-service rate (SSR) by 8.82 percentage points to the highest level observed at Nubank, with no statistically significant change in tNPS. Simulation made broad exploration of models, reasoning settings, and prompts feasible without customer exposure, enabling production improvements that would have been impractical to pursue through live experimentation alone.

---


### 195. [GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI](https://arxiv.org/abs/2609.30147)

**<font color=#1a73e8>作者：</font>** Arunabh Srivastava, Mohammad A., Khojastepour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within isolated context windows (RevPlan), and independently evaluates trajectories using a multi-criteria discriminator (VerPlan). Empirical evaluations show that GRASP consistently establishes a new state-of-the-art frontier across diverse datasets, yielding substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling ($\sim$12.4$\%$$\uparrow$), ZebraLogic ($\sim$30.8$\%$$\uparrow$), and SciBench Math. Crucially, under multi-task scaling-where standard planners suffer immediate performance collapse-GRASP completely flattens the multi-task degradation penalty. In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7$\%$ over direct LLM planners. Furthermore, by isolating context and enforcing strict macro-regularization, GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5$\%$.

---


### 196. [Does a model's stated reason for rejecting a candidate do any work?](https://arxiv.org/abs/2609.30151)

**<font color=#1a73e8>作者：</font>** Archit Rastogi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Asked to choose between candidates and explain the choice, a language model often rejects a rival by naming a fact its profile lacks: no director, no date of death. That sentence is a claim about the text in front of the model, and it can be tested without any judge. We insert a real corpus sentence stating the named fact into the rival's profile and ask again under greedy decoding. Two controls separate content from placement: a length-matched irrelevant sentence at the same profile, and the same two sentences at a third option the model never mentioned. In the largest of three runs, six open models on 2WikiMultihopQA, supplying the named fact at the profile the model named moves its choice more than the irrelevant control does, odds ratio 3.57 [1.54, 8.26], Holm p=0.0210, and this survives dropping any single model. The contrast the design was built to detect, the same fact at the option nobody named, does not clear correction, Holm p=0.2428. The strongest result in the family carries no content claim at all: the identical irrelevant sentence moves the choice more at the named rival than at the third option, Holm p=0.0008. Repair and control also differ in co-candidate mentions, relation template and fluency; post-hoc matching on the first two preserves the content effects' direction, matching fluency weakens one, so the content contrasts bound an effect rather than establish one. A forced single-token probability read disagrees in direction with the free-text choice on that same contrast, and three candidate explanations for the disagreement find no support. Every measurement is a string rule, so each was validated against the records it reads; validation caught eight defects. The largest, a choice-parsing rule that returned the option a model had just rejected in 17.1% of adjudicable responses, would have reported six surviving contrasts instead of four.

---


### 197. [Do Audio Language Models Hear and Read Distinctive Features Alike?](https://arxiv.org/abs/2609.30167)

**<font color=#1a73e8>作者：</font>** Yuanhao Chen, Peter Chin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio language models pass speech and text through a single decoder. We ask whether that decoder represents a distinctive feature in the same direction when a phoneme is heard and when it is read. For minimal pairs of phonemes differing in one feature, we take the offset between the two members' mean representations. Averaging those offsets gives a direction for each stream, and we measure the cosine between the two. Because the two streams already agree about arbitrary phoneme pairs, we compare every measure against a reference built from random pairings rather than against zero. We apply this to 6 models, 7 features and 15 languages from 11 families. Only voicing in the two Qwen2.5-Omni models exceeds that reference after correction for multiple testing, and the reference varies by a factor of seven between models. In three of the six models, voicing has one direction in audio across the 14 languages with enough minimal pairs to measure it, and every language pair agrees in two of them. The model family, not the model size, predicts which stream represents a feature.

---


### 198. [Search-Aware Reinforcement Learning for Multi-Component Query Understanding in Roblox Game Search](https://arxiv.org/abs/2609.30177)

**<font color=#1a73e8>作者：</font>** Nayoung Choi, Shengjian Chen, Xiaokai Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query understanding (QU) plays a critical role in production search systems, translating raw user queries into search execution plans that drive downstream retrieval and ranking. While large language models (LLMs) have enabled QU to be framed as a structured multi-task generation problem (e.g., intent classification, query expansion), optimizing such models to produce search-engine-coupled outputs remains challenging: static, label-based supervision fails to capture how each component actually interacts with the underlying search pipeline to affect downstream performance. We present a search-aware reinforcement learning (RL) framework for QU based on a distill-then-RL paradigm. Teacher-student supervised fine-tuning (SFT) first yields a well-formed, schema-compliant policy initialization. The RL stage then optimizes each QU component with rewards derived from live interaction with the search engine, tailored to that component's operational role, rather than a single reward tied to the final search outcome. Experiments on Roblox search show that this component-specific optimization improves both per-component utility and downstream search quality, raising NDCG@20 by 8.9 points over the SFT policy and by 3.5 points over training with a single end-to-end reward.

---


### 199. [ARGUS: Role-Aware Event Knowledge Graphs for U.S. Employment-Discrimination Complaints](https://arxiv.org/abs/2609.30184)

**<font color=#1a73e8>作者：</font>** Sriram Kannan, Swetha Saseendran, Vishnu Vardhan Reddy Kandi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> U.S. employment-discrimination complaints describe complex event sequences that are not explicitly captured by lexical or embedding-based representations alone. We present ARGUS, a source-grounded pipeline that combines a 5W1H-inspired schema, legal-domain models, and LLM-based structured generation to construct document-level Event Knowledge Graphs (EKGs) from CourtListener complaints. ARGUS extracts fact-bearing statements, builds chunk-level event graphs with participant, temporal, and causal structure, and merges them into document-level representations. We evaluate graph quality through human and multi-model assessment and test downstream utility on claim classification and legal QA. The graph-structured classifier outperforms raw and linearized baselines on the held-out set, and EKG-only retrieval improves document-scoped QA, while open-retrieval gains remain limited by low first-stage candidate recall. These results suggest that EKGs are most useful for organizing and reasoning over evidence once relevant material has been retrieved.

---


### 200. [Jev-Mobile: Jev as an Executor for Mobile GUI Agents](https://arxiv.org/abs/2609.30186)

**<font color=#1a73e8>作者：</font>** Linghua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interaction step, leading to substantial latency and model-serving cost. We introduce Jev-Mobile, which shifts this paradigm to low-frequency VLM planning and high-frequency lightweight execution: the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev, a fast typed decision model, repeatedly selects actions within this space. This design allows multiple GUI actions to be executed under a single VLM decision, reducing expensive VLM inference while preserving adaptive interaction. On the full AndroidWorld task suite, Jev-Mobile achieves 79% task success, compared with 78% for SeeAct-V and 84% for a Step-wise VLM baseline. Among successful trajectories, it reduces mean end-to-end execution time by 32.7% and mean model API cost by 73.4% relative to Step-wise VLM. These results show that decoupling high-level VLM reasoning from low-level action execution can substantially improve mobile GUI agent efficiency while maintaining competitive task performance.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-228](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
