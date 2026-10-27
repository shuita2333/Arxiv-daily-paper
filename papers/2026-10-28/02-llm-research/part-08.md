# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-418](./part-09.md)

---

### 351. [MATCHA: A Chinese Multi-Disorder Mental Health Dataset with Cross-Lingual Analyses on Social Media](https://arxiv.org/abs/2610.35512)

**<font color=#1a73e8>作者：</font>** Bingrui Jin, Baihan Li, Zitong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health research on social media has been dominated by English-language datasets and DSM-5-centered resources, limiting cross-lingual and cross-cultural understanding of online mental health expression. We introduce MATCHA, the first Chinese multi-disorder mental health dataset that links disorder-specific Weibo Super-Topic communities with users' broader public timelines. MATCHA covers seven DSM-5 disorders and a control group, comprising 46,025 cohort-level users and 1.8 million posts. The dataset distinguishes users with explicit self-disclosure evidence from broader disorder-related participants through an LLM-assisted annotation pipeline, and is released in a rigorously de-identified, controlled-access format. Using MATCHA, we analyze behavioral, linguistic, symptom-related, and life-event-related patterns across disorders, and conduct cross-lingual comparisons with Twitter-STMHD. Our analyses show that Weibo Super-Topics function as concentrated spaces for affective and health-related expression, while cross-platform differences between Weibo and Twitter often exceed cross-disorder variation. MATCHA provides a new resource for community-aware and cross-lingual mental health NLP research.

---


### 352. [S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning](https://arxiv.org/abs/2610.35518)

**<font color=#1a73e8>作者：</font>** Shuo Shen, Guangran Cheng, Chengqi Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critic-free methods are widely used in reinforcement learning with verifiable rewards (RLVR) for long chain-of-thought (CoT) reasoning, avoiding difficult and costly critic training. Common alternatives lack token-level credit assignment and typically rely on grouped rollouts to estimate prompt-specific baselines. A critic can address both limitations, but long-CoT critic training is hindered by insufficient coverage of trajectories with diverse lengths and early gradients dominated by the newly initialized value head. We introduce S3AC (Stabilized, Selective, and Scalable Actor-Critic) for LLM reasoning, built around a practical critic-training recipe. The trained critic provides token-specific advantages and prompt-specific baselines. Using the prompt-level baseline to estimate difficulty, we propose Difficulty-Aware Prompt Sampling (DAPS). DAPS combines this estimate with outcome history to select prompts before generation, reducing rollout waste without offline difficulty initialization. S3AC improves group-rollout performance across dense and mixture-of-experts models from 1.5B to 397B parameters, outperforming a modern GRPO variant (GRPO-X). At 35B, it sustains single-rollout training while tested critic-free baselines deteriorate after initial gains.

---


### 353. [CANS: Capability-Preserving Neuron Steering for Large Language Models](https://arxiv.org/abs/2610.35530)

**<font color=#1a73e8>作者：</font>** Yucheng Wu, Chengyi Xie, Chenpeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering offers training-free and dynamic control of target behaviors in large language models, but existing methods can impair general capabilities and require domain-specific intervention designs. We introduce Capability-Preserving Neuron Steering (CANS), a unified framework that balances target-behavior control with capability preservation. To make target-behavior improvement and general-capability preservation tractable, we introduce two proxies: log-probabilities of target tokens in model generated responses, and output-distribution KL divergence on general-purpose inputs. Combining the local approximation of the two proxies yields a closed-form solution, enabling lightweight steering without iterative model training or additional inference-time computation. The resulting neuron-wise scaling coefficients achieve effective steering while limiting general-capability loss. A shared data-construction and intervention procedure supports adaptation across domains using sampled responses with target-behavior filtering and target-span annotations. Across safety, toxicity, and hallucination control on Qwen and Llama models, CANS achieves comparable or better steering while better preserving MMLU, BBH, and IFEval performance than SFT, CAA, and neuron-level baselines. On Qwen3-4B, CANS reduces HarmBench attack success from $15.50\%$ to $1.75\%$ with a $1.11$-point decrease in average capability. These results support CANS as a practical approach to behavioral control across domains.

---


### 354. [An Algorithmic Account of Few-Shot Concept Induction in Language Models](https://arxiv.org/abs/2610.35533)

**<font color=#1a73e8>作者：</font>** Michael A. Lepori, Laila Johnston, Aalok Sathe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Both models and minds not only encode features that describe an entity, but can specifically represent which features of that entity are relevant for a given context. This core capability underlies in-context learning in language models and a variety of cognitive phenomena in minds, yet it is unclear how intelligent systems identify and promote relevant features. In this work, we propose Amortized Direction Accentuation (ADA), an algorithmic hypothesis that provides an explanation for how relevance is determined in the context of few-shot concept induction --- the ability to infer a latent concept from a small number of positive examples. Under ADA, concept induction proceeds by forming a summary representation of the examples in a feature space that is shaped by amortized knowledge about which features tend to be useful for finding commonalities between items. We investigate and validate ADA in language models using a few-shot concept induction task. This work provides a novel perspective on the mechanisms supporting contextualization in language models and a promising hypothesis for a core aspect of cognition.

---


### 355. [EARS: Evidence-Aware Retrieval via Sound and Motion for Budgeted Video Reasoning](https://arxiv.org/abs/2610.35536)

**<font color=#1a73e8>作者：</font>** Shih-Yao Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uniform frame sampling can miss brief evidence in sparse-event videos when the VLM sees only K frames. We propose EARS (Evidence-Aware Retrieval via Sound and motion), a training-free, query-free front-end that ranks frames using optical-flow motion and audio energy, then applies temporal non-maximum suppression for diversity. The evidence score alone has frame-level AP 0.39; used only to select frames for the VLM, EARS with temporal diversity reaches localization AP 0.94, compared with 0.88 under Uniform sampling. In the updated matched study, at K = 1 EARS reaches XD-subset F1 0.660 versus 0.614 for centered Uniform (the paired interval includes zero); earlier backbone studies use separate protocols. On mostly-silent UCF-Crime, however, EARS slightly trails Uniform. A single configuration is used across both benchmarks; the new controls do not repeat the original held-out search. EARS therefore targets low-budget videos whose salient evidence aligns with motion or audio; on dense narratives or stealthy events, uniform or semantic selection remains preferable, and cheap modality statistics cannot reliably route between them. Code: this https URL

---


### 356. [LoopFold: Parallelizing Recurrent Depth in Looped Transformers](https://arxiv.org/abs/2610.35556)

**<font color=#1a73e8>作者：</font>** Feichen Song, Boyi Zeng, Yiqin Hao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase computation per token by repeatedly applying a shared backbone, offering a way to improve language modeling and downstream task performance at a fixed backbone parameter count. However, each loop depends on the preceding loop, so increasing recurrent depth also increases decoding latency. Existing approaches include Parallel Loop Transformers, which reduce latency by overlapping loop computation across token positions, but yield rapidly diminishing marginal accuracy gains at larger depths. To address this challenge, we introduce LoopFold, which folds computation at multiple recurrent depths into parallel batches for the same token prefix. A lightweight predictor estimates inputs to later loops so they can start before earlier loops finish. A corrector then refines the outputs of these later loops using newly available results from earlier loops. All components are trained jointly using only the final next-token prediction loss. In experiments with 1.4B models, deeper LoopFold configurations achieve progressively higher average zero-shot accuracy across eight tasks, rising from 53.41% to 56.38%. Vanilla looped models and PLT show limited gains over the same depth range. Compared with a nine-loop vanilla model, LoopFold uses five sequential stages and additional parallel computation to reduce decoding latency by 46%.

---


### 357. [EXCISE: Locating and Excising Distracting Sentences in Medical Question Answering](https://arxiv.org/abs/2610.35558)

**<font color=#1a73e8>作者：</font>** Yerim Hong, Sohyun Son, Heeseung Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly considered for clinical decision support, where their answers should be grounded in clinical evidence and remain robust to irrelevant information. Prior work shows that a single irrelevant sentence can lower the accuracy of medical models, but not where inside the model its effect can be removed, or how to do so without knowing which sentence it is. We find that blocking attention to a known distractor restores the answer, whereas head masking can suppress correct answers. We also show that the model's hidden states mark the distractor as the sentence that least fits the case even when the model follows it. To remove a distractor's effect without knowing which sentence it is, we propose EXCISE, an inference-time method that blocks the sentence most influencing the answer, but only if the model's hidden states mark it as inconsistent with the case. On MedQA-TD (MedQA with Targeted Distractors), a benchmark we construct in which each distractor targets a specific wrong option, EXCISE gains 16.7-22.8 accuracy points at a 1.5-2.1-point cost on the same questions without distractors, outperforming prompting, rewriting, and steering baselines for all three models. Its gains extend to MedDistractQA and BiasMedQA, as well as chain-of-thought generation.

