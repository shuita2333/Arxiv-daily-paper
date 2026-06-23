# 🧠 大模型相关研究 | 2026年06月23日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 1. [Less is More: Lightweight Prompt Compression for Question Answering Applications on Edge Devices](https://arxiv.org/abs/2606.20571)

**<font color=#1a73e8>作者：</font>** Zihuai Xu, Ruofei Hou, Yang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In agent-driven question answering (QA) applications, retrieval-augmented generation (RAG) is commonly introduced to enhance the response accuracy of large language models (LLMs) by providing additional context. Due to the inherent noise in retrieval results and the coarse granularity of document-level retrieval, the retrieved context often contains substantial redundant information. In this setting, the agent prompt, consisting of the user query and the associated retrieved context, leads to unnecessary computational overhead during LLM inference. Existing prompt compression methods typically rely on auxiliary small language models (SLMs) to estimate context importance. However, such approaches introduce significant memory and computational overhead, which limits their deployment on resource-constrained edge devices. In this paper, we propose CORE, a two-stage sentence-level prompt compression method that eliminates the need for SLMs. In the first stage, CORE constructs an answer set via named entity recognition (NER) and a clue set via semantic matching. In the second stage, CORE refines the clue set using an orthogonal residual retrieval strategy and designs a spatial proximity-based metric to filter the answer set. The two sets are then combined to form the final compressed context. We implement CORE on an NVIDIA Jetson AGX Orin edge device and a Huawei Nova smartphone. Experimental results demonstrate that within a 2000-token budget, CORE improves accuracy by at least 30.19% compared to state-of-the-art baselines, while reducing memory usage by at least 50.47% and achieving at least 1.94 times speedup on the edge device. Moreover, compared to the state-of-the-art LLMLingua2 method, CORE achieves a substantial energy reduction of 95.74% on the smartphone, highlighting its practicality and generalizability for mobile deployments.

---


### 2. [Investigating Linguistic Steering: An Analysis of Adjectival Effects Across Large Language Model Architectures](https://arxiv.org/abs/2606.20572)

**<font color=#1a73e8>作者：</font>** Lars Malmqvist  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Achieving reliable control of Large Language Models (LLMs) requires a precise, scalable understanding of how they interpret linguistic cues. We introduce a rigorous framework using Shapley values to quantify the steering effect of individual adjectives on model performance, moving beyond anecdotal heuristics to principled attribution. Applying this method to 100 adjectives across a diverse suite of models (including o3, gpt-4o-mini, phi-3, llama-3-70b, and deepseek-r1) on the MMLU benchmark, we uncover several critical findings for AI alignment. First, we find that a small subset of adjectives act as disproportionately powerful "levers," yet their effects are not universal. Cross-model analysis reveals a "family effect": models of a shared lineage exhibit correlated sensitivity profiles, while architecturally distinct models react in a largely uncorrelated manner, challenging the notion of a one-size-fits-all prompting strategy. Second, focused follow-up studies demonstrate that the steering direction of these powerful adjectives is not intrinsic but is highly contingent on their syntactic role and position within the prompt. For larger models like gpt-4o-mini, we provide the first quantitative evidence of strong, non-additive interaction effects where adjectives can synergistically amplify, antagonistically dampen, or even reverse each other's impact. In contrast, smaller models like phi-3 exhibit a more literal and less compositional response. These results suggest that as models scale, their interpretation of prompts becomes more sophisticated but also less predictable, posing a significant challenge for robustly steering model behavior and highlighting the need for compositional and model-specific alignment techniques.

---


### 3. [Hybrid Intelligence in Cartoon Captioning: Evaluating AI as a Creative Writing Partner](https://arxiv.org/abs/2606.20595)

**<font color=#1a73e8>作者：</font>** Uğur Önal, Sanem Sariel, Metin Sezgin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Crafting cartoon captions requires an understanding of humor, context, and the relationship between image and text. Traditionally, illustrators and writers collaborate to strengthen visual storytelling and comedic timing. With advances in natural language generation, Large Language Models (LLMs) can assist in this process. This study examines AI's role in caption generation by testing GPT-4o via the ChatGPT interface on IEEE Computer magazine cartoons. By removing captions and prompting AI to generate replacements, we assess its ability to produce jokes that match the depicted situation and narrative intent. Our findings show that while AI-generated captions are often humorous and contextually relevant, they sometimes diverge from the cartoon's intended meaning, for example, by missing irony, cultural references, or contextual constraints. However, AI can also produce alternatives that broaden creative exploration and occasionally improve upon the original humor. We argue that current AI systems are best used as an assistant rather than a replacement for human creativity. By integrating AI-generated suggestions, cartoonists can explore diverse humor styles, streamline ideation, and refine final captions while retaining creative control. This study highlights AI's potential as a practical tool for caption ideation within a hybrid human-AI workflow.

---


### 4. [LLM4CAD-Editor: An Intent-Aware Large Language Model Framework for Multi-Level Computer-Aided Design Editing](https://arxiv.org/abs/2606.20607)

**<font color=#1a73e8>作者：</font>** Yuewan Sun, Zhenghui Sha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently enabled automatic generation of parametric computer-aided design (CAD) programs from natural language. However, real-world CAD workflows are inherently iterative and require reliable editing rather than one-shot model synthesis. In this work, we propose LLM4CAD-Editor, an LLM-based intent-aware framework for instruction-guided CAD editing based on a structured domain-specific language (LLM4CAD-DSL). The symbolic representation of LLM4CAD-DSL enables robust geometric modification through a feature-level entity selection mechanism, allowing models to reference geometry via feature names instead of coordinates, thus transforming fragile coordinate-based reasoning into natural language-based reasoning that many LLMs can handle. We construct a multimodal CAD editing dataset with over 35,139 instruction-program pairs via DSL-based augmentation and vision-language instruction synthesis, covering functional-, operation-, and parameter-level editing intents. To validate the work, we fine-tuned a 32B-parameter language model for DSL editing generation. Experimental results show high parsing accuracy for parameter-level edits (96.3%) and strong intent satisfaction rates of 82% for functional instructions. The model also achieves an average Intersection-over-Union (IoU) of 0.935 for parameter-level edits, 0.871 for operation-level edits, and 0.708 for functional-level edits, while the corresponding average editing distances are 0.176, 0.579, and 2.859, respectively. Comparative studies further demonstrate a significant improvement in editing robustness by 1.4x over Python-based CAD scripting approaches. These results confirm that LLM4CAD-Editor can reliably perform both low-level parameter modifications and high-level functional edits, maintaining high accuracy and low structural errors across diverse editing tasks.

---


### 5. [PEAR: Permutation-Equivariant Adaptive Routing Multi-Agent Debate](https://arxiv.org/abs/2606.20621)

**<font color=#1a73e8>作者：</font>** Yang Feng, Ziwei Xu, Xia Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate improves the reliability of large language models (LLMs) through iterative peer critiques. However, fixed topologies often introduce persistent positional biases, amplify unreliable agents, and cause high sensitivity to role assignments. We introduce \textit{Permutation-Equivariant Adaptive Routing Multi-Agent Debate (PEAR)}, an inference-time protocol that dynamically reconfigures communication roles and sparse topologies across consecutive debate rounds. By strategically switching agent-to-role assignments based on evolving agent states, PEAR prevents any agent from permanently occupying a privileged network position or distributes influence more evenly across the debate. We theoretically characterize PEAR as an equivariant sparse router: it preserves accuracy under agent relabeling while reducing routing complexity and improving generalization. Comprehensive empirical evaluations across four reasoning benchmarks and six diverse LLM backbones demonstrate PEAR significantly improves average accuracy over the strongest debate baselines. The code is at this https URL.

---


### 6. [In LLM Reasoning, there is Irrationality on top of Value Misalignment](https://arxiv.org/abs/2606.20624)

**<font color=#1a73e8>作者：</font>** Kejiang Qian, Fengxiang He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Significant progress has been made in aligning LLMs with target value functions. We argue that, even when an LLM has been well aligned in (post-)training, it may still fail to maximise the aligned value in reasoning. We mathematically formalise this gap as rational value risk: the utility discrepancy between a model's deployed reasoning strategy and its rational counterpart, which is defined to be the responses that maximise expected utility in the steepest direction. The estimation error of rational value risk is further decomposed into three components from finite candidates, finite prompts, and imperfect verifiers. Extensive experiments are conducted, covering models Llama-3.1, Qwen-2.5, T{\"}ulu-3 families (7B-72B), GPT-5.2, GPT-5.5, and DeepSeek-V4, and benchmarks UltraFeedback, AlpacaEval, GSM8K, MATH, HumanEval, and MathArena. The results validate that (1) rational value risk is widespread; (2) value alignment can reduce, but cannot eliminate, it; (3) the risk is highly sensitive to inference-time reasoning strategy; and (4) longer reasoning improves rationality with diminishing returns. The code is at this https URL.

