# 🧠 大模型相关研究 | 2026年06月02日

> 本类共 **168** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-168**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-168**

---

### 151. [BenHalluEval: A Multi-Task Hallucination Evaluation Framework for Large Language Models on Bengali](https://arxiv.org/abs/2605.31483)

**<font color=#1a73e8>作者：</font>** Shefayat E Shams Adib, Ahmed Alfey Sani, Ekramul Alam Esham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite Bengali being the sixth most spoken language in the world, no prior work has systematically evaluated hallucination in large language models (LLMs) for Bengali. We introduce BenHalluEval, a fine-grained hallucination evaluation framework for Bengali covering four tasks: Generative Question Answering (GQA), Bangla-English Code-Mixed QA, Summarization, and Reasoning. We construct 12,000 hallucinated candidates using GPT-5.4 across twelve task-specific hallucination types, drawn from three existing Bengali datasets, and evaluate seven LLMs spanning reasoning-oriented, multilingual, and Bengali-centric categories under a dual-track protocol that independently measures false-positive rate on ground-truth instances (Track A) and hallucination detection rate on hallucinated candidates (Track B). To jointly penalise both failure modes and prevent inflated scores from uniform response bias, we propose BenHalluScore, a dual-track calibration metric that ranges from 7.72% to 55.42% across models and tasks, revealing substantial variation in hallucination calibration. Chain-of-thought prompting, applied as a mitigation strategy, shifts response distributions without consistently improving hallucination discrimination. BenHalluEval establishes the first dedicated hallucination benchmark for Bengali and highlights the inadequacy of single-track and prompting-only evaluation approaches for low-resource language settings. The dataset and code are available at this https URL.

---


### 152. [LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories](https://arxiv.org/abs/2605.31492)

**<font color=#1a73e8>作者：</font>** Liwei Kang, Yee Whye Teh, Wee Sun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often solve reasoning problems by generating intermediate traces that explore and revise partial solutions. From a search perspective, these traces can be viewed as linearized search trees, where the model extends a partial solution, abandons it when it fails, and backtracks to try alternatives. Compared with traditional heuristic-guided search, such a policy has a potential advantage: it conditions on the whole search trace rather than only on the current local state. We first test whether LLMs utilize this advantage by comparing trace-conditioned reasoning policies against best-first search equipped with an LLM heuristic that only observes the current local state. Across three controlled reasoning environments, Blocks World, grid Navigation, and Sokoban, we find that raw access to search history alone is not enough to reliably outperform heuristic search. We then study one possible reason: in LLM reasoning traces, the underlying search tree is only implicitly represented, and when the model backtracks or switches branches, the trace does not explicitly identify which earlier search state is being revisited. We show that adding simple parent pointers to explicitly represent the linearized tree (LinTree) structure improves both task performance and search efficiency relative to implicit reasoning models and LLM-heuristic-guided search. These results suggest that search history becomes most useful when its tree structure is made explicit, motivating more structure-aware representations for LLM reasoning.

---


### 153. [Consolidating Rewarded Perturbations for LLM Post-Training](https://arxiv.org/abs/2605.31494)

**<font color=#1a73e8>作者：</font>** Zheyu Zhang, Shuo Yang, Gjergji Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training of language models is commonly framed as a sample-score-update loop implemented by gradient descent. A recent line of work, exemplified by RandOpt, relocates this loop to weight space, sampling Gaussian perturbations around a pretrained model and ensembling the top-K rewarded specialists at inference. While competitive with PPO and GRPO under matched training compute, this prediction-level ensemble incurs K forward passes per test example and does not extend cleanly to free-form generation. We ask whether the rewarded population can instead be folded into a single deployable model, replacing the inference-time ensemble with one consolidated update. A split-half analysis over 25 model-task pairs reveals reproducible low-rank structure in every case. We turn this geometry into CoRP (Consolidating Rewarded Perturbations), a gradient-free operator that combines reward-weighted aggregation, compatibility-aware reweighting, and a held-out validation gate, with no gradient flowing through the language model. Across five language models from 0.5B to 8B and five tasks covering math, code, and creative writing, CoRP improves the base model by 8.1 points on average. Using one tenth of RandOpt's perturbation budget, CoRP exceeds single-inference RandOpt by 6.5 points and recovers more than half of the gain of the 50-pass majority-vote ensemble, at one forward pass per test example.

