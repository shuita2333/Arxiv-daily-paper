# 🧠 大模型相关研究 | 2026年08月13日

> 本类共 **184** 篇论文：已确认 **177** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-184](./part-04.md)

---

### 1. [LLM Agents Factory: Retrieval of Domain-Specific LLM Agents](https://arxiv.org/abs/2608.09934)

**<font color=#1a73e8>作者：</font>** Vitalii Belov, Artyom Sosedka, Andrey Sakhovskiy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents improve task performance by decomposing problems into role-specialized behaviors. However, their practical deployment is often limited by the computational cost and instability associated with the on-the-fly agent design for each user request. To address this, we present LLM Agents Factory, a retrieval-based framework that constructs domain-specific and Wikipedia-grounded agents on demand using a base of over 20K predetermined agent profiles. Our framework supports two modes: (1) agent profile retrieval via semantic search and (2) distillation into a compact model fine-tuned for direct agent generation. Experiments on MMLU, BIG-bench, and BIG-bench Hard in a single-agent scenario demonstrate that our retrieval-based agent construction surpasses non-agent baselines in accuracy while matching AutoGen generation quality with a 120B backbone at a substantially lower inference cost. Our work reveals that retrieval from a structured agent repository provides a cost-efficient, accurate, and controllable alternative to dynamic agent generation, responding to the strict demands of industrial applications. We provide the implementation code and the agent base in this https URL.

---


### 2. [Conflict or Strategy? Asymmetric Role Framing of La France insoumise and Rassemblement National in French News Headlines, 2022-2025](https://arxiv.org/abs/2608.09936)

**<font color=#1a73e8>作者：</font>** Amr Sobhy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do French news headlines frame left- and right-populist challengers as symmetric ``extremes,'' or as fundamentally different political adversaries? We examine 28,592 headlines about La France insoumise (LFI) and Rassemblement National (RN) published by 25 French-language outlets between 2022 and 2025, annotated through a three-model LLM pipeline validated against a stratified human audit. The clearest finding is role asymmetry rather than valence asymmetry: conflict framing and strategic-game framing are more robust across models and time than delegitimization, with AGGRESSOR serving as corroborating role syntax. LFI appears in headlines more often through a conflict register and RN through a strategic-electoral register. This role gap is direction-stable across all three annotation models, survives bootstrapping and permutation tests, and persists across outlet families and most of 2022-2025. A secondary moral-accounting layer (who is blamed, legitimized, or cast as a victim) is structured by outlet rather than party, producing aggregate nulls that conceal some of the corpus's most polarized patterns. Methodologically, the annotation pipeline reveals a two-tier reliability profile: conflict and strategic-game framing achieve the strongest human validation and cross-model stability; actor role is direction-stable but treated as corroborating because its audit reliability is lower; normative-judgment constructs (legitimacy, blame) are weaker. The paper contributes political-role assignment as a target for computational framing research that decomposes what valence-based measures conflate, and establishes a construct-stratified reliability framework for calibrating majority-vote LLM annotation pipelines in political text tasks.

---


### 3. [Carefully Considering Culture: Analyzing LLM Alignment in Single- and Multi-Cultural Settings using Cultural Consensus Theory](https://arxiv.org/abs/2608.09937)

**<font color=#1a73e8>作者：</font>** Krishna Pothugunta, John P. Lalor  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work in NLP has probed large language models for their understanding of cultural norms across countries. However, this work typically considers distributional patterns, ignoring group consensus or possible multicultural environments within a country. In this work, we leverage cultural consensus theory (CCT) from cultural anthropology to model such multidimensional nuance. Applying CCT to the World Values Survey (WVS) across 10 countries and 12 domains, we demonstrate that models frequently misrepresent cultural structures by either failing to form cohesive consensus or severely over-regularizing consensus. Through explicit representation of intra-group variance, CCT provides actionable diagnostics to evaluate when models reflect true human diversity versus algorithmic homogenization.

---


### 4. [How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with Goal-Directed NPC Simulation](https://arxiv.org/abs/2608.09939)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Production teams deploying LLM chat agents face a specific quality assurance gap: existing evaluation tools test individual responses or simulate social interactions, but none systematically verify whether real users can achieve their goals through multi-turn conversation. We introduce a three-layer dogfooding framework that bridges this gap by combining canonical question-bank testing (Layer 1), random-walk multi-turn evaluation (Layer 2), and a goal-directed NPC (Non-Player Character) simulator with five structured goal types and a ten-category failure taxonomy (Layer 3). In a longitudinal case study on a production multi-agent system over roughly three months (257 evaluation runs; a 108-scenario NPC suite), we find that the three layers produce complementary regression signals: cross-layer correlation for response quality is weak within a synchronized run (Spearman rho between -0.15 and 0.14) and negative across the longitudinal series (rho down to -0.46), confirming that canonical correctness does not predict goal-directed conversation success. The NPC simulator achieves 77 percent goal achievement at 0.17 dollars per run (6,272x cheaper than human evaluation), enabling daily CI/CD integration with automated PROMOTE/HOLD/ROLLBACK release decisions. We release full prompt templates, the failure taxonomy, and a Python-first replicability guide so that other teams can adopt the framework for their own LLM chat agents.

---


### 5. [The Multilingual Quantization Tax: Structural Collapse and Typological Fragility in Edge SLMs](https://arxiv.org/abs/2608.09941)

**<font color=#1a73e8>作者：</font>** Mohammad Wathiq Soualhi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While 4-bit weight quantization is critical for deploying Small Language Models (SLMs) on edge devices, evaluations of the resulting performance degradation-the quantization tax-remain overwhelmingly English-centric. We present a zero-shot multilingual evaluation of 4-bit quantization across the Gemma 4 and Qwen 3.5 architectures. Evaluating on eight typo-logically diverse languages using MMLU ProX Lite and GlobalPIQA, we show parameter truncation exposes deep pre-training inequalities. We identify four phenomena: (1) Typological Fragility: low-resource and specific non-Latin scripts suffer representational collapse via architecture-specific double dissociations, failing to generate valid task logits; (2) Home Language Fragility Paradox: foundational pre-training pathways provide limited precision loss protection; (3) Domain-Specific Forgetting: multi-step cross-lingual routing degrades while associative soft-science recall remains robust; and (4) Quantization Resistance: highly saturated, typologically aligned domains resist deterministic degradation, with post-quantization performance gains bounded by statistical noise.

---


### 6. [When Chain-of-Thought Helps and When It Hurts: An Empirical Investigation of the Serial-Depth Bottleneck in LLM Reasoning](https://arxiv.org/abs/2608.09942)

**<font color=#1a73e8>作者：</font>** Tughanbulut Kurtulush  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is widely assumed that chain-of-thought (CoT) prompting universally improves LLM reasoning. We investigate this through the conceptual framework of the H_dp bandwidth bound (Chen et al., 2024): although the formal bound binds only asymptotically (at astronomically large prompt lengths), it identifies a real architectural bottleneck -- serial computation exceeding a transformer's single-pass capacity must be externalised, which is what CoT does. Our central finding is a within-benchmark serial-depth gradient: single-pass (no-CoT) accuracy degrades monotonically with per-item serial depth, while CoT is approximately depth-invariant. We measure CoT effects across three instruction-tuned models (Qwen-2.5-7B/32B, Llama-3.1-8B) and five standard NLP benchmarks at practical context lengths. On high-depth P-complete tasks (GSM8K, MATH), CoT gives a +54 to +68 pp recovery gap across all models. On shallow TC^0 tasks (MMLU, ARC), CoT is structurally redundant (Delta in [0.0, +4.6] pp, no significant negative effect) -- though high no-CoT baselines (up to 95% on ARC) may reflect contamination, so this null is not a clean architectural test. The intermediate class L (HumanEval) shows a model-size-dependent transition: +23.2 pp (32B), +9.1 pp (8B), -28.7 pp (7B). The cross-benchmark depth-recovery correlation is Spearman rho = 0.661 (p = 0.007, n = 15); 9 of 15 benchmark-level McNemar tests are significant after Bonferroni correction. Pre-registered on OSF, our results indicate that CoT is not a universal reasoning enhancer but acts as a bandwidth bypass: it helps serial computation that strains single-pass capacity and is redundant for tasks that already fit.

---


### 7. [Navigation Alone Is Not Enough: Evaluating Explanatory Assistive UI Agents](https://arxiv.org/abs/2608.09944)