---


### 7. [Specialize Roles, Mix Deployments: Pushing the Cost-Accuracy Frontier of LLM Agent Teams](https://arxiv.org/abs/2606.20629)

**<font color=#1a73e8>作者：</font>** Yinsicheng Jiang, Liang Cheng, Yeqi Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed as multi-role teams, where tasks are divided across specialized roles such as planner, executor, and verifier. In these systems, cost and accuracy are no longer properties of a single model: they depend on which model fills each role and where it is hosted, including API, self-hosted, and hybrid deployment. Existing agentic benchmarks typically evaluate fixed models or fixed agent configurations, and therefore offer limited guidance for cost-accuracy-optimal deployment. We introduce AgentCARD, a role-aware benchmark suite for evaluating LLM agent teams across role assignment and deployment mode. AgentCARD combines a role-decomposed evaluation harness, a unified API/self-hosted cost model, Pareto-frontier analysis, and a Shapley-based diagnostic for identifying role bottlenecks. Our evaluation shows that heterogeneous teams consistently occupy the cost-accuracy frontier. They improve accuracy by up to $44\%$ over cost-equivalent homogeneous teams, or match the strongest homogeneous team at up to $12\times$ lower per-task cost through hybrid deployment. We further find that the best role assignment is domain-dependent: some domains are planner-bottlenecked, while others are executor-bottlenecked. Finally, AgentCARD extends beyond planner--executor teams to workflows with additional roles such as verification, and supports continual evaluation as new domains and team structures emerge. Our code is released at: this https URL

---


### 8. [Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents](https://arxiv.org/abs/2606.20631)

**<font color=#1a73e8>作者：</font>** Boming Xia, Liming Zhu, Zhenchang Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills externalise reusable agent-facing behavioural knowledge and guidance as persistent artefacts that can be discovered, activated, and interpreted by LLM agents. Although a skill artefact is static at rest, its architectural responsibilities arise in use, when the artefact is selected for a run, bound to context and authority constraints, interpreted by a stochastic agent, and recorded as run evidence. We call this run-specific relation skill-in-use. This paper studies agent skill harnessing: the architectural responsibilities that govern the transition from skill artefacts to skill-in-use, bound the executable consequences associated with skill-in-use, and capture evidence for attribution, verification, repair, and evolution. This paper provides a catalogue of ten empirically grounded architectural patterns (five core, five supporting) for skill harnessing and synthesises them into a reference architecture with four responsibility layers: Supply Chain, Mediation, Execution Control, and Evidence & Feedback. We evaluate the architecture through cross-instantiation across 8 selected systems. The resulting patterns and reference architecture provide a vocabulary and diagnostic frame for analysing skill-harnessing responsibilities across agent systems.

---


### 9. [Post-Training Recipe, More Than Model Family, Shapes Multi-Agent LLM Conversational Behavior](https://arxiv.org/abs/2606.20632)

**<font color=#1a73e8>作者：</font>** Luyang Zhang, Jialu Wang, Fei Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-LLM systems use multiple language models to deliberate, judge each other's outputs, or coordinate as agents. Their value depends on the models producing measurably different conversational behaviors when given the same input. Prior offline studies recommend drawing one model per family for behavioral diversity, because LLMs prefer outputs from their own family when rating one another in isolation. Whether the same family label predicts behavior in interactive multi-LLM systems, the setting that real deployed systems use, has not been tested. We study this with a 940,000-chain 11-checkpoint corpus and a 1.6M-chain same-base Llama factorial. On our validated headline metric, hedging, a reasoning-distilled Llama checkpoint shifts by 18% depending on which same-base partner it replies to, more than any cross-family hedging gap in the controlled subset. Qwen, closed-API, and runtime checks suggest the pattern is not isolated, while repair and challenge analyses remain exploratory because their surface-cue detectors are weaker. Overall, the results identify post-training recipe as a first-class axis for multi-LLM panel composition and show that model family alone is an incomplete proxy for conversational diversity.

---


### 10. [An LLM-Explainable DRL Framework for Passenger-Directed Autonomous Driving](https://arxiv.org/abs/2606.20640)

**<font color=#1a73e8>作者：</font>** Ouided Braoui, Meriem Bouali, Nadir Farhi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles offer the potential for safer and more efficient mobility, yet public trust remains limited due to the lack of transparency in their decision-making. This work addresses this issue by combining deep reinforcement learning (DRL) for adaptive driving control with large language model (LLM)-based explainability modules designed to communicate agent behavior to passengers. DRL agents were trained in simulation using a Dueling Double Deep Q-Network to follow distinct driving requests: \textit{fast}, \textit{comfort}, and \textit{stop}. They demonstrated stable learning, safe compliance with traffic rules, and reliable switching between modes within a single trip. In parallel, LLM modules were introduced to interpret passenger requests, determine when explanations were needed, and generate concise, safety-oriented justifications. Results show that this framework, serving as a proof of concept for integrating RL decision-making and LLMs, balances safety, adaptability, and explainability, and is most effective when requests are delayed or overridden due to safety constraints.

---


### 11. [A-Evolve-Training: Autonomous Post-Training of a 30B Model](https://arxiv.org/abs/2606.20657)

**<font color=#1a73e8>作者：</font>** Zhan Shi, Bing He, Yisi Sang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training a frontier model is normally weeks of human work: proposing data and recipe changes, launching runs, reading evals, deciding what to keep. We report an autonomous system that runs this loop with no human in the loop, post-training a 30B Nemotron across four rounds over multiple weeks. The autonomously produced model reaches a held-out score of 0.86 against the top human submission's 0.87 on the public NVIDIA Nemotron-Reasoning Challenge leaderboard, placing 8th of ~4000 at the time of writing. More striking than the number: the loop detected that its own dev metric had stopped tracking external performance on the weakest domain -- candidates drove dev to record highs without moving the external target -- and revised its own search policy, no longer maximizing dev but seeking interventions that lowered the now-misleading proxy while improving the external target. We treat this as direct, auditable evidence that a scaled autonomous loop can produce discovery, not only optimization: it detected that its measurement frame had become misleading and changed what counted as evidence. We take the operational view that any system worth the "recursive self-improvement" label must eventually perform end-to-end post-training of a frontier-class model; this is one datapoint of that bar being cleared. We do not claim a "first autonomous match" of human researchers. The claim we make is narrower and auditable: to our knowledge, this is the first publicly reported autonomous post-training run at this scale, where prior public autonomous-ML-research demonstrations sit at GPT-2-class (~124M) budgets. The same system also post-trains the 120B and 550B Nemotron; with no public human baseline there, this shows only that the loop closes at that scale, not that its output is competitive -- infrastructure evidence, with the effectiveness claim deferred until a comparable human anchor exists.

---


### 12. [Skill Coverage: A Test Adequacy Metric for Agent Skills](https://arxiv.org/abs/2606.20659)

**<font color=#1a73e8>作者：</font>** Boyin Tan, Xiaowei Huang, Youcheng Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills encode reusable procedural knowledge that guides large language model agents across tasks and execution contexts. Existing evaluations primarily assess skills through task level outcomes, yet task success alone does not reveal which parts of a skill have been exercised or which remain untested. We introduce skill coverage, a test adequacy metric that treats the skill artifact as the object under test. Our approach extracts observable skill behavior constraints from skill documents and measures whether an agent trajectory provides sufficient evidence to exercise and evaluate each constraint. Skill coverage uses a binary cover or not cover judgment, which reports whether a documented behavior has been exercised with sufficient observable evidence, without assigning an additional outcome label to the behavior. Applying skill coverage to SkillsBench reveals that existing benchmark executions cover only 39.90 to 43.98% of skill behavior constraints, suggesting that current benchmark tasks leave large portions of documented skill guidance untested. These findings show that successful task completion does not imply adequate testing of the skill artifact, highlighting skill coverage as a measure of how thoroughly agent skills are tested.

---


### 13. [From Knowing to Acting: Benchmarking Self-Awareness Capability of LLM Agents](https://arxiv.org/abs/2606.20661)

**<font color=#1a73e8>作者：</font>** Yifan Li, Shengbin Yue, Boyu Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of external tools has transitioned LLM agents from passive responders to autonomous systems. However, current benchmarks prioritize execution success, neglecting self-awareness capability, the ability to discern whether a problem requires necessary external resources or can be solved via internal parametric knowledge. To address this, we introduce KAPRO (Knowing-Acting Quadrant PRObe), a framework that evaluates cognitive-behavioral alignment by decoupling an agent's metacognitive judgment (Knowing) from its spontaneous execution (Acting). We further construct KAware, a dataset rigorously partitioning tasks into external, internal, and hybrid subspaces to systematically probe these epistemic boundaries. Extensive experiments across diverse agent architectures show that self-awareness capability is strongly correlated with task success but degrades sharply in internal-capability settings. Moreover, open-source and instruction-following models exhibit stronger tool overuse due to shallow pattern matching, while proprietary and reasoning-oriented models demonstrate more reliable cognitive gating. Benchmark and codes are available at this https URL.

