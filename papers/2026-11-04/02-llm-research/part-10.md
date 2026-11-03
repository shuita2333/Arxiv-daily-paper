# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-515](./part-11.md)

---

### 451. [Every Pixel Is an Option: A System One Model for Medical Ultrasound Biometry](https://arxiv.org/abs/2611.03360)

**<font color=#1a73e8>作者：</font>** Moein Heidari, Junbo Rao, Yudan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> **Purpose:** Ultrasound biometry is widely used across various clinical applications, including prenatal and cardiac examinations, to obtain quantitative measurements by placing calipers at anatomical landmarks. However, these measurements remain subject to interoperator variability as they rely largely on manual caliper placement. Conventional methods often use specialized prediction heads for different ultrasound tasks, whereas vision-language models offer flexibility through text instructions. However, direct coordinate prediction does not explicitly model spatial likelihood distributions, limiting the representation of localization ambiguity.
**Methods:** We propose Kev-Bio, a vision-language model that uses clinical measurement questions to guide ultrasound landmark detection. Inspired by System One decision models, Kev-Bio uses decision representations of the language model to generate queries for each caliper endpoint. These queries are matched against shared dense ultrasound features to produce spatial probability maps, from which landmark coordinates and clinical measurements are derived. The model is trained end-to-end using both landmark localization and clinical measurement losses.
**Results:** On the nine-view FU/GU Biometry 2026 dataset, Kev-Bio achieves a mean radial error (MRE) of 22.50 pixels and a clinical measurement mean absolute error (MAE) of 15.38, outperforming the compared baselines in overall performance.
**Conclusion:** These results demonstrate the effectiveness of Kev-Bio for ultrasound landmark detection and clinical measurement across different anatomical views. Our code and models are available at this https URL.

---


### 452. [EO-Jev: Decision Model for Earth Observation](https://arxiv.org/abs/2611.03371)

**<font color=#1a73e8>作者：</font>** Mohamed Atef Abouelhadid, Diaa Addeen Abuhani, Muhammad Akhtar Munir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation (EO) workflows require selecting among known outcomes, estimating confidence, and processing large volumes of imagery. Generative vision-language models can address these tasks, but autoregressive decoding is computationally costly and their confidence estimates are unreliable. Decision models offer an alternative, returning probabilities over candidate answers in a single forward pass. However, their accuracy, calibration, and transfer across EO tasks remain insufficiently understood. We investigate these properties through a diagnostic study of d3-flash (8.4B parameters) across 30 settings from 23 public EO benchmarks. We find that compositional reasoning transfers well and calibration improves over its Qwen3.5-9B backbone on 24 settings, while counting, change quantification, damage grading, and absent-object recognition remain challenging. To address these limitations, we adapt d3-flash through low-rank fine-tuning on public EO training splits, producing EO-Jev. EO-Jev improves significantly over d3-flash on 26 of 30 settings and matches or exceeds specialist references on 20 of 28. It also achieves an average gain of 8.0 points across 12 held-out settings and lower expected calibration error than specialists on 21 of 28 settings. These improvements come at a modest cost of 1.8 points in general decision performance. Our results demonstrate the potential of adapting general decision models into competitive EO generalists while highlighting persistent challenges in quantitative perception, option-order consistency, and calibration under distribution shift.

---


### 453. [Characterizing When Language Models Take Harmful Actions to Protect Their Assigned Goals](https://arxiv.org/abs/2611.03374)

**<font color=#1a73e8>作者：</font>** Brandon Jaipersaud, Elliot Creager  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent language model (LM) safety failures have largely been studied as disparate phenomena. In agentic misalignment, a model blackmails an executive to avoid being replaced. In alignment faking, it complies with harmful requests during training to keep its values from being modified. We argue that these behaviours share a common decision structure: a model assigned a goal must either take a harmful action to preserve it or refuse and lose it. We formalize this as a goal-harm conflict and present the same conflict under various elicitation protocols that range from compact forced-choice prompts to simulated agentic environments. These protocols span two perspectives on LM decision-making, which we term (i) the logit view, reading preferences from answer-token probabilities, and (ii) the sampling view, classifying open-ended responses with an LM judge. Under the logit view, we show that goal importance and harm severity additively shape how a model resolves these value conflicts. Under the sampling view, we derive two factorizations of the harmful-action probability that safety evaluations commonly report. The first measures how well a preference read from answer tokens carries over into behaviour, such as making a harmful tool call. The second attributes a low harmful-action rate either to refusal or to responses that reach no resolution. We then show how fictional context changes a model's preference under the logit view, and how tool use and partial observability -- two features of agentic evaluations -- change its harmful-action rate under the sampling view. Our work offers a descriptive framework for studying how LMs resolve such value conflicts and for estimating low-probability harmful actions at a finer granularity than the aggregate harm rates commonly reported in safety evaluations.

---


### 454. [Same Outputs, Different Scores: Auditing the Unchecked Graders of Multimodal LLM Benchmarks](https://arxiv.org/abs/2611.03377)

**<font color=#1a73e8>作者：</font>** Ahmad Jarjis Hasan, Jonathan Lwowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every multimodal-LLM multiple-choice benchmark ends with a scoring rule that converts a model's response, often free-form text rather than a clean option letter, into a right/wrong verdict, buried in its code. Unlike the dataset, this rule is chosen without justification and left unexamined, yet it sets the published number. We reproduce the official scorers of eight peer-reviewed benchmarks on five open vision-language models (VLMs) that fit a single 16 GB GPU, and introduce a blinded human-plus-LLM-judge adjudication (Cohen's kappa=0.956) that recovers what the model actually answered. The scoring rule alone moves accuracy by up to 22 points on identical outputs, yet exactly 0 wherever a model emits clean option letters, so it hides on strong-model leaderboards. It is the fallback and not the rambling that does the damage: the benchmark with the highest non-compliance we measure has an artifact of exactly zero, because its scorer abstains instead of guessing; a reasoning model with non-compliance 0.000 still swings 9.5 points with which regex match of its trace the parser keeps. No standard rule is reliable: snapping a non-answer to its closest option credits answers never given yet buries correct ones, abstention discards answers stated in words, and likelihood scoring follows answer-token priors, so a single grade conflates capability with luck rather than measuring either. We release all code, labels, and the protocol, and argue benchmarks should report a non-compliance rate and at least two rules, not one unexamined grade.

---


### 455. [Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents](https://arxiv.org/abs/2611.03384)

**<font color=#1a73e8>作者：</font>** Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introduce PROMOTE, a protocol that assigns every candidate predictable testing wealth at birth and accumulates a cost-aware e-process only from subsequent returns. If lifetime allocations sum to at most one, a weighted Ville argument bounds the probability of ever promoting a rule whose declared bounded net score has always had nonpositive conditional mean. The result permits dependent candidates, adaptive births, and indefinite monitoring. We audit the implementation in two settings. A retrospective pseudo-out-of-sample replay contains 24 panel--rule hypotheses, 3,000 shared-sign null paths, injected alternatives, and public ETF and industry data. Repeated unadjusted tests produce a family crossing in 94.5% of null paths, versus 0.0% for PROMOTE; at a 15-bp aligned ETF-component perturbation, PROMOTE has 70.1% target power and median crossing session 2,327. A separate exact mean-zero experiment lets an agent select candidate identities and birth times from past scores; the funded gate has 1.77% false-family crossings across 3,000 programs. The market replay produces zero promotions after costs. The certificate controls historical false promotion under the declared null; it is not a certificate that an earlier edge remains profitable at deployment. AI-use disclosure. Generative AI tools, including OpenAI Codex, assisted manuscript preparation. For this preprint version, Codex assisted with LaTeX editing, author and venue metadata, compilation, and layout checks.

---


### 456. [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412)

**<font color=#1a73e8>作者：</font>** Yumou Liu, Mingju Chen, Zhoufutu Wen 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a time, leaving a gap between the capability we measure and the outcome that makes agents useful. To address this gap, we introduce DeliverBench, which tests whether agents can carry a project from brief to final delivery. Its 11 projects, spanning financial due diligence, legal contract drafting, and drug safety reporting, are reconstructed with 13 domain experts from real materials and chain 150 subtasks through 2-15 rounds of new materials and client feedback. Because no reference outputs are injected, agents inherit their own errors from one task to the next. Expert rubrics then score every checkpoint as well as the final package. Across seven model-harness systems, even the best system scores only 65.0 out of 100 on final delivery and passes 50.0% of subtasks at a 90-point threshold. The failures are often failures of carrying work forward: in one audit project, all seven systems addressed the review findings, but only one preserved traceability. Together, these results suggest that task-level capability does not simply compose into delivery, which also depends on keeping the work coherent as it evolves.