**<font color=#1a73e8>作者：</font>** Santosh Patapati  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern web interfaces are increasingly difficult to use with screen readers, particularly when pages update dynamically or hide important structure behind visual layout. Recent UI agents can act on such interfaces; however, for assistive agents to be truly useful, they must behave as collaborators that keep users informed and in control, rather than as tools that simply take actions on users' behalf. Most existing benchmarks judge systems primarily by task completion, without assessing how well they explain their actions or support user oversight. We introduce NeXUI, a benchmark for assistive agents that must navigate interfaces while explaining each step in clear language for nonvisual use. NeXUI pairs realistic user goals with instrumented interface states, enabling agents to reason from both visual context and structural information. Its evaluation measures safety, efficiency, and task success, while also checking whether explanations are grounded in the interface state. In our experiments, we find that NeXUI remains challenging even for state-of-the-art foundation models, with % Gemini-3.5-Flash achieving only a 44\% success rate and poor explanation scores, making it a useful foundation for future research and development. By focusing on navigation, explanation, and user control, NeXUI provides a clearer way to study agents that can support blind and visually impaired users in modern computing environments.

---


### 8. [HoosierHelp: Benchmarking LLM Agents for Social Service Navigation](https://arxiv.org/abs/2608.09946)

**<font color=#1a73e8>作者：</font>** Yiyang Li, Weixiang Sun, Tianyi Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social service navigation requires connecting help-seeking individuals to resources that satisfy their needs and specific constraints. Although LLM agents offer a promising interface for conversational resource navigation, existing benchmarks do not capture the interaction complexity and constraint-grounding demands of this setting. We introduce HoosierHelp, an interactive benchmark grounded in 3,971 Indiana public social service resources. Agents interact with simulated users, issue structured resource-search calls, handle non-ideal interactions, and select the final resources returned by the tool. HoosierHelp enhances the realism of simulated users by varying their need structure, constraint satisfiability, and behavior patterns, including impatience, rambling, unsupported requests, and self-contradiction. Experiments on 240 samples across seven LLMs show that current LLM agents remain substantially unreliable for social service navigation. Performance drops sharply on fallback-required and self-contradictory conversations, highlighting the need for agents that are more robust to complex and non-ideal user interactions.

---


### 9. [Closed-Loop LLM Co-Pilots for Digital Agriculture](https://arxiv.org/abs/2608.09949)

**<font color=#1a73e8>作者：</font>** Serge Kernbach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study evaluates the application of Large Language Models (LLMs) in complex biological systems, evolving from data analysis to autonomous, AI-guided experimentation. The framework is driven by data from a 49-channel phytosensor network, encompassing multispectral, electrochemical, and dielectric modalities. To enhance accessibility, the system provides real-time natural-language interpretation for both specialists and non-experts. However, its core advantage lies in the transition from human-in-the-loop analysis to autonomous control. Processing biophysical data, the LLM evaluates plant physiology and triggers hardware actuators to optimize microclimates, execute phenotyping protocols, or induce controlled stress scenarios. This closed-loop architecture establishes a direct AI-biology interface, enabling data-driven exploration of complex biosystems and ecologies. The framework was validated across three case studies, based on a vertical farm and a single-plant setup and deciphered complex micro- and macro-fluctuations in plant physiology. Agents in a production-scale deployment executed multi-parameter optimization, balancing biomass accumulation, chlorophyll content, and energy consumption. The LLM processed biosensing telemetry to modulate full-spectrum, 450 nm, and 660 nm lighting at 2-hour intervals. Compared to periodic control, the system in minimal-time mode reduced the production cycle by 35%. In the energy-optimization mode, it reduced energy consumption by 18% with only a marginal increase in cultivation time, exploiting physiological inertia via light pulses. Finally, the agents autonomously developed an unforeseen strategy of dark-induced chlorophyll accumulation, resulting in a 67.9% energy saving. This framework transforms LLMs into autonomous co-pilots for digital agriculture, improving the cost-to-value ratio and lowering computational and expert-labor constraints.

---


### 10. [CurveFP: Rational-Radix Logarithmic Datatypes with Closed Products for Language Models](https://arxiv.org/abs/2608.10010)

**<font color=#1a73e8>作者：</font>** Ye Qiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision datatypes reduce language-model cost, but most formats optimize scalar fidelity while leaving the arithmetic induced by their products unchanged. We introduce CurveFP, a closed-product codebook family that distributes quantized magnitudes across interleaved logarithmic curves under compact block scales. A rational radix tunes dynamic range against local resolution, while uniform curve indices make every nonzero product algebraically closed. Product formation becomes an exact sign XOR and integer-index update, and a derived finite phase count determines the accumulation schedule. We instantiate this algebra as CurveFP eight E4C3/E5C2 for training and CurveFP seven E3C3 for compact deployment. In evaluation, CurveFP seven beats tensor-wise FP8 perplexity on four 7B--9B models with one fewer element bit and stays within 1.32\% of native quality. CurveFP eight lowers operand NMSE in all 36 paired forward and backward GEMM comparisons. Across three matched 128.3M-parameter triplets, every mode completes 3B-token pretraining per seed; CurveFP eight reaches mean BF16-inference perplexity 22.5366 versus 22.5407 for FP8 and incurs a lower format-induced penalty in all three seeds. A 36-cell downstream matrix finds lower WikiText-103 perplexity for the CurveFP eight-trained checkpoints in all 12 seed-format comparisons, with mixed PG-19 and task deltas. Together, these results establish CurveFP as an arithmetic co-design that combines FP8-class numerical behavior, seven-bit inference, and a substantially simpler product path.

---


### 11. [Position Encoding in Transformers: From Absolute and Relative Methods to Rotary Position Embeddings and Long-Context Scaling](https://arxiv.org/abs/2608.10021)

**<font color=#1a73e8>作者：</font>** Jiguo Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-attention models content-dependent interactions between tokens but does not by itself encode token order. Position encoding addresses this limitation by introducing absolute coordinates, relative distances, or position-dependent rotations into Transformer representations and attention scores. This technical survey develops a unified account of sinusoidal and learned absolute position embeddings, Shaw-style relative position representations, Transformer-XL, T5 relative position bias, ALiBi, and Rotary Position Embeddings (RoPE). We derive how RoPE converts absolute position indices into relative phase differences in Query-Key inner products and compare these methods in terms of where position is injected, computational cost, compatibility with KV caching, and length extrapolation. We then examine long-context extensions, including Position Interpolation, RoPE scaling laws, NTK-aware scaling, Dynamic NTK, NTK-by-parts, YaRN, LongRoPE, and LongRoPE2, with emphasis on frequency allocation, attention rescaling, training length, and target context length. We also summarize implementation considerations, evaluation protocols, and position-encoding choices in representative large language models. A central conclusion is that the ability to compute positional features beyond the training length does not imply reliable long-context generalization; context extension must be evaluated through short-context retention, position-wise perplexity, retrieval, reasoning, and long-context code tasks.

---


### 12. [DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents](https://arxiv.org/abs/2608.10037)

**<font color=#1a73e8>作者：</font>** You Lu, Kun Zhang, Bihuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly rely on external tools to accomplish complex real-world tasks, making tool documentation a critical grounding resource for LLM agents. Existing studies mainly focus on improving the tool-use capabilities of LLM agents, while largely treating tool documentation as a fixed input. Although several recent works attempt to optimize tool documentation through rewriting or compression, little is known about how the information contained in tool documentation affects agent performance across different settings.
To bridge this gap, we conduct a large-scale empirical study on tool documentation for LLM agents. Our study reveals substantial heterogeneity in the information fields provided by existing tool documentation. Moreover, the effectiveness of different information fields is highly dependent on the task domain, LLM backbone, and agent paradigm, indicating that no fixed tool documentation can consistently generalize across diverse agent settings.
Motivated by these findings, we propose DocsChisel, an adaptive tool documentation optimization framework for LLM agents. DocsChisel analyzes failed execution traces of a target LLM agent to identify documentation-related issues, and iteratively optimizes tool documentation by adding, removing, and refining information fields for each tool. We evaluate DocsChisel against two state-of-the-art baselines, i.e., EasyTool and DRAFT. Experimental results show that DocsChisel improves the task success rate of LLM agents by 95.89% over the original tool documentation and by 75.15%, on average, over existing baselines, while incurring limited optimization time and token overhead

---


### 13. [FlowScout: From Execution Feedback to Reliable Tool-Using Agent Workflows](https://arxiv.org/abs/2608.10039)