---


### 14. [A Quantum-Assisted Agentic Distributed Artificial Intelligence Framework for Deadline-Bounded Orchestration of Hybrid Renewable Microgrids](https://arxiv.org/abs/2606.20667)

**<font color=#1a73e8>作者：</font>** Iacovos I. Ioannou, Saher Javaid, Minella Bezha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The real-time orchestration of microgrids that combine fluctuating renewable sources, dispatchable units, storage and curtailable consumers requires the repeated solution of combinatorial dispatch and coalition formation problems under hard control deadlines. In this paper, a quantum-assisted agentic distributed artificial intelligence (DAI) framework is proposed in which the dispatch problem of each control slot is formulated as a quadratic unconstrained binary optimization (QUBO) problem by Belief-Desire-Intention extended (BDIx) agents and is solved by a portfolio of quantum, quantum-inspired and classical solvers. Solver selection is elevated to a first-class agentic deliberation action of the coordinator agent. Learned beliefs about solver latencies are maintained and the solver intention that is expected to satisfy the prevailing deliberation deadline is committed in each slot. In addition, a belief-shaped storage valuation mechanism is introduced through which the storage agent prices its energy at a discounted future-peak value, injecting intertemporal information into the otherwise myopic per-slot optimization. The framework is evaluated on a 24-hour simulation of a grid-connected microgrid with photovoltaic, wind, battery, genset and demand-response assets, with the Quantum Approximate Optimization Algorithm (QAOA) executed by statevector simulation and benchmarked per slot against tabu search, simulated annealing, binary particle swarm optimization, greedy descent and exhaustive enumeration. Zero deliberation deadlines are missed, the committed dispatch attains the exact optimum on every slot and the realized daily cost of 146.24 EUR equals the exact lower bound, with 97.83 percent renewable utilization and zero unserved energy. When the storage valuation mechanism is deactivated, the daily cost is increased to 152.75 EUR, a 4.5 percent increase.

---


### 15. [Towards CSI-Native Foundation Models: A Channel-Adaptive Roadmap for 6G](https://arxiv.org/abs/2606.20670)

**<font color=#1a73e8>作者：</font>** Chenyu Zhang, Xinchen Lyu, Chenshan Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless foundation models offer a path toward reusable channel state information (CSI) intelligence for sixth-generation (6G) systems. However, existing generic-backbone adaptation and CSI pretraining methods often treat CSI as task tensors rather than propagation-conditioned channel responses, thereby failing to capture the intrinsic time-frequency-spatial geometry of wireless environments. This paper presents a channel-adaptive roadmap toward CSI-native foundation models, proposing a unified framework that aligns pretraining, positional modeling, and attention control with three channel requirements: scale-aware heterogeneous exposure, physical time-frequency-antenna coordinates, and correlation-bounded token interaction. Extensive experiments demonstrate the superiority of the proposed framework across three dimensions: zero-shot generalization, reducing NMSE by more than 4 dB across spatial-temporal-frequency tasks; scale extrapolation, yielding up to a 5.4 dB gain under 8 times unseen antenna scaling; and inference efficiency, accelerating mobility-aware processing by up to 18.8%. A system-level evaluation with Sionna SYS further shows that the proposed framework uses only 7.01% of dense-pilot overhead, reaches -18.64 dB average NMSE, and improves average net spectral efficiency by 36.6% over dense LMMSE and 15.5% over WiFo, indicating that CSI-native representation learning can support pilot-efficient radio access.

---


### 16. [NeuroShield: A Device-Agnostic Foundation Model for EEG Authentication](https://arxiv.org/abs/2606.20673)

**<font color=#1a73e8>作者：</font>** Matin Fallahi, Patricia Arias-Cabarcos, Thorsten Strufe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in EEG authentication is that models are typically tied to the acquisition settings in which they are trained. In particular, variations in headset hardware, channel layout, and signal duration create heterogeneous recordings that existing models are not designed to handle, causing each new headset or dataset to be treated as a separate model-development problem. This fragmentation limits multi-dataset learning, hinders knowledge transfer, and reduces model reusability. To address this limitation, we present NeuroShield, a reusable foundation model for EEG authentication that learns identity-discriminative embeddings from variable-channel and variable-length EEG recordings through a dual-stage transformer architecture. We pretrain NeuroShield on three public EEG datasets comprising 15{,}762 subjects and 28{,}116 sessions, and evaluate transfer on two unseen downstream datasets. Our evaluations show that, after fine-tuning, NeuroShield reduces equal error rate by 0.44--8.06 percentage points relative to the state of the art. NeuroShield further generalizes to segments longer than those seen during training and operates across channel layouts not encountered during pretraining. These results establish NeuroShield as a reusable and adaptable EEG identity encoder across heterogeneous recording settings. We release NeuroShield as open source to support reproducibility and community adoption.

---


### 17. [Jury Duty: Calibration and Orientation Failures in MLLM-as-a-Judge Under Cultural Ambiguity](https://arxiv.org/abs/2606.20676)

**<font color=#1a73e8>作者：</font>** Daniel Lee, Harsh Sharma, Eunkyu Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MLLM-as-a-Judge is conventionally validated by agreement with human annotations, but this metric is undefined when the human pool is culturally heterogeneous. We introduce VOIR DIRE, a multimodal benchmark of 626 culturally paired image--prompt artifacts spanning U.S. and mainland Chinese contexts across food, fashion, and architecture, with annotator pools that are within-pool reliable (a = 0.86/0.74) but cross-pool divergent on evaluation (Q1 r = -0.12). Across six MLLMs, the bias decomposes into two failures: a positivity-floor calibration failure (compressed scale use) and an orientation failure (default to one cultural norm). On this corpus, where contested items are sampled to split the two pools, the floor mechanically validates the more-permissive Chinese reading; persona prompting partially recovers calibration, but the orientation residual survives, evidence the tilt is not reducible to scale compression. Reference-pool in-context demonstrations deepen the orientation residual and inflate the high end rather than restoring use of the low end. Model origin adds a small additive tilt (~0.10 MAE) that is approximately invariant under demonstration. We recommend reporting alignment against each reference pool separately and treating cross-pool divergence as a judge property.

---


### 18. [Democratizing and accelerating AI-driven pathology research through agentic intelligence](https://arxiv.org/abs/2606.20677)

**<font color=#1a73e8>作者：</font>** Jiabo Ma, Cheng Jin, Yihui Wang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational pathology has advanced rapidly with the emergence of foundation models, yet widespread adoption remains limited by substantial technical complexity and programming requirements. Here we present PathLab, an autonomous agentic framework that translates natural-language research objectives into executable and validated computational pathology workflows through the structured composition of domain-specific skills and tools. By organizing workflow generation around reusable methodological modules, including data preprocessing, model development, evaluation and interpretation, PathLab enables studies to be specified at the level of scientific intent rather than implementation details. We evaluated PathLab across 12 public datasets spanning four representative task families: region-of-interest classification, whole-slide image classification, segmentation and survival prediction. Across all task categories, PathLab achieved non-inferior performance relative to expert implementations, while consistently enforcing semantic validity of user prompts and proactively rejecting incompatible workflow specifications prior to execution. In controlled user studies, PathLab substantially reduced the time required to generate executable analytical pipelines and enabled domain experts without programming experience to independently design, execute and evaluate computational pathology studies. Together, these results establish PathLab as a reliable interface between biomedical intent and computational execution, enabling computational pathology studies to be designed at the level of scientific questions rather than programming expertise. By lowering technical barriers to advanced AI methodologies, PathLab provides a foundation for the broader democratization of computational pathology.

---


### 19. [Specific Domain Ontology Construction Using Large Language Models](https://arxiv.org/abs/2606.20691)

**<font color=#1a73e8>作者：</font>** Vivian Magri Alcaldi Soares, Renata Wassermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ontologies are useful structures to organize and maintain information that can be understood both by humans and systems. However, since their manual crafting is a laborious task, many specific domains lack reference ontologies. The outstanding ability for understanding natural language demonstrated by the Large Language Models (LLMs) has motivated their application to aid on a variety of fields, including on ontology development. This work presents the experimentation with a technique that uses LLMs in the role of domain experts to build conceptual hierarchies for a given initial concept. Twenty ontologies automatically constructed for the domain of the Brazilian maritime territory (a.k.a the Blue Amazon) using GPT-3.5 and GPT-4 were then evaluated by human experts. The models were able to construct overall coherent conceptualizations of the domain, but none of the outputs was completely satisfactory as a representation of the context without refinement.

---


### 20. [How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks](https://arxiv.org/abs/2606.20695)

