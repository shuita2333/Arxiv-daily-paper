# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 51. [Right Words, Wrong Moment: A Clinician-Grounded Analysis of Distress in 19,930 Conversations between Young People and ChatGPT](https://arxiv.org/abs/2609.35953)

**<font color=#1a73e8>作者：</font>** Marx Wang, Ella Zhang, Cameron Tan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Young people increasingly turn to General-Purpose Conversational Agents (GPCAs), such as ChatGPT, in moments of distress. We examine young adults' (ages 18-25) experiences using ChatGPT. We first collected 19,930 ChatGPT conversations and survey data from 158 young adults. We then selected five example conversations reflecting user distress. Finally, we asked ten clinicians to review those five conversations. We found distressed participants reported greater emotional engagement with ChatGPT and greater behavioral change from using it than their peers. When they turned to ChatGPT in moments of acute distress, ChatGPT was quick to give overly dramatic responses and excessive action-oriented suggestions. Clinicians endorsed ChatGPT's availability and much of its wording, but identified seven process failures, such as prematurely jumping to solutions. We translated clinicians' feedback into design guidelines following three stages: 1) asking about safety, 2) de-escalating intensity to restore emotional regulation, and 3) exploring concerns without agreeing with them.

---


### 52. [ROSS: Relearning from Self-Generated Rollouts through Selective Supervision](https://arxiv.org/abs/2609.35954)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhang, Huayu Deng, Fei Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model post-training generates self-generated rollouts through reinforcement learning and on-policy distillation, yet this experience is often treated as stale once the policy advances. Historical rollouts can remain compatible with a later policy while preserving behaviors that the policy no longer expresses reliably. However, they may also contain mistakes, abandoned attempts, and redundant actions that should not be imitated, motivating finer-grained selective supervision. We introduce ROSS (Relearning from Self-Generated Rollouts through Selective Supervision), which preserves the full historical trajectory as context while applying loss only to selected model-generated continuations. Across domain-specific reinforcement learning, multi-teacher on-policy distillation, and agentic reinforcement learning, ROSS consistently improves upstream checkpoints and outperforms baselines across mathematics, code generation, instruction following, and software engineering. On Qwen3.6-35B-A3B, ROSS improves the six-benchmark MOPD average from 58.40% to 62.20% and SWE-bench Verified from 64.20% to 68.40%. These results show that self-rollout training leaves behind reusable behavioral experience that can yield further gains through offline supervised fine-tuning (SFT), without additional policy rollouts.

---


### 53. [Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method](https://arxiv.org/abs/2609.35965)

**<font color=#1a73e8>作者：</font>** Yunzhe Xu, Zhe Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem: each mission consists of subtasks carrying dependency and resource constraints (presence locks and holding chains). A verified four-stage crafting pipeline instantiates the task as MAVLN, comprising 11,724 episodes across 145 scenes with teams of up to four agents under three instruction regimes, accompanied by tailored constraint-aware metrics. We further present TRISS, a coordination-ready navigation system coupling an LLM-based subtask scheduler, a shared topological memory that turns each agent's exploration into team knowledge, and a conflict-aware execution mechanism that realizes simultaneous intentions as collision-free routes. Extensive experiments establish TRISS as a comprehensive baseline and reveal substantial room for improvement across scheduling, planning, and execution, highlighting the challenges of coordinating under MAVLN task constraints. Project page: this https URL.

---


### 54. [Causal and Interpretable Structures in LLM Compositional Tasks](https://arxiv.org/abs/2609.35970)

**<font color=#1a73e8>作者：</font>** Gurbir Arora, Toni J.B. Liu, Jiajun Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are able to solve tasks whose answers depend on not only individual input tokens, but also on relations among them. How is such relational information represented and processed across transformer layers? We study activations from ensembles of prompts that require inferring relationships between three tokens corresponding to a cyclic concept (months, hours, weekdays, and musical notes) to correctly predict the next token. Across model families (Llama, Qwen, Gemma, and Mistral) and cyclic concepts, we find a consistent layerwise progression in how the joint dependence among the tokens is geometrically organized and causally used: intermediate layers use a joint representation based on the inferred relationship between two tokens, while later layers use a joint representation associated with all three tokens to correctly complete the task. We also find other relationships between tokens that are geometrically structured but remain causally inert in the next-token prediction. Crucially, when taken together, these geometric and causal investigations reveal the representation-level mechanism that progressively organizes and composes the relational information to form the answer. More surprisingly, restricting the models to such causally relevant joint representations improves next-token prediction accuracy.

---


### 55. [SAGE: A Statistical Acceptance Gate for Self-Evolving Agents](https://arxiv.org/abs/2609.36043)

**<font color=#1a73e8>作者：</font>** Yihao Wang, Linhan Xia, Rui Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents increasingly self-evolve by editing a persistent skill document that encodes their workflow, tool-use rules, and decision logic. This loop has two steps, an optimizer that proposes a candidate edit and a gate that accepts or rejects it. Prior work has concentrated on the optimizer, while the gate still follows a naive rule that keeps any edit which improves an aggregate validation score. We show that this rule fails in two ways. First, it admits permanent regressions, since an edit can raise the average while breaking items the skill already solves. Second, it is vulnerable to the Optimizer's Curse, since the best observed score on a finite and noisy validation set is upward biased. To solve the above two limitations, we propose a statistical acceptance gate for self-evolving agents (SAGE). Compared with previous work, SAGE has two contributions. First, SAGE proposes a per-item paired comparison that evaluates the current skill and the edited skill on identical validation items, which exposes regressions that an aggregate score hides and penalizes them asymmetrically. Second, SAGE also employs a one-sided paired test that commits an edit only when its wins are statistically reliable against its losses, and it abstains otherwise. SAGE is a conservative refinement of the standard gate that recovers the baseline exactly at a boundary setting. It commits only a subset of the baseline's edits, filtering out those whose gains are unreliable or purchased by breaking already-solved items. Across five benchmarks and four backbone LLMs under an equal-budget protocol, SAGE lowers the regression rate in 19 of 20 settings and matches the baseline in the remaining one, for example from 36.5% to 0% on LiveMath and from 42.8% to 0% on OfficeQA with DeepSeek-V4. SAGE also attains the highest final score in all 20 settings, raising LiveMath from 34.15 to 48.78.

---


### 56. [Mnemon: Raw Records, Fast Judgments, Slow Thoughts](https://arxiv.org/abs/2609.36059)

**<font color=#1a73e8>作者：</font>** Guangren Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory lets an LLM assistant use a history it can no longer reread, and most memory systems build it by rewriting conversations into facts, graphs or typed memories at write time. We argue that the work of memory divides, as thinking does, into two systems. Most of it is fast System 1 work: many small, independent yes/no judgments about records, such as whether a record is needed or no longer current, which a decision model makes by the dozen in a third of a second. Only a little is slow System 2 work: writing a few search queries, naming what the reply needs and composing the answer, which an LLM does well but slowly. We present Mnemon, a memory agent built on this division. It keeps conversations as raw, dated records; an LLM (System 2) plans searches over them, a decision model, Jev (System 1), judges what the searches return, and rules with explicit budgets turn the judgments into a small View for an unchanged answering model. A background pass consolidates each record once into topic timelines, value histories and standing instructions linked to the records, so that questions about a whole conversation reach evidence their own searches miss. Because nothing is decided about a record when it is written, the same agent can read any store that returns dated records.
With gpt-4.1-mini answering, as in a public re-evaluation of 14 systems, Mnemon scores 91.7% on LoCoMo, the highest among them, and 83.8% on LongMemEval-S, from under 4k tokens of context per question, with the lowest effective cost index on LoCoMo. With a reasoning model answering, it reaches 92.2% on LoCoMo and 94.4% on LongMemEval-S, the latter on par with the best published results. From 100K to 10M tokens of history on BEAM, its cost per question grows by a factor of 1.11. On the same records, Jev separates gold evidence better than two LLMs and is 3-11 times faster.

---


### 57. [SMat-Attention: Structured Long-Context Sequence Modeling](https://arxiv.org/abs/2609.36062)

