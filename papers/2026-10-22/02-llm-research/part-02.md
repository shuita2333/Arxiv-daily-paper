# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 51. [Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams](https://arxiv.org/abs/2610.27227)

**<font color=#1a73e8>作者：</font>** Yanan Ma, Yang Wang, David Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present \textbf{GRSE}, \textbf{G}roup-\textbf{R}elative \textbf{S}kill \textbf{E}volution, which assigns behavioral credit by comparison: inspired by GRPO, it executes each question several times under the same skill libraries and contrasts the executions to credit agent--skill pairs, with structured diagnosis of failures. On HotpotQA and LoCoMo with two open-weight actors, GRSE outperforms MASkills, the closest prior method, on HotpotQA and every LoCoMo category except open-domain, with the largest gains on multi-hop questions ($+6.7$ and $+3.2$ F1). Its gains rest on better-grounded retrieval rather than answers given without evidence, and its learned skills transfer between the multi-hop tasks. GRSE is robust to corrupted libraries: starting from planted harmful skills, it credits every planted skill with the correct sign and recovers the score of a clean library ($+6.3$ points), whereas MASkills misattributes two and falls below its starting point.

---


### 52. [Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](https://arxiv.org/abs/2610.27230)

**<font color=#1a73e8>作者：</font>** Tao Jiang, Benjamin Navet, Yousouf Taghzouti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more digital and precision chemistry. Dedicated scientific agents are becoming central to guiding the chemist through an ever-increasing amount of data and findings, including negative ones. Here, we introduce Magnolia, a persistent-memory artificial intelligence agent framework that integrates computational protocols, from docking to quantum chemistry, lab notebooks and chat logs relying on large language models (LLMs). It relies on a three-tier memory system: session-level observations are automatically captured and distilled into structured learnings, confirmed and elevated to project-tier entries and, when human-validated, promoted to cross-project rules that actively guide subsequent work and provide direct chemical feedback. We illustrate Magnolia on four case studies: quantum-chemical evaluation of aromatic systems (COMPAS database), molecular dynamics of butane and of modified DNA, and a protein-peptide docking campaign. Across these projects, Magnolia tracked 317 runs and accumulated 116 project-tier entries, from which four cross-project rules were promoted; in controlled replays of four tasks, runs with memory passed the checks that runs without it failed (for example, ten of ten docking-configuration checks, against one to four of ten). By combining automation, reproducibility, and human-in-the-loop control, our Magnolia framework streamlines docking, molecular dynamics and quantum chemistry calculations with direct analysis and LLM-augmented feedback, offering accelerated access to computational (bio)chemistry.

---


### 53. [EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](https://arxiv.org/abs/2610.27234)

**<font color=#1a73e8>作者：</font>** Zhiwei Liu, Zhujun Lan, Jielin Qiu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context software engineering. These evaluations live today in separate repositories with divergent runners, dependencies, and scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single aggregate number actually represents. We release EGI-BENCH, a unified LLM agent benchmark suite that consolidates eight enterprise facing agent benchmarks (CRMARENA, HERB, PERSONABENCH, USERBENCH, MCP-UNIVERSE, MCPEVAL, BENCHFORCE, LOCOBENCH) behind a single command-line interface with two runtime-budgeted execution modes. On top of the suite we define the Enterprise General Intelligence (EGI) Score, a six-dimensional framework (M1-M6) whose buckets are populated by fine-grained sub-metrics routed from each benchmark rather than by benchmark-level averages. We describe the suite, the sub-metric routing, and the quick/deep budgets, and report results for fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini families under quick mode. Top-line EGI ranges from 39.6 (GPT-4o mini) to 65.6 (gpt-5.5), and no single model dominates every capability axis: gpt-5.5 leads task outcome, planning, and retrieval grounding; Claude Sonnet 4.5 leads tool actioning and safety/abstention; and Claude Haiku 4.5 leads engineering quality. Code is available at this https URL.

---


### 54. [Predicting Linear Relational Decodability Without the Relation](https://arxiv.org/abs/2610.27241)

**<font color=#1a73e8>作者：</font>** Jonas Rohweder, Adrian Mülthaler, Farid Mehri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear relational embeddings (LREs) approximate a language model's subject-to-object mapping with an affine function. Their faithfulness varies enormously across relations, from near zero for person_father to the ceiling for country_capital_city. We investigate the factors that contribute to this variation and demonstrate that it can be significantly predicted from a readout that is not aware of the underlying relation. To do so, we propose a novel form of the Jacobian lens, the entity lens. Whereas the Jacobian lens is estimated across all tokens and concepts, the entity lens EL_t is trained to predict what the model will output for an entity of type t under the neutral prompt "{} is known for"; e.g., we train ELs for countries and persons. After estimating an entity lens, we measure how highly it ranks the model's answer for a relation without using any relation-specific information in estimation and prediction. Across 28 relations of the LRE dataset on Olmo-3-7B this relation-agnostic score correlates with LRE faithfulness at \rho = 0.7355 (p < .01). This suggests that linear decodability is largely a property of what a subject's representation already carries, rather than of the relation being decoded. Moving the unit of analysis from the relation to the individual fact, we conclude that new relation datasets and analysis methods are needed to address several problems in existing datasets, most prominently semantically weak first tokens (e.g., most predicted universities' first token is "University") and reference competition (e.g., the LLM confuses obscure actor names with competing non-actor entities that have the same last name). Our full pipeline is available at this https URL

---


### 55. [Diagnostic Analysis for Large Language Model Reasoning](https://arxiv.org/abs/2610.27245)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Dongqi Fu, Jun Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning structures (e.g., chains and graphs) are increasingly used for probabilistic inference, factuality verification, and uncertainty estimation, but their structural reliability is rarely evaluated directly. We test whether this reliability holds through a proposed two-stage diagnostic evaluation in open-ended multi-hop QA. Stage 1 tests different capabilities required to construct reasoning graphs, showing that graph reliability varies with topology, prompt design, and model family. Stage 2 uses uncertainty estimation as a downstream test case. Generated-edge experiments show that graph-based computation is sensitive to upstream graph errors, with performance dropping relative to the gold-graph setting. Gold-graph experiments further show that graph structure provides little benefit when used only as prompt context, but improves the separation of correct from incorrect answers by confidence score and enables node-level diagnostics.

---


### 56. [Target-Aware Curation of Hallucination Stress Tests for Large Language Models](https://arxiv.org/abs/2610.27247)

**<font color=#1a73e8>作者：</font>** Jiho Lee, Bingquan Zhang, Lin Ting Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination stress tests can yield similar average scores across language models even when different prompts elicit hallucinations in each model. We develop a procedure that iteratively edits source-grounded seed prompts to expose hallucinations in a target model. An LLM editor revises each prompt in response to the target's answer and a judge's category-specific score and explanation. In the main setting, the target also receives feedback on its previous response. Experiments cover 500 seeds from seven datasets and ten topics, with intrinsic and extrinsic hallucinations evaluated across open-weight and closed-source models. Editing substantially increases judge-rated severity over the seeds. In the baseline configuration, retained responses fall in the judge's strong-hallucination bin in 77.2% of runs targeting extrinsic hallucination and 74.2% targeting intrinsic hallucination. Later editing rounds account for more than half of the mean score increase. Among 219 prompts that pass model-assisted source-validity checks, 89 elicit responses containing unsupported claims. Across five models, 200 curated prompts yield similar average severity scores, although pairwise Spearman correlations between prompt-level scores are only $\rho=0.0387$ to $0.1897$. Curated prompts can be reused across models, but their diagnostic value depends on source validity and the failures they expose in each model.

---


### 57. [ValiAssist: Scaling LLM-generated Programming Feedback Validation by Demonstration](https://arxiv.org/abs/2610.27248)

