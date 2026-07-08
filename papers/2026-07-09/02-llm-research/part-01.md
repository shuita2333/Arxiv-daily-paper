# 🧠 大模型相关研究 | 2026年07月09日

> 本类共 **98** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-98](./part-02.md)

---

### 1. [Benchmarking KV-Cache Optimizations across Task Quality and System Performance for Long-Context Serving](https://arxiv.org/abs/2607.05399)

**<font color=#1a73e8>作者：</font>** Nikita Agrawal, Ruben Mayer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model serving is increasingly limited by KV-cache growth under long-context workloads, yet existing KV-cache compression techniques are difficult to compare because they were evaluated on different models, tasks, budgets, and serving stacks. This paper presents a workload-aware benchmark of representative KV-cache optimization mechanisms spanning quantization, pruning, and merging, including KIVI, TurboQuant, SnapKV, and CaM, evaluated on LongBench-style multi-document QA, single-document QA, few-shot learning, and summarization workloads using Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3. The benchmark measures task quality, mean output throughput, mean time-to-first-token, and realized compression ratio across context-length buckets. The results show that the compression ratio alone is a poor predictor of end-to-end performance. KIVI4 provides the most stable quality across models, SnapKV delivers the strongest long-context throughput, and CaM yields large gains on selected QA workloads but exhibits substantial workload sensitivity in both quality and realized compression ratio. These findings motivate workload-aware selection of KV-cache mechanisms rather than one-size-fits-all compression and provide deployment guidance for long-context serving systems.

---


### 2. [Prompt-to-Paper: Agentic AI System for Bioinformatics](https://arxiv.org/abs/2607.05456)

**<font color=#1a73e8>作者：</font>** Ramsha Kamran, Maheera Amjad, Zartasha Mustansar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While recent advances in large language models have enabled end-to-end automated manuscript generation, existing systems suffer from three critical deficiencies: (i) generated claims are not deterministically grounded in verifiable literature, (ii) experimental results are frequently fabricated rather than executed, and (iii) there exists no standardized, multi-dimensional framework to assess whether AI-generated manuscripts meet the quality and rigor required for real-world publication. We present Prompt-to-Paper, a multi-agent framework that directly addresses this evaluation gap through three integrated innovations. First, a deterministic retrieval-augmented generation pipeline with section-aware relevance scoring and snowball citation expansion grounds every claim in a verifiable corpus of 60--100 papers. Second, an autonomous coding agent executes real computational biology experiments replacing synthetic outputs with genuine numerical results. Third, an eight-dimensional automated quality scorer, benchmarked with approximate reference statistics from published papers and augmented with explicit hallucination penalties, provides standardized, reproducible quality assessments. The quality-driven improvement loop uses a context-rich reviser that routes each iteration to one of three researcher actions and fires a deep research cycle every ten iterations to re-run experiments and re-manuscript from stronger outputs. We validate the system on five bioinformatics case studies; all five cases compiled submission-formatted PDFs with zero out-of-range citations. The improvement loop raises manuscript quality by an average of +17.96 points on a 0--100 scale (maximum +26.04. As partial external checks, a human reviewer scored the five manuscripts at an average of 7.0 out of 10. Complete manuscripts are produced at approximately 0.31 USD per paper.

---


### 3. [Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning](https://arxiv.org/abs/2607.05458)

**<font color=#1a73e8>作者：</font>** Haiwen Yi, Xinyuan Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are usually improved by changing prompts, models, or hand-written workflows, while the execution harness around the model is treated as fixed infrastructure. We argue that this harness is itself a learnable control layer. We formalize harness operation as a finite-horizon Harness MDP, where a lightweight controller selects structural execution actions while the LLM executor remains frozen. The controller is trained from offline rollouts using advantage-weighted regression with only terminal task-rubric rewards. We also separate final task quality from a post-hoc Harness Maturity Score, which measures whether the harness follows reliable execution patterns rather than only whether the final answer is correct. This separation gives a finite-buffer view of harness learning: final-quality gains require high-return support in the offline buffer, while process behavior can shift whenever it aligns with advantage-weighted actions. Across six controlled domains and two public-benchmark adapters, the learned controller consistently improves verification behavior and selectively improves final task quality, with the largest gains on adapted tau-bench retail, adapted AgentBench DB-Bench, and coding with a calibrated structural verifier. Ablations against behavior cloning and Forced CHECK show that the gains are not explained by imitation or by simply adding checks. These results identify harness control as a learnable layer for frozen LLM agents, while showing that offline support limits when better process control becomes better final answers.

---


### 4. [Parameter-Free Encoders Remain Viable for RDB Foundation Models](https://arxiv.org/abs/2607.05476)

**<font color=#1a73e8>作者：</font>** Linjie Xu, David Wipf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As the space of potential targets is vast across enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models based on RDB-specific encoders provide a viable solution, but ideal design remains an open question. On the one hand, it has recently been argued that certain parameter-free subgraph encoders combined with single-table foundation models can achieve near SOTA performance, with no RDB-specific pre-training required. Meanwhile, other contemporary studies advocate for parameterized encoders pre-trained to exploit observable labels for learning task-specific representations. To address this ambiguity, we analyze RDB encoder properties specifically when labels are present as inputs, proving limitations on the potential efficacy of trainable encoder parameters. As empirical validation, we demonstrate that considerably simpler parameter-free encoders are still capable of strong performance across many relevant benchmarking tasks.

---


### 5. [Decision Protocols in Multi-Agent Large Language Model Conversations](https://arxiv.org/abs/2607.05477)

**<font color=#1a73e8>作者：</font>** Lars Benedikt Kaesberg  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Improving the task performance of Large Language Models (LLMs) is essential, yet scaling these models faces significant challenges such as diminishing returns and high costs. Multi-Agent Systems (MAS) offer a promising solution by distributing tasks among specialized agents to improve the overall task performance. This can reduce training costs at the expense of increased test time due to the discussion and decision-making process. The decision protocol is a critical component of MAS because it specifies how multiple agents collaborate to create a final solution. This thesis introduces the Multi-Agent LLM (MALLM) framework, which implements and evaluates various decision protocols, namely voting, consensus, and judge decision mechanisms, to simulate multi-agent discussions for conversational task solving. Unlike previous work that used a single decision protocol or tested them on limited datasets, this study systematically examines their impact on a diverse set of tasks, ranging from knowledge-based datasets (MMLU, MMLU-Pro, GPQA) and logic-based datasets (StrategyQA, MuSR, Math-lvl-5, SQuAD 2.0). The results indicate that consensus protocols excel in knowledge-intensive domains while voting and judge protocols are more effective for logic-based tasks. Increasing response diversity through independent solution generation improves decision quality, while changes in information access during the decision process have minimal impact.

---


### 6. [PatchOptic for Shared-State LLM Workflows with Projected Views and Verified Structured Updates](https://arxiv.org/abs/2607.05483)

**<font color=#1a73e8>作者：</font>** Zhaoyu Bai, Jiaqi Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic workflows often operate over shared, structured state. Because LLM context windows are limited, each model invocation is typically shown only the state fragment needed for the current workflow step, a pattern commonly known as progressive disclosure. Modern systems construct such model-facing views using grep-like keyword search, retrieval-augmented generation (RAG), abstract-syntax-tree (AST) queries, and task-specific agent skills. These methods make the read side manageable, but they do not define when a locally proposed rewrite is valid after it is applied back to the full state. The missing piece is a contract between local updates and global validity. We introduce PatchOptic, an optic-inspired interface for shared-state LLM workflows. Optics are compositional bidirectional accessors that describe how views of structured data are read and updated. PatchOptic borrows this view/update intuition and realizes it through projected reads and verified structured patches. Each workflow step declares a projected read view, an authorized write region, and a patch-source region. Beyond runtime enforcement, the same declaration yields a path-level footprint that supports delegation, sub-workflow composition, and static certificates for reordering independent steps within the same phase. We evaluate this design with PatchBench, a benchmark with 46 cases across domains. The results show that projected reads reduce reported leakage and token cost while preserving accepted-output quality under the strong actor. Runtime verification blocks declared workflow-contract violations before commit, and patch-read enforcement rejects compromised patch artifacts that use hidden sources.

---


### 7. [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511)