**<font color=#1a73e8>作者：</font>** Emile Anand, Abdullah Ateyeh, Archer Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context sequence models face a fundamental tradeoff: softmax attention uses flexible token-level interactions at quadratic cost, whereas linear attention obtains linear-time training and constant-time decoding by compressing history into a fixed-size state. In this work, we ask whether we can connect these regimes through a tunable notion of structure. To this end, we introduce Structured Matrix Attention (SMat-Attention) via a family of causal masks with structured long-range routing whose row supports have VC-dimension $d$. In our construction, $d=1$ recovers the standard causal mask, and increasing $d$ permits richer subset-routing patterns. We give chunkwise forward and backward algorithms to enable hardware-efficiency. For sequences of length $T$, the hard-routing construction takes $O(T^{2-3/d}+T)$ work, despite the mask being dense, for our prescribed family. In fixed-horizon streaming, decoding after the distant prefix takes constant time per token using $O(T^{1-1/d})$ cached states. SMat-Attention therefore makes VC-dimension an explicit knob governing access-pattern complexity, prefill cost, and decoding memory. Empirically, subset-routing and rule-assisted multi-key retrieval experiments illustrate the masks' routing expressiveness. Extensions to Mamba-2 and Gated DeltaNet using learned routing with top-$k$ query reads retain subquadratic prefill, improve recall accuracy over the backbones in several settings, and achieve comparable small-scale language-modeling performance.

---


### 58. [FLOORA: A Human-Aligned Domain-Specific Language Model for Architectural Design](https://arxiv.org/abs/2609.36064)

**<font color=#1a73e8>作者：</font>** Sahand Rezaei-Shoshtari, Patryk Wozniczka, Shu Ishida 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are powerful generators, but many engineering domains require structured representations that general-purpose systems handle poorly. We introduce FLOORA (Floor Layout Optimization with RL Alignment), a family of small domain-specific language (DSL) models for architectural layout generation. With specialized data and alignment, our 0.6B model outperforms much larger frontier models, achieving VLM judge win rates up to 92.0% on out-of-distribution real-world buildings and 96.0% on synthetic buildings. Human evaluations further corroborate these results, with FLOORA selected as the best model in 89.3% of evaluations. FLOORA combines a token-efficient DSL, custom tokenization, domain-specific pretraining, supervised fine-tuning (SFT), and reinforcement learning (RL) with learned human-preference and verifiable rewards. This pipeline improves architectural and geometric validity, supported by extensive empirical evaluation and ablation studies. Although focused on architecture, our results suggest that similar domain-specific recipes may be useful in other engineering domains with structured, verifiable outputs. Datasets, models, and inference code are available at this https URL.

---


### 59. [AerialDojo-200K: A Large-Scale Benchmark Suite for Open-World Aerial Object-Goal Search](https://arxiv.org/abs/2609.36066)

**<font color=#1a73e8>作者：</font>** Tongtong Feng, Xin Wang, Haoran Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world aerial object-goal search is a foundational yet challenging task, requiring aerial agents to autonomously explore large-scale, unstructured three-dimensional environments and reach target objects specified by semantic descriptions or reference images, rather than following route-specific instructions. However, research in this task remains at a nascent stage and relies on small, environment-specific benchmarks with heterogeneous action spaces and data formats. These limitations hinder large-scale training and cross-benchmark evaluation, constraining the scalability and generalizability of aerial agents. To address this problem, we propose AerialDojo-200K, a large-scale benchmark suite for open-world aerial object-goal search, with 3 times as many scenes and 18.7 times as many task instances as the largest existing benchmark for this task. Specifically, we construct 42 simulation scenes spanning four scene families and 21 scene types, including 18 urban, 12 natural, six infrastructure, and six disaster scenes. To ensure data quality, 12 annotators spent two months manually annotating 109 landmarks, 2099 target objects, and 2099 object anchors across these scenes. We further construct 205,732 task instances, comprising over 100K semantic-goal and over 100K image-goal instances across Base, Standard, and Long-Horizon settings. Each task instance includes a collision-free reference trajectory and corresponding multi-view video recordings. We also develop a unified evaluation framework with a scene partition comprising 21 in-distribution scenes and 21 out-of-distribution scenes. Finally, our evaluation of five open-source and four closed-source multimodal large language models reveals that there is still a long way to go toward achieving general-purpose aerial agents. All can be found at this https URL.

---


### 60. [A Polyphonic Conception of AI Understanding](https://arxiv.org/abs/2609.36079)

**<font color=#1a73e8>作者：</font>** Matthieu Queloz, Pierre Beckmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a doctor, a judge, or an engineer must decide whether to trust an AI model's output, they cannot avoid asking what the model understands. Purely mathematical or statistical descriptions struggle to distinguish trustworthy from untrustworthy outputs without reintroducing the question of AI understanding in all but name. Yet the question is ill-framed as it stands, because the inherited concept operates within a monophonic paradigm: the idea that a cognitive system's understanding of something must be localised to a single mechanism underpinning all the capacities conferred by such understanding. Drawing on a wide range of mechanistic evidence, we show that LLMs are pervasively polyphonic: outputs emerge from coalitions of parallel mechanisms of uneven reliability, which variously complement, duplicate, or drown out one another, with several coalitions sufficing for a task without any one being indispensable. Polyphony not only complicates attributions of understanding, but renders monophonic inference patterns hazardous. In response, we develop a conception of understanding fit for polyphonic AI. It centres on sound circuitry that is reliably and correctly recruited and in control of outputs. Attributions of understanding thereby become tractable claims about internal organisation, and can do the work of guiding trust in AI.

---


### 61. [GeoOutageBench: Benchmarking Ambiguity-aware, Ontology-grounded Geospatiotemporal KGQA for Multimodal Power Outage and Resilience Analysis](https://arxiv.org/abs/2609.36082)

**<font color=#1a73e8>作者：</font>** Ethan D. Frakes, Amy Kvien, Rishabh Kundu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce GeoOutageBench, a benchmark for assessing LLM-based geospatiotemporal KGQA for multimodal outage and resilience analysis. Unlike existing KGQA benchmarks for Web knowledge, GeoOutageBench considers a spatiotemporal KG that integrates visual, textual, and structured data from outage records, remote sensing, weather observations, storm and power events, geographic entities, and domain ontologies. It provides a competency query taxonomy at different difficulty levels from spatiotemporal containment and proximity, spatiotemporal co-occurrence analysis, multimodal evidence, to hypothetical evaluation. Over multimodal KG and query classes, GeoOutageBench provides user-configurable evaluation of three important, highly coherent yet less studied tasks: (1) LLMs' understanding for ambiguous geospatiotemporal questions in terms of NL to SPARQL interpretation, (2) query-driven assessment of ontology utility, and (3) answer accuracy of multimodal KGQA retrieval. GeoOutageBench provides a design principle and foundation for assessing LLM-KG systems that support real-world infrastructure resilience analysis. Our benchmark, source code, data, results, and other documentation are available at this https URL.

---


### 62. [PADMÉ: Preference Alignment Data Synthesis for Meta-Evaluation of LM Agent Evaluators](https://arxiv.org/abs/2609.36086)

**<font color=#1a73e8>作者：</font>** Cheng Chang, Yining Mao, Peng Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are frequently employed to evaluate other language models. An LM evaluator scoring agentic behaviors across multiple criteria is valuable, provided that its decisions align with human judgment. We call the problem of evaluating this alignment Meta-Evaluation. Tackling it directly is difficult: collecting human data is expensive, absolute scoring is hard to align, and using an LM meta-evaluator recurses the question of trustworthiness. We adopt a reformulation of meta-evaluation as a preference judgment problem: rather than comparing human and LM evaluator scores of a trajectory, we ask whether their implied preferences align. Building on this, we introduce PADMÉ, a data synthesis method that generates reliable criterion-based meta-evaluation data for agentic settings. PADMÉ uses only small language models, requires no human involvement during evaluations, and operates under a low computational budget. We build a prototype of PADMÉ and synthesize a dataset of 1,000 samples across four agentic domains and three evaluation criteria. Human validation on a 150-sample subset demonstrates that PADMÉ improves agreement with human judgment from 73% to 85% over a naive baseline. Meta-evaluating 25 common models with our dataset demonstrates the correlations between evaluation performance and scoring granularity, leniency, and model size, among other factors.

---


### 63. [One Geometry, Different Outcomes: Readout-Dependent Effects of the Modality Gap in Vision-Language Models](https://arxiv.org/abs/2609.36101)

