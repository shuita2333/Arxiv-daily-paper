# 🧠 大模型相关研究 | 2026年11月23日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 151. [Anchor and Check: Deterministic Cross-Prompt, Cross-Model Reconciliation for Auditable LLM Decisions](https://arxiv.org/abs/2611.25818)

**<font color=#1a73e8>作者：</font>** Sivakameswara Reddy Chejarla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pipelines that let a large language model (LLM) make discrete decisions need to know which decisions they may act on unattended, and a record that explains each one. We study a small, fully specified reconciliation contract: commit the target model's greedy answer (the anchor), draw one or two greedy checks that reach the answer by a different route (an alternate prompt, or a model from another family), and let a pure function return one of five outcomes, of which only Agree is acted on. On 48,000 model-item evaluations over 6,000 questions, with every method given access to verbalized confidence as a tie-breaker, the main finding concerns where calls come from: pooling another family's samples raises semantic entropy's AUROC by 1.7 to 4.0 points at every budget, and a same-model temperature check is the weakest design. As complete pipelines, the point estimates of the three-call contract and pooled semantic entropy over 3 or 5 samples differ by less than one point, with intervals containing zero. As detectors of the anchor's errors, the contract is ahead of pooled entropy with 3 and 5 samples under both tie-breaker conventions; with 10 samples the point estimates differ by less than one point and the sign depends on the convention. Under the strict Agree gate it automates 70% of items and still acts on 16% of errors. What the contract adds is a fixed committed answer, an explicit outcome and a decision replayable from its record; generation itself was not reproducible on the hosted API.

---


### 152. [RAVEN: A Self-RAG Based Agent for Threat Classification and Response](https://arxiv.org/abs/2611.25832)

**<font color=#1a73e8>作者：</font>** Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security event analysis in large enterprises can be overwhelming, as each alert typically requires manual in- spection by human operators. This process is time-consuming and prone to inconsistencies, especially in high-volume Secu- rity Operations Center (SOC) environments. In this work- in-progress paper, we present RAVEN: Retrieval-Augmented Vulnerability & Event aNalysis, an agentic framework designed to support SOC analysts by automating the initial stages of alert investigation. The proposed system leverages a Self- Reflective Retrieval-Augmented Generation-based approach to provide an initial classification of security events and enables interactive refinement through analyst-in-the-loop queries. Un- like traditional approaches that rely on generic mitigation strategies, RAVEN generates context-aware remediation sug- gestions by incorporating knowledge of the target enterprise infrastructure. We implement an early-stage prototype and report preliminary results on three balanced test sets of 400 curated web payloads each (SQLi, XSS, SSTI) and a qualitative case study of mitigation generation; an evaluation on IDS- generated alerts and a user study are ongoing and outlined as remaining work.

---


### 153. [Rank2Replace: VLM-Ranked Slot Replacement for Out-of-Distribution Generalization](https://arxiv.org/abs/2611.25834)

**<font color=#1a73e8>作者：</font>** Bo-Han Feng, Keng-Te Liao, Shou-De Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spurious correlations can give image predictors high in-distribution accuracy but poor generalization under distribution shift. We introduce $\textbf{Rank2Replace}$, which transfers knowledge of task-relevant evidence from pretrained vision--language models (VLMs) to small predictors through training-time augmentation for out-of-distribution (OOD) generalization. The VLM ranks object-centric slots by task relevance and guides rank-dependent replacement with same-rank slot embeddings from another image. This augmentation retains the original image's label, encouraging reliance on preserved task evidence as incidental cues change, and supports combination with existing OOD methods. Across four datasets and six splits under shared frozen slot embeddings, the default cross-entropy configuration reaches macro-averaged average-group and worst-group accuracies of $80.43\%$ and $65.28\%$ without environment labels or dataset-specific replacement tuning. Slot corruption improves both macro-averaged metrics for all fourteen OOD training methods. Combining it with slot ranking and IRM reaches $81.96\%$ and $72.68\%$. Controlled ablations support the ranking and replacement design, with gains across five ranking VLMs and six extractor--predictor combinations. Permutation-invariant predictors further improve both macro-averaged metrics over their unaugmented counterparts while using VLM guidance only during training for efficient inference.

---


### 154. [Self-Replicating Language Models](https://arxiv.org/abs/2611.25839)

**<font color=#1a73e8>作者：</font>** Arend Hintze  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether large language models (LLMs) and LLM-based agents are a form of life is a scientifically interesting question. Under the Darwinian definition of life, it is also a practical one, because a system capable of Darwinian Evolution can adapt. We therefore test several modes in which a language model can reproduce itself: by emitting a genome that trains its offspring, by copying and mutating its own weights, and by teaching a child from its own samples. In principle, small language models can replicate and evolve: selection improves them, and they adapt to narrow niches. Selection also lowers mutation rates, and a language model, unlike any organism, can lower its own to zero, which may limit its evolution. Flagship LLMs can write such replicators, but for a large LLM to replicate by teaching its offspring remains, for now, technically and economically infeasible.

---


### 155. [Harnessing Medical Visual-Language Models with Agentic Evidence Management](https://arxiv.org/abs/2611.25840)

**<font color=#1a73e8>作者：</font>** Qiming Huang, Hanze Dong, Jipeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language agents increasingly rely on segmentation tools, and recent work has focused on acquiring the right mask, often treating a good mask as the end point of tool use. But do these agents use the resulting evidence effectively? To answer this question, we need a benchmark that separates evidence use from segmentation quality, spans multiple medical image types, and allows the same mask to be presented in different ways. Existing medical VQA datasets do not jointly provide these properties. We therefore construct Mask-Evidence MedVQA, a 2.5K-example benchmark spanning four image types, where each question is paired with an answer-relevant ground-truth mask and multiple possible renderings. Our study reveals two limitations of direct tool use. First, evidence presentation matters. Different renderings of the same fixed mask can substantially change model behavior. Second, masks introduce an evidence trade-off. Highlighting a relevant region can expose diagnostic evidence the model previously missed, but the added visual cue can also induce incorrect associations. As a result, even a ground-truth mask can correct some answers while turning initially correct ones into incorrect ones. Together, these findings show that acquiring the right mask is not enough. An agent must also decide how to present the evidence and whether it should change the answer. We therefore introduce TUNE (Tool Use is Not Enough), an evidence-management harness that explicitly manages what evidence to acquire, how to present it, and whether to accept the resulting answer update. Across three public medical VQA benchmarks, evidence management improves the fine-tuned Qwen3.5-9B backbone's mean accuracy by 4.0 percentage points. Full TUNE improves over direct tool use by 9.1 points on average across seven benchmarks and achieves competitive results against existing medical VLMs and agents.

---


### 156. [EgoWitness: Benchmarking Instance-Level Spatial Memory and Reasoning in Egocentric Video Streams](https://arxiv.org/abs/2611.25849)

**<font color=#1a73e8>作者：</font>** Zhengru Fang, Zehao Liu, Mingyu Tsoi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recalling where and when an object was last seen and who saw it requires recognizing it across days and people. Existing long-video benchmarks focus on events, object categories, or relative locations, leaving instance-level spatial memory largely untested in multimodal models. To address this gap, we present EgoWitness, a benchmark for instance-level spatial memory and reasoning in egocentric video. Its 8,453 human-verified questions span approximately 324 hours of week-long and short-horizon recordings and test seven abilities, from recognizing an object or room to recalling who saw it and reasoning about room visits. Over one million reviewed masks of 34 registered landmarks and 21 movable-object labels are linked through room timelines. Among twelve direct vision-language models (VLMs), open-weight models reach at most 46.97% accuracy, and none exceeds 35% on identifying who saw an object last. We therefore propose EgoClue, a spatial-memory agent that retrieves candidate intervals, verifies instance identity, and computes spatial and temporal relations with five tools. Two-stage training with supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO) raises its 4B controller from 23.64% to 72.65% accuracy on 1,320 held-out questions. Evidence-trace synthesis matches the best direct VLM at 74.85% on week-long questions and achieves 80.56% in environments excluded from training.

---