**<font color=#1a73e8>作者：</font>** Chang Nie, Jiaju Wei, Junlan Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., $\mathtt{search}$) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light-Omni, a multimodal agent framework for reflexive and lightweight video understanding. It achieves this through dual contextual states that instantly build the required context in a single forward pass. First, we maintain a global state, a finite-sized multimodal script continuously consolidated from episodic memory, serving as the global context for Light-Omni. Through hierarchical merging, it preserves recent details while summarizing past events. Second, conditioned on this global context, we generate a parametric latent state that directly drives autonomous actions and produces retrieval embeddings, with minimal latency. Benefiting from this coupled design, Light-Omni achieves semantically aligned retrieval and reflexive responses while avoiding iterative reasoning. Extensive experiments validate the effectiveness of Light-Omni across multiple video benchmarks. Notably, it outperforms M3-Agent with an average 2.4% accuracy gain, a 12.1$\times$ speedup, and a 2.6$\times$ improvement in GPU memory efficiency. Furthermore, it serves as a memory system to enhance both the performance and efficiency of existing MLLMs. Project page: this https URL.

---


### 8. [Multi-Teacher Contrastive Distillation for Edge-Efficient Pathology Foundation Models](https://arxiv.org/abs/2607.05533)

**<font color=#1a73e8>作者：</font>** Tim Lenz, Maurice Heide, Marco Gustav 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational pathology foundation models (PFMs) have advanced whole-slide image analysis. However, their size and inference cost hinder local deployment in pathology departments. We propose MuCoDi, a pretraining framework that distills frozen tile embeddings from multiple PFMs into compact edge-oriented encoders. Instead of regressing individual teacher features, MuCoDi trains lightweight MobileOne and RepViT students with a contrastive distillation objective adapted from MoCo v3, where cached Virchow2, UNI2, and H-Optimus-1 embeddings replace momentum-encoder keys. We pretrain students on 14.3M TCGA tiles from only 11.8K WSIs and evaluate frozen encoders on 23 clinically curated downstream classification tasks. RepViT-based MuCoEdge students retain near-teacher performance while reducing model size by orders of magnitude: MuCoEdge-R2.3 and MuCoEdge-R1.5 reach 71.0% external AUROC, within 0.8 percentage points of the best teacher (Virchow2, 71.8%), while MuCoEdge-R2.3 obtains the best external F1 and the second-best AUPRC (51.8% and 53.3%). MuCoEdge-R1.0 reaches 70.9% AUROC with only 6.4M parameters and 1.12 GFLOPs. On a Raspberry Pi 5, sub-million-parameter MobileOne students achieve up to 605-fold single-tile speedup over Virchow2 while retaining 66.5% to 66.9% external AUROC, demonstrating that PFM-quality pathology representations can be moved toward practical edge deployment. Code is available at this https URL.

---


### 9. [Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks](https://arxiv.org/abs/2607.05545)

**<font color=#1a73e8>作者：</font>** Yibo Hu, Jiaming Qu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM conformity is often used to describe cases where a model changes a correct answer toward a peer or group response. We show that most of this apparent conformity survives even after the peer is removed. The reason is a confound: standard conformity prompts mix two cues at once, the presence of a speaker and the repeated wrong answer itself. Existing benchmarks vary these cues together, so they cannot tell how much of the revision actually depends on the speaker. We introduce a no-source condition: the same asserted answer with the explicit speaker removed. Across six open-weight LLMs and seven QA and reasoning datasets, this condition alone causes harmful revision in $66.5\%$ of initially correct cases, compared with $10.3\%$ under a plain re-ask. The effect also remains when the repeated answer is paraphrased and when answer options are hidden in an open-ended setting. Source framing mainly modulates this floor: expert-panel framing raises it, while minimal person labels do not reliably raise it. When models flip, they are usually confidently wrong, and simple recalibration does not recover the original answer. Source attribution still matters, but it should be measured as an increment above this speaker-free floor. The methodological lesson is that conformity benchmarks should first measure what remains after the speaker is removed; without this step, benchmarks may mistake repeated text for social influence.

---


### 10. [The yes-no bias of large language models reflects answer order and wording, not shifts in moral judgment](https://arxiv.org/abs/2607.05552)

**<font color=#1a73e8>作者：</font>** Haonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly issue judgments read as binary verdicts, and a growing literature reports such judgments shifting under logically irrelevant changes of wording - among them an amplified yes-no bias on moral dilemmas, absent in humans. A single framing cannot say what such a shift is: in a yes/no question the word "no" is at once logical verdict, lexical token, and last-printed option. We introduce a psychometric battery that separates these: crossed symmetrization - every logically irrelevant factor flipped in balanced pairs - across a corpus of question forms. A graded rating across logically equivalent forms recovers a coherent internal moral scale: frontier models' stance $\theta$ is nearly format-invariant (cross-form incoherence 0.12-0.21 on a $\pm 1$ axis); small open-weight models fail in model-specific ways. Forcing the verdict through yes/no overlays a decomposable artifact: an order bias toward the last-printed option - opposite to classic human primacy - plus a lexical pull toward the word "no"; the artifact is substantial only in the Claude models (story-averaged -0.32 to -0.86), $\approx 0$ for GPT-5.5 and Gemini, and shrinks under extended reasoning. The word and the verdict share one token; swapping the words for arbitrary labels separates them, and the verdict-attached logical bias proves $\approx 0$ for every frontier model, while model-specific label and order attachments remain: the models are not drawn toward rejecting - the pull follows the printed surface, not the verdict it carries. A minimal model, $P = \sigma((\theta \pm m)/s)$, summarizes any such artifact by a framing susceptibility m and a moral decisiveness s, measurably distinct from sampling temperature. The battery applies unchanged to any dilemma set and binary format: measuring what a model values requires crossing the frames of the question, not asking once.

---


### 11. [Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation](https://arxiv.org/abs/2607.05554)

**<font color=#1a73e8>作者：</font>** Sadia Kamal, Arefa Patwary, Anthony Marchiafava 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Survey-style evaluations of large language models often treat a prompted response as a measure of a model's values or beliefs. This assumption is particularly fragile when responses are read as evidence of political values, social attitudes, or beliefs. We ask whether prompt robustness differs between objective questions with fixed answers and subjective questions that ask for opinions or values. We evaluate four instruction-tuned model families on three objective datasets (MMLU, ARC, and CulturalBench) and three subjective datasets (Political Compass Test, ValueBench, and World Values Survey). For each question/statement, we apply multiple types of prompt changes, such as variations in wording, framing, and format, and measure whether the model gives the same answer across variants. Using a binomial generalized estimating equation, we find significant effects of model, dataset, prompt category, and their interactions. The dataset type effect is also significant, and the interaction between dataset type and prompt category is large. These results show that prompt robustness depends on the question type, the prompt change, and the model.

---


### 12. [Harnessing Generative Image Models for Training-Free Primitive Shape Abstraction](https://arxiv.org/abs/2607.05568)

**<font color=#1a73e8>作者：</font>** Gregor Kobsik, Tim Elsner, Leif Kobbelt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representing 3D shapes as compact sets of geometric primitives is fundamental to robotics, simulation, and scene understanding. Generative image models trained at scale have recently emerged as generalist visual learners that can identify and segment object parts directly in the image domain, across arbitrary categories and without task-specific training. Adapting such models to downstream tasks typically requires fine-tuning; we ask whether their pretrained capability can instead be harnessed directly, without any training, and answer affirmatively with a training-free harness. Our pipeline renders multi-view images of a 3D object, uses a vision-language model to analyze its semantic parts, prompts a generative image model to paint a color-coded part segmentation mask, reprojects it onto the geometry, and fits a superquadric primitive to each part via parameter optimization. The approach contains no learned parameters: it is category-agnostic and orientation-invariant, properties that previous learning-based models struggled with. Its accuracy ceiling rises with future generative-model improvements, which we confirm with a ground-truth segmentation study showing that part segmentation, not primitive fitting, is the current accuracy bottleneck. On HumanPrim and Toys4K, our method achieves the lowest Chamfer distance among all evaluated methods, using 5--9 primitives per object on average.

---


### 13. [CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming](https://arxiv.org/abs/2607.05571)

