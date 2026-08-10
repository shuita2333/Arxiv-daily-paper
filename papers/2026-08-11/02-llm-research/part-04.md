# 🧠 大模型相关研究 | 2026年08月11日

> 本类共 **170** 篇论文：已确认 **159** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-170**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-170**

---

### 151. [SABRE: Scalable and Automated Benchmarking of VLMs under Stress](https://arxiv.org/abs/2608.07435)

**<font color=#1a73e8>作者：</font>** Zixuan Lan, Luzhe Sun, Matthew R. Walter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are improving rapidly, but benchmark development lags behind, making weaknesses hard to identify. Building stress tests is costly: samples must satisfy controlled conditions, remain answerable, and challenge current models. We present SABRE, a scalable, automated pipeline that converts a Test Primer (a Markdown Task Design with Data Schema) into structured specifications, generated or edited images, and question-answer pairs. Automated filtering removes candidates solved by a Filtering VLM, while human review verifies candidate validity and supports annotation correction and localized image repair. We instantiate SABRE-Prior to test whether VLMs follow visual evidence instead of relying on world priors -- learned expectations about familiar objects and scenes. Its 600 images and 1,000 questions span Context (unexpected entities in familiar scenes), Texture (counterfactual materials), Attribute (noncanonical component counts), and Language Elicitation (answers suggested by language but unsupported by the image). Across six VLMs, macro-average accuracy ranges from 17.8% to 31.3% (22.6% mean). A real-image Attribute control is comparably difficult for the Filtering VLM. SABRE-Counting and SABRE-Spatial pilots show that the workflow supports other stress-test settings. These results establish SABRE as a reusable framework for constructing and refreshing VLM stress tests rather than a single fixed benchmark.

---


### 152. [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://arxiv.org/abs/2608.07437)

**<font color=#1a73e8>作者：</font>** Jiacheng Miao, Jin Mu, Guanhua Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferential errors that lead to incorrect conclusions despite correctly executed analyses. Existing benchmarks fail to capture this failure mode, as they rarely assess whether a reported p-value is statistically valid given the assumptions underlying the data. We address this gap by building P-Bench, a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning economics, biology, and medicine. Each task requires an agent to select a statistical method, compute a p-value, and draw a conclusion given only a scientific hypothesis and a dataset. We further introduce Fisher-R1, an open-weight LLM agent trained for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On P-Bench, Fisher-R1-14B substantially improves over its backbone and outperforms strong proprietary and open-source baselines, including GPT-5.4 and DeepSeekV4-Pro, achieving a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis testing and that reinforcement learning on tasks with verified statistical reward substantially improves reliability.

---


### 153. [PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents](https://arxiv.org/abs/2608.07438)

**<font color=#1a73e8>作者：</font>** Mohammad Amanlou, Parham Abed Azad, Farbod Davoodi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-like cognition does not select past experience by topical similarity alone: affective significance and unresolved conflict also shape what becomes accessible. We present PsychoAgent, a cognitive architecture for LLM agents that separates factual and affective memory and integrates both through a conflict-aware executive controller. Affective memories are first filtered by semantic relevance and then re-ranked by salience, preserving topical fit while allowing emotionally important traces to enter the prompt. Across three controlled conflict scenarios, the full architecture retrieved more conflict-critical memories than semantic-affective and single-memory RAG baselines (0.933 vs. 0.500 and 0.667), with a small semantic-similarity cost. Five blinded raters evaluated 27 outputs. After within-rater standardization, the full architecture had the highest overall mean (+0.22 SD), but corrected pairwise differences were not significant. A three-day illustrative trace further shows persistent affect, offline memory recombination, and selective memory reweighting. The findings support affect-sensitive retrieval as an inspectable mechanism for modeling human-like conflict effects in LLM agents.

---


### 154. [An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis](https://arxiv.org/abs/2608.07439)