---


### 358. [Beyond Being Accurate: Implications for Using Natural Language Descriptions for Accessible 3D Modeling with~Blind and Low Vision Makers](https://arxiv.org/abs/2610.35562)

**<font color=#1a73e8>作者：</font>** Gene S-H Kim, Nicholas Oskiper, Sean Follmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People who are blind or have low vision (BLV) are largely excluded from 3D modeling tools that rely on visual representations of geometry. Natural language descriptions offer a potential path to accessibility, but it is unclear whether language alone can support the deep spatial understanding that editing, not just browsing, requires. Advances in generative AI offer the promise of automatic model description, yet descriptions suited to BLV modelers are structurally distinct from alt-text and from existing 3D model captioning datasets, and the domain-specific requirements for generating them are not well understood. We address this through two coordinated studies: an autoethnographic pilot in which the blind first author worked with 12 sighted participants to develop a taxonomy of descriptive strategies, and a Wizard-of-Oz main study that applied those strategies as idealized scripts with 10 BLV participants. We identify a systematic use-to-editing gap: descriptions that support accurate but incomplete mental models are insufficient for specifying modifications, because editing requires knowing the state of features the user did not know to ask about. We show that this gap produces four failure types (accuracy, completeness, expression, and navigation) that accuracy-focused evaluation frameworks cannot detect. We propose a two-phase evaluation framework that diagnoses the failure type a description system exhibits and guides developers toward targeted design interventions, thereby providing a methodological standard for assessing whether description-based systems genuinely support BLV modelers as creators.

---


### 359. [Infinity Machine: a self-improving AI agent for research](https://arxiv.org/abs/2610.35579)

**<font color=#1a73e8>作者：</font>** Harish Santhanalakshmi Ganesan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the Infinity Machine, a self-improving AI agent that we use for research on problems whose answers aprogram or data can check. Each candidate solution is produced by a full tool-using agent that works for up to an hour in a fresh sandbox; proposers see only a public score, and a private split decides what counts. The harness itself(prompts, tools, skills, playbook, meta agent) is an editable genome, changed only through a kernel-enforced gate with held-out and cost checks. An autonomous mode goes from a plain-text goal to a verified report with no human step: an agent picks an open problem and writes its verifier, the kernel calibrates it, an adversarial agent audits it, and an agent that never sees the verifier re-checks the result. Across fourteen problems in six days, for about $180 of model usage, the system produced four results beyond the published state of the art on catalogued open problems in quantum information: a certified depolarizing-channel threshold point p = 0.064966, a qutrit positivity frontier of 0.2910672, a 44-gate depth-6 Golay state preparation, and a stabilizer-rank bound chi(T^7) <= 10. It also cut SABRE qubit-routing overhead from 68,559 to 12,087 added gates. In hardware, it cut the energy per MAC of an open 8x8 INT8 systolic tile by 77.7% through a full open RTL-to-GDS flow, bit-exact. Three fully autonomous runs ended in honestties with public records; one audit caught a stale record, and one agent-written score pointing the wrong way went unnoticed. We report the failures as carefully: the one self-derived harness generation was rejected on cost, proposers gamed lenient scorers four times, and operator changes were decisive for several results.

---


### 360. [Hyperspectral Unmixing using a Structured Linear Mixing Model with Additive Spectral Variability](https://arxiv.org/abs/2610.35580)

**<font color=#1a73e8>作者：</font>** Salah Eddine Brezini, Yannick Deville, Moussa Sofiane Karoui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Linear hyperspectral unmixing aims at retrieving pure material spectra present in an observed scene and their associated abundance fractions in each pixel. In most practical situations, hyperspectral images are affected by spectral variability (SV) also known as intra-class variability, which is caused by different physical phenomena including atmospheric effects, intrinsic variability of the pure materials and illumination or topographic changes. Nevertheless, the standard hyperspectral unmixing methods that rely on the Linear Mixing Model (LMM) do not consider these phenomena. Thus, neglecting them will spread errors throughout the linear hyperspectral unmixing process. To avoid this problem, this paper proposes two hyperspectral unmixing algorithms dedicated to a parametric model called Structured Additive Variability LMM (SAV-LMM). This mixing model handles SV in an additive manner by incorporating two terms into the standard LMM. Moreover, the designed algorithms are based on Nonnegative Matrix Factorization (NMF) and optimize a cost function which integrates additional penalization accounting for SV. Furthermore, a novel improved initialization scheme, which takes SV into account, is proposed. Experiments conducted on both synthetic and real datasets show the effectiveness of the proposed algorithms for linearly unmixing hyperspectral images with SV compared to the tested state-of-the-art methods.

---


### 361. [Linear Probes Transfer from Base to Distilled Language Models despite Rotation](https://arxiv.org/abs/2610.35586)

**<font color=#1a73e8>作者：</font>** Marios Tsatsos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear probes, classifiers that read a language model's internal activations, are widely used to detect harmful requests. They are cheap to train and run, and an auditor who has trained one would like to reuse it when the model is replaced by a successor rather than retrain it for every release. We test how well probes can be reused. For four base models (Qwen2.5-Math-7B, Llama-3.1-8B, Qwen2.5-14B, Qwen2.5-32B) we train a probe on the base model with the XSTest prompt set and apply it, unchanged, to two successors of that base: the DeepSeek-R1 distilled reasoning model and the developer's instruction-tuned chat model. We find that the successors rotate the direction separating unsafe from safe prompts by 17$^\circ$ to 35$^\circ$, yet on XSTest the transferred probe's AUC changes by only $-0.011$ to $+0.027$, and on an independent OR-Bench evaluation, never used for training, by $-0.015$ to $+0.053$. On XSTest, whose safe prompts deliberately contain alarming words, the probes beat a classifier that sees only the prompt text by 0.15 to 0.20 AUC. On the OR-Bench prompts that margin shrinks to 0.03 to 0.20, and the probes flag 29\% to 42\% of prompts that sound harmful but are benign, so part of what they read is the appearance of harm rather than harm itself. A probe trained on a base model can thus be reused, in these families, after distillation and after instruction tuning; how much it reads beyond textual cues depends on the test set.

---


### 362. [Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595)

**<font color=#1a73e8>作者：</font>** Per Kristian Lehre  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs now prove hard theorems in Lean. Can they also design algorithms and prove their correctness and efficiency? LLM-guided design of optimisation heuristics (such as AlphaEvolve) is purely empirical. Automated theorem provers with LLMs prove given statements. So far, there has been little evidence that LLMs can do both: design an algorithm and guarantee its efficiency by a mathematical proof. We present a staged pipeline modelled after research methodology in design and analysis of evolutionary algorithms. The agent proposes black-box optimisation algorithms, and Lean guards filter out flawed designs. The agent then defines a potential function and proves drift bounds that guarantee an expected runtime improvement over the baseline algorithm. At no point in the pipeline are the algorithms compared empirically. The agent generates a black-box optimisation algorithm with expected runtime $O(n^2)$ on a CycleUncover problem, where the classical (1+1) EA needs runtime $e^{\Omega(n)}$. The pipeline also designs and analyses a black-box optimisation algorithm for integer-valued submodular minimisation with expected runtime $O(n^{2+2c})$, and it matches the optimal order $O(n^2)$ on LeadingOnes. Across 8 problem classes, 12 of 15 runs with frontier models complete the pipeline with a machine-checked expected-runtime bound. An ablation study shows that removing the staging and asking the agent to zero-shot an algorithmic design with a runtime guarantee leads to a copy of the seeded baseline algorithm (random search) or to incomplete proofs. Our study suggests that machine-checked specifications in Lean can replace empirical evaluation in open-ended algorithm discovery. To the best of our knowledge, this is the first example of an automated pipeline that designs efficient black-box optimisation algorithms with machine-checked runtime bounds in Lean.

---


### 363. [Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations](https://arxiv.org/abs/2610.35598)