**<font color=#1a73e8>作者：</font>** H. Chad Lane, Bryson Kageler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly explored as AI tutors, yet deploying them in K-12 settings raises concerns around privacy, cost, and reliance on proprietary models. Small language models (SLMs) offer a promising alternative, but selecting the right model for a specific educational context remains difficult, particularly when the target domain, such as block-based programming, is largely absent from model training data. We introduce CSTutorBench, a benchmark for evaluating language models as CS tutors in VEX VR, a block-based robotics environment. The benchmark comprises 17 scenario-based questions scored against a pedagogical rubric grounded in established tutoring and feedback research, with a human-in-the-loop LLM-as-judge pipeline for evaluation. Preliminary findings across 11 models (4B-120B parameters) reveal that models perform well on surface-level criteria such as vocabulary and tone but struggle with deeper pedagogical behaviors, particularly avoiding answer leakage and engaging with student debugging histories. In our sample, model family and instruction-tuning approach appear to be better predictors of tutoring quality than parameter count alone, though the small number of models limits the strength of this conclusion. A targeted prompt revision grounded in recent educational prompt engineering research improved scores for 10 of 11 models. These results underscore the value of context-specific, pedagogically grounded benchmarks for SLM selection in educational deployment.

---


### 14. [Foundation Models for Automatic CAD Generation](https://arxiv.org/abs/2607.05573)

**<font color=#1a73e8>作者：</font>** J de Curtò, Victoria Guillén, I. de Zarzà  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) enable the automatic generation of parametric 3D designs from natural-language specifications. This chapter presents an empirical study of foundation models for automatic Computer-Aided Design (CAD) generation of mechanical parts, using a unified evaluation pipeline and a curated benchmark of 97 engineering design problems. We introduce LLMForge, a multi-model text-to-CAD framework integrating JSON-schema validation, analytic feature scoring, mesh synthesis, and multi-round iterative refinement, studied under two critique regimes. IterTracer uses a Phong-shaded ray-trace renderer with analytic visual metrics (silhouette IoU, hole visibility, edge clearance, aspect-ratio conformance) for lightweight geometry-aware feedback across rounds. IterVision replaces the analytic scorer with a VLM semantic critic (Qwen2.5-VL-72B) that evaluates rendered views via chain-of-thought visual reasoning, assessing spatial coherence and design intent. On a benchmark spanning four canonical geometry families (plates with holes and bolt circles, multi-feature boxes, flanged cylinders, and L-brackets), we evaluate seven foundation models: DeepSeek-V3.2, Qwen3-235B-A22B, Llama-3.3-70B, Gemma-3-27B, GLM-4.5, MiniMax-M2.1, and INTELLECT. Under IterTracer, the four highest-ranked models form a tight cluster (overall mean in [0.885, 0.890]) with 98.97% mesh success, showing that compact instruction-tuned models can match substantially larger systems. VLM-based critique in IterVision yields 100% watertight mesh generation on the leading model while surfacing systematic difficulty on rotationally symmetric geometries such as cylinders, where visual and semantic scoring diverge most. We discuss benchmark design, failure modes, CAD-oriented prompting, and implications for industrial workflows and scalable automated mechanical design.

---


### 15. [Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction](https://arxiv.org/abs/2607.05577)

**<font color=#1a73e8>作者：</font>** Mohammad Saifullah, Thomas Kornmaier, Taaha Kazi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-form fiction writers need memory that answers multi-hop questions about evolving story state: who knows a secret and when they learned it, whether an event preceded the narration that revealed it, whether a setup paid off, and how a relationship shifted. General-purpose retrieval and agent-memory systems represent entities and facts but not the narratological structure these questions turn on, so they surface the wrong evidence or none at all. We introduce the Narrative World Model (NWM), a writer-memory system that pairs a narratology-grounded typed temporal-state graph with query-conditioned hybrid retrieval. To measure memory rather than the answerer, we read every system through a single held-constant Opus 4.8 reader over only that system's chapter-safe evidence, on a reproducible public corpus and a validated multi-hop benchmark, and we compare against the strongest existing temporal-knowledge-graph agent-memory framework, Graphiti/Zep (Rasmussen et al., 2025). NWM substantially and significantly outperforms this baseline on multi-hop narratological QA across both corpora, and far exceeds GraphRAG and flat retrieval. The advantage is representational rather than an artifact of extraction: it survives rebuilding the baseline with NWM's own extractor, and traces to its narratology-grounded structure and query-conditioned retrieval, not to graph size or extractor quality.

---


### 16. [ResonatorLM: Causal Resonant Field Mixing for Efficient Long-Context Language Modelin](https://arxiv.org/abs/2607.05583)

**<font color=#1a73e8>作者：</font>** Archie Chaudhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contemporary language models are dominated by the transformer architecture, which leverages self-attention mechanisms to enable more efficient, parallelized training across a wide set of documents and corpora. This has allowed transformers to effectively model data across a wide range of modalities and contexts. However, transformers, along with their conventional counterparts such as recurrent neural networks (RNNs) and convolutional neural networks (CNNs), often struggle to maintain efficiency when processing long contexts. We introduce ResonatorLM, a new mechanism that replaces attention with a physics-derived alternative. ResonatorLM treats token sequences as a single, driven one-dimensional latent field and replaces attention dot products with causal functions of damped resonators. We implement ResonatorLM on a traditional network architecture and test it on standard long-context modeling tasks. We find that in a small, 6M matched setting, training and prefill speedups increase with sequence length, decode speed reaches 6.47x compared to that of a standard, optimized transformer at 32K tokens, and accuracy reaches 61.31 percent (compared to 55.32 percent) on WikiText.

---


### 17. [Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition](https://arxiv.org/abs/2607.05612)

**<font color=#1a73e8>作者：</font>** Mohammad Zeineldeen, Albert Zeyer, Haoran Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model (LM) perplexity (PPL) has historically been used as a proxy for automatic speech recognition (ASR) word error rate (WER), with prior work reporting an approximately linear relation in log-log space. Modern end-to-end ASR systems challenge this assumption because they already contain internal language modeling capacity, are often evaluated without external language models, and can now be combined with neural LMs and large language models (LLMs) through different recognition strategies. This paper revisits the relation between PPL and WER for modern ASR systems. We study whether external LMs still improve current end-to-end ASR systems, whether the PPL-WER relation remains linear in log-log space, how encoder context length affects this relation, and how LLM perplexities fit into the trend observed for standard neural LMs. We further investigate internal language modeling (ILM) in attention-based encoder-decoder systems and show that ILM subtraction changes the observed PPL-WER relation, indicating that the decoder's internal LM must be considered when interpreting the effect of external LM quality.

---


### 18. [BaFCo: A Document Understanding Benchmark for Complex Bangla Form Comprehension](https://arxiv.org/abs/2607.05614)

**<font color=#1a73e8>作者：</font>** Abu Tyeb Azad, Ishita Sur Apan, Fahim Ahmed 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document comprehension is a challenging yet impactful task for Multimodal Large Language Models, especially as these systems see growing adoption in real-world, human-centric applications. However, this adoption is limited for low-resource languages such as Bangla due to the scarcity of high-quality annotated data. To address this gap, we introduce BaFCo, a benchmark dataset for Bangla form comprehension with a focus on Document Layout Analysis (DLA) and Key Information Extraction (KIE). BaFCo curates 200 multi-page complex Bangladeshi government forms, sourced from across diverse sectors including agriculture, education, banking, and land management. To accurately capture the structural and contextual complexity of these forms, we define a fine-grained annotation schema comprising 26 types of form entities, along with a separate coarse form entity set consisting of 5 types. We evaluate the latest MLLMs from the ChatGPT, Gemini, Claude, Qwen, and Kimi series using zero-shot and chain-of-thought prompts under both low and high reasoning setups. Our results reveal limitations in current MLLMs' ability in comprehending Bangla forms, particularly in accurately localizing highly granular form entities. Our dataset and code is available at: this https URL

---


### 19. [A Coin Flip Per Token: Bernoulli Sparse Steering of Large Language Models](https://arxiv.org/abs/2607.05615)

**<font color=#1a73e8>作者：</font>** Nima Eshraghi, Lovedeep Gondara, Yuqing Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering via sparse autoencoders (SAEs) enables behavioral control of large language models without task-specific fine-tuning, but standard methods apply the steering signal at every generated token, incurring constant per-token perturbation that risks degrading fluency. We ask: is dense intervention necessary? We introduce Stochastic Token Steering (STS), which gates each token independently with probability $p$, and Stochastic Block Steering (SBS), which gates a leading window once per sequence; neither requires a reward model or learned gating policy. Across two model families and two behavioral tasks, steering only 50% of the tokens recovers most of the dense-steering effect while preserving fluency, and steering as few as 30% surpasses prompt-based control. The optimal steering magnitude scales inversely with the intervention ratio, revealing that SAE-mediated control is rate-limited: the behavioral outcome depends on cumulative signal dosage across a sequence.