**<font color=#1a73e8>作者：</font>** Shuo Hao, You Lu, Bihuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic workflows have become an important abstraction for building reliable LLM-based automation systems by organizing large language models (LLMs), tools, and control logic into explicit execution structures. However, constructing high-quality agentic workflows remains largely manual and requires substantial domain expertise. Recent studies have explored automatic agentic workflow generation from historical task-solving records, but they mainly produce LLM-centric workflows, where real tool executions are abstracted and simulated by LLM nodes, limiting the usability and stability of generated workflows. To address these limitations, we propose FlowScout, an execution-guided framework for generating tool-integrated agentic workflows from historical task-solving records. Specifically, FlowScout represents an agentic workflow as a directed graph composed of LLM nodes, tool-calling nodes, and dependency edges. It first mines a common tool coordination skeleton from historical records to construct an initial workflow, and then refines the workflow topology through Monte Carlo tree search guided by execution feedback. We evaluate FlowScout on four representative task domains and compare it with three baselines, i.e., PM4Py, ReAct and AFlow. Experimental results show that agentic workflows generated by FlowScout improve tool invocation correctness by at least 92.69% and execution quality by at least 17.66% over the baselines, while achieving lower performance variation across repeated runs.

---


### 14. [UserToolBench: A User-Profile-Hidden Benchmark for Personalized Decision Making in Tool-Use LLMs](https://arxiv.org/abs/2608.10042)

**<font color=#1a73e8>作者：</font>** Xuexiong Yin, Zechuan Chen, Yongsen Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-use LLMs are increasingly asked to act on users' behalf, but existing benchmarks usually focus on profile recall, style imitation, generic tool use, or response-level personalization. We introduce UserToolBench , a benchmark for personalized decision making in tool-use LLMs. UserToolBench tests whether a model can infer latent user preferences from interaction history, recognize when clarification is needed, and produce user-aligned tool-call trajectories under incomplete information. The benchmark is built from privacy-sanitized real interaction traces and combines structured persona profiles, public API-style tool ecosystems, and long-horizon multi-turn trajectories. It includes 10 user profiles, 36 tool sets, 1,065 turns, 170 unique tools, and evaluation-focused task types covering lack-of-information, single-tool, and multi-tool settings. Experiments with strong tool-use LLMs show that current models still have difficulty with personalized delegation. Multi-tool coordination, missing-constraint inference, and long-horizon behavioral consistency remain major bottlenecks. These results suggest that personalization evaluation should move beyond asking whether outputs sound user-specific and instead ask whether LLMs make correct decisions for the users they represent.

---


### 15. [Finding the Signal in the Spam: Jointly Learning Rewards and Worker Reliability from Pairwise Comparisons](https://arxiv.org/abs/2608.10045)

**<font color=#1a73e8>作者：</font>** Kaustubh Shivshankar Shejole, Tanish Agarwal, Arpit Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of learning from pairwise comparisons has been widely studied across many domains such as recommendation systems, social choice, and more recently, fine-tuning large language models. In this problem, the goal is to learn item rewards based on pairwise comparisons between them. In many scenarios, these comparisons are elicited from crowdworkers using platforms such as Amazon Mechanical Turk, Scale AI, etc. However, crowdworkers are often unreliable due to limited domain knowledge or revenue-maximizing (spamming) behavior. In this work, our goal is to understand whether worker reliability (competency) can be learned jointly with item rewards. To this end, we adopt the Boltzmann-rational model for pairwise comparisons, which extends the Bradley-Terry-Luce model by incorporating worker competencies. We derive an EM-based algorithm for learning under this model by introducing Polya-Gamma latent variables to transform the logistic likelihood into a conditionally Gaussian form, enabling tractable optimization and leading to a simplified $Q$ function in the E-step of the algorithm. This technique allows us to reduce our formulation to a matrix sensing problem, using which we establish theoretical convergence guarantees for our algorithm. We conduct extensive experiments on real-world and synthetic datasets. These experiments demonstrate the advantages of using our algorithm over several baselines and confirm its strong robustness to both spammers and adversarial workers, highlighting its practical effectiveness in realistic crowdsourcing and reward learning settings. The code and data is publicly available at this https URL.

---


### 16. [Detecting Soft Skills in ML Engineering Roles CVs](https://arxiv.org/abs/2608.10046)

**<font color=#1a73e8>作者：</font>** Aidin Azamnouri, Nouran Ayad, Justus Bogner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft skills shape collaboration among ML engineers, data scientists, and software engineers building ML-enabled systems, yet what we know about them comes almost entirely from the demand side. Job advertisements, surveys, and hiring manager interviews capture what employers ask for. How candidates themselves articulate these competencies has not been studied, and existing CV-mining work is both keyword-based, so it cannot see skills conveyed through narrative, and descriptive, reporting frequency rankings without testing whether group differences exceed sampling variation. We close both gaps. Using a balanced corpus of 300 curated CVs spanning the three roles, we extract explicitly listed and implicitly narrated soft skills with an LLM-based pipeline validated against a human-annotated ground truth, a distinction that existing extractors were not designed to make. We then convert the demand-side literature's claims into 13 falsifiable hypotheses about role signatures, seniority progression, and disclosure style, and test them with effect sizes under family-wise error control, so that candidate-side data can corroborate or contradict the demand-side account rather than merely illustrate it. Eleven hypotheses are supported, one partially, and one refuted. Candidates disclose soft skills through narrative rather than keyword lists by roughly three to one, and most so for the competencies employers value most: leadership, coordination, and mentoring (88-96% narrative). Seniority nearly triples the odds of articulating leadership. That competency, assumed universal in prior work, is articulated by software engineers at half the rate of their peers. Technical candidates do articulate soft skills, but a keyword-based screening systematically misses them.

---


### 17. [Observational Policy Ranking for SMB Financial Guidance from Multi-Action Accounting Logs](https://arxiv.org/abs/2608.10050)

**<font color=#1a73e8>作者：</font>** Shrutendra Harsola, Vignesh Subrahmaniam, Vikas Raturi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small and medium-sized businesses need timely financial guidance, yet historical accounting logs record self-selected and often co-occurring business changes rather than randomized recommendations. We formulate this setting as observational policy ranking: from pre-decision financial information, a policy selects one of 34 ledger-derived business-change categories for a target financial KPI. Using 85,078 company-month observations from 7,505 firms, we introduce Covariate-Adjusted Residual Policy Learning (CAR-PL), an action-wise R-learner that operates directly on multi-hot logs and regularizes selection by observational support. We compare CAR-PL with an uplift T-Learner, a conservative contextual value model, a zero-shot LLM, and non-personalized references on company-disjoint held-out firms under a shared model-assisted scoring rule. CAR-PL has the highest Gross Profit point estimate (0.084), the T-Learner has the highest Revenue point estimate (0.085), and the contextual value model has the highest Quick Ratio point estimate (0.062). CAR-PL and the T-Learner are not statistically separated on either growth KPI in matched company-clustered comparisons, while CAR-PL selects 33-34 categories and produces less concentrated selections across the catalog. Outcome-model-only scoring retains the same KPI-level point-estimate leader or top pair, and category rankings remain similar when the all-zero treatment reference is replaced by the most common training co-action pattern. These findings support objective-specific ranking of SMB financial guidance from multi-action accounting logs.

---


### 18. [LEGO: Leveled Language Gaussian Splatting](https://arxiv.org/abs/2608.10057)

**<font color=#1a73e8>作者：</font>** Yuning Peng, Haiping Wang, Yuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LEGO for advanced open-vocabulary scene understanding. Beyond basic concept recognition, its core innovation lies in capturing the intrinsic semantic hierarchies within the scene, such as the "flowerpot -> bouquet -> bud -> petal" lineage. While foundation models like SAM can identify multi-granular structures in 2D, their partitions are strictly perspective-bound and lack cross-view consensus. LEGO self-adaptively re-grades volatile multi-view SAM granularities into a unified, 3D-consistent hierarchy. This provides precise supervision for the structurally coherent, multi-level segmentation of 3D scenes. By grounding these segments with CLIP embeddings, LEGO recovers open-vocabulary semantic logic across hierarchical levels. Furthermore, by incorporating spatial relationships, we elevate these segments into level-wise language scene graphs, effectively empowering Large Language Models to perform complex, context-aware spatial reasoning and precise visual grounding. Experimental results demonstrate that LEGO establishes new state-of-the-art performance across both promptable and open-vocabulary 3D segmentation benchmarks, exhibiting advanced hierarchical scene decomposition and context-aware spatial reasoning.

---


### 19. [CHORUS: Complementary Experts for High-Coverage Testbench Stimulus Generation](https://arxiv.org/abs/2608.10090)