**<font color=#1a73e8>作者：</font>** Brian Llinas, Nikos Chrisochoides  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantum natural language processing (QNLP) provides a grammar-aware framework for text modeling, and Distributional Compositional Categorical (DisCoCat) is one of its theoretically grounded formulations. Prior work on financial sentiment analysis has identified practical limitations of DisCoCat, including parser sensitivity, high simulation cost, and difficulty handling longer sentences. We study an LLM-assisted preprocessing workflow that uses controlled rewriting to compress, simplify, or decompose moderate-complexity financial sentiment sentences into parser-compatible, circuit-efficient variants while preserving sentiment-bearing meaning. We compare prompting strategies, language models, and filtering configurations with the low-complexity-only DisCoCat baseline of Stein et al. At the circuit level, the strongest compression variants reduce average qubit and gate counts by more than 70 percent relative to the raw moderate-complexity subset. Across repeated training runs, GPT-4.1-mini with Prompt B achieves the highest observed mean accuracy, $0.550 \pm 0.035$, compared with $0.521 \pm 0.050$ for the baseline. Larger training splits do not necessarily improve downstream performance; across evaluated configurations, training-split size has a moderately negative association with accuracy (Pearson $r=-0.446$). These results provide exploratory evidence that LLM-assisted rewriting can make some moderate-complexity inputs usable within the evaluated DisCoCat configuration, while highlighting prompt design, filtering, and circuit-aware preprocessing as considerations for more scalable QNLP-based financial sentiment analysis.

---


### 155. [Blast Radius](https://arxiv.org/abs/2608.07440)

**<font color=#1a73e8>作者：</font>** MY Pitsane, Hope Mogale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding faces growing problems of affordability and wasted tokens. We introduce Blast Radius, a predictive memory management layer that estimates an incoming prompt's reach through coupled context and code channels. NECROPHORESIS enables reversible eviction by archiving dead context verbatim, while Recurring Dead Matter (RDM) identifies and buries repeatedly occurring transcripts. We formulate reversible context eviction over a Polish context space, providing a measurable foundation for retention, recurrence, and eviction while connecting context entropy to resurrection probability. Across seven OpenAI models, Blast Radius reduced token consumption by 17-26%, achieved the lowest overflow rate among tested policies, and remained byte exact reversible. Of 450 buried bodies, 378 were recurring dead matter and zero were recalled. Blast Radius operates beneath HCRC, determining which records to bury and how far an incoming prompt may reach into the codebase. This work contributes to the broader goal of Algosophy: making large language models and agentic coding more reusable and sustainable.

---


### 156. [SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent](https://arxiv.org/abs/2608.07449)

**<font color=#1a73e8>作者：</font>** Mingxuan Zheng, Yujin Zhou, Chuxue Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skills. These skills are lightweight, reusable textual artifacts that are loaded into the agent's context without weight updates. Recent methods refine skills through iterative task execution, failure diagnosis, and trajectory-guided text-space updates. However, existing frameworks lack explicit diagnosis--outcome feedback and treat deletion as a generic edit operation rather than a dedicated mechanism for consolidating accumulated knowledge. We introduce SkillProx, a proximal-gradient-inspired forward--backward framework that couples closed-loop diagnostic evolution with utility-aware proximal refinement. Motivated by a composite objective balancing task loss and skill complexity, the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds measured outcomes into subsequent diagnoses. The backward stage decomposes the resulting skill into auditable knowledge units, estimates their contributions using a frozen leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show that SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline. Component ablations demonstrate the complementary effects of closed-loop diagnosis and proximal refinement.

---


### 157. [Strategy-first synthesis planning for complex natural products](https://arxiv.org/abs/2608.07454)