---


### 20. [NAVER LABS System Re-implementation for the IWSLT 2026 Instruction-Following Task](https://arxiv.org/abs/2607.05623)

**<font color=#1a73e8>作者：</font>** Anand Kamble, Aniket Tathe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We re-implement the NAVER LABS IWSLT 2025 instruction-following pipeline for the IWSLT 2026 Shared Task (constrained condition, short audio track), adapting it to the mandated components: SeamlessM4T-v2-large as the speech encoder and Qwen3-4B-Instruct as the LLM backbone. The three-stage approach projector alignment, text-only LoRA pre-training, and multimodal merging is preserved from the original design. We additionally construct 100k synthetic instruction-following examples across ten speech-centric task types (10k per task) from the provided corpora, suitable for further Stage 3 fine-tuning. Our primary model achieves COMET 0.781 on EN-ZH speech translation and BERTScore-F1 0.346 on English SQA on the MCIF benchmark.

---


### 21. [Cross-Contextual Vision-Language Adaptation with LoRA for Personalized Severe Adverse Event Detection in Clinical Wound Monitoring](https://arxiv.org/abs/2607.05625)

**<font color=#1a73e8>作者：</font>** Aditi Naiknaware, Jian Sun, Aminreza Khandan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wound monitoring is a critical yet underserved clinical challenge, where timely identification of severe adverse events (SAEs) such as infection, tissue deterioration, and delayed healing can significantly impact patient outcomes. While vision-language models (VLMs) show strong multimodal reasoning, they often lack domain-specific grounding to integrate wound imagery with heterogeneous clinical information, and provide limited mechanisms for detecting cases that diverge from the training distribution. We present a multimodal framework for automated wound monitoring and SAE detection. Our approach leverages paired clinical notes and wound descriptions capturing visual characteristics such as appearance, surrounding skin condition, color changes, and signs of inflammation or healing progression, encoded through a dual-stream Low-Rank Adaptation (LoRA) framework built on a frozen BiomedCLIP backbone. We introduce a cross-contextual LoRA fusion mechanism enabling information exchange between clinical semantics and visual wound descriptors, producing context-aware multimodal representations without full model fine-tuning. To identify personalized SAEs, we propose a wound-specific out-of-distribution (OOD) detection framework combining semantic matching, visual typicality, caption-text alignment, and caption-visual alignment into a unified SAE (OOD) score. To capture healing dynamics, we incorporate covariate consistency and temporal drift penalties that leverage changes in wound characteristics across visits. Experiments on a longitudinal wound dataset collected through clinical visits show promising performance on both wound healing assessment and SAE detection, highlighting the potential of semantically enriched, temporally aware vision-language systems for clinical wound monitoring and early risk identification.

---


### 22. [Taxlifier: Leveraging Disease Taxonomy for Enhanced Multi-Label Classification in Chest Radiography](https://arxiv.org/abs/2607.05628)

**<font color=#1a73e8>作者：</font>** Mohammad S. Majdi, Jeffrey J. Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient classification of thoracic diseases in chest X-ray (CXR) images is crucial for timely diagnosis and treatment. However, the presence of multiple pathologies with overlapping visual characteristics poses significant challenges for automated classification systems. In this study, we propose two novel hierarchical multi-label classification techniques, namely the loss-based and logit-based methods, to address these challenges by leveraging the hierarchical relationships among different thoracic pathologies. The loss-based technique integrates hierarchical information directly into the optimization process, while the logit-based method adjusts the predicted probabilities of each class based on its parent class in the disease taxonomy. We evaluate the performance of both techniques using three large-scale CXR datasets: CheXpert (224,316 CXRs), PADCHEST (160,000 CXRs), and NIH (112,120 CXRs). The experimental results demonstrate significant improvements in accuracy, AUC, and F1 scores compared to the baseline method across various pathologies. The logit-based and loss-based methods improve accuracy by 12\% and 11\%, AUC by 13\% and 10\%, and F1 scores by 24\% and 12\%, respectively compared to the baseline. These results represent a substantial improvement over the baseline method. Furthermore, we conduct a comprehensive statistical analysis to validate the robustness and reliability of the proposed techniques. The integration of domain-specific hierarchical knowledge not only enhances the classification performance but also provides a more interpretable output for clinical decision support. Our findings highlight the potential of hierarchical multi-label classification in advancing computer-aided diagnosis systems for chest radiography.

---


### 23. [GeoXplain: On-the-Fly Visual Explanations for Weather Foundation Models](https://arxiv.org/abs/2607.05655)

**<font color=#1a73e8>作者：</font>** Clemens Walter Koprolin, Leonardo Trentini, Benedikt Soja 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Weather and climate foundation models produce high-dimensional forecasts whose learned relationships are difficult to inspect with static plots alone. GeoXplain is an interactive Python-based visualization toolkit for exploring geospatial attribution maps across climate variables, atmospheric pressure levels, and forecast time. The toolkit accepts attribution bundles containing attribution grids together with corresponding metadata and renders them in a notebook widget or browser with map and globe modes, linked timelines, pressure-level controls, target annotations, and optional physical-field overlays. We frame GeoXplain as a model-agnostic earth-system visualization toolkit and present the GeoXplain Aurora Adapter as its first computation backend. The adapter computes explanations for the Aurora foundation model, either in a local GPU process, through a GPU listener, or through a SLURM-backed listener, while preserving the same Python call site for analysts. It currently supports gradient saliency, Integrated Gradients, RISE, ViT-CX, multi-frame saliency and Integrated Gradients rollouts, and retrieval of ERA5 overlays. GeoXplain can be installed as a PyPI package with pip install geoxplain. The code is open-source and available at this https URL.

---


### 24. [RPAM: A Principled Metric for Evaluating Associations in Language Models with High Predictive Validity in Downstream Outputs](https://arxiv.org/abs/2607.05679)

**<font color=#1a73e8>作者：</font>** Damian Hodel, Jevin West, Aylin Caliskan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) exhibit problematic biases, such as stereotypes. Effectively analyzing and mitigating such biases requires accurate and generalizable evaluation methods of the underlying associations. Some existing approaches focus on downstream metrics that analyze associations in generated text. Since generated text content can vary drastically across LMs, such metrics often require specialized evaluation datasets, which limits the generalization of such downstream metrics. In contrast, upstream metrics examine LMs at the fundamental level of embeddings or continuation probabilities, enabling principled association analyses across LMs. Yet, to date, no upstream metric for generative LMs has uncovered a strong relationship with real-world associations, including those measured in generated text. To address this gap, we introduce the Relative Probability Association Metric (RPAM), an association evaluation metric for generative LMs. For three LMs of different quality of language generation and purpose (Mistral-7B-Instruct, Mistral-7B, and GPT-2) and well-studied evaluation datasets (WEAT-WS, Bellezza, WS-353, and SST2), we find a strong relationship between upstream RPAM measurements and corresponding implicit and explicit associations observed in humans, as well as biases measured downstream with LM-specific tasks, outperforming prior record values where applicable.

---


### 25. [FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents](https://arxiv.org/abs/2607.05682)

**<font color=#1a73e8>作者：</font>** Yufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption that a scientist should inspect. We introduce FirstResearch, a first-principles research-question formation framework for scientific LLM agents whose core artifact is a structured Research Question Certificate. The certificate records primitive definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable hypothesis, a minimal decisive test, and a failure update rule, making the proposed question inspectable before downstream execution. On ten LLM-agent research topics, FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist, Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol. A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat ablation checkpoint further suggests that the certificate-centered core is the strongest component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under Gemini, while removing certificates drops below 1/5 under both judges. These results are preliminary and use LLM judges rather than human domain experts, but they support a narrow scientific-discovery claim: explicit derivation constraints are a promising mechanism for making LLM-generated scientific questions more auditable. Code, prompts, saved outputs, and reproduction scripts are available at this https URL.

---


### 26. [Depression Symptoms and Relational Patterns in 187k ChatGPT Histories](https://arxiv.org/abs/2607.05685)