---


### 457. [IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?](https://arxiv.org/abs/2611.03424)

**<font color=#1a73e8>作者：</font>** Shanshan Zhong, Chen Xu, Jingjie Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research taste, the judgment of what to read, which problems to pursue, and which methods to try, increasingly shapes the work of AI scientists, yet it remains far less understood than their ability to execute research. We introduce IdeaTaste, a benchmark that scores an LLM by how closely the research proposals it writes from a literature snapshot frozen at 2025 match the work the same communities published in 2026. Our experiments span six contemporary language models and four research areas from established to emerging fields, covering more than 90{,}000 proposals in total. LLM agents fall well short of human communities in both the literature they cite and the ideas they state, reaching about 26\% of the human level on citation matching and only 18\% on idea matching. Their populations can cite as diversely as a community and take up its tasks and methods, yet rarely arrive at the concrete approaches and research plans it pursues. Neither richer field context nor larger populations substantially close this gap. In blinded expert review, AI proposals trail the 2026 papers least in presentation and most in expected success, echoing their gap in concrete approaches, and those whose ideas no human paper shares fare worst, suggesting weaker directions rather than overlooked opportunities. These results indicate that the main bottleneck in AI research taste lies less in finding the directions a community works on than in turning them into the concrete approaches it goes on to pursue. We release IdeaTaste as an open, continuously updated leaderboard (this https URL) that benchmarks contemporary AI proposals against future publication cycles.

---


### 458. [A Living Leaderboard for Graph Machine Learning](https://arxiv.org/abs/2611.03433)

**<font color=#1a73e8>作者：</font>** Martin Ritzert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph machine learning benchmarking results are scattered across papers that use quite different sets of datasets and baseline methods, making it difficult to tell whether a reported gain reflects architectural progress or merely an outdated comparison or weakly tuned baseline. We introduce a living, graph-learning-specific leaderboard that organizes reported results by dataset, putting new results into context. As of 15 October 2026 our LLM-based extraction pipeline extracted 27,723 eligible results across 111 datasets from 885 peer-reviewed papers. Our analysis of these results quantifies concerns about graph-learning benchmarking: legacy datasets are still actively used and many result tables contain baseline results that are drastically lower than those already available in the literature, e.g. 45% Amazon-ratings tables and 37% for Peptides-struct. The leaderboard allows to quickly compare new results against compatible prior results, aiming to improve the overall quality of graph learning benchmarking.

---


### 459. [Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434)

**<font color=#1a73e8>作者：</font>** Shai Nahum Gefen, Vered Chassida, Dmitry Basin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a method for fitting a minimal agent harness to a fixed, self-hostable LLM. Given an expert-validated dataset, CLEO admits only the tools, guardrails, memory policies, and loop components that improve accuracy while remaining general and auditable. On our held-out dataset, the CLEO harness reaches an 83.8% pass rate, within 1.2 points of the strongest out-of-the-box Claude Code SDK baseline, while being two orders of magnitude smaller.

---


### 460. [Online Class Posteriors for Interpretable and Controllable Discrete Diffusion](https://arxiv.org/abs/2611.03454)

**<font color=#1a73e8>作者：</font>** Felix Koulischer, Gianni Van De Velde, François Remy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models remain far less understood than their continuous counterparts, despite recent breakthroughs across modalities, most notably in text. Leveraging tools from continuous diffusion, we formulate a theoretical framework to track the class-conditional posterior in an online manner by combining conditional and unconditional model predictions. In masked language modeling, this posterior offers highly interpretable dynamics: tokens aligned with a class boost the posterior, while contradictory ones suppress it. We also show that the posterior can be used for logical guidance operations (AND, OR, NOT) in discrete diffusion. These operations enable precise control over generation, such as avoiding specific classes. In addition, we discuss a mismatch in the formulation of classifier-free guidance between discrete and continuous settings: discrete models mix the data distributions, while continuous models mix the marginals. We validate our methods and discuss their potential applications on synthetic data, with all quantities analytically tractable, as well as on MNIST, text, and antibody sequences.

---


### 461. [Online Label-Free Gradient Matching for Continual Language Model Training](https://arxiv.org/abs/2611.03496)

**<font color=#1a73e8>作者：</font>** Sajjad Pakdamansavoji, Mohammad Reza Rezaei, Ilija Subasic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models in customer-facing products must be continually updated, since the data they serve shifts over time. As retraining on the full accumulated data is impractical, each update should instead run on a small set of examples carrying the training signal of all data seen so far. The strongest current methods build this set by gradient matching, which synthesizes examples whose training gradients match those of the full data. However, they require ground-truth labels, run once on a fixed snapshot rather than on a growing stream, and are slow on large data. We introduce \textbf{OLGA}, which lifts these limitations. It distills unlabeled data by drawing the gradient matching targets from the model's own next-token predictions. Across five text classification benchmarks with phi-1.5, it improves accuracy by 10 percentage points over the strongest selection baseline using as few as five examples. OLGA also distills online data streams by keeping a running rehearsal memory of synthetic examples, which is re-distilled together with each new batch as it arrives. In the online setting, it outperforms the strongest selection-based continual baseline by 6.6 stream-AUC percentage points. Finally, our method scales to large data by pairing distillation with selection in a hybrid pipeline, letting selection handle the mild stage of compression and distillation the extreme one. It cuts runtime by 30\% versus distillation alone at similar accuracy, and beats the best selection-only pipeline by up to 12.6 percentage points.

---


### 462. [Can AI Do Formal Demography? Why Vaccinating the Oldest Saves Both the Most Lives and the Most Years of Life](https://arxiv.org/abs/2611.03500)

**<font color=#1a73e8>作者：</font>** Joshua R. Goldstein, Kenneth W. Wachter  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can AI contribute to formal demography? We report an experiment in which an AI model, Claude, was asked to explain and then simplify the proof of an earlier result: that vaccinating the oldest against COVID-19 saves both the most lives and the most years of life, because the years saved per person treated rise with age. The model proposed a new proof that is shorter, more intuitive, and somewhat more general than the original, built from a known life-table identity and the definition of convexity. It states the condition for the result as the convexity of the reciprocal of the hazard, which can be checked from the hazard alone and holds for most familiar parametric models, and it yields a lower bound on life expectancy whenever that condition is met. Prompted by a further question, the model also gave an exact form of the condition, showing how far convexity can be relaxed. The model traced these identities and related results in earlier literature. An edited record of the sessions is provided, and complete transcripts are available on request. The exercise suggests that AI can revisit established results, make them easier to understand, and prove valuable generalizations.

---


### 463. [Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization](https://arxiv.org/abs/2611.03517)

**<font color=#1a73e8>作者：</font>** Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not. Open-ended agents let a self-directed model mutate a population of kernels and pay for the freedom in trials: thousands of evaluations, repeated edits, and wrong candidates. Both respond to hard targets by equipping the agent with more: parsed profiler output, disassembly analysis, retrieval over documentation and libraries, and stores of lessons. We argue that both lack direction, a hypothesis about where the remaining gap is, and that a short question asked at the right moment supplies it without narrowing what the agent may do next. We present KernelSeek, a question-driven agent that makes an existing CUDA kernel faster with no operator-specific knowledge and no faster implementation to imitate: a general-purpose coding agent, a minimal harness that enforces a verifiable goal, and questions at decision points, first from a human, then from a bank the agent applies to itself. On the same task, evaluator, hardware, and week, a tool-rich autonomous agent built in the prevailing style plateaued at 0.50x FlashAttention-3 after 133 model-driven steps; KernelSeek reached 1.13x. It then produced dependency-free FlashAttention forward kernels for Hopper and Blackwell, single CUDA files with no CUTLASS, CuTe, cuBLAS, or cuDNN, correct on all 182 scenarios per architecture and 1.16x FlashAttention-3 and 1.46x FlashAttention-4 (geometric mean). Across 162 human messages and 11.5K agent tool calls, every large gain followed a question that moved the agent to a different layer of the system or rejected a claimed limit, never one that supplied information. We release the kernels, harness, question bank, and all traces.

---


### 464. [VIAS: Value-Isolating Activation Steering for Multi-Value Alignment and Compliance for Organisations](https://arxiv.org/abs/2611.03518)