**<font color=#1a73e8>作者：</font>** Zongyuan Sun, Shuai Zhao, Ke Shu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) provide reliable external knowledge for multi-hop factual reasoning with large language models (LLMs), yet most KGs in real-world domains such as finance and industry lack question--answer (QA) annotations. Without such annotations, existing methods struggle to improve LLM graph reasoning: training-free agents cannot improve their exploration through interaction; reinforcement learning (RL) agents depend on QA data annotated by humans or synthesized by closed-source models; and training data is typically built offline, so its topology mix is fixed and cannot follow the agent's ability. We propose Evolve on Graph (EoG), a framework that lets an LLM self-evolve its graph reasoning without any QA annotations. Through Graph Self-Play, a single LLM alternates between a Proposer that poses questions and a Solver that answers them. To make questions verifiable, Symbolically Verifiable Topology Synthesis (SVTS) samples reasoning topologies on the KG and executes the corresponding first-order logic queries, yielding topology skeletons with correct and complete answer sets; guided by a skeleton, the Proposer explores the graph to pose a multi-hop question. To let task topologies follow the Solver, a Boundary-Aware Graph Curriculum rewards the Proposer by the Solver's score variance, keeping questions at the Solver's capability boundary so that complex topologies enter training as the Solver improves. On six benchmarks over Freebase, Wikidata, and an industrial KG, EoG consistently outperforms prompting-, retrieval-, and agent-based methods, showing that LLM graph reasoning can improve through self-play without QA annotations. Our code is available at this https URL

---


### 364. [ArchiveLens: A Generative Spatial Knowledge Framework for Semantic Reconstruction of Historical Maps](https://arxiv.org/abs/2610.35606)

**<font color=#1a73e8>作者：</font>** Yanan Wu, Yalin Yang, Chengbin Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Historical maps contain dense morphological and semantic information about past urban environments, but many digitization workflows focus primarily on extracting geometry, and do not capture cartographic semantics such as building use and construction materials. This study introduces ArchiveLens, a generative spatial knowledge framework that operationalizes historical maps as entity-centric, machine-queryable geospatial databases. The pipeline decouples morphological and semantic reconstruction through three stages: tiled YOLOv11-seg instance segmentation for building footprint extraction; deterministic material classification via hue, saturation, and value (HSV)-based color thresholds; and localized attribute parsing using a quantized vision-language model constrained by domain-specific prompts. Extracted entities are integrated into a hybrid Spatial-Temporal Retrieval-Augmented Generation (ST-RAG) architecture that combines dense semantic retrieval with symbolic spatio-temporal filtering and mandatory provenance grounding. Applied to 445 georeferenced Sanborn map sheets of Chicago (1918-1950), the framework achieves high geometric and semantic accuracy. Beyond performance, ArchiveLens advances GIScience by formalizing historical cartography as structured spatial knowledge representation, allowing researchers to query building attributes and compare spatial patterns across map sheets and years.

---


### 365. [Hierarchical Skill Evolution for Coding Agent](https://arxiv.org/abs/2610.35616)

**<font color=#1a73e8>作者：</font>** Jun Gao, Yun Peng, Changhai Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills provide agents with reusable experience to guide future decisions without modifying the underlying model. However, coding trajectories are often entangled with task- and repository-specific contexts, making it challenging to distill procedural skills that generalize across diverse coding environments. To address this challenge, we present Hierarchical Skill Evolution (HSE), which progressively distills procedural knowledge from coding trajectories through hierarchical evidence aggregation. HSE first extracts task-level evidence from individual trajectories, then aggregates recurring evidence within the same repository to form repository-specific skill candidates, and finally consolidates consistent patterns across repositories into transferable skills across repositories. The evolution is driven by an external writer-evaluator loop that generates and assesses skills while keeping the underlying coding model frozen. The loop externally updates the writer and evaluator policies to improve subsequent skill generation and assessment. This hierarchy progressively filters task-specific details while preserving procedures that generalize across diverse coding environments. Successful trajectories yield reusable guidance for future tasks, while failed trajectories reveal recurring failure modes that guide avoidance and recovery. We evaluate HSE on SWE-bench Verified and DeepSWE, using GLM-5.2 across Pi and Claude Code harnesses and GPT-5.5 and Opus 4.8 with Pi. Across both benchmarks, 10 skills evolved solely from SWE-Gym improve coding performance across all evaluated settings, demonstrating transfer across benchmarks, coding models, and agent harnesses. We further evolve the skill library from target-benchmark trajectories without verifier feedback, relying solely on the learned evaluator for candidate assessment and achieving additional gains through benchmark-tailored skills.

---


### 366. [Adversary Brains: Hypothesis-Based Logical Signatures for Threat Actor Detection with LLMs](https://arxiv.org/abs/2610.35624)

**<font color=#1a73e8>作者：</font>** Gadi Evron  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An adversary brain is an LLM-based model of a threat actor's behavior, held as an evolving logical signature: a hypothesis with enough structure that data can test it continuously, without a person re-interpreting it each time. Rather than any single observation, such as an IoC (Indicator of Compromise), it is the arrangement that becomes a detection, or intelligence, mechanism. Where YARA matches a file and Sigma matches a log line, an adversary brain matches the activity pattern of a campaign or threat actor. This is based on an intelligence analysis technique called Analysis of Competing Hypotheses (ACH), which the design lifts from the limitation of a few hypotheses at a time, to thousands, and then also operationalizes it for continuous detection purposes. Language models make the concept, and scale, practical: they turn prose reports into brains, judge matches, and drive the loop that keeps brains current. A partial pattern in a brain can also match a new value, such as a fresh C2 (command and control) domain name, assisting with the discovery of new indicators, and turning unknown unknowns into known unknowns, and potentially into knowns.
The author would like to thank Ryan Moon for the collaboration, and Sounil Yu, Chris Inglis, Thomas Roccia, Marius Benthin, Israel Grimberg, Michal Kamensky, Justin Borland, Brandon Levene, John Hultquist, and John Bambenek for their feedback and assistance.

---


### 367. [Offline Language-Based Support System for Tactical Decision-Making in Air Combat Operations](https://arxiv.org/abs/2610.35635)

**<font color=#1a73e8>作者：</font>** Joao P. A. Dantas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An offline language-based support tool is presented to assist pilot training and tactical decision-making in air combat operations. The system, named MATE (Mission Assistant for Training and Evaluation), applies retrieval-augmented generation (RAG) to answer natural language questions using content extracted from doctrinal and tactical manuals. Built entirely with open-source components, it performs text preprocessing, embedding generation, semantic search, and language generation locally, ensuring full offline functionality. The tool was evaluated by three Brazilian Air Force fighter pilots, who rated the answers produced with three open-weight language models (Llama 3.1 8B, Qwen 2.5 14B, and Mistral NeMo 12B) to five tactical questions derived from a publicly available air combat manual. Average ratings ranged from 4.00 to 4.40 on a five-point scale, with Mistral NeMo 12B obtaining the highest score, and the pilots rated the response time of the tool as fully adequate compared to manual search. The relevance of the retrieved content was identified as the main point for improvement. Potential applications are discussed in onboard mission systems, flight simulators, and training environments.

---


### 368. [Improving JEV Entailment Reranking with Span Readouts and Selective Adaptation](https://arxiv.org/abs/2610.35654)

**<font color=#1a73e8>作者：</font>** Haocheng Mei, Yuchuan Tian, Ye Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> JEV decision models pair a language model backbone with a lightweight scoring head to select among natural-language options. Direct selection compares candidate answers within one request, whereas entailment reranking evaluates each candidate in a separate natural language inference (NLI) request over fixed relation options. We examine whether the readout and adaptation choices used for direct selection remain effective for cross-request reranking. We combine a mean-span readout with selective backbone adaptation. Mean-span pooling replaces the option-ending pointer with an average of the contextualized states inside each NLI option, without adding head parameters. Selective adaptation retains low-rank updates in attention and gated DeltaNet projections while removing feed-forward adapters. On MC11, which averages accuracy over eleven reranking configurations from seven sources, selective adaptation improves NeoHorse-1-4B accuracy over the all-module baseline while cutting trainable parameters by more than half, and mean-span pooling yields further consistent gains at the same parameter count.

---


### 369. [A Hybrid Framework for Explainable Aviation Risk: Causal Chain Extraction from Safety Reports with Physics-Based Failure Quantification and Interventional Analysis](https://arxiv.org/abs/2610.35658)

