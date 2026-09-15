# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

---

### 51. [Harmfulness Propagation Dynamics: Layer-wise Trajectories of Adversarial Intent in Large Language Models](https://arxiv.org/abs/2609.13534)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Uluğ Bayazıt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify \textbf{Harmfulness Propagation Dynamics (HPD)}: for harmful prompts, the projection of the last-token hidden state onto a learned harm direction rises monotonically with transformer depth, whereas benign prompts remain flat or oscillatory. This cross-layer signature reflects harmful intent as a \emph{progressively resolved} semantic property: surface form appears early, while pragmatic intent consolidates later, making the \emph{trajectory shape} more informative than any single-layer snapshot. Moreover, LDA-based harm directions, learned per layer, remain stable across random splits (pairwise cosine similarity $>0.97$), supporting the projection sequence as a reproducible structured signal. Building on HPD, we introduce \textbf{\herald{}} (\textbf{H}armful \textbf{E}ncoding \textbf{R}ecognition via \textbf{A}ctivation \textbf{L}ayer \textbf{D}ynamics). This lightweight input moderator extracts a seven-dimensional feature record, slope, curvature, monotonicity, onset layer, and related statistics from the cross-layer projection sequence and classifies it with a 288-parameter MLP. \herald{} stores one $d$-dimensional direction per layer ($262$\,KB for a 32-layer, $d{=}4096$ model), requires no gradient computation during training, and adds only $2.6{\times}10^{-6}$ prefill FLOPs at inference. Across eight prompt-harmfulness benchmarks and four model families, \herald{} achieves an average F1 of $89.3$ on OLMo2-7B, surpassing all tested guard models on adversarial jailbreak detection ($98.4$ vs.\ $96.9$ F1) and outperforming prior latent-based methods by $2.3$-$4.1$ F1 points on every backbone. Per-instance trajectories provide machine-readable audit records that reveal \emph{when} and \emph{how} harmfulness emerges, offering an interpretability advantage over single-layer approaches.

---


### 52. [Asclepius: An Adaptive Harness for Long-Horizon Clinical Agents](https://arxiv.org/abs/2609.13543)

**<font color=#1a73e8>作者：</font>** Grace Chang Yuan, Xiaoman Zhang, Sung Eun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are predominantly benchmarked on short, single-task trajectories, yet real deployments run for hours under contention, surfacing a different class of failures. We use the Clinical Environment Simulator (CES), in which an agent manages an entire emergency-department shift under continuous time and resource pressure, as a testbed: long-horizon execution failures manifest measurably in a single rollout under structured, multi-dimensional grading. On CES, current agents reach the correct diagnosis in most cases yet fail to deliver complete and timely critical actions, revealing an execution gap. We attribute this gap to three long-horizon failure modes, each operationalized as a per-trace counter: instruction-adherence drift, treatment incompleteness, and a severity-equity gap in timeliness. We then introduce Asclepius, an adaptive agent scaffolding with a self-evolving harness that rewrites the operating manual between shifts from trace-level feedback, an externalized clinical skills library for high-stakes regimen knowledge, and three isolated subagents that partition per-turn decisions across the patient queue. On held-out batches never observed during harness evolution, Asclepius improves critical-action correctness by 22% (p = 0.024) over a strong baseline agent framework while preserving diagnostic accuracy, with consistent gains across five LLM judges from three model families; on the full ten-batch set, improvements reach 25% on critical actions and 13% on timeliness. The three failure modes form a coupled bottleneck: decisive reductions appear only when all three components act together.

---


### 53. [Toward a Decision-Assurance Layer for AI-Assisted Flight Planning in Air Traffic Management](https://arxiv.org/abs/2609.13552)

**<font color=#1a73e8>作者：</font>** Alexandre Barreto, Shou Matsumoto, Jorge Valverde-Rebaza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is increasingly being used informally in Air Traffic Management (ATM) for tasks such as flight plan generation, trajectory interpretation, and constraint checking. Although these tools can reduce workload and accelerate planning, their non-deterministic outputs create safety and operational risks in human-in-the-loop settings. This paper proposes the AI Trust and Assurance Layer (ATAL), a model-agnostic decision assurance architecture that evaluates whether AI-generated flight-planning outputs are sufficiently reliable for operational use. ATAL combines semantic stability under prompt variation, operational consistency of structured outputs, and normative constraint validation against domain rules, and maps these signals to a Decision Readiness Level (DRL) for human operators. An ATM-inspired experimental study shows how unsafe, inconsistent, or misleading outputs can be identified before influencing flight-plan validation or execution. Although demonstrated in aviation, the framework is also transferable to other safety-critical decision-support domains that require human oversight under regulatory constraints.

---


### 54. [Domain-Specific Jargon in Large Language Models: A Comparative Analysis between General-Purpose and Specialist Models](https://arxiv.org/abs/2609.13556)

**<font color=#1a73e8>作者：</font>** Darin Keng, Zhewei Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown remarkable proficiency on general-purpose tasks, yet their performance often degrades in highly-specialized technical domains. Moreover, little is known about how parametric knowledge of domain-specific terms is encoded within these models. We address this gap by contributing two novel medical jargon evaluation benchmarks and evaluate a general-purpose Llama-3.1 model against a variant fine-tuned on medical-domain data. Surprisingly, the general-purpose model outperforms the medically fine-tuned model on both tasks. Using mechanistic interpretability tools, we find systematic patterns of miscalibration for the medically fine-tuned model. Instead of reorganizing parametric knowledge, the fine-tuned model places greater emphasis on a small subset of model components associated with jargon-favoring predictions. We find that applying component reweighting strategies against the benchmark tasks successfully suppresses these components and closes the gap with the general-purpose baseline. We also observe that some jargon-sensitive components transfer knowledge to the same tasks involving materials science jargon, suggesting they encode a partially domain-agnostic notion of specialized terminology. Our results provide a case study in which a medically fine-tuned checkpoint does not improve jargon comprehension over its general-purpose counterpart, highlighting that domain adaptation should not be assumed to yield better performance on specialized terminology.

---


### 55. [Carbon-Aware Routing for Function Calling in Edge-Cloud LLM Systems](https://arxiv.org/abs/2609.13559)

**<font color=#1a73e8>作者：</font>** Aikaterini Maria Panteleaki, Varatheepan Paramanayakam, Spyros Tragoudas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) with function-calling capabilities are becoming critical for modern agentic AI systems. Nevertheless, current deployments typically route inferences to powerful cloud-based models, incurring significant energy use and carbon emissions. We address this sustainability challenge with a carbon-aware routing framework that distributes function-calling queries across a three-tier edge-cloud architecture, combining edge and cloud LLMs on heterogeneous hardware. At its core, a lightweight k-NN predictor operating in a unified semantic-lexical embedding space estimates query-specific accuracy, delay, and power consumption on each edge tier. These predictions are then combined with real-time grid carbon intensity to route every query to the lowest-emission tier capable of executing it successfully. Evaluated on state-of-the-art function-calling benchmarks and LLM families, our framework matches cloud-level accuracy while reducing operational carbon emissions by $4\times$ on average.

---


### 56. [FLoKD: Adaptive Knowledge Distillation for Federated Low-Rank LLM over Wireless Networks](https://arxiv.org/abs/2609.13580)

**<font color=#1a73e8>作者：</font>** Xinlu Zhang, Na Yan, Yang Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities across a wide range of natural language processing tasks. However, conventional fine-tuning typically relies on centralized data collection, bringing in privacy concerns. Federated learning (FL) enables collaborative LLM fine-tuning without sharing raw client data, but its deployment over bandwidth-constrained wireless networks is hindered by the communication overhead of model-parameter transmission. Although Low-Rank Adaptation (LoRA) reduces the number of trainable parameters, its communication cost still increases with model scale. Knowledge distillation avoids parameter sharing via output logits, but token-level logits in LLMs incur high communication cost due to sequence length and vocabulary size. Reducing logits lowers the cost but weakens supervision and degrades accuracy. To address these limitations, we propose FLoKD, an adaptive knowledge-distillation framework for federated LoRA fine-tuning of LLMs over wireless networks, which communicates intermediate LoRA activations as the distillation signal rather than logits or full parameters. Since transmitting all blocks over the entire public dataset remains costly, we further propose a transformer block importance scoring framework that selectively transmits the most informative blocks, and two dataset selection strategies that discard public samples deviating from the local data distribution and prioritise those most informative for distillation. Extensive experiments across multiple generative language datasets, including WikiText-103, PTB, and Dialog, demonstrate that our proposed framework reduces communication overhead by 50-65% while achieving rapid convergence to competitive perplexity compared to baselines.

---


### 57. [Toward Complete Hospital Discharge Summarization with Abstract Meaning Representation](https://arxiv.org/abs/2609.13581)