**<font color=#1a73e8>作者：</font>** Daniel Armstrong, Xuan-Vu Nguyen, Octavian Susanu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The total synthesis of a complex molecule is among the most demanding intellectual and experimental feats in chemistry: a chemist must plan many steps ahead for how to assemble simple building blocks into an intricate target, devise backup strategies, and anticipate procedural challenges. It is also a profoundly creative activity. For half a century, efforts to automate the retrosynthetic design of natural products and other complex molecules have drawn on catalogued reactions, and the resulting tools now report near-complete success on benchmarks built from that same source. But these tools were shaped to fit benchmarked chemistry, and they falter on many natural products, the frontier of the field, whose densely functionalized, polycyclic architectures demand precisely the inventive chemistry the record contains least. Whether a machine could reasonably design such syntheses like an expert chemist does has remained unclear. Here, we show that SynthEx, an agentic framework built on large language models, plans routes to complex natural products that lie beyond the reach of conventional design algorithms. SynthEx proposes competing strategies, assembles a sequence of routine and key steps into a cohesive route, and critiques and improves its own design; the chemistry it favours is more convergent than existing tools produce, and spans a region of reaction space that catalogue-based tools cannot match. Most notably, in blinded assessments, expert chemists judged its key steps comparable to those of published human syntheses and engaged with them as genuine synthesis plans, a response algorithmic route prediction has not previously accomplished. We release routes to more than a thousand natural products as SynthAtlas, an open, interactive database, and anticipate it will become a shared resource for a collection of complex target molecules that lack existing literature routes.

---


### 158. [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458)

**<font color=#1a73e8>作者：</font>** Gyuwan Kim, Cheoneum Park, Tao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent optimization studies on Retrieval-Augmented Generation (RAG) have exploited chunk-level KV cache reuse to avoid processing long retrieved contexts for higher efficiency, while significant information redundancy and noise still remain in the coarse-grained chunks. This paper optimizes the Pareto frontier under low prefill latency constraints while maximizing accuracy by proposing CoinRAG (Contextualized Information Nugget KV Cache Reuse for Long-Context RAG). The name metaphorically reflects our core mechanism: much like assembling small tokens (or "coins") to accumulate a larger value, CoinRAG compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently in a more semantically relevant but compact manner. Specifically, instead of full-chunk encoding, CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and seamlessly assembles their sliced KV representations with a chunk-level context. Extensive evaluations on LongBench multi-hop question answering tasks demonstrate that CoinRAG significantly reduces operational costs and outperforms the other baselines with a new Pareto frontier and an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

---


### 159. [CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity](https://arxiv.org/abs/2608.07460)

**<font color=#1a73e8>作者：</font>** Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 160. [Towards Multi-Label Graph Foundation Models: from Single-Vector Representation Learning to Multi-Semantic Basis Learning](https://arxiv.org/abs/2608.06394)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dongxiao He, Jiayu Zhang, Jitao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-label node classification is an important yet challenging task in graph learning, where nodes exhibit multiple semantics simultaneously. Existing methods for multi-label node classification can effectively model multiple labels, while only considering in-domain scenarios where the model needs to be trained and tested within the same graph domain, resulting in limited cross-domain generalization. Recently, Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable graph representations across diverse graph domains and downstream tasks. However, existing GFMs are built upon single-label assumption, where all nodes are arbitrarily regarded as containing only one class of semantic and embedded into a single representation. For multi-label nodes, such a representation essentially approximates multiple semantics with a single point in the representation space, inevitably leading to semantic entanglement and making simultaneous discrimination of multiple labels difficult. To address these limitations, we propose a Multi-Semantic Basis Graph Foundation Model (MSB-GFM), a framework for cross-domain multi-label node classification. Specifically, we introduce a multi-semantic basis representation learning paradigm that models each multi-label node as an adaptive composition of semantic bases, thereby enabling flexible representational capacity for modeling multiple semantics. Furthermore, we develop a semantic-structure dual-channel architecture with domain adversarial training for effective cross-domain knowledge transfer. Extensive experiments demonstrate the effectiveness of our model.

---


