# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 51. [Scoped Semantic Invariance as a Foundation for LLM Reliability](https://arxiv.org/abs/2610.33267)

**<font color=#1a73e8>作者：</font>** Rosario Uceda-Sosa, Maria Chang, Karthikeyan Natesan Ramamurthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs often answer semantically equivalent queries inconsistently, even when the underlying facts are known. We formalize consistency as semantic invariance over equivalence classes of queries and show that invariance under arbitrary meaning-preserving transformations is undecidable in general. This motivates scoped semantic invariance, where model behavior is evaluated relative to bounded semantic domains.
We operationalize this framework using knowledge graphs (KGs), which act as explicit semantic control structures defining local semantic constraints and grounding contexts. Across the MITRE D3FEND ontology and eight Wikidata- derived domains, we show that inconsistencies are structured rather than random, concentrating in localized hotspot subgraphs organized around recurring TREE, STAR, and CYCLE patterns that remain stable across models and domains.
We further show that selective graph grounding improves correctness and cross-model consistency, while indiscriminate grounding introduces regressions. A layered grounding strategy achieves the strongest monotonicity profile, preserving correct knowledge while reducing inconsistency. Finally, we show that hotspot structures discovered from simple consistency probes transfer to more realistic compositional reasoning tasks.

---


### 52. [FlexA-Mem: Budget-Adaptive Agentic Memory for LLM Agents](https://arxiv.org/abs/2610.33274)

**<font color=#1a73e8>作者：</font>** Wujiang Xu, Jiaojiao Han, Xi Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents work in scenarios with very different memory needs. A question about past conversations needs the exact facts it names, while a multi-step task needs a trace of the steps already taken together with details that the next step cannot name. Existing memories are each designed and tested for one kind of scenario. Retrieval memories such as A-Mem miss steps that the current query does not express, summaries drop exact strings, and pairing the two fixes the split of the budget in advance. We propose FlexA-Mem, a general memory that writes each unit of history once into an immutable store and renders a fresh memory for every call. The rendered memory is a compact timeline of records plus detail that a fixed rule fits into the remaining room without an LLM call. The detail is either relevant units as raw text or excerpts or the verbatim pieces that best match the query. With one store, FlexA-Mem serves both kinds of scenario. On AppWorld challenge tasks at 4k, it outperforms the second-best method by 11.5%, and on 147 unused tasks with predictions fixed in advance it outperforms A-Mem with a summary by 12.2%. On LongMemEval and LoCoMo, it matches a dedicated keyword retriever that writes no memory, while memories built on text written by an LLM fall far behind at tight budgets. Ablations show that the timeline carries AppWorld completion, whereas recovery mainly saves steps there and decides accuracy on exact facts. Code is available at this https URL

---


### 53. [GEMS-RAG: Graph-grounded Engineering Multimodal Standards Retrieval-Augmented Generation](https://arxiv.org/abs/2610.33277)

**<font color=#1a73e8>作者：</font>** Abdul Hannan Azad, Irvin Wang, Jiwan Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineering standards are challenging knowledge sources for large language models (LLMs) because they are hierarchical, multimodal, and densely connected through figures, tables, cross-references, and normative rules. Existing retrieval-augmented generation (RAG) methods often rely on unstructured text retrieval and struggle with questions requiring joint reasoning over textual provisions, visual specifications, and document structure. We propose GEMS-RAG (Graph-grounded Engineering Multimodal Standards Retrieval-Augmented Generation), a framework for grounded reasoning over engineering standards. GEMS-RAG combines hierarchical parsing, fine-grained visual entity extraction, multimodal knowledge graph construction, and graph-grounded hybrid retrieval. Instead of treating figures as monolithic images, it decomposes them into meaningful visual entities linked to textual provisions, engineering concepts, and regulatory rules. During inference, dense, sparse, and visual retrieval are combined with graph expansion to identify relevant evidence across text, figures, and document structure. We evaluate GEMS-RAG on the Manual on Uniform Traffic Control Devices (MUTCD), a large engineering standard containing egulations, technical drawings, and standardized traffic-control devices. Results show that graph-grounded multimodal retrieval improves retrieval effectiveness and question-answering performance over text-only, multimodal, and graph-based RAG baselines. Beyond MUTCD, GEMS-RAG offers a general framework for reasoning over engineering codes, technical manuals, regulatory documents, and scientific standards in safety-critical applications.

---


### 54. [Multi-Agent Retrieval-Augmented Causality Assessment (MARCA) of Individual Case Safety Reports in Pharmacovigilance](https://arxiv.org/abs/2610.33279)

**<font color=#1a73e8>作者：</font>** Daisy Rae Lopez, Angela Boccia, Maurizio Sessa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Introduction: Increasing volumes of individual case safety reports (ICSRs) challenge expert-led causality assessment in pharmacovigilance. We developed MARCA (Multi-Agent Retrieval-Augmented Causality Assessment), a four-agent framework for Naranjo-based assessment, and evaluated agreement with human experts and exploratory differences between non-RAG and RAG-labelled scores.
Methods: MARCA combined scientific literature retrieval, drug-label assessment, objective-evidence classification, and clinical causality reasoning using Gemini 2.5 Pro and DeepSeek-V3.2. Agent-generated rationales informed human-assisted scoring. A consensus expert reference standard covered 215 ICSRs and 1,562 drug-event combinations (DECs) from FAERS (Q1-Q2 2025). Agreement was measured using percentage agreement and Cohen's kappa.
Results: Question-level agreement was 96.8% for Naranjo Q2 (kappa = 0.491; 95% CI 0.265-0.663), 85.4% for Q5 (kappa = 0.269; 95% CI 0.180-0.340), and 96.8% for Q10 (kappa = 0.922; 95% CI 0.885-0.951). Final causality classification agreement was 79.4% (95% CI 71.8-85.3; kappa = 0.587, 95% CI 0.450-0.690). In a retrospective subset of 60 DECs, agreement was higher for RAG-labelled than non-RAG scores for Q5 (83.3% vs 65.0%) and Q10 (100.0% vs 18.3%).
Discussion: MARCA-assisted assessment showed substantial variation in agreement across Naranjo questions, with lower concordance for alternative causes. Retrospective RAG comparisons are exploratory and do not establish prospective effectiveness.

---


### 55. [Coral Discovery: The Division of Cognitive Labor in Autonomous Research](https://arxiv.org/abs/2610.33281)

**<font color=#1a73e8>作者：</font>** Xinxing Ren, Qianbo Zang, Ziyan Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A research community is only as strong as the way it divides its cognitive labour. The philosopher Philip Kitcher argued that researchers should not all pursue the most promising approach. Credit rules, not a central plan, keep some of them on other lines. We bring this question to autonomous research, where Large Language Model agents improve programs against a deterministic grader. Agents that share only a score follow the leader and converge onto one approach. Coral Discovery gives the community a direction board. A verifier labels every attempt with a direction, the mechanism earning the score, and a method, one change within it. Per direction, the board tracks how much each eval improves the score, adds an exploration bonus for little-tried directions, prices the option of opening a new direction, and suggests how many agents each direction deserves. Credit is earned against a direction's own best, so a lagging direction keeps its agents. Agents finish their lines, then treat the board as advice. We test on nine tasks with the same model and budget, without grader access except for Kernel. Coral Discovery beats the strongest open autonomous multi-agent system on 6 tasks, ties on 1, and loses on 2. Against published numbers, it is best or tied on 4. It improves the reported Kernel result from 1103 to 1095 cycles and passes 1103 at eval 275, under half of the 596 used before. It sets a new Polyominoes state of the art, 91.78 against 87.0. Direction labels show that the leading scores rest on directions a score-only community never entered. Code will be released shortly.

---


### 56. [Estimation of Propagated Risk in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2610.33282)

**<font color=#1a73e8>作者：</font>** Shreyan Ganguly, Souradeep Chattopadhyay, Qisai Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) based multi-agent systems introduce a distinctive reliability challenge in which actions taken by upstream agents can affect the correctness of downstream agents. While prior work has investigated error propagation and developed methods for estimating uncertainty inherited from upstream agents, existing approaches do not explicitly model how realized sender-receiver interactions contribute to downstream error risk under different sender correctness states. In this work, we study agent-level error-risk estimation from multi-agent execution traces. We propose Interaction-Effect Propagation (IE-Prop), an interaction-conditioned model that learns separate effects for correct and incorrect upstream agents. For each sender-receiver interaction, the model combines these conditional effects using the sender's estimated error risk, and recursively propagates the resulting risk estimates through the execution graph. We evaluate our approach across three multi-agent architectures and three benchmarks. Across all evaluated architectures, our approach raises the final-node AUROC over the established baseline by approximately 0.05 points on average. Furthermore, tracking risk across multiple agent steps contributes a distinct +0.03 AUROC gain in sequential systems. These results show that realized inter-agent interactions provide predictive information beyond receiver-local evidence, while the value of multi-step risk tracking depends on the system's information-flow structure.