**<font color=#1a73e8>作者：</font>** Paul Landes, Sitara Rao, Aaron Jeremy Chaise 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discharge summaries are lengthy medical documents that summarize a hospital in-patient visit. Automatically generating them can reduce documentation burden and return clinician time to patient care. Whereas Large Language Model (LLMs) could be used for this task, their Achilles heel is hallucinations, which can have drastic consequences for clinical documentation. We present an evidence-driven alignment framework for discharge summarization at the clinical encounter level, that treats provenance as a first-class constraint, using semantic graphs and deep learning models. Each summary sentence is selected and organized via cross-document semantic alignment and is accompanied by explicit evidence links to its source spans. We show our results on two corpora: a publicly available corpus (MIMIC-III) and clinical notes written by physicians at the University of Illinois Hospital (UIC Health). Additionally, we make source code and trained models available.

---


### 58. [Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs](https://arxiv.org/abs/2609.13582)

**<font color=#1a73e8>作者：</font>** Rohith Reddy Bellibatlu, Manpreet Singh, Zhoutian Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A clinical agent benchmark can report the same verdict on identical inputs while the agent files a materially different order on each run. Such agents order tests, request medications and place referrals, yet benchmarks typically score one run per task and rarely ask whether identical inputs produce identical actions; MedAgentBench, the benchmark we use, scores a single attempt and says so. To measure this gap we introduce "same-input rerun", which replays a task with every input held fixed and compares the orders rather than the score, with six reliability metrics, and apply it to 1000 MedAgentBench runs across 50 tasks from its five write-capable families, two open-weight models below ten billion parameters quantised to four bits, and two temperatures. The study establishes that action-level divergence exists and can pass unrecorded by the score, not that any rate generalises. Under the 8B model at temperature 0.7, all 43 ordering groups emit a different set of orders across five identical runs, 26 emit the order on some runs and not others, and 28 record a different coded value, dose or analyte. In 22 of those 43 the benchmark reports the same failing verdict for materially different behaviour, as it does for all 10 divergent groups of the 4B model at 0.7. Orders also reach different endpoints across runs, one of which the record server rejects while the agent is told it succeeded. These findings motivate repeated-run evaluation, action-level stability reporting and execution-faithful environment feedback in clinical-agent benchmarks.

---


### 59. [Mind the Gap: Detecting Description-Execution Mismatch Attacks in DAO Governance](https://arxiv.org/abs/2609.13601)

**<font color=#1a73e8>作者：</font>** Bowen Cai, Nanzi Yang, Weiheng Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized autonomous organizations (DAOs) change protocols through a proposal-based process: initiators submit a proposal, members vote on it based on its natural-language description, and if it passes, the project executes the code behind it. This process is inherently vulnerable to deceptive proposals, where the described intent and the actual code execution mismatch. A malicious proposer can submit a benign-looking description to pass voting while the executed code transfers funds or seizes control of the protocol, which we call a Description-Execution Mismatch (DEMI) attack.
We present the first systematic framework for DEMI detection in real DAO governance. First, the diversity of DAO deployments makes a unified, scalable analysis difficult; we address this with a DAO-agnostic simulation framework that builds a per-DAO governance profile from historical on-chain transactions and then drives each new proposal through the full governance lifecycle to obtain its execution behavior. Second, free-form descriptions and structured execution traces are hard to compare; we address this with an evidence-mapping paradigm that requires an LLM to locate explicit per-action textual justifications rather than issue a holistic judgment, substantially improving precision and recall over direct querying.
On a large-scale dataset of real-world Ethereum DAO governance, our simulation derives execution results for 92.7% of active DAOs and 89.3% of executed proposals, far exceeding existing platforms. Our detector reaches 81.7% mean precision and 98.3% mean recall under stratified cross-validation, and evidence mapping generalizes across LLM vendors rather than depending on one model. Under a systematic red-team/blue-team evaluation, the Robustness Guard defends most adaptive attacks even against an adversary that knows the detector, and this robustness generalizes to held-out proposals.

---


### 60. [In the Blind: Building Pseudo-References for MT Evaluation](https://arxiv.org/abs/2609.13611)

**<font color=#1a73e8>作者：</font>** Diptesh Kanojia, Chi-kiu Lo, Archchana Sindhujan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The WMT26 General MT task evaluates systems on 10 language pairs that have no human references (neither translated from scratch nor post-edited from MT output by humans). We describe how we built the pseudo-references for these pairs and six other language pairs (in which some forms of human references are available): seven models translate the 3,277 official documents under up to five prompt conditions, giving a total of 26 system-prompt combinations; then three reference-free quality estimation (QE) models score every candidate; and a per-document selector picks one translation, which GPT-5.5 post-edits where needed. Working without references exposed a failure mode of QE-guided selection: the metrics rank fluent output in the wrong language above correct translations. Adding a confidence-scaled language identification penalty to the score fusion drives the wrong-language count to zero, and the resulting selector still scores better on MetricX than the rank-fusion baseline it replaces. Since no references were available for these pairs while we were building them, we calibrate every selection decision on last year's WMT25 human judgments. The human evaluation, released after construction, shows the cost of getting selection wrong: our references stand with the strongest participating systems when the selector kept a frontier-model candidate, and fall up to 17 ESA points below them when it did not. We release the selection method and the provenance of every reference (this https URL)

---


### 61. [AttnFuse: A Composable DSL for Compiling Attentions to Fused GPU Kernels](https://arxiv.org/abs/2609.13612)

**<font color=#1a73e8>作者：</font>** Varun Kumar Dasoju, Tian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern AI systems are built on the Transformer architecture, whose core operation, attention, accounts for the majority of computation and memory cost. Researchers continually propose new attention variants to improve quality, efficiency, or context length, but each variant currently requires expert-written GPU code to run at usable speeds. PyTorch's recent flex\_attention lets researchers describe custom attention patterns in Python and compile them to fused kernels, but its design is limited to modifications applied after the central matrix multiplication, excluding Rotary Position Embedding (RoPE), the positional encoding used by every major LLM.
We introduce AttnFuse, a small DSL for attention that makes pre-multiplication transformations like RoPE first-class operations. Researchers compose ten high-level building blocks to describe a variant, and AttnFuse's compiler emits a single fused GPU kernel for the entire computation. On an RTX 3090, AttnFuse achieves a 2.10$\times$ speedup over flex\_attention on the RoPE+causal pattern. On an H100, it runs a full Llama-3-8B training step within 5\% of PyTorch's hand-tuned backend. Our investigation reveals the Rotation Calculus: whether to fuse RoPE or apply it separately depends on the GPU's compute-to-bandwidth ratio, with a derived crossover that matches measurement. AttnFuse demonstrates that a small, attention-specific compiler can close the gap between flexible research code and production kernels.

---


### 62. [The University of Melbourne WMT 2026 CreoleMT Submission: A Domain-Balanced Approach to Low-Resource Pacific Creole Machine Translation](https://arxiv.org/abs/2609.13615)

**<font color=#1a73e8>作者：</font>** Raphaël Merx, Nick Thieberger, Ekaterina Vylomova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For our submission to the WMT26 Creole Language Translation Shared Task, we focus on machine translation (MT) models for Pacific creoles: Tok Pisin, Bislama, and Solomon Pijin, with particular attention to broad domain performance. After pre-training on a large collection of domain-imbalanced data, we continue fine-tuning on a diverse mix of domain-balanced data. We rely on a number of data collection and preparation techniques, including LLM-assisted respelling and alignment, back-translation, and distillation from Gemini for domains originally not present in training data. Evaluated on Bouquet and a novel test set made of spoken language transcripts, our models beat open model baselines by 3+ chrF++ points in all directions with human-original references. Looking ahead, we plan to develop human-translated test sets for Solomon Pijin and Bislama, and to distil our best models into much smaller ones that retain broad domain coverage.

---


### 63. [From Advertised Improvements to Measured Capabilities: Evaluating ChatGPT Images 2.5 on Forgery Tasks](https://arxiv.org/abs/2609.13617)

**<font color=#1a73e8>作者：</font>** Ankit Raj, Yuxin Zhang, Kidus Zewde 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We evaluate whether the improvements advertised for ChatGPT Images 2.5 translate into better performance on forgery tasks with predetermined answers. We compare its Flare and Sunburst API models with GPT-Image-2 re-run in the same week, using receipt-field edits, repeated editing, product placement and fine-print rendering. After image registration, Flare and Sunburst show fewer OCR-detected changes to surrounding receipt text (31.7% and 31.2% versus 44.2% for both GPT-Image-2 baselines), mainly on CORD receipts, without a detectable improvement in target-field correctness. Flare retains fewer earlier edits on CORD receipts, while photo-edit sequences provide little separation between models. Product codes are more often legible with Images 2.5, alongside larger product placement; the analyses do not establish a fidelity gain independent of size. Fine-print improvements remain unresolved below the OCR reliability limit. Refusals are rare and localisation is weak in both generations. At a fixed detection threshold, Community Forensics flags 68.6% of controlled Images 2.5 images averaged across cells, versus 35.9% of self-reported images posted online. These results motivate task-specific evaluation of advertised capabilities and defences, with explicit limits on what automatic checks can establish.