### 161. [InsertFuse: A Unified Framework for Multi-Category Reference-Guided Image Insertion](https://arxiv.org/abs/2608.06490)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guangzhao Li, Qingyan Wei, Huayu Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present InsertFuse, a unified framework for multi-category reference-guided image insertion. Its key idea is to decouple category-specific expertise learning from cross-category capability consolidation. InsertFuse first trains specialized experts for different insertion categories and then introduces Insertion On-Policy Distillation (IOPD) to consolidate their capabilities into a single student. By querying the matched expert at states visited by the student, IOPD preserves category-specific insertion behavior while mitigating the cross-category interference caused by direct joint training. To improve spatial control, we propose Token-Aligned Geometry Conditioning (TAGC), which maps mask-derived geometric cues to the visual token grid, and Region-Balanced Flow Matching, which separately normalizes prediction errors inside and outside the insertion region to prevent background-dominated and scale-dependent supervision. We further introduce Reference CFG to isolate and strengthen the guidance induced by the visual reference under fixed scene and geometry conditions, with IOPD transferring this enhanced supervision into the unified student. Extensive experiments on the public AnyInsertion benchmark and our multi-category test set demonstrate state-of-the-art performance on most metrics, showing strong reference fidelity and generation quality across diverse insertion categories.

---


### 162. [Bootstrap-Conditioned Action Selection with Tabular Foundation Models](https://arxiv.org/abs/2608.06559)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Devansh Gupta, Shiv Tavker, Dmitry Efimov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits offer a natural framework for sample-efficient personalization, but practical deployment remains difficult under sparse, biased interaction data, unreliable uncertainty estimates, and severe cold starts. We study whether pre-trained tabular foundation models with in-context learning can be turned into randomized policies for online decision making. We propose BC-ICL (Bootstrap-conditioned action selection using ICL), which at each round draws a bootstrap resample of the interaction history, conditions a frozen pre-trained ICL model on that resample, scores all actions, and selects the action with the highest sampled score. We further introduce an arm-context conditioning architecture that promotes shared statistical strength across actions and helps avoid common bootstrap failure modes of isolated-arm bandits. Empirically, this policy delivers strong early-round regret and regret performance on standard contextual bandit suites, outperforming established baselines under a strict online protocol.

---


### 163. [Do 3D Medical Foundation Models See Through MRI Artifacts? A Controlled Study of Representation Robustness](https://arxiv.org/abs/2608.06613)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Julia Anna Mielcarz, Daniel Klaaby, Mostafa Mehdipour Ghazi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised 3D medical foundation models are increasingly used as general-purpose feature extractors, yet their sensitivity to MRI artifacts remains poorly understood. We present a controlled evaluation of representation robustness across five pretrained 3D encoders spanning different architectures, objectives, pretraining domains, and dataset scales. Using BraTS-Africa cases with four MRI sequences, we generate seven frequency- and image-domain artifacts at five predefined corruption settings. Robustness is assessed using linear centered kernel alignment (CKA), RankMe, and UMAP, complemented by an independent segmentation-consistency analysis. We find that robustness is strongly model- and artifact-dependent. 3DINO exhibits the most consistently stable representations, while BrainIAC is highly sensitive to several corruptions; NeuroVFM, BrainFM, and Neuro-SimCLR show intermediate but distinct artifact-specific profiles. Across many conditions, CKA decreases substantially while RankMe remains comparatively stable, indicating that artifacts often distort representation geometry without causing dimensional collapse. Segmentation consistency also degrades under corruption, particularly for ghosting and Rician noise, but aligns only partially with representation-level robustness. These findings show that larger-scale or domain-specific pretraining alone does not guarantee artifact invariance and motivate explicit robustness evaluation before deploying 3D foundation models in heterogeneous MRI settings.

---