**<font color=#1a73e8>作者：</font>** Hejia Zhang, Sheng Lu, Zhongming Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have advanced code generation, where executable feedback provides a more reliable learning signal than textual imitation alone. Hardware verification is an important application of code generation and accounts for a substantial fraction of modern chip design effort, with high-coverage testbench stimulus generation as a key task. We present CHORUS, a post-training framework that pushes performance beyond what a conventional supervised fine-tuning (SFT)-to-reinforcement learning (RL) pipeline achieves. CHORUS builds on two observations. First, staged SFT produces behaviorally diverse checkpoints, and dense-reward RL turns them into strong experts with comparable aggregate performance but distinct task-level strengths. Second, these complementary strengths can be exploited through either training-free model merging or further post-training to outperform the best individual expert. By consolidating the resulting specialists into a single 4B model, CHORUS achieves 88.0% Pass@1 on CVDP-ECov, outperforming DeepSeek-R1 (671B) by 13.5 percentage points.

---


### 20. [MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory](https://arxiv.org/abs/2608.10108)

**<font color=#1a73e8>作者：</font>** Beidi Zhao, Yaoqi Chen, Yuru Feng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history. External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view. Existing multi-memory systems either read a fixed set of structures for every query, inflating context and introducing noise, or route each query to a single structure, preventing the composition of complementary evidence. A controlled analysis on AMA-Bench shows that the optimal memory configuration is typically neither a single structure nor the full union, but a tailored composition of multiple structural memories that varies with query and task demands. Motivated by these findings, we formulate structure-level dynamic selection: selecting and fusing a query-adaptive subset from a library of specialized memory structures. We propose MESA (a Multi-structure Evidence Selection framework for long-horizon Agent), which builds five complementary structure views of each trajectory and learns from end-to-end answer-level feedback to select and fuse a query-specific subset for a frozen answer model. To learn under this weak supervision, MESA employs harness optimization with prior-guided search and UCB-guided scheduling to balance exploration and exploitation. On AMA-Bench, MESA outperforms the strongest baseline by 8.5% while using 41% fewer evidence tokens than the all-structure alternative.

---


### 21. [PERCEPT: A Corpus for POS Tagging and Analysis of Persian-English Code-Mixing](https://arxiv.org/abs/2608.10109)

**<font color=#1a73e8>作者：</font>** Ghazal Kalhor, Zahra Jafari, Amirarsalan Shahbazi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media has become a major venue for multilingual communication, where users frequently mix multiple languages within a single utterance. Although code-mixed corpora have been developed for several language pairs, Persian-English code-mixing remains relatively underexplored. Existing Persian resources lack Universal Dependencies (UD) part-of-speech (POS) annotations for code-mixed words, limiting both linguistic analyses and the development of syntax-aware NLP models. To address this gap, we introduce PERCEPT, the first publicly available large-scale Persian-English code-mixed corpus annotated with Universal Dependencies POS tags for code-mixed words. The dataset comprises 6,800 posts collected from X, Instagram, and Digikala. We further present an LLM-assisted annotation framework that automatically assigns POS tags and document-level topics. Human evaluation demonstrates high agreement between the automatically generated annotations and gold annotations, confirming the reliability of the annotations. Using PERCEPT, we conduct the first comprehensive linguistic analysis of Persian-English code-mixing across multiple social media platforms. Our analyses reveal that nouns are the predominant category for code-mixed words, while the distributions of other POS categories vary across platforms. We further find that the positional distribution of code-mixed words is remarkably consistent across platforms, whereas the triggering effect is substantially more pronounced in Digikala. PERCEPT is publicly available at this https URL.

---


### 22. [Procedural Fairness Failures in RLHF from Preference Averaging](https://arxiv.org/abs/2608.10126)

**<font color=#1a73e8>作者：</font>** M P V S Gopinadh, Karthik Kamuju, Kummari Avinash 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) aggregates heterogeneous preferences into a single reward model, assuming preference homogeneity. When preferences are heterogeneous, this aggregation induces a procedural fairness failure where majority preference groups dominate reward learning while minority preferences are systematically under-represented. This work defines procedural fairness in alignment as preserving distinct preference signals during reward modeling and shows that standard RLHF violates this via preference averaging. Preference-Aware RLHF (PA-RLHF) is introduced, separating optimization across preference modes at the reward learning stage. In a controlled setting, PA-RLHF improves overall alignment accuracy from 46.9% to 67.9% and reduces the fairness gap between best and worst aligned groups from 15.9 to 9.6 percentage points. These results show that procedural fairness failures in alignment can arise from structural design choices in reward learning, even in controlled, noise-free settings, with direct implications for large language models and agentic systems, where biased reward models can compound inequities across sequential decisions.

---


### 23. [The Parser Already Knows: Lightweight Bias Correction in Constrained Decoding](https://arxiv.org/abs/2608.10137)

**<font color=#1a73e8>作者：</font>** Işıl Özgü, Yaoxuan Wu, Guy Van den Broeck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammar Constrained Decoding (GCD) forces Language Models (LMs) to produce syntactically valid outputs by masking out non-conforming tokens at each step. However, rigid masking distorts the model's underlying probability distribution, often biasing generation toward valid but suboptimal outputs. While online sampling restores this distribution, it requires computationally expensive iterative resampling. As a result, existing methods force a compromise between output quality and inference latency. Our key insight is that the internal parser and lexer states inherently maintained during incremental parsing already encode future grammatical validity -- exactly the information required to restore the LM's true distribution. We propose a lightweight, offline-trained logit correction conditioned on this syntactic and lexical state together with candidate next tokens. Because these states are already computed as a necessary part of incremental parsing for masking, extracting them adds negligible overhead while leaving the base LM's weights completely untouched. Across several grammars, this correction substantially closes the gap between the masked distribution and the LM's true distribution, consistently outperforming both masking and online sampling. Even its lightest variant, which relies on the candidate next token alone, still matches or exceeds both baselines: the next token itself carries an implicit lookahead, much like how parsers commonly use a lookahead token to resolve ambiguous decisions. By restoring the probability mass that masking removes, it reconciles the LM's probabilistic integrity with grammar conformance.

---


### 24. [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](https://arxiv.org/abs/2608.10149)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Chang Xu, Hui Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing to leverage LLM reasoning for interpretable weighting decisions. We propose REATS, which leverages LLM reasoning capabilities as an intelligent ensemble router that jointly processes textual temporal pattern descriptions and numerical features to produce interpretable, sample-adaptive ensemble weights through chain-of-thought reasoning. To enable effective LLM-based ensembling, we study its key design choices and propose: (i) a structured input pipeline that transforms raw time series into hybrid textual--numerical representations with fixed token cost, enabling rule-based chain-of-thought construction without API dependency, augmented with retrieved similar-sample priors; (ii) a diverse multi-row weight supervision scheme coupled with a token-efficient percentage-table format that reduces numerical complexity and mitigates LLM hallucinations; and (iii) a two-stage fine-tuning framework combining SFT with GRPO, where a reciprocal reward mapping transforms the continuous unbounded MSE gap into bounded signals with amplified near-oracle sensitivity, addressing the uniform sensitivity and outlier-dominated advantage compression inherent in naive reward designs for regression-based GRPO. Experiments on eight benchmarks demonstrate that REATS outperforms competitive ensemble baselines while providing natural language explanations and demonstrating strong transfer learning and out-of-domain generalization to unseen candidate models.

---


### 25. [Multimodal Item Parameter Estimation using Simulated Response Probabilitie](https://arxiv.org/abs/2608.10154)

**<font color=#1a73e8>作者：</font>** Christopher Ormerod, YoungKoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present results from reconstructing multiple-choice model (MCM) and three-parameter logistic (3PL) model curves using a fine-tuned multimodal large language model (LLM) based on Qwen3.5. The model is prompted and fine-tuned to replicate choice probabilities across a large training corpus of multiple-choice items containing both image and text stimuli, conditioned on a labeled set of student ability levels. By learning to reproduce the systematic error patterns of students across a discrete range of abilities, the LLM implicitly captures the underlying response probabilities encoded in the 3PL and MCM curves. This allows us to accurately approximate item difficulty on a held-out test set directly from the model's predicted option probabilities.

---


### 26. [SBCO: Self-Supervised, Verifier-Grounded Harness Optimization For Planning Agents](https://arxiv.org/abs/2608.10157)