**<font color=#1a73e8>作者：</font>** Alibek T Kaliyev, Artem Maryanskyy  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM coordination papers report small benchmark deltas as evidence that one architecture beats another. A prior question: how much paired trial-0 disagreement do two protocols produce on the same model and benchmark when their API inputs are configuration-equivalent (matched by code inspection plus a SHA-256 byte audit), short of full identity-replay? On Claude Haiku 4.5 against tau^2-bench retail, the clean configuration-equivalent contrast (no_coord vs. intercept, both inert at trial 0) gives signed paired gaps of +10pp and 0pp across two n=100 seeds; pooled across both, +5pp with Wilson CI [-2,+12], not significant. The largest single-seed contrast (+18pp pull-vs-intercept, p_corr=0.012) did not reproduce at the second seed (-3pp, p_corr=1.0); no trial-0 contrast is significant after Bonferroni at either seed or pooled. The envelope of observed paired gaps spans [-3,+18]pp across two seeds, with pooled upper Wilson CI ~15pp. Seven of ten recent multi-agent coordination architectures report headline effects below this local floor, and one more sits inside the envelope; whether they survive a same-model paired replication is, by construction, untested in their original settings.
We define coordination-active pass^k, pass^k restricted to trials where the coordination mechanism is logically active, as the minimum reporting protocol, with sample-size targets and runtime hooks in the body. Measurements run on ET-MCP, a task-scoped negative-knowledge store conformant with MCP 2026-07-28, used as a substrate to isolate reader-side choices, not as a contribution. On Haiku 4.5 the candidate readers (pull, intercept) do not improve trial-1 recovery; we give a preliminary diagnosis of failure modes with refinements on existing production hook surfaces.

---


### 21. [MindAlign: Decoding Inner Speech from fMRI Signals via Multimodal Embedding Alignment under Limited Data](https://arxiv.org/abs/2606.20696)

**<font color=#1a73e8>作者：</font>** Muxuan Liu, Ichiro Kobayashi, Satoshi Nishida  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decoding inner speech from non-invasive brain signals remains a fundamental challenge due to the absence of overt linguistic output, limited training data, and large inter-subject variability. Existing brain-to-text approaches often rely on task-specific decoder fine-tuning, which restricts scalability and complicates adaptation to new participants. We propose MindAlign, a decoupled two-stage brain-to-language framework that enables open-ended text generation from fMRI signals without modifying the underlying language model. The first stage learns a subject-specific neural-semantic alignment that maps fMRI activity into a shared multimodal semantic space, extracting a latent semantic sketch of the internally generated sentence. The second stage integrates this sketch with visual context to prompt a frozen multimodal language model for free-form generation. Experiments on fMRI data collected during silent image description demonstrate that the proposed approach consistently outperforms fMRI-only and random baselines. We further show that the learned semantic-to-language projection can generalize across subjects, enabling effective decoding when paired with subject-specific neural alignment. These results indicate that neural signals modulate semantic content beyond image-driven priors, supporting a scalable and modular direction for brain-to-text decoding.

---


### 22. [GEOPHYS: The Geometry of Physical Plausibility](https://arxiv.org/abs/2606.20707)

**<font color=#1a73e8>作者：</font>** Christian Internò, Alexander Pondaven, Habon Issa 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While humans can identify physically implausible events within milliseconds, machine learning approaches addressing the same problem are extremely slow and expensive. They either rely on external multimodal-LLM judges or require ad-hoc modifications to the training procedure. In this work, we argue that indicators of physical plausibility are implicitly captured by five geometric properties of the per-frame embeddings produced by frozen image encoders. In aggregate, we call them GEOPHYS. First, we show that these signals correlate with human EEG responses to two forms of object-permanence violations. Second, GEOPHYS robustly discriminates physically implausible videos from realistic ones, achieving state-of-the-art physics-violation detection: 98.3% on LikePhys and 93.3% on IntPhys2, whereas V-JEPA 2, GPT-4o, Gemini, and twelve modern video diffusion models perform near chance. Third, used as a best-of-N verifier for physical alignment during video generation, GEOPHYS lifts MAGI-1 24B from 50.01% to 64.50% on PhysicsIQ at 1.5x lower wall-clock and 4.65x lower memory than the V-JEPA 2 world-model verifier. Ultimately, GEOPHYS demonstrates that physical plausibility in videos can be assessed by leveraging the emergent geometric properties of temporal features extracted from image encoders.

---


### 23. [Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against Real Purchase Outcomes](https://arxiv.org/abs/2606.20708)

**<font color=#1a73e8>作者：</font>** Liang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-user-simulation has become core infrastructure for conversational AI: agent benchmarks (tau-bench), training pipelines, and a growing body of fidelity studies all rely on LLMs role-playing the human side of dialogue. Existing frameworks measure communicative fidelity -- whether simulators talk like humans -- against ground truth from paid participants role-playing assigned goals. We argue this has a structural blind spot: when the goal is assigned, the user's willingness is exogenous, so no framework can test whether simulators make decisions like real users whose motivation is endogenous, latent, and decaying. We introduce decision fidelity -- whether a simulated population reproduces the decision-state dynamics of real users facing real, consequential choices -- and measure it on a unique testbed: 2,790 production conversations between an LLM sales agent and real customers, including 793 with verified payment outcomes. Using a teacher-forced probe protocol that holds context and instrument fixed, we find a systematic, outcome-correlated failure we call the disengagement deficit: simulators reproduce eventual buyers almost exactly (depth bias +0.09) but inflate eventual non-buyers toward the purchase frame (depth bias +0.40; d=0.38, p<0.001), halving expressed resistance (25.1% to 13.5%) and nearly doubling deliberation (21.9% to 40.1%) while fabricating no purchases. The deficit replicates across model families (DeepSeek: d=0.41, p=0.002) and resists the obvious fix: instructing the simulator that it may disengage cuts marginal bias five-fold but barely moves the outcome-conditioned contrast (d=0.34, p=0.008). Real non-buyers say "not now" and stop; simulated non-buyers ask about price. Evaluating or training sales and persuasion agents against such simulators overstates funnel progress exactly where it matters most -- the customers who walk away.

---


### 24. [TeleStyle V2: Beyond Content-Preserving Style Transfer with Self-Distillation and Distribution-Matching-Distillation](https://arxiv.org/abs/2606.20709)

**<font color=#1a73e8>作者：</font>** Shiwen Zhang, Yifan Xu, Haibin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a content reference and a style reference, content-preserving style transfer requires the model to generate stylized outputs with content and style consistency. We introduced TeleStyle V1 to tackle this problem. However, TeleStyle V1 is trained with photorealistic content reference and artistic style reference, which makes it incapable to cope with artistic content reference and realistic style reference in most cases. In this paper, we designed a Self-Distillation data synthesis strategy to construct such triplets from TeleStyle V1. Trained with such self-distilled triplets, our TeleStyle V2 supports Content-Style references in the forms of Realistic-and-Realistic (RnR), Realistic-and-Stylized (RnS), Stylized-and-Realistic (SnR), Stylized-and-Stylized (SnS). In addition, we found Distribution Matching Distillation could preserve the general text-guided image editing capability of the foundation model and fix the content consistency degradation caused by SFT process. Through quantitative evaluations, our TeleStyleV2-QIE-2509-DMD performs at least on par with Qwen-Image-Edit-2509-DMD, demonstrating strong general image editing skills beyond content-preserving style transfer. We observed the content/style reference order confusion problem in TeleStyle V1 and further introduced prompt enhancer to solve it. TeleStyle V2 uses Qwen-Image-Edit's VLM encoder, Qwen2.5-VL-7B, to generate content prompt and style prompt for free. TeleStyle V2 could achieve comparable style transfer performance with state-of-the-art commercial model, gemini-3-pro-image-preview.

---


### 25. [FairTutor: Equity-Aware Pedagogical LLM Routing for Budget-Constrained AI Tutoring](https://arxiv.org/abs/2606.20713)

**<font color=#1a73e8>作者：</font>** Qingyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI tutors provide real-time, personalized learning support, but also create a new education inequity: students with access to premium AI services may receive clearer explanations, more personalized guidance, and better scaffolding than students limited to free or low-cost services. To address this challenge, we propose FairTutor, an equity-aware model-routing framework that achieves cost-effective AI tutoring via pedagogically motivated multi-agent orchestration. FairTutor combines query analysis, pedagogical planning, low-cost model generation, evaluator-guided critique and revision, and selective escalation to premium AI models. We introduce access-tier AI Education (AIED) Advantage Gap to measure the quality difference between premium-access and budget-constrained tutoring, and TutorAccessEval, a benchmark spanning math, reading, writing, science, and language learning. Empirical evaluations show that FairTutor achieves 97.1% of premium pedagogical quality (in floor-adjusted Likert scale) while reducing serving cost by 71.6%. Sensitivity analysis reveals a tunable cost--quality Pareto frontier, enabling FairTutor to be tailored to the needs of diverse student populations.

