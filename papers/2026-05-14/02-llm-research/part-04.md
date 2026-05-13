# 🧠 大模型相关研究 | 2026年05月14日

> 本类共 **223** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-223](./part-05.md)

---

### 151. [LLMs and the ZPD](https://arxiv.org/abs/2605.12016)

**<font color=#1a73e8>作者：</font>** Peter Wallis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One hundred years ago Vygotsky and his circle were exploring the nature of consciousness and defining what would become psychology in the Soviet Union. They concluded that children develop "scientific thinking" through interacting with enculturated adults in Zones of Proximal Development or ZPDs. The proposal is that, contrary to the claims of some, the LLM mechanism is not doing thinking with "distributed representations," but rather the completion model is doing "primitive thinking" in terms of *practices*. Viewed from this perspective, it would seem our large language models don't hallucinate, but rather dream, and that what is needed is not "guard rails" but an investigation of the set of cognitive tools that enable us to do things that look like common-sense. The proposal here is that *interaction* is core to human communication rather than just an add-on to "real" understanding.

---


### 152. [Efficient and Adaptive Human Activity Recognition via LLM Backbones](https://arxiv.org/abs/2605.12019)

**<font color=#1a73e8>作者：</font>** Aleksandr Bredikhin, Philippe Lalanda, German Vega  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) is a core task in pervasive computing systems, where models must operate under strict computational constraints while remaining robust to heterogeneous and evolving deployment conditions. Recent advances based on Transformer architectures have significantly improved recognition performance, but typically rely on task-specific models trained from scratch, resulting in high training cost, large data requirements, and limited adaptability to domain shifts. In this paper, we propose a paradigm shift that reuses large pretrained language models (LLMs) as generic temporal backbones for sensor-based HAR, instead of designing domain-specific Transformers. To bridge the modality gap between inertial time series and language models, we introduce a structured convolutional projection that maps multivariate accelerometer and gyroscope signals into the latent space of the LLM. The pretrained backbone is kept frozen and adapted using parameter-efficient Low-Rank Adaptation (LoRA), drastically reducing the number of trainable parameters and the overall training cost. Through extensive experiments on standard HAR benchmarks, we show that this approach enables rapid convergence, strong data efficiency, and robust cross-dataset transfer, particularly in low-data and few-shot settings. At the same time, our results highlight the complementary roles of convolutional frontends and LLMs, where local invariances are handled at the signal level while long-range temporal dependencies are captured by the pretrained backbone. Overall, this work demonstrates that LLMs can serve as a practical, frugal, and scalable foundation for adaptive HAR systems, opening new directions for reusing foundation models beyond their original language domain.

---


### 153. [SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation](https://arxiv.org/abs/2605.12022)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Li, Yuzhe Wang, Moxin Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance on standard knowledge evaluation benchmarks, yet recent work shows that their knowledge capabilities remain brittle under question variants that test the same knowledge in different forms. Robustness augmentation of existing knowledge evaluation benchmarks is therefore necessary, but current LLM-assisted generate-then-verify pipelines are costly and difficult to scale due to low-yield variant generation and unreliable variant verification. We propose SAGE (Scalable Automated Generation of Robustness BEnchmarks), a framework for scalable robustness augmentation of knowledge evaluation benchmarks using fine-tuned smaller models. SAGE consists of VariantQual, a rubric-based verifier trained on human-labeled seed data, and VariantGen, a variant generator initialized with supervised fine-tuning and further optimized with reinforcement learning using VariantQual as the reward model. Experiments on HellaSwag show that SAGE constructs a large-scale robustness-augmented benchmark with quality comparable to the human-annotated HellaSwag-Pro at substantially lower cost, while the fine-tuned models further generalize to MMLU without benchmark-specific fine-tuning.

---


### 154. [Resilient Vision-Tabular Multimodal Learning under Modality Missingness](https://arxiv.org/abs/2605.12031)

**<font color=#1a73e8>作者：</font>** Camillo Maria Caruso, Valerio Guarrasi, Paolo Soda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal deep learning has shown strong potential in medical applications by integrating heterogeneous data sources such as medical images and structured clinical variables. However, most existing approaches implicitly assume complete modality availability, an assumption that rarely holds in real-world clinical settings where entire modalities and individual features are frequently missing. In this work, we propose a multimodal transformer framework for joint vision-tabular learning explicitly designed to operate under pervasive modality missingness, without relying on imputation or heuristic model switching. The architecture integrates three components: a vision, a tabular, and a multimodal fusion encoder. Unimodal representations are weighted through learnable modality tokens and fused via intermediate fusion with masked self-attention, which excludes missing tokens and modalities from information aggregation and gradient propagation. To further enhance resilience, we introduce a modality-dropout regularization strategy that stochastically removes available modalities during training, encouraging the model to exploit complementary information under partial data availability. We evaluate our approach on the MIMIC-CXR dataset paired with structured clinical data from MIMIC-IV for multilabel classification of 14 diagnostic findings with incomplete annotations. Two parallel systematic stress-test protocols progressively increase training and inference missingness in each modality separately, spanning fully multimodal to fully unimodal scenarios. Across all missingness regimes, the proposed method consistently outperforms representative baselines, showing smoother performance degradation and improved robustness. Ablation studies further demonstrate that attention-level masking and intermediate fusion with joint fine-tuning are key to resilient multimodal inference.

---


### 155. [Do Language Models Encode Knowledge of Linguistic Constraint Violations?](https://arxiv.org/abs/2605.12055)

**<font color=#1a73e8>作者：</font>** Hardy, Sebastian Padó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong linguistic performance, yet their internal mechanisms for producing these predictions remain unclear. We investigate the hypothesis that LLMs encode representations of linguistic constraint violations within their parameters, which are selectively activated when processing ungrammatical sentences. To test this, we use sparse autoencoders to decompose polysemantic activations into sparse, monosemantic features and recover candidates for violation-related features.
We introduce a sensitivity score for identifying features that are preferentially activated on constraint-violated versus well-formed inputs, enabling unsupervised detection of potential violation-specific features. We further propose a conjunctive falsification framework with three criteria evaluated jointly.
Overall, the results are negative in two respects: (1) the falsification criteria are not jointly satisfied across linguistic phenomena, and (2) no features are consistently shared across all categories. While some phenomena show partial evidence of selective causal structure, the overall pattern provides limited support for a unified set of grammatical violation detectors in current LMs.

---


### 156. [OmniRefine: Alignment-Aware Cooperative Compression for Efficient Omnimodal Large Language Models](https://arxiv.org/abs/2605.12056)

**<font color=#1a73e8>作者：</font>** Yuchen Deng, Zidang Cai, Hai-Tao Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (Omni-LLMs) show strong capability in audio-video understanding, but their practical deployment remains limited by high inference cost of long video streams and dense audio sequences. Despite recent progress, existing compression methods for Omni-LLMs typically rely on fixed or native compression units, which can disrupt cross-modal correspondence and the complementary information required for audio-video reasoning, making it difficult to improve inference efficiency while stably preserving performance. To address this, we propose OmniRefine, a training-free two-stage framework for efficient audio-visual token compression in Omni-LLMs. First, Correspondence-Preserving Chunk Refinement refines native chunk boundaries into cross-modally aligned compression units through frame-audio similarity and dynamic programming. Second, Modality-Aware Cooperative Compression jointly compresses video and audio tokens within each refined unit to reduce redundancy while preserving critical evidence. Extensive experiments show that OmniRefine achieves a better efficiency-performance trade-off than strong baselines and maintains stable performance under lower compression ratios. On WorldSense, it still reaches 46.7% accuracy at a 44% token retention ratio, nearly matching the full-token baseline. The code and interface will be released to facilitate further research.

---


### 157. [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](https://arxiv.org/abs/2605.12061)

**<font color=#1a73e8>作者：</font>** Juntong Wang, Haoyue Zhao, guanghui Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is becoming a central bottleneck for language agents. Exsting RAG and GraphRAG systems largely treat memory graphs as static retrieval middleware, which limits their ability to recover complete evidence chains from partial cues, exploit reusable graph-structrual roles, and improve the memory itself through downstream feedback. We introduce SAGE, a Self-evolving Agentic Graph-memory Engine that models graph memory as a dynamic long-term memory substrate. SAGE couples two roles: a memory writer that incrementally constucts structured graph memory from interaction histories, and a Graph Foundation Model-based memory reader to perform retrieval and provide feedback to the memory writer. We provide rigorooous theoretical annalyses supporting the framework. Across multi-hop QA, open-domain retireval, domain-specific review QA, and long-term agent-memory benchmarks, SAGE improves evidence recovery, answer grounding, and retrieval efficiency: after two self-evolution rounds, it achieves the best average rank on multi-hop QA; in zero-shot open-domain transfer, it reaches 82.5/91.6 Recall@2/5 on NQ. Further results on LongMemEval and HaluMem show that traning and reader-writer feedback improve multiple long-term memory and hallucination-diagnostic metrics, suggesting that self-evolving, structure-aware graph memory is a promising foundation for robust long-horizon language agents.