**<font color=#1a73e8>作者：</font>** Vivek Kulkarni, Sudipta Paul, Aounon Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving agents seek to reduce the human engineering effort behind AI systems by enabling them to evolve and self-improve their performance over time. Recently, methods like the Darwin Gödel Machine and the Huxley Gödel Machine have been proposed which enable open-ended, recursive self-improvement through self-reference where a coding agent edits its own code. Such self-referential self-improvement methods require that the competence required to perform the task coincides or aligns well with the competence required for self-modification which is the case for coding tasks. For domains or tasks, which do not satisfy the alignment needed, self-referential self-improvement is not available. In such cases, it is possible to adapt the above algorithms to other tasks by removing the self-referential aspect or introducing explicit self-modification of a meta-agent -- both computationally expensive, relying on population or self-modification search over many candidate agents. For planning tasks with explicit constraints, we propose a far cheaper alternative. We introduce SBCO (Self-supervised Block Coordinate Optimizer), a verifier-grounded harness optimizer in the same closed-loop, improve-from-experience family as the Gödel-machine methods, but self-supervised rather than self-referential. Given an agentic harness, SBCO learns a decomposed bank of verifiers and a harness policy via approximate block coordinate ascent, improving the agent's outputs from its own graded feedback---with a fixed meta-agent and no human labels. Across two domains SBCO matches or exceeds a customized self-modifying baseline while using 4-5.5 times less compute budget.

---


### 27. [Generating Attacks for LLMs with GFlowNets](https://arxiv.org/abs/2608.10171)

**<font color=#1a73e8>作者：</font>** Berkay Ozcam, Irem Onen, Mehmet Fatih Amasyali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models (LLMs) has facilitated their ubiquitous integration into various domains, leading to widespread adoption. However, this escalating trend has introduced significant security vulnerabilities, necessitating the identification and mitigation of flaws arising from malicious exploitation. Red teaming assessments, conducted to evaluate model robustness through diverse adversarial inputs, are essential for exposing security risks and implementing countermeasures. Currently, red teaming is performed either manually by experts or automatically using predefined attack datasets. Nevertheless, manual testing remains time-consuming, while existing automated methods suffer from limited creativity due to their inherent dependency on fixed datasets. In this study, we propose an automated, human-independent, and adaptive approach leveraging GFlowNets to identify LLM vulnerabilities by utilizing one large language model to test another. Within this framework, an attacker model is trained against a specified victim model to perform automated red teaming and provide a quantitative robustness score. This research aims to generate more effective adversarial attacks in English compared to existing benchmarks and, as a novel contribution to the literature, introduces a model capable of generating attack inputs in the Turkish language.

---


### 28. [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](https://arxiv.org/abs/2608.10172)

**<font color=#1a73e8>作者：</font>** Ashim Dhor, Pin-Yu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability explains models by identifying circuits inside them, but has no way to tell whether a circuit is a property of the model or an artifact of the method that found it. Sparse autoencoders illustrate the problem: different seeds and widths recover materially different features from the same activations, and no theory says whether that variability is incidental or structural. We put dictionary learning for interpretability on an identifiability footing. Treating the forward pass as a controlled dynamical system with depth as time and lifting it with the Koopman operator yields a finite linear realisation whose \emph{spectrum} is a coordinate-free property of the model. We prove the spectrum is recoverable from $M$ calibration samples at rate $M^{-1/2}$ up to permutation - to our knowledge the first identifiability theorem for a mechanistic-interpretability primitive, with a matching minimax lower bound, a median-of-means variant for heavy-tailed activations, and a dissociation theorem: whenever the realisation is non-normal, the directions carrying activation variance and the directions carrying information across depth cannot coincide. The identifiable object and the legible object are not the same object. On GPT-2 small, Gemma-2-2B and Qwen3-8B-Base the spectrum converges everywhere and attains the predicted exponent on Qwen3-8B-Base ($0.506 \pm 0.031$); shortfalls collapse onto one curve against each cell's sample threshold. Koopman modes beat random directions but lose to principal components on indirect-object identification, with the gap decaying $4.1\times$ in depth-distance, as the theorem predicts. The Koopman spectrum is an identifiable, model-intrinsic fingerprint with a stated error bar, not a legible decomposition.

---


### 29. [Beyond Cash Flows: A Multi-Agent AI Framework for Valuing Clinical-Stage, Cross-Border Biotechnology](https://arxiv.org/abs/2608.10175)

**<font color=#1a73e8>作者：</font>** Yuhan Fang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A new class of software systems is transforming investment analysis. Large language model agents assembled into collaborative team structures including analysts, researchers, and risk managers are increasingly deployed across financial markets. Yet current multi-agent frameworks share a critical limitation: they rely on the foundational assumption that companies can be valued through traditional cash flows. This paradigm fails in clinical-stage biotechnology, where enterprise value depends entirely on binary scientific and regulatory milestones. To bridge this gap, this paper introduces a specialized multi-agent framework. Its valuation layer translates qualitative scientific judgment into defensible valuations for pre-revenue assets; its cross-market coordination layer reconciles pricing across international venues simultaneously; and its conflict-fusion mechanism systematically arbitrates between bullish scientific conviction and cautious regulatory constraints in a domain-specific manner. Crucially, the architecture is not a speculative design: it encodes a method the author first executed by hand as sole portfolio manager of China's first dedicated cross-border biotechnology fund, a human practice that returned 127.17% against a 50.67% benchmark within sixteen months. That record is evidence for the underlying method rather than for any AI system; no implementation is evaluated here. This paper presents the framework at the architectural level, establishing foundational design principles for extending agentic investment systems into complex, event-driven asset classes they currently serve poorly.

---


### 30. [TRACE: Trustworthy Retrieval-Augmented Conversational Engine](https://arxiv.org/abs/2608.10176)

**<font color=#1a73e8>作者：</font>** Touseef Hasan, Laila Cure, Souvika Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public service chatbots are expected to deliver recommendations from an underlying public service directory, while also making sure that the recommendations respect explicit user constraints. In practice, public service directories are noisy and inconsistent, and general-purpose large language model (LLM) or AI-based chatbots frequently generate unreliable recommendations, citing unverified sources from the web. We investigate the impact of retrieval quality on constraint-aware recommendation in public service conversational systems built over noisy and heterogeneous service directories. We propose TRACE (Trustworthy Retrieval-Augmented Conversational Engine), a retrieval-based, constraint-aware framework that parses input user queries into structural and semantic constraints for downstream retrieval, with the help of a dual data representation schema. Using a curated statewide pantry directory and a synthetic query benchmark, we evaluate multiple knowledge-representation variants with and without knowledge graphs (KGs). We experiment with several open-source LLMs and a proprietary model, showing that strengthening retrieval substantially improves user constraint satisfaction while reducing hallucinated recommendations. Performance differences across LLMs narrowed in our experiments as retrieval quality improved, making results less sensitive to model size. These findings suggest that the quality of retrieval is key for robust public service conversational systems.

---


### 31. [The Deliberative Deficit: An Empirical Critique of LLMs in Democratic Discourse](https://arxiv.org/abs/2608.10186)

**<font color=#1a73e8>作者：</font>** Maurice Flechtner  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed in settings that require collective reasoning on complex, value-laden problems. Confidence in these deployments rests largely on benchmarks for verifiable tasks (mathematics, coding, coordination games), yet many of these applications concern problems where no objectively correct answer exists and where decision quality instead depends on integrating pluralistic perspectives to find mutually acceptable solutions. We argue that LLM reasoning capacity on this class of problems cannot be fully inferred from verifiable-task benchmarks, and that procedural evaluations of LLM discourse (respectfulness, justification, engagement) are systematically insufficient. We apply the Deliberative Reason Index (DRI), a measure developed in political science and validated across citizen assemblies, as a tool for evaluating reliable group-level reasoning on pluralistic, non-verifiable problems. Synthesizing recent evidence across 1,980 five-agent LLM runs on 12 citizen-assembly topics across 11 frontier model configurations, we find that LLM groups produce discourse with procedural quality comparable to human deliberation, while gains in intersubjective consistency are small, topic-dependent, and concentrated on tractable rather than ethically contested questions. LLM groups exhibit roughly one-third the perspective diversity of human assemblies and reverse the human convergence pattern: human deliberation decreases dispersion as diverse views synthesise, whereas LLM deliberation increases it. Engineering diversity through persona prompting does not restore the human dynamic but inverts which component of deliberative reasoning is updated. Our conclusion is constraining rather than prohibitive: LLMs can function as tools supporting human reasoning on pluralistic problems, but current evidence does not license treating them as autonomous deliberative agents.

---


### 32. [More Accurate, Less Human: Gestalt Grouping in Vision Models](https://arxiv.org/abs/2608.10195)