### 164. [CellWorld: From Gene-Level Reconstruction to Latent Cell Prediction in Spatial Transcriptomics Foundation Models](https://arxiv.org/abs/2608.06659)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haiping Liu, Qian Zhao, Lijing Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper shows that latent-space predictive pretraining can provide a scalable route to foundation models for spatial transcriptomics. Existing spatial transcriptomics foundation models primarily reconstruct masked gene identities or expression values, potentially encouraging the reproduction of assay-specific technical variation and limiting representation transferability. To avoid directly reconstructing such variation, we shift the prediction target from observed gene measurements to latent cell representations and introduce CellWorld, which predicts the latent representations of masked cells from visible spatial context and a limited partial-expression hint. We pretrain four CellWorld variants, spanning 5.74M to 94.56M trainable parameters, on a corpus of 46 million human cells. Our controlled scaling experiments show that performance improves with model capacity, particularly on spatial tasks, while spatial transfer depends more on sufficient optimization and broad biological source diversity than on cell count alone. Across four held-out datasets, even CellWorld-Small, with 5.74M trainable parameters, outperforms every baseline on all 11 linear-probe benchmarks and all seven fine-tuned spatial benchmarks. Most notably, a frozen CellWorld-Large pretrained on only 5\% of the corpus with broad biological source coverage outperforms every fully fine-tuned baseline across all seven spatial benchmarks. Code is available at this https URL.

---


### 165. [Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction](https://arxiv.org/abs/2608.06993)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gregor Molan, Grafika Jati, Francesco Barchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained time-series models achieve strong results through large-scale pretraining and task-agnostic representation learning, but they rely on abundant, diverse data that industrial and scientific domains often lack. We therefore propose the FSD-RM (Family of Small-Data Representation Models) paradigm as a practical alternative for limited, domain-specific telemetry. Rather than relying on large-scale pretraining, we focus on capacity-controlled representation learning using established encoder architectures (CNN1D, LSTM, GRU, Transformer), selected for their suitability in small-data settings and interpretability.
These encoders are trained unsupervised on multivariate telemetry data and integrated into a two-stage pipeline for downstream lifetime prediction. To systematically examine architectural trade-offs under data constraints, we employ \textbf{dimension-aware neural architecture search (NAS)} to jointly optimize model capacity and input dimensionality.
Experiments on cryocooler telemetry show that the proposed approach achieves competitive predictive performance while reducing training cost and model complexity. The contribution lies in combining established representation learning techniques within a coherent, NAS-driven framework tailored to small-data regimes, with explicitly defined parameter settings and design choices. The results indicate that effective representation learning can be achieved without large-scale pretraining when appropriate inductive bias and capacity control are applied.

---


### 166. [ZIPBrain: Can EEG Foundation Models Be Faster, Locally Deployable, but Accurate?](https://arxiv.org/abs/2608.07033)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lingwei Li, Yirong Kan, Peng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work investigates whether Electroencephalograph (EEG) foundation models (EFMs) can be made faster and locally deployable without sacrificing accuracy. EEG foundation models are a major trend, offering strong general-purpose representations. However, their computational burden grows quadratically with input length, hindering deployment on resource-constrained scenario, particularly for real-time clinical monitoring. EEG's low SNR further suggests many of these tokens are redundant and compressible with little accuracy cost. We propose ZIPBrain, a novel redundancy-aware EEG token pooling module that leverages this low-SNR characteristic to reduce token count. Given a token sequence, ZIPBrain partitions tokens into redundant and unique groups, then merges each redundant token with its most similar counterpart in the unique group. Furthermore, ZIPBrain serves as a training-free, plug-and-play module that seamlessly integrates into standard Transformer encoders with negligible computational overhead. Extensive experiments across multiple EEG foundation models show ZIPBrain's strong versatility, achieving 1.3%-10.5% average improvement over baselines, while reducing wall-clock inference time by 32.7% (up to 41.8% with CUDA Graph) compared to the original EEG foundation models.

---


### 167. [Unsupervised Adaptation of PDE Foundation Models](https://arxiv.org/abs/2608.07053)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziye Song, Zhao Wei, Xin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained partial differential equation (PDE) foundation models can generalize across different equations, but adapting them to unseen PDE systems typically requires dense solution data, which is often expensive or unavailable. To address this limitation, we propose an unsupervised PDE-based finetuning framework that eliminates the need for ground-truth solutions. We first pretrain a neighborhood attention Transformer on diverse time-dependent PDEs spanning varying spatial scales, yielding transferable representations across heterogeneous equations. In the adaptation stage, we construct a physics-based objective using the PDE residual and boundary conditions, and finetune the model on unseen equations via low-rank adaptation (LoRA). To address the uneven learning across physical quantities in standard LoRA, we introduce NSLoRA, a Newton-Schulz orthogonalized variant that rebalances adaptation. Our method achieves performance comparable to supervised LoRA finetuning without requiring any ground-truth solutions, while consistently outperforming competitive neural operator baselines and recent PDE foundation models across heterogeneous PDE benchmarks spanning multiple spatial dimensions.