---


### 64. [Identity Is More Than Recall: A Benchmark for Persistent Identity in Deployed AI Agents](https://arxiv.org/abs/2609.13637)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhao, Roy Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent agents need evaluations that distinguish identity facts they can recall from those they express and enact. We introduce PAI-Bench, a provider-neutral benchmark for fidelity to a versioned, update-governed identity contract. It separates recall, composition, behavioral enactment, resistance, persistence, lineage, and role-conditioned updates while keeping scoring oracles outside the target process. Two frozen campaigns cover sixteen synthetic profiles, thirty-two probes, and three independently initialized target configurations, yielding 1,536 retained responses. A judge-independent literal audit finds direct-parent identifiers in 48/48 atomic responses but only 1/48 implicit self-portraits. On eight profiles, explicit field cues increase joint presence of three identity identifiers from 0/8 to 7/8 under the same four-sentence instruction. A separate startup body-label substitution increases full-designation presence from 1/8 to 7/8 while parents remain absent. These contrasts reveal prompt-dependent component selection and component-specific sensitivity to startup cues in the tested deployments. Replaying identical factorial responses also yields a Claude headline mean 12.5 percentage points below Astra's, demonstrating evaluator sensitivity separately from target behavior. The studies use single target samples per condition, with post-hoc audits and follow-ups. PAI-Bench provides a reproducible evaluation protocol for measuring factual availability, identity expression, and behavioral enactment as distinct aspects of identity-contract fidelity.

---


### 65. [Solar Intelligence](https://arxiv.org/abs/2609.13648)

**<font color=#1a73e8>作者：</font>** Jyotsna Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solar energy decision support is fragmented across dashboards that provide data without explanation, research papers are slow to parse, and general-purpose language models are not solar domain specific and answer without evidence. This paper introduces Solar Intelligence, a hybrid retrieval-augmented framework that unifies structured solar analytics, evidence-grounded scientific question answering, and machine learning forecasting in one system. The platform integrates daily NASA POWER solar and meteorological data, Biosphere 2 ground-sensor readings, and a curated corpus of research papers and institutional reports. Structured queries use DuckDB SQL; scientific questions are answered by a hybrid retriever that fuses BM25 and ChromaDB dense embeddings via Reciprocal Rank Fusion, with responses grounded through a language model (llama3.2:3b). An Extreme Gradient Boosting (XGBoost) model produces daily forecasts of irradiance, temperature, and wind speed. The system is exposed via FastAPI, Streamlit, and an MCP server, so it can be used as an application, an API service, or an agent tool - by students, researchers, and energy analysts.

---


### 66. [Safety as a Constraint: Fine-Tuning a LLM Recommender to Explain Itself](https://arxiv.org/abs/2609.13657)

**<font color=#1a73e8>作者：</font>** Jiashu He, Emma Yanyang Kong, JJ Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional recommender systems are typically trained to predict what item users will interact with next, but not why. However, offering personalized evidence for why a user might like the predicted item is an important way to enhance the service and to raise the likelihood that the user will be genuinely interested in the recommendation. This service can be delivered by integrating a frontier-model call into the member-facing pipeline, but it will add extra cost and latency. In this paper, we train a recommender LLM to generate personalized explanations for its reccomendation, based on the user's watching history at a large video streaming service. We impose two requirements on the generated explanation: it must be faithful to the elements of the shows it links, and it must be strictly non-harmful to the user. To this end, we first train two LLM-judge reward models covering three specific criteria, and propose constrained GRPO to incorporate these different criteria. On a held-out real-world testing set, our fine-tuned model improves the all-three-criteria PASS rate rises from 0.649 to 0.956 under our own judges and from 0.677 to 0.931 under an independent judge, where as the frontier generator performs similar to the untuned recommender baseline. We conduct further experiments to show that the model's language and recommendation abilities remain unchanged. Based on these results, we conclude that an LLM-based recommender can be fine-tuned on other complex tasks without compromising its original recommendation performance, thus provide insights for further agentic user interface powered by a single model.

---


### 67. [GeoSkill:Experience-Driven Hierarchical Skill Learning with Collaborative Revision forGeospatialAgents](https://arxiv.org/abs/2609.13667)

**<font color=#1a73e8>作者：</font>** Han Luo, Xian Xu, Yinhe Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial agents are increasingly expected to support recurring and evolving analytical tasks rather than execute isolated workflows. In such settings, effective agents must distill prior execution experience into reusable geospatial procedural knowledge to guide future planning and tool use. However, existing memory-augmented paradigms struggle to summarize both long-horizon tool-chain orchestration experience and tool-level invocation constraints in geospatial analysis, while directly relying on LLM self-reflection to update experience often leads to misattribution and unreliable revisions. To address these challenges, we propose GeoSkill, an experience-driven hierarchical skill learning framework for geospatial agents. GeoSkill comprises two core components: (i) a Hierarchical Skill Bank (HSB), consisting of a Planning Skill Bank and a Tool Skill Bank, which respectively distill high-level task-planning experience and tool usage constraints, enabling structured representation and cross-task reuse of historical execution experience; and (ii) a Collaborative Trace-driven Skill Revision (CTSR) mechanism, where Judge, Critic, and Refiner collaboratively perform error identification, skill-level defect localization, and targeted modification, preventing misattributed and unreliable revisions from polluting the skill bank. GeoSkill learns and validates skills from historical executions during development, and freezes the skill bank for retrieval-only guidance on unseen tasks during deployment. Extensive experiments on EarthBench and ThinkGeo demonstrate that GeoSkill effectively transforms historical execution experience into reusable hierarchical skills, improving both end-to-end task accuracy and tool-execution reliability in geospatial tasks.

---


### 68. [Enhancing Event Candidate Acquisition for Event Linking](https://arxiv.org/abs/2609.13670)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Yinan Liu, Boyi Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Event linking associates event mentions in text with entries in a knowledge base (KB), or identifies them as out-of-KB events. Although existing methods use different architectures, candidate event acquisition can still be weakened by short ambiguous mentions, noisy arguments, and evidence that is unevenly useful for retrieval. We present MACE, a Multi-Agent Candidate Event acquisition method that refines event structure before linking. MACE uses evidence-specialized LLM agents to acquire time, location, participant, and event-type evidence, exposes intermediate queries to candidate-event lookup tools, and lets a coordinator revise the evidence set before final candidate construction. Experiments on two event linking benchmarks show that adding MACE to different event linking models consistently improves accuracy. These results show that MACE improves event linking through better candidate event acquisition without modifying the event linking model.

---


### 69. [Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct Models](https://arxiv.org/abs/2609.13680)

**<font color=#1a73e8>作者：</font>** Fei Yuan, Changjiang Gao, Yilei Tu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning instruct models often improves target performance while inducing behavioral drift from the reference model, which can degrade existing capabilities. Rather than treating this drift as an uncontrolled consequence of optimization, we specify a behavioral drift budget before optimization and ask how to boost the target-task performance within it. Locally, behavioral drift induces a shared geometry anchored at the reference model, with the drift budget defining a boundary within this space. In this space, drift determines distance from the reference, leaving update direction as the remaining degree of freedom. Fine-tuning updates can therefore be compared through their directional efficiency, naturally reformulating fine-tuning as a direction-selection problem. This reformulation makes a concrete prediction: changing the accessible directions can qualitatively alter the outcome of fine-tuning. We test this prediction in a stringent QA-only setting, where strong instruct models are fine-tuned only on final answers but must still generate multi-step reasoning at inference. Despite this mismatch, a coarse layer-selective probe reverses the failure of QA-only fine-tuning and reveals the existence of effective directions, with multiple neighboring configurations improving target performance while preserving reasoning and general capabilities. Across Qwen3-8B and Qwen3-14B, these directions substantially improve scientific reasoning and multilingual translation. Over more than 100 languages, the resulting models match or outperform dedicated translation systems and provide a stronger initialization for subsequent reinforcement learning. Our results suggest that fine-tuning is not just about how much a model changes, but how that change is spent. this https URL and this https URL

---


### 70. [LayerRoute: Adaptive Layer-Skipping with LoRA-Preserved Quality for Efficient LLM Inference](https://arxiv.org/abs/2609.13682)