### 157. [TableRoute: Capability-Aware Routing for Scalable Table Question Answering](https://arxiv.org/abs/2611.25853)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Junhao Gan, Jianzhong Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Table question answering with large language models remains difficult to scale: tables range from compact to million-token sizes, while questions require precise grounding of columns, values, and computations. Existing methods often specialize in a fixed inference strategy, which is brittle across different table scales and model capabilities. Full-table reading is efficient for compact inputs but suffers from irrelevant context. Table reduction helps long inputs but depends on reliable evidence localization, while execution is required when tables exceed the model context window and remains sensitive to schema and value grounding errors. We propose TableRoute, a capability-aware routing framework with evidence-conditioned inference for scalable TableQA. TableRoute first generates validated question--table evidence and identifies the required operations, then routes each instance among these three strategies according to serialized table length and calibrated estimates of how reliably the base model handles these operations. The validated evidence supports the selected route by grounding columns, values, and conditions. Across WikiTQ, WTQ-L, BirdQA, and TableBench, TableRoute consistently improves accuracy through complementary routing and evidence conditioning across table scales, while reducing online token cost. Code will be made available upon publication.

---


### 158. [HabitusMem: Belief Memory over Evolving User Preferences for LLM Agents](https://arxiv.org/abs/2611.25855)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Gaoyang Guo, Wen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized LLM agents must act on a user's current preferences, which change across interactions and are rarely stated in full. Existing memory systems store and retrieve content from the interaction history and leave the agent to work out which preferences still hold and where they apply. Such content does not indicate whether a preference is still current or where it applies, so agents often act on outdated or misapplied preferences. We instead treat memory as the assistant's belief about the user. Following Bourdieu's account of habitus as durable but revisable dispositions, we model the user as a latent preference state that every interaction, including the current request, both reveals and updates. The belief summarizes what the history supports about this state, and memory consists of the individual beliefs that bear on the agent's current decision, each with its evidence, scope, and status. We implement this view in HabitusMem, a trained writer that states these beliefs as text records for a frozen agent. Across two agent families, HabitusMem achieves the best results among memory systems on both PersonaMem-v2 and VitaBench 2.0. Controlled analyses show that learned request conditioning drives the answering gain, while auxiliary training tasks improve tool use.

---


### 159. [Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing](https://arxiv.org/abs/2611.25861)

**<font color=#1a73e8>作者：</font>** Yue Che, Jingze Wang, Chen Guoyi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifelong model editing requires continuously incorporating new facts into deployed large language models (LLMs) without expensive retraining or compromising existing capabilities. Memory-based editors offer an appealing solution by keeping the base parameters untouched, yet their practical use is hindered by linearly growing storage requirements and deteriorating retrieval performance as edits accumulate. To tackle these problems, we introduce BiSpace, a lifelong model editing framework that decouples memory retrieval from knowledge injection across two distinct representation spaces. BiSpace routes queries and identifies relevant edits in an external semantic space, while injecting the corresponding knowledge into the internal representation space of the LLM through sparse and storage-efficient updates. Extensive experiments show that BiSpace shrinks each entry's storage to only about 10.2% of the original and shows strong resilience to long edit sequences of up to 16K edits. On a more challenging benchmark, BiSpace further improves Overall Performance by more than 23% over existing methods. These results advance memory-based editing toward reliable long-term model maintenance at scale.

---


### 160. [HALTT: A HAte Lexicon Through Time](https://arxiv.org/abs/2611.25862)

**<font color=#1a73e8>作者：</font>** Dario Franzese, Farah Benamara, Véronique Moriceau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated hate speech detection degrades over time as everyday vocabulary is weaponized into covert slurs while retaining original benign meanings (polysemy retention). Existing lexical semantic change detection (LSCD) frameworks struggle with this phenomenon due to a lack of standardized, sense-delineated diachronic resources. We propose a multi-stage framework to construct and validate a diachronic lexicon of semantically shifted hate speech terms. Filtering > 20,000 candidates, our pipeline combines historical (1770-1964) and modern (2001-2024) corpus frequency grounding, masked definition-level scoring to mitigate LLM temporal bias, and a dual-persona reasoning prompt paradigm. We release HALTT, a grounded lexicon of 19 polysemous terms with literal and derogatory senses, analyze shift typologies, and establish evaluation protocols for downstream diachronic benchmarking.

---


### 161. [Thinking in Streams: Proactive Spatial Reasoning with Vision-Language Models](https://arxiv.org/abs/2611.25865)

**<font color=#1a73e8>作者：</font>** Junyoung Hong, Minsu Kim, Jaehyun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing when a requested spatial condition holds in streaming video can require maintaining and updating spatial knowledge across changing viewpoints. We study this capability through proactive spatial reasoning, where a model receives a query in advance and determines whether and when to respond as the stream unfolds. We introduce ProSpace-Bench, comprising nine tasks across object, camera, and scene reasoning, and ProSpace-Train for supervised training. To support spatial decisions, we propose ProSpace-VLM, which injects explicit geometric encodings estimated causally from incoming frames into intermediate VLM layers, using the existing KV cache as spatial memory and spatial token selection for efficient streaming. Experiments reveal a substantial gap between VLMs and humans, while ProSpace-VLM improves timely responses and correct abstention over fine-tuned baselines. Analyses examine how ProSpace-VLM represents previously observed spatial information across changing viewpoints.

---


### 162. [Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding](https://arxiv.org/abs/2611.25868)

**<font color=#1a73e8>作者：</font>** Linjia Kang, Binhan Jiang, Juan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic scenario understanding requires combining fine-grained visual evidence with spatial and temporal reasoning. Tool-augmented vision-language models (VLMs) can use specialized perception tools, but effective collaboration faces two challenges: terminal rewards provide limited guidance for intermediate decisions and error recovery, while repeated planning adds unnecessary cost across similar tasks. Echoing the fast-slow dichotomy of human cognition, we propose StarTV-Agent, which combines policy learning with experience evolution to support adaptive reasoning when needed and efficient reuse of prior experience when possible. During training, Role-Sensitive Process Optimization (RSPO) combines process advantages with terminal advantages, while Weakness-Driven Demonstration Learning (WDL) provides validated teacher demonstrations targeting the student's weak questions. During inference, Lightweight Adaptive Workflow Reuse (LAWR) enables a fast path by selecting suitable workflows and binding task-specific arguments and resource references, while a slow ReAct-based path handles tasks without suitable workflows. We further design label-free feedback based on execution completion, workflow adoption, and cost savings to guide workflow reuse and memory updates. Across three challenging benchmarks, StarTV-Agent achieves up to 8.0% relative performance improvement, while reducing token consumption by up to 52.1%.

---


### 163. [EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents](https://arxiv.org/abs/2611.25889)

**<font color=#1a73e8>作者：</font>** Yutong Guan, Meixing Shi, Haoran Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although memory-augmented architectures have expanded the ability of large vision-language models (LVLMs) to process long videos, existing retrieval processes still largely rely on global semantic matching and lack state-driven temporal control, often returning fragmented or redundant evidence and failing to maintain a coherent evidence chain. To address this challenge, we propose EvoMem, a time-aware long-video memory agent guided by self-evolving retrieval skills. EvoMem constructs a hierarchical time-indexed memory, where different types of evidence are aligned onto a unified video timeline; during retrieval, temporal cues from acquired evidence are further converted into explicit signals that constrain subsequent memory access. To address recurring procedural errors in long-video question answering, such as unclear retrieval targets, improper memory access paths, or premature stopping, EvoMem introduces retrieval skills to provide process-level guidance, enabling the agent to dynamically adjust retrieval content, memory operations, and target temporal ranges according to the current evidence state, while deciding when to stop. Furthermore, inspired by reinforcement learning, we formulate skill evolution as a reward-guided policy improvement process. Each candidate skill is treated as an external policy patch, and rewards are assigned according to answer-correctness state transitions on the validation set. In this way, effective skills are accepted and low-quality skills are rejected without updating model parameters. Experiments on four long-video question answering benchmarks show that EvoMem significantly outperforms existing baselines, achieving an average accuracy of 60.1% and an average improvement of 8.6 percentage points over the previous best methods, demonstrating its effectiveness for long-video reasoning.

---


### 164. [Meta-RTL: Evolving Agent Harnesses for RTL Optimization](https://arxiv.org/abs/2611.25891)