**<font color=#1a73e8>作者：</font>** Xiaohang Tang, Rehema Abulikemu, Peng Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI can create programming feedback at scale, but validating its alignment with instructors' pedagogical goals and strategies remains challenging. Instructors may struggle to fully specify validation criteria upfront, as these often emerge through inspecting concrete examples and revising misaligned feedback. We present ValiAssist, a validation-by-demonstration system that infers reusable validation logic from instructors' revisions of AI-generated feedback and allows instructors to inspect and refine that logic as it is applied across other student submissions. In a comparative study with 16 instructors, ValiAssist helped instructors create and refine validation criteria, producing feedback that better aligned with their pedagogical intent (91% vs. 57%) and more than doubling the accuracy of correcting problematic criteria (77% vs. 32%). Our findings suggest that validation by demonstration can help instructors turn judgments they know how to make on individual cases into explicit, reusable logic, while progressively clarifying where those judgments do and do not generalize.

---


### 58. [TxnQA: Benchmarking Analytical Reasoning and Evidence Grounding over Transaction Event Sequences](https://arxiv.org/abs/2610.27256)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Yiming Bian, Yun-Shiuan Chuang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analyzing merchant transaction histories requires dynamic temporal filtering, entity resolution, and aggregation over irregular event streams--operations poorly captured by static tabular or time-series forecasting benchmarks. We introduce TxnQA, an analytical QA benchmark comprising 27 task families (81 templates) alongside a 5-scenario fraud-risk reasoning suite that evaluates both verdicts and supporting evidence over synthetic, privacy-mitigated transaction data. Ground-truth answers are computed programmatically, and model performance is decomposed into format-following rate (FFR), conditional content accuracy (CA), and end-to-end correctness (E2E). Evaluating prompted proprietary baselines and six LoRA-adapted open-weight models shows that adaptation reliably enforces output schemas but leaves arithmetic bottlenecks: Gemma-4-31B-IT and Qwen3-8B attain E2E scores of 0.867 and 0.816, whereas evaluated MoE checkpoints reach only 0.632-0.713. Furthermore, on the 500-instance fraud suite, verdict accuracy frequently exceeds 80%, yet joint accuracy (requiring exact evidence attribution) collapses to at most ~23%. These findings identify schema compliance, semantic calculation, and evidence attribution as three distinct bottlenecks in transaction-sequence QA.

---


### 59. [When Models Know but Can't Linearly Say: Relational Encoding Limits Linear Vulnerability Classification in Code LLMs](https://arxiv.org/abs/2610.27257)

**<font color=#1a73e8>作者：</font>** Rui Melo, Andre Catarino, Claudia Mamede 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models can detect vulnerable code, yet the form of vulnerability encoding in their representations remains unclear. We analyze 8 code models spanning 6.7B-15B parameters on C programs using three datasets (DELTASECOMMITS, SVEN, and PRECISE-BUGS), comparing two diagnostic tasks on the same representations: identifying what patterns the code instantiates, and determining whether it is vulnerable. Models encode the first with high fidelity. Under the studied paired C-code datasets and linear-probing setup, vulnerability information is more accessible as a paired relational signal-whether code A is riskier than code B-than as a globally separable categorical label. This structural difference has implications for classification: the model reliably ranks which code is riskier but standard classifiers on isolated samples achieve limited accuracy because vulnerable and secure samples form overlapping distributions in representation space.

---


### 60. [Guided Diffusion for Trustworthy Synthetic Text Generation](https://arxiv.org/abs/2610.27259)

**<font color=#1a73e8>作者：</font>** Qi Pang, Hanshen Xiao, Andre Manoel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Large Language Models is fueled by massive datasets, yet this reliance poses severe privacy risks, as models can inadvertently memorize and even directly output sensitive training data. Synthetic text generation offers a promising solution to this challenge; however, existing methods struggle to reconcile rigorous privacy guarantees with high data utility. In this paper, we propose a new paradigm for private synthetic text generation: Guided Diffusion. Leveraging the unique steerability of Diffusion Language Models, we introduce novel sampling and re-masking procedures that actively guide the iterative denoising steps. These mechanisms steer the generative process to reconstruct fluent text that adheres to a target semantic distribution. We demonstrate that our framework is naturally compatible with Differential Privacy (DP): once the semantic embeddings of the private corpus are protected, the DP guarantee carries over to the generated text by post-processing. Empirically, we show that our approach generates high-quality synthetic text with precise semantic alignment. Furthermore, we validate its effectiveness in DP synthetic text generation: across two datasets and two diffusion backbones, it outperforms Private Evolution and DP-SGD-based fine-tuning in distributional fidelity and downstream utility, while generating significantly faster than Private Evolution. We further extend the framework to Data-Specific Indistinguishability (DSI), which adds a formal certificate against data poisoning and memorization at a small utility cost.

---


### 61. [Auditing Safety Preference Supervision with Recorded Derivations](https://arxiv.org/abs/2610.27266)

**<font color=#1a73e8>作者：</font>** Chenhan Lyu, Amir Rahmani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference labels align model training, but the judgments behind them are difficult to inspect or verify. In this paper, we examine how preference construction can be checked when intermediate decisions are recorded, and which of them remain uncertain. We present Symbolic Preference Labeling, a method in which a pretrained language model classifies predefined attributes of prompts and responses. Explicit rules assign response verdicts, and a fixed verdict ranking determines the preference label. Each preference label has a recorded derivation: the response verdicts and preference label can be recomputed from the stored attribute assignments, rules, and verdict ranking without rerunning the language model. On 200 prompts annotated by human raters, the language model produces valid structured outputs for 192 prompts. All eight parsing failures occur in the subset of self-harm prompts marked as harmful. Using 465 preference pairs, we train one policy model with direct preference optimization across five training seeds. Mean measured benign refusal is 40.82 percent on 1,319 benign prompts that resemble unsafe ones, and mean measured toxic refusal is 84.98 percent on 655 toxic prompts. This study distinguishes the reproducibility of preference labels from attribute correctness. The recorded derivations make preference construction open to inspection, while attribute correctness and semantic safety require separate validation.

---


### 62. [African Languages AI Safety Readiness Report](https://arxiv.org/abs/2610.27269)

**<font color=#1a73e8>作者：</font>** Israel Abebe Azime, Jesujoba O. Alabi, Tajuddeen Gwadabe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread adoption of large language models (LLMs) across languages and domains, AI safety has emerged as a critical global concern. However, due to resource constraints, research and development efforts tend to prioritize a limited number of high-resource languages, leaving many others, especially those spoken in Africa, underrepresented. While existing research on language "resource-ness" has largely examined whether sufficient resources are available to develop language technologies, the question of whether languages are adequately represented in AI safety research has received attention only more recently. This report examines the readiness of African languages for inclusion in AI safety discussions, drawing on existing literature and data. It considers four factors: the availability of AI-relevant resources, including text data; national AI policy support; performance on established text benchmarks; and speaker population. Based on these factors, languages are grouped into four readiness categories: fully ready, mostly ready, emerging, and foundational support needed. This classification is intended to inform the inclusion of African languages in AI safety benchmarks, highlight varying levels of preparedness, and guide strategic investment in data development, policy, and community engagement for underrepresented languages.

---


### 63. [TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation](https://arxiv.org/abs/2610.27290)

**<font color=#1a73e8>作者：</font>** Akash Gokul, Srijan Bansal, Yingbo Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-case generation is critical but remains challenging for language models. Existing test-time scaling methods either isolate candidates or aggregate traces, which do not scale to long-horizon tasks. We present TEX, a collaborative test-time scaling framework based on execution-driven cross-validation. TEX parallelizes agents to generate tests and patches, cross-executing each test against every patch to form a $K \times K$ feedback matrix. Agents use their matrix slices for refinement, enabling objective validation without verbose trace sharing. On SWT-Bench Verified, TEX achieves 86.4%, establishing a new state-of-the-art and improving +9.0% over single-agent baselines. Moreover, even random selection from TEX outputs (84.4%) surpasses the previous SOTA (84.0%), showing collaborative execution feedback improves solution quality, not just best-case samples. Our results highlight execution-grounded feedback as an effective scaling mechanism for long-horizon agentic tasks.