**<font color=#1a73e8>作者：</font>** Prateek Kumar Sikdar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce LayerRoute, a parameter-efficient method for adaptive transformer layer-skipping that combines per-layer hard-gated routing (trained via a straight-through estimator) with joint LoRA fine-tuning. LayerRoute augments each of the 24 transformer blocks in Qwen2.5-0.5B-Instruct with a lightweight per-layer router (~21.5K parameters) and LoRA adapters (rank 8, ~1.08M parameters), training both jointly under a gate-regularized language-modeling objective. Across 10 independently-seeded training runs, LayerRoute converges to an identical skip-pattern structure in every run - a consistent set of 9 middle layers (8-16) becomes skip-eligible in all 10 seeds - and delivers genuine, verified wallclock speedup in every run (1.02x-1.06x, mean 1.04x). Quality is preserved or improved in every configuration tested: joint LoRA adaptation yields a perplexity improvement over the unmodified backbone in all 10 seeds (mean delta = -1.16 and -1.11 across the two evaluation splits used). We further verify the router performs genuine, non-trivial per-input computation: gate decisions in skip-eligible layers change the actual skip/run outcome for 87-100% of held-out samples, confirming real input-dependent routing rather than a fixed pruning pattern. LayerRoute trains in under 7 minutes on a single A100 and adds negligible overhead beyond the routing decision itself. We report our full reproducibility methodology, including a systematic diagnostic investigation into what determines the router's per-input decisions, as part of this work.

---


### 71. [Not all Negation Cues are Equal: Affixal Negations Yield Better Negation Understanding](https://arxiv.org/abs/2609.13685)

**<font color=#1a73e8>作者：</font>** Tian Tan, Eduardo Blanco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation remains a longstanding challenge for both language models (LMs) and large language models (LLMs). Prior work mainly focuses on a small set of high-frequency single-word negation cues, such as not and never, with limited exploration of broader negation types and modern LLMs. To address this gap, we construct NegCue, a large-scale dataset containing over 1.8M samples spanning single-word, multi-word, and affixal negation with more than 200 unique cues. We further pre-train both encoder-only LMs and LLMs on NegCue to investigate how different negation types affect negation understanding. Experiments on five downstream benchmarks show that negation types contribute unevenly to performance gains under the same training scale. In particular, affixal negation yields the largest improvements, while the gains from the commonly studied single-word negation remain modest. Moreover, our results demonstrate that further pre-training improves negation understanding for both LMs and LLMs.

---


### 72. [Oops, Not Now: PEARL, a RAG-Based Support Agent for Gameplay and What Players Want from AI Help](https://arxiv.org/abs/2609.13718)

**<font color=#1a73e8>作者：</font>** Jiahong Li, Sai Siddartha Maram, Atieh Kashani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered gameplay support agents hold promise for game-based learning, yet grounding generative models in structured game data remains an open challenge. We present PEARL (Parallel Education Agent for Reflection and Learning), a dual-component Retrieval-Augmented Generation (RAG) system that combines semantic knowledge retrieval with structural board-state matching to deliver contextualized scaffolding in Parallel, a puzzle game for learning parallel programming. PEARL operates on two input streams (natural language queries and board topology), retrieving both conceptual explanations of gameplay moves and peer-generated board states as evidence: capabilities unavailable to a standard Large Language Model (LLM) with game state access alone. In a qualitative evaluation (N=10) comparing PEARL against an existing community-based Open Player Model (OPM) visualization system, participants preferred the visualization system on perceived usefulness and reported higher frustration with PEARL; five of ten minimized or abandoned the AI tool during play. Proactive delivery, generic responses, and trust deficits drove disengagement, while a subset of four participants found PEARL's grounded explanations complementary to visualization in specific contexts where they initiated the interaction. We position PEARL as a deployed design probe whose failure modes inform a concrete design agenda for AI gameplay support, captured as seven open problems for the community.

---


### 73. [Scaling Hindi Quantum Natural Language Processing through Automatic Pregroup Supertagging](https://arxiv.org/abs/2609.13721)

**<font color=#1a73e8>作者：</font>** Gautami Sanjay Naik, Krishna Bhatia, Mithun Paul Saint-Germain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantum Natural Language Processing (QNLP) uses pregroup grammars to translate grammatical structure into diagrammatic representations and quantum circuits. Recent Hindi QNLP work has shown that Hindi-specific pregroup grammars can support grammar-sensitive compositional models, but grammatical type assignment is still largely manual, limiting scalability. This paper formulates automatic Hindi pregroup supertagging as a token-level classification task. Using a manually annotated corpus of 380 Hindi sentences, we evaluate lexical, contextual, prompting-based, lexical-repair, and suffix/morphology-aware methods. Results show that simple lexical and contextual models are strong in this low-resource setting: contextual backoff achieves the best completed accuracy of 64.56\%, while raw Qwen2.5 prompting reaches only 11.65\%. Lexical repair raises LLM-assisted prediction to 64.08\%, demonstrating the value of constraining generative outputs with symbolic grammar knowledge. Diagnostic analysis further shows that seen and unambiguous tokens are much easier than unseen tokens, and suffix/morphology features improve karaka-token accuracy but not overall performance. These results show that automatic Hindi pregroup assignment is feasible and can reduce reliance on manual annotation in future multilingual QNLP pipelines.

---


### 74. [IBBench-Light: A Paired Evaluation of Task-Conditioned Responses to External Directives](https://arxiv.org/abs/2609.13725)

**<font color=#1a73e8>作者：</font>** Kainan Zhou, Gangzhen Qian, Zhaoyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An external record may contain a procedure to apply or text to read, depending on the user's request. IBBench-Light tests both uses against the same record. Twelve semantic bases yield 144 matched pairs per model; four quantized instruction models produced 1,152 archived greedy responses. Paired exact-contract accuracy (PECA) requires both members to satisfy their output contracts. Qwen succeeds on 132 execute and 109 process prompts, but only 97 complete pairs, showing what marginal averages omit. We audit literal-target exposure and case normalization, then add 1,722 logged CPU generations to test directive-absent controls, twelve additional semantic bases, within-base wording changes, and generation stopping. In the pinned Phi rerun, changing the end-of-sequence (EOS) set changes exact paired success from 0/144 to 62/144. A bounded IHEval comparison uses the same SmolLM2 checkpoint and output budget while preserving its published instruction roles and scorer. The benchmark measures conditional task and output-contract success. Its task margins and paired count need to be read together with the stopping policy.

---


### 75. [Trustworthy Agentic AI: A Comprehensive Cybersecurity and Systems Survey on Threat Landscapes, Defense Architectures, and Open Challenges](https://arxiv.org/abs/2609.13731)

**<font color=#1a73e8>作者：</font>** Seyedakbar Mostafavi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition from passive foundation models to autonomous, goal-directed agentic AI systems has introduced unprecedented capabilities by coupling recursive cognitive reasoning loops, persistent memory architectures, live tool execution planes, and multi-agent collaboration topologies. However, granting probabilistic neural cores execution authority across filesystems, networks, and cloud infrastructure dissolves classical security perimeters: natural language simultaneously serves as input data, internal control code, and communication protocols, exposing a Turing-complete blast radius where untrusted data represents executable instructions. This survey delivers a comprehensive systems-security reference framework for trustworthy agentic AI, synthesizing 206 foundational studies and regulatory standards. We formalize the general agent architecture as a stateful 5-tuple and establish a 6-dimensional trustworthiness taxonomy covering security, safety, privacy, explainability, fairness, and accountability. We systematically analyze threat surfaces across intra-execution loops and interaction planes, formulate a multi-layered zero-trust defense-in-depth architecture integrating Dual-LLM isolation, Capability-Based Access Control, kernel eBPF probes, and sandboxed runtimes, review standardized evaluation benchmarks, and map technical controls to international AI governance frameworks.

---


### 76. [PolicyMem: Geometric Policy Memory for LLM Governance](https://arxiv.org/abs/2609.13734)

**<font color=#1a73e8>作者：</font>** Yuanchen Bei, Zhengzhang Chen, Yanjun Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in real-world high-stakes applications, effective governance has become essential. Existing safeguards largely follow two paradigms: learning-based guards provide strong semantic discrimination but couple policy behavior to trained models and taxonomies, while programmable frameworks offer flexible control but require substantial manual prompt and workflow engineering. Neither externalizes policies as reusable operational states, making it difficult to consistently reuse policy evidence across detection, intervention, and verification. In this paper, we introduce PolicyMem, a geometric policy memory that externalizes natural-language policies as reusable geometric memory objects represented by low-rank subspaces in a shared representation space. A memory writer compiles natural-language policies into policy memory slots, and query-response pairs read the policy memory through projection energy. The resulting policy-evidence profile directly mediates the safety verdict and is reused for policy attribution and post-intervention verification. Coupled with a response rewriter, PolicyMem enables a detect-rewrite-verify loop for LLM governance. Across five widely used benchmarks, PolicyMem achieves state-of-the-art unsafe behavior detection while enabling effective policy attribution, rewriting, and post-intervention verification through the shared policy memory.

---


### 77. [ForeSight: Enhancing Risk Monitoring via Early Safety Signal Distillation](https://arxiv.org/abs/2609.13737)