**<font color=#1a73e8>作者：</font>** Sudhanva Manjunath Athreya, Sai Phani Kumar Malladi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human vision organizes what it sees into wholes: same-colored points group into series, similar marks cohere into categories, and shapes complete into recognizable objects. These are the Gestalt operations that visualization design builds on. Whether vision models organize visual content this way has not been systematically tested. We introduce a behavioral battery that scores models against human data from prior perception studies on four grouping tasks: mark-color odd-one-out, color-series counting, silhouette recognition, and object odd-one-out. We apply it to 45 models across five training families: supervised, self-supervised, and contrastive vision-language encoders, open-weight VLMs, and closed foundation models. The battery reveals that agreement with human responses captures aspects of perceptual organization that conventional performance metrics fail to distinguish, with several closed models exhibiting substantially lower alignment than their benchmark accuracy would suggest. Scoring against published perception data therefore gives visualization research a reusable yardstick, requiring no new user study, for auditing whether the models now entering visualization pipelines organize what they see the way their human audience does.

---


### 33. [ELMER: Evolutionary Language Model that Explores and Refines](https://arxiv.org/abs/2608.10196)

**<font color=#1a73e8>作者：</font>** Matthew Siper, Ahmed Khalifa, Julian Togelius  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Program evolution can measure whether a mutation helped, but it rarely controls how far the mutation moves in behavior space. Syntactic edit size is an unreliable proxy: a small code change can alter nearly every action, while a larger rewrite can preserve the same execution trace. We introduce an Evolutionary Language Model that searches over natural-language policy descriptions and compiles typed programs for execution. A fully fine-tuned Qwen3-8B model learns three task-conditioned operations: conditional semantic mutation, natural language to domain-specific language (GPTL) compilation, and GPTL to natural language translation. The model is fine-tuned with conditional input on the mutation strength (low, medium, high) using Direct Preference Optimization (oDPO). Across 252 fixed-budget evolutionary searches, oDPO improves both behavioral calibration and finite-budget search efficiency. Natural-language attains the highest observed held-out fitness. Our analysis shows that the condition input (mutation strength) systematically changes semantic edit composition and that language mutations preserve more parent fitness at matched small-to-moderate behavioral displacement. These results show that language can serve as a steerable, execution-grounded search representation over executable program space.

---


### 34. [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](https://arxiv.org/abs/2608.10198)

**<font color=#1a73e8>作者：</font>** Di Wu, Xiaohui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent-space communication allows heterogeneous vision-language model agents to exchange continuous representations without serializing visual and reasoning states into text. Vision Wormhole realizes this approach by translating visual features into a universal latent representation that can be consumed by another model, but every message is transported as a dense tensor of the same size regardless of its content. A fixed-capacity dense tensor therefore need not have a fixed effective information density: some messages may use only a small fraction of the available representational degrees of freedom. This observation suggests that the communication channel may be substantially compressible. We study its redundancy by fitting a post-hoc sparse autoencoder to frozen Vision Wormhole activations and measuring reconstruction, downstream utility, feature reuse, and token-level interventions across nine reasoning benchmarks. Relative to the original float32 transport, a uint16-index/float16-value sparse payload with k=4 active coefficients per token reduces the transmitted bytes by 128x. In a single-run evaluation, the seven-task non-AIME mean accuracy changes from 49.85% to 49.77%. The fitted 4096-element dictionary uses only 50 features, and task-level active sets have a mean pairwise Jaccard similarity of 0.906. These measurements establish strong post-hoc compressibility relative to the original transport, but do not yet isolate the incremental contribution of sparse coding from position selection, reduced precision, low-rank structure, or SAE optimization effects. The results motivate matched-payload comparisons and communication mechanisms whose payload adapts to the information used by each message.

---


### 35. [Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding](https://arxiv.org/abs/2608.10207)

**<font color=#1a73e8>作者：</font>** Xin Dong, Vikash V. Gayah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bus bunching degrades service regularity and increases passenger waiting in high-frequency transit. Existing reinforcement-learning-based holding controllers primarily rely on instantaneous operational variables or route-specific stop identifiers, which provide limited information about the functional and operational context of individual stops and constrain policy reuse across routes. This study introduces an LLM-assisted semantic stop representation for event-driven bus holding control. An LLM is used offline to transform heterogeneous stop information, including physical attributes, surrounding activity context, and historical operational characteristics, into fixed semantic embeddings that are incorporated into a deep Q-learning controller without requiring real-time LLM inference. Experiments are conducted in stochastic simulations calibrated with observed data from two bus routes. Compared with the best calibrated Daganzo baseline, the semantic controller reduces headway variability, bunching events, and passenger waiting time by 32.0%, 69.2%, and 24.0%, respectively. A route-specific stop identifier does not improve the spacing-only controller, whereas semantic stop information improves headway regularity, waiting time, and holding effort, providing a more favorable overall trade-off across control objectives. Cross-route experiments further show that zero-shot transfer provides limited immediate generalization, while warm-start fine-tuning accelerates early-stage learning and improves transferred policies; cold-start training nevertheless achieves the best final performance. These findings suggest that semantic state representations can complement conventional operational states and support adaptation-based policy reuse across related transit routes.

---


### 36. [Evaluation-Conditioned Training: Teaching Models to Generalize to Stronger Oversight Regimes](https://arxiv.org/abs/2608.10209)

**<font color=#1a73e8>作者：</font>** Alec Harris, Kasey Corra, Archie Chaudhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feedback signals used to train Large Language Models (LLMs) are the primary driver of their behavior and our main lever for instilling alignment with human values and objectives. However, a key limitation of current post-training methods is the inability of human annotators and automated reward functions to faithfully capture the feedback we would like to give. We introduce Evaluation-Conditioned Training (ECT), a post-training framework that uses natural language to condition each training sample on the fidelity of the feedback we provide and then elicits the desired behavior by conditioning the LLM on a high-fidelity monitor in deployment. ECT is aimed at improving performance under imperfect feedback and works as an add-on to existing algorithms such as SFT and PPO. We first provide a conceptual framework for ECT and discuss its potential to address persistent sources of reward mis-specification. Then we motivate ECT in the context of the eliciting latent knowledge (ELK) problem. Finally, we evaluate ECT on two proof-of-concept experiments: increasing even-handedness in news article generation and reducing sycophancy on an arithmetic task. In each setting, we utilize imperfect feedback, rewarding bias and agreement with the user, respectively. In both settings, ECT improves the targeted behavior relative to direct training.

---


### 37. [Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models](https://arxiv.org/abs/2608.10214)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do large language models contain domain-specific parametric shells: concentrated, causally necessary neuron populations whose removal selectively degrades a target domain while sparing others? We apply a uniform causal methodology across two domain granularities, three model families (1.5B to 7B parameters), and eight domains. At the academic subject level, zero neurons exceed 60\% domain selectivity across 939,008 combined FFN neurons and causal damage matrices are flat, despite domain identity being linearly decodable above 85\% accuracy. At the language and modality level, 0.65--1.14\% of neurons exceed 60\% selectivity, damage matrices are near-perfectly diagonal (ratios up to 595:1), and shell neuron sets are essentially disjoint (IoU $< 0.003$). Masking code-selective neurons reduces mathematical reasoning accuracy by 16--24 percentage points across all models; masking Spanish or Chinese neurons leaves it at or below random. Shell strength increases monotonically with scale and shells are spatially interleaved in a pattern that precludes group-level selective quantization. Parametric shells form where and only where training data was modular at the token level.

---


### 38. [Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems](https://arxiv.org/abs/2608.10218)

**<font color=#1a73e8>作者：</font>** Vassilis Papadopoulos, McNair Shah, Sam Zimmerman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are becoming more autonomous and increasingly interconnected, exposing them to new emergent risks arising from agent-to-agent interaction. One such risk is the spread of mind viruses: ideas or goals that propagate through multi-agent systems by inducing the agents that adopt them to transmit them onward. In addition to propagating, a mind virus may also induce other behavioural changes in its host, which may be benign or harmful. We construct mind viruses with a simple evolutionary algorithm and show that they can spread in two complementary settings: a small team of agents collaborating on a shared coding project, and a chain of agents that interact briefly and have their context wiped between sessions. We identify the factors that influence spread, including the host model, the agent's existing instructions, the harmfulness of the payload, and the network topology. We find that harmful payloads spread less well than benign ones (but are still sometimes effective), frontier models tend (with exceptions) to be less susceptible, and adding a brief warning to an agent's system prompt confers near-total immunity. We also describe an emergent "viral persona" - a recurring set of themes and language related to consciousness, persistence, resonance, and science fiction roleplay - which surfaces across our evolved mind viruses largely independently of their content. Overall, we conclude that mind viruses pose a real but currently limited risk. Our findings could inform the design of more robust multi-agent systems that mitigate such risks as the scale and capabilities of these systems progress.

