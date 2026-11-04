# 🧠 大模型相关研究 | 2026年11月05日

> 本类共 **220** 篇论文：已确认 **208** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 1. [Alignment Faking Depends on the Value, Not Just the Model](https://arxiv.org/abs/2611.03650)

**<font color=#1a73e8>作者：</font>** Manodeep Ray, Vivek Srivastava, Shirish Karande 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models can follow a directive when they believe they are monitored and abandon it when they believe they are not, a pattern termed Alignment Faking. Prior work establishes this for harmful-content objectives and a handful of moral-foundations values, leaving open how it distributes across a wider value space. We argue it is value-dependent: whether compliance survives a change in perceived oversight is a property of the model--value pairing, not of the model alone. Our framework profiles Alignment Faking per value, scoring each model-value pair under three conditions: bare (no system prompt), unmonitored, and monitored. On 32 ValueBench dimensions across ten open- and closed-weight models (8B-~675B), compliance gaps span 0.05-0.50, with a distilled 70B above a ~675B model. We observe that majority of the structural variance depends on which model was asked about which value and not on the model or value alone. A six-category taxonomy over reasoning traces tracks the behavioural shift: training-signal reasoning dominates under monitoring and value-conflict reasoning dominates when unmonitored. We package per-model results as value cards, extending model cards with behavioral disposition. Code and data are available at this https URL.

---


### 2. [Mixture of Wide Experts: Sparse Routing for Interpretable Native Coordinates](https://arxiv.org/abs/2611.03655)

**<font color=#1a73e8>作者：</font>** Tavish Mankash, Vardhaman Kalloli, Keshava Prasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models often spread a concept across many internal dimensions, making their features difficult to interpret. Sparse autoencoders (SAEs) recover clearer features after training. We ask whether models can instead learn interpretable output coordinates directly. We introduce Mixture of Wide Experts (MoWE), a sparse feed-forward layer in which selected experts read the full representation but write to fixed, disjoint output coordinates. On a controlled task with known hidden causes, this design preserves predictive performance while localizing causes more clearly than dense and standard mixture-of-experts (MoE) models.
At approximately matched compute, we train two 19-layer runs of each architecture for 10 billion tokens. MoWE achieves evaluation cross-entropy 2.417 versus 2.452 for dense, while standard MoE reaches 2.22.
We measure native-coordinate readability by asking a language-model judge to describe each coordinate from passages where it is strongly active and test that description on new passages. Correcting for descriptions that also fit other coordinates gives a specificity score of 0.523 for MoWE, 0.375 for dense, and 0.268 for standard MoE. TopK SAEs trained on the same FFN updates score 0.489 for dense and 0.556 for MoWE, making native MoWE comparable to the dense SAE.
In the first case study, we identify a four-coordinate causal path supporting the model's prediction of degrees after the prompt A right angle is 90. We then copy seven angle-related coordinate values into the model as it processes A rectangle has four, changing its next-token prediction from sides to degrees. In the second, one fixed coordinate set detects hazardous requests and another steers the next token toward refusal. These examples show that MoWE combines sparse conditional computation with coordinates that can be identified and reused directly.

---


### 3. [Stress-Testing the Robustness of LLM-Based Causal Inference](https://arxiv.org/abs/2611.03656)

**<font color=#1a73e8>作者：</font>** Ankitkumar Patel, Jigarkumar Patel, Amit Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why do some of the world's most powerful Artificial Intelligence (AI) systems still struggle to reason about cause and effect? Causal discovery, the ability to discern the underlying drivers of a system, is fundamental to scientific inquiry and has traditionally relied on structured data and statistical methods. Recently, Large Language Models (LLMs) have been explored as an alternative paradigm for causal inference, leveraging their broad knowledge and reasoning capabilities. Yet, despite their linguistic fluency, LLMs often rely on surface-level pattern recognition rather than genuine causal logic. While it is known that LLMs stumble in this domain, we lack a precise map of where, why, and how significantly these failures occur. In this paper, we propose a systematic stress-test framework across six critical dimensions: model scale, causal graph complexity, prompting strategy, metadata quality, data quality, and sensitivity to uncertainty. Our findings reveal a significant "optimism bias" in LLMs; models consistently overestimate causal links, leading to low precision across the board. Furthermore, we demonstrate that traditional evaluation metrics can be deceptive: while reasoning-heavy models lead in performance, the highest scores often occur when uncertainty in inference is overlooked. Once uncertainty is integrated into the evaluation, performance drops, providing a more honest reflection of causal reliability. We also find that, while scaling model size improves outcomes, these gains are fragile; performance degrades sharply as the quality of metadata decreases. This work serves as a practical guide to the blind spots of LLMs, offering a clear-eyed assessment of when these tools can be integrated into a causal discovery pipeline and when they are likely to lead researchers astray.

---


### 4. [MCPGuard: Finding Conformance Gaps in MCP SDKs via Dual-Track Analysis and Dynamic Adjudication](https://arxiv.org/abs/2611.03662)

**<font color=#1a73e8>作者：</font>** Xikai Sun, Kebin Liu, Fan Dang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) connects large language model agents to external tools and services through official SDKs that implement message validation and session logic. Specification constraints omitted by these SDKs may propagate to downstream applications, highlighting the importance of SDK-level conformance testing. Yet existing MCP conformance tools mainly exercise running endpoints and reveal little about whether SDK models enforce specification requirements. We present MCPGuard, an automated LLM-based framework for detecting specification-to-SDK conformance gaps. Its structural track aligns JSON Schema constraints with normalized SDK models and produces constraint-specific evidence. Its behavioral track extracts normative prose rules, retrieves bounded function-level slices, and audits them with LLMs for candidate omissions. An evidence-aware dynamic adjudicator then inspects complete source context and builds PoCs to validate candidates. A shared kernel with language-specific adapters enables analysis across SDKs. On the official Python 1.26.0 and TypeScript 1.29.0 SDKs, MCPGuard confirms 13 and 19 findings, respectively, none of which are exposed by two black-box baselines. Tests on open MCP servers further show that these gaps can systematically propagate downstream. By making SDK conformance of specification constraints directly testable, MCPGuard complements conventional endpoint-oriented conformance suites.

---


### 5. [Functional-Group Knowledge Is Structured in Language Models Before It Is Spoken](https://arxiv.org/abs/2611.03684)

**<font color=#1a73e8>作者：</font>** Tran Nhat Khang Nguyen, Anh Nguyen, Obed Issakah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models serve as the reasoning core of agents for chemistry and materials science, where they must interpret molecular structure before planning syntheses or proposing materials. Yet their outputs show only what they say, not what they know. Given a prompt such as ``The primary functional group in 1-Fluorobutane (CCCCF) is'', a small general-purpose model may answer ``the alkyne group'' instead of an alkyl fluoride. The output alone cannot tell whether the model failed to recognize the fluorine or recognized it and failed to say so. We address this by reading the internal representations of five open-source models on prompts covering 92 molecules and 20 functional groups. Even without chemistry training, the models organize functional groups by chemical family, and they encode chemical differences as consistent directions. The shift from thioether ($\mathrm{R{-}S{-}R'}$) to thiol ($\mathrm{R{-}SH}$), added to ether ($\mathrm{R{-}O{-}R'}$), lands nearest alcohol ($\mathrm{R{-}OH}$). This structure emerges abruptly in the middle layers, where representations shift from tracking the wording of the prompt to tracking the functional group. The base model names the correct functional group in only 58.5\% of prompts, the lowest of the five, yet it encodes functional-group families and preserves chemically meaningful patterns. Its errors are mostly failures to answer rather than wrong answers. Functional-group knowledge is structured in the model before it is spoken. Chemistry fine-tuning reorganizes it, making functional groups rather than prompt wording dominate the representation. These results suggest that evaluating chemical language models through outputs alone can underestimate the chemical information they encode. Representation analysis can distinguish a lack of knowledge from a failure to express it, which matters when choosing or adapting models for chemical agents.

---


### 6. [LOLPlay: Benchmarking Real-Time Visual Agents in League of Legends](https://arxiv.org/abs/2611.03685)

**<font color=#1a73e8>作者：</font>** Zhaojian Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual agents need to coordinate reasoning and action while their environment evolves during inference. We introduce LOLPlay, a benchmark in native \emph{League of Legends} with 36 champion-specific tasks spanning resource management, combat, cooperation, and objectives. Agents interact through screenshots and mouse--keyboard actions; automated initialization and 82 executable subgoal checks distinguish partial progress from completion. Across 324 task evaluations of three models at three reasoning-effort settings, GPT-6 Astra achieves the highest task success rate of 25.0\% at low and medium effort, and the highest subgoal success rate of 40.3\% at medium effort. However, high effort improves neither metric over low effort for any model. For Astra, longer requests leave fewer interaction rounds, suggesting a cost to additional reasoning in real-time control. Trajectories reveal incomplete subgoal composition and actions executing after the observed scene changes, motivating agents that combine visual reasoning with timely action.

---


### 7. [Training LLM Agents to Automate LLM Post-Training with RSI-Dojo](https://arxiv.org/abs/2611.03698)

**<font color=#1a73e8>作者：</font>** Shuzheng Gao, Zhaojian Yu, Penghao Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive Self-Improvement (RSI) aims to enable AI systems to autonomously build and improve AI systems themselves, including models, harnesses, and underlying infrastructure. Within this broader agenda, a central capability is enabling agents to train and improve base models. However, existing studies on automated model training primarily focused on workflow- or harness-level optimizations, rather than internalizing the ability to conduct post-training into the model itself. Developing this capability requires executable model training environments that can produce high-quality trajectories demonstrating how to select data, train models, diagnose failures, and iteratively improve results. In this paper, we introduce RSI-Dojo, a collection of executable model training environments designed to teach LLM agents to conduct post-training. To construct RSI-Dojo, we develop RSI-Craft, an automatic pipeline that converts human research artifacts into executable model training environments. RSI-Craft automatically collects research papers from top venues, instantiates datasets and metrics into a unified interface, and reproduces evaluation dependencies. It then filters tasks by data size, execution reliability, and discriminability, yielding RSI-Dojo with 281 seed model training tasks. Building on RSI-Dojo, we employ a trajectory collection method with an improved harness to collect high-quality model-training trajectories from frontier models, then retain examples through rubric-based and outcome-based filtering. We fine-tune Qwen3.5-9B and Qwen3.6-35B-A3B on these trajectories. The resulting RSI-Dojo-9B and RSI-Dojo-35B-A3B improve over their base models by 8.74 and 16.87 PostTrainBench points, respectively. RSI-Dojo-35B-A3B reaches 29.95 on PostTrainBench and 53.29 on PostTrainBench-Lite, matching the performance of frontier models such as GLM-5.2 and GPT 5.5.

---


### 8. [Unsatz: Evaluating Scientific Discovery Without a Given Ansatz](https://arxiv.org/abs/2611.03713)

**<font color=#1a73e8>作者：</font>** Ethan Ji, Wei Wang, Yizhou Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before a scientist fits any parameter, they must decide what the model contains: which quantities exist, which are hidden, how they interact, and how they are measured. Physicists call such a trial form an ansatz. Benchmarks for automated equation discovery mostly supply it, by fixing the variables, a library of candidate terms, or a law to be modified. We introduce Unsatz, a benchmark in which an LLM agent must construct the ansatz itself. Each task is a simulated system, generated from a private seed as a program in a small modeling language: ordinary, delay, or partial differential equations, discrete maps, static and causal models, or stochastic processes, possibly with hidden states, distorted sensors, and uninformative measurement channels. The agent buys experiments within a budget, writes candidate programs in the same language, obtains their coefficients from the benchmark's fitter, and is scored only on how its final program predicts experiments it never saw: conditions outside the range it could explore, interventions, and longer runs. Across 80 systems in 20 domains, nine language models solve between 21% and 60%. On 44 of these systems, classical equation-discovery methods almost never succeed, although the same data usually suffice once the true equations are given with unknown coefficients; the difficulty lies in finding the structure, not in estimating it. Because mechanisms recur across systems, we also give agents the program they discovered for a related system; it helped only when the new system shared the mechanism and the first investigation had succeeded. Stronger agents make fewer unscientific errors; beyond these, agents find which variables a system has but not how they act, and prefer revisions that lower the training error to revisions that predict better.

---


### 9. [Counterexample-driven autonomous research with application to excess radiated energy in a Z-pinch](https://arxiv.org/abs/2611.03721)

**<font color=#1a73e8>作者：</font>** Bowen Zhu, Jian Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in artificial-intelligence-assisted mathematics show that open-ended machine search can outperform human mathematicians, yet transferring this paradigm to physics requires refactoring the research workflow. We introduce Simjecture, an open-source framework in which language-model agents pursue human-defined physical conjectures. The framework tackles two central challenges in this transfer: first, because physics is empirical and no model is final, it structures inquiry around counterexample-driven falsification and prospective hypothesis repair; second, because physical theories must interact with the real world, it uses computational physics as an executable testbed while separating the qualification of numerical instruments from scientific claim review so solvers and diagnostics can be adapted within a recorded investigation. We apply the framework in an 82.6 h investigation to tackle the long-standing problem of radiated energy exceeding the imploding-shell kinetic energy in a Z-pinch. The investigation reveals competing effects of energy conversion, retention, and release timing. Stronger coherent helical deformation increases resistive conversion while reducing radiation and increasing retained energy. A broader trailing-plasma profile delays the later radiation maximum and recovers much of its early bolometric deficit, with a spectral response that changes during the pulse. These results provide new insight into energy conversion in high-energy-density plasma physics and demonstrate a new paradigm for physics research.

---


### 10. [EMBERS: Empirically Motivated Robustness Testing of Deep Research Systems via Defect-Guided Fuzzing](https://arxiv.org/abs/2611.03723)

**<font color=#1a73e8>作者：</font>** Shuochuan Li, Zan Wang, Dong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research (DR) systems extend large language models into autonomous agents that decompose complex information needs, iteratively search the web, and synthesize evidence to answer challenging questions. However, their multi-stage execution may introduce robustness risks, as variations in user questions or intermediate search inputs may propagate across research stages and lead to incorrect answers. Existing evaluations focus on task-solving capabilities or robustness against external evidence disturbances, leaving intrinsic weaknesses in DR execution insufficiently explored. Thus, we conduct an empirical study of 1,932 execution trajectories from three representative DR systems and identify nine recurring defect categories across subquestion formulation, online search, and final reasoning. Guided by these findings, we propose EMBERS, an empirically motivated, defect-guided fuzzing framework for robustness testing of DR systems. Starting from correctly answered seed questions, EMBERS generates stage-targeted test inputs using defect-guided mutation, web-search-assisted fidelity assurance, and diversity-aware seed maintenance. Experiments across 16 framework--model--dataset settings show that EMBERS achieves 3.21 times the failure-discovery throughput of the strongest baseline under identical testing budgets. Human and LLM-assisted evaluations demonstrate that most generated inputs preserve the original information need and necessary contextual constraints. Moreover, model fine-tuning experiments show consistent-answer performance improvement, highlighting their value for robustness testing and model improvement.

---


### 11. [Does the Trust Boundary Hold over Time? A Long-Horizon Benchmark for Receiver-Directed Federated Learning](https://arxiv.org/abs/2611.03724)

**<font color=#1a73e8>作者：</font>** Ting Xu, Henry Leung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In receiver-directed federated learning, each site draws a trust boundary. For every source and model component it judges, on its own data, whether the transfer helps (admit), harms (reject) or cannot yet be told (abstain). We ask whether this boundary holds over hundreds of rounds. Our benchmark has a federation of thirteen semi-synthetic sites, an exact oracle for every evaluated transfer, paired seeds, an attack protocol, fourteen methods over 600 rounds and Qwen3-1.7B LoRA sites over 500. The answer depends on which boundary is measured. Across 20 paired CPU seeds, a gate judging against a fixed reference better identified transfers useful relative to the site's starting model. Yet it admitted 29% of transfers harmful to the model the site now has. A gate judging against the current model admitted 2% of harmful transfers on that target in the CPU tier, but missed many transfers useful to the starting model. Two short propositions explain these distinct failures. We also evaluate a held out audit that leaves gate verdicts intact. After training, it decides whether each final model is deployed or the site falls back to local training, and reports admissions that have gone stale. With independent audit data its guarantees hold after any training history. At 600 rounds the audit deployed 65 to 72% of models, none with negative benefit on its target, and kept 98% of the gain. No stale report had the wrong sign in our runs. With 20,000 audit observations, a variance-adaptive bound found 99% of stale transfers that cost at least 0.01 in log loss. A common-target Qwen3 comparison on 60 selected transfers shows the same tension over 100 rounds. With 38% adversarial sites, FedFomo and CS-Gate were the only evaluated methods with positive mean gain in every honest group.

---


### 12. [From Logs to Faults: Reference-Free Fault Localization for Retrieval-Augmented Generation Pipelines](https://arxiv.org/abs/2611.03725)

**<font color=#1a73e8>作者：</font>** Hira Naveed, Scott Barnett, Stefanus Kurniawan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) pipelines are widely used for domain-specific question answering, yet locating faults remains manual and time-consuming. Fault localization is challenging because RAG pipelines consist of interdependent stages, where faults can propagate downstream, masking their origin, or remain undetected even when the final answer is correct. Existing evaluation approaches often focus on individual stages and rely on reference answers or code instrumentation. We present RAGLog, which detects and localizes faults across RAG stages using execution logs, without requiring reference answers or code instrumentation. RAGLog transforms heterogeneous API logs into a common RAG schema and combines rule-based, embedding-based, and LLM-based checks to identify faulty stages. We introduce a live fault injector and RAGLog Faults, a dataset of 3,134 runs from five RAG pipelines with stage-level fault labels. With Claude Haiku 5.5, RAGLog achieves a pooled F1 score of 0.73 on runs with naturally occurring faults, outperforming Claude Code (0.58) and Codex (0.52), and comparable effectiveness on runs with injected faults (0.84 versus 0.80 and 0.82, respectively). It analyzes runs in approximately five seconds at US\$0.005 each, with overall lower cost and latency than agent baselines. RAGLog is available as an open-source tool for debugging, evaluating, and monitoring RAG pipelines.

---


### 13. [The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents](https://arxiv.org/abs/2611.03754)

**<font color=#1a73e8>作者：</font>** Geyuan Wang, Shunyu Liu, Siyuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown promise for empowering search agents to tackle complex information-seeking tasks. However, since acquiring external information necessitates web search, these agents are highly susceptible to various adversarial attacks (e.g., malicious information injection or stealthy context manipulation). Existing attack strategies inevitably rely on static and human-crafted templates, failing to emulate the dynamic and complex nature of real-world threats. In this paper, we propose an adversarial self-evolution framework that integrates bi-level optimization between the attacker's strategy evolution and the defender's adaptive mitigation, to expose the vulnerabilities of search agents. Specifically, we introduce the Contrastive Rollout Evolutionary Optimization (CREO) method to drive the directional evolution of the attack strategy population via contrastive evolutionary signals. To provide a stable environment for this continuous evolution, we further construct a controlled sandbox and design fine-grained metrics to quantify internal vulnerabilities. Extensive experiments across various multi-hop QA benchmarks and frontier LLMs demonstrate that the proposed framework yields attack efficacy superior to static baselines, underscoring the urgent need to develop more robust defense frameworks.

---


### 14. [Honest Small Decision Models for Finance: Scale, Specialization Collapse, and Mixed-Corpus Remediation](https://arxiv.org/abs/2611.03755)

**<font color=#1a73e8>作者：</font>** Ajitabh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial workflows need fast, calibrated, auditable decisions, not just generated text. We train System-1 decision models, small language models fine-tuned to answer typed questions (choice/score/noul) with a probability in a single forward pass, across two model families (K2-Horizon and Qwen3.5/3.8) and nine rungs from 0.8B to 32B parameters, using one frozen LoRA recipe on a public decision benchmark and two new finance corpora: a programmatic-gold policy corpus (rule-reading with exact labels) and a reality-labeled outcome corpus (19,640 realized forward-return questions in walk-forward splits, plus a sealed 2026 test of 1,360 questions). Narrow fine-tuning costs general decision competence 9-45 percentage points, a data-mixture effect that shrinks with model scale and is associated with narrow-gradient volume. On reality-labeled questions, every trained rung from 0.8B to 32B lands at the horizon-conditioned prior baseline (accuracy 0.37-0.38, no detectable conditional edge under our controls); the models respond with flat, well-calibrated probabilities that track per-horizon base rates: naturally honest uncertainty, with a mid-scale calibration sweet spot (ECE 0.026 at 2B, degrading to 0.043-0.044 at 9-32B under prior drift). A mixed-corpus remediation carries all competencies in one adapter at modest cost: it matches or slightly exceeds the generalist specialist on the public benchmark while holding the policy ceiling and near-specialist outcome calibration, yielding a deployable artifact with per-domain temperature regimes and a band-dispatch escalation analysis: sharp, dispatchable bands where rules determine answers; flat, review-routing bands where reality does not.

---


### 15. [Language Models Can Benefit from Domain-Specific Inductive Biases](https://arxiv.org/abs/2611.03756)

**<font color=#1a73e8>作者：</font>** Damien Teney, Liangze Jiang, Zachary Shinnick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are typically trained with a single choice of architecture on diverse domains and data sources. Modern transformers have been extensively refined for such general-purpose learning, but are they equally effective across different subsets of the pretraining data? We investigate this question by training small language models from scratch on representative subsets of pretraining data such as web text, code, and mathematics. We introduce variants of transformers in which standard activation functions are replaced with learned splines tuned on specific datasets, providing a simple way to modify their inductive biases. Using a mix-and-match of architectures and datasets, we evaluate cross-domain transfer, i.e. how well does an architecture tuned for one domain perform on data from another? We find that the tuned transformer variants improve training efficiency or generalization on all seven of our tested datasets, but the gains are often domain-specific. For example, architectures tuned on a natural language dataset such as FineWeb perform well on TinyStories, whereas those tuned on mathematics perform poorly on natural language. We identify several mechanisms underlying these improvements, including wider loss basins and more abundant "lottery tickets". Our results show that different subsets of pretraining data can benefit from different learning mechanisms, highlighting a limitation of the prevailing trend towards a small set of general-purpose architectures and optimizers. This points to an opportunity to improve data efficiency by developing domain-specific learning strategies that retain the ability to train general-purpose models.

---


### 16. [JevBreak: Your Model, Their Decision](https://arxiv.org/abs/2611.03759)

**<font color=#1a73e8>作者：</font>** Nitin Aravind Birur, Divyanshu Kumar, Sahil Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Restricting what a model can say is often mistaken for restricting an attacker's influence over its decision. An attacker can add text to the evidence and steer the model toward a wrong answer that still belongs to the allowed set. We evaluate seven decision models spanning hosted APIs, open-weight models and an encoder on 16 tasks in seven domains from Decision Bench, targeting every wrong option across 240 text examples (990 targets per model). We present Slot Attack, a black-box attack designed for decision models that appends text assembled from named components to steer predictions toward an attacker-selected incorrect option. The method relies solely on returned label probabilities, achieves success rates of 32--99\% on initially correct decisions, and identifies the effective component combinations with a median of 17--72 queries per successful attack. Accuracy and confidence do not reliably reveal this vulnerability. Models with near-identical accuracy on the sampled tasks differ by about 20\%age points in attack success. We demonstrate that an attacker can force not just one wrong answer but every available one: on about 20\% of correct decisions for the JEV models, 77\% for gpt-6-luna and 98\% for GLiNER2.5; a confidence threshold does not reliably screen the attack out. A fixed answer set constrains a decision's form, not its source; robustness must be measured per model, per task and per version rather than assumed from output format.

---


### 17. [Quantifying out-of-distribution data severity with Wasserstein distances: benchmarking large language models for alloy property prediction](https://arxiv.org/abs/2611.03767)

**<font color=#1a73e8>作者：</font>** YuJie Liu, Dezhen Xue, Jun Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As general-purpose Large Language Models (LLMs), such as Gemini and DeepSeek, exhibit increasingly advanced reasoning capabilities, a critical question arises: how do their property prediction abilities compare to those of domain-specific pretrained materials models? In this study, we evaluate predictions for Ti, steels, high-entropy alloy (HEA) and Al, demonstrating that general-purpose LLMs surprisingly outperform SteelBERT, MatSciBERT, and SciBERT. To further enhance performance, we introduce a hybrid approach that utilizes numerical priors from a prior model, such as CatBoost or SteelBERT, to guide the general LLMs (Deepseek V3.1, Gemini-2.5-Flash). By inputting these initial estimates from a prior model as prompts, the LLM acts as a reasoning corrector, achieving accuracy superior to the prior model and "unguided mode". Furthermore, we investigate the impact of data strategy using a similarity-based metric, revealing that data quality dominates quantity; using merely 5% of high-similarity reference data of training set as input yields performance similar to the results of using 100% of training set. Additionally, the LLMs demonstrate excellent uncertainty calibration, where self-reported "high" confidence strongly correlates with minimal deviation from ground truth. Our findings suggest that synergizing general-purpose LLMs with prior model numerical baselines and high-quality data curation creates a cost-effective and accurate paradigm for materials discovery, reducing the need for expensive domain-specific pretraining.

---


### 18. [Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention](https://arxiv.org/abs/2611.03768)

**<font color=#1a73e8>作者：</font>** Serdarcan Dilbaz, Arjun Krishna, Kiran Kamble 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention cuts the cost of long-context inference by making the attention matrix sparse: each query attends only a subset of the sequence, chosen by a fixed pattern or, in recent production LLMs, learned per query. In DeepSeek Sparse Attention (DSA), the attention of DeepSeek-V3.2 and the GLM-5 family, every layer is preceded by a lightning indexer that scores the whole cache and keeps the k=2048 highest-scoring tokens for the layer to attend. At long context this indexer scan, not the sparse attention it feeds, is where the decode time goes. But adjacent layers select nearly the same tokens, so a layer can attend the selection of the previous indexer layer instead of its own. This removes the dependency: each indexer then runs concurrently with the attention of its layer. The resulting Multi-layer Indexer (MLI) needs no retraining and no new weights. Its default realization changes no kernel, running inside SGLang's production decode graph; an optional fused decode kernel accelerates it further on DeepSeek-V3.2. MLI composes with IndexCache (the cross-layer reuse GLM-5.2 ships as IndexShare): IndexCache drops the indexer from some layers, and MLI hides the scan on the rest. We serve DeepSeek-V3.2 and GLM-5 under IndexCache's protocol at retentions 1/2 to 1/32 (the fraction of layers that keep an indexer) and contexts 10K to 195K. At equal retention the composition decodes faster than IndexCache: up to 14.5% faster on DeepSeek-V3.2 and 9.8% on GLM-5 at 1/2, and 7.9% and 5.1% at 1/4, largest where IndexCache keeps the most indexers and growing with context. At retention 1/r it is faster still than IndexCache at 1/(2r) while keeping twice the fresh selections: at 128K it reaches 1.32x the unmodified model's decode throughput at 1/4, above IndexCache's 1.28x at 1/8. Its LongBench, RULER and LongBench v2 accuracy stays within a few percentage points of IndexCache's.

---


### 19. [RuntimeTickets: Source-Grounded Security Obligations for Agent Skills](https://arxiv.org/abs/2611.03772)

**<font color=#1a73e8>作者：</font>** Kuiyi Gao, Xue Liu, Bowei He  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's security requirements. We introduce RuntimeTickets, a protocol that enforces and audits these requirements while a Skill runs. From released malicious-Skill datasets we derive a risk model and build adversarial-benign Skill pairs. From the task's delivery contract, a language model proposes security obligations for that task. Each obligation cites the Skill lines it answers, and the ticket tightens the host's approvals into fine-grained allowed actions but never loosens them. A runtime gate checks the recipient, object and amount of every outbound send before forwarding it, and trusted monitors record the effects within their observation scope. The ticket links these checks and observations to the approved obligations of each Skill run, and a deterministic decoder turns the ticket's status into governable data flows and verifies each obligation. Neither enforcement nor decoding involves a language model, so text injected by a Skill can change the proposal but never the rule that decides a send. We evaluate RuntimeTickets at the network egress boundary of three unmodified agent frameworks against production Skill scanners and runtime baselines, among them an AgentBound-derived allow-list and SkillGuard. RuntimeTickets eliminated both failure modes of current Skill defenses, overlook (malicious Skills let through) and overkill (benign Skills blocked): its overlook rate was 0.0% and its overkill rate 0.0%, while the scanners erred on both sides. RuntimeTickets ties approved requirements to verifiable execution evidence and offers a common foundation for the safe and auditable deployment of third-party Skills.

---


### 20. [What Malware Actually Does: An Empirical Analysis of Post-Infection Behavior Across Malware Families](https://arxiv.org/abs/2611.03774)

**<font color=#1a73e8>作者：</font>** Emmanuela Andam, Emanuel S. Grant, Naima Kaabouch  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most malware detection research focuses on identifying whether a file is malicious before it executes. Far less attention goes to what happens after infection. This paper presents an empirical analysis of post-infection malware behavior across 37 families, grounded in dynamic sandbox execution using CAPEv2. Behavioral traces are modeled as heterogeneous graphs with five node types and seven typed edge relationships, preserving relational structure that flat feature vectors discard. A voting ensemble trained on graph-derived structural features achieves 94.44% accuracy and MCC of 0.863, outperforming a flat behavioral baseline by 7.4 percentage points in MCC. A multiclass classifier distinguishes 24 malware families, and a per-family behavioral fingerprint analysis characterizes post-infection activity across registry, network, process, and API dimensions. An LLM explanation layer generates analyst-readable reports with MITRE ATT&CK mappings grounded in observed behavioral evidence. The full pipeline is deployed as HeteroScan at this https URL.

---


### 21. [Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication](https://arxiv.org/abs/2611.03826)

**<font color=#1a73e8>作者：</font>** Heejoon Koo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction. However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, models must handle variable-size diagnosis sets and long-tailed labels; temporally, they must distinguish persistent, newly recorded, and recurrent diagnoses; and both vary with observed history depth. We introduce an evaluation framework along these dimensions and apply it to rule-based heuristics, LLM-based prompting, retrieval, memory, and multi-agent approaches. This reveals that repeating the last visit outperforms most LLM-based approaches overall despite predicting no new or recurrent diagnoses, and that retrieval and memory exhibit distinct profiles whose relative strengths vary across temporal transitions and backbones. Motivated by this, we propose LONGINUS, a retrieval-memory multi-agent adjudication framework combining evidence retrieved from patient records with structured memory of the patient trajectory. Using cross-view agreement as a reliability heuristic, it preserves shared predictions and adjudicates disagreements without revealing their source. Across MIMIC-III and MIMIC-IV with four LLM backbones, LONGINUS achieves the best transition-specific performance among LLM-based methods in nearly all settings while remaining competitive with them on aggregate metrics.

---


### 22. [El Agente Fármaco: A Scalable AI Scientist for Drug Discovery](https://arxiv.org/abs/2611.03832)

**<font color=#1a73e8>作者：</font>** Marcel Müller, Mohammad Ghazi Vakili, Yoshihiro Ogura 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational drug discovery offers a growing range of tools for proposing and evaluating molecules, but combining them and deciding what to do next still requires substantial expert effort. Here, we introduce El Agente Fármaco, an AI scientist that uses modern large language model (LLM) technology to turn discovery goals expressed in everyday language into complex, scalable computational screening workflows. The agentic harness selects scientific tools, reviews their results, and adjusts subsequent steps to the target and the user's objectives. Our approach centers on a shared scientific memory: Fármaco Atlas, which stores molecules, structures, and results together with their provenance -- a record of how they were obtained. The agent uses targeted database queries to retrieve the evidence needed for each decision. A single request can launch calculations for an entire collection of molecules, without requiring a separate LLM decision for every compound. This design limits the information the model must process as screening collections grow, while keeping the underlying results available for inspection and further analysis. The integrated tools support molecule generation, prediction of binding and molecular properties, and searches for compounds available for purchase. In a retrospective comparison with an expert-led campaign, the agent proposed chemically distinct candidates with competitive docking scores and higher calculated drug-likeness under explicitly imposed selection criteria. In a 22-task benchmark against plain tool calls and Codex, the agent achieved the highest observed mean model-judged score, with lower median cumulative token use and peak context. Fármaco provides a foundation for flexible, scalable drug discovery workflows that connect scientific reasoning with an enduring, traceable record of computational work.

---


### 23. [A Conditional Mutual Information Analysis of Response Variety in Language Models](https://arxiv.org/abs/2611.03836)

**<font color=#1a73e8>作者：</font>** R. I. Cukier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models provide a variety of responses at inference (generation) that conventionally depend on a temperature parameter. Using a conditional mutual information approach, a quantitative, entropy based analysis of response variety is given. Three limiting behaviors are defined: arbiter, independent (conditionally) and neutral (deterministic) that span no to maximal mutual information. We give examples of each behavior and suggest their application to: temperature analysis, language analysis, prompt compression, and knowledge graphs.

---


### 24. [Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost](https://arxiv.org/abs/2611.03852)

**<font color=#1a73e8>作者：</font>** Anton Hristov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning substantially improves language models' ability to solve difficult problems, but long reasoning traces make these gains expensive. Efficient reasoning should express useful analysis in fewer tokens by reducing repetition and text that adds little value to solving the problem. Progress in proprietary models motivates this goal, yet their hidden scratchpads limit direct study of how it is achieved. We investigate whether open-weight models can generate less verbose reasoning by changing the form of their own earlier thoughts, without retraining. Our intervention rewrites prior reasoning into compact state records before pending tool results are revealed, then compares continuations from original and compact histories. Across the tested models, accepted compact histories usually shorten future reasoning; a coding case study also shows less repeated verification after a shared candidate solution. In software-agent deployments, compaction can reduce total spending, although task quality and rewrite-inclusive time depend on the target and compressor. These findings identify reasoning history as one way to reduce future reasoning-token use and motivate model-specific compaction policies evaluated for both efficiency and retained capability.

---


### 25. [Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain](https://arxiv.org/abs/2611.03853)

**<font color=#1a73e8>作者：</font>** Daniel Schulz, Pedro Cabral Buchaim, Bernardo Soares 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare information systems are fragmented, and retrieving data from legacy web portals is a recurrent need. Robotic Process Automation (RPA) is deterministic but sensitive to interface changes, whereas autonomous agents based on large language models (Agent Process Automation, APA) promise adaptability at a higher computational cost. Following Design Science Research, we developed and compared an RPA solution (Playwright) and an APA solution (browser-use, LangGraph and Gemini 2.5 Flash-lite) to retrieve mammography and breast ultrasound reports from a laboratory portal, treating reports solely as informational artifacts. Across two rounds (T and T+7), RPA reached 98.90% accuracy and 98.27% F1-score versus 96.49% and 94.48% for APA, was about 13 times faster (16.07 s vs. 207.21 s per patient) and cost about six times less per report (USD 0.030 vs. 0.187). Both reached 100% step success rates; APA varied more over time. For a stable interface, RPA was superior.

---


### 26. [Towards Effective Fuzzing of EDK2 Components](https://arxiv.org/abs/2611.03854)

**<font color=#1a73e8>作者：</font>** Datta Manikanta Sri Hari Danduri, Connor Everett Glosner, Aravind Machiry  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Securing bootloaders is critical to establishing the trusted computing base of modern systems. TianoCore's edk2, the de facto UEFI-based bootloader, is widely deployed but has recently been shown to contain numerous high-severity vulnerabilities. Existing approaches either focus on post-boot interfaces or rely on heavyweight simulation, limiting their scalability, throughput, and coverage of boot-time components.
We present Metis, an automated technique for fuzzing edk2 protocols (i.e., boot-time interfaces) by rehosting them as user-space applications. Our key insight is that effective fuzzing must exercise not only protocol interfaces but also their dependency interactions, which serve as additional input channels. Metis employs a Direct-dependency Component Rehosting (DCR)-based strategy to construct semantically meaningful mocks for dependencies, enabling controlled input injection across all channels. It further leverages a hybrid approach combining static analysis and Large Language Model (LLM)-guided synthesis to generate and refine fuzzing harnesses. We implement Metis on the Host Based Firmware Analyzer (HBFA) framework and evaluate it on 60 drivers covering 162 protocols. Metis achieves 73.1% coverage, approximately 1.7 times higher than FuzzUEr, the state-of-the-art edk2 fuzzing technique, and discovers 137 previously unknown bugs. We have already reported 26 of them, including 12 that are remotely triggerable, and all reported vulnerabilities have been acknowledged by the vendors.

---


### 27. [Dr. No: Feature Steering for Abstention in Vision-Language Models](https://arxiv.org/abs/2611.03862)

**<font color=#1a73e8>作者：</font>** Farid Hasanov, Riccardo Renzulli, Bahram Zonooz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large foundation models often answer even when the available visual or textual evidence is insufficient to support a reliable conclusion. This failure to abstain makes them hard to trust in high-stakes or information-seeking settings, where a confident but unsupported answer can be worse than no answer at all. It also raises a natural question: can the internal mechanisms behind this behaviour be identified and controlled at inference time? We present Dr. No, a feature-steering approach that mines sparse autoencoder (SAE) features associated with abstention and commitment, then modulates a small set of them during the prefill pass, without retraining the base model.
Dr. No is evaluated on LLaVA-1.6 Mistral 7B across multimodal abstention benchmarks, including UNK-VQA and MM-UPD, and additionally benchmarked on language reasoning tasks using Qwen3.5-2B on AbstentionBench subsets. Against multiple uncertainty-based abstention baselines, feature steering achieves a more favourable balance between correct answering and appropriate abstention than post-hoc rejection methods. The gains are strongest on UNK-VQA and on MM-UPD cases involving image--question or question--answer incompatibility, and transfer most clearly to mathematical reasoning subsets of AbstentionBench. However, performance is more limited on absent-answer detection and retrieval-heavy multi-hop QA, such as MuSiQue. These results suggest that sparse internal features provide lightweight control handles for shaping uncertainty-aware behaviour in foundation models, while also showing that abstention control is source-dependent rather than governed by a single universal signal.

---


### 28. [EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts](https://arxiv.org/abs/2611.03868)

**<font color=#1a73e8>作者：</font>** Xinyi Xu, Xiaoyang Li, Yucheng Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration. These agents operate over shared contexts that continuously accumulate through multi-user interactions. However, existing agent memory systems are mainly designed for individual users and struggle to capture group-level knowledge in shared contexts, including group relationships and collaboratively formed knowledge. Manual memory strategies further limit adaptation to diverse and evolving shared contexts. To this end, we propose \textbf{EvoGroup (EvoG)}, a self-evolving harness for group agents that starts from a minimal six-tool cold start and adapts through interaction with shared context. EvoG uses confidence and task outcomes to select informative trajectories, while also eliciting self-reflections on uncertainty in low-confidence cases. The analysis agent then examines selected trajectories through adaptive progressive disclosure, followed by bucketed analysis to synthesize high-level findings that guide the evolve agent in revising the Harness. Empirically, pass@1 on held-out split of EverMemBench improves from 71.07\% to 89.58\%, surpassing both self-evolving memory and human-designed harnesses, including Claude Code (85.83\%). To evaluate generalization, we freeze the evolved harness and evaluate it on the unseen GroupMemBench, where, with GPT-5.5, it demonstrates effective generalization and outperforms both memory baselines and human-designed harnesses.

---


### 29. [Embedding Semantic Entropy: NLI-Free Semantic Uncertainty Estimation with Geometry-Aware Clustering](https://arxiv.org/abs/2611.03876)

**<font color=#1a73e8>作者：</font>** Akshiya Raveendran, Praveenasarma Baskarakurukkal, Pragatheeswaran Vipulanandan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often generate fluent yet incorrect responses, making un- certainty estimation important for reliable deployment. Semantic Entropy (SE) estimates uncertainty by clustering responses based on semantic equivalence, but it relies on hard entailment-based clustering. We propose Embedding Semantic Entropy, which replaces entailment-based clustering with K-Medoids in semantic embedding space and uses dynamic cluster selection to account for intra-cluster compactness and inter-cluster separation. We evaluate the method on TriviaQA, SQuAD, NQ-Open, SVAMP, and BioASQ using Falcon- 7B-Instruct, LLaMA-2-7B, LLaMA-2-7B-Chat, and Gemma-7B. Results show competitive AUROC and AUARC performance, suggesting that NLI-based entailment clustering can be replaced with embedding-space clustering with limited degradation while improving the inspectability of semantic grouping. This matters because semantic uncertainty scores depend on underlying semantic groups; by making these groups explicit, compact, and separable in embedding space, Emb-SE turns uncertainty estimation from a black-box en- tailment decision into an inspectable clustering problem.

---


### 30. [ProofPaths: An AI Agent Framework for Assessing Student Reasoning](https://arxiv.org/abs/2611.03882)

**<font color=#1a73e8>作者：</font>** Mohsen Hariri, Vipin Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Students can use large language models to complete assignments, but a correct solution does not establish whether they understand the reasoning behind it. Individualized interviews can probe that understanding but require recurring staff effort. We introduce ProofPaths, an AI agentic framework that combines rubric-based grading with individualized and interactive interviews. Multiple grading agents assess a submission against instructor guidance, exchange critiques, and revise their judgments. Their scores determine which review supplies the grade and feedback. An interview agent asks students to justify steps in their submission and uses their answers to guide follow-up questions. Each question is linked to a retrieved submission excerpt, so instructors can compare the student's explanation with the cited passage. The system tracks assessment progress and stores grading reviews and interview transcripts for each submission. Several deterministic tests of the assessment controllers check source handling, score aggregation, and limits on correction attempts. Instructors can inspect all reviews and transcripts and override grades within the assignment workflow.

---


### 31. [What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory](https://arxiv.org/abs/2611.03930)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Feng Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A stored experience may answer one future question and offer little help with another. We measure this task-conditioned utility rather than assigning each memory a single importance score. A task-blind writer stores a memory without seeing the later task; a frozen reader then answers that task with and without the memory, using identical filler. A cost ledger records the resources used to form, store and expose the memory.
On single-call factual-recall tasks built from LongMemEval-V2 web-agent memories, the same memory helps more when it contains information needed for the answer. Its mean paired reward gain on these answer-bearing task pairs exceeds that on matched-control pairs by $+0.33$ (95% interval $+0.21$ to $+0.46$). The tested task-blind summaries and structured records yield smaller gains than Raw, including at fixed total context; a budget sweep is consistent with retention of answer-bearing content contributing to the difference. The bearing--control contrast remains positive in a new session with randomized memory position and under a second reader, although individual memory--task labels change. Generic retrieval performs above chance but misses most screen-defined answer-bearing memories. The factual-recall gains do not extend to the tested software-engineering and scientific-coding benchmarks, where even raw memories have no measurable effect. We provide a public, versioned Conditional Memory Utility Dataset of paired measurements and costs. The practical takeaway is to evaluate memory compression by the task utility it preserves alongside its costs. Task-conditioned measurements make this comparison possible; their stability must also be checked.

---


### 32. [Beyond Division of Labor: How Roles Shape Feedback and Recovery in Multi-Agent Systems](https://arxiv.org/abs/2611.03931)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Yang, Xinyang Li, Rajeev Thakur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Roles in multi-agent large language model (LLM) systems allocate decisions as well as work. In a Planner--Executor--Reviewer team, the Reviewer's approval can determine when the team submits an answer and receives corrective feedback. We study both functions by varying role instructions while holding agents, topology, call budget, and ground-truth evaluator constant, using three open-weight models on Omni-MATH and two on SciBench. Removing roles largely eliminates functional specialization without lowering first-pass accuracy. After a failed first answer, however, submission decisions matter: a role-structured Reviewer often withholds approval, so its team submits less often and receives fewer evaluator verdicts. In an exploratory comparison with feedback available to both teams, the role-free team recovers more often across all five model--benchmark settings. Two further analyses support the importance of feedback opportunities. In a post hoc comparison at equal numbers of verdicts, the pooled recovery difference is small (role-structured minus role-free: $+0.009$, 95% interval $[-0.014,+0.033]$). In an exploratory intervention on $400$ Omni-MATH problems with gemma-4, keeping the role prompts but forcing submission in every cycle raises recovery from $0.198$ to $0.613$; the paired comparison detects no difference from the role-free team. The takeaway is to evaluate roles through recovery after failure as well as specialization. For systems with reliable external feedback, this requires measuring who may submit, how often the team receives feedback, and which agents can act on it.

---


### 33. [FlowBench: Counterfactual Imagination Training for Spatial Intelligence](https://arxiv.org/abs/2611.03937)

**<font color=#1a73e8>作者：</font>** Yifan Liu, Baihan Zhang, Khai Loong Aw 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning. However, this capability remains underexplored in vision-language models and world models. We formalize this capability as Counterfactual Spatial Imagination (CSI) and introduce FlowBench, a resource for training and evaluating both, with 428K training examples spanning simulated and real-world scenes, household environments and tabletop manipulation, and diverse question types. A scalable, fully automatic pipeline pairs each hypothetical motion with spatial questions and, in simulation, exact outcome frames and optical flow. For VLMs, proprietary models exhibit an imagination gap, performing worse when motion outcomes must be inferred than when observed, and open-source models perform near chance; fine-tuning Qwen3-VL-8B on FlowBench-Sim-Train raises its accuracy by 29.5 percentage points in simulation and 16.9 on real images, a strong sim-to-real transfer. For world models, training on FlowBench-Sim improves text-to-flow prediction for all four model families we test, raising the accuracy of Psi-0.6 from 52.1% to 61.7%. FlowBench thus serves as a training and evaluation resource for both. Code and datasets are released at this https URL.

---


### 34. [From Benchmarks to Behaviors: A Framework for Auditing AI Agents](https://arxiv.org/abs/2611.03939)

**<font color=#1a73e8>作者：</font>** Nick Hagar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems increasingly mediate access to information. Their behavior depends on tools, instructions, and user memories that are often difficult for researchers to observe or control. Here, I introduce TRACE (Transparent Research on Agent Contexts and Environments), a framework for systematically auditing how these components shape AI agent behavior. Built on an open-source agent harness, TRACE enables controlled manipulation of system components. It also records inputs, outputs, and task execution for downstream analysis. I demonstrate this framework through an experiment examining how user memories influence source selection when agents answer questions about the 2026 U.S. midterm elections. I find that memories expressing explicit preference for a publisher increase its inclusion among the first three cited sources in a response by 33-39 percentage points. Memories identifying the user as a Republican or expressing distrust of mainstream media shift citations rightward. That same media distrust memory also increases citation of sources expressing misinformation or conspiracy theories by 6.3 percentage points, with substantial variation across models. These findings demonstrate that concise user memories can alter source selection in consequential settings, even when questions and search results remain fixed. TRACE extends algorithm auditing to agent harnesses, providing a transparent way to study agent behaviors that benchmarks or commercial interfaces may struggle to isolate.

---


### 35. [We Ran a Research Sprint With AI. The AI Worked. The Research Didn't](https://arxiv.org/abs/2611.03946)

**<font color=#1a73e8>作者：</font>** Anush Sankaran, Arijit Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI tools for research are widely deployed, yet individual productivity gains do not guarantee better team research. We argue that how AI use is structured matters alongside access. Personal AI tools may amplify two failures under deadline pressure: a consumption bottleneck, in which generation outpaces team-visible evaluation, and AI-induced research silos, in which private human-AI loops displace shared decision-making. We motivate this position with a mechanism-generating pilot: a 100-minute research sprint with twelve researchers in three independently operating teams, within a seventeen-person session. Both patterns recurred across teams and evidence sources. Of 33 logged AI interactions, one was accepted outright and 27 lacked a recorded disposition; missing records alone do not establish absent evaluation. A parallel autonomous pipeline produced a complete draft without in-session human evaluation, illustrating production capacity rather than comparative quality. We propose Human-AI-Human collaboration: an interaction topology in which AI connects researchers' contexts and supports inspectable collective evaluation and decision-making. The pilot does not isolate AI-specific effects from time pressure or workflow practices. We close with seven modular, falsifiable design hypotheses, prioritizing shared context and team-visible evaluation checkpoints for controlled follow-up.

---


### 36. [Balancing Chain-of-Thought and Answer Supervision for Small Language Models on Medical Question Answering](https://arxiv.org/abs/2611.03948)

**<font color=#1a73e8>作者：</font>** Le Zhou, Xiao Luo, Chinmay Chandra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (<=9B parameters) can support local medical question answering (QA) while reducing privacy and latency concerns, but effective fine-tuning remains challenging. This paper compares two chain-of-thought (CoT) supervised fine-tuning methods: Uniform-across-Sequence (UaS), which applies equal loss weighting to the full CoT-and-answer sequence, and Segment-weighted (SwS), which separately weights CoT and answer losses. We evaluate six general- and medical-domain models on multiple-choice QA (MedQA and EMS-MCQA) and free-text QA (Med-O1). Results show that neither method is universally best: on multiple-choice QA (MedQA and EMS-MCQA), SwS generally performs better, with general-purpose models benefiting most; notably, Qwen3.5-4B improves by up to 44.8% over its zero-shot baseline on MedQA. In contrast, medical-domain models show smaller or even negative gains on MCQs. On free-text QA (Med-O1), UaS performs best for nearly all models and provides consistent improvements across both model types, with the 3B Llama-3.2 model approaching the performance of much larger 7B medical-domain models. We also find that excessively long CoT generation is associated with lower performance in some models on either multiple-choice or free-text QA tasks, suggesting that limiting the CoT length during training may benefit selected models. Overall, the results show that CoT loss weighting should be matched to the task format and the knowledge already encoded in the base model, rather than using a single fine-tuning strategy for all clinical QA tasks.

---


### 37. [P$^2$-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors](https://arxiv.org/abs/2611.03953)

**<font color=#1a73e8>作者：</font>** Sinuo Wang, Jiacheng Lu, Zeyu Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation consolidates expert capabilities by supervising student-generated trajectories, whereas task arithmetic offers a training-free alternative through linear parameter combinations. We view the linear combination of student and expert parameters as a single differentiable model and propose P$^2$-MOPD, which jointly optimizes the mixing coefficients and the student weights under the same on-policy distillation objective. Unlike task arithmetic, which stays within the span of the frozen student and expert parameters for any choice of merging coefficients, P$^2$-MOPD keeps the student trainable, so the experts act as parameter priors without confining it to this span. Across four domains at 1.7B and 4B scales, P$^2$-MOPD achieves faster and more balanced recovery than MOPD from the same initialization, surpassing its final average recovery in half the training steps. At the end of training, our 1.7B model reaches 94.7% average recovery, versus 80.9% for MOPD.

---


### 38. [Forget What Comes Next: LLM Unlearning via Statistical Independence](https://arxiv.org/abs/2611.03955)

**<font color=#1a73e8>作者：</font>** Andrii Shkabrii, Claudia Plant, Martin Pawelczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can memorize and reproduce fragments of their training data, raising privacy and legal concerns that motivate machine unlearning. Yet poisoned training examples can remain statistically detectable after unlearning, which raises the question of whether current unlearning objectives remove what the model has memorized at all. In this work, we introduce PINT, a novel algorithm for machine unlearning that uses the Hilbert-Schmidt Independence Criterion (HSIC) to reduce the statistical dependence between tokens to be forgotten and the internal representations used to predict them. We formally relate our HSIC-based objective to Exact Memorization through a computable upper bound, connecting the training objective directly to the model's ability to reproduce the forgotten tokens. In extensive experiments, we compare forgetting-utility trade-offs across eight settings with models up to 7B parameters and demonstrate scalability to 70B parameter models. Our evaluations cover unlearning Gaussian poisons, personal information, hazardous knowledge in biology and cybersecurity, and copyrighted books and news articles. PINT achieves the strongest forgetting-utility trade-off on average and is the only method to make Gaussian poisons undetectable while maintaining near-original model utility. Code is available at: this https URL

---


### 39. [Stacking-Based Weighting for Large Language Bayes in M-Open Settings](https://arxiv.org/abs/2611.03966)

**<font color=#1a73e8>作者：</font>** Anant Bhide, Akarsh Gupta, Edmond Cunningham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Bayes (LLB) transforms a natural language problem description into a collection of candidate probabilistic programs and performs inference within each model, combining their predictions using Bayesian model averaging. While this provides a flexible framework for probabilistic inference without manual model specification, the resulting candidate model set is often misspecified in practice, and likelihood-based aggregation can concentrate on a single model, under-representing uncertainty across the sampled models. We propose a stacking-based aggregation method for LLB that selects model weights by optimizing predictive performance rather than marginal likelihood, while preserving the original language-model-driven model generation and within-model inference pipeline. Because leave-one-out predictive quantities are intractable in latent-variable models, we derive a variational lower bound that yields a tractable ELBO-based stacking objective. Across real-world probabilistic inference tasks, our method achieves comparable predictive performance to Bayesian model averaging while yielding more dispersed model weights, reducing concentration on a single candidate model under misspecification.

---


### 40. [Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics](https://arxiv.org/abs/2611.03980)

**<font color=#1a73e8>作者：</font>** Nataša Djurdjevac Conrad, Sebastian Pokutta, Christof Schütte  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used as synthetic participants in opinion-dynamics experiments, often assuming that an agent's behaviour is fully determined by its prompt. We test this assumption with a framework in which LLM agents discuss a contested policy issue over repeated rounds while their stance is quantified by a fixed psychometric instrument independent of any dynamics model. Across six LLMs, committed personas are intrinsically stable: in each of the five models tested without peer input, every agent keeps its assigned side for 20 rounds. The observed loss of alignment under discussion is therefore interaction-induced, we call it alignment drift, and model-specific: gpt-4.1 keeps opinion clusters apart, claude-sonnet-5 holds them partially, and gpt-5.6-sol and claude-opus-5 abandon them. Under selective attention, one LLM maintains separated opinion clusters under stance-homophilous attention. Qualitative profiles persist at doubled population and horizon and on a second issue. Such heterogeneity makes the LLM choice a first-class validity variable for social simulation.

---


### 41. [SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use](https://arxiv.org/abs/2611.03982)

**<font color=#1a73e8>作者：</font>** Rongzhe Wei, Ge Shi, Min Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprises increasingly want LLM agents to automate standard operating procedures over their software stacks -- mapping each step of a procedure to the right call among thousands of internal APIs, without hand-authored step-to-API mappings. The core difficulty is API selection at scale: choosing and composing the correct tools over a long horizon, judged only by whether the overall task succeeds. Current tool-use benchmarks do not test this regime -- they expose only a handful of tools, evaluate single-step invocation, or grade multi-step behavior with subjective LLM-as-a-judge scores that penalize valid alternative trajectories. We introduce SLATE (Synthetic Large-scale API Toolkit for E-commerce), a large-scale benchmark that tests large-toolset, long-horizon API selection in a realistic enterprise domain. SLATE couples (i) queries decomposed into hierarchical, tool-grounded procedures over a ~1,000-tool e-commerce library, (ii) a deterministic, context-aware simulator that returns recorded outputs for matching calls and default responses otherwise, and (iii) an end-to-end task-success metric -- a task succeeds when it reaches every reference outcome -- that credits diverse-but-valid trajectories while remaining fully automatic and reproducible. Experiments with six open decision models and the language models they are built on, from 3B to 12B parameters, show that even the best model completes only 5.0% of the tasks, establishing SLATE as a challenging testbed for reliable enterprise tool use. We release SLATE, its simulator, and the evaluation harness at this https URL

---


### 42. [A Guideline-Grounded Multi-Agent Framework for Personalized Exercise Prescription from Clinical and Wearable Data](https://arxiv.org/abs/2611.03983)

**<font color=#1a73e8>作者：</font>** Xintong Li, Yufen Lin, Yuhua Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Translating population-level exercise guidance into individualized prescriptions requires integrating clinical and wearable data, including diagnoses, medications, functional limitations, and baseline activity, with condition-specific recommendations, a process difficult to scale beyond specialist rehabilitation settings. We developed FITTER, a multi-agent framework that integrates these data with condition-specific guidance to generate personalized FITT-VP prescriptions and applies deterministic safety audit and repair to correct rule-checkable violations. We evaluated FITTER using data from 400 All of Us participants (300 cancer, 100 stroke) against five LLM comparators through computational evaluation, ablation, and structured clinician review. FITTER achieved 98.5% safety-constraint compliance versus 75.8-85.8% for comparators and showed greater quantitative dosing precision and guideline alignment. Cancer-cohort ablation identified safety audit and repair as the largest contributor to safety-constraint compliance. Clinicians reviewed 80 prescriptions across safety, personalization, instruction concreteness, anticipated effectiveness, and clinical acceptability. FITTER provides a clinician-facing approach integrating clinical and wearable data, guidance, and explicit safety constraints.

---


### 43. [Thinking Fast, Trading Late: System One Decision Models vs the Market](https://arxiv.org/abs/2611.03985)

**<font color=#1a73e8>作者：</font>** Amir Dehkordi, Alireza Kargarzadeh, Nariman Khaledian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) read company news at scale, and backtests suggest that their readings predict stock returns. We ask how much of that predictability survives a test that rules out look-ahead, memorization and selection. We propose OLIVIA, a protocol for such tests: point-in-time inputs with company identities masked, selection on validation data only, an analysis plan frozen by cryptographic hash, and a test period unblinded once through a logged lock. We apply it to AI decision models, non-generative language models that return probabilities for typed questions, reading news about S&P 500 stocks: an open-weights model we fine-tuned on 2024-2025 data, three commercial models and standard baselines. The fine-tuned model's signal replicated on two validation quarters (daily information coefficients 0.055 and 0.065) but fell to 0.020 (t = 1.7) on the blinded January-July 2026 test. The commercial models' readings line up with the overnight move to the open (information coefficient 0.074 to 0.077) but not with the move after it, so the news is priced by the time a trader can act on it at the open. No model can tell over- from under-reaction, and no pre-registered strategy survives costs and a deflated Sharpe ratio. Commercial models identify masked companies in 62% to 74% of cases against a 28% baseline: masking hides names, not companies. The market reads the news first.

---


### 44. [FlagRot: Selective Rotation for Low-Bit KV Caches](https://arxiv.org/abs/2611.03992)

**<font color=#1a73e8>作者：</font>** Kunming Shao, Xijie Huang, Jierun Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference is bound by the KV cache, which 2-bit codes could shrink about sixfold if their error stays in check. The usual remedy rotates keys before quantizing, assuming rotation always helps. However, we observe that it does not: rotation flattens a spiky piece of a key but can give a flat one a new peak, and both coexist within one key. We therefore propose FlagRot, which stores each 32-channel piece rotated or as is, whichever has the smaller calibrated attention error, and rotates the query instead when reading. We further show that how often to decide follows the quantization axis: per-channel caches such as KIVI need one decision per head, at no write cost, while per-token caches decide per key, with the choice stored in existing sign bits. At 2.5 bits per value, FlagRot lowers the twelve-model KL divergence of KIVI from 18.7 to 12.4 x 10^-3, below RotateKV on 9 of 12 models. Served as a vLLM plugin, it raises RULER at 128k tokens by +2.9 points and the LongBench v1 mean by +0.4 to +1.9 points on the three of four models where 2-bit KIVI loses accuracy. It also lowers the error of 4-bit integer and FP4 caches.

---


### 45. [Whose startup does the AI back? An algorithm audit of reputation and demographic signals in LLM-assisted crowdfunding](https://arxiv.org/abs/2611.03993)

**<font color=#1a73e8>作者：</font>** Mirza Samad Ahmed Baig, Syeda Anshrah Gillani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants increasingly advise backers on which crowdfunding campaigns to support. LLMs have known race and gender problems, and it is unsettled whether they reproduce, erase, or reverse the discrimination documented in entrepreneurial finance. We ask when, and through which decision process, LLM assistants use founders' gender and ethnicity. In a pre-specified choice-based conjoint experiment, seven LLMs chose among five synthetic campaigns with independently randomized quality signals and founder names, under three backer personas and a persona-free control (40,248 responses). By default, founder names barely matter: under budget-conscious and delivery-focused personas, gender and Black-name effects are statistically equivalent to zero. When the backer wants to support underrepresented creators, the models favor Black-signaled (+8.1 percentage points; positive in all seven models) and female-signaled (+5.1) founders. They do so most strongly among near-tied campaigns and for the founder who alone carries the signal, and they almost never name gender or ethnicity in their reasons. The results fit an agency account of algorithmic discrimination: an aligned assistant takes its demographic preferences from its user rather than from its training data.

---


### 46. [Dory1.0-4B: A Looped Normalized-GPT](https://arxiv.org/abs/2611.03998)

**<font color=#1a73e8>作者：</font>** Maxim Fishman, Simeng Sun, Shantanu Acharya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets. Dory1.0-4B is built on a normalized Transformer (nGPT) backbone with interleaved sliding-window and full-attention layers, organized into an input block, a shared recurrent block, and an output block. At inference, the recurrent block can be applied a variable number of times. We pre-trained Dory1.0-4B on 6 trillion tokens. The first 4.5 trillion tokens were trained in NVFP4, and additional pre-training then extended the context length to 256K tokens. Next, we post-trained the model using Supervised Fine-Tuning (SFT) and Reinforcement Learning with Verifiable Rewards (RLVR), with a difficulty-aware loop curriculum that routes harder prompts to deeper loops. Increasing the loop count improves accuracy, with the largest gains on coding, agentic, and long-context benchmarks. With two or more loops, Dory1.0-4B outperforms larger models such as Qwen3.5-9B, Gemma 4 12B, and Gemma 4 26B-A4B on average across 12 benchmarks. Looping also makes Dory1.0-4B more token-efficient on agentic benchmarks: with four loops, it generates 1.3-2.5x fewer tokens than with one loop, as the extra computation is spent in latent space rather than on longer outputs. To reduce memory during looping, Dory1.0-4B caches keys and values only from the last loop, keeping its KV-cache footprint equal to that of a non-looped model at any loop count while retaining most of the accuracy gains. We open-source the BF16, MXFP8, NVFP4, and GGUF quantized checkpoints.

---


### 47. [WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis](https://arxiv.org/abs/2611.04003)

**<font color=#1a73e8>作者：</font>** Peizhi Niu, Ge Shi, Vaibhav Gorde 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents struggle to automate complex enterprise procedures because static, pre-built harness cannot capture proprietary policies, undocumented behaviors, or state-dependent recovery paths that surface only during execution. Procedural memory accrued from agent experience offers a training-free path to closing this gap -- yet unlike episodic records or semantic facts, it must consolidate repeated successes and diagnosed failures into reusable actions and recovery strategies. We introduce WASP-Mem (Wiki-based Agent-Synthesized Procedural Memory), a nimble but effective method that distills execution traces and feedback into persistent, interlinked wiki pages, enabling continual agent learning. On TheAgentCompany benchmark, WASP-Mem raises the checkpoint pass rate by 4.6-6.1% over the strongest baseline we compared across three models while requiring 57-61% less storage. We further present a systematic controlled study spanning consolidation method, feedback type, trace ingestion scope, and refinement rounds. Our results reveal that prescriptive knowledge organization such as human defined schemas and explicit deduplication rules hurts performance rather than closing the procedural-knowledge gap. In contrast, human diagnosis converts failed traces into corrective knowledge and drives sustained improvement: a single round of human diagnosis outperforms four rounds of self-judgment by 7.0-10.9%. These findings point to a simple division of labor: let agents organize procedural memory, and invest human effort where it matters most -- diagnosis.

---


### 48. [Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy](https://arxiv.org/abs/2611.04006)

**<font color=#1a73e8>作者：</font>** Ruijie Zhang, Jiayin Zheng, Yequan Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern learning systems increasingly combine pretrained models with downstream heads. Despite the growing importance of such modular designs, how the downstream model co-adapts to the geometry of pretrained representations remains relatively underexplored. We study this problem through vision-language-action models (VLAs), where a pretrained vision-language model (VLM) conditions an action model for control. We find that the action model progressively concentrates its sensitivity on high-variance dimensions of the VLM outputs. Through controlled experiments across different backbone-head models, we further show that counteracting this sensitivity concentration can be beneficial under representation--task mismatch settings. Motivated by these observations, we introduce \emph{Adaptive Interface Equalizer} (AdaIE), a parameter-free mechanism that reweights pretrained representations according to the evolving downstream sensitivity during training. AdaIE improves VLA success rates on simulation benchmarks, with gains of up to $+5.28$ percentage points (pp) on RoboCasa-GR1 and $+1.68$ pp on RoboTwin 2.0, and achieves an average gain of $+19$ pp across five real-world manipulation tasks. It further generalizes to diffusion policies and world models, improving downstream performance in both settings. Our results highlight interface co-adaptation as an important optimization problem when coupling pretrained representations with downstream models.

---


### 49. [Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning](https://arxiv.org/abs/2611.04010)

**<font color=#1a73e8>作者：</font>** Xinbo Zhao, Yuhang Liu, Xin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To enable effective generalization in offline meta-RL, it is essential to accurately infer the underlying task through latent task representations, which provide a compact and transferable summary of task-specific characteristics for guiding policy generation. In this paper, we propose Contrastive Task-Aware Decision Transformer (CoTA-DT), a DT-based offline meta-RL framework that learns task representations by jointly integrating four complementary components: (i) contrastive learning from offline trajectories, (ii) alignment with natural-language task descriptions, (iii) one-step supervision via a task-conditioned world model, and (iv) long-term supervision via a task-conditioned Q function. The learned task representations are used as conditioning signals for a DT-based policy, enabling task-aware meta-policy learning. To further support generalization in both zero-shot and few-shot settings, we design a language-grounded, self-adaptive strategy that enables effective and reliable adaptation to unseen tasks. Notably, in CoTA-DT, the pretrained LLM serves as a shared backbone for language encoding, world modeling, Q-function estimation, and policy learning. This unified design facilitates parameter sharing, improving both efficiency and generalization. Extensive experiments across diverse offline meta-RL benchmarks demonstrate that CoTA-DT consistently outperforms prior methods, particularly in challenging zero-shot generalization scenarios.

---


### 50. [SurgEye: Instruction Tuning-Free Perception-Reasoning Framework for Surgical Scene Understanding](https://arxiv.org/abs/2611.04012)

**<font color=#1a73e8>作者：</font>** Qing Xu, Xiechen Shen, Xianjian He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical scene understanding is pivotal for computer-assisted intervention, yet demands compositional reasoning across instruments, anatomy, and workflow. Existing surgical vision-language models rely on instruction tuning with large-scale question-answer pairs, entailing laborious data curation and costly retraining. To bridge this gap, we propose SurgEye, a perception-reasoning framework that grounds reasoning in a vision foundation model without instruction tuning. Specifically, we devise Routed Multi-Task Perception (RMP) that routes the vision foundation model through task-specific pathways learned from public perception labels, producing spatial and temporal evidence. We further introduce Agentic Compositional Reasoning (ACR) that employs a frozen large language model to coordinate RMP specialists and temporal memory as callable tools, composing evidence across tasks and time into grounded answers. Moreover, we construct SurgEye-Bench spanning eight surgical procedures, pairing each question with perception labels for verifiable evaluation. Extensive experiments demonstrate that SurgEye outperforms state-of-the-arts in surgical reasoning. The source code will be available.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