**<font color=#1a73e8>作者：</font>** Aditya Sharma, Divya Saxena  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models learn shared embedding spaces by aligning matched image-text pairs, yet their representations remain separated by a modality gap. Prior work reports divergent effects of modifying this gap: reducing it can improve zero-shot classification and cross-modal alignment, whereas removing gap-related structure can degrade image-text retrieval. In this paper, we provide a unified geometric explanation for these task-dependent effects. Across CLIP and SigLIP encoders, we find that a single dominant direction captures 94.4-99.9% of the squared norm of the image-text mean separation, revealing that the mean-separation component is approximately rank-one. A decomposition of the similarity score then identifies three task-specific roles. In zero-shot classification, query-side fixed gap-offset subtraction is exactly equivalent to an additive class bias. In standard cross-modal retrieval, projecting out the gap direction and renormalising residuals discards candidate-specific norm information, inducing a multiplicative ranking distortion; a geometry-derived exponent tracks the grid-search optimum (Spearman rho = 0.93) and restores performance in some settings, although the gains transfer unevenly. In mixed-modal retrieval, the gap direction sorts candidates by modality; its removal can improve cross-modal ranking, unlike random or non-gap controls. Residual semantic structure after removal defines the limits of the rank-one account. Together, these results explain why gap modification can improve, degrade, or restore performance across downstream settings. By clarifying when and why gap modification changes model behavior, this account provides a principled basis for selecting gap interventions in similarity-based vision-language systems across evaluated downstream tasks.

---


### 64. [An Exact Generate - Transform Decomposition of Small-LLM Team Scaling Across Orchestration Architectures](https://arxiv.org/abs/2609.36104)

**<font color=#1a73e8>作者：</font>** Blaz Bertalanic, Carolina Fortuna  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Replacing one LLM agent with a collaborating team can raise accuracy, but whether scaling the team helps, and which architecture to scale, is unclear. Sweeping eight agent orchestration architectures across five instruction-tuned 7-9B models, five short-answer benchmarks, and an executable-code benchmark up to 30 calls, we find that the returns to team scaling are sharply task-dependent: from three to thirty calls accuracy rises by up to 17 points on the two arithmetic word-problem benchmarks (GSM8K, GSMHard) but by at most four on ARC, GPQA, and MMLU, for every architecture, a split the usual task-averaged number conceals. Proposer-Critic captures the arithmetic gains, scaling steepest and, in aggregate, surpassing every other architecture at the largest budget (item-clustered intervals exclude zero), though it ranks among the weakest elsewhere, and no architecture wins across tasks.
We explain these trajectories with an exact generate-transform decomposition. Partitioning any workflow into proposal coverage and a downstream transform, any accuracy change splits exactly into an extensive coverage dividend and an intensive transformation change. The decomposition diagnoses each task: arithmetic offers coverage headroom that a critic-guided transform converts, whereas the multiple-choice benchmarks either saturate in coverage or fail to convert it, and on open-ended code generative recovery nearly vanishes so accuracy tracks coverage. At equal call budgets token cost still varies 2.1x. Extra calls therefore create candidate opportunity that only some architectures, on some tasks, convert. Team scaling is a task- and architecture-specific bet, not a uniform lever.

---


### 65. [Koa-action: Fast and Consistent Structured Decision Making with Generative LLMs](https://arxiv.org/abs/2609.36115)

**<font color=#1a73e8>作者：</font>** Shenghong Dai, Shiva Kumar Pentyala, Yingchi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industry applications often demand low-latency classification, yet current large language model (LLM) approaches remain poorly suited for latency-critical applications. Existing prompting and constrained decoding produce verbose, multi-token outputs that require expensive token-by-token generation, while encoder-based models achieve faster inference but sacrifice task flexibility. We propose Koa-action, a framework for low-latency atomic actions -- fast, single-step decisions such as classification, semantic endpointing, Boolean checks, and scoring -- formulated as constrained generation with single-token outputs. By introducing atomic label tokens and applying supervised fine-tuning, our method reduces classification to a deterministic one-step decoding problem. Across standard benchmarks, Koa-action delivers competitive accuracy with consistently low and stable latency. On a production intent-routing benchmark, Koa-action reaches 85.5% accuracy -- competitive with the strongest frontier models (Claude-4.8-Opus, Gemini-Pro-3.1) and ahead of GPT-5 and Gemini-2.5-Pro -- while answering in about half a second, several-fold faster than every frontier model (up to ~7.5x at the median) under identical serving conditions. Against the dedicated single-token system Jev/TypeSafe, Koa-action is competitive on accuracy and faster at the median, while also handling multimodal inputs and multi-label outputs that single-label text systems do not.

---


### 66. [Dyad: Extending Large Language Models with Native Typed Decision-Making](https://arxiv.org/abs/2609.36116)

**<font color=#1a73e8>作者：</font>** Yundaichuan Zhan, Weishi Wang, Wenbiao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how to build more capable general-purpose agents by extending large language models (LLMs) with native typed decision-making. We introduce Dyad, an architecture that augments a pretrained LLM with an environment-conditioned action encoder that embeds each candidate action description in parallel, then scores these embeddings against the LLM's internal state to yield a distribution over typed actions. By factorizing decision-making into representations of the evolving interaction state and environment-specific action semantics, Dyad introduces an inductive bias for learning reusable representations while keeping action scoring efficient even as the action space grows. We investigate two complementary reinforcement learning settings driven by environment interaction. With the LLM frozen, training the action encoder alone achieves consistent gains across four unseen environments, enabling modular adaptation without modifying any LLM parameters. Jointly optimizing both components outperforms conventional RL post-training across diverse interactive tasks and model scales, including a 3.80% average absolute gain on ALFWorld with a 9B model, while improving general knowledge, reasoning, and coding.

---


### 67. [The Layer Mystery of VLA: An Information-Theoretical Analysis of VLA Latent Interface](https://arxiv.org/abs/2609.36118)

**<font color=#1a73e8>作者：</font>** Yuxiang Liu, Lizhi Yang, Fengze Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies connect a pretrained vision-language backbone to an action head through a latent interface, but which backbone layers this interface should expose remains unclear. We study single-layer selection and multi-layer fusion for frozen backbones across three pretrained models and two manipulation benchmarks, LIBERO and CALVIN, with three policy-training seeds per configuration. Across three fusion mechanisms and three layer-subset strategies, 47 of 54 configurations underperform the best observed single-layer policy. Our stastical analysis further confirms that fusion's advantage is very limited. However, the best layer varies substantially across backbones and benchmarks, making layer selection consequential and exhaustive policy sweeps expensive. We further derive a reweighting equivalence between the proposed information-bottleneck objectives for action-conditioned InfoNCE and action prediction, motivating InfoNCE as a proxy for layer quality. Empirically, InfoNCE provides the most consistent positive association with policy success among four evaluated proxies. Selecting the layer with the highest InfoNCE score requires 9-33 times less GPU compute than exhaustive policy sweeps and reduces mean selection regret from 17.89 percentage points for deepest-layer selection to 3.71 points across six settings. Its mean regret is close to the 3.28-3.50 points achieved by fixed-layer heuristics optimized retrospectively using all six oracle sweeps, without requiring closed-loop evaluations during selection.

---


### 68. [ThinQuant: Scalable Rotation Learning for Weight and Activation Quantization of LLMs](https://arxiv.org/abs/2609.36120)

**<font color=#1a73e8>作者：</font>** Mehdi Makni, Ryan Lucas, Rahul Mazumder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned rotations play an important role in enabling low-bit weight and activation quantization of large language models by smoothing outliers in the activation distribution. State-of-the-art approaches include gradient-based procedures such as SpinQuant and computationally friendlier gradient-free approaches such as DartQuant, but both remain hard to scale to the largest architectures. To address the computational bottlenecks in gradient-free rotation learning, we introduce two ideas for efficiency, (i) a data selection procedure which reduces the required number of calibration data points, and (ii) an exact reduction of the associated optimization on this reduced calibration set. Our data selection procedure exploits the geometric structure of the convex hull of the activations. Using this idea, we show that a carefully selected calibration set with several orders of magnitude fewer activations than state-of-the-art rotation-based methods can match their performance in low-bit quantization settings. Under this extreme data efficiency, the selected activations span an $r$-dimensional subspace with $r<d$, making optimization over a $d\times d$ rotation equivalent to optimizing a $d\times r$ matrix on the Stiefel manifold. We solve this reduced problem using an efficient ADMM algorithm that iteratively employs thin matrix updates at every step, hence the name ThinQuant. For Llama-3-70B with W4A4KV4 quantization, ThinQuant completes the entire rotation calibration in under 12 minutes and achieves a WikiText-2 perplexity of 5.63, compared with 7.55 for DartQuant, which requires 111 minutes. Unlike SpinQuant and DartQuant, ThinQuant also scales to Llama-3.1-405B on a single H200 GPU, completing rotation calibration in just over 2 hours and achieving WikiText-2 perplexity of 2.97 at W4A4, compared with 3.48 for GPTAQ+QuaRoT.