---


### 154. [When Are Multimodal Predictions Biologically Supported? A Diagnostic Evaluation Framework](https://arxiv.org/abs/2605.31504)

**<font color=#1a73e8>作者：</font>** Dylan Steiner, Gustavo Arango-Argoty, Gerald Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal models in oncology can produce accurate predictions, but accurate prediction does not reveal whether the model has learned biology that is shared across modalities, biology confined to one modality, or spurious correlations that reflect confounders rather than genuine biology. We introduce DECAT, a model-agnostic post-hoc evaluation framework that classifies multimodal representations into four diagnostic scenarios for a given task and modality, using five null-referenced metrics and a rule-based decision procedure. The framework operates on learned representations, requires no knowledge of which specific confounder is present, and returns indeterminate when the evidence is insufficient. We validate DECAT on synthetic data across four multimodal model classes (over 2,500 trained representations) and on real data from 8,979 TCGA patients, evaluating both multimodal embeddings and five pretrained pathology foundation models. Entangled models (e.g., CLIP) achieve near-perfect shared biology detection but falsely claim shared biology in the majority of cases where it is absent on real foundation model embeddings. This false claim rate increases with confound strength so that larger cohorts and stronger representations produce more confident but still incorrect diagnoses. Applied to both multimodal TCGA embeddings and five pathology foundation models without paired RNA, DECAT detects confounding invisible to AUROC without requiring the confounder labels, as confirmed by post-hoc stratification.

---


### 155. [Skill Reuse as Compression in Agentic RL](https://arxiv.org/abs/2605.31509)

**<font color=#1a73e8>作者：</font>** Zhikun Xu, Yu Feng, Jacob Dineen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents trained with reinforcement learning (RL) often learn brittle, task-specific shortcuts. We hypothesize that agents generalize better when their successful trajectories are structurally compressible, decomposed into a small set of reusable abstract patterns. To formalize this, we introduce ReuseRL, which grounds agentic RL in the Minimum Description Length (MDL) principle. ReuseRL extracts a shared skill dictionary from successful trajectories and augments the RL objective with a segmentation cost, explicitly penalizing idiosyncratic behaviors that encode poorly. We prove a PAC-Bayes generalization bound for this compression penalty. Across ALFWorld, TextWorld-Cooking, and Countdown-Stepwise, ReuseRL improves in- and out-of-distribution success over vanilla GRPO and strong round-length baselines.

---


### 156. [Reliable Multilingual Orthopedic Decision Support from Clinical Narratives: Language-Aware Adaptation and Verification-Guided Deferral](https://arxiv.org/abs/2605.31512)

**<font color=#1a73e8>作者：</font>** Danish Ali, Li Xiaojian, Sundas Iqbal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual orthopedic decision support remains challenging in low-resource healthcare settings, where clinical narratives contain specialized terminology, mixed scripts, incomplete evidence, label imbalance and language-dependent documentation patterns. This article presents a reliability-oriented framework for classifying free-text orthopedic notes in English, Hindi and Punjabi. We compare task-aligned multilingual transformer encoders, a task-fine-tuned DistilBERT baseline, zero-shot instruction-tuned large language models (LLMs) and a domain-adaptive encoder, IndicBERT-HPA. IndicBERT-HPA augments IndicBERT with language-aware orthopedic adapter heads to support clinically relevant multilingual representation learning. Evaluation extends beyond aggregate accuracy to per-class performance, ROC-AUC, AUPRC, expected calibration error, cross-language stability and robustness under controlled balanced and natural-prevalence distributions. The evaluated zero-shot LLMs remain substantially less effective than task-adapted encoders for closed-set classification, with language-dependent instability. Under natural clinical prevalence, IndicBERT-HPA achieves the strongest overall performance, reaching an averaged Macro-F1 of 0.8792, Macro-AUROC of 0.894 and AUPRC of 0.902. We further implement a deterministic selective-verification layer combining confidence gating, evidence-consistency checking and language-risk screening. On a randomly selected held-out 5,000-record subset, it achieves 84.4% selective accuracy and 0.76 selective Macro-F1 at 72.3% coverage, compared with 71.5% accuracy and 0.65 Macro-F1 for accept-all prediction. These results support reliability-oriented multilingual clinical decision support with explicit deferral.