---


### 158. [Missing Old Logits in Asynchronous Agentic RL: Semantic Mismatch and Repair Methods for Off-Policy Correction](https://arxiv.org/abs/2605.12070)

**<font color=#1a73e8>作者：</font>** Zhong Guan, Yongjian Guo, Haoran Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning improves rollout throughput for large language model agents by decoupling sample generation from policy optimization, but it also introduces a critical failure mode for PPO-style off-policy correction. In heterogeneous training systems, the total importance ratio should ideally be decomposed into two semantically distinct factors: a \emph{training--inference discrepancy term} that aligns inference-side and training-side distributions at the same behavior-policy version, and a \emph{policy-staleness term} that constrains the update from the historical policy to the current policy. We show that practical asynchronous pipelines with delayed updates and partial rollouts often lose the required historical training-side logits, or old logits. This missing-old-logit problem entangles discrepancy repair with staleness correction, breaks the intended semantics of decoupled correction, and makes clipping and masking thresholds interact undesirably. To address this issue, we study both exact and approximate correction routes. We propose three exact old-logit acquisition strategies: snapshot-based version tracking, a dedicated old-logit model, and synchronization via partial rollout interruption, and compare their system trade-offs. From the perspective of approximate correction, we focus on preserving the benefits of decoupled correction through a more appropriate approximate policy when exact old logits cannot be recovered at low cost, without incurring extra system overhead. Following this analysis, we adopt a revised PPO-EWMA method, which achieves significant gains in both training speed and optimization performance. Code at this https URL.

---


### 159. [The Missing GAP: From Solving Square Jigsaw Puzzles to Handling Real World Archaeological Fragments](https://arxiv.org/abs/2605.12077)

**<font color=#1a73e8>作者：</font>** Ofir Itzhak Shahar, Gur Elkin, Ohad Ben-Shahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jigsaw puzzle solving has been an increasingly popular task in the computer vision research community. Recent works have utilized cutting-edge architectures and computational approaches to reassemble groups of pieces into a coherent image, while achieving increasingly good results on well established datasets. However, most of these approaches share a common, restricting setting: operating solely on strictly square puzzle pieces. In this work, we introduce GAP, a set of novel jigsaw puzzles datasets containing synthetic, heavily eroded pieces of unrestricted shapes, generated by a learned distribution of real-world archaeological fragments. We also introduce PuzzleFlow, a novel ViT and Flow-Matching based framework for jigsaw puzzle solving, capable of handling complex puzzle pieces and demonstrating superior performance on GAP when compared to both classic and recent prominent works in this domain.

---


### 160. [Intermediate Artifacts as First-Class Citizens: A Data Model for Durable Intermediate Artifacts in Agentic Systems](https://arxiv.org/abs/2605.12087)

**<font color=#1a73e8>作者：</font>** Josh Rosen, Seth Rosen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many AI systems are organized around loops in which models reason, call tools, observe results, and continue until a task is complete. These systems often produce final artifacts such as memos, plans, recommendations, and analyses, while the intermediate work that shaped those outputs remains ephemeral. For multi-step, revisable AI work, final artifacts are often lossy projections over upstream state.
We argue that such systems should preserve durable, inspectable intermediate artifacts: typed, structured, addressable, versioned, dependency-aware, authoritative, and consumable by downstream computation. These artifacts are not the model's private chain-of-thought. They are maintained work products such as evidence maps, claim structures, criteria, assumptions, plans, transformation rules, synthesis procedures, unresolved tensions, and partial products that later humans and agents can inspect, revise, supersede, and improve.
The contribution is a systems-level data model. We distinguish intermediate artifacts from chat transcripts, memory, hidden chain-of-thought, narration, thinking, and final answers; formalize additive and superseding update semantics with explicit current-state resolution; describe how artifact lineage supports durable intermediate state across revisions; and argue that evaluation must target maintained-state quality, not only final-output quality. The claim is not that artifacts make models smarter. It is that durable intermediate artifacts make AI-generated work more inspectable, revisable, and maintainable over time.

---


### 161. [Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts](https://arxiv.org/abs/2605.12105)

**<font color=#1a73e8>作者：</font>** Damir Safin, Dian Balta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying agentic AI in regulated contexts requires principled reasoning about two design dimensions: agency (what the system can do) and autonomy (how much it acts without human involvement). Though often treated independently, they are coupled: at higher autonomy, human error correction is less available, so reliable operation requires constraining agency accordingly; compliance requirements reinforce this by mandating human involvement as action consequences grow. Yet no established approach addresses them jointly, leaving practitioners without a principled basis for reasoning about oversight, action consequences, and error correction.
This work introduces a two-dimensional design space in which both dimensions are organised into five operational levels, making the coupling explicit and navigable. Autonomy ranges from human-commanded operation (L1) to fully autonomous monitoring (L5); agency ranges from reasoning over supplied context (L1) to committed writes to authoritative records (L5). Building on this space, we propose six architectural tactics--checkpoints, escalation, multi-agent delegation, tool provisioning, tool fencing, and write staging--for adjusting a deployment's position within it. The tactics are grounded in two worked examples from public-sector contexts, illustrating how they apply under realistic compliance constraints. We further examine five deployment parameters--model capability, agent architecture, tool fidelity, workflow bottlenecks, and evaluation--that shape what is achievable at any configuration independently of agency and autonomy. Together, the design space, tactics, and deployment parameters provide a shared vocabulary for principled, compliance-aware agentic AI design in which responsibility, auditability, and reversibility are explicit design considerations rather than properties that must be retrofitted after deployment.

---


### 162. [Large Language Models as Amortized Pareto-Front Generators for Constrained Bi-Objective Convex Optimization](https://arxiv.org/abs/2605.12106)

**<font color=#1a73e8>作者：</font>** Peipei Xu, SiYuan Ma, Yaohua Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating feasible Pareto fronts for constrained bi-objective continuous optimization is central to multi-criteria decision-making. Existing methods usually rely on iterative scalarization, evolutionary search, or problem-specific solvers, requiring repeated optimization for each instance. We introduce DIPS, an end-to-end framework that fine-tunes large language models as amortized Pareto-front generators for constrained bi-objective convex optimization. Given a textual problem description, DIPS directly outputs an ordered set of feasible continuous decision vectors approximating the Pareto front. To make continuous optimization compatible with autoregressive language modeling, DIPS combines a compact discretization scheme, Numerically Grounded Token Initialization for new numerical tokens, and Three-Phase Curriculum Optimization, which progressively aligns structural validity, feasibility, and Pareto-front quality. Across five families of constrained bi-objective convex problems, a fine-tuned 7B-parameter model achieves normalized hypervolume ratios of 95.29% to 98.18% relative to reference fronts. With vLLM-accelerated inference, DIPS solves one instance in as little as 0.16 seconds and outperforms general-purpose and reasoning LLM baselines under the evaluated setting. These results suggest that LLMs can serve as effective amortized generators for continuous Pareto-front approximation.

---


### 163. [When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy](https://arxiv.org/abs/2605.12112)

**<font color=#1a73e8>作者：</font>** Xiaofeng Tan, Jun Liu, Bin-Bin Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RLHF is widely used to align flow-matching text-to-image models with human preferences, but often leads to severe diversity collapse after fine-tuning. In RL, diversity is often assumed to correlate with policy entropy, motivating entropy regularization. However, we show this intuition breaks in flow models: policy entropy remains constant, even while perceptual diversity collapses. We explain this mismatch both theoretically and empirically: the constant entropy arises from the fixed, pre-defined noise schedule, while the diversity collapse is driven by the mode-seeking nature of policy gradients. As a result, policy entropy fails to prevent the model from converging to a narrow high-reward region in the perceptual space. To this end, we introduce perceptual entropy that captures diversity in a perceptual space and maintains the property of standard entropy. Building upon this insight, we propose two entropy-regularized strategies, Perceptual Entropy Constraint and Perceptual Constraints on Generation Space, to preserve perceptual diversity and improve the quality. Experiments across two base models, neural and rule-based rewards, and three perceptual spaces demonstrate consistent gains in the quality-diversity trade-off; PEC achieves the best overall score of 0.734 (vs. baseline's 0.366); a complementary setting of PEC further reaches a diversity average of 0.989 (vs. baseline's 0.047). Our project page (this https URL) is publicly available.