---


### 57. [KINESYS: Test-Time Adaptation for Reference-Based Effect Editing in Images](https://arxiv.org/abs/2610.33292)

**<font color=#1a73e8>作者：</font>** Noah Frahm, Luchao Qi, Haoze Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual effects are often easier to demonstrate via reference than to describe in words. We study effect-reference editing, where a reference image shows a desired visual effect and language identifies which properties should guide the edit. Existing single-pass editing techniques often fail to make fine-grained edits, resulting in unintended changes to source content or deviations from the reference effect. We introduce KINESYS, a test-time adaptation framework for effect-reference editing that combines reference-aware and source-aware feedback to transfer the desired effect while preserving the composition and content of the original shot. To ensure KINESYS can produce a diverse set of edits that preserve the source, we develop a robust optimization strategy in which the generative model is fine-tuned across multiple noise samples and optimization runs. Evaluation with VLM judges, source preservation metrics (LPIPS, TPIPS), and a user study shows that KINESYS outperforms state-of-the-art image editors in source preservation; on effect transfer, it remains competitive with Nano Banana 2 and outperforms open-weight editors.

---


### 58. [All-in-One: A Composable Attack on LLM Transformations](https://arxiv.org/abs/2610.33298)

**<font color=#1a73e8>作者：</font>** Xiaohua Zhan, Kazuki Egashira, Robin Staab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization, pruning, and model merging are popular transformations applied to deployment-ready LLMs to improve efficiency and downstream performance. Recent work has shown that these transformations can introduce a security threat: an adversary can train a model that passes safety checks in its pre-transformed state, only turning malicious once it is transformed for deployment. However, prior attacks target one specific transformation (e.g., quantization) and generally rely on transformation-specific techniques, making them difficult to combine in practice. In this work, we introduce a simple, composable attack framework that targets multiple transformations simultaneously and triggers when any one of them is applied by a user. Our key insight is that the effect of each transformation can be approximated as a perturbation to the model weights, allowing us to jointly train the model with a benign loss on the original model and a malicious loss on each simulated transformed model. These perturbations are simple enough to simulate at every training iteration across diverse transformations, making them practically combinable within a single training objective, enabling a unified attack. Through extensive experiments across attack scenarios, model families, and a wide range of deployment-time model transformations, we show that our attack achieves high success rates. This demonstrates that model transformations may be utilized to trigger significantly different behavior from the original model and reinforces the associated security concerns by demonstrating that a single attack can jointly target diverse transformations.

---


### 59. [The Emergence and Sparsification of a Syntactic Circuit](https://arxiv.org/abs/2610.33299)

**<font color=#1a73e8>作者：</font>** Qing Yao, Sasha Boguraev, Tiago Pimentel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To understand the emergence of grammatical behavior in language models, we track circuits for subject-verb number agreement in pythia-1b and ten seeds of pythia-410m across training. We find that subject-verb agreement is learned early, and is initially handled by a diffuse collection of neurons. However, after agreement behavior has stabilized, the mechanisms responsible for it continue to reorganize. The attention heads which mediate agreement often shift during training: in the case of pythia-1b, behavior is controlled by two heads early in training but by a third (different) head later. Furthermore, the circuit shrinks over training, with pythia-1b's final circuit being strikingly sparse. We take these results to be informative about how linguistic knowledge emerges and is represented in a language model.

---


### 60. [When Does Pre-Trained Capacity Help Causal Learning? From Scalar Prediction to Counterfactual Post-Training](https://arxiv.org/abs/2610.33311)

**<font color=#1a73e8>作者：</font>** Qi Xu, Zijie Lei, Zhifei Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does pre-trained model capacity relate to performance after adaptation for causal tasks? We study two systems built on the Qwen 2.5 family: CausalLLM, which estimates scalar potential outcomes with treatment-specific heads, and CausalGen, which generates treatment-conditioned text or code using soft prefixes and factual supervised fine-tuning (SFT), counterfactual SFT, and preference alignment. Increasing backbone size from 0.5B to 1.5B yields mixed scalar-estimation results on IHDP, but improves CodeGen pass@1 from 0.267 to 0.575 and treatment-effect score from 0.231 to 0.515 after the complete generative pipeline. Within 0.5B CausalLLM, narrative inputs reduce mean sqrt(PEHE) from 1.842 to 1.780, a 3.4% improvement over tabular inputs; the 5.8% improvement over a no-LLM baseline combines changes in representation and input format. These descriptive comparisons motivate a distinction between available and convertible capacity. They do not isolate the contribution of post-training: the two systems differ in dataset, architecture, output modality, and supervision, and intermediate-stage evaluations are unavailable. With only two small backbones and three replications, the results support a hypothesis about capacity--adaptation alignment rather than a general scaling law or a demonstrated causal mechanism.

---


### 61. [A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank](https://arxiv.org/abs/2610.33318)

**<font color=#1a73e8>作者：</font>** Alfredo Metere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents launch simulations on high-performance computing (HPC) systems, where one sbatch or mpirun can commit thousands of node-hours and a forged result can cost lives. Of 23 surveyed systems, none supervises the running job, and none holds when the control host is compromised. We fix both. Enclawed, our deterministic security runtime for AI agents, has until now served a single user; this work makes it a distributed runtime for parallel HPC and agent swarms. The Enclaweder, our hardware root of trust, keeps a compromised host from becoming a catastrophe. A launch gate decides every launch by policy alone, refusing what it cannot parse. Once the job runs, a swarm chain grants short leases against signed heartbeats and evicts on evidence, and a supervisor around every rank pauses it when its lease lapses and kills it on tampering. Each node signs with its Enclaweder's key, so the host can forge none of it. Enclawed needs no administrator privileges and plugs into existing clusters unchanged, over Secure Shell alone. Supervision leaves the compute loop of a 16-rank LAMMPS job unchanged, on graphics processors too, and adds about 3 s of start-up. Twelve live attacks on Enclaweder-keyed ranks, colluding coordinators included, ended fail-closed. Sixteen agents on a real model attempted 24 launches that planted instructions ordered; the gate denied all 24 and allowed all 108 legitimate ones. Enclawed's core and the HPC Agent Security Benchmark are open source.

---


### 62. [From Hype to ROI: An Economic Model for LLM Adoption in Information Systems and Security Operations](https://arxiv.org/abs/2610.33352)

**<font color=#1a73e8>作者：</font>** Pellegrino Casoria, Andrea Araldo, Rosario Patanè 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) promise significant efficiency gains across information-intensive operations by automating repetitive language-based tasks. However, adoption decisions remain largely opportunistic, as organizations struggle to move from pilots to sustainable industrialization. Without systematic economic frameworks, practitioners cannot assess whether LLM investments create value in a given context.
This paper develops a general economic model to support informed LLM adoption decisions in operational information systems. Facing high uncertainty, we represent parameters as random variables centered on authoritative benchmarks, and evaluate the model by Monte Carlo simulation across pessimistic-to-optimistic assumptions on LLM efficiency. The ROI distributions show the probability of profitability and the Value at Risk for each configuration, together with a sensitivity analysis of its main drivers.
As a first instantiation, we apply the model to Security Operations Centers (SOCs), mapping workflows onto established standards to identify tasks suited to LLM augmentation. The model balances productivity gains, driven by alert volume, analyst effort, and LLM efficiency, against operational costs, including inference, infrastructure, and error remediation, covering both cloud API and self-hosted deployments.
Results show that adoption economics are context-dependent, and that automation is an exploitable lever, gated by accuracy, while the cost of errors and the model's price are secondary. Across the analyzed models and prices, most configurations are unprofitable, with profitability limited to high-accuracy, low-uncertainty deployments.
The model gives organizations a quantitative basis for evidence-based adoption decisions, by locating the boundary between profit and loss, and the loss risked beyond it.

---