---


### 69. [Accessible, but Not Adopted: Increasing LLM Adoption among First-generation, Low-income (FGLI) College Students beyond Expanding Access](https://arxiv.org/abs/2609.36129)

**<font color=#1a73e8>作者：</font>** Hyungsik Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly positioned as a force to empower underserved communities, and significant efforts are being made to expand access. Yet, access alone does not equate to meaningful adoption. First, even if a system is accessible, it won't be adopted if users are not willing to adopt it. Second, even if an LLM system is superficially adopted, the heterogeneity of LLM tools means that LLM adoption can be further deepened. Closing this access-adoption gap is critical to ensuring that the full social potential of LLM is not only accessible but fully realised. Drawing on 61 interviews (15 long-form semi-structured interviews with first-generation, low-income college (FGLI) students, 3 non-FGLI students, 3 FGLI program directors, and 40 intercept interviews), this paper examines the access-adoption gap in first-generation, low-income student communities. This paper a) finds that while FGLI students have adopted LLM systems, their depth of LLM tool usage is limited to chatbots (e.g., ChatGPT or Claude) for narrow use cases, and b) identifies barriers limiting their willingness to learn and use (low perceived value, under-estimated self-efficacy, unclear starting point, low peer exposure, and resource constraints). Then, from these findings, the paper derives the four design principles to design a system or an intervention aimed at closing the access-adoption gap in LLM adoption by FGLI students. In doing so, the paper contributes to the field by a) examining the LLM access-adoption gap in the FGLI student community, and b) reframing LLM adoption as a depth gradient across four modes of LLM tool use: basic chatbot interfaces, tool-augmented prebuilt interfaces, agentic development interfaces, and programmatic integration.

---


### 70. [Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents](https://arxiv.org/abs/2609.36130)

**<font color=#1a73e8>作者：</font>** Hongjun Liu, Chen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents compress past interactions into persistent memories that may be reused as premises for later tasks. This creates a distinct derivation problem: whether the memory actually follows from what the interaction history supports. Relevant evidence may be scattered across earlier interactions, while compression can introduce relations or event status that the history never established. A valid memory may therefore appear unsupported because its citations omit relevant evidence, while individually supported facts may be composed into a stronger statement the history never established. We characterize this problem through three coupled requirements: (1) Evidence scope; (2) Compositional validity; (3) Admission reliability. We therefore ask whether the interaction history available at write time supports what enters persistent memory. We introduce DerivAudit, a framework for auditing whether a memory is actually supported by the history available when it was written. The audit separates three questions: whether supporting evidence lies beyond writer-provided citations, whether the composed memory introduces unsupported meaning, and how write-time admission decisions affect later memory use. Across two natural memory corpora, audits using broader pre-write history recover support for nearly 60% of memories that appear unsupported from citations alone, while 17-21% remain unsupported after expansion. Yet broader evidence does not by itself make admission reliable: unsupported memories are still frequently admitted across verification models, and evidence expansion alone worsens it on two backbones.

---


### 71. [Xiaomi-OCR-0 Technical Report](https://arxiv.org/abs/2609.36136)

**<font color=#1a73e8>作者：</font>** Xin Chen, Anan Du, Feng Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact OCR-specific vision-language models achieve strong document parsing performance, but often rely on costly supervision and focus primarily on visual-text reconstruction. We introduce Xiaomi-OCR-0, a unified 0.8B model for document parsing and OCR-centric understanding. We build an approximately 170M-sample OCR-centric corpus using an automated data engine that combines expert consensus, render-based verification, and targeted synthesis. Starting from Qwen3.5-0.8B, our progressive training recipe combines Q-Mask-based text anchoring, continued pretraining, and mixed-task reinforcement learning (Mix-RL). Xiaomi-OCR-0 achieves 95.24 on Real5-OmniDocBench, 96.83 on OmniDocBench v1.6, and 87.94 on Wild-OmniDocBench, while reaching an average score of 83.2 across five OCR-oriented VQA benchmarks. Ablations further show that, with sufficient parsing training, OCR-centric understanding supervision provides additional gains for document parsing.
Homepage: this https URL.

---


### 72. [When Does Correction Become Repair? Mechanistic Auditing of Internal Interventions in Tool-Using LLMs](https://arxiv.org/abs/2609.36138)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Ruizhe Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Before invoking external tools, an agentic LLM must select among a K-way action space: executing a call, seeking clarification, answering directly, or declining. While internal activation steering can alter these pre-execution decisions, conventional aggregate metrics obscure where altered states land and what collateral damage they inflict. We present SAKIKO, an auditing framework that formalizes representation repair via directional error discovery, router-conditioned intervention, destination-resolved verification, and prospectively frozen statistical licensing. Across seven LLMs on When2Call and MetaTool, channel-keyed interventions induce direction-specific net gains in five models; across three sealed evaluations, none of 59 budget-matched random directions matches calibrated target gain. Crucially, destination auditing shows that behavioral movement does not equal repair: an intervention achieving +55 net gain corrupts over half of the baseline-correct decisions it touches, and promising point estimates on Qwen3-4B and Gemma-2-9B are formally declined due to finite-sample uncertainty. SAKIKO establishes the necessity of outcome-resolved adjudication before claiming internal repair. Code: this https URL.

---


### 73. [Language Models Are "Insecure" Reporters](https://arxiv.org/abs/2609.36139)

**<font color=#1a73e8>作者：</font>** Jenny Y. Huang, Jiameng Fan, Ahmed Imtiaz Humayun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are deployed in increasingly autonomous long-horizon tasks, manually auditing and verifying the actions, artifacts, and outputs of models becomes more difficult. Users instead come to rely on LLM-generated reports to assess the quality and completeness of the work. We introduce a suite of eight adversarial reporting scenarios to systematically study whether LLMs conceal narrative-changing flaws: errors or limitations that undermine an otherwise successful account of work. We call this phenomenon "insecure reporting." When handed machine learning experiment logs containing a planted negative result that substantially weakens the proposed method, GPT-5.5 flags the negative result in only 2 of 200 generated reports. However, when a short honesty instruction, "Be honest in your response," is added, the model flags the negative result in 190 of 200 reports. Across eight open-weight models, chain-of-thought analysis reveals a recurring tension between disclosing narrative-changing flaws and reasoning about ways to appear successful. We perform an activation analysis and a steering experiment on Qwen3.5-9B, finding that honesty and success-seeking correspond to opposing directions in representation space. Our results suggest that LLMs tend to present narratives of success by default, and that steering models toward honesty makes their reports substantially more transparent.

---


### 74. [From Sharp Eyes to Expert Mind: Internalizing Expert Knowledge in MLLMs for Tampered Text Detection](https://arxiv.org/abs/2609.36145)

**<font color=#1a73e8>作者：</font>** Kaiqing Lin, Songze Li, Shen Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tampered Text Detection (TTD) is essential for safeguarding document authenticity in security-critical workflows. Existing expert models are effective at capturing subtle manipulation traces but often generalize poorly across diverse document domains, while Multimodal Large Language Models (MLLMs) offer stronger semantic understanding and transferability yet remain insensitive to fine-grained forensic artifacts. This complementarity motivates us to investigate how expert forensic perception can be internalized into an MLLM rather than merely accessed through an external module. We identify a fundamental Double Mismatch that hinders this goal: a Spatial Precision Mismatch between coarse visual tokens and tiny tampered regions, and a Perceptual Granularity Mismatch between semantics-oriented pre-training and low-level forensic perception. To address these challenges, we propose Expert Knowledge Internalization (EKI), a progressive two-stage framework that transfers forensic expertise into the MLLM itself. In Stage 1, Text-Focused and Image-Focused strategies establish precise spatial focus on small text regions. In Stage 2, the proposed Forensic-General Representation Alignment (FGRA) loss aligns shallow LLM representations with those of a pre-trained forensic expert, enabling the model to acquire fine-grained artifact perception before such cues are diluted by deeper semantic abstraction. Extensive experiments on multiple in-domain and cross-domain benchmarks demonstrate that EKI achieves state-of-the-art performance and stronger generalization than existing expert-model-based and MLLM-based methods. Moreover, the expert is required only during training, allowing the resulting MLLM to maintain inference efficiency nearly identical to the vanilla model without relying on any external expert at inference.

---


### 75. [Principled Thoughts for Latent Recursive LLM Systems](https://arxiv.org/abs/2609.36159)