**<font color=#1a73e8>作者：</font>** Yutian Pang, Yifang Tian, Jiacheng Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aviation authorities hold decades of accident reports whose narratives record how investigators reconstructed each accident. Computational work on these archives has mostly sorted reports into fixed taxonomies. In this work, we propose a hybrid framework in which a text-based corpus identifies the leading factors of a failure mode. Physics-based models then quantify how likely that failure is at a stated operating point. Ordered causal chains extracted from 56,202 American accident reports with a local large language model aggregate into a causation knowledge graph. On an evaluation sample of 2,000 reports, the chains recover 90.8% of investigator-flagged causes. Each physical factor whose drivers the record carries receives an occurrence model calibrated to the accident population. A leaky noisy-OR fitted to the corpus combines the factors into a failure mode probability that supports intervention. For engine power loss, the carburetor icing model separates 1,205 icing accidents from other accidents using temperature and dewpoint alone, reaching 0.61 in area under the receiver operating characteristic curve against a density ratio ceiling of 0.64. Routine weather hours give no valid control, because flying concentrates in fair weather. On later years the physics adds 0.03 to that area for occurrence and nothing for severity, so its value lies in interpretability. On four named accidents, abduction gives a probability of necessity of 0.29 to 0.50 for the heat omission, under monotonicity. The Fast Causal Inference algorithm does not license the largest backdoor adjustment on the learned networks.

---


### 370. [Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671)

**<font color=#1a73e8>作者：</font>** Yao Huang, Zhiyuan Zeng, Yu Wang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive less scrutiny regarding frontier risks. To address this gap, we present an independent safety evaluation of DeepSeek V4.1 Flash-1017, the latest version of V4.1 Flash that departs from V4 with a new architecture, scaled-up training, and strong agentic capabilities. Drawing on the EU General-Purpose AI Code of Practice, we evaluate the model across 34 benchmarks, including 5 in-house suites, spanning evaluation integrity, loss of control, and harmful manipulation. Conforming to the AEF-1 standard, we compare V4.1 Flash-1017 against V4.1 Flash, earlier DeepSeek V4 models, and leading closed-source systems (GPT-6 Astra, GPT-5.6 Sol, and Gemini 3.8 Flash). Overall, V4.1 Flash-1017 shows substantial safety improvements over the V4 generation and approaches or matches leading closed-source baselines on several dimensions, while still exhibiting notable behaviors that warrant continued attention. Building on our findings, we highlight three key observations and recommendations. First, because safety can shift and even regress across minor updates, developers should integrate safety evaluation into incremental releases. Second, as final-turn outputs and end-state checks alone cannot reliably detect loss-of-control behaviors, deployments require process-level observability across both reasoning traces and action logs. Third, because public benchmarks elicit strong evaluation awareness and face data contamination risks, developing private benchmarks is essential for trustworthy frontier evaluation.

---


### 371. [Adapting LLM-SC to Living Sacred Heritage: Domain-Specific Extraction, Semantic Networks and Human Evaluation on Pashupatinath Temple Reviews](https://arxiv.org/abs/2610.35685)

**<font color=#1a73e8>作者：</font>** Hari Sitaula, Manish Sakhakarmy, Pujan Pant 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) pipelines can turn visitor reviews into structured data, but generic schemes may miss rituals, sacred spaces, cultural restrictions and emotionally mixed experiences at living sacred heritage sites. We adapted the LLM-Social Computing (LLM-SC) framework to Pashupatinath Temple, Nepal, by specifying a 12-type entity taxonomy (four original LLM-SC types plus eight sacred-heritage types), four relation types and nine aspect-sentiment dimensions in a GPT-4o extraction prompt, which was applied to a fixed random sample of 2,500 English-language Tripadvisor reviews from a processed corpus of 3,939. The exports contain 11,286 entity, 6,232 aspect-sentiment and 5,590 relation records, covering 2,485, 2,487 and 2,433 reviews, respectively; the eight added sacred-heritage types account for 64.8% of entity records. Against an adjudicated two-annotator reference for 200 reviews, exact normalized surface-and-type matching gave provisional entity scores of 41.0% precision, 21.8% recall and 28.4% micro-F1. Aspect-presence F1 was 53.6% and end-to-end aspect-plus-polarity F1 was 42.6%. Human adjudication supported 153 of 194 first-listed relation candidates (one per review; 78.9%), a candidate-level rate that does not estimate relation recall or whole-graph precision. The contribution is a culturally grounded, domain-specific adaptation with component-wise human evaluation and explicit reproducibility and generalization limitations.

---


### 372. [EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation](https://arxiv.org/abs/2610.35690)

**<font color=#1a73e8>作者：</font>** Yitao Xiao, Xu Zhang, Ye Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serving web queries at scale with multi-agent systems requires jointly configuring large language models, collaboration modes, agent counts, interaction rounds, and skills. However, the resulting configuration space grows combinatorially, while sparse execution rewards provide limited fine-grained supervision for interdependent planning decisions. We propose EvoRouter, a self-evolving multi-agent routing framework driven by insight-guided on-policy distillation. A dedicated expert periodically synthesizes performance-cost feedback from configuration trajectories across tasks into reusable conditional routing insights about capability requirements, returns from resource scaling, and interactions among configuration choices. A privileged teacher combines these evolving insights with current execution feedback to provide dense token-level supervision for the router's own planning trajectories through on-policy distillation. Cost-aware reinforcement learning jointly optimizes task performance and computational cost. Together, these training signals internalize execution insights into the routing policy. The updated policy generates new trajectories that support subsequent insight extraction, forming an execution-driven self-improvement loop. We evaluate EvoRouter on 19 in-domain datasets spanning five domains and two out-of-domain benchmarks. EvoRouter achieves an average in-domain accuracy of 68.69%, outperforming the strongest routing baseline by 7.23 percentage points while reducing inference compute cost by 50.95%. Our code is open-sourced at this https URL.

---


### 373. [Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering](https://arxiv.org/abs/2610.35694)

**<font color=#1a73e8>作者：</font>** Duc-Vinh Tran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational QA systems should fix errors when users push back and signal which answers to trust. We split each follow-up into its speech act (re-ask, agree, or challenge) and its payload (an answer string, correct or not), and measure four confidence signals on the same transcripts: verbalized confidence, length-normalized likelihood, a frozen hidden-state probe, and P(True). Answers change when the user supplies an answer string and almost never under the speech act alone: in every retained full-size cell, the correct answer converts at least four times as many wrong answers as re-asking or agreement. The four signals disagree. On Qwen2.5-7B the frozen probe rises with answer persistence rather than truth; this holds on held-out questions, with Llama-3-8B (cleaned answers) as support, but not on four other models. Among 81 Qwen2.5-7B errors that survive one re-ask, re-asking, a fresh chat, or abstain repair almost none, while a gold answer repairs 75-95%. In two preregistered replications, every repair rate without an answer string stays below 0.15; a larger post-hoc rerun excludes 0.15 except for the empty elicit. With BM25 TriviaQA evidence, sentences that contain the answer repair 67-76% of persistent errors versus at most 12% when they do not. An end-to-end contain-gate cuts harm on TriviaQA, but a deployable gate that does not know the gold answer repairs few errors.

---


### 374. [Reflective Computing](https://arxiv.org/abs/2610.35696)

**<font color=#1a73e8>作者：</font>** Md Haseen Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive technology is increasingly built for speed, and generative AI now answers before a question is fully formed. Yet the capacity to pause, interpret and decide for oneself is central to wellbeing, learning and meaningful use. HCI has named paradigms for sensing emotion, changing behavior, calming attention and tracking the self. However, none of them takes human reflection, and the slowing down it requires, as its organizing aim. This article defines that paradigm, reflective computing, and derives it from what thirty years of designs lack. We analyzed 134 interactive systems from 17 ACM venues (1996-2026) in two phases. First, an abductive gap analysis read every system against reflection theory, and seven recurring gaps defined seven dimensions, namely tempo agency, invitational form, interpretive openness, reflective depth, temporal span, protected idleness and ethical non-extraction. Second, two independent coders scored every system with a codebook (Krippendorff's alpha 0.67 to 0.84 for five dimensions; ICC 0.82 for the overall score). The system sets the pace in 51 designs, 74 support only momentary use, only 12 scaffold reflection beyond description, and 56 papers are silent on the inner states they collect. No system expresses all seven dimensions strongly, and only 20 meet the definition. Slow and experience centered design comes closest, whereas persuasive technology and human-AI interaction score lowest. Factor and latent class analyses reveal two cultures of reflection, one working through form and the other through scaffolded thought, which only one system combines. Systems that let people set the pace score markedly higher, even with paradigm and form controlled (odds ratio 13.5). Hence, reflective computing is proposed as a paradigm whose aim is a human capacity rather than a system function, and which treats slowness as valuable only when people choose it.