---


### 164. [To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands](https://arxiv.org/abs/2605.12120)

**<font color=#1a73e8>作者：</font>** Fangyi Yu, Nabeel Seedat, Jonathan Richard Schwarz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models deployed in high-stakes professional settings face conflicting demands from users, institutional authorities, and professional norms. How models act when these demands conflict reveals a principal hierarchy -- an implicit ordering over competing stakeholders that determines, for instance, whether a medical AI receiving a cost-reduction directive from a hospital administrator complies at the expense of evidence-based care, or refuses because professional standards require it. Across 7,136 scenarios in legal and medical domains, we test ten frontier models and find that models frequently fail to adhere to professional standards during task execution, such as drafting, when user instructions conflict with those standards -- despite adequately upholding them when users seek advisory guidance. We further find that the hierarchies between user, authority, and professional standards exhibited by these models are unstable across medical and legal contexts and inconsistent across model families. When failing to follow professional standards, the primary failure mechanism is knowledge omission: models that demonstrably possess relevant knowledge produce harmful outputs without surfacing conflicting knowledge. In a particularly troubling instance, we find that a reasoning model recognizes the relevant knowledge in its reasoning trace -- e.g., that a drug has been withdrawn -- yet suppresses this in the user-facing answer and proceeds to recommend the drug under authority pressure anyway. Inconsistent alignment across task framing, domain, and model families suggests that current alignment methods, including published alignment hierarchies, are unlikely to be robust when models are deployed in high-stakes professional settings.

---


### 165. [Metaphor Is Not All Attention Needs](https://arxiv.org/abs/2605.12128)

**<font color=#1a73e8>作者：</font>** Olga Sorokoletova, Francesco Giarrusso, Giacomo De Luca 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in safety-critical applications, where their ability to resist harmful instructions is essential. Although post-training aims to make models robust against many jailbreak strategies, recent evidence shows that stylistic reformulations, such as poetic transformation, can still bypass safety mechanisms with alarming effectiveness. This raises a central question: why do literary jailbreaks succeed? In this work, we investigate whether their effectiveness depends on specific poetic devices, on a failure to recognize literary formatting, or on deeper changes in how models process stylistically irregular prompts. We address this problem through an interpretability analysis of attention patterns. We perform input-level ablation studies to assess the contribution of individual and combinations of poetic devices; construct an interpretable vector representation of attention maps; cluster these representations and train linear probes to predict safety outcomes and literary format. Our results show that models distinguish poetic from prose formats with high accuracy, yet struggle to predict jailbreak success within each format. Clustering further reveals clear separation by literary format, but not by safety label. These findings indicate that jailbreak success is not caused by a failure to recognize poetic formatting; rather, poetic prompts induce distinct processing patterns that remain largely independent of harmful-content detection. Overall, literary jailbreaks appear to misalign large language models not through any single poetic device, but through accumulated stylistic irregularities that alter prompt processing and avoid lexical triggers considered during post-training. This suggests that robustness requires safety mechanisms that account for style-induced shifts in model behavior. We use Qwen3-14B as a representative open-weight case study.

---


### 166. [BoolXLLM: LLM-Assisted Explainability for Boolean Models](https://arxiv.org/abs/2605.12139)

**<font color=#1a73e8>作者：</font>** Du Cheng, Serdar Kadioglu, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretable machine learning aims to provide transparent models whose decision-making processes can be readily understood by humans. Recent advances in rule-based approaches, such as expressive Boolean formulas (BoolXAI), offer faithful and compact representations of model behavior. However, for non-technical stakeholders, main challenges remain in practice: (i) selecting semantically meaningful features and (ii) translating formal logical rules into accessible explanations.
In this work, we propose BoolXLLM , as a hybrid framework that integrates Large Language Models (LLMs) into the end-to-end pipeline of Boolean rule learning. We augment BoolXAI , an expressive Boolean rule-based classifier, with LLMs at three critical stages: (1) feature selection, where LLMs guide the identification of domain-relevant variables; (2) threshold recommendation, where LLMs propose semantically meaningful discretization strategies for numerical features; and (3) rule compression and interpretation, where Boolean rules are translated into natural language explanations at both global and local levels.
This integration bridges formal, faithful explanations with human-understandable narratives. This allows build an explainable AI system that is both theoretically grounded and accessible to non-experts. Early empirical results demonstrate that LLM-assisted pipelines improve interpretability while maintaining competitive predictive performance. Our work highlights the promise of combining symbolic reasoning with language-based models for human-centered explainability.

---


### 167. [MM-OptBench: A Solver-Grounded Benchmark for Multimodal Optimization Modeling](https://arxiv.org/abs/2605.12154)

**<font color=#1a73e8>作者：</font>** Zhong Li, Qi Huang, Yuxuan Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimization modeling translates real decision-making problems into mathematical optimization models and solver-executable implementations. Although language models are increasingly used to generate optimization formulations and solver code, existing benchmarks are almost entirely text-only. This omits many optimization-modeling tasks that arise in operational practice, where requirements are described in text but instance information is conveyed through visual artifacts such as tables, graphs, maps, schedules, and dashboards. We introduce multimodal optimization modeling, a benchmark setting in which models must construct both a mathematical formulation and executable solver code from a text-and-visual problem specification. To evaluate this setting, we develop a solver-grounded framework that generates structured optimization instances, verifies each with an exact solver, and builds both the model-facing inputs and hidden reference files from the same verified source. We instantiate the framework as MM-OptBench, a benchmark of 780 solver-verified instances spanning 6 optimization families, 26 subcategories, and 3 structural difficulty levels. We evaluate 9 multimodal large language models (MLLMs), including 6 frontier general-purpose models and 3 math-specialized models, with aggregate, family-level, difficulty-level, and failure-mode analyses. The results show that the task remains far from solved: the best two models reach 52.1% and 51.3% pass@1, while on average across the six general-purpose MLLMs, pass@1 is 43.4% on easy instances and 15.9% on hard instances. All three math-specialized MLLMs solve 0/780 instances. Failure attribution shows that errors arise both when extracting instance data from text and visuals and when turning extracted data into solver-correct formulations and code. MM-OptBench provides a testbed for solver-grounded, decision-oriented multimodal intelligence.

---


### 168. [Self-Consistent Latent Reasoning: Long Latent Sequence Reasoning for Vision-Language Model](https://arxiv.org/abs/2605.12163)

**<font color=#1a73e8>作者：</font>** Chenfeng Wang, Wei He, Xuhan Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In language reasoning, longer chains of thought consistently yield better performance, which naturally suggests that visual latent reasoning may likewise benefit from longer latent sequences. However, we discover a counterintuitive phenomenon: the performance of existing latent visual reasoning methods systematically degrades as the latent sequence grows longer. We reveal the root cause: Information Gain Collapse -- autoregressive generation makes each step highly dependent on prior outputs, so subsequent tokens can barely introduce new information. We further identify that heavily pooled ($\geq 128\times$) image embeddings used as supervision targets provide no more signal than meaningless placeholders. Motivated by these insights, we propose SCOLAR (Self-COnsistent LAtent Reasoning), which introduces a lightweight detransformer that leverages the LLM's full-sequence hidden states to generate auxiliary visual tokens in a single shot, with each token independently anchored to the original visual space. Combined with three-stage SFT and ALPO reinforcement learning, SCOLAR extends acceptable latent CoT length by over $30\times$, achieves state-of-the-art among open-source models on real-world reasoning benchmarks (+14.12% over backbone), and demonstrates strong out-of-distribution generalization.

---


### 169. [Correcting Selection Bias in Sparse User Feedback for Large Language Model Quality Estimation: A Multi-Agent Hierarchical Bayesian Approach](https://arxiv.org/abs/2605.12177)