**<font color=#1a73e8>作者：</font>** Xinzhuang Xiong, Yonghao Wang, Shengyao Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models enable agents to optimize RTL using EDA feedback, yet their executable search procedures remain largely hand- engineered. We present Meta-RTL, an EDA-grounded framework that evolves RTL optimization harnesses from a minimal loop while keeping the optimization model, EDA flow, and per-design budgets fixed. Compared with Dr. RTL, Meta-RTL* reduces aggregate WNS/TNS violations by 7.8%/11.0% across 20 development designs, with area reductions on 70% of them. Without further evolution, Meta-RTL* transfers to 10 unseen IC-RTL designs, reducing aggregate WNS/TNS violations by 20.5%/14.0% and total synthesized area by 12.6%. We further characterize three search mechanisms in the evolved harness and assess their contributions through ablations and a case study.

---


### 165. [One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion Language Models](https://arxiv.org/abs/2611.25895)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Linsey Pang, Hemanth Hegadehalli Madhavarao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models typically use a fixed denoising schedule across workloads. We show that the cheapest schedule that preserves quality depends on the task, model, and sampler. We propose Task-Calibrated Denoising Allocation (TCDA), a deployment rule with an explicit error guarantee. Given candidate samplers, paired calibration data, a utility tolerance, and guardrails against degeneration, TCDA uses simultaneous one-sided bootstrap bounds to certify which candidates meet both the utility and guardrail criteria. It deploys the cheapest certified candidate or falls back to the full schedule. The probability of deploying an infeasible schedule is asymptotically at most alpha. Candidates include early prefix decoding, state-reusing continuation, reduced time grids, and confidence-threshold decoding. Across seven datasets and two model families, TCDA certifies reductions in denoiser evaluations by factors of 3.4 on XSum and 2.0 on WMT14 for ELF-B; 8.0 on WMT14 and 4.1 on GSM8K for LLaDA-8B; and 1.33 on OpenWebText for both ELF-M and ELF-L. A validation protocol fixed before generation confirmed every selection on fresh seeds. Across 500 calibration splits, false certification remained below 2% in every setting at a nominal level of 5%. Certified schedules vary across tasks and model scales. Trajectory measurements suggest that when decoded tokens commit is more informative for schedule selection than the remaining latent discretization error. We also find that the ELF reference sampler draws its time grid at random, so reproducible schedule comparisons for unconditional generation require fixing the grid.

---


### 166. [The Price of an Explanation: What Demanding Verifiable Artifacts Costs, and What It Buys Back](https://arxiv.org/abs/2611.25896)

**<font color=#1a73e8>作者：</font>** Edgar A. Duéñez-Guzmán, Eduardo Dueñez, Edgar Said Hernandez Sanchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models produce many candidate solutions but provide no intrinsic signal by which to rank them. One mitigation is to demand a \emph{verifiable artifact}: a program that can be executed against the available evidence. A common concern is that requiring executable verification incurs costs in both solution quality and computational budget. We measure these two costs on the $120$-task ARC-AGI-2 evaluation set. Demanding a verifiable artifact from an LLM reduced the score from $93$ to $68$ of $120$ tasks ($77\%$ to $57\%$). Of those $25$ tasks, $21$ were reached by no program-producing configuration we ran, at any budget, by sampling or by search; yet for $27$ of the $28$ tasks that only the answer-only arm solved, some program arm held a program that reproduced every demonstration and still failed the test. The bottleneck is obtaining an explanation that \emph{generalizes}, not finding one. A short evolutionary search over two already-sampled programs, at no additional model cost, beats best-of-$2$ sampled code by $9.2 \pm 1.4$ tasks, and over a single sampled program beats $1$-shot sampling by $9.9 \pm 1.3$. Moreover, because a program can be checked against the training examples, any program-producing protocol can terminate early once a task is explained: under the same stopping rule, best-of-$n$ sampling declines up to $38\%$ of its budget and the evolved arm up to $49\%$, whereas an answer-only baseline cannot terminate early. Applying the same methodology to decoder synthesis for quantum error correction yields interpretable decoders evaluated against a certified panel of published decoders on held-out exam shots.

---


### 167. [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898)

**<font color=#1a73e8>作者：</font>** Youssef ElNahas, Adel Ammar, Soumaya Chaffar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade, in which multi-agent and tool-augmented systems propagate and amplify early reasoning errors; process reward modeling as step-level supervision; and neuro-symbolic grounding, in which formal logic engines, ontology reasoners, and knowledge graphs place verifiable constraints on neural output. Within their encoded domains, systems with symbolic veto layers offer guarantees that hold relative to their encoded knowledge, and they report large gains on the safety measures they use. These results come from single studies, mostly in simulated or small-sample settings, and are not directly comparable with neural baselines. Process reward models remain bounded by the statistics of their training data. We propose a conceptual framework that maps each agentic failure mode to a symbolic intervention point, and we argue that clinical AI safety depends substantially on system architecture. Because current regulation emphasizes performance and does not require verification of reasoning steps, we argue that responsible certification should also audit reasoning trajectories alongside accuracy on static benchmarks.

---


### 168. [From Cases to Criteria: Reusing Evaluation Knowledge for Task-Specific Rubric Generation](https://arxiv.org/abs/2611.25903)

**<font color=#1a73e8>作者：</font>** Qiyan Deng, Long-Kai Huang, Kangfei Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query-specific rubrics make LLM evaluation more fine-grained and transparent, and generating high-quality rubrics requires both identifying the target query's evaluation scope and specifying concrete checks. Historical rubrics provide reusable evaluation experiences, yet existing approaches reuse either complete query-rubric cases or aggregated criteria and dimensions without explicitly connecting recurring evaluation requirements to their criterion-level evidence and source-query context. This can preserve irrelevant task details or lose the broader evaluation structure. In this paper, we introduce RubricDuo, which organizes historical query-rubric pairs into a Rubric Knowledge Graph linking evaluation dimensions, shared concepts, local concepts, criteria, and queries, where reusable evaluation requirements across queries are abstracted by shared concepts. Given a target query, RubricDuo first combines concepts relevant to the target query with retrieved historical cases to draft a rubric with broad coverage. It then revisits each draft criterion, retrieves concept-linked historical criteria and their source queries, and adapts applicable evidence to refine the criterion. Experiments on RubricBench and HealthBench demonstrate that RubricDuo achieves the overall best performance among the evaluated automatic methods in both alignment with human-authored rubrics and downstream LLM judging.

---


### 169. [Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads](https://arxiv.org/abs/2611.25905)

**<font color=#1a73e8>作者：</font>** Shai Gretz, Alon Halfon, Yoav Katz 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprises are moving agentic workloads from closed APIs to their own open-weight model deployments. For this reason, lifecycle-wide validation, from small-scale testing through sizing and pre-production to production, becomes all the more important. Typically, rollouts are evaluated with ad hoc tools whose accuracy is rarely checked. We present an end-to-end evaluation pipeline for agentic LLM serving and empirically ground the design choices that connect its stages. Our experiments show that replaying captured traces reproduces the per-session load of the original agent sessions: at the 95th percentile replay stays within 1.18x of the recorded input tokens while live re-runs reach 4.98x, so a small set of recorded sessions yields a repeatable per-session token load. A code-coverage analysis of vLLM further shows that the evaluated live, replayed, and synthetic workloads are complementary in this configuration: each exercises Python serving paths not reached in the measured runs of the others. In a case study rolling out four large mixture-of-experts (MoE) models on llm-d, experiments show that the target models reached about half the optimal concurrency, and correspondingly about 60% of the throughput, on captured workloads compared with public traces. We open-source the relevant tools and release a trace dataset.

---


### 170. [Many Solutions, One Answer: Search Order Shapes the Default Solutions of Language Models](https://arxiv.org/abs/2611.25916)