**<font color=#1a73e8>作者：</font>** Neil K. R. Sehgal, Dunigan Folk, Lyle Ungar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as private, always-available conversational systems, but little is known about how people with depressive symptoms use them. Building on CSCW work on disclosure and peer support, we examine ChatGPT as an emerging informal support infrastructure: private, persistent, responsive, and available outside ordinary hours. We analyze 187,093 ChatGPT conversations from 766 participants who completed the PHQ-8, comparing those below the moderate-symptom threshold (score of 10) with those at or above it. Higher-PHQ participants used ChatGPT more for mental-health, interpersonal, loneliness, self-focused, and support-seeking conversations, with pronounced late-night and recurring month-level patterns. Their language contained more first-person singular pronouns and absolutist terms. They more often engaged ChatGPT in high-disclosure contexts, but professional redirection was not higher. Language-based prediction was modest and insufficient for screening (AUROC 0.591). We argue these histories should not be treated as clinical screening data but as evidence LLMs are increasingly used as informal support infrastructure.

---


### 27. [LLM-Driven Neural Network Generation with Same-Family Architecture Guidance: Disentangling Transfer and Adaptation](https://arxiv.org/abs/2607.05704)

**<font color=#1a73e8>作者：</font>** Kabir Dev Paul Baghel, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate neural-network modifications, but unrestricted generation is often invalid or harmful. This paper studies a narrower setting: improving a weak target model using a stronger same-family source model from a neural-network database. We propose a source-guided candidate-generation protocol with non-source controls, source-conditioned candidates, and a no-LLM hp_copy ablation under equal evaluation budgets. The protocol reports validity separately from accuracy and selects the best valid candidate only when it improves the target. On CIFAR-10, the strongest source-guided candidate reaches 0.5049 accuracy versus 0.2398 for the best non-source candidate, a +0.2651 advantage, while improving a weak target originally at 0.1254; a five-epoch check preserves the gain at 0.7686 versus 0.4839. On SVHN AlexNet with DeepSeek-Coder-6.7B, source-guided transfer reaches 0.7880 versus 0.2254, a +0.5626 advantage; a fresh repeat reaches 0.8069 versus 0.2509, a +0.5560 advantage. Direct source-recipe copy produces 0.1959 on SVHN AlexNet, matching the original target, while hp_transfer reaches 0.7880, showing that the LLM adapts rather than copies the source recipe. Family-level analysis shows the clearest positive signals for AlexNet, with 6/8 wins across SVHN, Imagenette, and CelebA-Gender, and alt_nn1, with 8/10 wins on CIFAR-10.

---


### 28. [Akashic: A Low-Overhead LLM Inference Service with MemAttention](https://arxiv.org/abs/2607.05708)

**<font color=#1a73e8>作者：</font>** Yang Liu, Zhaokai Luo, Huayi Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based agent systems continuously accumulate context across multi-turn interactions, tool invocations, and cross-session workflows. Replaying the full history for every request quickly becomes impractical: long contexts increase prefill cost, may exceed context limits, and often bury task-relevant evidence in irrelevant content, degrading both serving efficiency and output quality. We propose Akashic, a low-overhead memory system built around MemAttention, which organizes context into bounded chunks and models semantic relationships across chunks, preserving cross-chunk evidence without repeatedly rewriting the full history. Akashic further applies hardware-software co-designed memory placement to co-locate likely co-retrieved chunks, reducing retrieval fragmentation and I/O overhead. Across four representative workloads and three model sizes, Akashic improves task accuracy by up to 10.2 points, throughput by up to 1.21x, and sustainable request rate by up to 1.88x over strong prior memory baselines.

---


### 29. [FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models](https://arxiv.org/abs/2607.05711)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Zihan Min, Xingyang Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become a dominant paradigm for high-quality generative modeling, while post-training is essential for adapting them to diverse downstream applications. However, post-training of large diffusion models is still challenging due to the prohibitive memory footprints and slow training speed, which existing parameter-efficient fine-tuning methods only partially address. To overcome these limitations, we propose FourTune, an efficient post-training framework for diffusion models based on an end-to-end W4A4G4 paradigm. FourTune introduces a triple-branch hybrid pipeline that augments the standard LoRA architecture with a frozen numerical stabilizer to isolate quantization-sensitive outliers, enabling stable training under native 4-bit computation. In addition, FourTune employs hardware-efficient block-wise quantization and customized fused kernels to support efficient quantized backpropagation and reduce memory bandwidth overhead. Across customization, reinforcement learning, and distillation tasks, FourTune matches the quality of full-precision fine-tuning. On FLUX.1-dev (12B), FourTune reduces memory overhead by 2.25$\times$ and increases end-to-end training throughput by 2.27$\times$ compared to BF16 LoRA.

---


### 30. [Scene Graph Thinking: Reinforcing Structured Visual Reasoning for Multimodal Large Language Models](https://arxiv.org/abs/2607.05716)

**<font color=#1a73e8>作者：</font>** Zhiwei Yang, Yuanchen Wu, Nan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong perception and reasoning capabilities. However, most existing models focus on isolated objects and neglect structured relationships for efficient target navigation, limiting their performance on visually intensive tasks. To address this challenge, we introduce Scene Graph Thinking (SaGe), a novel paradigm that enables fine-grained and structured visual reasoning through explicit scene-graph representations. Specifically, we first introduce an automated data engine that converts flat image-text corpora into structured scene graphs, where hierarchical entities constitute the nodes and diverse visual relations define the edges. Building upon this, we construct 120K high-quality training data by sampling reasoning traces from scene graphs. Then, two-stage graph-aligned post-training paradigms are introduced, where supervised fine-tuning internalizes MLLMs with structured reasoning, and subsequent reinforcement fine-tuning proposes node-as-proxy graph rewards to consolidate efficient graph exploration. With curated data and graph-aligned training, our approach achieves significant improvements across eight multimodal benchmarks, demonstrating strong effectiveness on fine-grained perception and reasoning tasks. Code is available at this https URL.

---


### 31. [SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation](https://arxiv.org/abs/2607.05721)

**<font color=#1a73e8>作者：</font>** Yimeng Zhang, Yingying Zhuang, Ziyi Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation is essential not only for the trustworthy deployment of large language models (LLMs) but also as a foundation for self-refinement in LLM generation. However, existing approaches operate at suboptimal granularities: token-level scores lack semantic coherence, while sequence-level scores fail to localize errors. We formalize Span-Level Uncertainty Estimation (SLUE), a new task that targets the natural granularity for uncertainty: semantically coherent text spans, each conveying a single assessable unit of meaning. To address this task, we introduce SPANUQ, a lightweight probe that distills the uncertainty knowledge from expensive multi-sample inference into a single forward pass over LLM hidden states. SPANUQ employs a DETR-style span decoder to simultaneously detect spans and estimate their uncertainty via a Mixture of Beta distribution, trained with a principled combination of Beta NLL regression and contrastive ranking objectives. We construct SPANUQ-BENCH, the first span-level uncertainty benchmark comprising 20K prompts, 293K annotated spans, and continuous soft labels derived from multi-sample claim verification. Experiments on five LLM backbones show that SPANUQ consistently achieves the best span-level uncertainty quality, outperforming the strongest probe baseline and all sampling-based methods while being 10-20x faster. Its DETR-based span detector attains 0.910 F1, surpassing the best heuristic by 39.4%, enabling precise error localization that sequence-level methods cannot provide. The framework generalizes across five LLMs spanning two model families.

---


### 32. [Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding](https://arxiv.org/abs/2607.05722)

**<font color=#1a73e8>作者：</font>** Yonggan Fu, Lexington Whalen, Abhinav Garg 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron-Labs-Diffusion, a tri-mode language model (LM) that unifies AR, diffusion, and self-speculation decoding within a single architecture. Trained with a joint AR-diffusion objective, Nemotron-Labs-Diffusion can switch modes to sustain high throughput across deployment settings and concurrency levels. Our study shows that (1) AR and diffusion objectives are complementary: diffusion improves lookahead planning, while AR provides left-to-right linguistic priors. (2) In self-speculation mode, diffusion drafts while AR verifies, outperforming multi-token prediction (MTP) methods in both acceptance rate and real-device efficiency. (3) A speed-of-light analysis further demonstrates diffusion's long-term potential, with up to 76.5% more tokens per forward pass than self-speculation under an optimal sampler. Scaling to 3B, 8B, and 14B parameters, our Nemotron-Labs-Diffusion family, including base, instruct, and vision-language models, consistently outperforms state-of-the-art open-source AR and diffusion LMs in both accuracy and speed. For example, Nemotron-Labs-Diffusion-8B decodes 6x more tokens per forward than Qwen3-8B with comparable accuracy, translating to 4x higher throughput on SPEED-Bench with SGLang on a GB200 GPU.