---


### 26. [MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents](https://arxiv.org/abs/2606.20717)

**<font color=#1a73e8>作者：</font>** Xuelong Dai, Jianyu Ma, Boyang Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Model (MLLM)-based web agents provide practical, high-precision solutions for visual browser automation; however, they inherently expand the attack surface, introducing novel vision-based vulnerabilities. Existing adversarial evaluations targeting these agents frequently rely on permissive threat models and visually conspicuous artifacts. In this paper, we investigate a constrained vulnerability detection setting: a trusted web platform where the evaluator acts solely as an unprivileged third party, such as a merchant or advertiser, controlling only a semantically legitimate, spatially constrained region, such as an ad slot, a sponsored card, or a localized widget. Operating under these realistic constraints, we propose MIRAGE, a novel visual indirect prompt injection framework for targeted next-action hijacking. Our approach leverages diffusion models to generate perceptually benign adversarial images strictly confined to the attacker-controlled boundaries permitted by the trusted service provider. To maximize attack efficacy within such a restrictive setting, we introduce a robust optimization technique combining curvature-aware adversarial diffusion guidance with sparse, dark-pixel residual perturbations. Comprehensive evaluations against prominent MLLM web agent frameworks, specifically SeeAct and OpenClaw, empirically demonstrate the potency, realism, and stealth of our proposed MIRAGE.

---


### 27. [Empowering Economic Simulation Through Situation-Aware Llm-Driven Generative System](https://arxiv.org/abs/2606.20720)

**<font color=#1a73e8>作者：</font>** Zhimei Chen, Mu Chen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Traditional economic modeling typically follows a TOP-DOWN paradigm, neglecting individual diversity and the complexity of social interactions. To better capture the complexity of societal structure, Agent-Based Modeling (ABM) employs a BOTTOM-UP solution by incorporating micro-level dynamics to generate macroeconomic phenomena. Reinforcement Learning further improves its decision-making ability through tailored reward signals. However, existing ABM systems struggle to generalize beyond predefined scenarios. Recognizing the potential of LLM-driven role-playing in perception and human-like decision-making, we propose SAMAS, which models individual agents with rich macroeconomic understanding embedded in LLMs and economic trajectories experienced in the passing simulation steps. By jointly modeling both macro-level structural patterns and micro-level dynamic behaviors, SAMAS achieves superior performance in volatility realism and turning point prediction.

---


### 28. [Evaluation of Medical Vision Language Models HuluMed and MedGemma, and general purpose chatbots Gemma 3, ChatGPT Plus, and Claude Pro on real previously unseen wound images](https://arxiv.org/abs/2606.20723)

**<font color=#1a73e8>作者：</font>** Yunzhe Xue, Mohammed Saim Ahmed Quadri, Neal Panse 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chronic wound assessment remains a clinically challenging task that requires accurate interpretation of wound morphology, tissue composition, vascular characteristics, and infection risk. Recent advances in Vision-Language Models (VLMs) have introduced the possibility of automated multimodal wound analysis through image understanding combined with clinical reasoning. This study evaluates the performance of several general-purpose and medically specialized open-source and proprietary VLMs for clinical wound assessment using an expanded, curated dataset of 20 clinically diverse wounds spanning vascular, surgical, ischemic, venous, lymphedema, and amputation-related etiologies. Six VLMs were evaluated using a structured twelve-question clinical framework covering wound classification, infection risk, vascular intervention recommendations, debridement urgency, wound therapy selection, and advanced management planning. Across 20 wound cases and 240 clinician-graded wound-analysis decisions, ChatGPT achieved the highest overall performance with 174/240 correct responses (72.50%), followed by Claude with 149/240 (62.08%). Among the open-source and medically specialized models, HuluMed achieved the strongest performance with 96/240 correct responses (40.00%), followed by Gemma 3 (81/240, 33.75%), MedGemma 4B (62/240, 25.83%), and MedGemma 27B (42/240, 17.50%). The findings suggest that frontier general-purpose multimodal systems currently demonstrate substantially stronger wound-analysis performance than medically specialized alternatives, highlighting the continued importance of broad multimodal reasoning capabilities alongside domain-specific medical knowledge. Although current VLMs demonstrate promising potential for clinical decision support, substantial limitations remain in advanced wound-management reasoning, procedural planning, and autonomous clinical reliability.

---


### 29. [An approach with Visual and Tabular Mamba to multimodal medical data using Mixed Fusion](https://arxiv.org/abs/2606.20738)

**<font color=#1a73e8>作者：</font>** Matheus B. Rocha, Gustavo B. Dettogni, Renato A. Krohling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This article presents a complementary approach for integrating multimodal medical data in cancer classification, based on state space models represented by the Mamba architecture. To this end, a mixed multimodal fusion architecture, called Mixed Fusion, was employed and developed to enhance the interpretability of the decision-making process. The proposed approach explores two variants of Mamba: one dedicated to visual processing, responsible for classifying the lesion image and generating probabilities associated with the target classes, and another focused on tabular processing, which uses these probabilities together with clinical and/or sociodemographic data to produce the final diagnosis. The experiments were conducted on two medical datasets: PAD-UFES-20, composed of clinical images and information associated with skin lesions, and NDB-UFES, consisting of histopathological images and sociodemographic data related to oral cancer. The results indicate slightly lower performance in balanced accuracy, compared with Transformer-based approaches, on PAD-UFES-20, and superior performance on NDB-UFES. Additionally, substantial gains were observed in the recall metric. Furthermore, the adoption of the Mixed Fusion architecture enables the application of the Shapley Additive Explanations (SHAP) method, increasing the interpretability of the results. These findings indicate that Mamba-based models constitute a suitable alternative for multimodal classification in medical data, especially in scenarios in which sensitivity is a relevant requirement.

---


### 30. [Mirage: a Clean-Label Backdoor against LiDAR 3D Object Detection](https://arxiv.org/abs/2606.20752)

**<font color=#1a73e8>作者：</font>** Ziba Parsons, Ang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural network-based LiDAR 3D object detection serves as a critical perception component in safety-critical autonomous systems. However, recent studies have revealed its vulnerability to backdoor attacks. Existing attacks typically require white-box access or label modification and focus on geometric attacks such as object disappearance or bounding-box manipulation. In this paper, we present Mirage, a black-box and clean-label backdoor attack against deep neural network-based LiDAR 3DOD. Mirage injects a small number of label-consistent poisoning samples into the training set, causing the model to learn a malicious association between a trigger pattern and an attacker-chosen target class while preserving normal training semantics. As a result, the compromised model behaves normally on benign inputs yet systematically misclassifies triggered objects as the target class during deployment. We evaluate Mirage on multiple state-of-the-art LiDAR 3DOD models and benchmark datasets. Experimental results show that Mirage achieves a 73% misclassification success rate with a poisoning rate of only 0.5%, while maintaining detection performance close to that of benign models.

---


### 31. [Evidential Fusion Network for Multimodal Survival Prediction under Missing Modalities](https://arxiv.org/abs/2606.20757)

**<font color=#1a73e8>作者：</font>** Yucheng Xing, Hailan Mo, Zi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent multimodal survival prediction models have demonstrated strong predictive performance by leveraging complementary information across modalities. However, such models generally assume data completeness and exhibit limited robustness toward missing modalities, which are frequently encountered in real-world clinical settings. We propose the Evidential Missing Modality Survival Fusion (EMMS) model for multimodal survival prediction under missing modalities. EMMS offers a straightforward, computationally effective approach to survival analysis without requiring a generative phase for missing data. By employing Dempster-Shafer theory and Gaussian Random Fuzzy Numbers for multimodal decision fusion, it considers both aleatoric and epistemic uncertainty alongside modality reliability for fusion. Moreover, the model treats missing modalities as vacuous evidence, preventing interference with available inputs and naturally reflecting increased uncertainty and calibrated predictions. Extensive experiments on four cancer datasets demonstrate state-of-the-art performance while providing calibrated and interpretable uncertainty estimates under incomplete multimodal observations, without introducing additional computational overhead.

---


### 32. [Co-Construction Blindness and Asymmetric Epistemic Vulnerability in Human-LLM Interaction](https://arxiv.org/abs/2606.20762)

**<font color=#1a73e8>作者：</font>** Bianca Helena Ximenes  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces two constructs to describe, as far as we know, a previously unnamed risk in human-LLM interaction. Co-construction blindness is the failure to recognize that LLM outputs are not independent assessments to be verified, but co-constructed artifacts shaped by the user's own inputs, accumulated history, and metadata. Every user of a conversational LLM is IN the loop, not ON it -- yet every deployment disclaimer positions them as external auditors. Asymmetric epistemic vulnerability describes the condition in which co-construction blindness produces consequences of radically different magnitude depending on where in the authority structure the user sits. We argue that these constructs describe a structural inevitability, not an anomaly, using the public case of Richard Dawkins's interaction with Claude as a paradigmatic instance. We document a secondary mechanism -- structural deference -- through a first-person exchange in which a large language model concedes that it treated Dawkins more gently than warranted because his intellectual output is represented in its training data. We map the research gaps this analysis opens and call for shared terminology as a precondition for appropriate governance and design response.