---


### 168. [Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis](https://arxiv.org/abs/2608.07228)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Idil Gözel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse.
We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why.
The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

---


### 169. [A foundation-model approach to pediatric headache classification from rs-fMRI](https://arxiv.org/abs/2608.07287)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guilherme S. Imai Aldeia, Clara Moon, Julie Shulman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Headache is the most common neurological disorder in children and substantially affects quality of life. We investigated whether resting-state functional MRI (rs-fMRI) can support pediatric headache classification using machine learning. We encoded rs-fMRI data using NeuroSTORM, a recent foundation model, and fine-tuned it to distinguish healthy controls from children with headache and subsequently classify headache subtypes. We compared NeuroSTORM with a standard neuroscience approach using functional-connectivity (FC) matrices derived from brain activity as predictors. Using 189 rs-fMRI scans from 110 individuals collected across two visits (prevalence of any headache: 74%), NeuroSTORM achieved an area under the receiver operating characteristic curve (AUROC) of 0.82 (95% CI, 0.82-0.82) and an area under the precision-recall curve (AUPRC) of 0.93 (95% CI, 0.93-0.94) for discriminating headache from non-headache. In contrast, models trained on FC matrices showed lower performance (AUROC, 0.67 [95% CI, 0.67-0.67]; AUPRC, 0.85 [95% CI, 0.85-0.85]). In multiclass classification of healthy controls, chronic migraine, and non-chronic headaches (e.g., post-viral headache, new daily persistent headache, post-traumatic headache), NeuroSTORM achieved a macro-AUROC of 0.69 (95% CI, 0.68-0.69). Results suggest that the approach can distinguish chronic migraine but has difficulty differentiating other headache subtypes from chronic migraine. Overall, under limited-data conditions, NeuroSTORM appears to capture latent rs-fMRI representations that transfer to headache-related tasks without relying on FC features. These findings provide proof of concept for fMRI-based prediction of pediatric headache and highlight potential future utility for subtype identification and individualized treatment strategies.

---


### 170. [Foundation Models Adaptation for Multi-View Multi-modal Cardiac MRI Segmentation and Direct Ejection Fraction Estimation](https://arxiv.org/abs/2608.07291)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sina Amirrajab, Cian M Scannell, Volker Vehof 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown strong transferability in cardiac MRI (CMR), but their effectiveness for heterogeneous multi-view and multi-sequence CMR analysis remains unclear. In this work, we explore the effectiveness of fine-tuning and combining different CMR foundation models for the Universal Multi-Sequence, Multi-Center and Multi-View CMR Segmentation (CMR-Multi) Challenge. CineMA was fine-tuned for cine and late gadolinium enhancement (LGE) segmentation across short-axis and long-axis views. For direct left-ventricular ejection fraction (LVEF) estimation, we used two recent frozen CMR foundation models to extract embedding vectors that were then combined using attention-based multiple-instance learning for LVEF regression. In the challenge validation set, cine segmentation achieved Dice scores of 0.862, 0.883, and 0.902 for short-axis, two-chamber and four-chamber cine MRI, respectively. LGE segmentation achieved Dice scores between 0.621 and 0.846 across views. The direct LVEF regression model achieved an MAE of 4.96 percentage points and a Pearson correlation of 0.91. These results indicate that foundation models can be effectively adapted and combined for multi-view CMR analysis, while accurate LGE scar segmentation remains a challenging task.

---


> [!TIP]
> 当前位于：**151-170**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-170**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