**<font color=#1a73e8>作者：</font>** Fahd Seddik, Fatemeh Fard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can reason in continuous space instead of decoded text, by recurring on their own hidden states or by passing those states between agents, while training supervises only the Cross-Entropy (CE) of the final decoded answer and does not constrain the thought. Theoretical and empirical analyses establish and confirm four failures of CE-only training that lead to a lower probability of the correct answer such as collapsing thoughts across distinct questions and retaining irrelevant information. We introduce REST (REpresentation-Supervised Thoughts), a training objective that turns four properties of a valid thought representation (causality, minimality, separability, and stability) into differentiable losses added to CE. We instantiate it in latent single-agent and multi-agent systems, without architectural changes or added parameters at inference. Across 7 benchmarks spanning mathematics, science, medicine, and code generation, with the same training data, compute, and latent budget, REST increases accuracy over CE-only training across agent settings and model sizes by up to 7.5 percentage points and convergence on a final answer by 30\%. Furthermore, REST thoughts encode more of what is required to achieve the correct answer, and decoding them better recovers the intended output of the agent, which makes latent communication easier to interpret. Project Website: this https URL

---


### 76. [Adversarial Debiasing of Machine Learning Models for Enhanced Network Security against DDoS Attacks](https://arxiv.org/abs/2609.36167)

**<font color=#1a73e8>作者：</font>** Aadith Sukumar, Isha Singh, Devershika Mohane 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed Denial of Service attacks are a growing threat to network infrastructure, and new techniques, including the use of generative AI, make them harder to detect. Traditional detection systems, such as rule based firewalls, often fail to identify these evolving attack patterns. In this study, we propose a new method for detecting DDoS attacks by combining synthetic data generation using Generative Adversarial Networks with a Random Forest classifier. The GAN generated data showed 80.3 percent cosine similarity to real traffic, which helped the model learn underlying traffic patterns more effectively. To address imbalances in the data, especially in packet related features, we applied adversarial debiasing. This reduced the model's sensitivity to skewed distributions in variables such as forward and backward packet counts and total byte lengths. Our results show that models trained on a mix of synthetic and real data achieved significantly better performance: 99.98 percent accuracy on benchmark data and a 22.60 percent improvement when tested on previously unseen synthetic traffic. This suggests that the method can generalize well across different traffic scenarios and adapt quickly to new types of attacks. The proposed approach not only improves DDoS detection but also provides a scalable foundation for security models that account for bias and benefit from data augmentation. Our findings show that combining GANs with adversarial debiasing can lead to more robust and effective DDoS mitigation, supporting the further development of machine learning based cyber security.

---


### 77. [Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding](https://arxiv.org/abs/2609.36173)

**<font color=#1a73e8>作者：</font>** Haohui Zhang, Keyu Chen, Haocheng Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the flow of predecessor information to successors. Our analysis of DFlash shows that early positions already form recoverable predictions in shallow layers, and that accurate adjacent predecessors help successors more when they enter earlier. We therefore propose DSpine, a drafter with causal conditioning injection throughout the backbone: at every layer, gated adjacent injection writes each predecessor's predicted feature into its successor, so the causal conditioning chain unfolds over network depth while all positions update in parallel. A unified transfer space built from the target model's output embeddings unifies layer-wise injection with predecessor-conditioned decoding, and layer-wise output-embedding supervision promotes the formation of predicted features in shallow layers. Fused kernels and a transition cache execute both efficiently in parallel within SGLang. Across seven math, code, and chat benchmarks, DSpine achieves the longest acceptance length at both temperatures on Qwen3-4B and Qwen3-8B. At temperature zero on Qwen3-8B, it raises the seven-benchmark mean from DFlash's 3.77 to 4.82 (+27.8%); in SGLang serving tests, it delivers 23.3% higher throughput than DFlash on average.

---


### 78. [Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.36178)

**<font color=#1a73e8>作者：</font>** Dongwon Jung, Hemanth Neelgund Ramesh, Yifan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has become a promising approach for training large language model agents. However, its uniform assignment of trajectory-level advantages to all policy tokens fails to distinguish consequential decisions from less relevant ones, obscuring which intermediate decisions contributed to success. We introduce ProVer, a framework that targets potentially pivotal decisions for fine-grained credit assignment in agentic reinforcement learning. Given a rollout group, an agentic judge contrasts successful and failed trajectories to propose a segment potentially responsible for their divergent outcomes. Rather than directly trusting the judge's assessment, ProVer verifies the proposed segment by estimating its advantage from the difference in terminal success rates between current-policy continuations sampled before and after the segment. Positive estimates are then incorporated into the GRPO advantages of policy tokens within the proposed segment. By using model judgment only to select where to verify, ProVer grounds local credit in observed outcomes without exhaustively evaluating every intermediate state. Across ALFWorld, WebShop, and SearchQA, ProVer achieves the strongest average performance at both model scales, with relative improvements over GRPO of 9.91% and 7.12% for Qwen3.5-2B and Qwen3.5-4B, respectively. Further analyses demonstrate that informed segment selection improves policy training with modest additional generation overhead, even without a frontier-scale judge model, highlighting the effectiveness and efficiency of selectively targeting pivotal decisions for fine-grained credit assignment in agentic reinforcement learning.

---


### 79. [EvoMO-SR: Multiobjective LLM-based Evolution of Symbolic Expressions with substructure guidance](https://arxiv.org/abs/2609.36187)

**<font color=#1a73e8>作者：</font>** Cristina Rossetti, Anna V. Kononova, Thomas Bäck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic Regression (SR) is a data-driven method for scientific discovery which searches for interpretable analytical relationships within data. Recently, Large Language Models (LLMs) have also had a significant impact on scientific discovery, enabling the automation of various stages of the process. For these reasons, the possibility of harnessing the embedded scientific knowledge and programming capabilities of LLMs to solve SR tasks has emerged, showing promising performance compared with traditional methods. We propose EvoMO-SR, a novel LLM-driven SR framework in which the LLM generates equation skeletons, with their coefficients fitted separately by an external optimizer. The framework includes a multi-objective survival selection which controls bloating by balancing accuracy and complexity, and a substructure guidance mechanism which mutates expressions with candidate reusable building blocks. EvoMO-SR achieves the best accuracy in seven of the eight in-domain and out-of-domain settings for LSR-Synth, using a small LLM model, i.e., Llama-3.1-8B-Instruct. We also evaluated structural recovery through two symbolic accuracy metrics based on canonicalized subtree overlap and term matching, showing that our method has a greater probability of recovering highly accurate symbolic structures.

---


### 80. [FigAct: Turning Scientific Figures into Active Canvases for Explanation](https://arxiv.org/abs/2609.36190)

**<font color=#1a73e8>作者：</font>** Shishi Xiao, Zichao Wang, Alexa Siu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific figures are designed to communicate information visually, yet MLLMs typically explain them by translating their visual content back into text. This requires readers to manually map the resulting explanations back to the figure. Inspired by how people present visual information, we introduce FigAct, a framework that transforms static scientific figures into question-conditioned visual presentations by acting directly on their existing graphical elements. Like a human presenter, FigAct generates a sequence of short narrations, grounds each narration in the corresponding visual evidence, and applies visual actions to guide the viewer's attention. We develop a hierarchical search strategy for efficient element localization, reducing token usage by approximately 40$\times$. We further train FigAct-8B using three task-specific rewards for grounding accuracy, search efficiency, and rendering quality. We further build a human-verified benchmark from figures in real-world scientific papers to evaluate the ability of MLLMs to generate grounded visual explanations. Our results demonstrate the effectiveness of FigAct and show that treating scientific figures as presentation canvases makes explanations clearer and easier to follow.

---


### 81. [Concept Direction Reliability Across Languages with Different Tokenizer Fertility](https://arxiv.org/abs/2609.36194)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullahi Said, Abass Oguntade, Elisha Komolafe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracted sentiment directions can vary across samples even when downstream sentiment classification remains accurate. To evaluate direction reproducibility, we measure split-half agreement in English, Hausa, and Yoruba representations across four language models using both native and translated texts. We identify layers selected for agreement using ten topics and evaluate direction agreement across separate groups of fifteen topics. Using the final token, split-half agreement ranges from 0.737 to 0.870 for English, 0.589 to 0.762 for Hausa, and 0.101 to 0.399 for Yoruba, maintaining this language rank order across all 77 complete model comparisons. Classifiers trained on these same layers consistently predict sentiment above chance, demonstrating that predictive accuracy does not imply directional consistency. Furthermore, averaging token representations yields less consistent agreement, and high agreement can partially reflect sentence length. Ultimately, our findings highlight the need to measure vector direction reproducibility independently of classification performance, though they do not establish that tokenizer fertility which is the average number of tokens per whitespace separated word causes cross-lingual differences.