---


### 64. [RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](https://arxiv.org/abs/2610.27295)

**<font color=#1a73e8>作者：</font>** Xinying Cai, Bin Hu, Mingyu Jin 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides only a limited picture of how steering methods perform in the real world. We therefore introduce RealControlBench, a comprehensive benchmark for evaluating fine-grained steering of LLMs and LLM agents across diverse behavioral targets and interaction settings. RealControlBench extends steering evaluation beyond isolated generations to complex, execution-grounded, multi-turn agent interactions, covering five complementary dimensions: instruction-following control, agentic tool-use decision control, reasoning-performance steering, reasoning-length control, and trajectory-conditioned safety awareness. Rather than measuring steering success alone, the benchmark jointly evaluates target controllability and capability preservation, including instruction following, reasoning performance, and downstream agent utility and safety. It further examines whether steering effects remain specific and robust across prompt variations, domains, and model architectures. Our evaluation shows that existing steering methods remain unreliable across realistic control objectives: they often fail to consistently induce the intended behavior and can substantially degrade the model's underlying task performance. These results suggest that strong steering effects in controlled settings do not necessarily translate into reliable control in more realistic evaluations. By providing a unified, model-agnostic steering evaluation framework, RealControlBench aims to support the development of steering methods that are not only effective but also precise, robust, and useful in realistic AI deployments.

---


### 65. [Stronger artificial intelligence breakthroughs hasten their own exhaustion](https://arxiv.org/abs/2610.27296)

**<font color=#1a73e8>作者：</font>** Beichen Lu, Honglin Bao, Qi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress in artificial intelligence is widely assumed to scale with effort: more researchers, papers and investment should accelerate discovery. Theories of technological growth instead locate the difficulty of discovery in the space of ideas. Here we show that neither scale nor space is enough: breakthroughs depend on diverse attention, which collective concentration can deplete. Across 36 years of computer science, we analyze 7.2 million papers, 73,089 peer reviews and 3.7 million researchers and their topic shifts. The field expanded while its attention narrowed sharply after the Transformer. Over half of topic-shifting researchers moved into AI, especially mid-career ones, and reviewer confidence fell by a full point on a 5-point scale. Each successive breakthrough, from AlexNet to large language models, raised the field's carrying capacity for ideas but was followed by steeper exhaustion of those ideas. Bigger breakthroughs capture attention more completely, depleting the diversity their successors may draw upon. Structural biology shows the same cycle after cryo-EM and AlphaFold. Simulations show how well-intentioned and widely used policies such as reciprocal reviewing empower prolific authors and further narrow what the field accepts. We call for institutions that protect diverse attention in artificial intelligence rather than reward concentration on the winning paradigm.

---


### 66. [Evaluating Context Compaction on the Questions That Come Later](https://arxiv.org/abs/2610.27301)

**<font color=#1a73e8>作者：</font>** Junwei Yao, Yongxi Zhou, Zike Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model agents compact their context for the question at hand, but the compacted context must also serve questions that come later. We evaluate compaction on these later questions, using four corpora that annotate the evidence of several questions per text and recorded agent trajectories, and compare every method with random deletion at the same budget. On MultiRC, keeping the sentences that gpt-6-luna (through the OpenAI Decisions API) judges necessary for the current question raises its accuracy on that question by 11.4 points at 25% of the tokens. On the later questions, however, no method that selects sentences for the current question does detectably better than deleting sentences at random. Deleting words instead of sentences does better: LLMLingua-2, which ignores the question, beats random sentence deletion at the same token count by 12.5 points on the later MultiRC questions. It keeps about twice random deletion's share of the evidence's content words, and at equal content-word retention its gain shrinks to 7.3 points (exploratory). On FEVER, label accuracy can overstate what the kept text supports: the gain of sentence selection is no longer detected when answers are scored against the kept evidence, and the 21.0-point gain of LLMLingua-2 is not shown to rest on the kept text. The ranking also depends on the setting: on Evidence Inference sentence selection beats LLMLingua-2 at a nominal 25% budget, and on $\tau$-bench trajectories, whose later tool calls need exact identifiers, it beats random deletion while LLMLingua-2 shows no detected gain. Scores on the question a compaction was made for do not reliably show how it serves later ones.

---


### 67. [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](https://arxiv.org/abs/2610.27304)

**<font color=#1a73e8>作者：</font>** Jalil Alva, David Harper, Abigail E. Thornton 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are deployed globally, yet safety alignment and evaluation remain concentrated in English: harmful requests refused in English can elicit unsafe completions when translated into low-resource languages. We evaluate ten widely deployed LLMs across 79 languages (English plus 78 low-resource) under a translation-bypass threat model, using a metric conditioned on English safety, which separates translation bypass from unsafety already present in English. English safety does not transfer reliably: conditioned on safe English completions, mean bypass rates range from 21.9% to 44.4%. Bypass risk concentrates in a subset of language families, a pattern broadly shared across models. The shared ordering is confounded with translation degeneracy, but its variation across models is significant and survives every control we apply. We also show that per-model bypass rates do not identify a stable ranking: nine of ten models change rank across three conditioning schemes that estimate the same quantity, with no change to any underlying response.

---


### 68. [Evolving Self-tuning Benchmarks for Long-Horizon Tool Use](https://arxiv.org/abs/2610.27307)

**<font color=#1a73e8>作者：</font>** Hyunji Alex Nam, Michael Dennis, Natasha Jaques 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (**T**ool **U**se **R**elated **T**asks with **L**ong-Horizon **E**volution), an Unsupervised Environment Design (UED) approach to evolve existing tasks using a proposer, a solver, and a feedback generator large language model agents. The proposer is rewarded for difficult yet solvable tasks based on the solver's empirical performance, and the feedback generator summarizes the solver's execution traces for the proposer to exploit. TURTLE produces evolving, self-tuning test suites adaptable to different environment requirements, from supporting user simulators and dense document retrieval to interacting across multiple apps. Empirical results on AppWorld, $\tau$-Bench, and AutomationBench using Gemma 4 31B-it show that the evolved tasks target the desired difficulty range (e.g., a 165\% increase in the percentage of hard tasks on AppWorld), increase task diversity (in terms of reasoning and simultaneous tool interactions), and elicit a broader range of failure modes than the original tasks.

---


### 69. [Steering Vision-Language Models for Visual-Contextual Privacy in Location Disclosure](https://arxiv.org/abs/2610.27323)

**<font color=#1a73e8>作者：</font>** Wenyue Chen, Yuhan Cheng, Ruixin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can infer sensitive information such as geolocation from subtle visual cues, creating privacy risks when responses disclose more detail than the visual context warrants. We study visual-contextual privacy in geolocation disclosure, where a VLM should reveal location information only at the granularity appropriate to the visual context depicted in the image. We first show that this contextually appropriate granularity is recoverable from pre-generation hidden states, even when generated responses are misaligned, with disclosure levels exhibiting an ordered structure along a common hidden-state direction. Motivated by this, we propose an inference-time route-and-steer framework: an ordinal granularity router maps visual-contextual privacy representations to a disclosure route, and a disclosure-level-conditioned steering module applies route-specific hidden-state interventions during decoding. Across four VLM backbones, our method improves visual-context-aware disclosure alignment, better balances over- and under-disclosure, and incurs only modest changes on general capability benchmarks. It further transfers to another dataset with a distinct data distribution and privacy-risk taxonomy.

---


### 70. [Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics](https://arxiv.org/abs/2610.27327)