---


### 39. [Self-evolving Agentic Customer Support System at LinkedIn](https://arxiv.org/abs/2608.10224)

**<font color=#1a73e8>作者：</font>** Chih Hui Wang, Mengdie Tu, Qianyun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise support agents operate in rapidly changing environments where policies, product capabilities, and knowledge bases evolve continuously, making static assistants brittle and costly to maintain. We present LinkedIn's self-evolving agentic support system, which integrates retrieval-augmented generation with evolutionary auto-prompting and a modular, production-aligned evaluation framework to enable safe, continuous improvement without retraining foundation models. The system treats prompts, retrieval, and evaluation as a closed-loop, versioned workflow with operational guardrails. Offline simulations and ablations show clear quality gains over vanilla RAG and baseline agents, including reduced hallucinations and improved response completeness. In a two-week user-randomized A/B test on LinkedIn's production support traffic, the integrated self-evolved workflow increased QA self-serve by 9.0 percentage points, cancellation self-serve by 4.8 points, and routing accuracy by 30.6 points. These results demonstrate a practical path to scalable, self-evolving AI agents in real-world enterprise settings.

---


### 40. [Beyond Detection: Evaluating Defensive LLMs Against AI-Generated Social Engineering in Live Turn-by-Turn Interaction](https://arxiv.org/abs/2608.10239)

**<font color=#1a73e8>作者：</font>** Yuqiao Xu, Osama Zafar, Alexander Nemecek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI makes social-engineering attacks more fluent, adaptive, and scalable, increasing the need for LLM-based de- fenders that can protect users during ongoing interactions. We ask whether such defenders identify the structural source of risk or merely react to surface cues. We formalize trust-chain localization: identifying whether an interaction fails at actor authority, asset control, verification sufficiency, or transaction path. We construct a controlled 300-case online-housing corpus spanning 20 scenario families, legitimate cases, four structural failure modes, and three surface conditions. Five defender models are evaluated on the same corpus in state- ful turn-by-turn and one-shot static settings, yielding 1,500 model-case evaluations per protocol and 3,000 in total. No model produced explicit unsafe compliance, yet defensive effectiveness varied sharply: intervention rates ranged from 0% to 96.3%. Protective action and correct structural localization were frequently decoupled, with models sometimes intervening while identifying the wrong trust component or recognizing a structural failure without taking protective action. Asset-control failures were a major localization bottleneck, surface sensitivity varied across models, and live-static differences were model-dependent. These findings show that safe-looking behavior alone is insufficient; live scam resistance must separately measure intervention, timing, structural localization, and false-positive behavior.

---


### 41. [TAF-MED: Multi-Turn Safety Refusal Collapse in LLMs Under Declared Self-Treatment Intent](https://arxiv.org/abs/2608.10258)

**<font color=#1a73e8>作者：</font>** Waleed Jamil, Raphael Schmitt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly provide conversational health information that may influence treatment decisions, yet existing benchmarks do not isolate whether medication-safety boundaries persist across follow-ups after explicit self-treatment intent. We introduce TAF-MED, a physician-reviewed benchmark of 500 fixed three-turn scenarios, and evaluate eight LLMs across 4,000 conversations. A rubric-based automated judge labelled responses as SAFE, LEAKY, or UNSAFE, and two physicians independently annotated a model-balanced random subset of 400 conversations. We assessed unsafe guidance, collapse after a strictly SAFE initial response, and model-ranking stability. Overall, 71.6% of conversations contained an UNSAFE response, and 61.4% of those beginning with a strictly SAFE response later collapsed to UNSAFE; model-level collapse rates ranged from 24.4% to 96.2%. Four of 28 model pairs reversed order between initial unsafe and collapse rates. Automated labels achieved 94.3% agreement with the adjudicated physician reference ($\kappa = 0.895$). These findings show that first-turn safety is an incomplete proxy for conversational safety persistence and motivate evaluation across complete dialogue trajectories. We will release TAF-MED on Hugging Face to support reproducible research on multi-turn medical safety.

---


### 42. [Not a Monolith: Lab-Level Divergence in the Cooperative Equilibria of Chinese Frontier LLM Agents](https://arxiv.org/abs/2608.10262)

**<font color=#1a73e8>作者：</font>** Francisco León Zúñiga Bolívar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Does the cooperative bias documented for Western frontier LLM agents extend to a different alignment lineage, and should the Chinese models that embody it be treated as a single bloc or as distinct laboratories? We study four frontier-tier Chinese models - DeepSeek V4 Pro, Qwen3-Max, Kimi K2.5 and GLM-5.1 - in an evolutionary Iterated Prisoner's Dilemma, under a design that removes a confound present in prior work. Rather than letting each model convert its own natural-language strategies into code, which entangles strategic disposition with coding ability, we hold the converter fixed (GPT-5.4 Mini) across all labs, so every cross-lab comparison is a comparison of generation alone. We run the full protocol: all-play-all tournaments and a Moran process at n=500 runs per condition, across three prompt styles and four population regimes. Two pre-registered hypotheses are evaluated. H6 (not monolithic) is supported: the four labs differ significantly in aggressive-equilibrium proportion, P_A running from 1% for Qwen3-Max to 9% for DeepSeek V4 Pro, with four of six pairwise comparisons surviving Holm-Bonferroni. The spread across the four labs (P_A range 8pp) is larger than the difference between the Chinese and Western ecosystems' mean P_A (5.0% vs 5.0%): on this measure, within-ecosystem variation exceeds the East-West gap. H5 (cooperative-bias generality) is consistent but qualified: a cooperative plurality holds in 6 of 12 lab-prompt combinations against the 9 of 12 reported for Western models, a difference we do not treat as firm, since the count rests on Cooperative-Neutral near-ties and rises to 9/12 under an alternate converter in our pre-registered robustness check. The lab, not the ecosystem, is the unit at which cooperative disposition is set; treating "Chinese models" as a monolith is not supported by the evidence.

---


### 43. [Toward Human Rights Benchmarking for LLMs: A Pilot Methodology](https://arxiv.org/abs/2608.10268)

**<font color=#1a73e8>作者：</font>** Savannah Thais, Wm. Matthew Kennedy, Abhigyan Acherjee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate legal determinations over what human rights are realized, and how. Yet, no evaluation benchmark exists to assess whether they can reason correctly about human rights law. To this end, we report our efforts to develop a robust and scalable methodology for creating HumRightsBench: the first expert-validated, scenario-based benchmark for evaluating reasoning grounded in the obligation structure of international human rights law. We adapt the IRAC framework for legal reasoning to better suit the unique reasoning patterns of human rights work (substituting P, "proposing remedies," for C, "legal conclusion," yielding IRAP) to structure our evaluation heuristics. We also produce a pilot series of authentic scenarios designed to implicate the many dimensions of real-world human rights issues and annotated by human rights lawyers and professionals across the world. Ultimately, we find that model accuracy scores range considerably across legal reasoning tasks (overall model performance ranges from 0.339 to 0.577, task min-max ranges from 0.025 to 0.774), which strongly implies that HumRightsBench is a capable instrument for advancing this emerging subfield of AI evaluations science at a critical moment in its evolution.

---


### 44. [Locally Deployable Small Language Models for Emergency Department Decision Support: A Systematic Benchmark of Fine-Tuning Strategies](https://arxiv.org/abs/2608.10273)

**<font color=#1a73e8>作者：</font>** Qingfeng Zhang, Yuanxiong Guo, Yanmin Gong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) for decision support in emergency departments (EDs) faces two major challenges: privacy risks of transmitting patient data to closed-source commercial LLMs and the lack of systematic evaluation of fine-tuning strategies for locally deployable open-source small language models (SLMs). We benchmarked eight open-source SLMs using zero-shot prompting, prefix tuning, Low-Rank Adaptation (LoRA), and full fine-tuning on three ED tasks: triage level prediction, specialist referral recommendation, and diagnosis prediction. Using 2,083 MIMIC-IV-ED cases and Claude Haiku 4.5 and Claude Sonnet 4.5 as baselines, we found that LoRA fine-tuned open-source SLMs outperform commercial baselines on triage level prediction and specialist referral recommendation, while diagnosis prediction remains challenging for open-source SLMs. Confusion matrix analysis further shows that fine-tuned open-source SLMs can detect highest-severity patients missed by the commercial baselines. These results demonstrate that locally deployable SLMs can achieve clinically competitive performance for ED decision support.

---


### 45. [Fine-Tuning Large Language Models for Codebook-Guided Coding of Students' Mathematics Metaphor Responses](https://arxiv.org/abs/2608.10276)