**<font color=#1a73e8>作者：</font>** Hanling Wang, Chenlong Wei, Ling Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed, the generation of harmful content has become a critical safety concern. Existing safeguards operate at the input, output, or streaming-generation stages, while early-risk methods that rely on surface tokens or output logits may suffer from weak initial signals, and internals-based detectors using dense representations may retain highly entangled and redundant safety-irrelevant information. It therefore remains unclear whether the earliest post-generation hidden states already contain reliable signals about final-response harmfulness. To address this gap, we propose ForeSight, a first-token output-risk forecasting framework that distills weak and redundant early safety signals into compact, layer-aware risk representations. Experiments on five safety benchmarks and two target models demonstrate that ForeSight achieves superior and efficient early-risk forecasting while relying solely on first-token hidden states. The code is available at: this https URL

---


### 78. [HarnessBandit: Joint Learnability-Transferability Scheduling for Multi-Harness Agentic Reinforcement Learning](https://arxiv.org/abs/2609.13739)

**<font color=#1a73e8>作者：</font>** Hongliang Wei, Xiaobing Tu, Yinggui Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly deployed through diverse harnesses that differ in system prompts, tool schemas, control loops, and trajectory formats. The same model can perform unevenly across these interfaces, making robustness to harness variation an important objective. A natural approach is to train a shared policy through multiple harnesses, but doing so introduces a scheduling problem: each training step should favor a harness that currently provides a useful learning signal while also producing an update that benefits the other harnesses. We develop HarnessBandit, an online scheduler that selects one harness per optimizer step. After a group-relative policy optimization (GRPO) update, it observes learnability -- the mean absolute advantage on the batch -- and transferability -- the cosine between a low-dimensional gradient sketch of the current harness and exponential moving averages of the remaining harnesses. The two signals are fused after pooled sliding-window min-max normalization and sampled with a visit-dependent bonus and an explicit exploration floor. We train Qwen3.5-2B across six harnesses on ClawGym and evaluate on PinchBench (held-out tasks, in-distribution OpenClaw) and ClawEval (held-out tasks and harness). HarnessBandit improves over mixed-batch multi-harness training on both benchmarks, while training diagnostics indicate that learnability and transferability provide distinct, evolving signals.

---


### 79. [Hyper-LLaVA: Hyperbolic Uncertainty-aware Modality-Balanced Routing for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2609.13742)

**<font color=#1a73e8>作者：</font>** Kunlun Xu, Yanqin Zhang, Wenwen Qiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Continual Instruction Tuning (MCIT) aims to exploit the incrementally accumulated knowledge to process multimodal inputs of diverse tasks, where parameter routing plays an important role. State-of-the-art methods rely on sample-to-task center similarity and cross-modal fusion with equal weight during routing. However, such solutions face two fundamental flaws: (1) Within each modality, the sample-to-task center distance is sub-optimal for routing since the abundant intra-task diversity information is underleveraged. (2) Different modalities exhibit varying reliability across tasks, where the modality with inter-task ambiguity can easily misguide the routing result. To address these problems, we propose Hyperbolic Uncertainty-aware Modality-Balanced Routing (Hyper-LLaVA) to improve parameter routing capacity based on cross-modality task feature uncertainty modeling. Specifically, to improve intra-modality task matching, Hyper-LLaVA accesses the sample-to-task distribution similarity in the Hyperbolic space. Besides, to alleviate the degradation brought by unreliable modalities, Hyper-LLaVA quantifies the task matching ambiguity within each modality to achieve adaptive balancing between task matching across modalities. Based on the complementary intra- and inter-modality task matching enhancement, our Hyper-LLaVA outperforms state-of-the-art approaches by large margins. Our source code is available at this https URL

---


### 80. [Inside VLM Chart Reading: Tracing Value Reading from Vertical Bar Charts Across Space and Depth](https://arxiv.org/abs/2609.13745)

**<font color=#1a73e8>作者：</font>** Tianhao Niu, Qingfu Zhu, Wanxiang Che  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision--language models (VLMs) can answer chart questions accurately, but output accuracy does not show how they combine the evidence needed to recover an exact value. We study vertical-bar value reading with controlled counterfactual activation patching in Qwen2.5VL-7B-Instruct and InternVL3.5-8B. The study connects three analyses: (1) The single-factor results show that the changed bar-top region restores much more answer preference than the unchanged bar body, despite containing fewer visual tokens. Legend- and series-related states also lose local recoverability earlier than bar-geometry and axis-scale states. (2) In the handoff analysis, restoration shifts from visual legend regions in early layers to prompt-series positions in middle layers. Resetting the prompt-series state selectively reduces legend-source rescue, supporting its role as a partial mediator. (3) In the factorial analysis, both models can use geometry and scale states from separate donors to favor the combined target. InternVL performs similarly when the states come from separate donors or one image, while Qwen shows lower restoration for separate donors which suggests higher context sensitivity. Together, these results provide preliminary causal evidence for localizing the internal computations that support exact bar-value reading.

---


### 81. [How Many Thoughts Can a Vector Hold? The Capacity of Reasoning by Superposition](https://arxiv.org/abs/2609.13747)

**<font color=#1a73e8>作者：</font>** Hongyu Gu, Chang Liu, Jingwen Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models solve hard problems through intermediate computations across multi-step reasoning. Traditional chain-of-thought encodes these computations as tokens. Recent continuous and recurrent methods instead move partial computations into fixed-dimensional latent states, where a single thought can superpose multiple alternatives. This raises a fundamental design question:what should continuous thoughts preserve as reasoning proceeds? An intuitive approach discards past computations and keeps only the current reasoning frontier. Storing more items seems to dilute states and waste limited representational capacity. We show this intuition can be incorrect. Under identical downstream computations, cumulative superposition retaining full reasoning history can require lower representational dimensions than frontier-only superposition holding only current alternatives. At fixed hidden width, this advantage allows latent reasoners to retain more valid evidence, distinguish more plausible downstream outcomes, and delay the point where compressed states turn unreliable. This counter-intuitive effect emerges because informative historical components coherently reinforce each other, while unrelated alternatives bring random interference. This perspective also answers a practical design question: how should models weight memories accumulated inside latent states when their future use is unknown? Across reusable weighted superpositions, prioritizing a small set of recent or salient items produces weakly-represented memories that bottleneck subsequent attention. Uniform cumulative weighting avoids this flaw, and we prove it is minimax-optimal for robust future reasoning. Our results turn superposition from an observed latent-space effect into a design principle: balanced cumulative memory lets a fixed representational budget support more reliable, reusable computations.

---


### 82. [Positioning manuscripts in the scientific landscape with agentic AI](https://arxiv.org/abs/2609.13760)

**<font color=#1a73e8>作者：</font>** Jiawen Chen, Zichen Zhang, Bingxuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Publishing a research manuscript is a routine yet demanding part of scientific life: time-consuming, stressful, and often uncertain in outcome. Recent advances in large language model (LLM)-based agentic AI have shown promise across a range of scientific tasks, and here we ask whether agentic AI can help researchers navigate the publication process itself by reliably inferring a manuscript's eventual publication venue from its content and literature context. We introduce PASS (Publication-oriented Agentic Scientific System), an agentic system that understands manuscripts within their domain-specific literature context and predicts top-matched publication venues. PASS positions each manuscript within its surrounding literature landscape by reconstructing its local scientific neighborhood, tracing its topic trajectory, and reasoning over field-specific journal spaces. Evaluated on a leakage-audited benchmark of over 2,000 preprints across 16 biomedical fields, PASS achieved Top-1 accuracy of 50.3% and Top-5 accuracy of 86.1%, outperforming state-of-the-art LLM baselines and established journal-selection tools. PASS-produced quality scores, such as impact potential and novelty, aligned with independent measures of publication outcome. We also found that the designed literature retrieval module is the strongest performance contributor, particularly for positioning manuscripts relative to nearby work, and that PASS maintained near-full performance from the abstract alone, whereas LLM baselines required the full manuscript text. An independent human evaluation found strong researcher agreement with PASS's manuscript understanding and recommendation rationale. PASS has been released as a public platform (this https URL) for broad researcher access.

---


### 83. [Does Reasoning Improve Psychological Depth in Large Language Models? It Depends on Who's Judging](https://arxiv.org/abs/2609.13773)

**<font color=#1a73e8>作者：</font>** Ruichen Zheng, Yihe Wang, Fabrice Y Harel-Canada 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge evaluators are increasingly used to score open-ended generation, yet a judge's correlation with human ratings on its development set may not guarantee valid measurement when outputs are closely matched and human preferences are subjective. We study this failure mode through psychological depth in short stories. Seven human readers and an LLM-judge ensemble selected on the original scalar Psychological Depth Scale dataset ($\rho = 0.646$) evaluated 60 blinded, prompt-matched story pairs from GPT-5 vs.\ GPT-4o and DeepSeek-R1 vs.\ DeepSeek-V3. Human preferences showed no universal reasoning advantage: GPT-5 was modestly preferred over GPT-4o (60.0--62.9\%), whereas DeepSeek-R1 trailed V3 (42.9\%), and inter-reader agreement was near chance (Krippendorff's $\alpha = 0.070$), with within-reader consistency and recurring weighting patterns suggesting structured heterogeneity rather than random responding. The judge, by contrast, favored reasoning outputs in 89.0\% of dimension-level comparisons and 59 of 60 pairs on aggregate PDS, uniformly across all five evaluator configurations, and its scores were associated with surface features such as sentence length and lexical diversity. These results suggest that development-set performance is insufficient evidence for deployment validity on a shifted distribution, and that point-estimate judges can obscure the heterogeneity in subjective human evaluation.