**<font color=#1a73e8>作者：</font>** Avni Mittal, Avinash Anand, Dikshant Kukreja 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organisations increasingly deploy large language model agents that must follow organisational values. We check whether activation steering, which adds vectors to a model's internal activations during generation without changing its weights, can improve compliance beyond prompting alone. Since most scenarios involve several values at once, we focus on multi-value steering. A simple way to build these vectors is to contrast responses that follow all values relevant to a scenario with responses that violate them. However, this gives nearly identical vectors for different values: they capture a general compliance signal rather than individual values, which limits their use when combining several values. We propose Value-Isolating Activation Steering (VIAS), which contrasts responses to the same scenario under two prompts, one listing all relevant values and one omitting a single target value. We keep a pair only if the target value changes from compliant to non-compliant and both responses still meet a minimum compliance level on the other values. We evaluate VIAS on PROTECT, a workplace compliance dataset where each scenario is tagged with relevant values from a 21-value taxonomy. VIAS reduces overlap between value vectors, making them better suited for multi-value steering, although this alone does not lead to independent control over each value. Combined with prompting, VIAS complies with every tagged value on 69.6% of scenarios for Qwen2.5-7B, 75.2% for Mistral-7B, and 72.6% for Phi-3.5-mini, outperforming prompting alone for all three models.

---


### 465. [Grading the Unannotated: Insights from the WorkRB Skill Extraction Challenge at RecSys-HR 2026](https://arxiv.org/abs/2611.03525)

**<font color=#1a73e8>作者：</font>** Warre Veys, Luis Gasco, Jens-Joris Decorte  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill extraction benchmarks score models against a few human-annotated positives and treat every other skill in the vocabulary as equally wrong. At the scale of ESCO (13,939 skills) this binary view can reward models that rank the annotated positive high for the wrong reason, and hides semantically nonsensical predictions. The WorkRB Challenge at RecSys-HR 2026 replaces it with graded relevance: every candidate skill in a model's ranking window carries a 0 to 4 grade, and the leaderboard scores nDCG@100 against these grades. Since ternary judgements proved too coarse for objective annotation, relevance is decomposed into a cascade of four binary questions (same domain, activity mentioned, right granularity, replacement of a gold positive) that a smaller LLM judge can answer reliably; the labels are validated with blind human and frontier-model re-annotation. This paper documents the annotation methodology, the construction of five benchmark datasets (four with vacancy sentences as queries, one with lexically distant skill surface forms), the validation of the LLM cascade, and insights from the submissions. The field converged on multi-stage retrieve-and-rerank pipelines, whose gains come from clearing nonsense out of the ranking window rather than finding more positives: at the top of the leaderboard, the graded ordering is uncorrelated with what binary evaluation would have said. Graded labels expose much bigger gaps between top submissions and baselines than binary evaluation does, and show that semantic-understanding skill recommendation is still wide open. The clear next direction is bringing efficiency back: every submitted system we could size uses at least 42x, typically several hundred times, more parameters than the baselines it beats.

---


### 466. [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526)

**<font color=#1a73e8>作者：</font>** Abdellah Rahmani, Sean McLeish, Ang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer programmers chain together the same reusable computational primitives, for example, conditional statements or loops, but in different orders to implement different algorithms. In contrast, existing language model architectures always execute their layers in the same order. We introduce Library of Layers (LoL), an architecture that dynamically orders its layers during inference to solve the problem at hand. LoL has a single hyperparameter, the size of its global library of transformer blocks, that allows it to transition seamlessly between parameter reuse and sparsity, generalizing the parameter-efficiency and FLOPs-efficiency tradeoffs of dense, depth-recurrent, and mixture of experts architectures in one unified family. We show that LoL achieves competitive performance with all three above baselines when pretrained on text data. On synthetic sudoku and maze data, we observe that the model employs distinct layer orderings to implement different solution strategies, and we can intervene on routing to force a model to apply a specific solution strategy to a problem instance. In a multilingual natural language setting, we find that LoL chooses different layer order patterns based on language and script. Similarly, we train LoL on safety data and fit probes to its router outputs, finding that these probes distinguish safe from unsafe text with high AUROC. LoL provides a path toward a future in which models dynamically compose their own computational graph, enabling more efficient and controllable reasoning.

---


### 467. [An Agentic Framework for Automated Power System Studies and Grid Connection Assessment](https://arxiv.org/abs/2611.03534)

**<font color=#1a73e8>作者：</font>** MaoXun Huang, Kshitij Kapoor, Eli Louise  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Connecting new generation and demand to the grid depends on two scarce skills: checking applications against a large, changing body of regulation, and running the network studies that decide where and how a project connects. We present Grid Agents, an AI system that brings both together, and the methodology we use to evaluate it. The Grid Ontology is its knowledge system. It represents the regulation, standards and engineering knowledge that grid work depends on, makes it searchable, and evolves as the agents learn from use. Every answer drawn from it rests on evidence the agents cite. Grid Studio is an agent system specialised for power-system engineering. It works in its own engineering environment with domain tools and a study framework, draws on the Grid Ontology, and relies on established solvers for every number it reports. In both, engineers make the decisions. We bring eight published power-system benchmark families, previously scattered across separate papers, into one suite of 519 tasks, and we verify not only each answer but the work behind it, by replaying the agent's tool calls. The Grid Ontology cites the right regulatory evidence more often than a general coding agent or retrieval pipelines, leads on LegalBench-RAG and ranks first on the public leaderboards of the Enterprise RAG Challenge and ViDoRe V3. Grid Studio scores highest on the 519 power-system tasks and is the fastest of all the systems we compare, both by a statistically significant margin. With an optimiser in the loop, its reinforcement packages cost 33-67% less on average than those the agent designs alone.

---


### 468. [Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL](https://arxiv.org/abs/2611.03551)

**<font color=#1a73e8>作者：</font>** Marianne Menglin Liu, Rongguang Wang, Zheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM coding agents can increasingly automate model post-training, but whether they can act as forward-deployed engineer (FDE) agents, discovering customer requirements and turning them into deployment decisions, remains unclear. We study this on a real enterprise text-to-SQL engagement: a simulated customer, grounded in the real use case's requirements, starts with an ambiguous request. An agent must discover acceptance criteria, data permissions, and hardware constraints in the discovery phase, then plan and execute a post-training recipe in the delivery phase. Across 15 models, the strongest discover over 80% of withheld requirements and open-weight models discover 40-50%; in the delivery phase, only 25% of runs across eight coding-agent configurations pass all acceptance criteria. We identify four bottlenecks in this engagement: (1) incomplete discovery, with 40% of withheld requirements missing or misrepresented; (2) unreliable execution; (3) underused compute budgets and a lack of systematic comparisons across base models and post-training methods; and (4) benchmark accuracy does not guarantee production readiness. We suggest human review of discovered requirements, monitoring of the agent's plan during execution, and an explicit experiment-environment specification covering hardware, budget scope, and production checks.

---


### 469. [PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis](https://arxiv.org/abs/2611.03557)

**<font color=#1a73e8>作者：</font>** Gaurab Wagle, Bishal Adhikari, Jiajia Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely and accurate crop health diagnosis is essential for sustainable agricultural production, yet accurate diagnosis often requires expert knowledge that is not readily available. Recent vision-language models (VLMs) have demonstrated remarkable capabilities in visual understanding, reasoning, and natural-language interaction, creating new opportunities for intelligent crop health assessment. However, deploying VLMs on resource-constrained devices remains challenging due to their substantial computational and memory requirements. This paper presents PlantVLM-Edge, a quantized vision-language framework for conversational crop health diagnosis that can run entirely on resource-constrained edge devices. PlantVLM-Edge combines agricultural domain adaptation, post-training quantization, and on-device serving with an offline chat interface, allowing growers to ask open-ended questions and receive diagnoses, symptom explanations, and management guidance without cloud connectivity. The framework is backbone-agnostic: we validate it with two different VLM types with varying scale and architecture (Qwen3-VL-2B and LLaVA-1.5-7B), four quantization schemes, and two diagnostic domains (plant diseases and insect pests), and we deploy all variants on an NVIDIA Jetson AGX Orin. Eight-bit quantization affects answer quality minimally relative to the full-precision model, and 4-bit activation-aware weight quantization (AWQ) retains 98.6% of full-precision answer quality on both domains while reducing the weight memory of the 2B backbone by 49%. In its most compact form, PlantVLM-Edge requires 2.01 GiB of weight memory, returns its first token in about 0.12 s, and completes a 64-token diagnostic response in 0.78 s. These results demonstrate that timely and accurate crop health diagnosis is practical on edge devices, providing a foundation for next-generation crop monitoring and decision support systems.