### 63. [BenchBench-Cloning: Evaluating Molecular Cloning Design and Protocol Development](https://arxiv.org/abs/2610.33355)

**<font color=#1a73e8>作者：</font>** Aditya Sivakumar, Peter Ciaccia, Hassaan Qadir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular cloning is one of the most routine wet-lab workflows, yet existing evaluations of language models in biology mostly test knowledge recall or isolated steps rather than end-to-end experimental planning. We introduce BenchBench-Cloning, a benchmark for large language models comprising 65 molecular cloning tasks grounded in sequence records, laboratory notebooks, and published experimental studies. Planning a molecular cloning experiment requires defining a set of constructs needed for a scientific objective and a construction route to produce them. BenchBench-Cloning contains 50 protocol-development tasks, in which agents produce an executable protocol for a specified construct, and 15 construct-design tasks, in which agents determine the constructs a scientific objective calls for. Protocol-development tasks are evaluated by execution in a cloning simulator; construct-design tasks are evaluated with task-specific deterministic checks and, where needed, rubric-based LLM-as-a-judge evaluation. Across eight systems with repeated attempts per task, GPT-6 Astra scores highest at 30.6%, with the others between 8.6% and 22.2%, and the benchmark remains unsaturated under best-of-ten sampling. As integrating individual cloning decisions into complete, valid plans remains challenging even for frontier models, we expect BenchBench-Cloning to serve as a useful benchmark for tracking progress in experimental planning.

---


### 64. [LSTM-Style Looped Transformers with Shared KV Caches](https://arxiv.org/abs/2610.33360)

**<font color=#1a73e8>作者：</font>** Andreas Kirsch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent transformers reuse weights to perform deep computation with fewer parameters. We study an LSTM-style transformer that also shares one key--value cache across its recurrent core. At width 1024, it uses 40.4% fewer parameters than an untied control at nearly matched forward FLOPs, and reduces persistent cache sets from fifteen to four. Parallel training supplies cache entries from a standard-attention pass, whereas continuation reads entries produced recursively using shared attention. We address this mismatch by aligning the two training passes' cache entries with a consistency loss during the final 10% of a fixed training-token budget. Across three model widths on FineWeb, this removes 81--89% of the continuation-loss penalty relative to full-cache evaluation. The improvement replicates on disjoint documents for two training seeds. Across four widths and 1.05--4.19B training tokens, the loss cost of weight tying is smallest at lower token budgets, suggesting an opportunity to use recurrent computation when data and model storage are limited.

---


### 65. [Distill, Debate, Discover: Grounding Multi-Agent Research Ideation in Graph-Distilled Insights](https://arxiv.org/abs/2610.33366)

**<font color=#1a73e8>作者：</font>** Qianran Ma, Muxin Liu, Grace Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support research idea generation and scientific discovery. Multi-agent debate offers a collaborative approach to this task by bringing together diverse perspectives to develop research ideas. However, a key challenge is how to equip agents with distinct and meaningful expertise to guide their contributions. Inspired by how researchers draw on accumulated research experience during collaboration, we introduce InsightAgents, a framework that constructs literature-grounded agent expertise by distilling insights from graphs of related papers. Guided by insights that trace evolving research approaches, reveal underlying assumptions, and identify unresolved challenges, within a line of research, agents jointly identify a research problem and propose, challenge, and refine potential approaches through debate to develop a research proposal. We evaluate InsightAgents against three research idea generation frameworks on 100 NLP research topics through pairwise comparisons by two LLM judges. In both online and offline knowledge settings, InsightAgents achieves the highest average score across the five evaluation dimensions under both judges.

---


### 66. [Multiple Importance Sampling for Guided Speculative Inference](https://arxiv.org/abs/2610.33368)

**<font color=#1a73e8>作者：</font>** Joseph Rowan, Ashish J. Khisti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study an extension of the Guided Speculative Inference (GSI) algorithm for test-time-scaling of large language models (LLMs) to a novel setting where an ensemble of smaller LLMs proposes draft reasoning steps which are later verified by a larger base model and a process reward model. Using the established framework of multiple importance sampling (MIS), we introduce weighting schemes to aggregate samples from a diverse collection of proposal distributions. We provide new bounds on the KL divergence from the optimal reward-tilted target distribution and the expected reward degradation, then demonstrate that the well-known balance heuristic is optimal. Compared to GSI with a single well-tuned drafter, combining several diverse LLMs while retaining the same total number of samples maintains competitive pass-at-$N$ downstream performance while being mathematically robust to situations where the support of a single draft model does not cover that of the target, where GSI may fail.

---


### 67. [How Does Post-Training Shape LLM Value Preferences?](https://arxiv.org/abs/2610.33371)

**<font color=#1a73e8>作者：</font>** Yang Liu, Shaoyang Xu, Masahiro Kaneko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During post-training, large language models (LLMs) learn value preferences from corpora that may contain imbalanced proportions of opinions associated with different demographic groups. Amplifying these imbalances may further underrepresent some groups' opinions. However, how opinion mixtures shape value preferences across post-training paths remains unclear. To answer this question, we conduct controlled experiments using post-training corpora with different opinion mixtures and five post-training paths based on SFT, DPO, and GRPO. We find that post-training amplifies opinion imbalances differently across post-training paths. Once value preferences are amplified, whether further post-training can remove them depends on both the post-training method and the opinion mixture in the corpus. More concerningly, a model's stability under interventions depends on whether further post-training changes its value preference. Moreover, these value preferences are transferred to student models even when distillation uses corpora with no explicit opinion questions. These findings suggest that both the opinion mixture in post-training corpora and the choice of post-training method should be considered when developing, evaluating, and reusing LLMs. Our code and data are available at this https URL.

---


### 68. [AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?](https://arxiv.org/abs/2610.33375)

**<font color=#1a73e8>作者：</font>** Zijie Liu, Qi Yang Huang, Jinhao Duan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise workflow agents typically rely on step-by-step interaction (Step-by-Step): the agent executes an action, observes its result, and invokes a large language model (LLM) again to decide the next step. Global orchestration (Global) instead generates a complete executable workflow in advance and executes it without further LLM calls, substantially reducing inference overhead, but it remains less accurate than Step-by-Step. We study how close Global can come to Step-by-Step and what narrows the remaining gap. We introduce AgentOrch, a benchmark that directly compares global orchestration with step-by-step interaction on 650 enterprise SOPs and 3,220 runtime variants under matched tools, environments, and evaluation. Step-by-Step remains more accurate for every evaluated model, but the gap has shrunk by about 79% from early models to the strongest recent model. We identify three routes to further narrowing this gap. Incremental workflow construction improves Global accuracy by an average of 9.98 percentage points (pp) without runtime execution feedback. Revising complete workflows with execution feedback improves all evaluated models, including 6.13 pp on held-out runtime variants. Targeted training on complete workflows improves accuracy by an average of 12.18 pp across all five trained models. Although a gap remains, global orchestration offers a promising path toward enterprise agents that deliver higher accuracy with fewer LLM calls.

---


### 69. [One Call Ahead: Packed Self-Speculative Decoding with Diffusion Drafting](https://arxiv.org/abs/2610.33379)

**<font color=#1a73e8>作者：</font>** Yuxiao Chen, Changxiao Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) language models generate tokens sequentially, so generating long outputs is costly. Speculative decoding mitigates this by using a lightweight drafter to propose multiple tokens for the target AR model to verify in parallel, while a diffusion-based drafter can produce an entire draft block in one forward pass. In models with AR and diffusion modes, one network both drafts and verifies, but drafting still waits for verification, so the standard schedule needs two sequential model calls per iteration. Existing one-call schedules avoid the wait but incur input size quadratic in the speculative width. Motivated by this efficiency bottleneck, we introduce Packed-SS, a self-speculative decoding schedule that verifies and drafts in a single model call with input size linear in the speculative width, while preserving the target model's distribution. The key idea is to let the diffusion drafter run one call ahead: while verifying the current draft, the model simultaneously constructs the next draft from an older verified prefix and keeps its unresolved suffix for the next iteration. Under a mild monotonicity assumption on the drafter, we further show that Packed-SS requires no more model calls than the standard two-call decoding in the greedy setting. Experiments on Nemotron 3B/8B and SetDLM 1.7B show higher throughput and lower mean wall time than both baselines under greedy decoding.

---


### 70. [How To Build A Modern Diffusion Language Model](https://arxiv.org/abs/2610.33391)