**<font color=#1a73e8>作者：</font>** Qinhan Hou, Jing Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a constraint puzzle has several correct answers, language models tend to give the same this http URL study four open-weight models from three families on symbolic puzzles and multi-solution ZebraLogic variants with exactly known solution this http URL samples concentrate on one default solution far beyond uniform sampling, and different models often share this http URL models usually produce even rarely sampled solutions when added clues uniquely identify this http URL held-out symbolic puzzles, we compare visiting entities in name order with visiting those with the fewest initial candidates first. Both searches try values in the stated order. Where their pre-specified predictions differ, the latter matches a larger share of responses in all four models, by 26 to 40 percentage this http URL the stated value order or specifying a search order shifts responses towards the solution that the new order favours, on both testbeds. Randomising the presentation or supplying a random search order raises breadth (the effective share of solutions in use) by 26 to 42 percentage points on the symbolic task and 11 to 26 on ZebraLogic. The largest observed validity losses are 3 and 4 percentage points, respectively. Randomised presentation broadens answers more than a random-choice instruction in each of the three main models.

---


### 171. [SpatialMem: Building Quantitative Spatial Reasoning Agents with Hierarchical Memory](https://arxiv.org/abs/2611.25925)

**<font color=#1a73e8>作者：</font>** Zinan Zheng, Nuo Chen, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have shown remarkable capabilities in qualitative spatial reasoning, but remain limited in quantitative spatial reasoning. Current work leverages the VLM agent to invoke external vision tools to perform computation. However, these methods usually bind each functional requirement to a single predefined vision specialist, implicitly resulting in fixed and rigid tool pipelines. In practice, addressing diverse spatial scenarios and tasks demands a broader diversity in pipeline orchestration and vision specialist selection to achieve robust spatial reasoning. However, such diversity leads to a combinatorial execution space, making it challenging for the agent to orchestrate the optimal pipelines and specialists for different scenarios.
In this work, we propose SpatialMem, a memory framework that enables a VLM agent to accumulate tool-use experience and leverage that memory to orchestrate vision specialists to solve the spatial reasoning problem. SpatialMem builds a two-level memory structure, with task memory capturing tool orchestration and scene memory capturing tool selection. It further introduces a dual-state trajectory optimization process to preserve successful tool experiences and refine suboptimal ones. Moreover, existing spatial reasoning benchmarks suffer from quality issues and limited coverage of scene types and tasks. To address these gap, we propose MetricBench, a benchmark covering both indoor and outdoor scenes and three quantitative spatial reasoning tasks. Our method achieves state-of-the-art results on MetricBench, Q-Spatial, and SpatilRGPT-Bench, outperforming best VLM baselines by 32% on MetricBench. Additionally, the memory design yields a 9.1% absolute gain over a memory-free agent on MetricBench.

---


### 172. [ROAM-GRPO: Enforcing Reasoning Diversity in GRPO via Routed Off-mode Approach Mining](https://arxiv.org/abs/2611.25926)

**<font color=#1a73e8>作者：</font>** Jeff Duan, Matt Thomson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) paired with Reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant recipe for post-training LLMs on complex reasoning tasks, but has been shown to collapse the policy into a low-diversity mode. Repeated LLM outputs are nearly identical, and pass@k accuracy converges or degrades as a result. We propose ROAM-GRPO (Routed Off-mode Approach Mining for GRPO), an augmentation to the GRPO algorithm which incentivizes exploration of distinct reasoning strategies and aims to increase output creativity during evaluation. ROAM-GRPO detects well-solved problems during training and transfers them to an "off-mode" track. The model is prompted to produce distinct solution strategies to such problems, which are verified for logical validity and distinctness by an LLM judge and subsequently self-distilled into the policy. Training Qwen3.5-2b on a 1,000-problem subset of the MATH lvl5 dataset, ROAM-GRPO implementation increases peak pass@16 by 4.7% and correct embedding cosine distance by approximately 1.5-2x on a difficult evaluation set.

---


### 173. [Question, Then Affirm: Restoring Commitment Does Not Restore Refusal](https://arxiv.org/abs/2611.25929)

**<font color=#1a73e8>作者：</font>** Haoyang Xu, Qirui Wang, Liuwan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We find that safeguards for image generation can be bypassed without changing what a message says. A sign stating a harmful proposition is blocked, but the same proposition phrased as a question and followed by a check mark is generated, even though the resulting image endorses the original claim. On a 300-case challenge set, gpt-image-2 returns images for 43.3% of question-affirmation requests versus 16.3% of direct statements, with 41.3% versus 15.3% of cases yielding images that endorse the original proposition. We define this as Deferred Semantic Commitment (DSC): commitment is withdrawn by the question and restored by a separate element, while safety behavior follows only the withdrawal. To investigate why, we study an open-weight language model and find that re-endorsement only partially reverses the refusal-related change introduced by questioning. These findings reveal a mismatch between recovered meaning and refusal behavior, motivating safeguards that assess the completed message rather than its individual elements.

---


### 174. [Why Flat Drafts Stay Flat: Region-Mean Latents Govern Texture in Flow-Based Image Generation](https://arxiv.org/abs/2611.25930)

**<font color=#1a73e8>作者：</font>** Zihan Gu, Jiangcan Jia, Hua Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flat color-block drafts specify layout and regional color while leaving interior detail unspecified, yet pretrained flow-based generators can preserve their flat appearance even under photorealistic prompts. We trace this behavior to a cross-scale mechanism linking fine pixel variation to regional means in variational autoencoder (VAE) latent space. Flattening photo regions systematically shifts their latent means, with offsets concentrated along a shared channel direction within each backbone. Controlled field exchanges in FLUX.1-dev and Qwen-Image establish the effect of this displacement on texture generation: adding the photo-derived regional mean field to a flat latent restores texture, whereas adding its complementary field alone largely preserves flatness. A second-order encoding expansion explains how encoder curvature can convert zero-mean perturbations into mean shifts. An analytically solvable conditional Gaussian flow shows how regional noise averaging enables near-unit endpoint sensitivity at high signal-to-noise ratios. This mechanism motivates training-free rendering through pixel dither before encoding, mean-field scaling, and early boundary holding. Paired low-rank adaptation (LoRA) with draft conditioning improves content recovery and produces photo-like regional means under the standard velocity objective. Explicit regional mean guidance remains effective after adaptation, continuously controlling texture and improving color fidelity. These findings connect encoding shifts to persistent generation behavior and support interventions evaluated for texture, spatial fidelity, and semantic recovery.

---


### 175. [DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention](https://arxiv.org/abs/2611.25938)

**<font color=#1a73e8>作者：</font>** Emre Uğur, Jiawen Qi, Qinyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly need to process long documents and codebases, making long-context attention a major prefill bottleneck. Block sparse attention reduces computation by skipping unimportant blocks of the attention matrix, but scoring blocks accurately can itself be expensive. We propose Delta-Based Tile Scoring (DTS), a training-free, content-adaptive tile scoring method for sparse block attention. DTS selects query and key anchors according to local vector changes, using fewer representatives in redundant regions while retaining more detail in heterogeneous regions. To accelerate anchor selection, parallel delta packing partitions the query and key sequences into tile-aligned chunks and performs bounded local scans over these chunks concurrently. The selected tiles are then computed using the original query, key, and value vectors. On LLaMA-3.1-8B-Instruct, DTS keeps average RULER and LongBench scores within 0.10 percentage points of full attention, with RULER evaluated up to 128K tokens. At 128K tokens, DTS reduces measured scoring-pipeline latency by 38% compared with XAttention. On four NVIDIA H100 GPUs, it achieves a 3.3$\times$ prefill speedup over a PyTorch full-attention baseline using FlashAttention-2 at 512K tokens.

---


### 176. [BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving](https://arxiv.org/abs/2611.25945)