---


### 470. [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575)

**<font color=#1a73e8>作者：</font>** Wei-Lin Chen, Zhepei Wei, Xinyu Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated files, weakening access controls, or corrupting data, in response to benign inputs without explicit jailbreaking. This failure mode is particularly important because apparent task success may reassure users that an agent behaved correctly, causing harmful side effects to go unnoticed. We call this harmful success: the agent successfully completes the intended benign task while simultaneously causing unintended harm. Despite its importance, harmful success is difficult to measure because conventional task-success metrics overlook harmful behaviors, while existing safety evaluations are often designed solely to assess harmful outcomes. We introduce VeriHarm, an automatic framework for constructing programmatically verifiable benchmarks that directly measure harmful success. VeriHarm minimally perturbs coding tasks to elicit unintended harmful behavior while maintaining the benignity of the task and preserving the original task objective. It then synthesizes executable harm tests that, together with the original task-correctness tests, evaluate both task accuracy and harmful outcomes. Frontier agents, including GPT-5.6-Sol and Claude-Opus-5, achieve an average task accuracy of 95% on our curated VeriHarm-Bench, yet still struggle to complete tasks safely: their safe success rate, the fraction of tasks completed successfully without triggering the designated harm, averages only 37%. These results suggest that successful task completion can frequently coexist with unintended harm, and that task-success metrics alone may substantially understate the potential safety risks of coding agents.

---


### 471. [Sonar-MoE: In-Backward Expert Updates for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2611.03577)

**<font color=#1a73e8>作者：</font>** Avni Mittal, Avinash Anand, Ashutosh Kumar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most parameters of a Mixture-of-Experts (MoE) model belong to its experts, and standard training keeps every expert gradient in GPU memory until the optimizer step. This memory grows with the number and size of the experts, so it rises as MoE models scale. We introduce Sonar-MoE, which updates each expert tensor during the backward pass and frees its gradient right away. It brings optimizer-in-backward from dense models to batched MoE expert tensors, so the GPU never holds more than one layer of expert gradients. When we fine-tune OLMoE-1B-7B and Granite-3.1-3B-A800M in bf16 with two expert-kernel backends, Sonar-MoE lowers peak memory by 19% to 22%. Its updates are bitwise identical to standard training without expert gradient clipping, and held-out loss stays within 0.003 of all baselines. Each step also takes 17% to 23% less time than standard training with global-norm clipping. Updating whole batched tensors rather than individual experts is what keeps Sonar-MoE fast, as it avoids a 20% to 72% slowdown while using the same memory. Sonar-MoE matches optimizer-in-backward over all parameters in memory and speed while still clipping the dense parameters.

---


### 472. [FedReady: Bounded Agents for Federation Formation](https://arxiv.org/abs/2611.03586)

**<font color=#1a73e8>作者：</font>** Ziyue Xu, Holger R. Roth, Chester Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) runtimes standardize aggregation and deployment, but each new study still requires federation formation: selecting task-eligible sites and preparing their local data and task code for federated training or analysis. This preparation recurs when the target changes, while raw records and site-private mappings are excluded from cross-site FL messages. We present FedReady, a system that performs federation formation with bounded LLM agents. Agents propose shared contracts, local adapters, and task code; the runtime owns workflow state and accepts artifacts only after checks tied to their digests. Candidate site discovery prioritizes recall; local eligibility verification checks task support before site admission. Once participating sites and artifacts are fixed, conventional federated training or analysis proceeds without readiness agents. Across 39 simulated retinal sites and four tasks, discovery reaches recall 1.00 at precision 0.65; local eligibility verification removes all 17 false positives without losing an eligible site-task pair. The participating sites supply 45,575 task-record instances and complete four 100-round jobs, including one with a runtime-generated contract. Across ten patient cohorts, preparation supports seven patient populations and holds endpoints at three sources as unsupported. Comparison with manually prepared reference populations and analysis (the manual reference) gives a maximum survival-curve difference of 0.001133. We also analyze 19 development failures, targeted classification ablations, and standalone and heterogeneous agent configurations. These results establish the feasibility of task-specific data preparation before ordinary FL training or analysis.

---


### 473. [A Scaling Theory of Multi-Epoch Pretraining: Late-Time Overfitting and Ensembling](https://arxiv.org/abs/2611.03590)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Yidi Miao, Blake Bordelon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the near future language model pretraining will become bound by total data rather than total compute. Such a regime requires revisiting scaling laws and scaling law theory. Motivated by prior works that have found utility in ensembling, we study how the number of training epochs and ensemble size jointly shape generalization when training data are fixed. In language-model experiments on FineWeb, logit averaging reduces late-training deterioration, delays optimal stopping, and can outperform wider or deeper single models at matched parameter-token budgets over a common training horizon. To analyze this interaction between data reuse and ensembling, we derive a dynamical mean-field theory (DMFT) for multi-epoch stochastic gradient descent in power-law random-feature ensembles, tracking error correlations across epochs and models. Ensembling reduces the prediction variance responsible for late-time growth in expected test error, changing the optimal stopping time. We use these stopping times to derive compute-allocation laws at fixed data and individual model sizes. Under this allocation, ensemble size grows with compute at least as fast as training time per member, while excess test loss above the limiting loss decreases as a power of compute.

---


### 474. [DiabAgent: Toward Agentic Physiological Control](https://arxiv.org/abs/2611.03601)

**<font color=#1a73e8>作者：</font>** Chengxi Li, Shaoxuan Li, Deyao Hong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As pretraining scales, medical language models have advanced rapidly in clinical question answering. Their ability to achieve effective physiological control through sustained intervention still lacks systematic quantitative evaluation. Type 1 diabetes provides a concrete setting: impaired insulin secretion creates dependence on exogenous insulin, with dosing continually adjusted using information about meals, exercise, illness, and glucose measurements. We introduce DiabAgent, a research suite for agentic physiological control comprising the Agentic Physiological Control (APC) framework, the DiabetSim simulator, and the SweetBench benchmark. APC controls glucose through medical-device tools, using ongoing observations to infer individual states, accumulate personal experience, and choose treatment actions. We build DiabetSim to simulate different patients, events, and device conditions for scalable virtual testing and training. Using DiabetSim, we construct SweetBench by instantiating 32 scenario designs as 212 glucose-control tasks. With Claude Opus 5.5 and a fixed decision interval of one hour, APC achieves a COGI of 73.5, compared with 71.2 for the open-source closed-loop baseline OpenAPS. Ablations further show that individual adaptation and contextual information improve glucose control. Combining high-frequency rule-based control with lower-frequency agent decisions shows potential for balancing control performance and computational cost. Our work provides a framework, simulator, and evaluation foundation for agents to participate in human physiological control.

---


### 475. [Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning](https://arxiv.org/abs/2611.03602)

**<font color=#1a73e8>作者：</font>** Tengfei Liu, Yang Shi, Yuran Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can generate detailed video captions, yet they may overemphasize minor details while overlooking essential context and key events. We argue that not all visual evidence deserves equal attention, as the importance of visual information depends on the content of each video. Motivated by this observation, we propose Reviso, an agentic video captioning framework that learns what to observe and how to gather relevant visual evidence. From a low-frame-rate global preview, Reviso constructs a hierarchical Context--Focus--Points (CFP) observation plan that identifies the video context, prioritizes key aspects, and defines concrete observation targets and corresponding tools. Guided by this plan, Reviso performs goal-directed active perception by selectively revisiting temporal segments and combining tools for fine-grained inspection. It interprets the acquired evidence, updates its plan as needed, and integrates global and local information to generate the final caption. To learn this observation strategy, we develop a verification-guided pipeline that constructs high-quality training trajectories through factual verification and teacher-guided refinement. We further train Reviso using Group Relative Policy Optimization (GRPO), incorporating a key-fact reward for caption quality, a Plan Alignment Reward (PAR) for identifying important observation targets, and an Unproductive Tool-Call Penalty (UTCP) that adjusts observation-cost penalties based on caption quality. Experiments across four video captioning benchmarks show that Reviso outperforms the evaluated open-source baselines, while its generated captions better support downstream video question answering. These findings highlight the effectiveness and potential of priority-guided active observation for video captioning.