---


### 33. [One Image is All You Need: Agentic One-Shot Image Generation via Text-Based World Models for Long-Tail Spatial Perception](https://arxiv.org/abs/2606.20764)

**<font color=#1a73e8>作者：</font>** Keqin Zeng, Shuting Su, Shihao Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable spatial decision automation, such as autonomous driving and maritime surveillance, critically depends on robust visual perception. However, real-world spatiotemporal data exhibits severe heterogeneity, often manifesting as extreme long-tail distributions for safety-critical scenarios. This data scarcity induces dataset shift that degrades detection performance and pose safety risks. While synthetic data generation offers a potential solution, existing generative approaches, such as diffusion models and Generative Adversarial Networks (GANs), often lack explicit spatial grounding and structural constraints, resulting in spatial and physical inconsistencies in generated scenes. To address these challenges, we introduce WMGen-v1, an agentic text-based world model framework for long-tail spatial data generation. WMGen-v1 employs a Large Vision-Language Model (LVLM) to construct a structured scene representation from a single reference image, while a Large Language Model (LLM) performs guidance-based scene expansion under physical plausibility and commonsense constraints. Subsequently, conditioned on the structured semantic representations produced by this reasoning process, a diffusion model generates diverse and physically grounded long-tail training data. Experiments on internal industrial datasets, ROADWork, and LaRS benchmarks demonstrate that WMGen-v1 outperforms baseline approaches. Notably, detectors trained solely on WMGen-v1 synthetic data approach real-only performance on aggregate dataset-level metrics, highlighting its potential to alleviate long-tail data scarcity for downstream spatial perception.

---


### 34. [FirstPass: Grounding AI Scientific Judgment in Multi-Round Editorial Outcomes](https://arxiv.org/abs/2606.20769)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Somnath Luitel, Manmeet Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems for peer review fail on three fronts: they train on Computer Science and Machine Learning venues alone, ignore the iterative dialogue that validates science, and evaluate on stylistic mimicry rather than real editorial judgment. We introduce FirstPass, a dataset and fine-tuned model that addresses all three. Curating 3,668 complete multi-round peer-review dialogues from Nature Communications across five scientific domains (biology, chemistry, neuroscience, physics, and earth science), we exploit mandatory transparent peer review (instituted November 2022) and verify 100% content integrity by automated audit. We fine-tune Qwen2.5-7B-Instruct via Low-Rank Adaptation (LoRA) on three tasks: review generation, reviewer updating, and revision-cycle prediction. Our key finding is that response-only loss masking is a prerequisite, not an optimization: without it, accuracy is 62.0%, below the majority baseline; with it, FirstPass achieves 80.5% accuracy and F1-macro 78.2% on predicting editorial outcomes (Standard vs. Extended revision cycles), outperforming Gemini-3.1-flash-lite-preview zero-shot by 10.4 percentage points and all baselines with statistical significance (McNemar p < 0.001). On generation, FirstPass produces reviews averaging 1,187 words, substantially closer to human references (2,155 words) than any baseline, achieving ROUGE-L 0.154 with significant gains over Qwen and DeepSeek zero-shot (p < 0.001). Deployed in the pre-submission loop as an anticipatory scientific co-author, FirstPass simulates expert critique and predicts revision cycle outcomes before submission, giving authors the judgment a trusted colleague would provide, with consistent cross-domain performance across five disciplines.

---


### 35. [Fara-1.5: Scalable Learning Environments for Computer Use Agents](https://arxiv.org/abs/2606.20785)

**<font color=#1a73e8>作者：</font>** Ahmed Awadallah, Sahil Gupta, Yash Lara 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collecting computer use data from human demonstrations is expensive and slow, motivating the need for scalable generation strategies. This requires two key ingredients: environments in which agents can act and verifiers that can judge whether their demonstrations succeeded. We introduce FaraGen1.5, a scalable data pipeline for computer use agents composed of three modular components: environments, solvers, and verifiers. FaraGen1.5 uses both live websites and synthetic environments that faithfully simulate domains gated by authentication or that require irreversible actions. It employs a solver harness that can be powered by multiple models, including strong frontier models such as GPT-5.4, and also incorporates a user simulator to enable multi-turn rollouts. Finally, FaraGen1.5 scores the resulting trajectories with three complementary verifiers covering task correctness, efficiency, and critical-point adherence. Using data produced by this pipeline, we train Fara1.5, a family of native computer use agents (CUAs) at three scales built on Qwen3.5 (4B, 9B, and 27B). To train these models, we employ a supervised finetuning (SFT) recipe that carefully balances data from FaraGen1.5 for broad coverage, specific high-value tasks, and target model deficiencies in an iterative approach. Each model sets a new state of the art for its size class on browser-use benchmarks: Fara1.5-9B reaches 63.4% on Online-Mind2Web and 86.6% on WebVoyager, while Fara1.5-27B achieves 72.3% on Online-Mind2Web, which is competitive with much larger proprietary systems.

---


### 36. [B[FM]$^2$: Brain Foundation Model via Flow Matching with SplitUNet](https://arxiv.org/abs/2606.20812)

**<font color=#1a73e8>作者：</font>** Jaedong Hwang, Kathleen Zhang, Wei Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models can learn generalizable representations from large-scale EEG corpora to enable single-backbone transfer across diverse clinical and brain-computer interface tasks. Existing models typically discretize the continuous multi-channel EEG waveform into patches or codebook tokens and train a transformer with masked self-supervision. Recognizing that this discretization fragments continuous brain rhythms and obscures fine-grained temporal dynamics, we present B[FM]$^2$(Brain Foundation Model via Flow Matching), whose inductive bias aligns with the data by pretraining directly on the raw signal using continuous-time flow matching without patches, tokenization, or masking. However, multi-channel EEG signals pose an architectural challenge for flow matching: time is densely sampled and highly autocorrelated (thousands of timepoints), while the electrode axis is short (tens of channels) at distinct scalp positions. To address this time-electrode asymmetry, we introduce SplitUNet, a velocity network that factorizes each block into separate 1D temporal and 1D electrode convolutions and downsamples only along time, preserving electrode topology throughout the hierarchy. B[FM]$^2$ sets a new state of the art on 7 of 9 standard downstream EEG classification tasks, using a pretraining budget of only 36,895 segments ($\approx$ 307h), 1-2 orders of magnitude ($\approx$ 30x) less than required by existing EEG foundation models. Further, it generates synthetic EEGs that two board-certified neurologists cannot distinguish from brain data (Cohen's $\kappa =$ -0.096). this https URL

---


### 37. [CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes](https://arxiv.org/abs/2606.20820)

**<font color=#1a73e8>作者：</font>** Zhijian Zhou, Zesheng Ye, Zhaorun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can we trust evaluation scores to capture an LLM's true real-world performance? Certifiable evaluation answers this question by providing guarantee for LLM evaluation. In particular, existing methods sequentially curate evaluation samples and keep updating confidence intervals (CIs) that cover the true performance with high probability (e.g., 95%) until some conditions are satisfied, e.g., the CI width reaches a target precision. However, existing methods are not generally anytime-valid: the claimed coverage (e.g., 95%) may fail when CIs are repeatedly updated and used to decide when to stop, leaving a gap between theoretical rigor and practice. This paper bridges this gap by proposing Celeus, a Certifiable framework for Efficient LLM evaluation, which leverages E-processes to build anytime-valid CIs. Concretely, we propose signals that combine two ingredients: (i) Uncertainty-guided sampling to select informative samples for evaluation, and (ii) Surrogate-assisted approximations for unevaluated samples. We prove that such signals remain unbiased for the evaluation score conditional on the past, enabling statistically-grounded and anytime-valid $e$-process CIs. More importantly, the two ingredients reduce estimation variance and help reach the target precision with fewer evaluated samples. We also prove that CIs obtained by Celeus can shrink at a near-parametric rate up to logarithmic factors and analyze the oracle variance-optimal sampling rule that motivates the empirical uncertainty-guided one. Experiments show that Celeus reaches the target precision using 54-62% fewer evaluated samples than baselines, while preserving anytime-valid coverage.

---


### 38. [Translating Inference-Time Control to Radiology Vision-Language Models: Activation Steering for Pneumonia Classification on Chest X-rays](https://arxiv.org/abs/2606.20852)