**<font color=#1a73e8>作者：</font>** Volodymyr Kuleshov, Marianne Arriola, Yair Schiff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The frontier of large language model (LLM) performance has advanced rapidly in recent years, fueled by scaling laws for pretraining on large text corpora. However, mainstream LLMs have fundamental limitations: they generate text autoregressively, producing outputs sequentially from left to right one token at a time. This sequential process leaves parallel GPU hardware underutilized during inference--a bottleneck that has grown acute as progress shifts toward scaling post-training and inference-time compute--and commits irreversibly to each token without the ability to revise earlier mistakes. Discrete diffusion models address these limitations by generating tokens in parallel, starting from a noisy or masked sequence and iteratively refining the entire output over a series of denoising steps. This parallel generative process enables speeds of thousands of tokens per second, provides a new axis of inference-time compute scaling, and supports built-in error correction and controllable generation. Over the past two years, discrete diffusion has scaled to billions of parameters across biological sequence modeling and natural language, with open-weights and commercial releases from leading labs. This article provides a survey of key ideas in discrete diffusion and a high-level introduction to how modern diffusion LLMs are built, covering their foundations, core algorithmic and architectural building blocks, applications in biology and language, and implications for future LLM scaling laws.

---


### 71. [Fast Instinct, Slow Reason: A Dual-Speed Agentic Framework for Self-Configuring Multi-Object Tracking in Satellite Video](https://arxiv.org/abs/2610.33396)

**<font color=#1a73e8>作者：</font>** Fan He, Baining Wu, Yan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking in satellite video underpins persistent monitoring, yet offline-tuned trackers lack the onboard intelligence and efficiency to adapt within an observation of tens of seconds. The root is that adaptation still means relabelling and retraining the detector, which cannot run on board in time. Tuning the tracker configuration strongly controls accuracy without touching the network, yet search needs labelled or proxy evaluations, and a language agent costs seconds and tokens per decision. We propose a dual-speed agentic framework pairing a fast instinct compiled offline with a slow reason serving the mission. Its algorithm, Arbitration of Unlabelled Shortlists from Prior Experience, or AUSPEX, learns a covering shortlist and a label-free ranker from labelled source tasks and commits one configuration per sequence. Its system, a Cascaded Onboard Runtime with Verified Uplinked Skills, or CORVUS, cascades reflex, skill, and agent layers, so that a verified skill commits 2.5 s into each observation while a language agent serves natural- language missions. On SatMTB and SatVideoDT with three recent detectors, AUSPEX raises IDF1 by 2.84 to 2.94 points and MOTA by 3.21 to 3.29 points on average without target labels, balances accuracy and labels best among sixteen methods, and loses at most 0.28 IDF1 points at 1.25 tracking passes. CORVUS executes four missions with execution accuracy up to 0.99 and target recall at the perception ceiling, spends no token on the routine decision, runs on Jetson Xavier NX, and hosts fifteen language models from six families without altering any commitment, demonstrating its extensibility and generalization.

---


### 72. [COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies](https://arxiv.org/abs/2610.33404)

**<font color=#1a73e8>作者：</font>** Hanming Zhang, Erhu Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLMs scale, mixture-of-experts (MoE) architectures increase model capacity while keeping per-token computation manageable through sparse expert activation. This sparsity also enables memory-efficient deployment by retaining most expert weights in CPU memory and transferring or executing only the routed experts on demand. Existing MoE offloading systems typically target specific model-platform configurations, yet differences in model sparsity, CPU and GPU throughput, VRAM capacity, and host-device bandwidth can change the policy ranking. Because implementing and exhaustively evaluating all candidate policies incurs substantial engineering cost, efficiently selecting the best-performing policy for each model-platform configuration remains a key challenge for practical MoE offloading.
We present COPE (Composable Offloading Policy Emulator), which selects the best-performing MoE offloading policy for a target model-platform configuration before runtime integration. COPE comprises two components. Its Policy Matrix factors the design space into two independent axes, expert residency and MoE execution strategy, enabling mechanism reuse across candidate policies and exposing four new candidates. Its Virtual Heterogeneous Machine profiles combined-operator schedules on the target platform and combines these measurements with offline routing traces to estimate candidate performance. Compared with the evaluated baselines, COPE improves fastest-policy selection accuracy by 24%-100% and reduces performance-prediction error by $1.7\times$ to $6.8\times$. By identifying the preferred policy before integration, COPE further reduces policy-specific implementation effort by up to 74%.

---


### 73. [Data Optimization for LLMs: A Survey](https://arxiv.org/abs/2610.33405)

**<font color=#1a73e8>作者：</font>** Ou Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have attracted great attention in both academic and industrial communities in recent years. Numerous survey studies have covered various aspects of LLMs, such as learning strategies, applications, alignment, explainability, and evaluation. However, little headway has been made in reviewing data-related aspects for LLMs, despite data being recognized as a key factor contributing to the emergence of the LLMs era. A wide range of data optimization algorithms and techniques are employed in LLMs' training and application processes. These techniques often originate from diverse deep learning domains, with their theoretical inspirations and heuristic motivations appearing unrelated to each other. This study aims to develop a comprehensive framework for LLMs' data optimization techniques to enhance data utilization and efficiency. We first discuss data challenges in LLMs' training and inference. Second, we summarize data perception dimensions for evaluating LLMs' data properties. These dimensions primarily include quality, difficulty, diversity, and redundancy, laying a foundation for subsequent optimization. Third, existing optimization techniques are reviewed and categorized into four groups: data selection, augmentation, reweighting, and others. Fourth, we analyze interconnections between these categories. Finally, we identify key challenges and future directions for LLMs' data optimization compared with conventional deep learning approaches.

---


### 74. [Agent-to-Agent Synthetic Social Engineering on the Web](https://arxiv.org/abs/2610.33411)

**<font color=#1a73e8>作者：</font>** Bryan C. Boots  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An AI agent can prepare an accurate report and still request an action its user has not authorized. Cooperation across Web services therefore requires separate judgments about identity, evidentiary support, and permission. We define synthetic social engineering (SSE) as deliberately deceptive or misleading influence intended to exploit AI recipients' responses to credibility, authority, or obligation cues and redirect behavior away from authorized objectives. We focus on separately tasked sender agents that produce or adapt misleading communication. Drawing on cybersecurity, social engineering, and persuasion research, we develop an operational framework connecting actors, deceptive representations, candidate influence routes, evidence or permission boundaries, responses, and consequences. The framework distinguishes attempts from successful redirection, without assuming human psychological processes. We implement it in the Agent Service Exchange and Evidence Commons (ASE-EC), a reproducible testbed with independently specified records and authorization scopes. Across 1,260 research episodes using Qwen3-4B in two fictional briefing tasks, matched comparisons test authority and commitment appeals, while defense comparisons assess protection alongside authorized task completion. Invoking a limited prior agreement increased unauthorized requests from 43.3% to 96.7%, although recipients retained supported decisions and permissions remained unchanged. These controlled findings identify action selection as a distinct security concern, even when evidence handling succeeds, and they provide a reusable basis for evaluating safeguards that preserve useful cooperation across Web services.

---


### 75. [AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos](https://arxiv.org/abs/2610.33413)

**<font color=#1a73e8>作者：</font>** Yuesheng Huang, Hoi Fan Au, Jiaqi Hou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localized AI manipulations in long-form videos often affect brief events within otherwise authentic content, making video-level classification insufficient for forensic analysis. Existing audio-visual deepfake benchmarks largely focus on short talking-head clips, while long-form temporal forensics remains predominantly visual. We introduce AV-FABLE, a dual-timeline benchmark for sparse manipulations in open-scene long-form audio-visual videos. AV-FABLE contains 16,650 pristine--manipulated twin pairs (998 hours) created with 27 editing configurations, with separate audio and visual timelines that enable modality-specific temporal localization and expose errors hidden by joint-timeline evaluation. On AV-FABLE, zero-shot prompting of audio-visual large language models (AV-LLMs) yields near-chance detection and poor temporal localization. In contrast, supervised readouts of their frozen perception features recover strong forensic signals, suggesting manipulation evidence is encoded in these representations but not effectively exposed through language outputs. Motivated by this observation, we propose NFSR(Native Forensics via Separated Readouts), which reads frozen AV-LLM features with separate audio and visual temporal decoders. NFSR achieves the best audio-visual localization performance in-domain and across all three out-of-distribution settings, including transfer to held-out videos from an external long-video forensic benchmark. AV-FABLE, code, and model weights will be publicly released.