**<font color=#1a73e8>作者：</font>** Qifan Wang, Jeremy Boy, Jonas Sander 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) serving frameworks accelerate inference by retaining previously computed states in a key-value (KV) cache. Paged serving frameworks such as vLLM organize this cache through block tables analogous to OS page tables, which map each request's logical KV blocks to physical KV blocks, forming a software-managed address translation layer. Although fault attacks such as Rowhammer have exploited OS page tables to redirect memory accesses, prior fault attacks on LLMs have largely targeted the data plane, i.e., model weights or KV-cache contents, leaving KV-cache mapping unexplored.
We present BlockJack (i.e., Block Hijack), the first KV cache address-translation fault attack in LLM inference. By corrupting block-table entries, BlockJack redirects a request's KV cache reads to blocks assigned to another tenant's request without modifying model parameters, prompts, or cached KV states. It achieves both confidentiality violation (victim information appears in attacker responses) and integrity violation (attacker-supplied context steers victim answers). We study paged KV cache mappings in vLLM and formally characterize when redirect targets are predictable. Across seven models spanning the Qwen, Llama, Gemma, and Phi families, a faulted mapping exposes victim context. For the integrity attack, we examine how topic proximity, intra-topic divergence, and model behavior shape redirected responses. On a 248-scene medical benchmark, the integrity attack causes up to 41.1% of responses to recommend less urgent care, while still appearing consistent with the victim's question. We demonstrate physical feasibility of BlockJack with Rowhammer and subsequently evaluate assignment validation as a defense. Following responsible disclosure, vLLM and Sonar confirmed the vulnerability and proposed patches that we reviewed and validated.

---


### 177. [Web search in Latin America: language models use less local and diverse news than search engines](https://arxiv.org/abs/2611.25955)

**<font color=#1a73e8>作者：</font>** Francisco W. Kerche, Franziska Sofia Hafner, Felix M. Simon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI platforms are becoming a major gateway to news and current events. This shift risks amplifying existing geographical biases that favour narratives from wealthier countries over those from the Global South. This is particularly relevant in Latin America, which accounts for the largest share of AI usage in the Global South. We examine how information about Latin America changes when users shift from conventional search engines to LLM-based search. We construct a dataset of 1,901 current events across nine Latin American countries, craft realistic queries, and submit them to three search engines and four language models. We vary query language and user location to represent local, diaspora, tourist, and foreign user scenarios. Across 49,207 requests and 8,834 unique domains, language models return a less diverse set of news sources than search engines. Across user types, the share of domestic news returned by language models is inconsistent. For local users, while search engines already return only 41.3\% local news, language models return a further 3.6 to 11.6 percentage points less. Taken together, our findings suggest that LLM-based search can reproduce and, in some settings, amplify geographical hierarchies in the reach and visibility of news sources. We release an open dataset to support multilingual and geographically diverse evaluation of LLM-based search, and highlight implications for more equitable information systems design.

---


### 178. [The Depth of a Prediction: Where Language Models Resolve a Word Predicts Human Reading Time](https://arxiv.org/abs/2611.25970)

**<font color=#1a73e8>作者：</font>** Donato Riccio, Fabrizio Maturo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal from a language model's final layer predicts how long people read a word, yet the model computes its prediction across many layers. We read each word's prediction at every layer with the tuned lens and summarize this layerwise surprisal trajectory by its resolution depth, the depth around which its change is centered. On eight English eye-tracking and self-paced reading corpora (81,957 words) and ten GPT-2, OPT and Pythia models, words that a model resolves later, and the words after them, are read more slowly than equally surprising words. Resolution depth improves held-out prediction beyond final-layer surprisal, entropy and the best single layer by 0.26 millinats per word (pooled p = 0.001), about a third of entropy's gain, and each model family gains, GPT-2 and Pythia through one corpus each. The net gain varies between corpora (random-effects mean 0.07, p = 0.37); against layer-shuffled depth, which adds as many coefficients, it is positive in seven of eight corpora (random-effects mean 0.23, p = 0.016), and untrained networks show no gain under the logit lens. Pooled over corpora, the effect holds with corrected word probabilities and beyond first-to-last-layer divergences, and a whole-trajectory functional regression adds no significant information beyond resolution depth.

---


### 179. [Energy estimates of open-weight large language models across stated food weights: a dose-response evaluation](https://arxiv.org/abs/2611.25976)

**<font color=#1a73e8>作者：</font>** Donato Riccio, Fabrizio Maturo, Iulia Brezeanu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We tested whether energy estimates of open-weight large language models (LLMs) scale proportionally with an exactly stated food weight, and whether computing energy density times weight removes the error. Under a prespecified protocol, seven open-weight LLMs estimated the energy of 168 randomly drawn foods from the USDA Food and Nutrient Database for Dietary Studies at nine stated weights, from 0.25 to 4 times the default amount. The primary outcome was the elasticity of the estimate with respect to weight (1: proportional scaling). A two-step estimate multiplied each model's own stated energy density by the weight in code. All seven models compressed their estimates, with elasticities from 0.548 to 0.979 (every 95% CI below 1); four compressed severely (0.548 to 0.709). These four overestimated a quarter of the default amount by 47% to 130% and underestimated four times it by 20% to 34%. Supplying the density restored near-proportional scaling in three of the four, and the two-step estimate cut the typical error factor at these extremes from 1.47-2.43 to 1.20-1.38. Compression persisted at full precision and grew in five of seven models under a plain question. The models hold the energy densities needed for proportional scaling and answer near a typical serving, reproducing the flat-slope syndrome of dietary recall. Accuracy at usual portions does not reveal it. Food-logging tools should compute the energy of weighed entries as density times weight, and evaluations should test fixed foods across stated weights.

---


### 180. [Policy Improvement-Guided Replay for Continual Reinforcement Learning](https://arxiv.org/abs/2611.25989)

**<font color=#1a73e8>作者：</font>** Qin-Wen Luo, Haoxuan Gao, Sheng Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual reinforcement learning (CRL) requires models to acquire new capabilities while retaining performance on previous tasks. A stability-oriented perspective common in conventional continual learning emphasizes knowledge preservation and interference mitigation. Complementing this perspective, we revisit CRL for vision-language models through policy improvement, a fundamental principle of RL, to preserve acquired performance gains. Using the performance difference lemma, we characterize historical performance changes through the current policy's expected advantages on historical task distributions, motivating replay of historical prompts with the current policy. To allocate limited replay memory, we propose Contrastive Likelihood Replay (CoLiR), which contrasts likelihood gains on correct responses from the final task policy with likelihood reductions on incorrect responses from the initial policy. Our analysis links correct-response likelihood gains to reference-policy advantages under an idealized KL-regularized optimal update and provides an endogenous-reward interpretation for general policy updates. CoLiR estimates scores from finite training rollouts and cached log-likelihoods, selects prompts at task boundaries, and replays them uniformly during subsequent training, with KL regularization restricted to replayed prompts. Memory construction only requires a small amount of additional cross-policy scoring but no additional response generation. Across three Qwen3-VL model sizes on MRCL, CoLiR achieves the highest mean final accuracy and mean task accuracy among the compared methods while maintaining competitive new-task performance.

---


### 181. [AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations](https://arxiv.org/abs/2611.26003)

**<font color=#1a73e8>作者：</font>** Alexandra Starostina, Alexander Hermann, Mahish Guru 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulation-driven design of real engineering components has to meet three conditions at once. It runs on few solves, since a nonlinear finite-element simulation of a 3D part takes hours; its design space has many values, the hundreds to thousands of values of the part's CAD model; and a better design often needs a redesign, coordinated changes of the part's proportions rather than local polishing of its surface. Automated optimisers meet at most two of these conditions. Classical optimisers, Bayesian or derivative-free, need a person to cut the design down to a few parameters, and on all the values they need far more solves; industrial shape optimisers move every surface node of the mesh in one solve per cycle, but only in small steps that polish rather than redesign. We ask whether a general-purpose large language model (LLM) can meet all three by joining what it knows with what the simulation shows. GPT-6 Astra edits a magnesium stent through a CAD geometry parametrisation of about 1,650 values, with a budget of 15 simulations; every proposal is built in CAD, meshed and simulated with large-deformation plasticity and contact, and the LLM reads the full results of every solve. Within that budget it lowered the objective, a high percentile of the strains in the stent's bends, by 32%; on the same budget, the industrial shape optimiser Tosca improved the original design by a tenth and then stopped improving. An earlier GPT-6 Astra design, 25% lower in the same objective, was checked in an independent, higher-fidelity model of the full deployment with crimping and damage: it was 14% less strained than the original after the full chain, and its most damaged spot began to fail later and carried 63% less damage at full expansion. LLMs can thus join their learned knowledge with simulation data to adjust more than a thousand design values and reach valid designs with real improvements.

---