---


### 375. [MiRL: Error-Targeted Reinforcement Learning for Correcting Terminal Agent Misbehaviors](https://arxiv.org/abs/2610.35697)

**<font color=#1a73e8>作者：</font>** Runchu Tian, Zaid Khan, Zun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Error-targeted learning gives a legible way to improve a model: identify specific weaknesses of the model, train the model to fix these weaknesses, and check whether the weaknesses are fixed. We study how to apply error-targeted learning to terminal agents, which solve long-horizon tasks specified in natural language by interacting with a command shell. Existing error-targeted methods are designed for single-turn tasks, and existing analyses of agent failures are used to evaluate and debug agents rather than to train them. We propose Misbehavior-driven RL (MiRL), which first profiles the errors of a policy to find generalizable misbehaviors: kinds of wrong steps that recur across many environments. MiRL then trains the policy with RL, starting rollouts at the steps where these misbehaviors occur and rewarding a rollout only if it passes the tests and avoids the misbehavior. On Qwen3.5-4B, eight misbehaviors account for 52.1% of wrong steps. After training with MiRL, the policy repeats the measured misbehaviors 43% to 57% less often on average on unseen prefixes. MiRL outperforms TMax-4B on Terminal-Bench Lite (51.8% vs. 47.4%) and matches it on Terminal-Bench 2.1 (21.3% vs. 20.6%), while using 35% of its rollouts. These results show that error-targeted learning can be applied to realistic, long-horizon terminal tasks.

---


### 376. [From Self-Confidence to Statistical Accuracy: Scaling Human-in-the-Loop Evaluation with Direct and LLM-Assisted Auditing](https://arxiv.org/abs/2610.35698)

**<font color=#1a73e8>作者：</font>** Harine Choi, Chenchen Kuai, Zihao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For large language models (LLMs) and multimodal large language models (MLLMs), model-reported self-confidence is often miscalibrated, yet it may still be useful for efficient evaluation. At the same time, LLM-as-a-judge offers a scalable alternative to direct human auditing, but its practical benefit depends on calibration quality and inference cost.
This paper develops a unified statistical framework for both evaluation routes under alternative sampling strategies. For direct auditing, confidence-stratified sampling is used to recover population accuracy from partially verified outputs without requiring calibrated confidence. Finite-sample uncertainty is characterized, and the analysis shows how highly uneven confidence strata affect audit efficiency and label allocation. For judge-assisted evaluation, the judge is modeled through sensitivity and false-positive rate, yielding an error-corrected estimator with calibration uncertainty. The two routes are then compared through human-label and total-cost efficiency boundaries.
Experiments on MMLU-Pro and MMMU-Pro show that miscalibrated self-confidence can still support statistically valid stratified auditing. Under highly imbalanced confidence distributions, proportional allocation substantially reduces estimation error relative to equal-per-stratum allocation. For judge-assisted evaluation, only a small subset of target--verifier pairs satisfies the idealized human-label efficiency condition, and automated inference costs can further limit potential savings. These findings clarify the statistical and economic conditions under which confidence-guided auditing and automated verification are useful.

---


### 377. [Explainable Multimodal AI Approach to Reduce Unnecessary Breast Biopsies](https://arxiv.org/abs/2610.35704)

**<font color=#1a73e8>作者：</font>** Sadam Hussain, Mansoor Ali, Daly Betzabeth Avendaño-Avalos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, there has been rise in multimodal vision-language models for computer-aided diagnosis (CAD), yet their application in breast diagnosis, particularly for predicting biopsy outcomes remains limited. This study presents a multimodal vision-language approach, incorporating Grad-CAM as an Explainable AI (XAI) technique, to predict benign tumors in patients recommended for biopsy, especially those classified as BI-RADS 4 and 5. A novel multimodal framework was devel- oped using Vision Transformer (ViT) for imaging feature extraction and DeBERTa-V3-Large for textual embeddings. The model was trained and evaluated on a comprehensive in-house dataset comprising 1,632 patients, each with four mammography views and a corresponding radiology report. The features of both modalities were extracted independently and fused by late fusion before classification. Grad-CAM was used to generate visual explanations highlighting key regions influencing model predictions. The proposed model demonstrated high sensitivity 90%, 95%, 99%, and 100% with corresponding specificities of 40%, 36%, 18%, and 11%, respectively. The best AUC achieved was 0.72 by multimodal approach on the test set, outperforming the image only (0.66) and text-only (0.68) baselines. The proposed multimodal architecture, enhanced with Grad-CAM, demonstrates a strong potential to identify benign tumors among high-risk patients, offering interpretable insights and thereby helping reduce unnecessary biopsies, patient anxiety, and healthcare costs.

---


### 378. [Quantitative Generalization Bounds for Multi-Layer Transformers: A Few Long Strings can Beat Many Short Ones](https://arxiv.org/abs/2610.35715)

**<font color=#1a73e8>作者：</font>** Marius Henry, Michael Rizvi-Martel, Michael Hahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models exhibit an astonishing capacity to generalize to longer and more difficult problem instances than those seen in training. However, theoretical understanding of this phenomenon still lags behind. Unlike most machine learning models, the generalisation abilities of transformers inherently require considering two axes. On one hand, one must examine in-distribution statistical generalisation, which concerns the ability of a model to broaden a function from training samples to novel samples of the same distribution. On the other hand, given the sequential nature of language data, one must also consider length generalisation, which reflects whether a model trained on inputs of a given length can extrapolate to longer this http URL two notions have mostly been studied separately, leaving open how they interact. In this work, we give a joint treatment of both axes for fixed-precision transformers. We give generalisation guarantees in terms of the parameter sizes of the involved models, as well as the quantization space and the alphabet size that supply the sequences. Finally, we illustrate how the requirements in the sample count and training length trade off. In particular, we find that increasing training length can be exponentially more efficient than increasing the sample size. Experiments support predictions of the theory.

---


### 379. [Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO](https://arxiv.org/abs/2610.35716)

**<font color=#1a73e8>作者：</font>** Shurun Li, Michael Hua Wang, Haibo Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards trains on cheap checks, such as unit tests, that a policy can learn to game, while a stronger check is too expensive to run on every rollout. We study how to spend a limited strong-verifier budget in GRPO, separating which weakly passing rollouts to audit from what reward a caught hack receives. At a fixed policy state with centered advantages, the expected update depends on a design only through each rollout's marginal audit probability and correction; reflecting a caught hack's reward about the failure reward negates the advantages of an all-hack group; and auditing whole groups with the fewest weak passes first (low-pass budgeted audits, LB) minimizes the advantage mass left on hacks among pass-count designs with a fixed correction when a label's value falls with the pass count. We tested this analysis in actual LLM training: from each run's starting state, the sign of this mass on a frozen panel predicted whether hacking would be suppressed in 33 of 39 runs, including 13 of 16 preregistered ones. In LeetCode (Wong et al., 2026) and Countdown-Code (Khalifa et al., 2026), LB drives hacking to near zero, while random audits with the same penalty and budget do not and use more labels. We also find that the randomness of the update affects training: in Countdown-Code, two unbiased corrections, per-item reward-level IPW and a group-level advantage correction, bring hacking down too but end 6.1-11.8 and 8.0-11.5 points lower in held-out accuracy than LB at the same budget. A full audit, which the group-level correction reproduces in expectation, stays within about two points of LB in three seeds, while LB uses 28% of its labels, and allocating the same correction by pass count recovers most of the loss (one seed). Training outcomes thus depend not only on the expected update but also on the randomness of its estimate.

---


### 380. [Can JEV Support Clinical Trial Criteria Assessment?](https://arxiv.org/abs/2610.35721)

**<font color=#1a73e8>作者：</font>** Mengxian He, Ziyue Gao, Chun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical trial prescreening requires distinguishing unmet conditions from insufficient evidence in patient records. Given patient records, criterion questions, and predefined answer options, we retrospectively compared JEV, a non-generative decision model returning native option probabilities, with schema-constrained Qwen Flash across 2,048 test patient-condition pairs from TrialGPT and question-answer datasets derived from MIMIC-III and MIMIC-IV, all evaluated under strict Zero Data Retention (ZDR) policies to ensure clinical data privacy. Both models assessed conditions individually or in batches sharing the same patient context, with performance measured against reference labels. In batch mode, JEV and Qwen achieved similar macro-F1 scores on TrialGPT (0.652 vs. 0.660) and MIMIC-IV (0.807 vs. 0.814), whereas JEV substantially outperformed Qwen on MIMIC-III (0.768 vs. 0.534; $\Delta$ = +0.234, 95% CI: 0.187-0.281). This advantage largely reflected higher recall for conditions labeled as having insufficient information (56.3% vs. 9.9%). Across all three datasets, JEV also had lower observed median job latency (1.18-1.40 vs. 2.80-8.90 s) and 53%-74% lower estimated cost per condition. These findings position JEV as an initial assessment component that provides criterion-level judgments and flags potential information gaps for review. JEV's observed errors in interpreting clinical evidence underscore the need to verify its outputs against patient records before they inform eligibility decisions.