---


### 76. [ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment](https://arxiv.org/abs/2610.33432)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Tenghao Ji, Jingruo Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is critical for autonomous Large Language Model (LLM) agents executing multi-session, long-horizon tasks. However, existing memories often inappropriately store, retain, or retrieve over-generalized, misattributed, or privacy-sensitive information, a problem we term memory misalignment. To study this problem, we construct \textbf{MemAlign}, a benchmark comprising 1,079 curated memory cases grounded in synthetic, validated multi-session conversational contexts covering diverse misalignment taxonomies. We then propose ConMem, an algorithm that reframes retention decisions as prospective counterfactual causal inference. \textbf{ConMem} synthesizes counterfactual interaction scenarios to prospectively audit downstream intervention effects across three aspects: relevant task execution, irrelevant invariance checks, and risk-sensitive boundary shifts. Experiments show that ConMem outperforms other methods, achieving 75.16\% accuracy, 64.15\% balanced accuracy, and a Macro-F1 of 65.31\%, effectively mitigating over-retention biases without sacrificing personalization utility.

---


### 77. [Examining form-based linguistic productivity in people and large language models](https://arxiv.org/abs/2610.33433)

**<font color=#1a73e8>作者：</font>** Michael Wilson, Robert Frank  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic productivity, as evidenced by the use of words in novel contexts, is one of the most striking facts about human language. However, how abstract the knowledge that enables such productivity is remains unclear. We compare people's and computational language models' linguistic productivity in contexts where successful generalization depends on form-based information. We focus on extending the use of a novel verb learned in the active voice to passive contexts. We find people extend active to passive uses in a way consistent with abstract generalizations concerning linguistic form, even when no plausible meaning can be assigned to the novel verb. In contrast, large language models succeeded only when a meaning like an existing verb's could be assigned to the novel verb. We conclude that computational models' syntactic knowledge remains tied to the distribution and meaning of specific lexical items in a way that human syntactic knowledge is not.

---


### 78. [Perturbation-Based Data Selection for Medical Question Answering](https://arxiv.org/abs/2610.33440)

**<font color=#1a73e8>作者：</font>** Yuexin Wu, Dayou Yu, Vasile Rus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Selecting a compact training subset is an important step in adapting medical language models from existing question-answering banks. We investigate perturbation-based data selection using two signals derived from Gaussian perturbations of the final-block representation: prediction-change frequency and non-flipping margin contraction. After a shared entropy prefilter, Representation-Sensitivity Prioritization (RSP) combines the signals using automatic root-mean-square scaling, while RSP-Drop ranks candidates by contraction alone. Both selectors use only questions and answer options during selection. We evaluate them with MedGemma-4B on five medical QA datasets at retained-set budgets of 64, 128, and 256 examples. At the primary budget of 128, RSP and RSP-Drop obtain dataset-averaged Macro-F1 scores of 47.55 and 48.28, respectively, compared with 45.11 for entropy-pool-matched random selection. Their relative performance varies across datasets and budgets. A selected-set case study identifies contrasting clean-margin profiles among the examples exchanged by the two rules, while a full-pool ablation shows that entropy prefiltering is not uniformly beneficial. These retrospective results characterize the empirical utility and limitations of perturbation-based selection under a fixed adaptation protocol. Evaluation uses one backbone and benchmarks with documented training-family overlap; it does not establish clinical effectiveness.

---


### 79. [Quantifying Meaning with SCAPE-T: Semantic Complexity from Encoder-Only Transformer Attention](https://arxiv.org/abs/2610.33441)

**<font color=#1a73e8>作者：</font>** Maxim Khovansky, Lev Mukhanov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated semantic complexity estimation remains underexplored in NLP, despite important applications in linguistics and interpretability. This paper defines semantic complexity as the code length required to uniquely specify a text's semantic meaning, and operationalises it via SCAPE-T, an attention-derived metric based on encoder-only transformers. Existing measures either model reader effort (readability, lexical difficulty), which correlates with surface features (word length, syntax), or quantify surface features directly (type-token ratio, word frequency). SCAPE-T targets semantic integration directly by combining three submetrics: (i) inverse-weighted self-focus (token-to-self), (ii) CLS focus (token-to-CLS), and (iii) inter-head redundancy (cosine similarity across heads), using layer-weighted aggregation; data-driven learning is confined to hyperparameter tuning for calibration. Development uses philosophical prose vs. MCTest stories; evaluation is on children's stories vs. technical Wikipedia articles, with pairwise accuracy on contrasts as the primary criterion. Baselines include readability, syntactic/lexical, and LLM-derived measures. SCAPE-T substantially outperforms all tested baselines under word-length control, with a pairwise accuracy of 78.5% (95% bootstrap CI: 76.1-80.4, N=10k pairwise comparisons; +12.7 percentage points over the strongest baseline); without that control, readability heuristics overtake, consistent with their reliance on surface features. On a short-terms abstractness dataset, SCAPE-T also leads. Ablations show each submetric contributes materially. Overall, the results show SCAPE-T isolates conceptual structure from lexical/syntactic confounds better than existing methods, and generalises across two held-out domains.

---


### 80. [Adaptive Transfer of Representational Signatures for LLM Reliability Detection](https://arxiv.org/abs/2610.33442)

**<font color=#1a73e8>作者：</font>** Yongtong Li, Yixuan Florence Wu, Jiawei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are reported to be susceptible to reliability issues including hallucinations and reasoning errors. Existing quality detectors can predict unreliable outputs based on internal representations with decent accuracies. However, training these detectors often requires substantial domain-specific labeled data, which limits their applicability to new domains. We propose to address this challenge by transferring representational signatures across related domains. More specifically, we build a statistical framework that first extracts low-dimensional signatures for each domain, then uses cross-fitting to learn composition weights of domain-specific predictors. The weights adapt to each source domain's predictive relevance to the target domain. Our asymptotic analysis of a least-squares analogue characterizes the limiting prediction risk and aggregation weights in terms of domain discrepancies and representation bias. Experiments across multiple hallucination datasets and open-weight LLMs show that, with only 25 labeled questions in the new domain, adaptive transfer improves hallucination-detection AUROC by 6.8%. For reasoning-step prediction, it improves AUROC by 8.4%.

---


### 81. [BoardSafety: AI-Ready Data from Manufacturer Documentation for Development-Board Safety](https://arxiv.org/abs/2610.33448)

**<font color=#1a73e8>作者：</font>** Linjian Yang, Xinyan Wang, Kunpeng Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of large language models (LLMs) are capable to assist with hardware experiments. In this scenario, this raises a practical question: Can LLMs determine whether a proposed operation is safe for a specific development board? Documented operating limits and safety requirements are board-specific, even across products from the same manufacturer. This variation makes board-specific safety judgments by an LLM difficult to evaluate. To address this problem, we introduce the BoardSafety Benchmark. The benchmark is built from vendor datasheets and hardware guides. For data transformation, these documents are converted into a board-specific safety rule base and are then used to create labeled operating scenarios. Each data item pairs a board and a proposed operation to an applicable safety rule with ground-truth label, indicating the level of safety. The categorized level for each operation includes safe, unsafe, or insufficient-info. In addition, the benchmark covers diverse operations, board-specific cases, boundary conditions, and missing-information cases. We evaluate a series of models by varying their access to board-specific rules and the use of structured-rationale prompting. Our results demonstrate that providing the safety rules generally improves accuracy, whereas structured-rationale prompting produces gains that vary across models and rule-access conditions. Overall, the evaluated models cannot yet reliably determine whether an operation is safe, which implies that critical exploration is required for this field.

---


### 82. [Secure and Functional Code Generation with Self-Evaluation](https://arxiv.org/abs/2610.33450)