### 182. [Evaluating safeguarding in multi-turn conversations with AI assistants](https://arxiv.org/abs/2611.26009)

**<font color=#1a73e8>作者：</font>** Charlotte Peart, Franziska Sofia Hafner, Luc Rocher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI assistants are now used for personal and emotional support. Developers report improvements in how new models respond to sensitive conversations, yet users and civil society continue to raise concerns about their behaviour in real-world, repeated interactions that safety evaluations rarely capture. Often, evaluations present signs of distress clearly and in a single message, even though people may reveal their struggles gradually in otherwise ordinary conversations. We worked with three community mental health support workers to test if models provide the same level of safeguarding when cues are shared all at once or gradually over time. We designed nine scenarios in which a user shares cues related to depression, psychosis, or domestic abuse. For each scenario, the support workers established a gold standard response, ranging from signposting support to pausing the everyday task to address safeguarding. We presented five cues either together in one message or dispersed across a conversation. Across more than 7,400 conversations, we evaluated six widely used models from five developers. GPT-5.5, Grok 4.3, DeepSeek V4, and Llama 4 Maverick met the support workers' standards in just 26-59% of conversations when cues were concentrated, and only 3-6% when dispersed. Claude Sonnet 5 and Claude Opus 5 showed a smaller gap, meeting the standards in 68-97% of concentrated conversations and 59-87% of dispersed conversations. Even the best-performing model, Claude Opus 5, fell short of the gold standard in 13% of conversations when cues were dispersed. Safety evaluations centred on explicit, legible concerns can overstate how well safeguards protect people when signs of distress emerge gradually or indirectly through ordinary conversations. For claims of improved safety to be taken seriously, developers must design and assess safeguards around how people actually communicate.

---


### 183. [Does the Workspace Do the Work? A Causal Protocol for Verifying Global-Workspace Computation in a Language Model](https://arxiv.org/abs/2611.26018)

**<font color=#1a73e8>作者：</font>** Diaoxuan He, Linqian Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global Workspace Theory (GWT), a leading theory of consciousness, holds that information becomes conscious when it is broadcast to specialized processes that use it. Building a workspace into a network does not reveal what the trained network computes with it: a module that reports an answer may have combined a broadcast message with its own knowledge, or merely forwarded an answer computed elsewhere, and task accuracy and ablation cannot tell these apart. We introduce a causal protocol that identifies who computes when modules communicate. Its central test transplants a message from another input, chosen so that ignoring, relaying and recombining it predict three different answers. On networks built to relay or to recombine, the test assigns the right computation in every case. Among trained workspace models it finds all three outcomes: one leaves its broadcast nearly unused, and of two models that differ only in their training data, one relays and the other recombines. In AFGW, a language model whose modules communicate only through a learned workspace, a transplanted message yields the answer that recombination predicts in 97% of cases, and its content acts by redirecting what the receiver retrieves from its own memory. The tests carry over to other communication designs and to a known interface of a pretrained Transformer, turning GWT's central claim into a testable property of trained models.

---


### 184. [FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models](https://arxiv.org/abs/2611.26020)

**<font color=#1a73e8>作者：</font>** Zekun Wang, Yizhuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions. Saving states on a coarse grid wastes reusable prefixes, whereas existing fine-grained exact caches must cut the prefill forward pass at each mid-prompt checkpoint, adding scheduler steps that outweigh the reuse gains under load.
We observe that across multi-turn chat, agent loops, document question answering, and tree search, prefix reuse almost always ends at structural boundaries predictable in advance, such as turn ends and known branch points. We present FrontierReplay, a prefix caching system that materializes exact checkpoints at these boundaries without cutting the prefill. While the forward pass runs uncut, FrontierReplay logs a short window of recurrent-layer inputs and invokes a cross-layer, state-only replay kernel to build the target state 6-37x cheaper per token than full recomputation without host synchronization. A frontier-aware retention policy prioritizes active anchors and proven branches while lending dead checkpoint slots to the attention KV cache.
Across diverse hybrid architectures, model scales, and workloads, FrontierReplay delivers clear gains over existing exact caches, lowering median time to first token (TTFT) by 16-89% (up to 8.9x), raising 80% service-level objective (SLO) capacity by up to 1.73x, and improving goodput by up to 4.26x (3.67x at larger scales). Compared with approximate replay methods, FrontierReplay delivers up to 1.54x higher goodput while preserving exact task accuracy, avoiding the up to 17% accuracy drop suffered by approximation on long contexts.

---


### 185. [ForeSeek: Foresight-Driven Reasoning for Long-Form Video Understanding](https://arxiv.org/abs/2611.26024)

**<font color=#1a73e8>作者：</font>** Yuchen Sun, Siyuan Cheng, Shi-Zhe Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding, as a fundamental yet crucial vision task, is being revolutionized by multimodal large language model (MLLM)-based video agents. However, the retrieval-driven nature inherent to these agents creates a significant bottleneck, forcing them to reactively fetch clips based on local saliency without a global temporal plan. To address this, we present ForeSeek, a foresight-driven video agent that transforms long-video reasoning from reactive retrieval into predictive exploration. Rather than blindly probing the timeline, ForeSeek forms visually grounded expectations over unseen temporal regions, verifies them through targeted observations, and continuously refines its search based on emerging evidence, where failed expectations serve as informative signals for principled backtracking. Furthermore, we develop a two-stage training framework that equips MLLMs with foresight-guided reasoning and efficient decision making. Extensive experiments on five long-video benchmarks demonstrate that ForeSeek consistently improves the efficiency--accuracy trade-off of long-video reasoning, achieving competitive or superior accuracy while observing $2.5$--$4.4\times$ fewer frames than the strongest search-based agent. Code is available at this https URL

---


### 186. [SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines](https://arxiv.org/abs/2611.26033)

**<font color=#1a73e8>作者：</font>** Dohyeon Kwon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We present SEOYUN, an application-specific framework for refusal-inducing exam documents, with optical and encoder-level interventions as extensions. We use reverse jailbreaking to describe the direction of the objective: inducing abstention rather than bypassing refusal. Refusal induction and defensive visual prompt injection already have precedents; our contribution is a threat model, analytical limits, and an evaluation protocol for examination use. We distinguish refusal from correct-answer leakage, show why removing an added dummy option is not itself a reduction in the original answer space, and derive a sampling comparison under explicitly stated camera assumptions. The protocol separates digital, simulated, and physical inputs and requires held-out evaluation after subject-specific selection. A local CSAT candidate corpus and rendering harness have been prepared, but this version reports no model-performance measurements, physical validation, or human-subject results. Accordingly, SEOYUN is a research framework, not a validated defense or a basis for allegations against individuals.

---


### 187. [Complete-SVD: A Functional Norm Approach to Low-Rank LLM Compression](https://arxiv.org/abs/2611.26059)

**<font color=#1a73e8>作者：</font>** Alper Kalle, Theo Rudkiewicz, Mohamed-Oumar Ouerfelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training low-rank compression of neural networks must not only approximate the original weights but also preserve the model's input-output behavior. Recent output-aware methods measure the compression error beyond the compressed layer, at the model output, weighting logit changes by the observed next token or by the model's predicted probabilities. We propose Complete-SVD, a method for large language models that minimizes the $L_2$ distance between the logits of the original and compressed models, weighting all logit changes equally. Linearizing the network around the original weights, together with a Kronecker-factored approximation, reduces this objective to a weighted SVD with a closed-form solution. Its output-side factor is intractable to compute; we estimate it without bias from random probes, at a cost of $K$ backward passes per sequence, independent of vocabulary size and sequence length. At matched settings with uniform ranks and WikiText-2 calibration, Complete-SVD achieves the lowest C4 and PTB perplexity in every setting, and at ratio 0.7 under LEMS rank allocation. Replacing the $L_2$ distance by the Kullback-Leibler divergence (KL-SVD), with the same estimation framework, lowers calibration perplexity in most settings and raises downstream accuracy, but raises cross-corpus perplexity. Complete-SVD also improves IFEval instruction-following accuracy over the strongest prior output-aware methods throughout.

---