---


### 84. [Surprising Effectiveness of Self-Demonstrations in Enhancing Schema-Ontology Mapping with LLMs](https://arxiv.org/abs/2609.13776)

**<font color=#1a73e8>作者：</font>** Siddhesh Thombre, Manasi Patwardhan, Sunita Sarawagi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating heterogeneous relational databases into a centralized ontology remains a persistent challenge in enterprise knowledge representation, primarily due to semantic heterogeneity, cryptic schema naming, missing metadata, and the abstraction gap between relational schemas and ontological models. Although large language models (LLMs) offer strong semantic reasoning capabilities, we show that directly applying them through one-shot prompting or naive multi-stage pipelines leads to poor performance for schema-ontology mapping. This paper presents a self-demonstration-driven approach that combines a neuro-symbolic task decomposition with a novel mechanism for automatically generating pattern-guided, dependency-aware demonstrations to address this integration challenge. Our approach incorporates two key strategies to achieve substantial accuracy gains over existing LLM-based schema integration methods: (i) a neuro-symbolic decomposition of the task into cascaded sub-tasks, where symbolic constraints structure the search space and LLMs perform semantic reasoning within each focused sub-task, and (ii) self-generated demonstrations guided by domain-agnostic patterns to supervise each sub-task. Experiments on three of the most challenging scenarios from the RODI benchmark show that our approach achieves state-of-the-art performance, substantially outperforming (25 percentage points F1 improvements) both traditional schema-to-ontology mapping techniques and recent LLM-based schema-to-ontology and schema matching approaches. Ablation studies further reveal the significant benefits of pattern-guided self-demonstrations and the complementary benefits of neuro-symbolic task decomposition.

---


### 85. [StepPrune: Adaptive Sequential Visual Token Selection across Multimodal Large Language Models](https://arxiv.org/abs/2609.13804)

**<font color=#1a73e8>作者：</font>** Hansen Zhang, Landi He, Mingde Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prefixes account for a major portion of the per-layer computation in multimodal large language models (MLLMs), making visual-token pruning a direct approach to accelerating inference. Existing top-K methods typically evaluate tokens independently and apply a uniform budget to all inputs, overlooking both selection-dependent interactions and variations in visual complexity across samples. In contrast, we propose StepPrune, which formulates visual-token pruning as an adaptive sequential decision process. Conditioned on previously selected tokens and textual context, StepPrune progressively constructs the retained subset and automatically determines its size through a learned STOP action. During training, a variance-preserving noise gate provides a differentiable surrogate for the discrete selection process, whereas during inference, unselected tokens are physically removed before language-model prefill. A grouped selection mechanism further extends StepPrune to high-resolution inputs. Experiments across LLaVA-1.5, LLaVA-NeXT, Qwen2.5-VL, and InternVL3 show that StepPrune achieves the best average normalized performance retention across all evaluated pruning rates on LLaVA-1.5, Qwen2.5-VL, and InternVL3, while remaining competitive on the substantially longer AnyRes prefixes of LLaVA-NeXT. On LLaVA-1.5, StepPrune retains 94.6% of the full-prefix normalized performance while pruning 88.9% of the visual tokens. At a mean retained count of 64, StepPrune reduces prefill latency from 59.95 ms to 40.05 ms, corresponding to a 1.50x prefill speed-up.

---


### 86. [LLM-Enhanced Multi-Agent Reinforcement Learning for Unified Electric Vehicles-Charging Station-Grid Optimization in Public Charging Systems](https://arxiv.org/abs/2609.13805)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Lindong Xie, Chongyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the era of the Internet of Things (IoT), coordinating connected electric vehicle (EV) charging scheduling to balance EV charging satisfaction, station profitability, and smart grid stability presents a complex multi-objective challenge. Existing Multi-Agent Reinforcement Learning (MARL) approaches often struggle with high-dimensional state spaces generated by massive IoT sensing data and conflicting stakeholder interests. This paper proposes a novel LLM-enhanced MARL framework that, for the first time, simultaneously optimizes the Grid, EVs, and Stations within a unified loop. By integrating Large Language Model (LLM), we address two critical bottlenecks: interpretable feature selection and adaptive multi-objective balancing. The LLM analyzes real-time IoT-collected environmental states to extract physically significant features and dynamically assigns weights to conflicting objectives-including profit, user satisfaction, and grid load-using semantic reasoning instead of complex manual tuning. Extensive experiments demonstrate that our framework significantly outperforms state-of-the-art baselines, achieving superior market efficiency while reducing training time by over 70%. This approach offers a scalable, transparent solution for efficient and sustainable IoT-enabled urban charging infrastructure management.

---


### 87. [Bypass Observation: A Conceptual Design of a Non-Intrusive Layer-Wise Semantic Extraction Architecture](https://arxiv.org/abs/2609.13807)

**<font color=#1a73e8>作者：</font>** Haibin Tong, Jiang Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models reason in high-dimensional hidden-state spaces, while users observe only final outputs. We introduce Bypass Observation, a non-intrusive layer-wise readout architecture that attaches read-only observation heads to selected Transformer layers without feeding their outputs back into the backbone. We consider three variants: a shared LM head across layers, layer-specific heads, and a layer- or step-adaptive head. For full-vocabulary readout, we derive a closed-form overhead approximation governed primarily by V/(12d), with representative estimates ranging from about 30% to 240%, and discuss cost reductions via sparse observation, low-rank factorization, reduced vocabularies, top-k readout, and selective positions. We argue that Bypass Observation can make model computation more observable while remaining only a partial, potentially misleading projection of hidden states. We further distinguish bypass chain-of-thought from conventional chain-of-thought: conventional reasoning tokens enter the autoregressive computation, whereas bypass readouts remain causally external at inference time, although they can still provide training signals in reinforcement learning. Finally, we discuss applications to looped and recurrent-depth Transformers, where iteration-wise readout may expose convergence, oscillation, and potential halting signals. The proposal is conceptual and analytical; systematic empirical validation remains future work.

---


### 88. [DARE: Dialectical Agentic Reasoning for Structured Knowledge Fact Checking](https://arxiv.org/abs/2609.13808)

**<font color=#1a73e8>作者：</font>** Yifei Li, Xiaohan Zheng, Wentao Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured knowledge fact checking aims to determine the truthfulness of natural language claims by reasoning over structured evidence. Recent program-generation approaches leverage large language models (LLMs) to generate executable graph reasoning programs, achieving strong performance on structured knowledge fact checking benchmarks. However, these methods remain limited by invalid relation generation, single-path reasoning that lacks self-correction, and biased evidence assessment that tends to overestimate supporting signals. We propose Dialectical Agentic Reasoning (DARE), a multi-agent framework that formulates structured knowledge fact checking as an iterative retrieve-reason-reflect process. DARE integrates relation-grounded evidence retrieval to constrain reasoning to valid structures, dialectical bidirectional verification to evaluate evidence from both supporting and refuting perspectives, and confidence-driven meta-reflection to dynamically determine whether additional evidence exploration is necessary. Extensive experiments demonstrate the effectiveness of DARE in structured knowledge fact checking, with an 8B backbone achieving 88.12% accuracy and matching or surpassing GPT-4o-based program-generation baselines, which attests to the efficacy of dialectical agentic reasoning in eliciting the latent reasoning capabilities of LLMs.

---


### 89. [Realtime-Venus: A full-duplex interaction system with asynchronous delegation](https://arxiv.org/abs/2609.13814)

**<font color=#1a73e8>作者：</font>** Ruixiang Zhao, Hualei Wang, Renhe Sun 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural interaction in digital and physical environments requires continuous perception and timely responses. Spoken dialogue relies on acoustic and linguistic cues, while video interaction also requires grounding the conversation in evolving visual context. We present Realtime-Venus, a proactive full-duplex interaction system with two separately trained 9B models: Realtime-Venus-Omni for audio-visual interaction and Realtime-Venus-Audio for spoken interaction. Each model serves as a complete conversational frontend, integrating continuous perception, conversational control, and native speech generation through a shared causal timeline for user inputs, model outputs, and delegation events.
A dual-loop runtime coordinates live interaction with background reasoning and tool execution. Foreground interaction continues while Realtime-Venus-Harness executes tasks asynchronously and returns results for integration into the ongoing dialogue.
Both models follow a common post-training recipe combining offline understanding, proactive full-duplex trajectories, and delegation workflows.
Among the evaluated online models, Realtime-Venus-Omni achieves the highest scores on six of eight video benchmarks, including StreamingBench (70.2%), OVO-Bench (64.7%), and Daily-Omni (81.3%). Across eight audio understanding and spoken question answering benchmarks, Realtime-Venus-Audio leads the compared models on MMAU (78.0%), MMAU-Pro (63.2%), Llama Questions (83.8%), and Speech CMMLU (67.8%), while matching the best VoiceBench AlpacaEval score of 4.81. On Full-Duplex-Bench v1.5, Realtime-Venus-Audio responds to 75% of user interruptions and achieves continuation rates of 97%, 88%, and 86% under backchannels, other-directed speech, and background speech, respectively, exceeding Gemini 3.1 Live and GPT-4o on all three continuation metrics.