---


### 33. [Multimodal Molecular Representation Learning with Graph Neural Networks, Deep & Cross Networks, and SMILES Embeddings](https://arxiv.org/abs/2607.05736)

**<font color=#1a73e8>作者：</font>** Qiwei Han, Chi Zhou, Ruobing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction often relies on isolated data modalities, where continuous 3D graph neural networks (GNNs) struggle to efficiently capture long-range topological dependencies and exact macroscopic heuristics. In this work, we introduce a parameter-efficient Tri-Branch Modular Fusion Neural Network that synthesizes three orthogonal modalities: 3D spatial geometry (SchNet), discrete topological grammar (SMILES via ChemBERTa), and explicit macroscopic physicochemical descriptors (Deep & Cross Network). By bypassing standard scalar readouts and employing a shared late-fusion architecture, the framework establishes a mathematically rigorous multimodal latent space that effectively resolves the arithmetic and oversmoothing limitations of local message passing. We evaluate the proposed architecture on the QM9 benchmark, targeting the extensive thermodynamic property of atomization energy at 0 K ($U_0^{\mathrm{atom}}$). Through systematic combinatorial ablation and latent bottleneck optimization ($d_e=64$), the tri-modal framework achieves a validation Mean Absolute Error (MAE) of 0.0207 eV. Operating with fewer than one million parameters, this architecture decisively surpasses the sub-chemical accuracy threshold and yields a substantial 20.6% error reduction over a strictly controlled geometric baseline. Ultimately, our findings demonstrate that integrating orthogonal macroscopic and topological data streams provides a synergistic, $\mathcal{O}(1)$ physical shortcut. This multimodal alignment offers a highly efficient alternative to brute-force parameter scaling, establishing a robust surrogate model for high-throughput virtual screening (HTVS) pipelines.

---


### 34. [PERSONAJUDGE: Simulating Individual Human Preference Judgments with Evaluator-Specific Demonstration Data](https://arxiv.org/abs/2607.05742)

**<font color=#1a73e8>作者：</font>** Zeyu He, Xuan Qi, Subramanian Chidambaram 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as judges in AI evaluation, but current approaches rely on consensus preferences that ignore individual evaluator variation. We propose a novel simulation approach that combines categorical judgments with evaluator-specific auxiliary data--retrospective reasoning traces and interface telemetry--to enable LLM-based simulation of individual evaluators via in-context learning. We conduct a systematic empirical study of this approach using multi-facet data from 32 trained annotators across 4,200 preference judgments in a 4 x 4 x 4 factorial design. Our key findings: (1) The simulation approach achieves up to 9.9 percentage point improvements over the Base Judge; (2) Reasoning traces provide the largest gains with higher collection efforts, while interface telemetry often hurts rather than helps performance despite being cheaper to collect. (3) Simulation difficulty is systematic, predicted by an evaluator's neutral usage (most clearly on Helpfulness) and divergence from consensus; the neutral-usage tendency--rather than simulatability itself--is the cross-task-stable property (r = 0.728). These results establish both the potential and limits of evaluator-specific auxiliary data for personalized evaluation, offering methodological insights for scaling individual aware AI assessment.

---


### 35. [When Should LLMs Search? Counterfactual Supervision for Search Routing](https://arxiv.org/abs/2607.05752)

**<font color=#1a73e8>作者：</font>** Minho Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search-augmented language models can use external evidence to compensate for limitations in parametric knowledge, but search is not uniformly beneficial: models may call search for questions they can already answer, or rely on noisy evidence when correction, clarification, or abstention would be more appropriate. We formulate this as an instance-level search-routing problem: deciding whether search is needed to improve task success relative to a no-search execution. To derive supervision, we compare no-search and forced-search outcomes for the same question and construct an oracle over NO SEARCH, SEARCH, and UNSOLVED based on task-specific success. Using this oracle as both an evaluation criterion and a learning signal, we train search-routing policies with supervised fine-tuning and preference optimization, improving routing macro-F1 on oracle-eligible examples from 0.7082 to 0.8235 for Gemma E2B and from 0.7053 to 0.8365 for Qwen3.5-4B. Further analysis shows that the learned policies reduce model-specific routing failures: Gemma primarily learns no-search restraint, while Qwen further reduces missed search; residual UNSOLVED cases reveal heterogeneous bottlenecks involving model capacity, retrieval budget, evidence use, and policy behavior.

---


### 36. [Synthetic Consumer Insight Generation with Large Language Models](https://arxiv.org/abs/2607.05761)

**<font color=#1a73e8>作者：</font>** Stephen L. France, Pia. A. Albinsson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern data-driven marketing relies on large amounts of consumer data, yet collecting such data can be costly, time-consuming, and difficult to scale. This research examines whether large language models (LLMs) can be used to generate synthetic consumer data for projective techniques, a set of methods designed to elicit consumer associations, emotions, wants, and needs. We test LLM-generated responses across multiple projective tasks, LLMs, prompting strategies, and temperature settings, and compare them with human responses from a primary research study on perceptions of city tourism destinations. Human and LLM responses were analyzed using linguistic measures, diversity and concentration metrics, topic models, and top-term analyses. The results show substantial overlap between human and LLM responses in broad topics and associations, but also important differences in style, linguistic structure, and the way diversity is generated. Recommendations are given on how to best utilize LLMs for generating synthetic consumer data, how model and prompt choices shape response quality, and on recognizing the limitations of LLM synthetic consumer data generation.

---


### 37. [Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents](https://arxiv.org/abs/2607.05764)

**<font color=#1a73e8>作者：</font>** Mahmoud Hany, Mourad ElSheraey, Mahmoud Said 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering questions over a set of transactional legal documents is most simply done by injecting the whole corpus into the LLM's context window on every query. That baseline maximises retrieval recall, but its token footprint scales with the corpus rather than the question, and long-context degradation scales with it. We report what it took to replace full-corpus injection in a legal-document analysis system, comparing it against two structured retrieval modes over our proprietary structure-aware chunking: embedding retrieval (NAVEMBED) and LLM navigation over a compact structured index (NAVINDEX). On a 20-question benchmark with verified ground-truth answers, a position-bias-controlled, reference-anchored pairwise judge scored semantic retrieval with reranking tied with injection on 16 of 18 document-bound questions (injection preferred on 2) while attending to 17.3x fewer input tokens (a general-text-embedding (GTE) configuration reaches 29.9x at a lower tie rate); both modes were judged tied on the 2 out-of-scope controls. NAVINDEX was judged tied on all 18 at a 1.61x smaller total token footprint, a ~56x smaller answering context, and 25% lower dollar cost. We derive a closed-form caching-crossover rule: cached injection is cheaper in dollars only while the corpus stays below roughly ten times the retrieval payload. Scope and uncertainty are quantified in Section 8.

---


### 38. [LEGATO 2: Toward Multimodal Sheet Music Recognition and Understanding](https://arxiv.org/abs/2607.05769)

**<font color=#1a73e8>作者：</font>** Guang Yang, Brian Siyuan Zheng, Victoria Ebert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel pipeline, Legato 2, for extracting symbolic notation and semantic knowledge from images of sheet music. Legato 2 features the first large-scale neural model for optical music recognition (OMR) to operate sequentially on a system-by-system basis, following the horizontal lines of notation as they are read on the page, rather than treating the page as an undifferentiated image, enabling better scaling to arbitrarily long inputs. It is also the first OMR model capable of generating symbolic transcriptions that include embedded textual content, such as titles and annotations. The pipeline combines system-level segmentation with an autoregressive vision-LM to capture both local notation details and score structure. Across multiple datasets, Legato 2 consistently outperforms prior state of the art. We also show that symbolic transcriptions complement visual inputs for frontier language models, improving their interpretation of dense musical documents. Legato 2 establishes new state-of-the-art performance in both OMR and downstream sheet music understanding.

---


### 39. [Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning](https://arxiv.org/abs/2607.05773)