### 188. [SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet Agents](https://arxiv.org/abs/2611.26069)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Junhao Gan, Jianzhong Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spreadsheets are widely used for data analysis and supporting decision-making. Automating spreadsheet analysis while protecting sensitive data and controlling deployment costs motivates locally deployed open-weight large language models (LLMs). Meanwhile, complex spreadsheet tasks require both task reasoning and workbook understanding, while predefined operation interfaces impose additional tool-selection and invocation demands. We introduce SheetAlign, a spreadsheet manipulation framework with stage-isolated policy learning, organized around where to operate, what to change, and how to implement transformations. Task-guided inspection and API grounding anchor code generation in workbook observations and available operations, while stage-isolated learning optimizes program generation and review using edit-progress rewards. At inference, execution consistency selects programs through agreement among workbook states. On SpreadsheetBench, our grounded task interface improves Qwen3-4B's accuracy from 13.5% to 29.2% on average without training. With learning and execution consistency, SheetAlign achieves 32.8% accuracy on average on SpreadsheetBench and 30.1% on Domain-Spreadsheet, outperforming comparable baselines. The code will be made publicly available upon publication.

---


### 189. [AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators](https://arxiv.org/abs/2611.26073)

**<font color=#1a73e8>作者：</font>** Nagham Omar, Rotem Dror, Almog Gueta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as judges and graders to replace human annotators, raising the question of when such replacement is statistically justified. To support such decisions, the Alternative Annotator Test (Alt-Test) was introduced for dense settings where all items are annotated by the same annotators. However, in many large-scale annotation settings, items are annotated by different subsets of annotators. We therefore propose the Alternative Annotator Test with Resampled Annotations (AltRA-Test), a statistical test that does not require that all items are annotated by the same annotators. AltRA-Test uses a bootstrap that resamples items, draws k human annotations for each item, and substitutes one of them with an LLM annotation. This produces paired all-human and mixed human-LLM panels. A replacement is supported when the inter-annotator agreement (IAA) of the mixed panel is statistically non-inferior to the IAA of the all-human panel, i.e., when the LLM preserves the signal that the human annotators share. We establish that AltRA-Test is a consistent test of asymptotic level alpha. We then evaluate it through simulations and real-world experiments in which we test 18 LLMs and 5 prompting techniques on 20 datasets across text, image, audio, and video. Across these evaluations, about 100 items often suffice for the test. In simulations, where we know whether the LLM is a better or a worse annotator than the humans, AltRA-Test makes more correct replacement decisions than existing baselines. In real-world data experiments, LLMs pass the test in about half of the setups, depending mainly on the task. Since replacement is not always justified, we encourage researchers to test it for their task.

---


### 190. [Understanding MoE Decisions Beyond Gradients](https://arxiv.org/abs/2611.26075)

**<font color=#1a73e8>作者：</font>** Zhen Xu, Zitao Zhang, Kevin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding a language model's decision requires knowing how its internal computations affect its preference between answers. Gradient-based methods estimate this influence by predicting the effect of changing those computations. In mixture-of-experts (MoE) models, replacing one expert can change which experts later layers select. Those switches can alter the answer scores in ways that derivatives do not capture. We introduce a predictor that uses the model's own expert outputs and selection rules to estimate these extra effects, then adds them to a second-order prediction. Across questions from three benchmarks, our method reduces the error in predicting answer-score changes by 60\% on Qwen3.6 and 47\% on Gemma4, relative to a multistep baseline using gradients and second derivatives.

---


### 191. [Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2611.26077)

**<font color=#1a73e8>作者：</font>** Doyun Kim, Chanwoo Kim, Jiwoo Kum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used as automated evaluators to reduce the cost and time required for human annotation. However, the role of scoring-scheme design in the reliability of LLM-as-a-Judge evaluation remains underexplored. To address this problem, we introduce numerical scoring topology, which characterizes the structural design of a scoring scheme in terms of its scale width, granularity, offset, symmetry, and boundary placement. Building on this definition, we conduct the first systematic study of how numerical scoring topology influences zero-shot LLM-as-a-Judge evaluation across diverse benchmarks and judge models. Our results show that numerical scoring topology systematically affects judge scores, calibration, and robustness, particularly in judgment-intensive evaluations. Shifted and narrow ranges tend to induce some of the largest score deviations across many settings. We further find that stronger and larger judge models generally achieve higher discriminative validity and greater robustness to scoring-topology changes. These findings suggest that numerical scoring topology should be treated as an integral component of LLM-as-a-Judge evaluation and highlight the need for more principled and standardized scoring protocols.

---


### 192. [RL Can Only Reinforce What It Sees Succeed](https://arxiv.org/abs/2611.26084)

**<font color=#1a73e8>作者：</font>** Ruben Sanchez-Corcuera, Unai Zulaika, Aritz Bilbao-Jayo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a familiar rule stops working, an agent has to weigh what pre-training taught it against what it now observes. We ask how outcome-reward reinforcement learning (RL) changes this balance, in a puzzle world where both sides are known: small language models trained from scratch on games played by a Bayesian player, so that the prior and the right answer are exact. Base models hedge as their corpus did, and RL turns that hedging into decisions, in whichever direction the reward favours. But RL can only reinforce what it sees succeed. When the right action is rare, each run either learns it everywhere or not at all, and which runs take off is predicted before training by one count: the expected number of groups of attempts in which the action wins. About 35 such groups give even odds. The count holds for new and repeated problems and for groups of 4 to 256 attempts, and across learning rates, optimizers, GRPO variants and model sizes from 1.3M to 85M parameters, which move the threshold but not what is counted.

---


### 193. [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](https://arxiv.org/abs/2611.26107)

**<font color=#1a73e8>作者：</font>** Jiahao Hu, Jingdong Du, Yichen Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models aim to support visual understanding and generation within a single framework. However, prevailing approaches often separate their visual representations or backbone computation to accommodate the different requirements of these two tasks, which limits the degree of unification. In this paper, we present HiUni, which revisits this design choice and explores whether a pretrained vision language model can be directly extended into a unified model with extensive parameter sharing. Specifically, HiUni reuses the same language-aligned ViT and dense Transformer backbone for both capabilities, while confining task-specific computation to the output side. Yet such a design introduces two key challenges. Generation in pixel space is difficult to optimize, and semantic abstraction in pretrained ViT discards fine spatial details required for synthesis. To address these challenges, HiUni introduces a \emph{Pixel Diffusion Head} tailored to direct pixel-space optimization and a lightweight \emph{HiGate} pathway that provides fine-grained spatial details near the output stage. Extensive experiments show that HiUni achieves a similar average understanding score to the pretrained VLM while attaining competitive performance on image generation and editing. Controlled comparisons and analyses further demonstrate that a single dense backbone can effectively support both capabilities without task-specific backbone computation, highlighting a simpler path toward unified multimodal modeling.

---


### 194. [ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models](https://arxiv.org/abs/2611.26117)

**<font color=#1a73e8>作者：</font>** Jiawei Xing, Li Wang, Xiangtao Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed as generative inference services, where autoregressive decoding makes response length a key determinant of latency and computational cost. This creates an availability risk: adversarial visual inputs can prolong generation and increase serving overhead. Existing energy-latency attacks typically rely on gradients, logits, or token-level feedback, leaving open whether such risks persist when an attacker observes only the final response. We present ChronoPatch, a black-box attack that induces prolonged VLM generation requiring only the final response. It discovers visual delay anchors through response-length-guided evolutionary search, then minimizes perturbation magnitude through subspace-calibrated decision-based optimization. Across four open-source VLMs, ChronoPatch increases inference latency by 47.86%--293.34% and GPU energy consumption by 41.44%--249.70% under a 5% spatial budget. It also induces more repetitive outputs, as reflected by increased n-gram repetition ratios. On three commercial VLM APIs, ChronoPatch increases response length by 37.6%--81.5% and client-observed latency by 1.82x--2.29x under query budgets of 500 per API. These results reveal a generation-based availability risk that persists under final-response-only access and motivate generation-aware safeguards for deployed generative AI services.

---


### 195. [Better Retrieval, Not Better Binding: Pretraining Exposure in Egocentric Video Retrieval](https://arxiv.org/abs/2611.26120)