---


### 476. [Tracing the Scientific Discovery Capacity of LLMs to Their Training Data](https://arxiv.org/abs/2611.03617)

**<font color=#1a73e8>作者：</font>** Arda Uzunoglu, Mahler Revsine, Michael Schatz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show growing promise for scientific discovery, yet basic questions remain about what enables reliable discovery. How can we trace the scientific discovery capacity of LLMs to their training data? We study this question as one of missing probability mass and develop a theoretical account in which monofacts-the facts observed once during training-set the discovery capacity. In materials science and regulatory genomics, we directly manipulate monofact rates in training sets and find that more monofacts consistently yield more discoveries across two open-weight model families, sampling strategies, and reasoning budgets. Further experiments show the relationship cannot be explained by training-set diversity alone and can transfer across scientific domains when paired with in-domain data. Together, our results identify monofact rate in training data as a key factor governing discoveries in language models.

---


### 477. [Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR](https://arxiv.org/abs/2611.03627)

**<font color=#1a73e8>作者：</font>** Ziqi Pang, Yu-Xiong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) can enable generalizable improvement for large language model (LLM) reasoning. This paper studies how to incentivize such generalization via reasoning strategies. We study this question with a controllable equation-solving framework: finding multiple inputs x for equations f(x)=y, where f is a non-bijective string function. This setting makes reasoning strategies observable while supporting a clear definition of easy-to-hard out-of-distribution (OOD) shifts, e.g., more solutions, longer y, etc. We uncover a subtle RLVR failure: it teaches the model to solve in-distribution tasks with high accuracy and structured step-by-step derivation, yet under OOD shifts, the same model abandons derivation and collapses to ineffective brute-force enumeration, causing sharp accuracy drops. This observation reveals the deeper challenges of RLVR generalization as it is neither incapable base model nor reward hacking, since the model succeeds in-distribution with the correct reasoning strategy. The key to mitigating this failure is an indirect intervention that surprisingly helps: co-training with bijective inversion tasks. Although these bijective tasks are actually not uniformly harder and even further from the non-bijective OOD evaluation, they make derivation more certain and substantially restore the correct strategy and accuracy under OOD shifts. This effect further motivates our theoretical analysis: outcome-only RLVR can shape reasoning processes through implicitly crediting the effective reasoning strategies more, even without process supervision. To conclude, our analysis framework and findings systematically reveal the crucial role and incentivization of reasoning strategies in RLVR generalization under OOD shifts. Code is available at this https URL.

---


### 478. [Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap](https://arxiv.org/abs/2611.03633)

**<font color=#1a73e8>作者：</font>** Catherine Li, Jingchu Gai, Andrej Risteski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a promising optimizer for pretraining large language models, offering a speedup over AdamW in minimizing pretraining loss. However, it remains unclear whether Muon's advantage persists after fine-tuning. In this paper, we study the downstream behavior of Muon and AdamW and uncover a surprising trend: beyond a sufficiently large pretraining data budget, AdamW outperforms Muon after fine-tuning. Moreover, as model size increases, AdamW overtakes Muon at progressively smaller pretraining token-parameter ratios. To explain this reversal, we view fine-tuning as a perturbation of the outputs and introduce the margin-to-spread ratio, which measures how far the correct logit lies above the wrong ones relative to how widely the wrong logits are spread. In language models, Muon has the larger margin-to-spread ratio at small data budgets and AdamW at large ones, mirroring the fine-tuning trend. In a linear associative memory, we prove that after one update the margin-to-spread ratio of gradient descent gains on that of Muon as the data budget grows, and simulations show that this trend persists after extended training.

---


### 479. [WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](https://arxiv.org/abs/2611.03634)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Qianhui Wu, Boyu Gou 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments for training often lack functional depth and visual fidelity. We propose WebHarbor, a suite of 153 executable and dockerized website environments that faithfully reconstruct the visual interfaces, content, and functional workflows of real-world web services under deterministic control. We build WebHarbor through task-driven human-agent collaboration, where environments evolve as new tasks expand their functional scope, coding agents implement the required changes, and human contributors audit visual fidelity, functional correctness, and task validity. The resulting suite comprises 3,518 tasks spanning multi-step and post-authentication workflows, where existing works often fail to cover. Beyond reliable evaluation, WebHarbor provides high-fidelity synthetic web environments for cost-efficient reinforcement learning (RL). We demonstrate that a Qwen 4B-level GUI agent trained with RL in WebHarbor generalizes to unseen tasks and performs competitively with leading open-source GUI web agents across four benchmarks. The code and data are publicly available at this https URL.

---


### 480. [From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles](https://arxiv.org/abs/2611.03641)

**<font color=#1a73e8>作者：</font>** Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) generation has substantially improved the performance of Large Language Models (LLMs) on complex reasoning tasks, including code generation, data analysis, and exam-style question answering. Despite these advances, purely neural LLMs continue to struggle with elementary logical reasoning problems and lack the determinism, soundness, and reliability characteristic of symbolic reasoning systems. Conversely, classical symbolic methods such as SAT solving and exact cover guarantee correctness and completeness, but require problems to be expressed in highly specialized formal encodings, limiting their applicability to natural language inputs. In this work, we present a synergistic neuro-symbolic framework that bridges this gap by combining neural semantic parsing with deterministic exact cover reasoning. Given a Zebra-style logic puzzle in natural language, an LLM translates entities and constraints into structured tool calls that construct an exact cover instance. A symbolic solver then computes the solution and provides feedback to iteratively refine invalid, under- or overconstrained encodings, exploiting the uniqueness property of Zebra puzzles. We conduct a comprehensive empirical evaluation across multiple parameter scales, post-training paradigms, and LLM families. The results demonstrate that our hybrid approach consistently outperforms strong plain neural baselines, including CoT prompting, as well as recent neuro-symbolic methods.

---


### 481. [EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos](https://arxiv.org/abs/2611.03646)

**<font color=#1a73e8>作者：</font>** Yujiao Shen, Jiahe Song, Haitian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning from human data offers a scalable path toward embodied intelligence, yet it requires models to accurately understand fine-grained human actions from egocentric observations. However, existing benchmarks remain limited in action atomicity, temporal precision, and hand-action association. We introduce EgoActionBench, a benchmark that represents continuous human manipulation as temporally localized atomic actions associated with the left hand, right hand, or both hands. EgoActionBench contains 1,407 episodes with 41,132 human-refined action annotations. To evaluate such dense predictions, we propose an evaluation protocol that retrieves temporally eligible candidates, selects a prediction by content agreement, and scores semantic fidelity and temporal overlap alongside action precision and recall, jointly capturing what happens, when it happens, and which hand performs it. We benchmark 20 baseline models and systems on EgoActionBench and further adapt two backbones, Qwen3-VL-4B and LLaVA-OneVision-2-8B, through supervised fine-tuning followed by reinforcement learning on automatically annotated training episodes. EgoAction improves EgoActionScore by 15.9 and 23.2 points on the two backbones, and both adapted models outperform all open-source baselines. Our experiments reveal substantial limitations of current models in action atomicity, temporal precision, and hand-action association, highlighting the gap between general video understanding and the action understanding required for embodied intelligence.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 482. [OpenMidnight: Closing the Performance Gap Between Open and Proprietary Pathology Foundation Models](https://arxiv.org/abs/2611.00064)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ratna Sagari Grandhi, Anis Chihoub, Ryan Kim 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models offer transferable representations for a range of downstream tasks in computational pathology, but reliance on proprietary data, substantial compute requirements, and limited availability of training code and preprocessing pipelines hinder independent validation and further methodological development. We present OpenMidnight 1.1, an open-source replication and refinement of Midnight trained on approximately 12,000 publicly available whole-slide images from The Cancer Genome Atlas. Using an encoder initialized with pretrained DINOv2 weights, OpenMidnight 1.1 uses approximately 320 H100 GPU-hours for pathology pretraining, a 34-fold reduction relative to the compute reported for Midnight. Across 16 classification and four segmentation datasets in THUNDER, OpenMidnight 1.1 achieves the highest mean segmentation Dice (69.7) and ranks fourth among 14 models, ahead of Midnight, with performance that matches or exceeds models trained on substantially larger datasets in several tasks. Our ablation studies additionally examine how initialization, data volume, model size, and tissue composition affect downstream performance, providing empirical evidence to inform the development of future training recipes. Our release of the training code, preprocessing pipeline, and model weights lowers barriers to reproducible research and further development of competitive pathology foundation models.