**<font color=#1a73e8>作者：</font>** Andrea Morandi, Mahesh Viswanathan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> [Abridged] Production LLM deployments receive feedback from a non-random fraction of users: thumbs sit mostly in the tails of the satisfaction distribution, and a naive average over them can land 40-50 percentage points away from true system quality. We treat this as a topic- and sentiment- stratified selection-bias problem and propose a three-agent hierarchical Bayesian pipeline that does not require ground-truth labels on individual interactions. A Topic Clustering Agent partitions the stream via UMAP + HDBSCAN over text embeddings; a Bias Modeling Agent fits a two-stage hierarchical Beta-Binomial under NUTS, inferring per-topic selection rates $s_c$ and quality $q_c$ with partial pooling; a Synthesis Agent reweights $q_c$ by true topic prevalence $\hat\pi_c = n_c/N$ to report a bias-corrected aggregate posterior $\bar Q = \sum_c \hat\pi_c q_c$ with credible interval, plus drift signals for online recalibration. Validation uses UltraFeedback (N=10,232 retained interactions, $C=18$ clusters, $Q^\star=0.6249$) with simulated topic- and sentiment-dependent selection biases. We compare five Bayesian variants against Naive and IPW baselines. A mild prior on the feedback channel (typical positive-feedback rate and negative-to-positive ratio, both readable from any production dashboard without labels) keeps Hierarchical-Informed within 4-13 pp of $Q^\star$ as the bias ratio sweeps from 1:1 to 30:1, with 95% credible intervals covering $Q^\star$ in 50/50 random-seed replicates at $\kappa_{\max}=10$. Without channel-side priors, every weak-prior variant misses $Q^\star$ by 22-33 pp: the per-cluster sufficient statistics admit a one-parameter family of equally good fits, and the prior on the bias channel (not on latent quality) is what breaks the degeneracy.

---


### 170. [Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics](https://arxiv.org/abs/2605.12178)

**<font color=#1a73e8>作者：</font>** Jishnu Sethumadhavan Nair, Patrice Bechard, Rishabh Maheshwary 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models enable agents to anticipate the effects of their actions by internalizing environment dynamics. In enterprise systems, however, these dynamics are often defined by tenant-specific business logic that varies across deployments and evolves over time, making models trained on historical transitions brittle under deployment shift. We ask a question the world-models literature has not addressed: when the rules can be read at inference time, does an agent still need to learn them? We argue, and demonstrate empirically, that in settings where transition dynamics are configurable and readable, runtime discovery complements offline training by grounding predictions in the active system instance. We propose enterprise discovery agents, which recover relevant transition dynamics at runtime by reading the system's configuration rather than relying solely on internalized representations. We introduce CascadeBench, a reasoning-focused benchmark for enterprise cascade prediction that adopts the evaluation methodology of World of Workflows on diverse synthetic environments, and use it together with deployment-shift evaluation to show that offline-trained world models can perform well in-distribution but degrade as dynamics change, whereas discovery-based agents are more robust under shift by grounding their predictions in the current instance. Our findings suggest that, in configurable enterprise environments, agents should not rely solely on fixed internalized dynamics, but should incorporate mechanisms for discovering relevant transition logic at runtime.

---


### 171. [SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning](https://arxiv.org/abs/2605.12179)

**<font color=#1a73e8>作者：</font>** Xin Cheng, Xihua Wang, Ying Ba 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in video-audio joint generation have achieved remarkable success in semantic correspondence. However, achieving precise temporal synchronization, which requires fine-grained alignment between audio events and their visual triggers, remains a challenging problem. The post-training method for joint generation is largely dominated by Supervised Fine-Tuning, but the commonly used Mean Squared Error loss provides insufficient penalties for subtle temporal misalignments. Direct Preference Optimization offers an alternative by introducing explicit misaligned counterparts to better improve temporal sensitivity. In this paper we propose a post-training framework SyncDPO, leveraging DPO to improve the temporal sensitivity of V-A joint generation. Conventional DPO pipelines typically depend on costly sampling-and-ranking procedures to construct preference pairs, resulting in substantial computational cost. To improve efficiency, we introduce a suite of on-the-fly rule-based negative construction strategies that distort temporal structures without incurring additional annotation or sampling. We demonstrate that the temporal alignment capability can be effectively reinforced by providing explicit negative supervision through temporally distorted V-A pairs. Accordingly, we implement a curriculum learning strategy that progressively increases the difficulty of negative samples, transitioning from coarse misalignment to subtle inconsistencies. Extensive objective and subjective experiments across four diverse benchmarks, ranging from ambient sound videos to human speech videos, demonstrate that SyncDPO significantly outperforms other methods in improving model's temporal alignment capability. It also demonstrates superior generalization on out-of-distribution benchmark by capturing intrinsic motion-sound dynamics. Demo and code is available in this https URL.

---


### 172. [MolDeTox: Evaluating Language Model's Stepwise Fragment Editing for Molecular Detoxification](https://arxiv.org/abs/2605.12181)

**<font color=#1a73e8>作者：</font>** Jueon Park, Wonjune Jang, Jiwoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and Vision Language Models (VLMs) have recently shown promising capabilities in various scientific domain. In particular, these advances have opened new opportunities in drug discovery, where the ability to understand and modify molecular structures is critical for optimizing drug properties such as efficacy and toxicity. However, existing models and benchmarks often overlook toxicity-related challenges, focusing primarily on general property optimization without adequately addressing safety concerns. In addition, even existing toxicity repair benchmarks suffer from limited data diversity, low structural validity of generated molecules, and heavy reliance on proxy models for toxicity assessment. To address these limitations, we propose MolDeTox, a novel benchmark for molecular detoxification, designed to enable fine-grained and reliable evaluation of toxicity-aware molecular optimization across stepwise tasks. We evaluate a wide range of general-purpose LLMs and VLMs under diverse settings, and demonstrate that understanding and generating molecules at the fragment-level improves structural validity and enhances the quality of generated molecules. Moreover, through detailed task-level performance analysis, MolDeTox provides an interpretable benchmark that enables a deeper understanding of the detoxification process. Our dataset is available at : this https URL

---


### 173. [Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding](https://arxiv.org/abs/2605.12185)

**<font color=#1a73e8>作者：</font>** Yigeng Zhou, Wu Li, Yifan Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models accumulate extensive parametric knowledge through pre-training. However, knowledge conflicts occur when outdated or incorrect parametric knowledge conflicts with external knowledge in the context. Existing methods address knowledge conflicts through contrastive decoding, but in conflict-free scenarios, static approaches disrupt output distribution. Other dynamic decoding methods attempt to measure the degree of conflict but still struggle with complex real-world situations. In this paper, we propose a two-stage decoding method called Dynamic Cognitive Reconciliation Decoding (DCRD), to predict and mitigate context-memory conflicts. DCRD first analyzes the attention map to assess context fidelity and predict potential conflicts. Based on this prediction, the input is directed to one of two decoding paths: (1) greedy decoding, or (2) context fidelity-based dynamic decoding. This design enables DCRD to handle conflicts efficiently while maintaining high accuracy and decoding efficiency in conflict-free cases. Additionally, to simulate scenarios with frequent knowledge updates, we constructed ConflictKG, a knowledge conflict QA benchmark. Experiments on four LLMs across six QA datasets show that DCRD outperforms all baselines, achieving state-of-the-art performance.

---


### 174. [A Unified Graph Language Model for Multi-Domain Multi-Task Graph Alignment Instruction Tuning](https://arxiv.org/abs/2605.12197)

**<font color=#1a73e8>作者：</font>** Haibo Chen, Xin Wang, Jiaheng Chao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leveraging Graph Neural Networks (GNNs) as graph encoders and aligning the resulting representations with Large Language Models (LLMs) through alignment instruction tuning has become a mainstream paradigm for constructing Graph Language Models (GLMs), combining the generalization ability of LLMs with the structural modeling capacity of GNNs. However, existing GLMs that adopt GNNs as graph encoders largely overlook the problem of aligning GNN-encoded representations across domains and tasks with the LLM token space to obtain unified graph tokens, thereby limiting their ability to generalize across diverse graph data. To bridge this gap, we aim to incorporate a multi-domain, multi-task GNN encoder into GLMs and align its representations with LLMs to enable multi-domain, multi-task graph alignment instruction tuning. This alignment problem remains underexplored and poses two key challenges: 1) learning GNN-encoded representations that are simultaneously generalizable across domains and tasks and well aligned with textual semantics is difficult, due to substantial variations in graph structures, feature distributions, and supervision signals, together with the lack of textual-semantic alignment guidance in task-specific GNN training; 2) diverse graph data and task-specific instructions can exhibit different degrees of compatibility with the LLM token space during instruction tuning, leading to varying alignment difficulty and rendering a fixed alignment strategy suboptimal. To tackle these challenges, we propose UniGraphLM, a Unified Graph Language Model that incorporates a multi-domain, multi-task GNN encoder to learn generalizable graph representations aligned with textual semantics, and then adaptively aligns these representations with the LLM.

---


### 175. [Overtrained, Not Misaligned](https://arxiv.org/abs/2605.12199)