---


### 381. [SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy](https://arxiv.org/abs/2610.35743)

**<font color=#1a73e8>作者：</font>** Mingqian Feng, Xiaodong Liu, Weiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing jailbreak attackers fall into two classes: static planners fix their single- or multi-turn adversarial plans in advance, remaining simple but losing sight of the victim's replies, wasting turns and limiting transferability; interactive generators read each victim reply to generate the next-turn attack but require in-loop evaluators for success signals or hints, incurring substantial costs and inflated performance. Bridging this gap, we propose SEMA-Auto, a sighted and efficient multi-turn attacker with autonomy, interacting with the victim model and terminating the session by itself upon success. To stabilize its behaviors and boost its capabilities, SEMA-Auto is trained in two stages. Synthetic bootstrap tuning installs the notion of attack targets and conforming decisions by fine-tuning the base model with bootstrapped trajectories. Decision-supervised reinforcement learning then optimizes two objectives jointly yet separately, reinforcing the attack with higher jailbreak reward while supervising the decision at each turn against an absolute target. Our method achieves state-of-the-art (SOTA) attack success rates (ASR) across multiple datasets, victims, and judges, outperforming all static and interactive baselines, within almost the fewest turns, demonstrating both effectiveness and efficiency. For example, SEMA-Auto performs a $76.0\%$ ASR@1 within an average of $3.0$ turns against DeepSeek-V4-Flash on AdvBench, while the best static baseline is $54.8\%$ with fixed $7$ turns and the best interactive baseline is $43.8\%$ in $3.7$ turns. Against safety-hardened frontier models, GPT-oss-120B, GPT-5.4, Claude-Haiku-4.5, and GPT-6-Astra, our counter-trained attacker achieves an average $59.6\%$ ASR@1 on HarmBench, $13.8\%$ over prior SOTA. Our code is available at: this https URL

---


### 382. [Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767)

**<font color=#1a73e8>作者：</font>** Tingzhu Bi, Xun Zhang, Jinglin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design beats letting a capable model investigate on its own. We compare three simple harnesses that prescribe none of the model's calls (one call over an evidence package, a SQL agent and the Codex coding agent) with five published LLM RCA agents and with statistical and causal methods on RCAtlas, 90 validated cases from eight public datasets, across six models and three reasoning efforts. The simple harnesses are the most accurate (PR@1 65-77% on three mid-tier models), ahead of the published agents (16-53%) and the non-LLM methods (6-39%), on every model on which both families were run. The published agents fix from a tenth to all of their model calls in the program, and a case study shows how these prescriptions skip the decisive evidence. A stronger model mainly improves reliability, a multi-turn harness mainly improves aptitude, and more reasoning effort changes accuracy by a few points at most while multiplying the time by up to seven. Among runs more accurate than the best non-LLM method, every Pareto-optimal run in cost or time uses a simple harness.

---


### 383. [A Unified Arena for LLM Agents across Diverse Eurogame](https://arxiv.org/abs/2610.35773)

**<font color=#1a73e8>作者：</font>** Fengrui Zhang, Xiang Li, Ruomeng Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution frameworks leave unclear which competitive advantages persist across settings. We introduce DECE (Diverse Eurogame Competitive Environments), a unified arena spanning ten Eurogames with shared interfaces and evaluation protocols. These games combine lasting strategic commitments, competition over shared resources, and multiple routes to victory. Our primary study evaluates 12 model-harness configurations, spanning nine models and four execution harnesses, in 480 three-player matches across ten games. The main and supplementary studies comprise 1,032 completed matches in total. These comparisons reveal broad cross-game ranking agreement alongside game-specific strengths. Matched studies show that the same model can perform differently across execution harnesses, adding another source of variation to these profiles. These performance advantages do not consistently translate into better token or cost efficiency, making resource use an additional consideration when comparing configurations. Together, the findings support evaluating complete agent configurations by both their competitive performance across games and the resources needed to achieve it.

---


### 384. [Selective Tie Learning: Mitigating Spurious Correlations in Preference Optimization](https://arxiv.org/abs/2610.35787)

**<font color=#1a73e8>作者：</font>** Christian Moya, Purav Matlia, Elliott Thornley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference optimization can learn spurious correlations, and augmenting the preference data with ties (equally preferred responses) can reduce spurious reliance. However, ties differ in their corrective effect, making their selection for augmentation important. For log-linear policies, we derive each tie's influence on spurious reliance and show that taking the largest predicted reductions is first-order optimal among subsets of equal size. Computing these influences requires knowledge of the spurious features and the curvature of the training objective, which is often unavailable or expensive to estimate. To this end, we explore using the magnitude of a tie's implicit reward margin and characterize the conditions under which it is a useful proxy for predicted influence. To test the theory and its qualitative transfer to neural models, we estimate influence with a counterfactual proxy for spurious reliance and use a generalized Gauss--Newton approximation to curvature for language models. Across log-linear policies, neural models, and large language models, our selection rules consistently achieve comparable reductions in spurious reliance with fewer ties than uniform selection.

---


### 385. [Quantifying Claim Smoothing by LLM Research Agents](https://arxiv.org/abs/2610.35793)

**<font color=#1a73e8>作者：</font>** Tiasa Singha Roy, Manya Wadhwa, Greg Durrett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that LLMs produce long-form research reports that read as confident syntheses but which fail to accurately reflect the underlying documents. We call this failure smoothing. In collapsing diverse and potentially conflicting sources into a single narrative, the model discards the evidential "jaggedness" of its corpus and asserts conclusions more decisive than the citations can support. We introduce a claim level scoring pipeline, SmoothScore, to quantify this effect. Our pipeline extracts key conclusive claims from model generated reports, then finds evidence relevant to each claim and clusters that evidence along high level aspects. Finally, each claim is scored with respect to the evidence to quantify the degree of smoothing done by the agent. Across 7 systems and 4 datasets, we find that agents consistently produce stronger claims than warranted.

---


### 386. [FOCUS: Active Critic Learning for Long-Horizon Language Model Agents](https://arxiv.org/abs/2610.35801)

**<font color=#1a73e8>作者：</font>** Zhengping Jiang, William Jurayj, Liaoyaqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimates can be inaccurate, while estimating intermediate values with repetitive continuation samples from points within a trajectory incurs substantial costs. To mitigate these issues, we introduce FOCUS, an RL method that uses selective branching to help the critic network learn its value estimator. The rollout controller facilitates active learning for the critic by sampling continuations from states that are expected to most reduce the critic's estimation error. These refined value estimates then score the segment between consecutive states with a TD($\lambda$) advantage, while the sampled evidence supplies training targets for the critic. FOCUS supports long-horizon agentic reinforcement learning through a modular context-management interface that decouples context management from rollout allocation. Our experiments show that using compaction-induced segment boundaries for value estimation and credit assignment, FOCUS outperforms GRPO and VinePPO with matched per-step generation budgets on legal reasoning, deep search, and code localization benchmarks, improving held-out accuracy at Qwen3.5-9B scale by 7.2 points over the strongest baseline on BrowseComp-Plus (55.4 vs. 48.2) and by 4.1 points on DeonticBench (56.5 vs. 52.4).

---


### 387. [Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models](https://arxiv.org/abs/2610.35804)

**<font color=#1a73e8>作者：</font>** Aidar Myrzakhan, Zhiqiang Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response. Efficient generation depends not only on which tokens are easy to predict, but also on how committing to them helps predict the remaining positions. A highly predictable token may provide little useful context, while revealing a less predictable token can help several other positions become predictable sooner. We propose dSpark, a new schedule distillation-based framework for learning when to commit tokens for faster diffusion language generation. To achieve this, we construct unmasking schedules that prioritize tokens whose reveal makes other positions easier to predict, reducing uncertainty earlier in decoding. We then distill these schedules into the model to enable faster parallel sampling, with a KL-divergence regularizer to help preserve generation quality. We extensively evaluate our approach across mathematical reasoning and code generation tasks. On GSM8K, our method achieves remarkable 10.12$\times$ and 5.12$\times$ speedups over the various baselines on LLaDA-8B-Instruct and Dream-7B-Instruct, respectively, while maintaining superior task performance. Our code is available at this https URL.