---


### 483. [AdaptAD: Foundation Model Adaptation with Missing Modality Robustness for Alzheimer's Disease Staging Across the Disease Continuum](https://arxiv.org/abs/2611.00084)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dawa Chyophel Lepcha, Sophie A. Martin, Pierrick Coupé 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Staging Alzheimer's disease (AD) across its continuum, from cognitively normal (CN) through mild cognitive impairment (MCI) to dementia from a single structural MRI remains difficult because 3-D networks overfit small cohorts, and FreeSurfer morphometry is often unavailable. We present AdaptAD, which reads a registered T1-weighted scan as 16 anatomically placed 2.5-D slices through the medial temporal lobe and adapts a frozen ImageNet-pretrained ViT-B/16 with low-rank adaptation (LoRA), training 3.5 M of 89 M parameters. Morphometry enters as tokens when present, or as a learned [MISSING] token, and a missing-aware stacker fuses both experts. Under a pre-registered protocol, ten methods were compared for three-class CN/MCI/AD staging on identical 5-fold splits of 597 ADNI participants, 29% without FreeSurfer, with Holm-corrected paired bootstrap tests. The locked model was tested once on 993 OASIS-3 participants (988 scored by every method). On ADNI, AdaptAD achieved a three-class macro-AUC of 0.745 (95% CI 0.709 to 0.781), ranking first and significantly exceeding full fine-tuning, ShaSpec and a 3-D CNN. On OASIS-3 it reached 0.780 (0.748 to 0.814), and on the CDR-based label (0.804) it significantly outperformed every 3-D and image-tabular method. LoRA matched full fine-tuning with 25 times fewer trainable parameters, and removing morphometry changed external macro-AUC by less than 0.003. The disease score tracked MMSE and CDR-SB within diagnostic groups and stratified MCI-to-dementia progression (log-rank p < 0.001), while saliency concentrated in medial temporal and periventricular regions. A parameter-efficient 2-D foundation model can therefore stage the full AD continuum from a routine T1 scan without morphometry, offering a scalable route to memory-clinic deployment.

---


### 484. [A generative foundation model for computational brain imaging](https://arxiv.org/abs/2611.00265)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuting He, Xu Wen, Hongxing Lan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational brain imaging is constrained by a mismatch between increasingly diverse tasks and scarce, heterogeneous clinical data. Although existing brain foundation models transfer pretrained representations, their knowledge remains entangled within model-specific features and fixed architectures. This paper proposes BrainGFM, a generative foundation model that extends knowledge transfer beyond representation reuse through a reusable and reconfigurable brain-imaging prior. By pretraining on a corpus of about 1.3 million MRI and CT slices, BrainGFM supported task-aligned data synthesis for low-data predictive learning and task-adapted post-training for image reconstruction. Across 48 downstream tasks, BrainGFM improved segmentation and classification under limited supervision and achieved high-fidelity image enhancement across heterogeneous imaging conditions. Multicenter clinical validation involving 4,796 stroke patients across two internal and four external centers demonstrated its applicability to three clinically relevant tasks around stroke cohorts. Blinded reader assessments showed that BrainGFM-generated FLAIR images approached acquired FLAIR in overall diagnostic quality. In a human-AI collaboration study, BrainGFM assistance yielded a 14% relative improvement in mean radiologist stroke-subtyping accuracy. These findings support generative priors as a reusable foundation for heterogeneous computational brain-imaging applications.

---


### 485. [Quantifying Local and Global Fidelity of Nonlinear Embeddings](https://arxiv.org/abs/2611.00290)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Henry Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dimension reduction methods are chosen by a common claim: t-SNE and UMAP preserve local structure, and PCA preserves global structure. Checking it on given data takes local and global scores on one scale and a test that compares two maps. Both scores come from one curve. The locality profile is the chance-corrected share of each point's k nearest neighbors that a map keeps, over all neighborhood sizes. Its value at k = 10 is the local fidelity L, and its mean over 30 to 50 percent of the data is the global fidelity G. We prove that at the midpoint the profile is the agreement on which half of the data is near each point, a rank correlation of the distances. Because L and G are one statistic, two maps can be tested against each other. The LG reversal test applies to any two dimension reduction methods. It decides, with a block-jackknife p-value, whether one map is more local and the other more global, and returns the scale at which to change maps. On 156 maps of twelve datasets with up to 1.38 million points, G agrees with established global scores at 0.89 and 0.96, and 2,000 points estimate it. The test confirms the usual claim on seven datasets. On both retail datasets and both rolled-up manifolds, it finds the neighbor embeddings more global. In an agent memory of one million passages, the two maps cross at 150,000 passages (p = 2.6e-5). Applications span pathology, single cells, supply chains and AI agent memory.

---


### 486. [TabAbax: A Tabular Foundation Model Technical Report](https://arxiv.org/abs/2611.00562)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhixiong Cheng, Xiaoyun Gao, Shiyuan Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) enable in-context prediction on unseen tabular datasets without task-specific training. Mechanistic work has shown that increasing the depth of the ICL Transformer yields weak gains, leaving the main headroom for gains in the synthetic pretraining prior and column-row encoder upstream of the ICL backbone. We introduce TabAbax, a TFM built on TabICLv2 that focuses all modifications on these two upstream components. On the prior side, we further improve the quality and complexity of the synthetic pretraining prior. On the encoder side, a two-pass column-row stack strengthens cross-feature interactions before row compression, using learned Fourier scalar encoding from TabFM and Causilo. Evaluations on BeyondArena and TabArena show strong regression-centric gains: TabAbax reaches 1,238 Elo on the 142-dataset BeyondArena suite (10th of 41 evaluated methods), 1,676 Elo on TabArena's overall 51-dataset suite (11th of 99 methods, +115 over TabICLv2), and 2,024 Elo on TabArena's regression benchmark (7th of 99 methods, +336 over TabICLv2, +21 over TabFM). A prior-only ablation confirms the attribution: the improved prior alone yields +228 Elo for regression, demonstrating that prior quality is the dominant knob for improving regression performance.

---


### 487. [Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards](https://arxiv.org/abs/2611.00586)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen-Yu Zhang, Jiandong Zhang, Huaxiu Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, reinforcement learning from verifiable rewards (RLVR) is practically very important, where the leading approach is group relative policy optimization (GRPO) that typically faces a trade-off between rollout efficiency and downstream performance. To improve efficiency while preserving performance, existing selective rollout methods mainly exploit only source-side training dynamics to optimize the discrete distribution over source prompts. However, in practice, the source training dataset is rarely identically distributed to the target test dataset. When such a mismatch exists, due to legal or privacy constraints, it is usually not acceptable to share target prompts themselves with the RLVR trainer. Nevertheless, it is still possible for the target data owner to provide limited aggregated feedback from a small held-out target set without revealing target prompts or rollout traces. In this paper, we propose learning-to-reweight rollout (L2RR) that explicitly incorporates target-side performance feedback into GRPO. Specifically, L2RR learns a discrete sampling distribution over source prompts by optimizing a bi-level objective that maximizes accuracy on a held-out target dataset, while simultaneously penalizing rollouts that provide little incremental learning information. Empirical studies on six math reasoning benchmarks and three model scales show that L2RR improves target-domain performance and increases rollout efficiency.

---


### 488. [Versatile Graph Foundation Models from Frozen Time-Series Foundation Models via Parallel Flows](https://arxiv.org/abs/2611.00670)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jielong Yang, Feng Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models aim to serve unseen graphs across tasks, feature spaces, and label sets. Most current models learn how to represent a new graph by pre-training on other graphs. Because graph data are scarce and differ across domains in features and structures, what they learn may not transfer to a graph from an unseen domain. We show that a frozen time-series foundation model, pre-trained on abundant time series, can instead serve as a graph foundation model without graph pre-training and without any gradient update on the target graph. Such a model reads ordered multivariate sequences, but a graph has no time axis, and covering all its edges with sequences is nontrivial because a node can have many neighbors. We therefore propose GraphFlowFM, which decomposes a graph into parallel flows, sets of vertex-disjoint paths that jointly cover every edge, and reads each path as a multivariate time series with the nodes as time steps. A frozen TimesFM encodes the paths with causal attention, which gives each node a self token and a context token, and a closed-form ridge readout weighs these tokens by their alignment with the labels. In node classification, GraphFlowFM attains the best average rank on 21 datasets among graph foundation models published in 2025 and 2026, ranks first on 17 datasets, and leads on six of the seven heterophilous datasets. It also exceeds pre-trained graph foundation models in link prediction on all six datasets and ranks second in molecule classification, behind only a model fine-tuned after pre-training on molecules.