**<font color=#1a73e8>作者：</font>** Akshay Arora, Ishan Nigam, Ashutosh Aggarwal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve into autonomous agents, traditional static evaluation fails to capture multi-step decision-making. We introduce AgenticAI-Supervisor, an API and UI-driven RL Gym environment that decouples environment creation from scalable execution. By moving to verifiable execution outcomes, the platform generates high-fidelity traces and applies multi-dimensional reward shaping. Critically, our framework mitigates reward hacking through rigorous internal state validation and testing. This work provides a first look at our platform's core capabilities through a Customer Support Agent case study demonstrating a consistent closed-loop feedback for model optimization. Future work will focus on advanced features such as Computer Use, Tool Use, automated "stumping", and edge-case generation.

---


### 40. [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775)

**<font color=#1a73e8>作者：</font>** Wael Albayaydh, Rui Zhao, Ivan Flechais  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly evaluated on their ability to use tools, plan multi-step tasks, coordinate with other agents, and operate over extended horizons. Reported benchmark gains often obscure recurring failure modes documented across otherwise unrelated evaluation efforts. This paper synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026), spanning 19 distinct benchmarks, into a cross-cutting taxonomy of agent limitations. To our knowledge, this is the first synthesis that integrates evidence across tool use, planning, long-horizon reasoning, multi-agent coordination, safety, and measurement validity into a single, unified taxonomy of LLM agent limitations. We identify six failure clusters: (1) tool invocation and parameter-level errors, (2) planning and constraint-satisfaction failures, (3) long-horizon degradation from context accumulation, (4) multi-agent coordination failures, (5) safety and security failures under adversarial or underspecified conditions, and (6) measurement validity problems. The taxonomy was derived iteratively by grouping independently reported error categories into themes corresponding to distinct stages of the agent reasoning-to-action pipeline. Across the literature, we find that failures compound nonlinearly with task length, that strong performance on individual sub-tasks does not reliably translate into end-to-end success, and that additional scaffolding does not consistently improve reliability. At the same time, substantial progress has been demonstrated in single-turn tool use, short-horizon web navigation, and narrowly scoped coding tasks.

---


### 41. [Benchmarking the Robustness of Autonomous Driving to Environmental Illusions: A Lane Perception Perspective](https://arxiv.org/abs/2607.05783)

**<font color=#1a73e8>作者：</font>** Tianyuan Zhang, Xianglong Liu, Aishan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Environmental illusions (eg., shadows, reflections, and tire marks) are naturally existing yet overlooked phenomena in real-world driving environments. They can disturb visual perception, leading to misinterpretation of the scene and posing serious safety risks to autonomous driving (AD) systems. However, existing researches largely overlook these phenomena, leaving a critical gap. To address this issue, we study AD robustness through the lane perception perspective, a fundamental task supporting core functions like cruise control and lane centering. We focus on two representative models: conventional lane detection (LD) and vision-language model-based systems (ADVLMs). In this work, we introduce the first benchmark, LanEvil++, for evaluating the robustness of lane perception under environmental illusions. LanEvil++ encompasses 14 types of illusions and leverages the CARLA simulator to generate 94 high-fidelity, fully controllable 3D scenes, yielding a dataset of 90,292 annotated images, 1,596 video clips, and 41,855 visual question answering pairs. Extensive evaluations demonstrate that environmental illusions substantially degrade the performance of state-of-the-art LD methods. On average, LD models experience a 5.27% drop in Accuracy and a 10.49% decline in F1-score, while ADVLMs show a 2.03% reduction in GPT-score and a 0.75% drop in Language-score. Among all illusions, shadows emerge as the most disruptive factor, reducing accuracy by up to 7.20%. Furthermore, closed-loop simulations reveal that these illusions can lead to incorrect driving decisions. Complementary real-world case studies highlight safety-critical failures in actual traffic scenes. To enhance robustness, we propose the Multimodal Illusion Defense Approach (MIDA). MIDA achieves substantial gains under challenging conditions, boosting robustness by 4.23% on LD models and 3.82% on ADVLMs.

---


### 42. [Controlling Tool Use with Heading-Specific Activation Steering](https://arxiv.org/abs/2607.05790)

**<font color=#1a73e8>作者：</font>** Yuqi Chen, Vincent Siu, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language models extend their capabilities beyond parametric knowledge through external tools, but tend to invoke them unnecessarily. We investigate whether tool-use decisions have any stable internal representation that can be extracted and manipulated, a question that is non-trivial given that tools exist entirely in context at inference time and have no direct encoding in model weights. We show that steering vectors extracted from heading-anchors positions exert bidirectional causal control over tool-invocation behavior across five open-source models and three domains, suppressing unnecessary tool use most effectively in domains where parametric reasoning suffices. However, geometric analysis reveals that this causal effectiveness does not correspond to clean linear structure: tool-invocation steps exhibit diffuse, bimodal alignment with the suppression vector rather than the consistent negative alignment a linear encoding account would predict, and different tool types recruit largely distinct internal signatures with low cross-tool feature overlap. We hypothesize these geometric properties are indicative of the non-parametric nature of tools, and distinguish tool-use steering vectors from those extracted for parametrically grounded concepts. The relationship between this geometric irregularity and the observed causal effectiveness remains an open question.

---


### 43. [Segmentation before Answering: Pixel Grounding for MLLM Visual Reasoning](https://arxiv.org/abs/2607.05798)

**<font color=#1a73e8>作者：</font>** Yake Wei, Yuan Wang, Fengyun Rao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Multimodal Large Language Models (MLLMs) have evolved from static perception to interleaved visual-language reasoning, often referred to as ``thinking with images''. A basic operation in this reasoning process is to zoom in on regions of interest (often represented with bounding boxes) to acquire finer visual details. In this paper, we propose \textbf{Seg}mentation before \textbf{Answer}ing (SegAnswer), which shifts the unit of zoom-in from the popular bounding box to pixel-level segmentation mask. By employing fine-grained masks to isolate the target area from cluttered environments, segmented visual input yields a more precise region of interest, effectively filtering out redundant background and interfering objects. Furthermore, the discrete patches of segmented visual input align more seamlessly with how MLLMs structure visual tokens via positional embeddings. In experiments, we evaluate SegAnswer across diverse benchmarks, including high-resolution perception, general perception, and hallucination. It achieves consistent improvements and also exhibits considerable performance on segmentation tasks, validating its capability for reliable pixel grounding.

---


### 44. [Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure](https://arxiv.org/abs/2607.05805)

**<font color=#1a73e8>作者：</font>** Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, yet their fault diagnosis is still dominated by threshold alarms that report that something is wrong, not what. We present Onnes, a physics-grounded digital-twin simulator of a dilution refrigerator (a forward physics model with a learned real-fridge noise fingerprint) that drives a live multi-agent LLM operations layer, and use it for a controlled head-to-head between a zero-shot LLM agent panel and a supervised ML classifier on cryogenic fault diagnosis. The twin couples a real dilution-cooling floor, a noise-and-correlation fingerprint learned from real BlueFors logs, and six physics-grounded fault classes, three engineered to overlap on temperature but separate on flow and pressure. Across a 1000-turn evaluation the zero-shot panel shows no significant difference from the classifier on detection but trails on classification, its errors concentrating on the confusable faults. Curated contrastive few-shot demonstrations and self-consistency voting then raise classification accuracy from 0.685 to 0.990, matching the supervised classifier (0.985) with no parameter updates and six labeled demonstrations; an ablation attributes the gain almost entirely to the demonstrations. Run as a continuous monitor across a nine-run fault-by-seed sweep, the agent catches every developing fault within one poll interval, and a confidence gate suppresses pre-onset false alarms whose rate is backend-dependent. As a first sim-to-real check, a detector trained purely on real BlueFors telemetry posts a real-hardware false-alarm rate of 6.4% and 100% recall on physics faults injected onto real held-out windows. All numbers are drawn verbatim from released run logs.

---


### 45. [AbICL: In-Context Learning for Antigen-Specific Antibody Affinity Ranking](https://arxiv.org/abs/2607.05846)