---


### 157. [Personalize Your Large Vision-language Models With In-context Prompt Tuning](https://arxiv.org/abs/2605.31513)

**<font color=#1a73e8>作者：</font>** Yanshu Li, Jiaqian Li, Kuai Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated strong general multimodal capability and are increasingly deployed in downstream systems. This trend has driven growing interest in LVLM personalization, which aims to enable models to quickly and effectively learn out-of-distribution multimodal concepts to meet user-specific needs. However, many existing methods rely on inference-time training, which reduces efficiency. They also struggle to maintain accuracy in complex multi-image, multi-concept settings. These limitations restrict the broader deployment of LVLM-based systems. Therefore, this paper proposes in-context prompt tuning (ICPT). Specifically, ICPT employs a lightweight projection module capable of operating in complex scenarios to extract fine-grained visual semantics from multiple reference images, seamlessly transforming these features alongside identity-label mappings into continuous prompts. To maximize computational efficiency, this module adaptively determines the prompt length based on the intrinsic visual complexity of each concept. Crucially, to overcome the environmental biases and cross-concept interference prevalent in real-world applications, we introduce two novel geometric regularizations. These constraints refine prompt representations by decoupling key identities from transient environmental states and separating concepts to avoid semantic confusion. Extensive experiments show that ICPT achieves state-of-the-art personalization accuracy across diverse tasks and LVLM backbones.

---


### 158. [If LLMs Have Human-Like Attributes, Then So Does Age of Empires II](https://arxiv.org/abs/2605.31514)

**<font color=#1a73e8>作者：</font>** Adrian de Wynter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much research has been carried out on large language models (LLMs) and LLM-powered agentic workflows. However, many works within the field state emergence of, ascribe to, or assume, generalised anthropomorphic attributes to them (e.g., morality or understanding of natural language). Our goal is not to argue in favour or against the existence of these attributes, but to point out that these conclusions could be incorrect. For this we build and train a simple neural network on the videogame Age of Empires II, and note that any entity in a sufficiently-powerful substrate, such as LEGO or the Greater Boston Area, could also present such attributes. Hence, the purported anthropomorphic attributes of LLMs are empirically non-unique: although some properties (e.g., responses to prompts) could remain constant, others, such as the interpretation of their perceived behaviour, might change with the substrate. Thus, any empirically-grounded discussion requires explicit measurement criteria; otherwise the interpretation is left to the representation. We then show that assuming that these attributes exist or not in a system, independent of the substrate and in a generalised way, leads to either circular or uninformative conclusions, regardless of the experimenter's viewpoint on the subject. Finally we propose a 'null' assumption, where one assumes LLM non-uniqueness instead of assuming anthropomorphic attributes to set up an experiment, along with examples of it. We also discuss potential objections to our work, briefly survey the field, and prove that \textit{Age of Empires II} is functionally- and Turing-complete.

---


### 159. [Preference-Aware Rubric Learning for Personalized Evaluation](https://arxiv.org/abs/2605.31545)