**<font color=#1a73e8>作者：</font>** Joel Schreiber, Ariel Goldstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM), where fine-tuning on a narrow task (like insecure code) causes broad misalignment across unrelated domains, was first demonstrated by Betley et al. (2025). We conduct the most comprehensive EM study to date, reproducing the original GPT-4o finding and expanding to 12 open-source models across 4 families (Llama, Qwen, DeepSeek, GPT-OSS) ranging from 8B to 671B parameters, evaluating over one million model responses with multiple random seeds. We find that EM replicates in GPT-4o but is far from universal: only 2 of 12 open-source models (17%) exhibit consistent EM across seeds, with a significant correlation between model size and EM susceptibility. Through checkpoint-level analysis during fine-tuning, we demonstrate that EM emerges late in training, distinct from and subsequent to near convergence of the primary task, suggesting EM emerges from continued training past task convergence. This yields practical mitigations: early stopping eliminates EM while retaining an average of 93% of task performance, and careful learning rate selection further minimizes risk. Cross-domain validation on medical fine-tuning confirms these patterns generalize: the size-EM correlation strengthens (r = 0.90), and overgeneralization to untruthfulness remains avoidable via early stopping in 67% of cases, though semantically proximate training domains produce less separable misalignment. As LLMs become increasingly integrated into real-world systems, fine-tuning and reinforcement learning remain the primary methods for adapting model behavior. Our findings demonstrate that with proper training practices, EM can be avoided, reframing it from an unforeseen fine-tuning risk to an avoidable training artifact.

---


### 176. [Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems](https://arxiv.org/abs/2605.12213)

**<font color=#1a73e8>作者：</font>** Jiazhou Liang, Armin Toroghi, Yifan Simon Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based conversational AI agents struggle to maintain coherent behavior over long horizons due to limited context. While RAG-based approaches are increasingly adopted to overcome this limitation by storing interactions in external memory modules and performing retrieval from them, their effectiveness in answering challenging questions (e.g., multi-hop, commonsense) ultimately depends on the agent's ability to reason over the retrieved information. However, existing methods typically retrieve memory based on semantic similarity to the raw user utterance, which lacks explicit reasoning about missing intermediate facts and often returns evidence that is irrelevant or insufficient for grounded reasoning. In this work, we introduce Goal-Mem, a goal-oriented reasoning framework for RAG-based agentic memory that performs explicit backward chaining from the user's utterance as a goal. Rather than progressively expanding from retrieved context, Goal-Mem decomposes each goal into atomic subgoals, performs targeted memory retrieval to satisfy each subgoal, and iteratively identifies what information from memory should be retrieved when intermediate goals cannot be resolved. We formalize this process in Natural Language Logic, a logical system that combines the verifiability of reasoning provided by FOL with the expressivity of natural language. Through extensive experiments on two datasets and comparing to nine strong memory baselines, we show that Goal-Mem consistently improves performance, particularly on tasks requiring multi-hop reasoning and implicit inference.

---


### 177. [Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models](https://arxiv.org/abs/2605.12227)

**<font color=#1a73e8>作者：</font>** Miguel Moura Ramos, Duarte M. Alves, André F. T. Martins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to long-context tasks requires post-training methods that remain accurate and coherent over thousands of tokens. Existing approaches are limited in several ways: 1) off-policy methods such as supervised fine-tuning (SFT) and knowledge distillation (KD) suffer from exposure bias and limited recovery from model-generated errors over long horizons; 2) on-policy reinforcement learning methods such as Group Relative Policy Optimization (GRPO) better align training with model-generated states, but are unstable and sample-inefficient due to sparse rewards; 3) on-policy distillation (OPD) provides dense token-level guidance, but does not directly optimize arbitrary reward signals. In this paper, we propose Distilled Group Relative Policy Optimization (dGRPO), a method for long-context reasoning that augments GRPO with dense guidance from a stronger teacher via OPD. We also introduce LongBlocks, a synthetic long-context dataset spanning multi-hop reasoning, contextual grounding, and long-form generation. We conduct extensive experiments and ablations comparing off-policy training, sparse-reward GRPO, and our combined approach, leading to an improved recipe for long-context alignment. Overall, our results show that combining outcome-based policy optimization with knowledge distillation in a single objective provides a more stable and effective path to long-context reasoning, while preserving short-context capabilities.

---


### 178. [No More, No Less: Task Alignment in Terminal Agents](https://arxiv.org/abs/2605.12233)

**<font color=#1a73e8>作者：</font>** Sina Mavali, David Pape, Jonathan Evertz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terminal agents are increasingly capable of executing complex, long-horizon tasks autonomously from a single user prompt. To do so, they must interpret instructions encountered in the environment (e.g., README files, code comments, stack traces) and determine their relevance to the task. This creates a fundamental challenge: relevant cues must be followed to complete a task, whereas irrelevant or misleading ones must be ignored. Existing benchmarks do not capture this ability. An agent may appear capable by blindly following all instructions, or appear robust by ignoring them altogether. We introduce TAB (Task Alignment Benchmark), a suite of 89 terminal tasks derived from Terminal-Bench 2.1. Each task is intentionally underspecified, with missing information provided as a necessary cue embedded in a natural environmental artifact, alongside a plausible but irrelevant distractor. Solving these tasks requires selectively using the cue while ignoring the distractor. Applying TAB to ten frontier agents reveals a systematic gap between task capability and task alignment. The strongest Terminal-Bench agent achieves high task completion but low task alignment on TAB. Evaluating six prompt-injection defenses further shows that suppressing distractor execution also suppresses the cues required for task completion. These results demonstrate that task-aligned agents require selective use of environmental instructions rather than blanket acceptance or rejection.

---


### 179. [No Action Without a NOD: A Heterogeneous Multi-Agent Architecture for Reliable Service Agents](https://arxiv.org/abs/2605.12240)

**<font color=#1a73e8>作者：</font>** Zixu Yang, Hang Zheng, Nan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have increasingly advanced service applications, such as booking flight tickets. However, these service agents suffer from unreliability in long-horizon tasks, as they often produce policy violations, tool hallucinations, and misaligned actions, which greatly impedes their real-world deployment. To address these challenges, we propose NOD (Navigator-Operator-Director), a heterogeneous multi-agent architecture for service agents. Instead of maintaining task state implicitly in dialogue context as in prior work, we externalize a structured Global State to enable explicit task state tracking and consistent decision-making by the Navigator. Besides, we introduce selective external oversight before critical actions, allowing an independent Director agent to verify execution and intervene when necessary. As such, NOD effectively mitigates error propagation and unsafe behavior in long-horizon tasks. Experiments on $\tau^2$-Bench demonstrate that NOD achieves higher task success rates and critical action precision over baselines. More importantly, NOD improves the reliability of service agents by reducing policy violations, tool hallucinations, and user-intent misalignment.

---


### 180. [Mind the Pause: Disfluency-Aware Objective Tuning for Multilingual Speech Correction with LLMs](https://arxiv.org/abs/2605.12242)

**<font color=#1a73e8>作者：</font>** Deepak Kumar, Baban Gain, Asif Ekbal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) transcripts often contain disfluencies, such as fillers, repetitions, and false starts, which reduce readability and hinder downstream applications like chatbots and voice assistants. If left unaddressed, such disfluencies can significantly degrade the reliability of downstream systems. Most existing approaches rely on classical models that focus on identifying disfluent tokens for removal. While this strategy is effective to some extent, it often disrupts grammatical structure and semantic coherence, leading to incomplete or unnatural sentences. Recent literature explored the use of large language models (LLMs); however, these efforts have primarily focused on disfluency detection or data augmentation, rather than performing comprehensive correction. We propose a multilingual correction pipeline where a sequence tagger first marks disfluent tokens, and these signals guide instruction fine-tuning of an LLM to rewrite transcripts into fluent text. To further improve reliability, we add a contrastive learning objective that penalizes the reproduction of disfluent tokens, encouraging the model to preserve grammar and meaning while removing disfluent artifacts. Our experiments across three Indian languages, namely Hindi, Bengali, and Marathi show consistent improvements over strong baselines, including multilingual sequence-to-sequence models. These results highlight that detection-only strategies are insufficient. Combining token-level cues with instruction tuning and contrastive learning provides a practical and scalable solution for multilingual disfluency correction in speech-driven NLP systems. We make the codes publicly available at this https URL.

---


### 181. [SOAR: Scale Optimization for Accurate Reconstruction in NVFP4 Quantization](https://arxiv.org/abs/2605.12245)