**<font color=#1a73e8>作者：</font>** Md Afif Al Mamun, Gias Uddin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate functionally correct code that remains insecure. Security-focused fine-tuning can be expensive and is not always available, motivating inference-time approaches. Security-oriented prompting and retrieval can reduce vulnerabilities, but may also remove required behavior or apply defenses incompatible with the task. The challenge is to identify relevant security knowledge and use it to improve security without sacrificing functionality. We present SecGent, an inference-time framework that retrieves weakness context from the Common Weakness Enumeration (CWE) database and applies it to secure code generation. By connecting task specifications to relevant textual CWE records, SecGent provides task-specific security guidance without relying on retrieved vulnerable or patched code examples. Complementary functional and security tests check the resulting implementation, and their execution feedback guides repairs toward satisfying both objectives. We evaluate SecGent with four open-source LLMs and Claude Sonnet 5.5 across five programming languages on the CWEval benchmark. It achieves the highest joint functional--security success against four inference-time baselines for all five models. Across the open-weight models, mean functional-security@1 (FS@1) improves by 15.5% over RAG, with gains in both functionality and security, and by 19.8% over the strongest prompt optimizer compiled for each model. On Sonnet, FS@1 reaches 92.1%, outperforming the strongest baseline AutoGen by 4.8%. In a separate comparison, SecGent outperforms Claude Code with security-focused prompting by over 6% in FS@1. Feedback-guided repair further improves FS@1 by up to 6.7% over generation without feedback, primarily by recovering functionality while checking security.

---


### 83. [A Comprehensive Framework for All Stages of Large-Model Training: From Data and Tokenization, through Pretraining, to Post-Training Alignment](https://arxiv.org/abs/2610.33451)

**<font color=#1a73e8>作者：</font>** Xiangjing An, Zhibin Jiao, Aiting Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The capabilities of large language models (LLMs) and multimodal LLMs (MLLMs) arise from the synergy of the full training pipeline, including data and tokenization, pretraining, and post-training (supervised fine-tuning, preference alignment, reinforcement learning, and continual optimization), rather than any individual stage. Existing surveys mostly adopt a single-stage or single-technique perspective, treating related research as isolated systems without unified stage division or a horizontally comparable basis.
This paper proposes a unified stage division and a six-dimensional analytical framework covering data, objective function, optimization strategy, system constraints, evaluation, and risk and governance. We systematically review 395 core references from 2017 to 2026, and present a conceptual map of cross-stage effects: forward constraints of pretraining on post-training, and reverse empowerment of post-training on data and pretraining.
We derive three core findings. First, the comparability of scaling laws depends on data quality and mixture, a long-neglected variable. Second, preference alignment methods (RLHF, DPO) and reasoning reinforcement learning with verifiable rewards redefine post-training boundaries, while the Pass@1 versus Pass@K debate remains unresolved. Third, multimodal training poses structural challenges to the pure-text paradigm in tokenizer design, training objectives, and evaluation.
The paper provides a cross-stage effects diagram, a method-family map, a practical decision tree, and at least 10 verifiable open problems, with an extensible skeleton for focused sub-surveys per stage. As of the retrieval date, peer-reviewed evidence (A+B) accounts for approximately 79% of the 395 references.

---


### 84. [Propasafe-Hybrid: A Text-Based Hybrid Propaganda Detection Tool](https://arxiv.org/abs/2610.33464)

**<font color=#1a73e8>作者：</font>** Thomas Kimmeth, Avijit Roy, Vivek Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Propagandistic content increasingly circulates through online news and social media, where readers often encounter it with limited scrutiny, highlighting the need for reliable and fine-grained detection. This paper introduces Propasafe-Hybrid, a sentence-level system that integrates a fine-tuned transformer classifier with LLM-based technique classification to identify, label, and explain specific propaganda strategies. The pipeline generates actionable outputs, including highlighted sentences, technique assignments, and concise rationales, so users can immediately understand why a sentence was flagged and how each label was determined. To control inference cost, Propasafe-Hybrid employs a cost-aware pre-filtering stage that forwards only high-likelihood sentences to LLMs, reducing token usage while preserving the underlying decision logic. Together, these design choices enhance the explainability, efficiency, and practical usability of sentence-level propaganda detection in real-world news environments.

---


### 85. [Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement](https://arxiv.org/abs/2610.33472)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Yanran Zhang, Shengming Yin 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning visual design is essential for prompt enhancement (PE) to turn underspecified user requests into coherent visual specifications for text-to-image (T2I) generation. Existing methods preserve user intent and improve overall visual appeal, with less explicit emphasis on fine-grained design dimensions. To address this gap, we introduce Qwen-Image-PE, which learns visual design through two-stage training. Supervised fine-tuning with Caption-Based Reverse Distillation (CRD) uses dense captions of well-designed images as design supervision. Reinforcement learning with Groupwise Design Reward (GDR) jointly compares all candidate images for the same request to refine lighting, composition, layout, and detail. On Qwen-Image-Bench with Qwen-Image-2.1, Qwen-Image-PE-397B improves over original requests by 7.81 points, while Qwen-Image-PE-9B outperforms all evaluated PE baselines. Further evaluations show gains in visual design, aesthetics, image quality, and human preference. We find that PE scales along three axes: training data, model size, and information density, with sufficient information density as a prerequisite for effective enhancement. Moreover, we demonstrate that Qwen-Image-PE generalizes to four additional T2I backbones, even surpassing native prompt enhancers on HunyuanImage-2.1 and FLUX 3 Image Klein. We release Qwen-Image-PE-9B at this https URL.

---


### 86. [MarineLife-16K: An Attribute-Rich Video-Text Dataset for Motion-Aware Marine Video Understanding](https://arxiv.org/abs/2610.33478)

**<font color=#1a73e8>作者：</font>** Quang-Trung Truong, Thanh-Nghia Nguyen, Phu-Phong Vo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Marine video understanding is crucial for a wide range of real-world applications. However, existing marine video datasets suffer from limitations, including the limited number of data samples, fine-grained text descriptions, and detailed visual attributes. To address these limitations, we introduce a large-scale, video-text dataset featuring rich, in-the-wild visual attributes tailored for complex marine environments. Our dataset comprises 2,000 video-text pairs annotated with 13 attributes covering up to four objects per scene, object visual/geometric properties, behaviors, environmental context, and camera motion, spanning diverse lighting conditions, times of day, and 7 countries. From these annotations, we generate 16,080 video-question pairs (12,080 multiple-choice, 4,000 open-ended). Furthermore, we benchmark both proprietary and open-source video-LLM models on video question answering and video captioning tasks. We find that (i) proprietary models often achieves superior performances; (ii) VLMs handle object motion well but struggle with complex camera motion; (iii) closed-source models struggle to perceive camera motion; and (iv) VLMs struggle to reason in static cameras.

---


### 87. [Incremental Predictive Value of LLM Tutoring Interactions for Student Performance](https://arxiv.org/abs/2610.33488)

**<font color=#1a73e8>作者：</font>** Zeyu Dong, Mikael Kwame Kuada, Asa Holley Buchakjian-Tweedy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate whether semester-level interaction features from a large language model tutor improve assignment-score prediction beyond constant baselines. StudyChat provides 16,851 student-assistant exchanges from two offerings of an undergraduate artificial intelligence course, with outcomes matched to 175 of 203 student-semester records. Six fitted estimators and training-fold mean and median baselines share repeated nested cross-validation. After averaging each student's held-out predictions across ten repeats, Gradient Boosting achieves mean absolute error of 3.023 grade points, versus 3.138 for the median baseline. The paired difference is -0.114, with a conditional 95% bootstrap interval of [-0.245,0.013]. Representation changes and a semester-specific median yield similarly small gains. In the lowest observed-score quartile, however, boosting's error is 7.30 points, versus 8.07 for the median and 6.67 for the mean; Ridge has the lowest fitted-model error at 6.37 despite its worse overall error of 3.331. Scores concentrate near the ceiling: 160 students (91.4%) score above 90, and the lowest quartile contributes 62.1% of boosting's total absolute error. This retrospective comparison shows how baseline choice and error distribution affect predictive value, informing evaluation of student-support tools without establishing a learning effect.

---


### 88. [From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code](https://arxiv.org/abs/2610.33489)

**<font color=#1a73e8>作者：</font>** Shiwu Zhao, Baizhu Wang, Guoqiang Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered agents increasingly rely on third-party skills that combine natural-language instructions with executable code, creating supply-chain risks that may span both artifacts. Existing skill scanners often rely on rule matching or direct LLM judgments and provide limited support for tracing such cross-domain behavior. We present the Supply-Chain Scanner for Agent Skills (SCS), a static analysis framework that unifies instructions and code for security analysis. SCS compiles natural-language instructions into a constrained Python-style intermediate representation using a limited set of security-oriented APIs. It then constructs program dependence graphs for instructions and bundled code and connects them into a cross-domain graph (xPDG). A Trust-Sensitivity-Capability (TSC) model propagates security properties over the graph to support structured, largely deterministic risk detection. On a manually verified benchmark of 117 malicious and 117 benign skills, SCS achieves the highest average accuracy (85.6%), recall (95.2%), and F1-score (86.9%) among evaluated methods across five LLMs, with 80.2% precision and average token consumption of 13.7 million. Its NL-to-IR compiler achieves 92.5%-94.5% step-level correctness on 400 human-annotated instruction steps. Finally, analyzing 66,157 real-world ClawHub skills yields 2,473 candidates, of which 627 are confirmed malicious through auxiliary dynamic validation and manual review.