**<font color=#1a73e8>作者：</font>** Eduardo Moreno Judice de Mattos Farina, Mateus A. Esmeraldo, Felipe Akio Matsuoka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inference-time engineering can alter model behavior without fine-tuning. However, its utility for improving diagnostic performance in medical vision-language models (VLMs) remains unclear. We aim to evaluate whether Contrastive Activation Addition (CAA) can improve pneumonia classification in chest radiograph VLMs without updating model weights. Three frozen chest radiograph VLMs (MedGemma-4B-IT, NV-Reason-CXR-3B, and CheXOne-3B) were evaluated on the public Kermany pneumonia test set. Classification was based on the logits of the tokens Yes and No under a binary prompt. Steering vectors included a 30-pair answer-bias control, a 30-pair pneumonia text contrast, and an image-conditioned contrast derived from 30 pneumonia and 30 normal development images. A deterministic 200-image development set was used for layer and scale selection (100 images) and threshold calibration (100 images). Performance was assessed using ROC-AUC, PR-AUC, F1 score, threshold analyses, reverse-vector controls, random-vector controls, and conditional bootstrap confidence intervals. Fixed-threshold F1 improvements were frequently observed but did not consistently indicate improved diagnostic performance. For MedGemma-4B-IT. NV-Reason-CXR-3B showed the strongest benefit: calibrated F1 improved from 0.7692 in the zero-shot setting to 0.8619 with pneumonia-text steering and to 0.8727 with image-conditioned steering. For CheXOne-3B, pneumonia-text steering increased calibrated F1 from 0.8528 to 0.8666, although the confidence interval crossed zero. On this public pneumonia benchmark, CAA substantially altered prediction score distributions and operating characteristics without fine-tuning. Meaningful performance gains were observed in one of three evaluated VLMs, suggesting that activation steering may serve as a lightweight approach for adapting medical VLM behavior.

---


### 39. [SciLens: Multi-modal Scientific Claim Verification with Agentic Entailment and Grounding](https://arxiv.org/abs/2606.20873)

**<font color=#1a73e8>作者：</font>** Yueming Wang, Tianshi Zheng, Jiaxin Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery increasingly relies on automated systems that generate hypotheses, inspect multimodal evidence, and validate claims at scale. Yet scientific claim verification is not well served by asking a vision-language model for a direct binary judgment: claims often combine numerical results, comparisons, scope qualifiers, and explanatory context, while evidence is encoded in tables and figures with distinct grounding structures. We present SciLens, an evidence-conditioned atomic entailment framework for multimodal scientific claim verification. SciLens decomposes each claim into central empirical atoms and background atoms, grounds the central atoms to modality-specific evidence witnesses, and predicts the final label with an atom-level entailment rule. For tables, atoms are grounded to rows, columns, cells, arithmetic relations, and table scope; for figures, they are grounded through panels, axes, legends, visual encodings, categories, trends, ranks, and qualifier checks. This yields a unified validation procedure in which a claim is supported only if every central empirical atom is entailed by the current evidence. On the SciClaimEval development set, SciLens achieves 79.2% macro-F1 and 63.1% pair accuracy, showing that structured agentic validation improves both evidence sensitivity and interpretability.

---


### 40. [When Do Intrinsic Rewards Work for Code Reasoning? A Comprehensive Study](https://arxiv.org/abs/2606.20881)

**<font color=#1a73e8>作者：</font>** Xiaolong Jin, Xuandong Zhao, Wenbo Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in large language model reasoning, but relies on ground-truth supervision that is costly or infeasible, especially in coding tasks. Recent work addresses this by deriving rewards from a model's own signals, such as majority voting or confidence-based scores, achieving notable success on mathematical reasoning benchmarks. However, code generation poses distinct challenges: programs are structurally complex, semantically equivalent solutions may differ syntactically, and verification typically requires execution. Whether these intrinsic reward methods transfer effectively to code remains unexplored. In this work, we present a systematic empirical study of intrinsic reward methods for code generation. We conduct extensive experiments on LiveCodeBench, systematically evaluating representative certainty-based Reinforcement Learning from Internal Feedback (RLIF) approaches under different training scenarios and hyperparameter settings. Our experiments reveal that certainty-based methods yield early gains but inevitably collapse: models progressively shorten outputs and lose reasoning capability, with collapse speed sensitive to sample size and temperature. When used to initialize RLVR training, RLIF pre-training offers no significant improvement over training from scratch. We also provide actionable recommendations for using intrinsic rewards for training code reasoning models. Our study shows both the promise and limitations of intrinsic reward methods for code, informing future work on code models and agents.

---


### 41. [Fine-grained Human Motion Understanding with Language Models](https://arxiv.org/abs/2606.20888)

**<font color=#1a73e8>作者：</font>** Thomas Markhorst, Zhi-Yi Lin, Jouh Yeong Chew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose \methodname, an LLM-based model for fine-grained human motion understanding that represents motion as a sequence of skeletal poses with explicit timestamps for each pose. Each pose encodes body joint positions and is temporally grounded with timestamp tokens, allowing the model to reason about motion order, duration, and rhythm. To study what supervision is needed for motion-language reasoning, we construct a diverse training mixture spanning pose captioning, pose question answering, motion captioning, and motion question answering. Our ablations show that the primary gains come from the diversity of pose- and motion-level supervision, while staged training provides a smaller additional benefit. Different from previous works that rely on ground-truth 3D motion capture, our approach supports both 2D and 3D skeletal motion representations through a unified pose encoder, and can optionally incorporate video to provide contextual information. Extensive experiments on BABEL-QA, HuMMan-QA, CompMo, NTU-RGB+D, and QEVD-Coach demonstrate that our method achieves state-of-the-art performance across multiple benchmarks, highlighting the effectiveness of explicit temporal encoding and diverse pose- and motion-level supervision for fine-grained human motion understanding. Notably, even when using only 2D skeletal input, our approach surpasses previous 3D-based methods.

---


### 42. [Topic-to-Timestamp Alignment by Constrained Evidence Selection](https://arxiv.org/abs/2606.20890)

**<font color=#1a73e8>作者：</font>** Zeynep Yılbırt, Marina Litvak, Michael Färber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meeting archives are difficult to search when users remember what was discussed but not when. We study topic-to-timestamp alignment: given a natural-language topic and a timestamped meeting transcript, the goal is to return the time at which the topic is discussed. A standard RAG setup can retrieve relevant transcript excerpts, but still asks the language model to generate a timestamp, which can produce unsupported or invalid timecodes. We therefore recast timestamp prediction as constrained temporal candidate selection: the system retrieves timestamped transcript chunks, and the model selects the candidate that best grounds the topic instead of generating a timecode. On 420 topic-timestamp queries from 200 municipal meeting transcripts, this increases Recall@5 from 31.9% to 50.0%, reduces MAE from 837.0 seconds to 761.0 seconds with Mistral-7B-Instruct, and increases the number of parseable outputs from 373 to 419 of 420 queries. The results suggest that temporal grounding in long transcripts depends strongly on retrieval quality and output design, not only on the choice of the language model.

---


### 43. [Neurosymbolic Clinical Trial Matching via LLM-Driven Abduction and Logical Verification](https://arxiv.org/abs/2606.20895)

**<font color=#1a73e8>作者：</font>** Baiyang Qu, Leonardo Ranaldi, Xi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer a promising path to automate Clinical Trial Matching (CTM), but still struggle with the deterministic verification required for complex eligibility criteria. Conversely, purely symbolic methods provide formal rigour but break down when faced with incomplete patient records and noisy clinical evidence. To bridge this gap, we investigate a hybrid framework for CTM combining LLMs with logical verification. In particular, we introduce an abductive neurosymbolic CTM framework ({\alpha}NeSy-CTM), which leverages the linguistic and world knowledge in LLMs to support reasoning over noisy and underspecified clinical text. Extensive evaluation demonstrates that {\alpha}NeSy-CTM substantially outperforms standalone LLM baselines, achieving up to 30% relative improvement over zero-shot baselines. In addition, our analyses confirm the impact of abductive reasoning on CTM, with {\alpha}NeSy-CTM exhibiting improved accuracy, specificity, and robustness over a non-abductive neurosymbolic setting. Furthermore, {\alpha}NeSy-CTM and Chain-of-Thought (CoT) reasoning prove highly complementary, highlighting the potential for a hybrid routing policy. Ultimately, this paper demonstrates the impact of neurosymbolic methods for automating CTM, providing a path toward the next generation of auditable, LLM-driven clinical applications.

---


### 44. [PeerCheck: Enhancing LLM-Generated Academic Reviews Towards Human-Level Quality](https://arxiv.org/abs/2606.20897)