**<font color=#1a73e8>作者：</font>** Yilun Qiu, Xiaoyan Zhao, Yang Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve from general-purpose assistants to user-centric agents, personalization has become central to aligning model behavior with individual preferences, making the evaluation of personalized alignment a critical bottleneck. Existing evaluation methods-ranging from automatic metrics to LLM-as-a-judge approaches-fail to capture subjective, user-specific preferences embedded in long-term interaction histories. We identify three essential principles for reliable and effective personalized evaluation: Representativeness, User-Consistency, and Discriminativeness. To address these principles, we introduce Personalized Evaluation as Learning, a paradigm that formulates personalized evaluation as a learning problem rather than a static judgment. Under this paradigm, we propose PARL (Preference-Aware Rubric Learning for Personalized Evaluation), a framework that learns to induce preference-aware evaluation rubrics directly from raw user histories and performs a self-validation mechanism to ensure consistency with the user's preferences. PARL integrates rubric induction with a discriminative reinforcement learning objective that contrasts user-authored responses against competitive personalized model outputs, enabling the learned rubrics to capture precise, user-specific decision boundaries. Experiments on real-world personalized text generation tasks show that PARL consistently induces high-fidelity rubrics that reliably identify user-aligned responses and generalize across users and tasks, while capturing stable stylistic preferences and fine-grained evaluative patterns. To ensure reproducibility, our code is available at this https URL.

---


### 160. [Semantic Triplet Restoration: A Novel Protocol for Hierarchical Table Understanding in Large Language Models](https://arxiv.org/abs/2605.31550)

**<font color=#1a73e8>作者：</font>** Yibin Zhao, Fangxin Shang, Dingrui Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Table question answering requires models to recover semantic relations encoded implicitly by two-dimensional layout, merged cells, and hierarchical headers. Current pipelines typically use HTML or Markdown as intermediate table representations, but these layout-oriented serializations introduce markup overhead and require large language models to infer header-cell alignments from row and column spans. We propose Semantic Triplet Restoration (STR), a protocol that rewrites each cell as an atomic fact <item path, feature path, value>, where the item path specifies the row-wise entity, the feature path specifies the hierarchical attribute, and the value contains the cell content. We also present TripletQL, a lightweight query-aware router that uses STR to select an appropriate rendering or filtered subset of triplets for each question. Across four Chinese and English table-QA benchmarks, STR matches or improves upon HTML-based baselines while reducing input tokens. The relative benefit grows for smaller language models and longer table contexts, suggesting that explicit semantic representations are especially useful under constrained inference budgets. Code and data are available at this https URL .

---


### 161. [Vision-Language Models Suppress Female Representations Under Ambiguous Input](https://arxiv.org/abs/2605.31556)

**<font color=#1a73e8>作者：</font>** Arnau Marin-Llobet, Simon Henniger, Mahzarin R. Banaji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alignment teaches vision-language models (VLMs) to avoid expressing demographic biases, and when gender is clearly visible they largely succeed. Far less is known about ambiguous inputs (a worker in full gear, a figure seen from behind) cases common in practice yet rarely studied. We find that minimal prompting pressure exposes occupation-gender defaults when prompting ambiguous input images, with models collapsing to male even for strongly female-stereotyped occupations. But do these outputs reflect what models actually encode internally? We introduce LALS (Latent Association Leaning Score), a zero-shot metric that projects visual-token activations into the model's text-embedding space to measure concept associations per token and layer. Across 15 occupations, over 800 gender-ambiguous images, and four VLMs, internal representations and outputs are systematically decoupled: models often encode a female association internally yet output male. Layer-wise analysis reveals an asymmetric filter -- male signal amplifies end-to-end while female signal peaks mid-network and is suppressed before generation -- and a color ablation shows that culturally loaded visual cues such as clothing color further modulate these internal associations.

---


### 162. [What Am I Missing? Question-Answering as Hidden State Probing](https://arxiv.org/abs/2605.31561)

**<font color=#1a73e8>作者：</font>** Chu Fei Luo, Samuel Dahan, Xiaodan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time reasoning has become a significant field of study since the introduction of chain-of-thought reasoning in large language models (LLMs). However, the mechanisms of this reasoning process are still under-explored -- from the same input prompt, and even the same partial solution, LLMs can produce varied answers if sampled multiple times. We propose to leverage question-asking as an inference-time intervention that articulates information about the model's hidden state. To achieve that, we present a student-teacher setting where a student asks questions to a teacher. We train a probe on the student's hidden state before and after asking a question and find it is predictive of the trajectory's final correctness, even before generating the teacher's answer. This suggests there is a meaningful signal from the self-diagnosis that occurs during question generation rather than information transfer from the teacher. We then frame question-asking as a sequential decision problem, using this probe as a quality score, and define a gating policy to ask questions that maximize likelihood of correctness. We find that the success of question-asking as an intervention is largely dependent on the model's self-consistency. Our empirical results show a gap between detection and recovery; while our gating policy captures model correctness and uncertainty, interventions are equally likely to harm correct trajectories as they are to recover incorrect ones. This gap between diagnosis and correction has broader implications on language models' capacity for self-refinement under uncertainty.