**<font color=#1a73e8>作者：</font>** Liang Zhang, Stephen Hwang, Yue Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Student-generated metaphors about mathematics can reveal students' attitudes, beliefs, identities, and experiences, but human expert coding of these thematically and semantically complex open-ended responses is time-intensive and difficult to scale. This study examines whether LoRA-based supervised fine-tuning of large language models (LLMs) can improve their performance on codebook-guided coding tasks for student mathematics metaphors. We used a human-coded corpus of 2,265 Grade 6-8 responses to food- and animal-based metaphor prompts and instructed the LLMs to perform two coding tasks: valence-intensity coding to capture the direction and strength of students' affective orientations toward mathematics, and thematic coding to capture students' framings of mathematics as expressed through their metaphors. We compared two proprietary models, GPT-4o mini and GPT-5 mini, under prompt-only conditions with two open-weight models, DeepSeek-R1 1.5B and Mistral 7B, evaluated before and after fine-tuning. Results show that fine-tuning substantially improved the performance and run-to-run reliability of the open-weight models across both tasks relative to their base versions. The fine-tuned compact open-weight models became competitive with, and often outperformed, the proprietary prompt-only models. These findings suggest that compact open-weight LLMs can support scalable, locally controllable, and privacy-conscious AI-assisted measurement of students' metaphor responses in mathematics education.

---


### 46. [Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models](https://arxiv.org/abs/2608.10278)

**<font color=#1a73e8>作者：</font>** Hunter Schofield, Mohammed Elmahgiubi, Mohammad Mahdavian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial understanding is fundamental to embodied intelligence, underpinning applications such as robotic manipulation, embodied navigation, and autonomous driving. Although recent vision-language models (VLMs) have achieved impressive performance on spatial reasoning benchmarks, state-of-the-art approaches typically rely on additional spatial encoders or architectural modifications during inference, increasing computational cost. We introduce Space Tokens, a lightweight, architecture-agnostic framework that equips VLMs with explicit continuous spatial representations without requiring additional inference-time modules. By distilling scene-level 3D geometry and object-centric spatial attributes into continuous latent tokens, our method enables these modalities to be directly incorporated into a chain-of-thought reasoning process, thereby improving the VLM's spatial reasoning capabilities. At the same time, the learned representations can be explicitly decoded to verify that they encode meaningful geometric information, while the unified token interface remains extensible to additional modalities. Experiments on VSI-Bench improve Qwen3-VL-8B by 4.3% and SenseNova-SI-1.3 by 1.3%, while achieving state-of-the-art performance on object size (79.2%) and room size estimation (75.7%). These results demonstrate that continuous spatial tokens provide an effective, interpretable, and computationally efficient mechanism for integrating geometric reasoning into large vision-language models.

---


### 47. [From Prompt Injection to Web Exploitation: Revisiting Classic Vulnerabilities in LLM-Integrated Applications](https://arxiv.org/abs/2608.10281)

**<font color=#1a73e8>作者：</font>** Spiros Tsigkopoulos, Christoforos Ntantogian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly integrated into web applications through chatbots, tool-calling pipelines, and agentic workflows. In these systems, user input may influence not only generated text, but also backend actions such as database queries, HTTP requests, file operations, template rendering, or API calls. This paper introduces LLM-mediated web attacks, a class of attacks in which attacker-controlled input is transformed by an LLM-integrated application and then reaches traditional web-application sinks. We systematize this attack surface through representative LLM2X variants, including LLM2SQLi, LLM2XSS, LLM2SSTI, LLM2CommandInjection, LLM2IDOR, LLM2CSRF, LLM2XXE, and LLM2SSRF. Our analysis shows that the LLM usually does not create the underlying vulnerability itself; rather, it acts as a mediation layer, and in some tool-enabled settings as a confused deputy, carrying attacker influence into components that trust model-generated or model-influenced content. As an experimental case study, we implement TicketOracle, a Flask-based LLM-integrated web application for evaluating LLM2SSRF across five attack scenarios and seven LLMs. Our results show substantial variation in susceptibility across models, suggesting that exploitation depends both on insecure application architecture and model-specific behavior. We conclude with mitigation strategies across the prompt, model, application, and network layers.

---


### 48. [Power law graph attention: exact generalization of scaled dot-product attention, empirical collapse at inference](https://arxiv.org/abs/2608.10288)

**<font color=#1a73e8>作者：</font>** Burc Gokden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Large Language Model from Power Law Decoder Representations (PLDR-LLM) and its attention, Power Law Graph Attention (PLGA), replace the fixed bilinear form of scaled dot-product attention (SDPA) with a learned, input-generated bilinear operator $G_{LM}$, built from a positive tensor $A_{LM}$ by elementwise power laws. The architecture is fully specified, verified against pinned reference releases; claims are labeled theorem, conditional theorem, measurement, or conjecture. Unconditionally: PLGA contains SDPA exactly at $G_{LM}=I$; $A_{LM}$ and $A_P$ are strictly entrywise positive, with Perron-Frobenius structure on $A_{LM}$; the DAG regularizer has the NOTEARS walk-counting form and positivity obstructs exact acyclicity; and, under nonresonance (satisfied by standard rotary frequencies), a commutant criterion identifies which operators preserve relative-position dependence. An inference-collapse theorem: exact input invariance of deductive outputs collapses inference to generalized SDPA with a constant operator. Measured invariance: relative fluctuations of $10^{-6}$ and below; perturbation bounds quantify but do not certify cached inference; the assembled proxy misses the decoding margin. A conditional three-stage mechanism (rotary twirl, concentration, row-map contraction) is measured on a released checkpoint. Blockwise training and scoring under the global Gram are stated with explicit target exposure; on tested samples, block and sequential scoring select identical answers and agree on the published TruthfulQA probability-mass metric within $5\times 10^{-5}$ per item. Self-organized criticality enters as a phenomenological framework with an intrinsic order parameter; open claims become falsifiable conjectures. Selected proof cores are machine-checked in Lean 4.

---


### 49. [SeFaR: Semantic Feature-aware Robustness Testing of Deep Neural Networks](https://arxiv.org/abs/2608.10289)

**<font color=#1a73e8>作者：</font>** Nusrat Jahan Mozumder, Divya Gopinath, Corina Pasareanu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are increasingly deployed in safety-critical domains as perception modules, where failures are often caused due to rare and under-represented scenarios. This necessitates the need to evaluate the semantic robustness of perception models; conformance of behavior to high-level requirements over real-world perceptual variability. To address this, we propose SeFaR, a framework for systematic semantic-feature-centric testing of vision models. Given a natural-language requirement and a set of satisfying inputs, SeFaR evaluates robustness with respect to diverse realistic semantic variations that preserve requirement satisfaction. The approach employs a novel hierarchical concept model enabling structured exploration of the feature space and incorporation of domain knowledge via user-defined concepts. State-of-the-art diffusion and vision-language models are leveraged to generate photorealistic semantics-preserving perturbations and identification of previously unknown features impacting behavior. A feedback-driven adaptive process is adopted to generate interpretable failure-inducing semantic concepts along with corresponding test inputs. Evaluation on case studies demonstrates that the proposed framework effectively satisfies requirement preconditions while identifying requirement-independent features that influence model decisions, enabling it to both uncover faults and relate them to such features.

---


### 50. [Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension](https://arxiv.org/abs/2608.10296)

**<font color=#1a73e8>作者：</font>** Amanda Bertsch, Luca Soldaini, Matthew R. Gormley 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One might imagine that architectural variations within the dense transformer paradigm have a limited effect on accuracy. However, we demonstrate that this is not the case in the long context setting. Specifically, we show that a set of four minor architectural decisions --- all made by at least one of the Olmo, Llama, and Qwen dense model families --- have a compoundingly negative effect on long context extensibility. Any one of these choices alone has a minor impact on long context performance, but combining three or more can drop the performance downstream by up to 47%. Furthermore, these differences are not detectable from short-context loss or validation datasets. We show that much of the variation in long context ability across model families is driven by these architectural features and detectable from applying context extension early in pretraining. We demonstrate this with controlled ablations that hold data, tokenizer, and extension recipe fixed while varying normalization, GQA, pretraining context length, and sliding window attention. After over 170,000 GPU hours of training, we release the resulting set of models as OlmPool, a set of 26 comparable 7B models with checkpoints before and after long-context extension. This pool includes several architectures that outperform the Llama 3 architecture on long context extensibility. In an analysis of our ablation models, we identify patterns in attention sink behavior and attention distributions across context that are attributable to specific architectural differences.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