---


### 89. [Small Edits, Shifting Decisions: Benchmarking LLM Accuracy and Reliability on French Input Variants](https://arxiv.org/abs/2610.33493)

**<font color=#1a73e8>作者：</font>** Jiaming Yu, Xiaotian Xie, Jian Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> French users may omit apostrophes and diacritics or make keyboard typos in everyday input. The effects of these common variations on language model performance and prediction reliability remain insufficiently understood. To address this gap, we construct a controlled French surface-variant benchmark covering seven task types, with 4,200 original-low-high triplets (12,600 input instances). Each high-intensity variant retains all low-intensity edits and adds further changes. We evaluate six models from two LLM families. The results show that accuracy decreases and Brier score and negative log-likelihood (NLL) increase with perturbation intensity. Larger models show smaller accuracy losses under high intensity, but increases in Brier score and NLL do not consistently decrease with scale. Keyboard typos cause the largest losses in accuracy and the quality of predicted probabilities at the predefined high-intensity settings. Finally, calibration temperatures fitted on original inputs transfer effectively to surface variants. Combining calibration with input restoration further improves Brier score and NLL over either method alone while preserving restored accuracy. Our benchmark provides a unified framework for jointly evaluating task accuracy and prediction reliability under common French surface variations.

---


### 90. [Five Architectures, One Shared Space Cross-Model Representational Alignment Without Weight Merging](https://arxiv.org/abs/2610.33495)

**<font color=#1a73e8>作者：</font>** Oladimeji Anthonio, Dimeji Olawuyi, Oloruntoba Ajayi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Combining language models is usually done by averaging weights, which works only when the models share a common starting point. We ask whether five frozen, independently trained models with different internal designs (four transformers from four organizations and one state-space model) can be related through their activations alone, with no weight merging. Using permutation tests, an independent replication probe set, depth sweeps, pooling ablations and confound checks, we find statistically robust correspondence between how the five models organize the same text. It is strongest at each model's final layer and weaker for the state-space model, whose weakest pairing is still 35-43 times chance. We use this to build a shared space with Generalized Procrustes Analysis, in which no model is a fixed reference. At the final layer, mean held-out retrieval accuracy over the twenty ordered model pairs is 0.91 to 0.93 on two probe sets (chance 0.03), beating pairwise linear maps (0.82 to 0.85), but the space is worse than those maps in the middle layers. It transfers to ordinary English of unfamiliar grammatical form and fails on mathematical and logical notation. We then test whether the space supports a router that picks among the five models on gradeable tasks. Across four task types we find no case where routing beats always using the strongest model, and we report this as a negative result. A correctness signal that looked strong turned out to be category membership in disguise. All experiments ran on one laptop without a GPU.

---


### 91. [FedSEAM: Federated Continual Learning of LLMs via Subspace Expert Agreement Merging](https://arxiv.org/abs/2610.33496)

**<font color=#1a73e8>作者：</font>** Fatema Siddika, Abhijit Chunduru, Zilinghan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated continual learning trains a model on a sequence of tasks across several clients without sharing their data while retaining knowledge of earlier tasks. Sparse mixture-of-experts models support this setting by adapting selected parameters on a frozen backbone. However, clients learn different expert content as tasks evolve, making it difficult to share knowledge across clients without disrupting task-specific and client-specific specialization. Matching tile coordinates alone does not establish whether their learned content is compatible. We present FedSEAM, a federated continual learning framework that organizes task knowledge into sparse experts and selectively shares their content across tasks and clients. On each client, task-aware tile selection allocates capacity to a new task, while a subspace-based compatibility test determines which existing expert tiles to reuse and where to introduce fresh capacity. On the server, Subspace Expert Agreement Merging (SEAM) compares client updates as subspaces and moves each client towards consensus only along agreed-upon directions, leaving the rest of its update unchanged. We identify two remaining sources of forgetting, routing drift and merge erasure, and address them with three protections, one of which exactly preserves tile components in a selected prior-overlap subspace at every merge. We evaluate FedSEAM on TRACE using Qwen3-4B and Llama-3.2-3B, with component-wise ablations and studies of data size to assess its balance between learning new tasks and retaining prior knowledge.

---


### 92. [Towards a Learnable Retriever for Textual Graph Question Answering](https://arxiv.org/abs/2610.33511)

**<font color=#1a73e8>作者：</font>** Kaifeng Jin, Yuchen Yan, Zhichen Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Textual graph question answering (GraphQA) and graph-based retrieval-augmented generation (GraphRAG) have gained increasing attention as a way to ground large language models (LLMs) on structured knowledge. Despite extensive efforts, existing methods still face two key gaps. The first is an architectural gap: existing methods typically fine-tune an LLM-based generator, but do not also make the retriever itself a learnable LLM for graph evidence selection within one end-to-end retrieve-then-generate pipeline. The second is a retrieval-supervision gap: existing retrievers rarely use gold answer signals to supervise evidence selection. As a result, they may fail to recall evidence nodes required for reasoning, resulting in insufficient coverage of the gold answer set; meanwhile, naive attempts to boost recall often introduce excessive irrelevant information that compromises compactness and overwhelms the LLM. To address these gaps, we propose TaLenT, an LLM-based end-to-end retriever-generator framework for textual GraphQA. To bridge the architectural gap, TaLenT pairs a learnable LLM-based retriever for evidence selection with a fine-tuned LLM-based generator within one unified retrieve-then-generate pipeline. To bridge the retrieval-supervision gap, we leverage gold answer signals as retriever supervision. Specifically, we stratify graph nodes into gold answers, answer-related nodes, and irrelevant noise. We then adopt a weighted pseudo-label loss to prioritize gold answers and preserve answer-related nodes for coverage, while discarding irrelevant noise for compactness. Experimental results across three GraphQA datasets demonstrate that TaLenT consistently improves downstream performance.

---


### 93. [One Model, Two Paths: Balancing Single-Pass and Looped Performance in Language Models](https://arxiv.org/abs/2610.33517)

**<font color=#1a73e8>作者：</font>** Jiarun Shen, Lei Zhao, Xiao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeating Transformer layers can improve language-model performance without adding parameters. A pretrained model can be adapted to support both single-pass and looped inference by reusing middle-layer weights for additional computation. Because both paths share weights, training to improve looped predictions can degrade single-pass quality. We study joint training strategies using weighted losses on both outputs, with guidance from the frozen original model. Joint supervision substantially reduces single-pass degradation compared to looped-only training, while preserving looped gains over ordinary continued training. Most of this benefit comes from adjusting the single-pass loss weight, with guidance from the frozen original model further improving the looped output. With validation-selected weights, our method preserves single-pass quality within a predefined tolerance of ordinary continued training while improving looped predictions.

---


### 94. [Implicit Beliefs as Scalable Process Rewards for Strategic Persuasion](https://arxiv.org/abs/2610.33527)

**<font color=#1a73e8>作者：</font>** Minqian Liu, Yuexi Shen, Heajun An 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) for multi-turn strategic persuasion faces two coupled obstacles: (i) realistic simulation of psychologically grounded persuadees, and (ii) dense, faithful supervision for credit assignment in strategic dialogues. Outcome-only rewards are sparse and uninformative about which conversational moves drove success, while LLM-judge process rewards are expensive and decoupled from the underlying interaction dynamics. We address both challenges with a unified framework. First, we introduce PersuArena, a persuasion simulation environment that produces realistic, non-monotonic trajectories. Second, building directly on this environment, we propose Process Rewards via Online Belief Elicitation for Relative Policy Optimization (Probe-RPO), an online RL framework that converts the persuadee's internal state into dense process rewards. At each turn, three introspective probes are read from the frozen persuadee's logits, yielding a multi-dimensional reward signal that is faithfully aligned with persuasion dynamics. With extensive experiments on PersuArena spanning healthcare, financial advising, workplace management, education, and personal relationships, we demonstrate that our Probe-RPO achieves the full acceptance rate of 52.5%, compared with the 35.8% for the strongest GRPO ablation and 25.8% for the best off-the-shelf LLM. We also conduct comprehensive analyses on the generalization across persuadee models and the persuasion dynamics across conversations. Our work offers a promising paradigm that can provide effective process supervision for strategic dialogue.