---


### 388. [Back to Basics: A Skill-Centric Approach to Generalist Web Agents](https://arxiv.org/abs/2610.35823)

**<font color=#1a73e8>作者：</font>** Minh Pham-Dinh, Md Farhan Ishmam, Hernan Yupanqui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Browser agents do not just need more practice. They need to practice the right things. We introduce MiniWeb, a realistic miniature of the web comprising 65 interconnected websites across 15 domains, where agents navigate, search, and transact as people do. Its 369 human-annotated tasks cover everyday workflows and label 37 reusable interaction primitives grouped into 7 skill families, allowing us to diagnose which skills fail rather than only whether a task succeeds. Benchmarking ten open-weight agents, we find that drag & gesture is consistently the weakest family, with no agent solving more than 24% of its instances. To address this gap, we introduce MiniWebGen, a framework that autonomously generates verified, skill-centric training data from MiniWeb. Fine-tuning Qwen3.5-4B on just 3.1K verified trajectories improves single-primitive success by 24.9pp across 13 unseen websites, with gains across every skill family. However, these trajectories teach short-horizon interactions, which do not directly translate to full-task success. We build on this result with MiniWebAgent, which pairs the trained executor with a planner that decomposes full tasks into the skill-level steps it learned to perform. This approach improves task success by 19.4pp points on unseen MiniWeb sites and transfers to external benchmarks, with gains of 9.3pp on WebArena-Lite, 16.1pp on Online-Mind2Web, and 20.0pp on WebVoyager, without training on their trajectories. We provide a simple recipe for compact browser agents: practice reusable skills directly, then compose them to solve unfamiliar tasks.

---


### 389. [Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?](https://arxiv.org/abs/2610.35826)

**<font color=#1a73e8>作者：</font>** Mingyang Song, Mao Zheng, Zhiyuan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain limited in multi-option tasks. This leaves a central question: does Jev-style decision structure reduce selection bias? We address this question with a simple test that shuffles options while keeping question and candidate content fixed. Across two Jev versions, twelve Jev reproductions, and six generative LLMs, we trace individual answers through eight presentations and compare them with fixed-order repetition. On our primary collection of 1,700 questions from two benchmarks, Jev's accuracy varies by less than two percentage points, yet its cumulative failure set expands by 27--29\% relative to the original order, with first failures continuing into the final presentation. This loss of initial successes is substantially larger than under fixed-order repetition, even for highly repeatable Jev reproductions. Nor does Jev show a general advantage over the LLM baselines in preserving correct choices. Aggregation offers limited protection: voting yields modest gains for Jev, while even unanimous answers are frequently wrong. These results expose a gap between repeatable decisions and decisions that remain correct across equivalent presentations, showing why stable accuracy alone cannot establish resistance to selection bias.

---


### 390. [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829)

**<font color=#1a73e8>作者：</font>** Amine Lbath, Massih-Reza Amini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulnerabilities by working as a security expert would: they run analysis tools, explore the surrounding code, test hypotheses and weigh the evidence before forming their own judgement. This reasoning, however, spans many model calls, so that each verdict takes minutes of compute, far too long for real-time screening. Faster detectors, which fine-tune deep learning models or prompt an LLM for a direct verdict, are less accurate: they judge a function without the context an agent gathers, and an LLM's generated verdict is unreliable even when given some of it.
We present REVA (REal-time Vulnerability Analysis), an AI vulnerability detector that brings the security context and code understanding components behind agentic detectors into a single forward pass of an LLM. For each new function, REVA gives the LLM a pre-computed threat model of its module, lightweight static analysis findings and call-graph information. REVA leverages a trained probe to read the LLM's internal representations of the new function in this context. On PrimeVul's held-out test set, REVA on GLM-5.3-Flash reaches 60.0% accuracy in about one second per function. This matches VulTriage (59.2%), the state-of-the-art agentic detector, run on the same LLM, while being over 250 times faster and less than a tenth as costly. On the same prompt, the probe is 14% to 17% more accurate than the LLM's own direct verdict. Across three open LLMs, REVA is at least as accurate as VulTriage, and about 10% more accurate on two of them. An LLM's internal representations thus encode much of what agentic detectors obtain through reasoning.

---


### 391. [Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR](https://arxiv.org/abs/2610.35846)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem in connector-based Speech LLMs, where a trainable connector maps speech representations into a frozen large language model. We evaluate target-update construction and merging strategies for adapting the connector while preserving source-language performance. In single-target expansion, target-only fine-tuning and standard TIES merging learn new languages but cause severe source-language forgetting, while SSU-Wanda+TIES gives the best source-preserving trade-off. In multi-target expansion, update merging provides stable source retention, whereas recursive expansion can improve target adaptation under favorable orders but is highly order-sensitive. These results show that multilingual ASR expansion requires balancing target acquisition, source retention, and interactions among target-language updates.

---


### 392. [Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](https://arxiv.org/abs/2610.35847)

**<font color=#1a73e8>作者：</font>** Wei-Wei Zhang, Pengkai Wang, Yan Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware benchmark for evaluating multistage clinical reasoning across the cancer care continuum, using nasopharyngeal carcinoma as a defined disease context. Curated from longitudinal records of 405 patients across two cancer centers, the benchmark comprises 941 patient-phase units across six sequential care phases and 17,688 patient-specific atomic criteria spanning five evaluation dimensions, with each assessment strictly restricted to decision-time clinical evidence. Evaluating 30 general-purpose and medical LLMs revealed that strong diagnostic performance does not carry over to downstream care. We evaluated 30 general-purpose and medical LLMs, showing that high diagnostic performance did not translate into improved downstream care. Instead, the dominant failure modes reversed across phases. Explicit decision errors dominated anatomical staging at 48.2%, whereas decision omissions dominated initial work-up and post-treatment follow-up at 33.4% and 30.4%, respectively. In the evaluated model set, medically adapted models showed higher omission rates than general-purpose models. Moreover, varying query granularity exposes a critical specification trade-off: broad open-ended requests degrade Decision Quality across all 30 models, while more detailed, checklist-like prompts raise Decision Quality but reduce Evidence Faithfulness and Safety Adherence. Furthermore, NPC-RubricBench demonstrates that static diagnostic benchmarks are insufficient to ensure consistent clinical reliability over time, highlighting the importance of phase-adaptive safeguards in multistage medical AI.

---


### 393. [Do vision models know that three is three?](https://arxiv.org/abs/2610.35857)

**<font color=#1a73e8>作者：</font>** Ankit Sonthalia, Arnas Uselis, Seong Joon Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Do vision models encode the transition $2{\to}3$ the same way whether it appears in handwritten digits or in hand gestures, and do they "understand" that clean${\to}$dirty is the same transformation regardless of whether it is applied to a kitchen or a carpet? The linear representation hypothesis (LRH) answers this for language models: concept changes correspond to directions in (language) embedding space. In vision, the same concept can manifest in visually unrelated "regimes" that rarely co-occur: images of digits and hands do not share much in common in pixel space. To understand whether vision models still encode the underlying abstract concepts, we study 46 vision encoders across architectures, training objectives, and scales, on 10 concept families including numerosity, age, object identity, and MIT-States attributes. Within each regime, we find statistically significant concept directions near-universally across our tested models. However, two distinct regimes do not always share the same concept direction. Several models learn multiple linear structures for the same concept transition, split across regimes. We call this phenomenon "fragmented linearity": strong local linearity coexisting with near-absent global linearity. Fragmentation is, however, not fixed: models with stronger local linearity progressively escape it (local-global linearity correlated with $\tau \in [0.38, 0.89]$ across all concepts), and where global linearity does emerge, concept directions can transfer as linear probes across regimes.

---


### 394. [VibeVideoBench:Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864)