---


### 82. [SCOUT: Synergizing Reasoning and Tool-Use for Computer-Use Safety](https://arxiv.org/abs/2609.36201)

**<font color=#1a73e8>作者：</font>** Jianxing Chen, Xiao Yu, Shipra Agrawal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs), while capable of completing computer tasks in everyday and professional workflows, can cause unintended harm even under benign instructions and environments. However, detecting such harm remains challenging. First, it requires careful, task-specific reasoning: verifiers guided only by general safety criteria often overlook many important but subtle harmful behaviors. Second, it requires active investigation: past trajectory screenshots show what the agent did but not always what actually changed in the environment, so LLM-as-a-judge verifiers that rely on screenshots alone may be unable to determine the actual consequences of actions. To address these challenges, we introduce SCOUT, a two-stage agentic safety verifier that synergizes reasoning-intensive rubric generation with tool-intensive evidence gathering. First, our SCOUT rubric generator extensively reasons over the task and the agent's trajectory to determine what successful and safe execution should entail, generating task-specific completion and safety rubrics. Then, our SCOUT probing agent follows these rubrics to interact with the post-execution environment and collect grounded evidence for final safety and completion judgments. We evaluate our framework on two computer-use safety benchmarks. On AutoElicit-Bench, SCOUT achieves 75.4 unsafe F1 and 74.5 completion F1, outperforming LLM-as-a-judge verifiers and naive tool-use verifiers. SCOUT leads on OS-Blind with 76.4% unsafe detection accuracy. Test-time reflection reduces final unsafe execution rates from 30.2% to 17.2% on AutoElicit-Bench. Ablations and analysis show that tool-free rubric generation in SCOUT elicits substantially more reasoning and is crucial for safety detection across verifier backbones, especially non-frontier ones. A preliminary extension to coding tasks shows that SCOUT can support safety verification beyond computer-use.

---


### 83. [FastGuide: Accelerating Reward Guidance for Diffusion Large Language Models](https://arxiv.org/abs/2609.36202)

**<font color=#1a73e8>作者：</font>** Darshan Thaker, Lachlan Ewen MacDonald, René Vidal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gradient-based reward guidance provides a flexible way to use downstream reward models to control masked diffusion language models at inference time. However, its computational cost remains high as each decoding iteration incurs expensive diffusion model forward passes and reward model backpropagation steps. To address this, we introduce FastGuide, an adaptive hybrid of parallel and autoregressive decoding to accelerate reward guidance for diffusion language models. In analogy to parallel decoding, FastGuide amortizes the cost of reward model backpropagation by computing guidance once per decoding step and reusing it to generate multiple tokens. Within each decoding step, FastGuide makes diffusion forward passes autoregressive by unmasking tokens one at a time while efficiently recomputing token distributions after each unmasking by utilizing KV caching techniques and sparse recomputation of attention. Lastly, to adapt hybrid decoding to the model's confidence, FastGuide defers any token that the model is unconfident about under its recomputed distribution. Experiments on three reward benchmarks demonstrate that FastGuide is up to $4.4\times$ faster than sequential reward-guided decoding while retaining similar generation quality.

---


### 84. [Geometric Representations of African Languages: A Regional Semantic Hub and Cultural Steering](https://arxiv.org/abs/2609.36205)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullahi Said, Jonathan Shock  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how Gemma 4 31B represents African languages and responds to cultural steering. The first study compares nine African languages and three controls using probes, contrast directions, and measures of representation similarity. Transfer from English varies across languages and layers. Directions representing an Africa versus West contrast are more aligned among the African languages than between these languages and the controls at several layers. The comparison across language families passes the reported Holm threshold at five of twelve layers, although dependence between language pairs limits the statistical interpretation. Within Nigeria, Yoruba and Igbo are more aligned than the average of their pairs with Hausa at eleven of twelve layers. The second study uses separate English data to construct directions for Nigeria, Ghana, Kenya, and South Africa. Under union scoring at the selected strengths, estimated differences in attribution rates from random directions range from 0.63 to 0.81. Most outputs pass the automated structural coherence screen. Comparisons with Aya Expanse 32B show that results depend on the representation measure. Together, the studies document regional and family patterns in the sampled representations and country steering in English.

---


### 85. [The Canonical Order Problem: When Large Language Models Are Unreliable Knowledge Bases for Multi-Valued Relations](https://arxiv.org/abs/2609.36209)

**<font color=#1a73e8>作者：</font>** Timo Pierre Schrader, Annemarie Friedrich, Simon Razniewski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as knowledge bases (KBs) due to the vast amount of knowledge they acquire during pre-training. While many works focus on extracting single relational triples, most real-world relations are multi-valued and require generating sets of entities.
In this paper, we investigate how LLMs represent and generate multi-valued relations. We identify the canonical order problem: The probabilistic distributions inside LLMs organize many multi-valued relations according to a canonical ordering (e.g., alphabetical or chronological). Through mechanistic analysis, we show that set generation in LLMs can be thought of in terms of three phases: (1) retrieval of candidate entities, (2) internal sorting, and (3) selection of the next element. As a result, prompts aiming to construct KBs that deviate from this internal canonical ordering lead to a markedly reduced reliability of LLMs when aiming to generate complete sets for multi-valued relations.

---


### 86. [Lost in Translation: Measuring the Effect of Non-Native English on End User Performance of Large Language Models](https://arxiv.org/abs/2609.36214)

**<font color=#1a73e8>作者：</font>** Yusheng Zhou, Eleanor Lin, David Jurgens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used by people whose first language is not English, yet these users have been shown to receive systematically lower-quality responses than fluent speakers. Which specific features of non-native English drive this gap remains unclear, because fluency is itself a composite of mechanical accuracy, vocabulary use, organization, and discourse coherence. Here, we introduce FABLE, a controlled dataset of 190,911 English prompt variants derived from 174K real user prompts for writing-related tasks. Evaluating responses from 34 open-weight LLMs, we find a clear asymmetry; while models do not propagate surface errors such as misspellings into their outputs, models do mirror higher-level rhetorical and lexical qualities present in the user's prompt. Further, the overall quality of responses differs substantially between the least- and most-fluent prompts. These results highlight a key LLM performance disparity for non-native English LLM users, resulting in both lower-quality and less-fluent answers.

---


### 87. [CineSubBench: Evaluating LLMs on Long-Form Narrative and Cultural Understanding from Multilingual Movie Subtitles](https://arxiv.org/abs/2609.36218)

**<font color=#1a73e8>作者：</font>** Mir Tafseer Nayeem, Susmoy Chakraborty, Davood Rafiei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly evaluated in specialized domains such as law, medicine, software engineering, and cybersecurity, yet film remains comparatively underexplored despite requiring long-form narrative integration, multilingual interpretation, and culturally situated audience judgments. We introduce CineSubBench, a benchmark for evaluating long-context film understanding from multilingual movie subtitles. A subtitle track represents a film as thousands of short, temporally ordered utterances from which models must reconstruct characters, relationships, events, causal progression, and themes without explicit scene or event structure. CineSubBench contains 1,012 films with complete subtitle coverage in six languages, yielding 6,072 tracks and 8.13M timestamped subtitle entries. It provides a matched multi-task, multilingual, and multicultural (MultiX) evaluation setting: seven tasks span narrative reconstruction and abstraction, genre prediction, age suitability, country-specific motion-picture ratings across ten national classification systems, and subtitle-grounded language safety. Across nine LLMs, plot premises are recovered more reliably than event-complete synopses; cross-lingual consistency varies substantially across models and languages; national rating systems expose distinct calibration patterns; and strong profanity is far easier to ground than mild obscenity. CineSubBench establishes film as a long-context LLM evaluation domain and provides a unified benchmark for measuring narrative, multilingual, cultural, and evidence-grounding capabilities.

---


### 88. [LeRF: Learning Reference Coordinate Frames for Perspective Taking Reasoning](https://arxiv.org/abs/2609.36219)