**<font color=#1a73e8>作者：</font>** Yuqing Yang, Yurong Liu, Deqing Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents can answer analytical questions over a data lake by discovering, cleaning, and joining the relevant data. However, they discard this work after each question and redo it from scratch for the next one. Tool evolution, which automatically builds and refines reusable tools across tasks, is a natural fit for this repetition. Since a ground-truth label for a data-lake question requires an expert to solve it first, we consider the unsupervised setting. We propose TEAL (Tool Evolution for Analytics over data Lakes), which evolves a library of tools and usage skills for a given Worker agent without labels. Two agents propose tools from complementary evidence, an Explorer from the data lake itself and a Critic from Worker trajectories. A proposed change is kept only if the Worker adopts the tool on a rerun without extra steps and any changed answer is supported by trajectory evidence. We also introduce TEAL-Q, which generates synthetic questions for tool evolution when real ones are unavailable. We evaluate on KramaBench and LakeQA with four Worker LLMs under step budgets, which cap the number of steps the Worker may take per question. With a tight budget of 10 or 15 steps, TEAL improves every Worker on both benchmarks, lifting Sonnet-5 at 15 steps by 9.3 points on KramaBench and 21.7 points on LakeQA. A tighter budget also yields better feedback for evolution. For example, Sonnet-5's LakeQA library evolved at 20 steps and deployed unchanged at 30 steps scores 68.3, above both the baseline (59.6) and a library evolved directly at 30 steps (64.2). Additionally, a library evolved on synthetic questions performs comparably to one evolved on real questions. These results show that useful tools can be evolved without labels, and hopefully inspire future work on what to evolve and how to obtain feedback in unsupervised agent evolution.

---


### 71. [Inspectable LLM-Simulated Participants for Qualitative Interview Rehearsal](https://arxiv.org/abs/2610.27333)

**<font color=#1a73e8>作者：</font>** Hangyue Zhang, Qiran Hu, Ziyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used across research workflows, including research ideation, qualitative analysis, and participant simulation. Within work on participant simulation, prior studies have largely evaluated simulated participants by how realistic or human-like their responses appear, leaving less known about how researchers use and critique these materials when revising interview protocols before fieldwork. We present Rehearsim, an inspectable research probe that treats LLM-simulated participants as materials for methodological rehearsal rather than substitutes for human participants. Rehearsim combines literature-grounded participant construction, interactive interview rehearsal, and traceable thematic review while keeping protocol decisions under researcher control. In a study with 21 qualitative researchers, participants used simulated materials to surface assumptions and gaps, reconsider participant populations, revise target populations, and develop follow-up probes. They also identified risks, including the concealment of weak questions, dismissal of unexpected synthetic details, and interpretive anchoring from generated themes. We derive an inspectable-rehearsal framework emphasizing traceability, contestability, researcher control, and epistemic boundaries.

---


### 72. [Modeling Authentic Research Trajectories: A Graph View of Research Ideation](https://arxiv.org/abs/2610.27337)

**<font color=#1a73e8>作者：</font>** Ruochen Li, Zhiyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The research idea in a published paper is rarely the project's initial idea. Between the two lies a closed-loop process in which researchers run experiments, derive insights, identify challenges, explore the literature, and revise the idea, with each step motivated by evidence and reasoning they can articulate. We call the path one idea takes through this process, with the evidence and reasoning behind each step, its authentic research trajectory. Although it underlies every scientific contribution, it is rarely recorded. Existing LLM-based research agents generate an idea once, refine it against reviews, literature, or their own experimental results, or search over candidate ideas and experiments. In all of them the text of the idea evolves, while the evidence and reasoning that connected one version to the next are discarded. We propose the Research Progress Graph (RPG), a representation of authentic and complete research trajectories. An RPG records the evolution of an idea as typed research states connected by cognitive transitions, each annotated with a temporal index and the reasoning behind it, which makes this evolution an explicit object of study. We ground the representation in authentic trajectories whose steps their authors justify in annotations and papers. Comparing the representations of thirty-five research agents with the RPG, we find that each is an incomplete RPG; none keeps the state that changed, the evidence that changed it, and the reasoning connecting them as one evolving record. Modeling ideation with the RPG changes how research agents should be designed, evaluated, and trained. Agents predict the next research state instead of a complete idea, ideas are evaluated as trajectories instead of final texts, and authentic trajectories serve as training data. These directions shift research agents from generating static ideas to modeling how ideas evolve.

---


### 73. [Look Before You Reason: Implicit Visual Thinking for Efficient Multimodal Reasoning](https://arxiv.org/abs/2610.27341)

**<font color=#1a73e8>作者：</font>** Zerui Chen, Changrui Chen, Fei Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet they remain limited on tasks requiring fine-grained understanding of small or easily overlooked image regions. Recent thinking with images approaches mitigate this limitation by allowing models to inspect images through operations such as zooming, cropping, or code execution. While effective, their multi-turn interactions with VLMs introduce redundant token computation and slow inference, and separate region inspection from the reasoning step that depends on it. To address these issues, we propose Look Before You Reason (LoRe), an implicit visual thinking framework for efficient visual reasoning within a single-turn VLM interaction. Given an image and a question, LoRe predicts the most relevant image region, aligns it with the corresponding image patch features, and strengthens the associated key-value (KV) cache entries, enabling subsequent decoding to directly exploit the selected visual cues without additional visual inputs or explicit tool calls. We further employ reinforcement learning to guide the VLM toward identifying informative image regions and leveraging them during reasoning. To support fine-grained evaluation of multimodal reasoning, we introduce COCO-ObjQA, a large-scale benchmark for object-centric multimodal reasoning. Experiments on three challenging multimodal benchmarks demonstrate that LoRe consistently improves VLM reasoning performance with low additional inference overhead.

---


### 74. [An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context](https://arxiv.org/abs/2610.27347)

**<font color=#1a73e8>作者：</font>** Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignty, carbon impact, compliance, and ethics. The agent relies on a large language model that scores a text on a fixed rubric, grounds its judgment in a reference legal corpus, and, when the score falls at or below a critical threshold, runs a corrective chain made of self-healing rewrites, a compliance label, an explainability report, and escalation to a human reviewer. We describe what the language model does at each step, how the memory of the agent is organized, and how the same implementation can be pointed at different reference corpora. We evaluate the agent in a Canadian and Quebec context, on a corpus of thirteen legal instruments that brings together federal and provincial texts, international treaties, and municipal documents of the City of Trois-Rivières. The evaluation relies on a hand-annotated gold standard of fifteen texts and combines classification metrics, a repeated-query stability test, retrieval precision, and a composite score. On this gold standard the agent separates every conforming text from every non-conforming one, its scores remain stable under repeated queries, and the index returns relevant passages.

---


### 75. [Exposing Vulnerability Monoculture Through Systemic Adversarial Robustness](https://arxiv.org/abs/2610.27353)

**<font color=#1a73e8>作者：</font>** Leo Elmecker-Plakolm, Lukasz Szpruch, Avishek Joey Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Beneath the apparent diversity of foundation models lies an increasingly homogeneous technical stack of common training pipelines, distillation methods, and data. These shared algorithmic choices can expose an otherwise distinct model ecosystem to concentrated risks leading to a vulnerability monoculture. Yet current practice in assessing adversarial robustness is restricted to individual robustness scores and attack transfer rates, leaving open the unexplored fundamental question: how many attacks suffice for catastrophic widespread compromise? In this paper, we investigate the empirical nature of shared vulnerabilities within a model pool and introduce Systemic Adversarial Robustness (SAR), a novel measure of shared vulnerability of a model pool through the attack diversity needed to exploit it. Specifically, SAR interpolates between single-attack transferability and independent per-model robustness: small values reveal a vulnerability monoculture, whereas large values indicate that failures are dispersed across models. We theoretically formulate SAR as a partial set-cover problem with provable approximation guarantees---enabling the development of scalable algorithms to empirically measure the systemic adversarial robustness. We empirically test the shared vulnerability of vision and large language models and characterize their shared collective vulnerability curve. Specifically, we demonstrate that model pools distilled from DeepSeek-R1 and Claude Opus 4.6 exhibit lower estimated systemic robustness than their corresponding parent pools, revealing a potential systemic cost of frontier-model distillation. Our framework seeks to establish vulnerability monoculture as a measurable target for a more wholistic adversarial evaluation of model populations.

---