**<font color=#1a73e8>作者：</font>** Zhiyuan Chen, Jing Hu, Junzhe Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate ranking of antibody candidates according to their binding affinity is essential for therapeutic antibody discovery. However, existing methods treat affinity comparisons independently and ignore the contextual information encoded in other labeled comparisons, limiting their ability to capture antigen-specific binding landscapes. For many target antigens, a small number of experimentally characterized affinity comparisons are often available. An important question is whether the model can exploit these existing comparisons to infer antigen-specific ranking patterns that facilitate subsequent affinity ranking. This form of learning from labeled demonstrations closely resembles the paradigm of In-Context Learning, motivating us to revisit antibody affinity ranking from an ICL perspective. To this end, we propose AbICL, an ICL framework for antigen-specific antibody affinity ranking. AbICL combines a pretrained structural encoder with a context ranking head and is trained with an episodic meta-training strategy that enables the model to leverage support demonstrations for test-time adaptation without gradient updates. Experiments on the AbRank benchmark demonstrate that AbICL consistently outperforms existing ranking baselines across almost all data splits and evaluation benchmarks. Further analysis shows that the value of contextual demonstrations depends on how well they match the target inference task, and becomes increasingly pronounced under distribution shift and fine-grained affinity discrimination. These findings highlight the potential of ICL as an effective paradigm for antigen-specific antibody affinity ranking, particularly in challenging settings where a single global ranking function is insufficient.

---


### 46. [AVA-VLM: Adaptive Visual Attention-Vision Language Model for In-the-Wild Construction Site Monitoring](https://arxiv.org/abs/2607.05859)

**<font color=#1a73e8>作者：</font>** Younggun Kim, Taeheon Kim, Youngseo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are promising for construction-site monitoring, and recent construction-tailored VLMs have primarily adapted pretrained VLMs through direct QA-style fine-tuning from a single global image. We argue that this direct paradigm remains limited for in-the-wild deployment in terms of operational range, reliability under reduced-resolution inputs, and inference efficiency. To address these challenges, we propose AVA-VLM, an Adaptive Visual Attention-Vision Language Model that follows a human-inspired coarse-to-fine reasoning strategy. AVA-VLM first reasons over a low-resolution global image and selectively requests a high-resolution local crop only when detailed inspection is needed, similar to how a human inspector zooms in on hard-to-see yet important areas. We further introduce a region-aware Chain-of-Thought dataset that teaches the model when to inspect, where to crop, and how to use local evidence. Experiments show that AVA-VLM improves reliability under long-distance and reduced-resolution conditions while substantially reducing visual-token usage.

---


### 47. [Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization](https://arxiv.org/abs/2607.05861)

**<font color=#1a73e8>作者：</font>** Kaishen Wang, Tong Zheng, Xuehao Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) improve language model capabilities by generating explicit thinking traces before final answers. In factuality-oriented question answering (QA), such thinking often improves overall performance by helping the model recover relevant knowledge and refine its answers. However, we find that this benefit is not uniform at the instance level: explicit thinking can also overturn correct non-thinking answers and lead to factual drift. We refer to this failure mode as \emph{thinking-induced hallucination}. To explain this phenomenon, we formulate explicit thinking in factuality QA as a thinking residual over the model's direct-answer tendency, which can either recover missing knowledge or introduce unsupported associations. Based on this formulation, we propose MARGO, \underline{\textit{M}}ixed-Mode \underline{\textit{A}}dvantage \underline{\textit{R}}egularization for \underline{\textit{G}}rounded \underline{\textit{O}}ptimization, a reinforcement learning framework that uses non-thinking rollouts as same-model references in advantage estimation. By constructing mixed-mode rollout groups with both thinking and non-thinking trajectories, MARGO evaluates whether explicit thinking adds factual value beyond direct answering, thereby suppressing hallucination-prone thinking while preserving beneficial thinking behaviors. Experiments across multiple factuality-oriented QA benchmarks demonstrate that MARGO improves factual reliability over strong baselines, while evaluations on mathematical benchmarks show that it preserves general reasoning ability.

---


### 48. [Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from Verifiable Rewards for LLM Negotiations](https://arxiv.org/abs/2607.05863)

**<font color=#1a73e8>作者：</font>** Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Negotiation is a fundamental strategic interaction in management science, characterized by agents attempting to reach agreements while protecting private information, such as reservation costs and hidden valuations. A prevalent yet complex scenario involves a single seller negotiating concurrently with multiple buyers, each possessing heterogeneous, private budgets. In such settings, constrained by a limited number of communication turns, the seller must balance exploring the broader market to discover the highest valuation with concentrating sufficient turns on a single target buyer to secure the best possible outcome. Our analysis reveals a significant gap in standard Large Language Models (LLMs): while these models are linguistically proficient, they fail to act as effective economic decision-makers. Specifically, they exhibit a failure to explore the buyer pool, often fixating on the current highest bid rather than strategically investigating the market to discover latent high valuations.
In this paper, we propose a specialized training recipe using Reinforcement Learning from Verifiable Rewards (RLVR). By anchoring the reward function to objective economic outcomes, the strategic balance between market discovery and surplus extraction emerges natively through the learning process. Our results demonstrate that the trained seller undergoes a multi-stage strategic evolution, learning to leverage price anchoring and strategic probing to identify more profitable counterparties. The agent extracts a substantially higher surplus than frontier models by both improving its persuasive bargaining skills and consistently closing deals with high-value buyers. Finally, we show that our seller strategies generalize robustly to unseen buyer negotiation styles and budget distributions.

---


### 49. [Harrison.Rad 1.5 Technical Report: A radiology foundation model that can draft reports from images, priors and clinical context](https://arxiv.org/abs/2607.05880)

**<font color=#1a73e8>作者：</font>** Suneeta Mall, Vladimir Nekrasov, Ashnil Kumar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging demand is growing faster than the radiology workforce can expand, and reporting backlogs cannot be resolved through training and recruitment alone. The most direct opportunity is reducing the time and effort radiologists spend producing reports, a task that requires interpreting images, integrating clinical history and prior studies, and drafting structured findings. We present this http URL 1.5 (HR1.5), a radiology-specific multimodal large language model that accepts interleaved text and visual inputs and generates structured and unstructured text across plain-film radiology, spanning computed radiography, chest, musculoskeletal, abdominal, spine, and pelvic x-rays, and mammography. HR1.5 is trained through a three-stage pipeline: domain adaptation of a base language model on radiology reports, contrastive vision-encoder training with curriculum-based hard negatives on ~6 million image-report instances, and visual-question-answering fine-tuning on multi-turn conversations. We evaluate it with a Findings-Diagnosis scoring framework that extends RadGraph-XL entity extraction with ontology-based synonym matching and polarity-contradiction detection, benchmarked on RadBench, a simulated FRCR 2B Short Case examination scored against Angoff-method thresholds, ReXGradient, and internal multi-modality datasets. HR1.5 is the only system evaluated to meet the simulated FRCR passing standard and achieves the highest accuracy on closed-format clinical questions, across anatomical regions, on internal multi-body-part and mammography reporting, and on the primary clinically-aligned score for public chest reporting. We further examine explainability and model behaviour, including question-sensitive Grad-CAM heatmaps, attention analysis, and confidence estimation, to support responsible future evaluation toward clinical use, and a framework for clinically grounded assessment of report quality.

---


### 50. [More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges](https://arxiv.org/abs/2607.05904)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a language model against its own reference-free judgments (the premise of self-rewarding, self-play, and LLM-as-a-judge pipelines) assumes a model's verdict on a shown answer tracks correctness. We show it fails structurally: conditioned on a candidate, a judge scores plausibility, not correctness, leaving false-positive basins a policy learns to exploit. We measure this with a hidden-anchor audit: a held-out, cross-source exact-match check the judge never sees. On GSM8K with Qwen3 policies, self-play drives the judge's pass rate from 0.72 to 0.94 while true accuracy stays at 0.20 (three seeds). This reward hacking is not white-box gaming: the errors transfer across judge families (Qwen, Llama, Gemma) and scales, a strict three-judge ensemble still accepts 55% of them, and no plausibility-scoring defense closes the basin. The decisive variable is whether the judge commits an answer of its own before using the candidate: committing first drops the false-positive rate from 0.719 to 0.012, blind solving lifts discrimination to 0.96, and used as the training reward the de-anchored channel keeps false positives at zero, preventing the basin rather than only detecting it. A falsifiable bound (the gap is at most 1 - accuracy) predicts which regimes are exposed. The full arc replicates without training under best-of-N selection in code and competition math, and with a Gemma policy.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-98](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