---


### 163. [What Gets Unmasked First? Trajectory Analysis of Diffusion Models for Graph-to-Text Generation](https://arxiv.org/abs/2605.31564)

**<font color=#1a73e8>作者：</font>** Qing Wang, Jacob Devasier, Chengkai Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of masked diffusion language models (MDLMs) for graph-to-text generation. We analyze MDLM generation trajectories -- the order in which tokens are unmasked during iterative decoding -- and find that, unlike autoregressive LLMs which generate text linearly, MDLMs naturally prioritize entities first, followed by relational and function words, with structural tokens resolved last. We further identify a previously undocumented failure mode of supervised fine-tuning: SFT disrupts this strategy by prematurely anchoring structural sentence-ending tokens early in the decoding trajectory, effectively fixing the output length which can lead to omitted or hallucinated information. To address this, we propose lambda-scaled structural decoding, a training-free inference-time modification that downweights structural token confidence and recovers +9.4 BLEU-4. Finally, we introduce Graph-LLaDA, which integrates a Graph Transformer encoder into LLaDA's decoding process to explicitly incorporate relational graph structure. Cross-dataset evaluation on LAGRANGE reveals that previous baselines overfit to dataset-specific patterns, while LLM- and MDLM-based approaches generalize significantly better.

---


### 164. [Giving Sensors a Voice: Multimodal JEPA for Semantic Time-Series Embeddings](https://arxiv.org/abs/2605.31580)

**<font color=#1a73e8>作者：</font>** Utsav Dutta, Gerardo Pastrana, Sina Khoshfetrat Pakazad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based architectures have advanced sequence modeling in language and vision, yet general-purpose representation learning for heterogeneous multivariate time series remains underexplored. We introduce CHARM (Channel-Aware Representation Model), which incorporates channel-level textual descriptions into a Transformer encoder equivariant to channel order. CHARM is trained with a Joint Embedding Predictive Architecture (JEPA) and a novel loss promoting informative, temporally stable embeddings; latent-space prediction encourages robustness to sensor noise while description-aware gating provides interpretability through learned inter-channel relationships. Across anomaly detection, classification, and short- and long-term forecasting, the learned embeddings achieve strong performance using only a linear probe. Performance is driven primarily by the JEPA objective and conditioning architecture, with text descriptions serving as channel identifiers for cross-dataset generalization.

---


### 165. [LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards](https://arxiv.org/abs/2605.31584)

**<font color=#1a73e8>作者：</font>** Nianyi Lin, Jiajie Zhang, Lei Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning remains a central challenge for large language models, which often fail to locate and integrate key information in extensive distracting content. Reinforcement learning with verifiable rewards (RLVR) has shown promise for this task, yet existing methods are limited by low-confusability distractors and sparse, outcome-only reward signals that cannot supervise intermediate reasoning steps. To address these issues, we introduce \textsc{LongTraceRL}. For data construction, we generate multi-hop questions via knowledge graph random walks and leverage search agent trajectories to build \emph{tiered distractors}: documents the agent read but did not cite (high confusability) and documents that appeared in search results but were never opened (low confusability), producing training contexts that are far more challenging than those built by random sampling or one-shot search. For reward design, we propose a \emph{rubric reward} that uses the gold entities along each reasoning chain as fine-grained, entity-level process supervision. This rubric reward is applied only to responses with correct final answers (positive-only strategy), distinguishing the reasoning quality among correct responses and preventing reward hacking. Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that \textsc{LongTraceRL} consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning. Codes, datasets and models are available at \href{this https URL}{this https URL}.