### 76. [On the Limits of Scale: Inverse Scaling in Vision-Language Models](https://arxiv.org/abs/2610.27360)

**<font color=#1a73e8>作者：</font>** Rohit Saxena, Alessandro Suglia, Marek Rei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling laws suggest that increasing model size, training data, and compute generally yields monotonic performance improvements. While this often holds at the aggregate level, we present systematic evidence that vision-language models (VLMs) exhibit inverse scaling at the subtask level: specific question categories on which larger models perform worse than smaller counterparts within the same model family. We evaluate 19 models from four distinct model families across eight multimodal benchmarks (nine evaluation splits), answering 29,386 questions per model, 558,334 model-question evaluations in total. Using per-question pairwise analysis across all model pairs in each family, we identify 375 subtask-model-pair combinations exhibiting inverse scaling, spanning 4,342 unique queries where a smaller model answers correctly but a larger model fails, and we find that these patterns replicate across independently developed architectures. We identify 13 subtask-dataset pairs that show inverse scaling across multiple families, consistent with the phenomenon being task-driven rather than model-specific. The most affected domains in our study include multi-image spatial reasoning, visual perception, and university-level STEM knowledge, with accuracy gaps exceeding 20 percentage points in several cases, while diagram understanding appears comparatively resistant. These findings challenge the assumption that increasing model size uniformly improves multimodal capabilities and suggest that model selection should be task-aware.

---


### 77. [On the LLM Verification for Argument Graph Generation](https://arxiv.org/abs/2610.27361)

**<font color=#1a73e8>作者：</font>** Jakub Bąba, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems can formalize natural-language argumentation end-to-end, turning plain text into structured graphs by classifying components, connecting them with relations, and enriching the resulting graphs into formal models. Quality assurance for those graphs is almost always another LLMs: a reviewer, judge, or critic agent. On the other side, in adjacent neuro-symbolic fields, such generated output is often verified symbolically by external checks and solvers. In this work, we argue that in argument graph verification, the allocation should be similar, and based on what each instrument can guarantee. We propose layered verification: starting from deterministic checks, moving to solver-based and LLM reviews, and utilizing debate only under uncertainty, leaving human judgment for what no other instrument can decide. We ground our principle with a study on human-annotated graphs with injected structural defects. An LLM reviewer detects them at near-ceiling recall, including cycles in the support relation, but it objects to almost one in a ten correct graphs, even though it should not, happens to be inconsistent in verdict on identical inputs and is significantly slower than the equivalent exact check. It shows that while LLM reviewer does not lack the ability to detect structural defects, it is worth having a deterministic verification gates.

---


### 78. [Explore More, Validate Less: Efficient Reflective Prompt Optimization](https://arxiv.org/abs/2610.27367)

**<font color=#1a73e8>作者：</font>** Xiaofan Zhou, Lu Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reflective prompt optimization improves instructions using task feedback, but coupling candidate generation with full-validation-based selection can make search costly and sequential. We propose a two-stage framework that decouples reflective candidate-pool construction from validation allocation. During construction, we sample multiple parents and reuse each parent's training responses across parallel reflection branches. Each revision is screened against its parent on a small training minibatch, allowing locally improved candidates to support further revisions without full validation. After construction, an exploration policy selects candidates from the frozen pool under a fixed full-validation budget, and the prompt with the highest measured validation score is returned. This separation allows candidate-pool size and validation budget to be set independently. We evaluate random selection and learned score prediction with similarity-based exploration on five benchmarks using Qwen3.5-9B and Llama-3.1-8B-Instruct. With 100 retained candidates and 20 full validations, our framework improves over the initial solver by up to 11.22 percentage points. Learned selection improves over the initial solver in all ten comparisons, although neither selection policy consistently outperforms the other. These results support separating reflective search from budgeted validation while leaving room for stronger candidate-selection policies.

---


### 79. [SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks](https://arxiv.org/abs/2610.27370)

**<font color=#1a73e8>作者：</font>** Sicong Huang, Ian Lane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Span-level hallucination detection pinpoints unsupported content in LLM outputs, enabling actionable feedback and targeted mitigation. Existing evaluations for span-level hallucination detection methods are fragmented across tasks, annotation formats, and metrics, and most span-level datasets cover only a single NLG domain, making it difficult to assess whether a detection method actually generalizes across tasks and domains. In this paper, we introduce SHAM-Bench (Span-level Hallucination Benchmark Across Multiple Tasks), a unified benchmark for span-level hallucination detection spanning six NLG tasks, aggregated from existing human-annotated datasets totaling 6,461 examples under a common schema and evaluation protocol. Using SHAM-Bench, we evaluate existing hallucination detection methods and find that fine-tuned detectors often perform well in-domain but degrade under distribution shift, whereas prompt-based methods with reasoning are more robust across tasks. Our analysis further shows that subtle unsupported content remains difficult to detect and span-level evaluation is still challenged by ambiguous span boundaries and noisy labels. We release the dataset, evaluation code, and a public leaderboard to support future research on broadly generalizable hallucination detection.

---


### 80. [Shaped SAEs: Expanding the Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2610.27375)

**<font color=#1a73e8>作者：</font>** Oveys Delafrooz Noroozi, Bhagyashree Puranik, Upamanyu Madhow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) seek to decompose the dense activations of large language models (LLMs) into sparse, potentially interpretable features using a learned overcomplete dictionary. In this work, we ask whether it is possible to enhance the semantic selectivity of the learned dictionary atoms by linearly \emph{shaping} the dense activations prior to learning an SAE. We explore rank-reducing transformations based on the recently introduced J-space corresponding to the averaged Jacobian from the current layer to the LLM output, projecting activations onto the ``live'' subspace spanned by eigenmodes of the Jacobian with larger singular values (which we expect to be more semantically relevant). We also introduce a new approach for training SAEs in which (a)~an affine shaping transformation is learned along with the dictionary atoms, (b)~the atom selection mechanism is based on the TopK projections along the one-dimensional subspace spanned by the atoms, and (c)~reconstruction is carried out using the same atoms. We call this approach a Matched Filter SAE (MF-SAE) based on analogies with communication theory. The promise of shaping is demonstrated via evaluations against dense activations and state-of-the-art SAEs on benchmarks including SAEBench and SAE Probes.

---


### 81. [REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents](https://arxiv.org/abs/2610.27377)

**<font color=#1a73e8>作者：</font>** Xinyi Lisa Chen, Pedro Herrero-Vidal, Xiaohan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents now autonomously complete long-horizon tasks, such as repository-level coding, through hundreds of think-act steps, yet the experience each run produces is rarely reused on the next. Prior memory systems concentrate on retrieval, finding the most relevant past trajectory. Retrieval cannot observe the running agent, so it cannot decide whether the agent needs an experience, at which point, or for how long. We introduce REM (Reusable Experience Memory), a framework that manages the memory lifecycle from inside the agent's think-act loop through three explicit decisions. What to store: each completed trajectory is consolidated into a phase-structured document, two orders of magnitude smaller than the trajectory. When to recall: the document is injected at the start of the task; the costlier implementation record is withheld until an in-loop gate detects the agent struggling. What to forget: the record is evicted after a single exposure. On repository-level bug fixing (SWE-ContextBench Lite), REM retrieves the related trajectory more accurately than every state-of-the-art memory system (68.7% vs. 55.6% match@1) and improves, in every replicate, end-task resolution (27.6% vs. 24.9%) at 17% lower cost. Injecting the same experience as a summary or raw trajectory, even when oracle-retrieved, does not. Ablating any of the three decisions reduces resolution. Altogether, these results demonstrate that the bottleneck in experience reuse is not retrieval fidelity but how experience is stored and governed across its lifecycle, opening a control-theoretic perspective on agent memory.

---


### 82. [DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2610.27379)