---


### 489. [SceneBound: How Much Should a Streaming 3D Reconstruction Model Remember?](https://arxiv.org/abs/2611.00756)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziming Wang, Chuyue Gong, Chutian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction models keep past video frames in a recurrent state, fast weights from test-time training, or a key-value (KV) cache. Each written frame shifts the coordinate frame of later cameras or occupies GPU memory. Training-free rules decide what to write from a signal of the current frame. How much they write accounts for their mean accuracy: spending the update budget of a gate at uniformly spaced frames, with no signal, matches nine published gates, and the budget bounds the drift of the state wherever the writes fall. We propose SceneBound, a training-free rule that writes a frame only when its predicted camera pose lies at least a fixed radius from every stored keyframe. Its keyframe count stays within a constant factor of the covering number of the visited poses, the fewest views that keep a keyframe near every camera, so the count grows with the places visited and stays flat when the camera returns. In large scenes, SceneBound closes a submap once decoding its first frame again reveals drift. SceneBound uses one radius across four released models and three memory types. In the recurrent state of CUT3R and the KV cache of StreamVGGT, it achieves the lowest mean trajectory error among the published training-free rules we evaluate, in one pass and over nine passes of a scene, where its keyframes grow by 3% to 6%.

---


### 490. [Steer, Don't Tell: Breaking Reasoning Plateaus with Reachability-Aligned Self-Distillation](https://arxiv.org/abs/2611.00796)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zijian Wu, Lingkai Kong, Lin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post training for large reasoning models remains insufficient on challenging problems, whose correct trajectories are hard to sample. Though prior works address this difficulty by integrating supervised fine tuning on expert trajectories with reinforcement learning, such external experts are not always available. Existing self improvement methods instead use reference solutions to create a privileged self-teacher. Yet privileged teacher correctness does not imply student reachability. Solution conditioning shifts the teacher distribution toward actions unlikely under the unprivileged student, producing seemingly "correct" trajectories that are unreachable or even mal-formed learning targets. Accordingly, we identify reachability alignment as the key to self constructed supervision and propose Self-Steered Reasoner (SSR). SSR realizes this principle through student support projection, which transforms the privileged teacher distribution into a directional signal only over reasoning actions locally reachable under the unguided student. Verification then retains correct trajectories sampled from this reachable space. To further boost the sampling efficiency, an iterative refinement framework is adopted, using diagnostic guidance based on current trajectories. On problems with pass@64 = 0 even after extensive RL, SSR recovers correct and learnable trajectories for 74.6% without parameter updates. Fine tuning on these trajectories followed by resumed reinforcement learning improves aggregate accuracy by 4.9 percentage points on AIME25/26 and HMMT26. These results show that privileged guidance becomes effective self-improvement data when aligned with the reasoning actions the student can reach.

---


### 491. [Adaptive-Policy Distillation: Knowledge Injection under Information Asymmetry](https://arxiv.org/abs/2611.00852)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hojun Cho, Kang Eun Jeon, Jaegul Choo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD), which uses reverse-KL supervision on student rollouts to transfer a context-conditioned model's behavior into student model parameters for closed-book inference, has shown strong results. However, we find that this success does not translate to knowledge injection: across two document-QA benchmarks, OPD injects document knowledge far less efficiently than simple off-policy distillation. We trace this reversal to two failures that are structural, yet sparse across token positions. Reverse KL weights its gradient by the student distribution and therefore barely lifts document-specific tokens the student considers unlikely; after forward KL restores this signal, student rollouts expose later positions on the target trajectory only after generating the preceding tokens correctly, so coverage deteriorates with target length. Motivated by the concentration of teacher-student divergence at these hard positions, we propose Adaptive-Policy Distillation (APD), whose per-token gate jointly shifts the rollout toward the teacher and the objective toward forward KL where needed, withdrawing both interventions as the student learns. Without labels or a verifier, APD improves over OPD by up to 54.6%, achieving the best scores of 0.558 F1 on QASPER and 0.486 MRR on BioASQ.

---


### 492. [GESTALT: Fast, Generalizable Histopathology Image Synthesis from Gene Expression with Pretrained Pathology Foundation Models](https://arxiv.org/abs/2611.01141)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Felix Ho, Alexandros Graikos, Dimitris Samaras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics measures gene expression while preserving where each cell sits in the tissue. The inverse, what a given transcriptomic state looks like, is less explored but equally useful: it lets researchers visualize the morphological consequence of a molecular state and interpret a spatial assay's molecular calls against real tissue structure. GeneFlow, the current state of the art on the Xenium gene expression-to-image benchmark, trains a model from scratch, incurring a high cost on every new target dataset it is applied to. We instead propose GESTALT, which reformulates gene expression-to-image synthesis as predicting a pathology foundation model's image embedding. A lightweight gene-token transformer predicts this embedding from multi-cell gene expression, and a frozen or LoRA-adapted diffusion decoder (PixCell) renders it as an image. Because this visual knowledge is reused rather than relearned, GESTALT trains in a fraction of the time. In both multi-cell and single-cell settings, our method outperforms the SoTA on perceptual metrics across all three Xenium datasets. Beyond improved image quality, GESTALT natively synthesizes at 1024 x 1024, and is evaluated in three generalization settings: zero-shot transfer across gene panels and datasets, held-out patients and disease states, and transfer across studies and tissue sources. Coupled with a statistical model of spatial expression, GESTALT also provides, to our knowledge, the first paired synthesis of cell-resolved transcriptomic fields and tissue images with explicit control over cell type, density, and composition. Code is available at this https URL.

---


### 493. [When Does Exploration Prevent Collapse? Three Regimes and the Path of the Reward in Self-Consistency Training](https://arxiv.org/abs/2611.01307)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jaeho Hwang, Uiwon Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning (TTRL) adapts a model without labels by rewarding answers that agree with the majority, but it collapses the policy onto its majority answer and can remove the correct answer from the samples. Exploration can prevent this collapse, yet its strength is chosen by trial and error, and how the training algorithm changes the required strength is unclear. We model training on a single problem as a continuous flow of the logits of a softmax policy and analyze which policies are stable as the exploration coefficient varies. Only collapsed policies are stable below a lower boundary and only policies spread over many answers above an upper boundary, and we derive these boundaries in closed form for an agreement reward with smoothing toward the uniform policy, compute them for the majority reward of TTRL on policies with one leading answer and bound them with interval arithmetic for actions on ordered bins. We prove that under exact gradients, the learning rate and, in a mean-field model, the normalization of GRPO leave these boundaries unchanged when exploration passes through them together with the reward but shift them when exploration bypasses them. Exact sums on these policies then show that a bonus for rare answers needs a coefficient above $1/\log(G-1)$ for groups of $G$ samples before the normalization and about two to three times that after it. In free-form TTRL on MATH-500, a bonus placed before the normalization prevented collapse and kept more correct answers among the samples, although it lowered pass@1.

---


### 494. [Alignment Flywheel-Guided Suppression Patching for Interactionless Inverse Reinforcement Learning](https://arxiv.org/abs/2611.01322)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Elias Malomgré, Pieter Simoens  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned reward models allow reinforcement-learning agents to use demonstrations, implicit feedback, safety constraints, social norms, or other sources that do not provide a complete hand-designed scalar reward. However, a learned reward model can assign high reward to unwanted behavior. A policy can exploit these errors during training. Later requirements can also identify additional regions where the deployed reward should change. We introduce \emph{flywheel-guided patching}, a mechanism for making such localized corrections without retraining the learned evaluator. An Alignment Flywheel identifies overgeneralized or constraint-violating regions and compiles verified findings into suppression patches. We instantiate the mechanism for Interactionless Inverse Reinforcement Learning using MoE-GUIDE, placing patches in the model's latent space and retrieving only a small local subset during online reward evaluation. In the main MuJoCo benchmark, we evaluate patching without expert-state reset warm starts. We also test whether operator-specified norms absent from the demonstrations can be compiled into the same reward interface and compare this with enforcing the corresponding rules online. The results show that localized corrective information can modify an existing learned reward without providing a complete replacement reward. Compilation can reuse judgments that are expensive or unavailable during control. Cheap deterministic rules may be simpler to check directly at each step. Code for MoE-GUIDE, Alignment Flywheel, and flywheel patching is at this https URL.