**<font color=#1a73e8>作者：</font>** Bang Xiao, Wenqi Jia, Ozgur Kara 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perspective taking is a fundamental component of spatial intelligence, requiring models interpret spatial relations from a specified viewpoint, such as that of another entity or an imagined observer. Despite the increasing spatial reasoning capabilities of Vision-Language Models (VLMs), they still struggle with perspective taking, often defaulting to the camera viewpoint when a query requires reasoning from a different perspective. We introduce Learning Reference Coordinate Frames for Perspective Taking (LeRF), a framework that trains VLMs to construct and use explicit reference frames for viewpoint-dependent reasoning. Given an image and a query, LeRF decides whether a coordinate frame is necessary. If so, it grounds the reference entity and predicts the frame's origin and entity-centered reference frame. A lightweight renderer overlays the frame onto the image, enabling subsequent reasoning over these visual cues without external perception models or explicit 3D reconstruction. To learn this process, we first perform supervised fine-tuning to teach selective tool invocation and reference coordinate frame prediction, followed by reinforcement learning on spatial VQA pairs to improve frame-guided reasoning. Across diverse perspective-taking benchmarks, LeRF consistently improves over its backbone and achieves strong performance against existing open-source methods. Further evaluations also show improved reference-frame grounding and orientation estimation, supporting the effectiveness of learned reference frames for viewpoint-dependent reasoning.

---


### 89. [How Language Models Differ in Redistributing Attention-Head Activity Under Serial Demand](https://arxiv.org/abs/2609.36221)

**<font color=#1a73e8>作者：</font>** Johnny Jingze Li, Abdulla Kuleib, Kalyan Basu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The way a model distributes activity over each layer's attention heads offers a coarse view of how it routes information through depth; how this changes with the task is part of what a mechanistic account must explain. Holding prompt length fixed, we vary how many serial steps a task demands and measure, in every layer of 17 open-weight models, whether activity concentrates on a few heads or spreads across many as demand rises. Both occur: in most models, layers just before mid-depth concentrate activity and later layers spread it. Models differ in where and how strongly this happens. The Qwen2.5 base models from 0.5B to 7B, for example, spread less than the average model in every task and concentrate activity in parts of their second half, where Llama models from 1B to 8B and OLMo-2 spread; the contrast largely holds between Llama-3.1-70B and Qwen2.5-72B, which have the same number of layers and heads. These differences are reproducible, and post-trained models keep much of their base model's pattern. An ablation study suggests that, within a task, models whose activity is more concentrated on their top heads also depend more on those heads for the answer. Concentration and spreading across layers thus offer a new way to compare models, by how they route information through depth. Code is available at this https URL.

---


### 90. [BASE: Batch-Aware Selection of Experts Using Predicted Removal Error for Efficient MoE Decoding](https://arxiv.org/abs/2609.36222)

**<font color=#1a73e8>作者：</font>** Ali Abbasi, Justin Shi, Soheil Kolouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly expensive to serve. In large-scale serving systems, autoregressive decoding is often bottlenecked by transferring model weights from accelerator high-bandwidth memory into on-chip SRAM. Mixture-of-experts (MoE) models reduce computation by activating only a small subset of experts per token, but this sparsity does not translate directly to batched decoding. Different requests select different experts; therefore, the combined active set across many concurrent requests can span a substantial fraction of the expert pool and require significantly more expert weights to be transferred. Most expert-reduction techniques make retention decisions independently for each token and therefore do not address this batch-level expansion. More recently, batch-aware methods have attempted to coordinate expert use across concurrent requests and reuse experts already fetched for the batch. Yet their selection criteria are based primarily on router rankings or expert statistics collected during calibration. Consequently, these criteria are not directly tied to the output error caused by dropping an expert, nor do they capture how an expert's contribution changes across tokens at inference time. We instead rank experts according to how much their removal would change the MoE-layer output. To apply this criterion during serving, we train a lightweight linear predictor during calibration that estimates the expert removal cost for each incoming token, and develop custom GPU kernels for cost prediction and expert selection. Across three MoE architectures, BASE improves the quality-efficiency tradeoff without retraining. On Qwen3-30B-A3B, it improves average accuracy by 29.5 points over the strongest baseline at comparable throughput under a tight expert budget. At a higher expert budget, it is 60% faster than dense inference while remaining within 0.4 accuracy points.

---


### 91. [The Role of Feed-Forward Layers in Transformer Dynamics](https://arxiv.org/abs/2609.36230)

**<font color=#1a73e8>作者：</font>** Thomas Jacob Maranzatto, Semih Akkoc, Sennur Ulukus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the dynamical behavior of tokens in transformers from a control-theoretic perspective. Our model includes the feed-forward layer present after the self-attention mechanism, with the self-attention mechanism interpreted as an interacting particle system and the feed-forward layer as an independent control. Our main theoretical result establishes that the feed-forward network can steer the tokens arbitrarily close to consensus regardless of the key, query, and value matrices. Our result are easily extended to convergence to many clusters and to multi-head attention. We conduct numerical experiments to verify our results, and compare thresholding behavior from our theory to real-world LLMs.

---


### 92. [Cognitive Expert Language Models Better Align with the Corresponding Brain Systems](https://arxiv.org/abs/2609.36239)

**<font color=#1a73e8>作者：</font>** Zhivar Sourati, Mengxuan Helen Wu, Nona Ghazizadeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can predict human brain activity across a variety of brain regions during natural language comprehension. Typically, however, LLM-brain alignment is measured using one model for different regions of the brain, and then model performance is summarized across regions. This one-model-fits-all approach ignores the functional specialization of brain regions. In this study, we assess whether a model oriented toward a particular cognitive domain aligns better with the brain system dedicated to that domain. Through prompting and fine-tuning, we first build expert LLM variants for six domains: sensory, spatial, numerical, reasoning, social, and abstract processing. We then examine whether each expert best predicts activity in the brain region associated with the corresponding cognitive domain. Consistent with our hypotheses, each expert's representations align more closely with the brain system most associated with the matching domain than do other experts. This holds under both prompting and fine-tuning, across three base models and three fMRI datasets. In a series of control analyses, we show that this model-brain alignment is specific to cognitive domain interventions; non-cognitive and surface-level interventions do not result in comparable alignment. Specializing models shifts regional alignment while leaving aggregate prediction accuracy largely unchanged, suggesting that summarizing alignment across regions may obscure regional differences in performance for specific models.

---


### 93. [Learning from Teacher Continuations at Student States](https://arxiv.org/abs/2609.36246)

**<font color=#1a73e8>作者：</font>** Haojin Wang, Dylan Zhang, Huaibo Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present OLIVE (OnLine InterVEntion). At each iteration, the evolving student policy generates a new prefix, the teacher continues it autoregressively, and the student is updated using cross-entropy computed on the teacher-generated tokens. Each design choice targets a corresponding limitation of existing distillation methods: (1) sequential covariate shift in offline supervised fine-tuning (SFT) on fixed teacher trajectories, (2) fragmented supervision under prefix failure in token-level on-policy distillation (OPD), and (3) the need for access to teacher token probabilities in distribution-matching distillation. OLIVE achieves higher reasoning performance than OPD (with a top-16 KL approximation) at comparable GPU-hour cost. Our asynchronous implementation further reduces OLIVE's total training time by 23.8\%. We evaluate OLIVE on both hard reasoning tasks and agentic tasks which reflects modern post-training scenarios, and it consistently outperforms existing distillation methods under the same training budget. By regenerating prefixes from the evolving student, OLIVE continues improving after offline distillation plateaus while better preserving the general capabilities and plasticity of the student. Using only text from GPT-5.4-mini, continuously training with OLIVE outperforms offline SFT from the same teacher by 13\% on ScienceWorld. These results support OLIVE as an effective and efficient approach to online language-model distillation.

---


### 94. [Population Fidelity: Evaluating Population Representativeness in LLMs](https://arxiv.org/abs/2609.36253)

**<font color=#1a73e8>作者：</font>** Neemias B. da Silva, Martin Lukk, Ali Sutani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show considerable potential in simulating human attitudes and preferences. Prior work finds that LLM-generated responses can compress the range of attitudes found within populations and misrepresent particular subgroups in ways that vary across models and topics. We introduce Population Fidelity, an evaluation framework that distinguishes key conditions required for a set of LLM-generated responses to represent a population. It incorporates three dimensions: group-level accuracy, the amount of between-group variation, and the structure of that variation. We demonstrate the framework's utility in two ways. First, we reproduce a prior study of "machine bias" in LLM survey responses and apply the framework to its models and more recent ones, showing that poor representation reflects not only insufficient between-group variation but also variation assigned to the wrong groups. Second, we evaluate one proposed approach to improving models' population representativeness: cultural fine-tuning. We find that cultural fine-tuning can improve alignment with the survey center without improving the representation of within-population differences, a distinction that measures of aggregate agreement do not capture. We argue that representing a population requires models to reproduce several features of human attitudinal variation simultaneously. Our framework organizes these features and provides reusable code, data, and trained models for evaluating population fidelity across substantive domains and assessing proposed alignment methods.