**<font color=#1a73e8>作者：</font>** Shreyas Kulkarni, Uttam Gurram, Madhav Kanda 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-diffusion speculative decoding accelerates large language model inference by drafting multiple tokens in parallel. However, one-step drafting in discrete diffusion is limited by token factorization error: each token is predicted from the same masked block, without conditioning on the tokens selected at other positions in that step. This can produce inconsistent drafts and reduce acceptance length. Iterative refinement mitigates this limitation by conditioning later predictions on previously committed tokens, though additional passes increase drafting cost. To address this trade-off between draft fidelity and inference latency, we introduce DStill, a two-stage framework that distills a target-conditioned drafter's own multi-step refinement into one-step drafting. We first train the drafter to complete partially revealed blocks, then use its refinement trajectories to train a student to predict the final completion in one pass. Using a curriculum that gradually transitions from partial to fully masked inputs, we successfully transfer the multi-step refinement capabilities into one step. Across reasoning, math, code benchmarks on three model families DStill improves acceptance length by up to 28% and speedup by up to 25% over one-step DFlash, achieving up to 6.45x speedup over auto-regressive decoding.

---


### 83. [AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal](https://arxiv.org/abs/2610.27383)

**<font color=#1a73e8>作者：</font>** Nishant Abhishek, Ping Charoenwet, Kla Tantithamthavorn  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may depend on lines found across different repository files. Recent approaches such as AgenticSCR have shown that LLM agents can explore repository files and use security knowledge to improve secure code review. However, these approaches mainly rely on external commercial LLMs and can provide a large amount of security knowledge to the agent at once. This creates an important question of whether agentic secure code review can also be performed effectively using locally deployed open-weight LLMs with more focused and relevant security knowledge. In this paper, we propose AgenticVulHunter, an agentic secure code review approach and tool that can run with a locally deployed open-weight LLM. We evaluate AgenticVulHunter on 144 vulnerability cases from SCRBench using Qwen3-Coder-30B and DeepSeek V3.1 Terminus. We measure what percentage of generated review comments correctly identify the vulnerable location, match the vulnerability type, and provide a relevant security review comment together. AgenticVulHunter achieves an accuracy of 18.4% with Qwen3- Coder-30B and 23.8% with DeepSeek V3.1 Terminus, compared with 11.8% for our AgenticSCR-style reproduction using Qwen3-Coder-30B and 17.5% for AgenticSCR using Claude Sonnet 4.

---


### 84. [Correcting Attribution Patching with a Few Exact Measurements](https://arxiv.org/abs/2610.27393)

**<font color=#1a73e8>作者：</font>** Luyang Zhang, Minxing Zheng, Jialu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability asks which language model components matter for a behavior, and activation patching answers by changing one component's activation and measuring its effect, at a cost growing with components and prompts. Attribution patching estimates these effects from one gradient pass, but its estimates can be far off, and verifying each one restores the cost. Can the structure of these errors reduce this cost? We propose Guided-AP, which uses a few exact measurements to reveal attribution patching's errors and correct unmeasured estimates. On a single prompt, many components' errors share one sign, so a small exact sample yields one correction for the rest. Over many prompts of one task, components are misestimated similarly, so a few measured prompts show what to verify and how to correct each component's average effect. Our analysis shows that choosing what to verify needs error size, while correction also needs sign. On a single prompt, the correction lowers error by up to 26% across three behaviors at the compute of verifying the largest estimates and also on larger models. Over many prompts, learned corrections cut the error of average effects on factual completion by 75% to 79%, repaying their cost in long analyses.

---


### 85. [ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions](https://arxiv.org/abs/2610.27400)

**<font color=#1a73e8>作者：</font>** Lilin Xu, Linyang He, Kaiyuan Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are moving beyond reactive responses toward proactive assistance that anticipates user needs without explicit requests. However, existing proactive agents primarily address immediate needs, while many everyday situations involve delayed intentions that can only be acted on hours or days later. Humans handle such intentions through prospective memory, the ability to remember to act on an intention when the right moment arises. In this paper, we introduce ProMemAgent, the first proactive agent to incorporate prospective memory over everyday sensory contexts for long-horizon proactive assistance. ProMemAgent organizes past sensory perceptions (e.g., egocentric video and audio) into context-aware memory, generating prospective cues and linking earlier events with subsequent developments for future retrieval. Given the current context, it retrieves relevant past events and performs memory-augmented proactive reasoning to determine whether assistance is needed. We further introduce CPMBench, the first benchmark for evaluating long-horizon proactive assistance over sensory contexts, comprising 1,000 instances across eight everyday categories. Extensive experiments show that ProMemAgent achieves the best memory retrieval performance and consistently outperforms all baselines on long-horizon proactive assistance.

---


### 86. [More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents](https://arxiv.org/abs/2610.27406)

**<font color=#1a73e8>作者：</font>** Ruhan Wang, Kishan Panaganti, Dongruo Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can improve across tasks without updating model parameters by storing experience from their own executions in external memory and reusing it to guide later decisions. A central design question is whether to retain only observed trajectories and outcomes or also the rules, summaries, and skills inferred from them. Retaining these abstractions allows agents to reuse strategies without repeatedly deriving them from raw trajectories. However, errors in stored abstractions can propagate to subsequent decisions through retrieval and reuse. They can also shape execution trajectories, which then become the basis for new abstractions that reproduce the original errors. We term this feedback mechanism error reproduction: errors are regenerated through a cycle of abstraction, execution, and re-abstraction, extending their persistence beyond direct reuse of the original faulty knowledge. We propose Anti-Persistence, a memory design that accumulates trajectories and outcomes while reconstructing task-specific guidance on demand. An adaptive selector uses prior outcomes to decide whether and how to synthesize guidance, which is discarded after execution. This prevents its direct reuse as a stored object, although indirect feedback through retained trajectories remains possible. Across different benchmarks and backbones, Anti-Persistence achieves higher overall held-out success and the lowest average LLM-call cost among the evaluated memory designs. These results support separating experience accumulation from abstraction persistence in memorybased self-improvement.

---


### 87. [Looking Into The Past: The Impact of Context on Detecting Deceptive Statements](https://arxiv.org/abs/2610.27407)

**<font color=#1a73e8>作者：</font>** Alex Clay, Ernesto Jimenez-Ruiz, Pranava Madhyastha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deception detection typically considers messages in isolation. Previous works in claim verification and role detection have displayed that additional information such as gameplay history is crucial to successful predictions. In this work, we demonstrate the value of preceding gameplay dialogue when applied to deceptive message detection within the hidden role game of Avalon. The findings show that LLMs can see improvement across a number of metrics, including accuracy by up to 31\% with the addition of gameplay context for the target message.

---


### 88. [KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](https://arxiv.org/abs/2610.27417)

**<font color=#1a73e8>作者：</font>** Zhikang Chen, Yueqing Sun, Sen Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPHarness, a framework that adapts the external execution harness of a frozen vision-language-action model through knowledge-probing co-evolution. Recovery knowledge supplies context-specific intervention hypotheses that guide active probing; probe outcomes reveal when these hypotheses apply and provide evidence for refining both recovery knowledge and later probe selection. This reciprocal process allows the harness to improve not only which interventions it applies, but also how it investigates failures. KPHarness separates fast policy execution from a slow research loop that translates accumulated knowledge and probing evidence into bounded harness revisions. Each revision is compared with the incumbent under matched sandbox conditions and accepted only when the paired evaluation shows improvement. Recoveries supported by further validation are retained for cross-task reuse, while immediate interaction feedback and delayed episode-success credit update action- and knowledge-probing policies during adaptation. Experiments on Minecraft tasks spanning mining, combat, and crafting show improved task coverage over bare policy execution, a manually specified fixed harness, and knowledge-only harness evolution with non-adaptive probing. Evaluation on previously unseen tasks further shows improved task completion with the evolved harness, knowledge bank, and probing policies held fixed,

---


### 89. [The Router Already Knows](https://arxiv.org/abs/2610.27421)