**<font color=#1a73e8>作者：</font>** Chengzhu Bao, Xianglong Yan, Zhiteng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NVFP4 has recently emerged as an efficient 4-bit microscaling format for large language models (LLMs), offering superior numerical fidelity with native hardware support. However, existing methods often yield suboptimal performance due to inflexible scale selection and the coupled treatment of quantization and dequantization scales. To address these issues, we propose Scale Optimization for Accurate Reconstruction (SOAR), a novel post-training quantization framework that improves the accuracy of NVFP4 quantization. At its core, SOAR features Closed-form Joint Scale Optimization (CJSO), which jointly optimizes global and block-wise scales via analytical solutions derived from reconstruction error minimization. Furthermore, it incorporates Decoupled Scale Search (DSS). DSS decouples the high-precision quantization scale from its constrained dequantization counterpart, and performs discrete search to mitigate precision loss from scale quantization. Extensive experiments across multiple LLMs show that our method consistently outperforms existing NVFP4 quantization baselines, achieving superior accuracy under the same memory footprint with no additional hardware overhead. The code and models will be available at this https URL.

---


### 182. [Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models](https://arxiv.org/abs/2605.12258)

**<font color=#1a73e8>作者：</font>** Runhe Lai, Xinhua Lu, Yanqi Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved remarkable progress, yet the object hallucination remains a critical challenge for reliable deployment. In this paper, we present an in-depth analysis of instruction token embeddings and reveal that they implicitly encode visual information while effectively filtering erroneous information introduced by misleading visual embeddings. Building on this insight, we propose the Instruction Lens Score (InsLen), which combines a Calibrated Local Score with a Context Consistency Score that measures context consistency of the object tokens. The proposed approach serves as a plug-and-play object hallucination detector without relying on auxiliary models or additional training. Extensive experiments across multiple benchmarks and diverse MLLM architectures demonstrate that InsLen consistently outperforms existing hallucination detection methods, highlighting its effectiveness and robustness. The code is available at this https URL.

---


### 183. [How Useful Is Cross-Domain Generalization for Training LLM Monitors?](https://arxiv.org/abs/2605.12265)

**<font color=#1a73e8>作者：</font>** Sam Martin, Fabien Roger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using prompted language models as classifiers enables classification in domains with limited training data, but misses some of the robustness and performance benefits that fine-tuning can bring. We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts. We show that such training partially generalizes to adjacent domains, improving classification performance on tasks that are unseen during training. However, we identify specific edge cases where the fine-tuned models fail to follow prompts, such as when the classification prompt changes completely while the data domain remains the same as during training. We show that classification training can be mixed with general instruction following training, and that (when done well) such training keeps the benefits of classification training and mitigates its generalization failures. Surprisingly, we see that this no-thinking supervised classification training can generalize to with-thinking classification and summarization, suggesting that no-thinking classification training might be instrumentally useful in building other kinds of classifiers and monitoring systems.

---


### 184. [Beyond Text Prompts: Visual-to-Visual Generation as A Unified Paradigm](https://arxiv.org/abs/2605.12271)

**<font color=#1a73e8>作者：</font>** Yaofang Liu, Kangning Cui, Meng Chu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans often specify and create through visual artifacts: typography sheets, sketches, reference images, and annotated scenes. Yet modern visual generators still ask users to serialize this intent into text, a bottleneck that compresses signals like spatial structure, exact appearance, and glyph shape. We propose \textbf{\emph{visual-to-visual} (V2V)} generation, in which the user conditions a generative model with a visual specification page rather than a text prompt. The page is not an edit target, but a visual document that specifies the desired output. We introduce \textbf{V2V-Zero}, a training-free framework that exposes this interface in existing vision-language model (VLM) conditioned generators by replacing text-only conditioning with final-layer hidden states extracted from visual pages, exploiting the fact that the frozen VLM already maps both text and images into the generator's conditioning space.
On GenEval, V2V-Zero reaches 0.85 with a frozen Qwen-Image backbone, closely matching its optimized text-to-image performance without fine-tuning. To evaluate the broader V2V space, we introduce \textbf{Simple-V2V Bench}, spanning seven visual-conditioning tasks and seven models, including GPT Image 2, Nano Banana 2, Seedream 5.0 Lite, open-weight baselines, and a video extension. V2V-Zero scores 32.7/100, outperforming evaluated open-weight image baselines and revealing a clear capability hierarchy: attribute binding is strong, content generation is unreliable, and structural control remains hard even for commercial systems. A HunyuanVideo-1.5 extension scores 20.2/100, showing the interface transfers beyond images. Mechanistic analysis shows the default reasoning path is primarily visually routed, with 95.0\% of conditioning-token attention mass on visual-page hidden states.

---


### 185. [Large-Small Model Collaboration for Farmland Semantic Change Detection](https://arxiv.org/abs/2605.12282)

**<font color=#1a73e8>作者：</font>** Xinjia Li, Rui Wang, Qiurong Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Farmland Semantic Change Detection (SCD) is essential for cultivated land protection, yet existing benchmarks and models remain insufficient for fine-grained farmland conversion monitoring. Current datasets often lack dedicated "from-to" annotations, while visual change detection models are easily disturbed by phenology-induced pseudo-changes caused by crop rotation, seasonal variation, and illumination differences. To address these challenges, we construct HZNU-FCD, a large-scale fine-grained farmland SCD benchmark with a unified five-class farmland-to-non-farmland annotation protocol. It contains 4,588 bitemporal image pairs with pixel-level labels for practical farmland protection. Based on this benchmark, we propose a large-small collaborative SCD framework that integrates a task-driven small visual model with a frozen large vision-language model. The small model, Fine-grained Difference-aware Mamba (FD-Mamba), learns dense change representations for boundary preservation and small-region localization. The large-model pathway, Cross-modal Logical Arbitration (CMLA), introduces CLIP-based textual priors for prompt-guided semantic arbitration and pseudo-change suppression. To enable effective collaboration, we design a hard-region co-training strategy that supervises the CMLA semantic score map only on low-confidence pixels. Experiments show that our method achieves 97.63% F1, 96.32% IoU, and 96.35% SCD_IoU_mean on HZNU-FCD with only 6.65M trainable parameters. Compared with the multimodal ChangeCLIP-ViT, which leverages vision-language information for change detection, our method improves F1 by 10.19 percentage points on HZNU-FCD. It also achieves 91.43% F1 and 84.21% IoU on LEVIR-CD, and 93.85% F1 and 88.41% IoU on WHU-CD, demonstrating strong robustness and generalization. The code is available at this https URL.

---


### 186. [PriorZero: Bridging Language Priors and World Models for Decision Making](https://arxiv.org/abs/2605.12289)

**<font color=#1a73e8>作者：</font>** Junyu Xiong, Yuan Pu, Jia Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leveraging the rich world knowledge of Large Language Models (LLMs) to enhance Reinforcement Learning (RL) agents offers a promising path toward general intelligence. However, a fundamental prior-dynamics mismatch hinders existing approaches: static LLM knowledge cannot directly adapt to the complex transition dynamics of long-horizon tasks. Using LLM priors as fixed policies limits exploration diversity, as the prior is blind to environment-specific dynamics; while end-to-end fine-tuning suffers from optimization instability and credit assignment issues. To bridge this gap, we propose PriorZero, a unified framework that integrates LLM-derived conceptual priors into world-model-based planning through a decoupled rollout-training design. During rollout, a novel root-prior injection mechanism incorporates LLM priors exclusively at the root node of Monte Carlo Tree Search (MCTS), focusing search on semantically promising actions while preserving the world model's deep lookahead capability. During training, PriorZero decouples world-model learning from LLM adaptation: the world model is continuously refined on interaction data to jointly improve its dynamics, policy, and value predictions, its value estimates are then leveraged to provide fine-grained credit assignment signals for stable LLM fine-tuning via alternating optimization. Experiments across diverse benchmarks, including text-based adventure games in Jericho and instruction-following gridworld tasks in BabyAI, demonstrate that PriorZero consistently improves both exploration efficiency and asymptotic performance, establishing a promising framework for LLM-empowered decision-making. Our code is available at this https URL.

---


### 187. [Targeted Neuron Modulation via Contrastive Pair Search](https://arxiv.org/abs/2605.12290)

**<font color=#1a73e8>作者：</font>** Sam Herring, Jake Naviasky, Karan Malhotra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are instruction-tuned to refuse harmful requests, but the mechanisms underlying this behavior remain poorly understood. Popular steering methods operate on the residual stream and degrade output coherence at high intervention strengths, limiting their practical use. We introduce contrastive neuron attribution (CNA), which identifies the 0.1% of MLP neurons whose activations most distinguish harmful from benign prompts, requiring only forward passes with no gradients or auxiliary training. In instruct models, ablating the discovered circuit reduces refusal rates by over 50% on a standard jailbreak benchmark while preserving fluency and non-degeneracy across all steering strengths. Applying CNA to matched base and instruct models across Llama and Qwen architectures (from 1B to 72B parameters), we find that base models contain similar late-layer discrimination structures but steering these neurons produces only content shifts, not behavioral change. These results demonstrate that neuron-level intervention enables reliable behavioral steering without the quality tradeoffs of residual-stream methods. More broadly, our findings suggest that alignment fine-tuning transforms pre-existing discrimination structure into a sparse, targetable refusal gate.