---


### 90. [Beyond OCR Accuracy: Text-Centric VQA Under Image Degradation with Modular and End-to-End](https://arxiv.org/abs/2609.13815)

**<font color=#1a73e8>作者：</font>** Ritali Vatsi, Rachapudi Jagadeesh, Shruti Singh Baghel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-centric Visual Question Answering (VQA) requires reading and reasoning over text embedded in images, a task made substantially harder when images suffer from real-world degradation such as motion blur, low resolution, or compression artifacts. While modular OCR-based pipelines and end-to-end vision-language models are both widely used for this task, their comparative robustness under degraded conditions remains underexplored. We present an empirical study comparing two modular pipelines with SA-DBNet, a custom detector architecture combining ResNet-18 with self-attention spatial modeling and deformable convolutions against an end-to-end vision-language baseline, evaluated on 4013 degraded images with 7000 question-answer pairs. Fine-tuned modular pipelines achieve up to 57.50% exact-match accuracy versus 38.00% for the end-to-end baseline, with domain-specific fine-tuning yielding a gain of up to 29.50 percentage points. Critically, we find that conventional OCR error metrics like Character Error Rate and Word Error Rate are unreliable predictors of downstream VQA performance, as semantic reasoning can compensate for recognition failures when contextual cues are present. These findings highlight the importance of task-aware evaluation for text-centric VQA systems under realistic visual conditions. Codes are available here

---


### 91. [Exploring Automated Vulnerability Identification in JavaScript Code Using Large Language Models](https://arxiv.org/abs/2609.13816)

**<font color=#1a73e8>作者：</font>** Manit Kaushik, Ishir Bhardwaj, Pranav Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> JavaScript powers approximately 98.8% of all websites, making vulnerabilities in its code a significant security risk, yet existing detection approaches such as Static Application Security Testing (SAST) tools often fail to identify many real-world vulnerabilities when applied to isolated code snippets. This paper presents an empirical study of Large Language Model (LLM)-based vulnerability identification for JavaScript programs, evaluating three LLM families (Gemini 1.5 Flash, GPT-4o Mini, DeepSeek-R1-Distill-Llama-8B) across multiple prompting strategies (zero-shot, chain-of-thought, few-shot) and fine-tuning approaches on a dataset of 1,125 JavaScript code snippets spanning five Common Weakness Enumeration (CWE) categories: Injection (CWE-74), OS Command Injection (CWE-78), Cross-Site Scripting (CWE-79), SQL Injection (CWE-89), and Uncontrolled Resource Consumption (CWE-400). Our experiments show that LLMs substantially outperform traditional SAST tools on snippet-level vulnerability identification, with a fine-tuned Gemini 1.5 Flash model achieving 60% detection accuracy compared to near-zero performance from rule-based analyzers. We find that fine-tuning improves accuracy from 29% to 60%, Chain-of-Thought prompting benefits reasoning-capable models such as GPT-4o Mini, few-shot prompting is effective for polymorphic vulnerabilities such as Cross-Site Scripting, and performance varies across vulnerability categories, reaching up to 84% accuracy for structured vulnerabilities such as SQL Injection. These results indicate that LLMs provide a practical approach for automated vulnerability identification in JavaScript code, particularly when combined with task-aligned supervision, though they should complement rather than replace existing security analysis workflows due to limited recall and uneven performance across vulnerability types.

---


### 92. [When Consistency Does Not Mean Reliability: Evaluating Local LLM Judges Against Human Ratings](https://arxiv.org/abs/2609.13824)

**<font color=#1a73e8>作者：</font>** Aakash Kumar Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to evaluate the responses of other language models. This approach, known as LLM-as-a-Judge, is faster and cheaper than human evaluation. However, a judge may produce consistent scores without necessarily agreeing with human evaluators. In this work, we study this issue using two local open-weight LLM judges, LLaMA-3-8B and Qwen2.5-7B. We evaluate 300 responses generated by an instruction-tuned GPT-2 (124M) model for 100 questions covering five categories: factual knowledge, instruction following, mathematics, reasoning, and writing. Each response is scored by nine human annotators and is evaluated three times by each LLM judge using the same rubric. We compare the judge scores with the average human scores using Pearson correlation, Spearman correlation, mean absolute error (MAE), signed bias, and self-consistency. LLaMA-3-8B shows a Pearson correlation of 0.275 with human scores, while Qwen2.5-7B achieves 0.340. Their MAEs are 27.71 and 18.64, respectively. Despite this limited agreement, both judges show high self-consistency, with exact consistency rates of 97.3\% for LLaMA-3-8B and 92.3\% for Qwen2.5-7B. These results show that high self-consistency does not necessarily indicate high agreement with human judgments. Our findings highlight the need to evaluate both consistency and human alignment when using local LLMs as automatic judges.

---


### 93. [DiVA: Enabling Interactive Digital Life Simulation via Video Models](https://arxiv.org/abs/2609.13830)

**<font color=#1a73e8>作者：</font>** Cheng Chen, Hao Ouyang, Qiuyu Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DiVA, a deeply interactive digital life simulator pioneering a new paradigm for long-term, open-ended interactive experiences within digital character worlds. DiVA's architecture pairs a Multimodal Large Language Model (MLLM) as a router with a meticulously designed stacked video pipeline for seamless, multi-turn interactions with action and audio response. To maintain continuity and avoid degradation, we model generation as a three-part coupled system: waiting video, action video, and the transitions between them. These transitions are critically handled by our Anchored Video Continuation (AVC) module, which returns the character to stable states to prevent degradation. By encoding information from the preceding action video segment, AVC ensures smooth transitions, significantly reducing camera jitter and inconsistencies common in current video transition methods. This design also enables complex pose changes (e.g., sitting to standing) typically difficult for audio-driven models. These system designs together ensure high-fidelity identity, coherence, and dynamics for extended experiences. To validate our pipeline design, we comprehensively compare our system against alternatives by replacing our core generation module with mainstream long-video, continuation, and interpolation methods. We further analyze the necessity of the three-stage design, anchor-state selection, transition naturalness, spatial grounding, and the quality-latency trade-off, and we expand the comparison to additional long-form audio-driven avatar models. Results confirm DiVA is markedly superior in maintaining long-term visual quality and realism, validating its effectiveness as a sustainable, interactive simulation.

---


### 94. [Sweet Talkers: How Query Formulation Shapes Sycophancy in Romantic Relationship Advice](https://arxiv.org/abs/2609.13841)

**<font color=#1a73e8>作者：</font>** Helena Choi, Edric Castel Hao, Karl Bautista 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for emotional support and relationship advice, where a model's tendency to preserve a user's face can inadvertently reinforce harmful interpersonal behaviors. To systematically examine this risk, we developed the Romantic Relationship Advice-Seeking Prompts (RRASP) dataset of 2,400 prompts across five relationship themes and evaluated social sycophancy using the ELEPHANT framework on two consumer-facing models, GPT-5 Mini and Gemini 3 Flash. Contrary to our initial hypothesis, grammatical mood alone did not produce systematic differences in sycophantic behavior, suggesting that what a user implies matters more than how they phrase it. Instead, perspective-driven framing had a stronger influence, with gaps between original and flipped prompts widening in follow-up responses. Consistent increases in framing and moral sycophancy across turns indicate that models become more likely to accept a user's stated premises and affirm their ethical stance as a dialogue progresses. Notably, Gemini 3 Flash exhibited substantially smaller increases in moral sycophancy than GPT-5 Mini, suggesting it is more resistant to reinforcing ethically problematic positions across turns.

---


### 95. [Affinity-Aware Sharding for Delayed Tensor Parallelism](https://arxiv.org/abs/2609.13846)

**<font color=#1a73e8>作者：</font>** Eloi de Reynal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delayed Tensor Parallelism (DTP) removes the blocking all-reduce of tensor-parallel Transformer inference. Every device adds its own partial output to its residual stream (and broadcasts it) immediately, but only gathers (receives) the other devices' partials $\delta$ modules later. A TP to DTP change therefore amounts to a real architecture change, and dense Transformer models need to be retrained or distilled after adaptation. We show that DTP breaks the permutation symmetry of neurons inside FFNs and of KV heads inside attention modules, and that this symmetry breakage makes the sharding itself a modelling decision. We show that maximising the affinity between the KV heads and the FFN neurons co-located on a device, by permuting the dense model before sharding, speeds up the distillation or retraining process. The affinity is measured with a first-order approximation of the damage that losing a head's contribution does to each neuron's output, and the co-located affinity is maximised with a coordinate-ascent optimiser that alternates an exact balanced assignment of neurons with an exhaustive search over the KV head partitions. The whole procedure takes under two minutes on one GPU for Qwen3-0.6B and Danube3-500M. On these models, at $\delta=1$, the affinity-optimised layouts reach any distillation target in about half to two thirds of the steps needed by the naive contiguous layouts, over the whole 10k-step range we tested, and every optimised seed beats every contiguous seed and all but one of the sixteen random layouts. We also show that the co-located affinity score at initialisation predicts the KL to the base model after training, across seventeen layouts ranging from anti-optimised to optimised (Pearson $-0.81$ and $-0.89$).