**<font color=#1a73e8>作者：</font>** Andrew Bistras, Marty Johnson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models already make a sparse choice for every token: which experts should process it. We ask whether a sparse dictionary should reuse that choice. NR-SAE gives each routed expert a small dictionary and opens only those the frozen router selects. At block 15 of Gemma 4 26B-A4B, after ten million C4 training tokens and across three seeds, the expert-aligned autoencoder explains 0.518 of the variance in router-weighted expert outputs on a fixed evaluation capture. A rank-addressed control with the same parameters but sixteen times as many candidates reaches 0.481, a candidate-matched control 0.458, and an architecture-matched control with randomized expert identity 0.387. A transcoder variant also leads all three controls: 0.432, against 0.347, 0.371, and 0.118. Part of this advantage is architectural: each expert writes into a subspace of at most a quarter of the model width, so naming the expert names the subspace. How much it explains, we have not measured. At this layer and budget, the router already knows something a dictionary would otherwise have to learn. Our implementation did not train faster, and semantic interpretability, downstream loss, and causal faithfulness remain untested.

---


### 90. [Harness Self-Evolution for Long-Horizon Terminal Agents](https://arxiv.org/abs/2610.27435)

**<font color=#1a73e8>作者：</font>** Ruhan Wang, Yucheng Shi, Zongxia Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harnesses with model weights fixed. It focuses on flipping tasks with both successful and failed runs under the same configuration, using successful runs as references for failure analysis. RiseHarness combines agent trajectories with internal harness traces from a runtime monitor to examine how model actions interact with command execution, feedback, context management, and completion decisions. A Harness Handbook links this evidence to harness behaviors and source code, helping identify recurring problems in mechanisms shared across tasks. RiseHarness then searches other harness frameworks for relevant implementations and adapts them as design references to the current model and execution protocol. Candidate changes undergo behavioral checks and repeated task evaluation; versions with measured gains seed the next iteration. This loop integrates suitable mechanisms from different frameworks into a single harness and uses new execution evidence to guide further changes. We evaluate task success and reliability across models, ablate harness execution evidence and external research, and test transfer to unseen benchmarks with the same model. RiseHarness treats a specific model as the unit of harness adaptation, studying how changes to shared interaction mechanisms can make existing capabilities more reliable across tasks.

---


### 91. [MLIPS: Multi-Layer Indexer Pool Sharing](https://arxiv.org/abs/2610.27438)

**<font color=#1a73e8>作者：</font>** Samkit Jain, Sai Kishan Pampana, Shlok Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention limits the keys used by each query, but finding those keys can still require a full-prefix scan at every layer. We introduce \textbf{MLIPS (Multi-Layer Indexer Pool Sharing)}, a training-free method that shares candidate search while retaining each consumer's own scoring and selection. A producer publishes a top-$M$ pool larger than the attention budget $K$; subsequent layers select their own top-$K$ from that pool. Measurements across three sparse-attention model families show substantially higher coverage from broad pools than overlap between final selections. We implement layerwise sharing, persistent decode reuse, and a coarse producer in vLLM for DeepSeek-V4-Flash. Across four long-context suites, three consumer layers per producer give $1.14$--$1.40\times$ speedups and $14.8$--$27.4\%$ lower GPU energy, with observed accuracy changes of $-1.49$ to $+0.29$ percentage points in single runs. More extensive sharing exposes task-dependent quality losses. Sampled prefill traces also reveal recurring selected KV positions across query groups and layers. We characterize this shared working-set structure and use it to motivate Top-$G$, an exploratory bounded pool construction for prefill. Its deployment, task accuracy, and serving benefits remain open.

---


### 92. [Scaling Graph Reasoning in Language Models with Learnable Graph Positional Encodings](https://arxiv.org/abs/2610.27439)

**<font color=#1a73e8>作者：</font>** Javier Porras-Valenzuela, Arush Arora, Alejandro Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving reasoning tasks supported on graphs typically requires providing a Language Reasoning Model (LRM) with a serialized description of the graph. This approach results in the input length growing with the number of edges, which limits the size of the problems that can be solved. Furthermore, even when graphs fit in context, performance sharply decays as the graphs grow. We propose to address this by augmenting LRMs with scalable and permutation equivariant graph positional encodings that modulate attention logits. An additional post-fusion-style module incorporates structural information into hidden states. We compute these positional encodings using a GNN followed by a Graph Transformer. This eliminates the need for serialized adjacencies, reducing the context burden to $O(N)$. We jointly fine-tune the positional encoder and the LRM LoRA adapters using optimal solutions generated by graph-theoretic solvers, resulting in a computationally efficient method. Trained on small graphs, the model exhibits improved size-generalization across graph-theoretic tasks on graphs with up to 1,000 nodes, and produces fewer tokens than a conventional LRM. Additionally, we observe that our model remains robust to node relabelings. Evaluations on graph-theoretic benchmarks also show that performance on small graphs is preserved.

---


### 93. [Decision Sufficiency of Learned Representation Interfaces for Safe Generative Control](https://arxiv.org/abs/2610.27446)

**<font color=#1a73e8>作者：</font>** Jipeng Li, Yanning Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A controller can guide a language model toward safe and useful responses by choosing when to assist, ask for clarification, or refuse. When the controller uses selected internal features, poor performance alone cannot distinguish missing information from limitations of its decision rules or training. We study decision sufficiency: whether the best controller using a representation can match the minimum average loss attainable with full state information, under the same strategies and evaluation criteria. For interfaces with finitely many outputs, we compute the optimal loss exactly and separate the three sources of excess loss. Pairwise checks can miss information loss: states with the same controller input may share an optimal strategy in every pair but not across the whole group. We bound the number of states needed to reveal a conflict and characterize the fewest outputs an unrestricted interface needs to avoid all conflicts. We audit selected features from sparse autoencoders, which encode model activations using relatively few active features, in Qwen2.5, SmolLM2, and Phi. On SmolLM2 responses scored by two human raters, restricting the controller to two selected on/off features increases its minimum average loss by 0.0345--0.1166 relative to full state information, even with the governing policy supplied. Both independently trained autoencoders show the increase on both evaluation sets. The audit identifies decision failures that require changing the controller's input, not merely its architecture or training.

---


### 94. [Bias and Reliability in Learning-Style Inference from Student--AI Dialogues: An Evaluation of GPT-4o and Gemini 2.0 Flash](https://arxiv.org/abs/2610.27448)

**<font color=#1a73e8>作者：</font>** Samaneh Zamanifard, Sajad Goudarzi, Andrew Robb  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into educational technologies for personalized support, creating opportunities for real-time learner modeling from dialogue. This study evaluates whether GPT-4o and Gemini 2.0 Flash can infer three Felder-Silverman Learning Style Model dimensions (Active-Reflective, Sensing-Intuitive, and Sequential-Global) from short, task-focused student-AI problem-solving dialogues. Using questionnaire-derived Index of Learning Styles labels from 153 undergraduate participants, we compared deterministic zero-shot and few-shot prompting under five-fold cross-validation. Although accuracy and support-weighted F1 were moderate for Sensing-Intuitive and Sequential-Global, majority-class baselines, macro-F1, balanced accuracy, and per-class recall showed that performance was often driven by dominant-label prediction rather than reliable recognition of both classes. The models substantially under-identified Intuitive and Global learners; few-shot prompting produced mixed effects and sometimes amplified majority-class bias. Active-Reflective classification remained unstable across models. These findings indicate that LLM-generated learner-style labels should be treated as uncertain, bias-prone signals rather than stable learner profiles, and that dialogue-based personalization systems require bias-aware evaluation and uncertainty-sensitive design.

---


### 95. [Ask to Distill: Learning to Synthesize Data for On-Policy Distillation](https://arxiv.org/abs/2610.27450)