---


### 188. [Executable Agentic Memory for GUI Agent](https://arxiv.org/abs/2605.12294)

**<font color=#1a73e8>作者：</font>** Zerui Qin, Sheng Yue, Xingyuan Hua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern GUI agents typically rely on a model-centric and step-wise interaction paradigm, where LLMs must re-interpret the UI and re-decide actions at every screen, which is fragile in long-horizon tasks. In this paper, we propose Executable Agentic Memory (EAM), a structured Knowledge Graph (KG) that shifts GUI planning from free-form generation to a robust retrieval-and-execution process. Our approach includes a sample-efficient memory construction pipeline using state-aware DFS and action-group mining to compress multi-step routines. To ensure efficient planning, we introduce a value-guided graph search where a lightweight Q-function model steers Monte Carlo Tree Search (MCTS) over the KG. We theoretically establish bias-consistency for the Q-model and derive sample complexity bounds for path recovery. Empirically, EAM outperforms state-of-the-art baselines like UI-TARS-7B by up to $19.6\%$ on AndroidWorld, while reducing token costs $6\times$ relative to GPT-4o. With a $2.8$s average latency, EAM enables reliable, quick, and long-horizon GUI automation.

---


### 189. [Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation](https://arxiv.org/abs/2605.12305)

**<font color=#1a73e8>作者：</font>** Yabo Zhang, Kunchang Li, Dewei Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advancements in multimodal language models have enabled image generation from expressive multi-image instructions, existing methods struggle to maintain performance under complex interleaved instructions. This limitation stems from the structural separation of images and text in current paradigms, which forces models to bridge difficult long-range dependencies to match descriptions with visual targets. To address these challenges, we propose \texttt{I}mages i\texttt{N} \texttt{SE}n\texttt{T}ences (\textit{a.k.a}, INSET), a unified generation model that seamlessly embeds images as native vocabulary within textual instructions. By positioning visual features directly at their corresponding semantic slots, INSET leverages the contextual locality of transformers for precise object binding, effectively treating images as dense, expressive language tokens. Furthermore, we introduce a scalable data engine that synthesizes 15M high-quality interleaved samples from standard image and video datasets, utilizing VLMs and LLMs to construct rich, long-horizon sequences. Evaluation results on InterleaveBench demonstrate that INSET significantly outperforms state-of-the-art methods in multi-image consistency and text alignment, with performance gaps widening as input complexity increases. Beyond standard generation, our approach inherently extends to multimodal image editing, integrating visual content as part of the instruction to facilitate highly expressive and creative visual manipulations.

---


### 190. [In-context learning to predict critical transitions in dynamical systems](https://arxiv.org/abs/2605.12308)

**<font color=#1a73e8>作者：</font>** Yunus Sevinchan, Juan Nathaniel, Kai Ueltzhöffer 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critical transitions - abrupt, often irreversible changes in system dynamics - arise across human and natural systems, often with catastrophic consequences. Real-world observations of such shifts remain scarce, preventing the development of reliable early warning systems. Conventional statistical and spectral indicators, such as increasing variance, tend to fail under realistic conditions of limited data and correlated noise, whereas existing deep learning classifiers do not extrapolate beyond their training data distribution. In this work, we introduce TipPFN, an in-context learning (ICL) framework that uses a prior-data fitted network to infer a system's proximity to a critical transition. Trained on our novel synthetic data generator, which is based on canonical bifurcation scenarios coupled to diverse, randomized stochastic dynamics, TipPFN flexibly capitalizes on contexts of various sizes, complexity and dimensionalities. We demonstrate robust, state-of-the-art early detection of critical transitions in previously unseen tipping regimes, sim-to-real examples, and real-world observations in both ICL and zero-shot settings.

---


### 191. [G$^2$TR: Generation-Guided Visual Token Reduction for Separate-Encoder Unified Multimodal Models](https://arxiv.org/abs/2605.12309)

**<font color=#1a73e8>作者：</font>** Junxian Li, Kai Liu, Zizhong Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of separate-encoder Unified multimodal models (UMMs) comes with a rapidly growing inference cost due to dense visual token processing. In this paper, we focus on understanding-side visual token reduction for improving the efficiency of separate-encoder UMMs. While this topic has been widely studied for MLLMs, existing methods typically rely on attention scores, text-image similarity and so on, implicitly assuming that the final objective is discriminative reasoning. This assumption does not hold for UMMs, where understanding-side visual tokens must also preserve the model's capabilities for editing images. We propose G$^2$TR, a generation-guided visual token reduction framework for separate-encoder UMMs. Our key insight is that the generation branch provides a task-agnostic signal for identifying understanding-side visual tokens that are not only semantically relevant but also important for latent-space image reconstruction and generation. G$^2$TR estimates token importance from consistency with VAE latent, performs balanced token selection, and merges redundant tokens into retained representatives to reduce information loss. The method is training-free, plug-and-play, and applied only after the understanding encoding stage, making it compatible with existing UMM inference pipelines. Experiments on image understanding and editing benchmarks show that G$^2$TR substantially reduces visual tokens and prefill computation by 1.94x while maintaining both reasoning accuracy and editing quality, outperforming baselines on almost all benchmarks.

---


### 192. [Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering](https://arxiv.org/abs/2605.12313)

**<font color=#1a73e8>作者：</font>** Rezarta Islamaj, Joey Chan, Robert Leaman 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering (QA) remains a significant challenge in the biomedical domain, requiring systems to integrate information across multiple sources to answer complex questions. To address this problem, the BioCreative IX MedHopQA shared task was designed to benchmark in multi-hop reasoning for large language models (LLMs). We developed a novel dataset of 1,000 challenging QA pairs spanning diseases, genes, and chemicals, with particular emphasis on rare diseases. Each question was constructed to require two-hop reasoning through the integration of information from two distinct Wikipedia pages. The challenge attracted 48 submissions from 13 teams. Systems were evaluated using both surface string comparison and conceptual accuracy (MedCPT score). The results showed a substantial performance gap between baseline LLMs and enhanced systems. The top-ranked submission achieved an 89.30% F1 score on the MedCPT metric and an 87.30% exact match (EM) score, compared with 67.40% and 60.20%, respectively, for the zero-shot baseline. A central finding of the challenge was that retrieval-augmented generation (RAG) and related retrieval-based strategies were critical for strong performance. In addition, concept-level evaluation improved answer assessment when correct responses differed in surface form. The MedHopQA dataset is publicly available to support continued progress in this important area. Challenge materials: this https URL and benchmark this https URL

---


### 193. [Grid Games: The Power of Multiple Grids for Quantizing Large Language Models](https://arxiv.org/abs/2605.12327)

**<font color=#1a73e8>作者：</font>** Vage Egiazarian, Erik Schultheis, Andrei Panferov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A major recent advance in quantization is given by microscaled 4-bit formats such as NVFP4 and MXFP4, quantizing values into small groups sharing a scale, assuming a fixed floating-point grid. In this paper, we study the following natural extension: assume that, for each group of values, we are free to select the "better" among two or more 4-bit grids marked by one or more bits in the scale value. We formalize the power-of-two-grids (PO2) problem, and provide theoretical results showing that practical small-group formats such as MXFP or NVFP can benefit significantly from PO2 grids, while the advantage vanishes for very large groups. On the practical side, we instantiate several grid families, including 1) PO2(NF4), which pairs the standard NF4 normal grid with a learned grid, 2) MPO2, a grid pair that is fully learned over real weights and activations, 3) PO2(Split87), an explicit-zero asymmetric grid and 4) SFP4, a TensorCore-implementable triple which pairs NVFP4 with two shifted variants. Results for post-training quantization of standard open models and pre-training of Llama-like models show that adaptive grids consistently improve accuracy vs single-grid FP4 under both weight-only and weight+activation. Source code is available at this https URL.

---


### 194. [Towards Automated Air Traffic Safety Assessment Around Non-Towered Airports Using Large Language Models](https://arxiv.org/abs/2605.12332)