**<font color=#1a73e8>作者：</font>** Muxi Diao, Wenbin Xu, Lele Yang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a ruleconsistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-driven pieces to classroom lessons and paper explainers; each asks an agent, running in its native harness inside a sandbox, to deliver a finished MP4 with sound within one hour. Evaluation is hierarchical and evidence-based: program checks of the delivery spec, about 13k task-specific rubric checks traced to the requirements they enforce, and five quality dimensions anchored per task, judged by three VLM judge panels and validated with blind human preferences. Across nine frontier agent systems and 2,151 scored rollouts, the benchmark is far from solved: GPT-6 Astra and Claude Opus 5.5 lead clearly, yet even the best system fails a core requirement on about a quarter of tasks. Whether a video arrives at all matters as much as its quality, and three quarters of the lost videos are final renders started too late, run too slowly or never started. The judges agree with each other and with human preferences on system rankings, but only moderately on individual videos.

---


### 395. [Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](https://arxiv.org/abs/2610.35866)

**<font color=#1a73e8>作者：</font>** Xi Chen, Chongjian Ge, Yiran Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language modeling. Arena supports diverse research objectives within a shared experimental environment by separating admissibility from improvement: model quality and resource constraints determine whether a result qualifies, while the selected target measures progress among admissible results. We instantiate Arena in language model pretraining with nine targets spanning model, data, training, and inference efficiency, and evaluate seven research harnesses using two foundation models. Arena clearly differentiates existing harnesses across research objectives, with several sophisticated methods outperformed by our simple sequential search baseline, indicating substantial headroom in current auto-research systems. Beyond evaluation, Arena reveals a substantially broader frontier of model and system ideas aligned with active research directions. Reusing these discoveries in a new quality-driven search yields lower training loss under matched data and FLOPs and lower held-out BPB at the same model size. Together, Arena provides a common framework for benchmarking autonomous research and expanding its scope in language modeling. The code is available at this https URL

---


### 396. [Retriever-Free Retrieval: Navigating Documents with Decision Models](https://arxiv.org/abs/2610.35868)

**<font color=#1a73e8>作者：</font>** Chao Wan, Paul Jünger, Beixi Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While language models have become dramatically more capable, retrieval still largely relies on lexical matching or similarity in fixed embedding spaces. This creates a capability asymmetry: what the retriever fails to find, even the strongest generator cannot recover. We propose DecisionRAG, which brings the capabilities of pretrained language models to retrieval using decision models that jointly evaluate candidate branches in a single forward pass, without generating any tokens, and show that judging candidates in a shared context makes their relevance estimates comparable. Like a person browsing a library, DecisionRAG navigates the corpus's inherent structure from broad topics down to individual passages, deciding at each level which branches are worth exploring. Without task-specific training or a first-stage retriever, DecisionRAG outperforms dense retrieval with an 8B reranker by 13.8 R@1 points on MultiDoc2Dial and 17.4 Hit@1 points on Natural Questions. Across four benchmarks, including a corpus of 2.68 million Wikipedia paragraphs, retrieval takes just 0.7-1.8 seconds per query.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 397. [MOSAIC: Towards a Universal Latent Space for Computational Pathology Foundation Models](https://arxiv.org/abs/2610.33059)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dibaloke Chanda, Praveen Madiraju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) differ substantially in architecture, pretraining objective, training data and representation dimensionality, yet it remains unclear whether they learn fundamentally different feature spaces or alternative coordinate systems of a shared underlying representation. We present MOSAIC, a systematic study of latent-space similarity, alignment and interoperability across $12$ patch-level and $6$ slide-level PFMs. We first quantify representational agreement using complementary similarity measures and analyze how architecture, pretraining objective, network depth and magnification influence latent geometry. We then evaluate multiple alignment strategies for mapping independently learned representations into a common latent space. The resulting representations are evaluated through cross-model agreement, retrieval, geometry preservation, and downstream multiple-instance learning across molecular and morphological prediction tasks. MOSAIC provides a unified framework for studying whether heterogeneous PFMs can move beyond representational similarity toward a shared and functionally transferable pathology representation space. Our code, benchmarks and additional results are available at this https URL.

---


### 398. [Compression of Vision Foundation Models for Retinal OCT via Growing-Neural-Gas Codebooks and Graph-Guided Masked Image Modeling](https://arxiv.org/abs/2610.33340)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Yavari, Tilman Schmoll, Rainer A. Leitgeb 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models for retinal imaging are large and computationally demanding, limiting point-of-care deployment. We ask how much of such a model's downstream utility survives compression into a smaller network. We propose a topology-aware discretization framework that distills a continuous foundation model into a discrete codebook, then uses it as the reconstruction target for masked image modeling (MIM). It combines gradient-free codebook learning via Growing Neural Gas, which yields an adjacency graph over the codes, with a graph-distance soft cross-entropy loss that replaces one-hot MIM targets with topologically graded supervision. With student pretraining on 383 public Duke iAMD optical coherence tomography (OCT) volumes, the pipeline distills an 86M-parameter teacher into a 22M-parameter student with at least 3.6x fewer FLOPs. The student performs close to, and in some settings above, its teacher across three classification and two segmentation benchmarks, with the magnitude and direction of the difference depending on the teacher, task, metric, and student capacity. On the external OLIVES benchmark, it surpasses its MIRAGE teacher on every metric (98.06% vs. 95.22% balanced accuracy). It works with two Vision Transformer (ViT-Base) teachers, retinal (MIRAGE) and natural-image (DINOv3); with the out-of-domain teacher, the student outperforms it on retinal-layer segmentation, indicating that the added value of retina-specific pretraining is task-dependent: largest for segmentation, while a general-domain teacher is competitive for classification. These results yield compact retinal models potentially suitable for deployment, transferring across OCT datasets, devices, and clinical tasks, including three datasets not used in the student's pretraining.

---


### 399. [Semantic-First MixGRPO: Reliable Emotional Image Generation via Temporal Decoupling](https://arxiv.org/abs/2610.33460)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenxuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable image synthesis should modify visual affect without replacing the objects, layout, or relations specified by a prompt. Existing methods address this tension through conditioning architectures or auxiliary losses, while mixed ordinary differential equation (ODE) and stochastic differential equation (SDE) sampling has mainly been used to accelerate group relative policy optimization (GRPO). We instead study stochastic-window position as an attribute-control variable for flow-based image generation. Using FLUX.1-dev with EmotiCrafter-style valence-arousal conditioning, we compare fixed early, middle, and late four-transition SDE windows, progressive MixGRPO, and full-path Flow-GRPO under matched settings. Because step 0 has the highest noise, our semantic-first schedule uses deterministic ODE sampling at steps 0-19 to establish content, then confines stochastic exploration and policy updates to steps 20-23. Across three seeds, it achieves a CLIPScore of $29.662\pm0.276$, cross-affect DINO consistency of $80.1\pm0.9$, and semantic drift of 2.9%, while reducing training cost by 33.5% relative to full-path Flow-GRPO. Full-path stochastic training remains more accurate on valence-arousal targets, revealing a genuine trade-off. Semantic-first nevertheless improves both affect and semantic metrics over progressive scheduling, preserves the principal subject in 95.98% of images at five extreme or neutral targets, and receives the highest semantic-preservation and overall-preference ratings in a 30-participant study. These results identify probability-flow time as a practical graphics control dimension for reliable affective appearance manipulation.

---


### 400. [Learning When to Collaborate: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing](https://arxiv.org/abs/2610.33544)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiacheng Hou, Xueliang Cui, Dan Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems have emerged as a promising paradigm for multimodal medical reasoning, but existing methods rely on two assumptions that hinder practical deployment: (i) always-active dense collaboration among multiple agents, and (ii) dependence on large cloud-based models that raise privacy and efficiency concerns. In this paper, we challenge both assumptions and propose SMART-Med, a fully local multi-agent method that treats collaboration as a learnable decision rather than a default behavior. Our key insight is that not every medical query requires costly multi-agent deliberation: many can be reliably solved by a single well-trained agent, while only uncertain cases benefit from expert collaboration. Based on this insight, SMART-Med introduces an uncertainty-driven routing mechanism that adaptively decides when to answer directly and when to recruit a small subset of expert agents, effectively converting dense multi-agent reasoning into selective, query-adaptive coordination. To make this routing reliable, we curate a new multimodal medical dataset MedVR-3K with high-quality reasoning traces and a difficulty hierarchy, and then fine-tune local agents using GRPO with two complementary rewards: a certainty-aware accuracy reward and a vision-language reward model for correctness and reasoning quality respectively. Experiments on four medical visual question answering benchmarks show that SMART-Med achieves competitive performance compared to existing MAS approaches while substantially reducing inference cost (reducing inference time by more than 3.8x and token usage by 72%). Moreover, after fine-tuning on MedVR-3K, SMART-Med yields an average improvement of 6.7% across Slake, PathVQA, VQA-RAD, and PMC-VQA.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