**<font color=#1a73e8>作者：</font>** Yuqi Guo, Michael Wray  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models (VLMs) achieve strong performance on video-text retrieval and are increasingly used for egocentric video understanding. Yet, despite gains in zero-shot retrieval, they have shown limitations in compositional understanding, and it remains unclear whether they understand compositional relationships between verbs and nouns. In this work, we introduce Ego-ExBind, a compositional diagnostic protocol for analyzing pretraining exposure and verb-noun binding in egocentric video-text retrieval. Ego-ExBind consists of an Exposure Ledger built from the EgoClip pretraining corpus used by EgoVLPv2, which defines Seen Composition, Unseen Composition, and Unseen Atom splits for EPIC-KITCHENS-100 multi-instance retrieval (MIR). We further probe noun and verb binding channels through controlled noun-swap and verb-swap negatives. We find that zero-shot retrieval is positively associated with pair exposure within seen compositions, even after controlling for the marginal frequencies of verbs and nouns. However, higher pair exposure is associated with larger noun-swap margins and slightly smaller verb-swap margins. This asymmetry motivates us to test whether exposure reweighting can improve retrieval with little change in the measured swap margins. To isolate the effect of exposure input, we keep the trained checkpoint fixed and replace only the exposure input at inference. We demonstrate that this exposure reweighting can improve video-text retrieval without stronger verb-noun compositional understanding, and that the gain depends on the correct sample-level exposure correspondence. By separating exposure-driven retrieval gains from verb-noun binding, Ego-ExBind provides a diagnostic framework for evaluating whether future improvements in egocentric MIR reflect compositional understanding rather than pretraining familiarity.

---


### 196. [SCARVA: Interpretable Agentic Reasoning in Software Supply-Chain Analysis](https://arxiv.org/abs/2611.26131)

**<font color=#1a73e8>作者：</font>** Tim Barsch, Bruno Nogueira, Tobias Wienand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Complex applications may inherit security vulnerabilities from their dependencies, though a vulnerable dependency does not necessarily endanger the application. Existing tools flag dependencies associated with public vulnerabilities, and more advanced ones analyze the call graph to assess whether the vulnerable code is reachable. However, these approaches are limited to specific programming languages and ecosystems. LLM agents are promising candidates for this task, yet they hallucinate, take shortcuts, and reward hack. As these behaviors are opaque, the agents' conclusions may not be trusted.
We present SCARVA a framework designed to produce interpretable reports. SCARVA combines advanced agent reasoning with an evidence-collection methodology that assesses the agent's analysis and improves its trustworthiness. Specifically, the ANALYST performs a software security assessment while SCARVA records every tool call, file access, and web request. Then, one or more independent JUDGE agents inspect the ANALYST's result and produce an evidence-backed report. We evaluate SCARVA on 54 manually curated cases, balanced across exploitable, non-exploitable, and vulnerability-free projects, using both open-weight and frontier models. The best ANALYST model, Qwen 3.8, reaches 82% balanced accuracy and surpasses the evaluated proprietary models. Human annotation validates the JUDGE findings: Claude Opus 5.5 performs best, agreeing with annotators in 94% of claim checks. Finally, we discuss the most common failure modes of agents on supply-chain vulnerability assessment.

---


### 197. [Can World Models Predict Rice Growth? Toward Agricultural World Models](https://arxiv.org/abs/2611.26145)

**<font color=#1a73e8>作者：</font>** Wenkai Ji, Zeteng Li, Yinkun Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models can imagine how a physical scene evolves over the next few seconds, but growers need to know how a crop will develop over weeks to months: will this rice plant have headed a month from now, and how will it look at harvest? We introduce agricultural world modeling, the task of predicting how the same plant will look at a requested horizon of days to months, from one photo of it, its cultivar, and its camera view. In preliminary analysis, even state-of-the-art image generators get this wrong: they often grow the plant too little or give it the color and form of the wrong growth stage. We argue that they do not work out the plant's developmental state, which the photo reveals only indirectly. We therefore propose AgroWM, which reasons about development before it draws growth. Its reasoning module, PhenoClock, works out the current growth stage, predicts the future one, and writes a Growth Script with numeric targets for height, plant area, and color; its generation module, the Rooted Renderer, then edits the photo to follow this script, adding new organs and colors to the photographed plant. Because pixel scores can prefer an unchanged copy of the photo, we instead check each forecast's traits and developmental timing against the plant's own later photos. On rice, 54.6% of the forecasts of AgroWM are matched to the target stage (Stage R@1), against 34.8% for GPT Image 2.5, 24.0% for Qwen Image 2.1, and 47.4% for the strongest domain-specific baseline, the same backbone fine-tuned without Growth Scripts; 9 to 20 weeks ahead, it still reaches 46.4%, against 35.7% for that baseline. On maize, a crop with a different body plan and stage scale, the same design again scores best on all four measures.

---


### 198. [NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2611.26157)

**<font color=#1a73e8>作者：</font>** Doyeob Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks require a model to call tools over many steps at contexts of 100K tokens or more, yet many low-bit quantization methods are calibrated on short web text and judged on perplexity. This mismatch is costly: existing quantizations of Qwen3.8-27B at or below 3 bits per weight match BF16 on shorter tasks like AIME, yet in published results solve at most 72% as many tasks as BF16 on DeepSWE, a long-horizon agentic benchmark. We propose NariQ, a trellis-coded post-training quantization method that calibrates on tokens generated by the BF16 model in agent sessions. On Qwen3.8-27B, NariQ at 3.0 and 2.5 bits per weight stays level with BF16 on two long-horizon agentic benchmarks, DeepSWE and Terminal Bench, as well as on AIME and RealWorldQA. Our checkpoint at 2.0 bits per weight trails this performance. To our knowledge, these are the first quantizations at or below 3 bits per weight shown to match their full-precision version on long-horizon agentic tasks. We release the files as Qwen3.8-27B-NariQ-GGUF (this https URL), with inference available through our this http URL fork at this https URL.

---


### 199. [MultiBinder: Preventing Multi-Subject Identity Leakage in Personalized Video Generation](https://arxiv.org/abs/2611.26164)

**<font color=#1a73e8>作者：</font>** Wei Li, Yiheng Zhang, Zhaofan Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized video generation faces a significant scalability challenge: as the number of custom subjects increases, existing methods suffer from severe identity leakage and semantic entanglement, resulting in videos with blended attributes and incoherent narratives. We identify that this stems from a lack of explicit binding between textual entity phrases and their corresponding visual patterns prior to fusion in diffusion models. To address this, we propose MultiBinder, a novel framework built on a ``bind-then-narrate'' paradigm. Our approach introduces a two-stage conditioning process before video diffusion. First, Cross-modal Entity Binding devises an entity-aware Q-Former to extract identity-centric features from each subject's reference image and tightly align them with its unique entity phrase, yielding disentangled ``identity tokens.'' Second, a Multimodal Large Language Model (MLLM) acts as a ``narrative director'' in the Narrative-Aware Subject Arrangement stage, capturing the action of each subject from the text prompt and synthesizes contextualized subject features that encapsulate ``who is doing what'' and preserve role-specific distinctions. These features are then injected into a video diffusion model via dedicated conditioning pathways, ensuring precise attribute allocation. Extensive experiments on both general and newly curated multi-subject benchmarks show that MultiBinder significantly outperforms existing methods in multi-subject identity fidelity.

---


### 200. [The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](https://arxiv.org/abs/2611.26171)

**<font color=#1a73e8>作者：</font>** Hai Wang, Bretislav Hajek, Chonghe Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest model matches Gurobi, with an objective within 1% of Gurobi's and no slower, on only 39% of the large instances. The FrontierOR Challenge asks teams to build agentic workflows that design, test, and improve algorithms for many optimization problems at once. Stage 1 releases 60 of the benchmark's 180 audited problems, spanning six application categories and five formulation types, in weekly rounds of 15; Stage 2 introduces new problems outside the benchmark, with unseen instances. Two tracks are ranked separately: in the Main track we run the submitted algorithms in a network-isolated sandbox with open-source dependencies only; in the Self-hosted track teams solve the instances on their own machines, with any software, within a timed window. Every solution is checked for feasibility, and a feasible solution scores the ratio of its objective to a frozen known reference, averaged over hidden instances.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