---


### 166. [Language Models Learn Constructional Semantics, Not To Mention Syntax: Investigating LM Understanding of Paired-Focus Constructions](https://arxiv.org/abs/2605.31586)

**<font color=#1a73e8>作者：</font>** Wesley Scivetti, Ethan Wilcox, Nathan Schneider 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grasping the semantics of rare constructions (form-meaning pairings) has been shown to be a challenging problem that has currently only been solved by the largest LLMs. It remains an open question if open-source models have robust constructional understanding, and if so, what learning dynamics underlie the acquisition of this knowledge. Focusing on a set of rare Paired-Focus constructions in English (e.g. "let alone", "much less"), we construct a novel dataset to test their meanings using both scalar adjectival semantics and general world knowledge. Testing a wide range of models differing in parameter count, architecture, and pretraining dataset size, we find that several modestly sized models are sensitive to both the forms and the meanings of Paired-Focus constructions, though models trained on human-scale data fail at all meaning evaluations. Turning to training dynamics for a set of open-checkpoint models, we find that Paired-Focus understanding emerges later in training than Paired-Focus syntactic knowledge, and that learning of Paired-Focus semantics is correlated with gains in some domains of world knowledge. Overall, our empirical results support the conclusion that modestly sized open-source models can grasp the rare Paired-Focus constructions, and demonstrate a connection between knowledge of Paired-Focus constructions and other meaning domains.

---


### 167. [SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models](https://arxiv.org/abs/2605.31597)

**<font color=#1a73e8>作者：</font>** Olaf Dünkel, Basavaraj Sunagad, Haoran Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measuring structured object understanding in vision foundation models remains challenging due to inconsistent evaluation protocols and limited part-level supervision. Semantic correspondence (SC) evaluates this capability by testing whether object parts can be matched across instances and categories under large variations in appearance, viewpoint, and geometry. To enable a systematic SC evaluation, we introduce SOCO, a new benchmark for Semantic Object Correspondence that introduces a taxonomy of correspondence types and provides consistent, functionally meaningful keypoint annotations across 100 categories and over 1M correspondence pairs. In addition, SOCO includes keypoint language descriptions, enabling the evaluation of large vision-language models (LVLMs) and their fine-grained part-level understanding. Comprehensive experiments reveal that (i) vision foundation backbones encode strong semantic structure but transfer correspondences poorly across related categories and only partially capture object-part position, (ii) LVLMs are stronger at text-prompted part localization than at visual-reference cross-image matching, exposing a gap between language-grounded localization and fine-grained visual correspondence, and (iii) correspondence performance predicts performance on dense downstream tasks, including segmentation, tracking, 3D pose estimation, and 3D detection, more strongly than ImageNet classification. Together, these findings position SOCO as a benchmark for structured, part-level representation quality in vision and multimodal foundation models.

---


### 168. [Representation Forcing for Bottleneck-Free Unified Multimodal Models](https://arxiv.org/abs/2605.31604)

**<font color=#1a73e8>作者：</font>** Yuqing Wang, Zhijie Lin, Ceyuan Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) aim to handle perception and generation in a single model. Yet existing UMMs still rely on a frozen, separately pretrained VAE for image generation, imposing a structural bottleneck. Naively removing it introduces a quality gap, as the model must learn both high-level structure and low-level details from raw pixels. In this paper, we propose Representation Forcing (RF), a technique that closes this gap by making representation prediction a native capability of the model. Concretely, RF forces the decoder to autoregressively predict visual representations as intermediate tokens before pixels; these tokens then stay in context to guide pixel diffusion within the same backbone. By turning representations from perception outputs into generation targets, RF eliminates the need for any external generative latent space. We find that RF benefits both understanding and generation. On image generation, our pixel-space model with RF matches state-of-the-art VAE-based unified models. On image understanding, pixel-space RF generally outperforms its VAE-based variant. Together, these results offer an effective step toward end-to-end, bottleneck-free UMMs.

---


> [!TIP]
> 当前位于：**151-168**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-168**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