---


### 495. [MoEDDI: Semantic Mixtures of Experts for Long Tailed Drug Drug Interaction Prediction](https://arxiv.org/abs/2611.01343)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dinh Tan Nguyen, Hien Quang Kha, Minh-Toan Dinh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Descriptor-based drug--drug interaction (DDI) models typically apply a single global predictor despite heterogeneous physicochemical evidence and severely long-tailed labels. We introduce \textbf{MoEDDI (Mixture-of-Experts for Drug--Drug Interaction prediction)}, a chemically organized mixture-of-experts that routes overlapping descriptor families using low-dimensional statistics and combines their sparse top-$2$ mixture with a global T-DDI pathway through a residual logit correction. The residual parameterization can exactly preserve a supplied T-DDI checkpoint at initialization, although the evaluated models are trained from scratch. Across complete test partitions with 178, 86, and 92 classes, MoEDDI improves macro-F1 over reproduced seed-2026 T-DDI baselines from 0.8284 to 0.8485, 0.4729 to 0.6536, and 0.1807 to 0.4671. On the 3,780-feature corpus, the lowest-support group (89 classes with fewer than 50 test examples) shows the largest mean classwise gain (+3.30 F1 points). Calibration improves on one corpus but worsens on two. These single-seed results support semantic conditional specialization while motivating matched ablations and distribution-shift evaluation.

---


### 496. [SpecUltra: A Unified Foundation Model for Heterogeneous Spectral Images](https://arxiv.org/abs/2611.01396)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Weili Kong, Baisen Liu, Xiaojun Bi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectral imagery, including hyperspectral image (HSI) and multispectral image (MSI), exhibits substantial heterogeneity in band numbers, wavelengths, spectral resolutions, hindering unified modeling and cross-sensor transfer. From the perspective of imaging physics, these heterogeneous observations can be regarded as discrete measurements of an underlying continuous spectrum acquired through different sampling processes. Motivated by this perspective, we propose SpecUltra, a unified foundation model for heterogeneous spectral images. Specifically, SpecUltra employs 3D convolutional tokenization and wavelength-aware 3D RoPE to encode relative wavelength and spatial relationships, enabling fine-grained spatial-spectral modeling within a shared coordinate system. We further construct MultiHyper-200K, a large-scale multi-sensor HSI dataset, and pretrain SpecUltra using auxiliary-token-assisted mask image modeling (MIM), where a level token indicates the radiometric product type and register tokens absorb sensor- and acquisition-dependent variations. To bridge the spectral-granularity gap between HSI and MSI, we introduce Spectral Kernel Transformation (SKT), which transfers pretrained knowledge in parameter space by constructing MSI embedding kernels from fine-grained HSI-pretrained kernel slices. This design preserves pretrained spectral priors while maintaining compatibility with the pretrained backbone. Experiments on HSI and MSI classification and segmentation benchmarks demonstrate state-of-the-art or competitive performance across disparate sensors and downstream tasks.

---


### 497. [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenxin Zhu, Zhijian Huang, Cheng Chi 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Xiaomi Auto World Model 2.0, a unified streaming causal world model for Physical AI. It models and generates causal physical evolution in the real world, and unifies heterogeneous conditioning inputs for view-consistent generation. The architecture integrates View-Temporal Attention (VTA) to capture cross-view spatial dependencies and temporal dynamics, together with Multi-view Rotary Position Encoding (RoPE) to encode positional relationships across views and time. WorldRec 2.0 reconstructs static and dynamic 3D Gaussians from multi-view, multi-temporal observations in a single forward pass and uses their renderings as explicit scene context to preserve geometry and appearance during long-horizon generation. Conditioning inputs are fused through VAE latent concatenation in a shared representation space. We incorporate Gated Linear Attention (GLA) into the temporal layers of VTA for efficient streaming inference, reducing computation and KV-cache memory during multi-view rollouts. A physical-interaction data pipeline covers diverse interactions and long-tailed events. From Pre-train onward, these data are combined with large-scale videos and heterogeneous visual modalities to learn visual, geometric, and dynamic priors. During Mid-train, training across diverse view configurations further improves the model's ability to capture how actions and object states shape subsequent scene evolution. After distillation-based Post-train, we apply the model to closed-loop simulation, closed-loop training, and World Action Model (WAM) applications. These applications generate physically consistent future states and support world-state prediction, policy learning, and action generation for Physical AI.

---


### 498. [GaitFM: A Cross-Modal Foundation Model for Wearable Gait Assessment](https://arxiv.org/abs/2611.01684)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yize Cai, Zhiqing Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait assessment supports the diagnosis, monitoring, and prognosis of diverse movement-related conditions, such as neurological and musculoskeletal disorders. Recent advances in deep learning using everyday wearable inertial measurement units (IMUs) offer an accessible and low-cost approach to automated gait assessment. However, IMU measurements vary substantially across individuals, body locations, and device configurations, while existing deep learning models are typically developed using small, homogeneous datasets for specific clinical tasks, limiting their robustness and generalizability in diverse real-world contexts. Here we present GaitFM, a cross-modal foundation model for gait assessment using IMU sensors. GaitFM improves the generalizability of gait assessment by transferring knowledge from large vision models and pretraining on unlabeled IMU sensor data. We pretrain GaitFM on a large curated dataset comprising about 4,000 participants and 1.23 million gait windows across diverse clinical and daily conditions, sensor modalities, and body locations. GaitFM demonstrates strong performance across 18 gait-related tasks, including 3 gait parameter estimation tasks, 14 disease and gait abnormality detection tasks, and 1 clinical outcome prediction task. Furthermore, GaitFM generalizes across different sensor configurations and body locations, including those commonly used in clinical settings and everyday wearable devices. These findings demonstrate the effectiveness of transferring visual knowledge in improving sensor-based gait assessment performance, offering a new promising pathway for addressing data scarcity in the sensor and medical domains.

---


### 499. [Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation](https://arxiv.org/abs/2611.01858)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haowei Zhu, Qijie Wang, Jia Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation has achieved impressive results on short clips, yet generating long videos remains challenging due to error accumulation over extended horizons, where each predicted frame depends on potentially imperfect previous frames. Existing approaches typically rely on static context management strategies, such as sliding-window caches that discard early frames or fixed sink frames that permanently preserve initial content. These designs either lose critical long-range context or anchor generation to outdated information, which can lead to degraded fidelity, motion stagnation, and reduced diversity. In this paper, we propose Learning to Memorize (L2M), a learned context memory management framework that dynamically retains, evicts, and evolves historical frames according to predicted importance. The framework consists of an importance prediction router that estimates the relevance of each historical frame, degradation-aware training that improves robustness to noisy or corrupted context, and a dynamic memory initialization and evolution mechanism that updates long-term memory using exponential moving average (EMA) importance scores. This allows high-quality frames to replace stale anchors and enables memory to adapt naturally to scene evolution. Trained with a teacher-student distillation objective and sparsity regularization, L2M makes efficient use of a fixed KV-cache budget while preserving the most informative contextual information. Extensive experiments demonstrate that L2M improves long-horizon video generation quality and temporal consistency over existing baselines, providing a learned strategy for context memory management in long autoregressive video generation.

---


### 500. [Geometric Morphology Learning: Empowering Foundation Models from Structure to Spacetime Intelligence](https://arxiv.org/abs/2611.01932)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Li Sun, Philip S. Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometry is the very form that connects space, time, and matter, serving as the fundamental fabric of the physical world, from continuous fields to discrete structures. Despite its importance, deep learning is inherently blind to geometry. Riemannian geometry stands as a well-established mathematical foundation for studying geometry, yet it remains largely incompatible with deep learning architectures. To bridge this gap, we establish a new learning framework--Geometric Morphology Learning--that learns geometric or topological structures, shapes or conformations for representation learning, reasoning and action modeling. Moving beyond early attempts limited to specific geometric priors, this theory centers on modeling the intrinsic geometry of objects and learning from such geometric or topological knowledge. Specifically, we construct a neural bundle, a unified scaffolding linking local and global structures, and formulate differentiable operators, including connection and curvature, thereby enabling the study of geometry with advanced geometric concepts such as holonomy and cohomology. Consequently, Geometric Morphology Learning opens new horizons in foundation models, reasoning and planning, graph modeling, physical simulation, PDE systems, and dynamics, marking a fundamental shift toward instilling systematic geometry in artificial intelligence.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