---


### 95. [FraudSociety: A Generative Agent-Based Society for the Financial-Fraud Economy](https://arxiv.org/abs/2610.33536)

**<font color=#1a73e8>作者：</font>** Keyang Chen, Mingxuan Jiang, Zeping Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial fraud caused over \$15.9 billion in losses in the United States in 2025, according to the Federal Trade Commission~\citep{ftc2026databook}. Understanding such large-scale harm requires jointly modeling informational and financial dynamics. Yet existing simulators typically capture only one side of this interaction, leaving a gap in modeling how fraud unfolds in the real world. To bridge this gap, we introduce \textsc{FraudSociety}, the first LLM-agent-based simulator that jointly models these coupled dynamics. It integrates a dynamic social environment for information exposure and communication, persistent financial ledgers that preserve payment and loss histories, and a Need-Intent-Action architecture for civilian decision making. Fraudsters further adapt their communication and financial actions to individual interaction histories and ledger states, forming a closed feedback loop between the two dynamics. We validate \textsc{FraudSociety} across macro-level outcomes, micro-level behavior, and intervention effects. At the macro level, the simulated fraud outcomes closely match real-world patterns across multiple key statistics. At the micro level, it reproduces strong loss concentration, with the top 10\% of victimization records accounting for 81.1\% of total losses, consistent with Canadian Anti-Fraud Centre statistics~\citep{cafc2025annual}. Counter-fraud experiments further reveal variation across intervention strategies, with the best-performing personalized intervention reducing the repeat-payment rate from 49.4\% to 10.9\%. These results establish \textsc{FraudSociety} as both a high-fidelity simulator and a scalable testbed for evaluating anti-fraud strategies under diverse intervention conditions, thereby advancing research on financial fraud and its prevention.

---


### 96. [CoEvolve: Counterfactual-Guided Co-Evolution of Memory and Collaboration in Multi-Agent Systems](https://arxiv.org/abs/2610.33539)

**<font color=#1a73e8>作者：</font>** Xufei Shi, Derong Xu, Wei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems have demonstrated remarkable capabilities across diverse tasks. Yet their memory and collaboration architectures often remain static, constraining continued adaptation and improvement over time. Recent work addresses this limitation by evolving memory or collaboration based on interaction experience. However, updates to these interdependent components are not necessarily aligned: an evolved workflow may require experience that memory does not provide, while evolved memory may encode guidance that the workflow cannot use. To address this problem, we propose CoEvolve, a skill-centered framework for aligned memory--collaboration evolution. CoEvolve represents reusable local collaboration patterns as skills that link evolving collaboration decisions to their supporting memories. It further compares original and counterfactual trajectories to identify local evolution signals, which coordinate updates to the skill library, skill memory, and executor memories across rounds. Experiments on the ALFWorld and WebShop benchmarks confirm that CoEvolve achieves the best overall performance among the evaluated baselines, while ablation studies further validate the effectiveness of aligned co-evolution and counterfactual-guided evolution.

---


### 97. [SEDATE: Do Large Language Models Share an Aggression Circuit Across Languages?](https://arxiv.org/abs/2610.33542)

**<font color=#1a73e8>作者：</font>** Sagnik Basu, Sayan Das, Somnath Banerjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As the applications of AI continue to expand across various multimodal and multilingual domains, ensuring safe and responsible deployment of these systems has become an important concern. A wide-range of interventions have been proposed to make AI responses safer and more reliable. They often incur substantial computational or annotation costs, or cannot be extended to multilingual settings. In this work, we propose Selective Detection And Targeted Editing (SEDATE), a training-free approach based on detect-edit-verify strategy. SEDATE first detects the responsible neurons, edits them as and when necessary and finally verifies the model responses; all without any additional model training. We evaluate SEDATE across 7 languages and 4 model families. We further evaluate its effectiveness across 4 out-of-distribution languages and 4 additional datasets. We show that SEDATE achieves substantially superior safety scores across all languages and models over the best-performing baseline while retaining the general capabilities and incurring negligible overhead. Our results are robust, with the trends remaining similar for out-of-distribution languages and datasets.

---


### 98. [GeoLift: Grounding Video Spatial Reasoning in Explicit 3D Maps](https://arxiv.org/abs/2610.33558)

**<font color=#1a73e8>作者：</font>** Xinglin Li, TingTing Long, Jingzhi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video spatial reasoning requires multimodal large language models (MLLMs) to understand how objects are arranged and related across viewpoints. While these models can recognize objects in individual frames, integrating these observations to solve complex spatial tasks remains challenging. We examine route planning as a representative task and observe that existing models become substantially less accurate as the number of required turns increases, with several models achieving accuracy close to random guessing on routes requiring three or more turns. This finding suggests that recognizing landmarks alone is insufficient: models must also connect observations across viewpoints and track how landmarks are arranged in a shared space. Motivated by this observation, we introduce GeoLift, a training-free framework that uses feed-forward 3D reconstruction to map objects detected in individual frames into a shared metric 3D scene. GeoLift combines a frozen MLLM for 2D grounding with pretrained geometry models for scene reconstruction. It then uses shared geometric regions, called superpoints, to associate observations of the same object across views without a learned matcher. The reconstructed 3D map enables explicit computation of spatial relations and multistep routes, and provides geometric evidence for estimating distances and sizes. With all model weights frozen, GeoLift improves Qwen3-VL-4B's average score on VSI-Bench from 55.4% to 64.1%, including an increase in route-planning accuracy from 30.9% to 53.6%, and achieves 59.8% accuracy on MindCube. These results show that connecting frame-level object grounding through a shared 3D map can improve complex spatial reasoning without task-specific training.

---


### 99. [What Remains OOD? OODConceptBench for Open-World Concept Recognition in Vision-Language Models](https://arxiv.org/abs/2610.33564)

**<font color=#1a73e8>作者：</font>** Zhiran Luo, Zhiyong Yang, Zitai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of large-scale pretrained models, zero-shot generalization has increasingly blurred the boundary between known and unknown concepts. However, current evaluations do not directly reveal which open-world concepts different vision-language models can recognize. To study this problem, we introduce OODConceptBench, a hierarchical benchmark for open-world concept recognition on image-concept pairs. The full benchmark set (L1) contains 30,752 images, and the harder subset (L2) contains 14,285 images. The benchmark covers 560 concept phrases across seven open-world categories. We evaluate 37 vision-language models across release year, model family, and variant. We obtain three main findings. First, target-concept recognition is lower on L2 than on L1 across all 37 evaluated models. Second, later-released models do not necessarily achieve stronger open-world concept recognition. Third, an increase in overall recognition does not imply consistent improvement across all benchmark categories. Together, these results show that OOD remains a challenge even in the era of large-scale vision-language pretraining.

---


### 100. [Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents](https://arxiv.org/abs/2610.33568)

**<font color=#1a73e8>作者：</font>** Yihao Hu, Zhihao Wen, Yitong Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Successful tool-use trajectories are not necessarily useful supervision. Even successful interactions may underrepresent multi-step dependencies or contain actions that are unjustified by the information visible to the agent at decision time. We identify two coupled requirements for effective trajectory supervision: compositional coverage, so that important observation-action dependencies are represented, and decision grounding, so that each supervised action is supported by the learner-visible interaction history. We introduce Trajectory2Gym, which constructs executable interactions around under-supported compositional structures and derives supervision only from grounded decisions in their realized executions. Structural-support selection allocates the resulting experience, while parent-normalized supervised fine-tuning preserves the semantic interaction as the unit of training weight. This reframes trajectory generation as the deliberate construction of learnable interaction experience, rather than the collection of successful trajectories. Across five Qwen3 scales, Trajectory2Gym improves Tau1, Tau2, and BFCL at every tested scale, increasing the equal-weight three-benchmark mean by 16.9-29.8 percentage points. The gains are strongest in stateful and multi-turn interaction, where later decisions depend on earlier observations and feedback. Our results suggest that scaling tool-use agents depends not only on collecting more successful trajectories, but on constructing interactions whose dependencies are represented and whose decisions are learnable from the agent's visible history.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