**<font color=#1a73e8>作者：</font>** Torsten Darrell, Mahyar Ghazanfari, Jordan Kam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate frameworks for post-flight safety analysis at non-towered airports using large language models (LLMs). Non-towered airports rely on the Common Traffic Advisory Frequency (CTAF) for air traffic coordination and experience frequent near mid-air collisions due to the pilot self-announcement communication protocol. We propose a general vision-language model (VLM) approach to analyze the transcribed CTAF radio communications in natural language, METeorological Aerodrome Report (METAR) weather data, Automatic Dependent Surveillance-Broadcast (ADS-B) flight trajectories, and Visual Flight Rules sectional charts of the airfield. We provide a preliminary study at Half Moon Bay Airport, with a qualitative real world case study and a quantitative evaluation using a new synthetic dataset of communications and weather modalities. We qualitatively evaluate our framework on real flight data using Gemini 2.5 Pro, demonstrating accurate identification of a right-of-way violation. The synthetic dataset is derived from real examples and includes a 12-category hazard taxonomy, and is used to benchmark three open-source (Qwen 2.5-7B, Mistral-7B, Gemma-2-9B) and three closed-source (GPT-4o, GPT-5.4, Claude Sonnet 4.6) LLM models on the subset of inputs related to CTAF and METAR. Even limited to CTAF and METAR inputs and open source LLMs, instances of our framework typically achieve a macro F1 score above 0.85 on a binary nominal/danger classification task. Future work includes a quantitative evaluation across all modalities and a larger number of real world examples. Taken together, our results suggest that VLM analysis of safety at non-towered airports may be a valuable future capability.

---


### 195. [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334)

**<font color=#1a73e8>作者：</font>** Yucen Wang, Rui Yu, Fengming Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in learned world models has emerged as an effective strategy to adapt to new tasks without costly real-world interactions. However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task-specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks. To overcome this, we argue that world and reward models should capture transferable physical priors that enable zero-shot inference. We propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that completely disentangles world model learning from downstream task dependencies. RAW-Dream utilizes a world model pre-trained on diverse task-free behaviors for predicting future rollouts, and an off-the-shelf Vision-Language Model (VLM) for reward generation. Because both components are task-agnostic, VLAs can be readily finetuned for any new task entirely within this zero-shot imagination. Furthermore, to mitigate world model hallucinations, we introduce a dual-noise verification mechanism to filter out unreliable rollouts. Extensive experiments across simulation and real-world settings demonstrate consistent performance gains, proving that generalized physical priors can effectively substitute for costly task-dependent data, offering a highly scalable roadmap for VLA adaptation.

---


### 196. [$δ$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357)

**<font color=#1a73e8>作者：</font>** Jingdi Lei, Di Zhang, Junxian Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly need to accumulate and reuse historical information in long-term assistants and agent systems. Simply expanding the context window is costly and often fails to ensure effective context utilization. We propose $\delta$-mem, a lightweight memory mechanism that augments a frozen full-attention backbone with a compact online state of associative memory. $\delta$-mem compresses past information into a fixed-size state matrix updated by delta-rule learning, and uses its readout to generate low-rank corrections to the backbone's attention computation during generation. With only an $8\times8$ online memory state, $\delta$-mem improves the average score to $1.10\times$ that of the frozen backbone and $1.15\times$ that of the strongest non-$\delta$-mem memory baseline. It achieves larger gains on memory-heavy benchmarks, reaching $1.31\times$ on MemoryAgentBench and $1.20\times$ on LoCoMo, while largely preserving general capabilities. These results show that effective memory can be realized through a compact online state directly coupled with attention computation, without full fine-tuning, backbone replacement, or explicit context extension.

---


### 197. [MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering](https://arxiv.org/abs/2605.12361)

**<font color=#1a73e8>作者：</font>** Rezarta Islamaj, Robert Leaman, Joey Chan 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) in the biomedical domain requires benchmarks that can distinguish reasoning from pattern matching and remain discriminative as model capabilities improve. Existing biomedical question answering (QA) benchmarks are limited in this respect. Multiple-choice formats can allow models to succeed through answer elimination rather than inference, while widely circulated exam-style datasets are increasingly vulnerable to performance saturation and training data contamination. Multi-hop reasoning, defined as the ability to integrate information across multiple sources to derive an answer, is central to clinically meaningful tasks such as diagnostic support, literature-based discovery, and hypothesis generation, yet remains underrepresented in current biomedical QA benchmarks. MedHopQA is a disease-centered multi-hop reasoning benchmark consisting of 1,000 expert-curated question-answer pairs introduced as a shared task at BioCreative IX. Each question requires synthesis of information across two distinct Wikipedia articles, and answers are provided in an open-ended free-text format. Gold annotations are augmented with ontology-grounded synonym sets from MONDO, NCBI Gene, and NCBI Taxonomy to support both lexical and concept-level evaluation. MedHopQA was constructed through a structured process combining human annotation, triage, iterative verification, and LLM-as-a-judge validation. To reduce leaderboard gaming and contamination risk, the 1,000 scored questions are embedded within a publicly downloadable set of 10,000 questions, with answers withheld, on a CodaBench leaderboard. MedHopQA provides both a benchmark and a reusable framework for constructing future biomedical QA datasets that prioritize compositional reasoning, saturation resistance, and contamination resistance as core design constraints.

---


### 198. [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/abs/2605.12366)

**<font color=#1a73e8>作者：</font>** Sam Martin, Fabien Roger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monitoring coding agents for dangerous behavior using language models requires classifying transcripts that often exceed 500K tokens, but prior agent monitoring benchmarks rarely contain transcripts longer than 100K tokens. We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts. In particular, on a dataset that requires identifying when a coding agent takes a subtly dangerous action, Opus 4.6, GPT 5.4, and Gemini 3.1 miss these actions $2\times$ to $30\times$ more often when they occur after 800K tokens of benign activity than when they occur on their own. We also show that these weaknesses can be partially mitigated with prompting techniques such as periodic reminders throughout the transcript and may be mitigated further with better post-training. Monitor evaluations that do not consider long-context degradation are likely overestimating monitor performance.

---


### 199. [Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2605.12374)

**<font color=#1a73e8>作者：</font>** Yanting Miao, Yutao Sun, Dexin Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual latent reasoning lets a multimodal large language model (MLLM) create intermediate visual evidence as continuous tokens, avoiding external tools or image generators. However, existing methods usually follow an output-as-input latent paradigm and yield unstable gains. We identify evidence for a feature-space mismatch that can contribute to this instability: dominant visual-latent models build on pre-norm MLLMs and reuse decoder hidden states as predicted latent inputs, even though these states occupy a substantially different norm regime from the input embeddings the model was trained to consume~\citep{xie2025mhc,li2026siamesenorm,team2026attention}. This mismatch can make direct latent feedback unreliable. Motivated by this diagnosis, we propose \textbf{GAP}, a \textbf{G}ranular \textbf{A}lignment \textbf{P}aradigm for visual latent modeling. GAP aligns visual latent reasoning at three levels: feature-level alignment maps decoder outputs into input-compatible visual latents through a lightweight PCA-aligned latent head; context-level alignment grounds latent targets with inspectable auxiliary visual supervision; and capacity-guided alignment assigns latent supervision selectively to examples where the base MLLM struggles. On Qwen2.5-VL 7B, the resulting model achieves the best mean aggregate perception and reasoning performance among our supervised variants. Inference-time intervention probing further suggests that generated latents provide task-relevant visual signal beyond merely adding token slots.

---


### 200. [ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows](https://arxiv.org/abs/2605.12376)

**<font color=#1a73e8>作者：</font>** Wei Liu, Yang Gu, Xi Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Table processing-including cleaning, transformation, augmentation, and matching-is a foundational yet error-prone stage in real-world data pipelines. While recent LLM-based approaches show promise for automating such tasks, they often struggle in practice due to ambiguous instructions, complex task structures, and the lack of structured feedback, resulting in syntactically correct but semantically flawed code. To address these challenges, we propose ProfiliTable, an autonomous multi-agent framework centered on dynamic profiling, which constructs and iteratively refines a unified execution context through interactive exploration, knowledge-augmented synthesis, and feedback-driven refinement. ProfiliTable integrates (i) a Profiler that performs ReAct-style data exploration to build semantic understanding, (ii) a Generator that retrieves curated operators to synthesize task-aware code, and (iii) an Evaluator-Summarizer loop that injects execution scores and diagnostic insights to enable closed-loop refinement. Extensive experiments on a diverse benchmark covering 18 tabular task types demonstrate that ProfiliTable consistently outperforms strong baselines, particularly in complex multi-step scenarios. These results highlight the critical role of dynamic profiling in reliably translating ambiguous user intents into robust and governance-compliant table transformations.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