---


### 96. [Measuring the Cost of Variety Conflation in Multilingual MT Evaluation: Adding Mozambican Xichangana, Nyanja and Sena to FLORES+](https://arxiv.org/abs/2609.13847)

**<font color=#1a73e8>作者：</font>** Felermino D. M. A. Ali, Delfina Lázaro Mateus, Manuel Valente Mangue  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we extend FLORES+ with Portuguese-source evaluation sets for three Mozambican Bantu varieties: Xichangana, Mozambican Nyanja, and Sena. We compare Xichangana with the existing Tsonga reference and Mozambican Nyanja with Chichewa, and evaluate NLLB-200, Google Translate, GPT, and a variant-aware NLLB model. Holding system output fixed reveals substantial reference sensitivity. On \textit{devtest}, changing only the reference from Tsonga to Xichangana reduces spBLEU by 13.10 points for NLLB-200 and 15.30 for Google. On matched Nyanja subsets, replacing Chichewa with Mozambican Nyanja produces smaller but consistent reductions of 3.03 and 6.10 spBLEU, respectively. Variant-aware fine-tuning reverses this pattern on the intended targets: relative to NLLB-200, it improves Xichangana by 7.04 spBLEU and Mozambican Nyanja by 5.33 on \textit{devtest}, while losing performance on the sibling references. GPT is competitive on Tsonga and Chichewa but substantially weaker on the Mozambican varieties. For Sena, the finetuned model reaches 12.64 spBLEU and 36.21 chrF++ on \textit{devtest}. These findings motivate variety-aware language identifiers, references, and reporting for cross-border languages or language dialects/variants. The data is publicly available on Hugging Face at this https URL

---


### 97. [UniCAR-RL: Seeing Better before Thinking Deeper in Visual Mathematics](https://arxiv.org/abs/2609.13849)

**<font color=#1a73e8>作者：</font>** Yuzhe Li, Hao Yan, Hao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) often struggle with complex mathematical visual reasoning primarily due to a lack of fine-grained perception, causing initial visual hallucinations to directly trigger cascading reasoning failures. In traditional end-to-end reinforcement learning (RL), sparse rewards fail to decouple perceptual hallucinations from logical missteps, hindering targeted perception optimization. Alternatively, fine-tuning with perception-enhanced CoT data incurs high costs and hallucinations. In this paper, we address these challenges by proposing UniCAR-RL, an annotation-free RL framework. By explicitly decoupling the optimization of perception and reasoning during the training process, it achieves isolation and optimization of both capabilities. Specifically, UniCAR-RL consists of three synergistic branches: 1) a Caption-RL branch that optimizes perception capabilities through verifier-guided reasoning validation; 2) a Reasoning-RL branch that performs logical reasoning based on a gold image description to halt cascading errors; 3) a QA-RL branch that retains native end-to-end alignment to ensure robust question-answering performance. Experiments show that UniCAR-RL substantially improves MLLMs' mathematical and visual reasoning using only raw short-answer data. Furthermore, it demonstrates strong generalization across diverse architectures and scales.

---


### 98. [ShopEase: A Generative AI-Based Multi-Agent Framework for Intelligent Enterprise Customer Support Using Hybrid Retrieval-Augmented Generation](https://arxiv.org/abs/2609.13856)

**<font color=#1a73e8>作者：</font>** Aakash Kumar Tiwari, Somesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise customer support systems must answer customer questions correctly, retrieve the right policy information, use customer context, and pass difficult cases to human agents when needed. This paper presents ShopEase, a Generative AI-based multi-agent framework for enterprise customer support. The system combines six components: Intent, CRM, Memory, Hybrid RAG, Escalation, and Supervisor, and uses LLaMA 3.2 running locally through Ollama for response generation. The retrieval module combines FAISS (dense retrieval) and BM25 (sparse retrieval), and six configurations are evaluated: BM25-only, FAISS-only, Fair RRF, Weighted RRF, RRF with Cross-Encoder, and Top-10 Hybrid with Cross-Encoder. Instead of using a fixed mapping between intent and policy, the policy category is decided directly from the retrieved documents. The system was evaluated on 2632 held-out customer queries across six categories: Refund, Return, Shipping, Cancellation, Damaged Product, and Unknown. FAISS-only achieved the highest accuracy of 85.37\% (2247 correct predictions), closely followed by Weighted RRF at 85.07\%. BM25-only achieved only 55.74\% accuracy. Adding cross-encoder reranking did not improve results: RRF with Cross-Encoder reached 83.24\%, and Top-10 Hybrid with Cross-Encoder reached 81.88\%, while also increasing response latency. Category-level analysis shows strong performance on Shipping, Cancellation, and Return, while Unknown queries remain the main source of errors. Statistical testing using McNemar's test shows no significant difference between FAISS-only and Weighted RRF, though both perform significantly better than Fair RRF and the cross-encoder configurations. Overall, dense retrieval gives the best accuracy on this dataset, and additional reranking adds processing time without improving classification performance.

---


### 99. [ClinAgent: A ReAct-Based Agent for Conversational Access to Clinical Trial Information](https://arxiv.org/abs/2609.13860)

**<font color=#1a73e8>作者：</font>** Antonino Vaccarella, Riccardo Cantini, Domenico Talia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Querying clinical trial registries remains a manual and error-prone process, requiring researchers to navigate large volumes of semi-structured data without support for natural language interaction or cross-source synthesis. To address this, we introduce ClinAgent, a conversational system based on agentic Retrieval-Augmented Generation (RAG) that enables clinicians and researchers to query clinical trial information in plain language and receive grounded, up-to-date responses across multi-turn interactions. The system centers on a Large Language Model (LLM) agent following the ReAct paradigm, which iteratively reasons over queries, selects among a set of integrated tools, and refines its actions based on intermediate outputs. These tools include a this http URL search interface, a PubMed module, and a Python-based analyzer operating on a locally cached structured dataset of clinical trials. We evaluate the system using a three-phase framework assessing operational effectiveness, planning quality, tool-use efficiency, and expert qualitative judgments, comparing three LLM backends: Gemini 3.0 Flash and two variants of DeepSeek V3.2 (thinking and non-thinking). Results reveal complementary strengths, with DeepSeek (thinking mode) excelling in planning quality, while Gemini achieves the highest overall performance and strongest expert ratings. Overall, our findings highlight the potential of agentic AI systems to improve the accessibility and synthesis of clinical trial information, supporting more efficient and user-centered biomedical research workflows.

---


### 100. [The Filter Metric is Safety-Critical: Phantom Advantages in Group-Relative RL under Shaped Rewards](https://arxiv.org/abs/2609.13866)

**<font color=#1a73e8>作者：</font>** Juntao Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative policy optimization (GRPO and descendants) can discard no-contrast rollout groups through dynamic sampling, while practical implementations expose a configurable filter metric. We identify and quantify a metric-predicate mismatch under composite shaped rewards. When filtering follows the shaped training score rather than the task outcome, all-fail groups retain nonzero within-group spread and pass the predicate; standard-deviation normalization then promotes shaping differences among failures to full-size phantom advantages. In a controlled GSM8K comparison (Qwen2.5-1.5B, LoRA), no filtering and shaped-score filtering end at EM 0.080 +/- 0.112 and 0.040 +/- 0.008, whereas binary-outcome filtering holds 0.754 +/- 0.005 across four runs per arm (three default-seed reruns and one seed-123 run; mean +/- sample SD). On verl's native recipe/dapo trainer, holding model, data, reward and trainer fixed and changing only the metric, the score arm requires no batch refill in any of 40 observed steps and ends at EM 0.160; the accuracy arm refills in 29/40 steps and ends at 0.763. Both use the same custom shaped-reward hook and unmodified trainer/filter code. Prior work established shaping-induced amplification and all-fail filtering; our contribution isolates the metric-predicate semantic mismatch and directly instruments native deletion/refill telemetry. Across tested positive coefficients lambda in {0.1, 0.3, 0.5}, unsafe arms collapse; exploratory one-run cells reproduce the failure at 1.5B/7B on MATH and under GSPO, while disabling standard-deviation normalization avoids the observed collapse. Filtering under a composite reward should use a task-outcome signal whose semantics are independent of shaping.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