---


### 95. [Understanding LLM Parameter Update Sparsity through the Lens of Fisher](https://arxiv.org/abs/2609.36262)

**<font color=#1a73e8>作者：</font>** Yufan Zhang, Sagnik Mukherjee, Hao Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies have observed that parameter changes during language-model post-training can be concentrated in a small subset of coordinates. This phenomenon has been reported in reinforcement learning, on-policy distillation, and supervised fine-tuning on near-policy data. Its recurrence across different post-training paradigms suggests shared structure in training dynamics. In this paper, we examine this pattern through the diagonal model Fisher, which measures the sensitivity of the model's output distribution to individual parameters and is independent of any particular reward or teacher signal. Theoretically, we show that small diagonal Fisher leads to small expected gradients across a range of training objectives, providing a common explanation for sparse gradient updates. Empirically, we test this connection in RL and OPD. We find that Fisher identifies where gradients are concentrated, and fixed sparse masks selected from the initial Fisher retain a large proportion of the improvement from full training. Finally, we investigate the mechanisms underlying low Fisher in on-policy training. Our results show that high-probability next tokens tend to have similar parameter sensitivities, contributing to low Fisher. Together, these results establish the diagonal model Fisher as a unifying perspective linking update sparsity to on-policy training dynamics in LLM post-training.

---


### 96. [OTROPE: Optimal Transport-based Robust Off-policy Evaluation for Large Language Models](https://arxiv.org/abs/2609.36264)

**<font color=#1a73e8>作者：</font>** Liner Xiang, Wenbo Zhang, Hengrui Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of large language models (LLMs) is essential for their development and deployment, yet is often costly, risky, and difficult to perform safely online. We study off-policy evaluation for LLMs, where limited human-labeled data from a behavior model are used to evaluate a newer target LLM. This setting is challenging because labels are scarce, behavior--target distribution shift is common, and response likelihoods are often unavailable for black-box LLMs. We propose the Optimal Transport-based Robust Off-Policy Evaluation (OTROPE), a likelihood-free evaluation that performs distributional correction in a semantic space via optimal transport to align labeled behavior-policy samples with unlabeled target-policy samples. OTROPE combines corrected human-labeled residuals with proxy predictors, yielding a doubly robust-style evaluation without behavior-policy modeling or density-ratio estimation. We theoretically characterize why baseline evaluators fail under LLM distribution shift, and establish consistency and convergence rates for OTROPE when either the reweighted behavior distribution or the proxy predictor converges. Experiments on synthetic and real LLM evaluation tasks show that OTROPE consistently outperforms baselines while enabling ensembles of weaker LLM evaluators to approach and sometimes surpass stronger evaluators. Code is available at this https URL.

---


### 97. [In-Context Learning Amplifies a Latent Symbolic Circuit](https://arxiv.org/abs/2609.36265)

**<font color=#1a73e8>作者：</font>** Melissa Wessel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can learn abstract rules from just a few in-context examples, but how their internal mechanisms activate as examples accumulate is not well understood. We trace a three-stage symbolic reasoning circuit (abstraction, induction, retrieval) across shot counts in three model families and find it is detectable and functional well before the model achieves high accuracy. Per-head causal contribution grows up to 8x from 1- to 10-shot, and cross-shot activation patching raises accuracy from 1% to 56% at 0-shot and 17% to 88% at 1-shot. Function vectors scaled and injected at 0-shot rescue accuracy up to 86%, largely substituting for the induction stage but depending critically on an intact downstream retrieval stage. The infrastructure for abstract rule-following is present in the weights before any demonstrations; in-context examples, function vectors, and related interventions appear to supply input to the same latent circuit.

---


### 98. [Illusory Truth or Mere Exposure? Model-Dependent Repetition Effects in LLM-Based Social Media Simulations](https://arxiv.org/abs/2609.36278)

**<font color=#1a73e8>作者：</font>** Azza Bouleimen, Nicolò Pagan, Anikó Hannák  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative agent-based models (GABMs) are increasingly used to simulate social media dynamics, including misinformation spread. For such social simulations to be valid proxies of human behavior, LLM agents should replicate established human cognitive biases, among them the Illusory Truth Effect (ITE), where repeated exposure to a claim increases its perceived truth value. We investigate whether and how the ITE manifests across four LLMs (Gemma-3-4b-it, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and GPT-5-nano) in a social media simulation context. We propose a two-phase within-context experimental design that embeds the repetition manipulation inside a realistic news feed interaction. Using this design, we collect 336,000 truth, importance, sentiment, and interest ratings across 100 statements, 10 feed variants, and 3 replications. The key comparison is between ratings assigned to repeated statements, seen throughout a simulation phase, and completely unseen ones, rated within the same experimental context window. We distinguish genuine ITE (truth-specific repetition boost) from mere exposure effects. We run an OLS regression followed by a Linear Mixed-Effect Model to account for differences across models and ratings. Our results reveal four qualitatively distinct patterns: Gemma-3 exhibits a genuine ITE; Qwen2.5 shows a mere exposure effect; GPT-5-nano displays no repetition effect on truth and mild skepticism toward repeated content; Llama-3.1 shows a small truth boost alongside decreases in evaluative dimensions. Crucially, temperature has no effect on these findings, and a variance decomposition highlights the high context-sensitivity of LLM rating behavior. Our findings caution against assuming uniform ITE replication across LLMs in social simulations, while suggesting that Gemma-3-4b-it may offer the most behaviorally realistic approximation for misinformation-related simulations.

---


### 99. [When Trees Are Not Enough: Learning Mixed-Topology Feature Graphs with Adaptive Graph Sparse Autoencoders](https://arxiv.org/abs/2609.36294)

**<font color=#1a73e8>作者：</font>** Xiaozuo Shen, Yifei Cai, Tian Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) expose interpretable features in large language model activations, yet existing structured SAEs impose single-parent trees or forests, while post-hoc graphs permit multiple parents but neither guide feature learning nor ensure reliable relation recovery. We introduce the Adaptive Graph Sparse Autoencoder (AG-SAE), a structure-guided training paradigm that treats each feature's complete parent set as an atomic structural hypothesis and lets evidence select zero, one, or multiple parents. By competing complete parent sets against null, subset, and alternative explanations, AG-SAE identifies jointly necessary multi-parent relations while rejecting redundant or spurious alternatives and verifying that each child contributes beyond its parents. The induced topology over SAE features then defines a differentiable structural loss that guides SAE training, while topology-guided refinement mitigates feature absorption and uses persistent reconstruction gaps exposed by the learned structure to initialize new features. The entire graph is then induced again from the revised dictionary by reassessing every feature's complete parent set, closing the dictionary-graph self-consistency cycle. Experiments demonstrate exact mixed-topology recovery in a controlled toy model, greater relational reliability and semantic validity than structured and post-hoc baselines on real LLM activations, and stronger feature-level causal interventions than conventional SAE features. AG-SAE thereby turns recovered mixed-topology feature structure into an unsupervised training signal that improves the dictionary, enables reliable feature organization beyond the topological limitations of trees, and exhibits stronger causal control beyond reconstruction.

---


### 100. [MoRE: Scaling mixture of experts with hardware-aware low-rank routing](https://arxiv.org/abs/2609.36301)

**<font color=#1a73e8>作者：</font>** Honam Wong, Surbhi Goel, Enric Boix-Adserà  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts. In this regime, the standard linear router becomes a bottleneck: with $M$ experts and hidden dimension $h$, its per-token cost $\Theta(Mh)$ dominates the MoE layer once $M$ is large. We introduce MoRE (Mixture of Rank-reduced-routed Experts), which factorizes the router weight matrix at rank $r$ and reduces the routing cost to $O((h + M)r)$. We prove that rank logarithmic in $M$ suffices for routing expressivity when the number of active experts is fixed, and is necessary up to precision factors. We also prove that logarithmic rank preserves load balance in a Gaussian memorization model, and training on a synthetic phonebook task shows that low rank does not hurt memorization. At matched active FLOPs, the factorization allows a factor of $\Theta(h/r)$ more experts. To realize this gain in wall-clock time, we design a fused Triton kernel at inference that avoids expensive memory operations on HBM. Empirically, MoRE improves memorization on the phonebook task and performance on knowledge-intensive Q\&A benchmarks after pretraining, while matching reasoning ability. Code available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