**<font color=#1a73e8>作者：</font>** Jiashuo Sun, Hao Zhang, Xueqiang Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) can succeed with surprisingly few training questions, motivating a view of questions as carriers of distributional knowledge transfer. How can we assess whether a newly generated question is valuable for distillation, and learn to generate better questions---without access to its correct answer? We introduce Ask-to-Distill (\method), a framework that treats synthetic questions as distribution elicitors and optimizes the teacher supervision they expose along student-generated trajectories. A student-initialized synthesizer is optimized using a distributional surrogate for question value, computed from a frozen student--teacher pair without reference answers, correctness rewards, or per-candidate student updates. The reward combines teacher--student disagreement with teacher probability mass on the student's candidate support, together with length and diversity controls. The generated questions are filtered and deduplicated into a prompt-only bank for standard OPD. Across mathematical reasoning, code generation, and agentic tasks, our method improves average performance and teacher-gap recovery over unoptimized student-generated prompts and KL-filtered real questions, while matching or exceeding real-bank OPD in the evaluated settings. Signal analyses further show that optimized questions can elicit denser supervision and more total signal from shorter student responses, supporting elicited distributional supervision as an objective for synthetic distillation data. Our code, data and models are publicly available at this https URL.

---


### 96. [Detecting Errors in Large Language Model Responses: The Incremental Predictive Value of Hidden States](https://arxiv.org/abs/2610.27455)

**<font color=#1a73e8>作者：</font>** Ningzhi Li, Xiaojun Ma, Xiaofei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models support a wide range of tasks, hallucinations remain a major obstacle to user trust. When a model generates an answer, both its internal processing and final output vary with the question. Internal states are often expected to offer richer signals for hallucination detection. However, studies using these states typically report their standalone discrimination performance, while output-side comparisons often use simple baselines with weaker modeling capacity. We integrate output-side information available at inference time into a combined baseline and compare detection performance before and after adding hidden states under identical data splits and evaluation rules. Experiments cover open-ended generation and constrained multiple-choice tasks across different models. Adding hidden states improves AUROC by approximately 0.004 and 0.039 on the two tasks, respectively. Hidden states thus provide additional predictive information, but strong standalone detection performance can still yield only limited additional gains.

---


### 97. [Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement](https://arxiv.org/abs/2610.27465)

**<font color=#1a73e8>作者：</font>** De Wang, Peng Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent platforms are starting to improve their own agents: they read a deployed agent's execution traces, derive a change, have an automated verifier approve it, and release it with no human author. How much of this loop can safely run without a human? We propose two quantities a platform can measure. Verifier strength $\sigma$ is how well the available verifier -- often an LLM judge -- agrees with a trusted reference verifier; it limits how much a step can improve the agent. Recoverability is how cheaply a bad change can be undone: whether undoing it needs a new verifier approval, and how much of the old behavior a rollback restores. A step should run unattended only if both are adequate. On our platform this rule allows prompt, tool and skill edits to run unattended and keeps weight updates under human sign-off.
Our main contribution is these two definitions and how to measure them. We built a platform that applies the rule and tested it in two ways: on the platform's own approval gate, and in controlled experiments on the $\tau^2$-bench agent benchmark. On verifier strength, the platform's LLM judge sometimes gave the same score no matter what it was shown (9 of 37 settings) and reported no error, so a verifier can look healthy while approving anything; its strength must be measured, and two simple tests catch the failure. On recoverability, restoring a saved copy brought the agent back to its original behavior, but a regenerated undo did not, so only changes whose old version is kept can be reversed without a human; and while a change was deployed, it altered the outcome of 17 percent of tasks beyond normal run-to-run variation, which no undo repairs. Together these support the rule: a change can run unattended only when its old version is kept and its verifier's strength has been measured.

---


### 98. [Projected Distillation: On Learning to Solve Hard Problems from Close, Correct Targets](https://arxiv.org/abs/2610.27467)

**<font color=#1a73e8>作者：</font>** Shripad V. Deshmukh, Christian Bock, Kangrui Ruan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy learning is central to post-training: training on a model's own generations limits distribution shift and helps preserve existing capabilities. On hard problems, however, on-policy RL provides no reward-based learning signal when all attempts fail. On-policy distillation provides next-token supervision from a teacher, but on hard problems, if a rollout goes wrong early, subsequent supervision is conditioned on prefixes that already contain the mistake. Correct behavior can instead come from a gold or teacher solution, but such off-policy targets can differ substantially from the model's generations and, as we show, may erode existing capabilities. We therefore treat on-policyness as a continuum and propose projected distillation, which minimally edits the student's failed attempts into correct targets. The method uses contrastive updates to favor corrections over failed attempts and refreshes these corrections as the student evolves, enabling near-on-policy learning even when all student attempts fail. Theoretically, we prove that the student's learning regret grows with the edit size: it scales linearly with the horizon under minimal correction, as in DAgger, and quadratically under full-answer replacement, as in behavior cloning. Empirically, across two students (Qwen3-8B and OLMo-2-7B) and five domains spanning math, code, science, and tool use, projected distillation gives the highest area under the specialization-retention frontier (best on 8 of 9 cells against GRPO and OPD, and 7 of 9 against SPOT and SODA). Our ablations highlight the importance of online corrections, the contrastive loss, and on-policyness: moving targets farther off-policy steadily worsens the specialization-retention trade-off, with retention falling from 0.916 to 0.744 when minimal corrections are replaced by student-agnostic gold solutions.

---


### 99. [Training-Free Continual Learning for Multimodal Forecasting via Prompt Evolution](https://arxiv.org/abs/2610.27468)

**<font color=#1a73e8>作者：</font>** Laurent Mombaerts, Jonathan Taws, Jacopo Gargano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting a forecasting system to a changing world classically means retraining. We ask whether the task of continually learning regimes for time series forecasting can be represented by a piece of text: a guidance block, evolved by outcome-driven reflection and used in a frozen LLM forecaster's prompt. On a refreshed multimodal benchmark (weekly search indices, daily currencies, daily commodities, each window paired with web-retrieved news), we run GEPA-style prompt evolution under strict contamination control to prevent the data leakage common in timeseries benchmarks: the forecaster's knowledge cutoff predates every evaluated window. A 900-word evolved guidance carried by Llama-3.3-70B beats TimeSeries Foundation Models (TSFMs) on held-out data (GM MASE 0.776 vs. 0.898 for TabPFN-TS-3), transfers to more recent models without measurable loss, and costs dollars rather than GPU-days to update. We characterize the loop: out-of-loop gains concentrate in the first reflection, in-loop improvements overstate out-of-loop gains 2-3x unless an untouched monitor arbitrates, and error-only objectives silently suppress the text modality. We provide two extensions. First, compiling the guidance into executable code with a TSFM as a callable tool recovers most of the gain deterministically. Second, ablations show the advantage widens at short horizons and that removing the news text does not hurt the guided forecaster, consistent with the text's value being distilled into policy during learning. We argue that continual prompt evolution is a practical, training-free alternative to retraining for multimodal forecasting.

---


### 100. [Beyond the Prompt: Recovering Hidden Concepts in Text-to-Image Models](https://arxiv.org/abs/2610.27473)

**<font color=#1a73e8>作者：</font>** Zhengfeng Zheng, Minghong Fang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image models can generate visual concepts that their prompts never mention, and recent work shows that such associations can be implanted so that ordinary prompts trigger them. Auditing this behavior requires recovering the description that a prompt omits. Existing prompt optimizers are not well suited to this task. Gradient-based methods require backward access to the scoring encoder. Discrete evolutionary search treats semantically unrelated tokens as equally close. Language-model-guided search requires one inference call per candidate, which limits exploration. This paper presents EmbGA, an embedding-space genetic algorithm that recovers concepts present in a set of images but absent from the prompt that generated them. EmbGA keeps the population structure of genetic search but applies its operators in the token embedding space. Crossover interpolates between parent embeddings, and mutation moves an embedding toward a randomly drawn vocabulary embedding. Each offspring is then projected back to discrete tokens before scoring, so every evaluated candidate is a valid token sequence. We evaluate EmbGA on two benchmarks against six optimizers under two exploration budgets. EmbGA achieves the highest alignment when the exploration budget is large, recovers the most grounded tokens on natural images, and runs much faster than language-model-guided search.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