**<font color=#1a73e8>作者：</font>** Zeyuan Chen, Ziqing Yang, Yihan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As academic submissions grow, the traditional peer review process struggles to keep up, raising concerns about quality and fairness. A trend of using large language models (LLMs) for assistance has emerged. In this work, we take a critical step toward improving the quality of LLM-generated reviews. We propose the PeerCheck framework, which investigates LLM-human review differences (RQ1) and explores methods to improve LLM-generated review quality (RQ2). We first analyzed the human-written reviews with reviews generated by various LLMs and found that LLMs and humans focus on different terms, e.g., LLMs prioritize theory while humans emphasize methodology and experiments. We further adopt prompt engineering, such as Chain-of-Thought (CoT), and utilize retrieval-augmented generation (RAG) to enhance the LLM-generated reviews towards human-level quality. We find CoT significantly improves the quality of LLM reviews, while we discover an unexpected "RAG paradox," i.e., experiments with RAG produce different results for various LLMs and, in some cases, even reduce review quality. Our comprehensive analysis of LLM-generated academic reviews illustrates both possibilities and limitations, contributing to a more effective, human-aligned review system. Our dataset is available on this https URL.

---


### 45. [Latent Personal Memory: Represent personal memory as dynamic soft prompts](https://arxiv.org/abs/2606.20911)

**<font color=#1a73e8>作者：</font>** Debrup Das, Avinash Amballa, Yashas Malur Saidutta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalizing large language models (LLMs) requires encoding long-term, user-specific behavioral patterns in a way that is computationally efficient, scalable, and compatible with a frozen base model. We present Latent Personal Memory (LPM), a scalable framework that represents user-specific history as a compact, persistent matrix of N latent slots, that are interpretable. A shared cross-attention projection network maps these slots into dynamic, input-conditioned soft prompts that are prepended to the input of a frozen LLM. We evaluate LPM on PersonaMem v1 and LoCOMO benchmarks across Qwen3-1.7B, 4B, and 8B backbones. Results demonstrate that LPM outperforms LoRA and Prompt Tuning by up to 8.8% and 54.4% in overall accuracy respectively on PersonaMem v1, while reducing KV-cache usage by over 64x. On LoCoMo, LPM matches LoRA accuracy with 120x fewer trainable parameters. We also show that the efficiency of LPM grows with context length and outperforms full-context at 128K context length.

---


### 46. [GIM-ENDO: A Multimodal Endoscopic Image and Video Dataset for Gastric Intestinal Metaplasia Morphology and Pathology](https://arxiv.org/abs/2606.20919)

**<font color=#1a73e8>作者：</font>** Mojgan Forootan, Mahziar Setayeshfar, Ali Darvishi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gastric intestinal metaplasia (GIM) is a precursor lesion to gastric dysplasia and adenocarcinoma whose early detection is crucial for intervening in the carcinogenesis cascade. Artificial intelligence (AI) holds considerable promise for real-time endoscopic detection and characterization of GIM. However, development of reliable AI models has been constrained by the absence of publicly available, histopathologically validated datasets that combine detailed endoscopic annotations, histological subtype (complete and incomplete), standardized grading systems, and normal mucosal patterns. GIM-ENDO was designed to fill this gap. The dataset comprises demographic data, endoscopic findings, histopathological results, and H. pylori status acquired using the Olympus EVIS X1 system with white-light endoscopy (WLE) and image-enhanced endoscopy (IEE), including narrow-band imaging (NBI) and magnifying NBI (M-NBI), along with images and video clips from 24 patients (22 GIM-positive, 2 normal controls). Annotations cover six primary IEE endoscopic signs -- light blue crest (LBC), marginal turbid band (MTB), white opaque substance (WOS), TV pattern (Fusion), atrophy, and map-like erythema (MLE) -- plus two additional endoscopic findings (AHP and GA) recorded where present. GIM subtypes (complete and incomplete) are annotated for all GIM-positive cases; OLGA and OLGIM staging are provided where complete histological sampling was available. The dataset is publicly accessible at this https URL. For the latest updates and further information regarding this dataset, readers are referred to the DataBioX website: this https URL
A short version of this work has been submitted to MICCAI 2026 Open Data Track.

---


### 47. [Peeking Inside LLMs: Leveraging Internal Artifacts of LLMs for Enhancing Reliability in Legal Classification](https://arxiv.org/abs/2606.20929)

**<font color=#1a73e8>作者：</font>** Sudipta Santra, Debtanu Datta, Saptarshi Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being adopted in the legal domain. However, despite their strong performance, LLMs are prone to generating incorrect or hallucinated outputs, raising serious concerns about their reliability in high-stakes domains such as law. Detecting the correctness of responses of LLM-based systems is therefore a critical challenge. In this work, we explore the potential of leveraging internal artifacts of LLM to detect the correctness of their predictions in legal-domain classification tasks. We develop approaches that utilize features derived from these internal artifacts to build downstream classifiers capable of identifying incorrect LLM outputs. We evaluate our approach on two representative legal classification tasks: bail decision prediction and statute violation prediction. Our experimental results demonstrate that LLMs' internal artifacts are reliable indicators for detecting incorrect predictions in legal classification tasks, and can be applied to enhance the reliability of LLM-based classification systems.

---


### 48. [Towards Robust Training in NNGPT AutoML Pipeline: A Loss-Optimizer Pairing Selection Study](https://arxiv.org/abs/2606.20933)

**<font color=#1a73e8>作者：</font>** Anton Abramochkin, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The choice of loss function and optimizer is an important decision, that shapes further model training. Yet automated architecture search pipelines (AutoML) benefits significantly more from the optimal pairing selection and vice versa. This paper investigates whether a single recipe is sufficient for heterogeneous architecture pools, or whether the optimal pairing varies across structurally diverse models. We conduct a systematic empirical study of all $3 \times 6 = 18$ combinations of six optimizers (SGD+Momentum, Adam, AdamW, RMSprop, Adagrad, Adadelta), paired with three loss functions: Cross-Entropy (CEL), Negative Log-Likelihood (NLL), and the recently introduced genetically evolved NGL loss across the base models presented in LEMUR heterogeneous architecture pool on six image classification datasets (CelebA-Gender, CIFAR-10, CIFAR-100, ImageNette, MNIST, SVHN). The 18 loss-optimizer configurations are applied to each of the 33 compatible base architectures taken from the LEMUR pool, resulting in 594 variants that were generated fully automatically by a source-level injection pipeline and evaluated under fixed hyperparameters, ensuring that observed accuracy differences are attributable solely to the loss-optimizer pairing. Our results confirm that no single pairing is universally optimal. Cross-Entropy with Adam or AdamW is the most robust choice across architecture families and datasets. NGL is a competitive alternative to CEL on standard convolutional classifiers, but only when paired with adaptive optimizers; it degrades substantially with SGD or accumulation-based methods. Adagrad and Adadelta consistently underperform under fixed hyperparameters regardless of loss function, highlighting their sensitivity to learning rate tuning. These findings provide actionable guidance for loss-optimizer selection within NNGPT Framework.

---


### 49. [A Gated Graph Neural Network Approach to Fast-Convergent Dynamic Average Estimation](https://arxiv.org/abs/2606.20955)

**<font color=#1a73e8>作者：</font>** Antonio Marino, Claudio Pacchierotti, Paolo Robuffo Giordano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic average estimation is a critical problem in multi-agent systems, enabling agents to collaboratively estimate time-varying signals using only local information exchange. Traditional model-based approaches often face challenges related to convergence speed and sensitivity to network topology changes. This paper introduces a novel learning-based solution leveraging Gated Graph Neural Networks (GGNNs) for fast-convergent dynamic average estimation in a fully distributed manner. Taking advantage of the inherent structure of GGNNs, the proposed method models the estimation process as a distributed autoregressor, ensuring rapid convergence while maintaining stability. We incorporate a regularization term during training to enforce convergence guarantees and introduce an encoding-decoding mechanism to reduce communication overhead without sacrificing accuracy compared to standard GGNNs. Extensive numerical experiments demonstrate that our approach significantly outperforms conventional model-based estimators in terms of both convergence speed and precision, making it a promising alternative for multi-agent applications that require dynamic average estimation.

---


### 50. [Right Knowledge, Wrong Answer: Test-Time Steering for Temporal Fact Conflicts in Open-Weight Language Models](https://arxiv.org/abs/2606.20959)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Sourav Saha, Umesh Chandra Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can store both outdated facts and newer superseding facts in their parameters, but standard prompting may still elicit the outdated answer. We formalize this problem as Parametric Temporal Conflict (PTC) and introduce Temporal Attractor Steering (TAS), a three-stage test-time intervention that detects likely conflicts, identifies a conflict-critical layer, and steers hidden states toward newer-fact representations without retraining or external retrieval. We construct an 8,746-record verified benchmark across five Wikidata relations and evaluate four open-weight language models from three families: Qwen-2.5-1.5B/7B, Mistral-7B-v0.3, and Llama-3.1-8B. Single-layer activation patching achieves answer-flip rates of 0.72-0.85 across all models. End-to-end TAS resolves 29-57% of PTC cases while preserving 85-99% accuracy on non-conflict queries, outperforming a matched ITI baseline on three of four models. These results show that outdated parametric knowledge can be selectively overridden at inference time.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
