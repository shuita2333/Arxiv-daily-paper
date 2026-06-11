# 🧠 大模型相关研究 | 2026年06月12日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-128](./part-03.md)

---

### 1. [PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference](https://arxiv.org/abs/2606.11196)

**<font color=#1a73e8>作者：</font>** Arther Tian, Alex Ding, Frank Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decentralized LLM inference networks need lightweight, reference-free quality evaluation for Proof of Quality (PoQ). We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references. We study three architectures across the quality-cost tradeoff: a TextCNN judge, a MiniLM cross-encoder, and a DeBERTa judge. Using two-stage training on UltraFeedback plus GPT-labeled in-domain data, the best model reaches 0.747 Pearson correlation with the ground-truth proxy on a held-out test set, outperforming reference-based evaluators from prior work. As a reference-free component in composite scoring, it achieves 0.645 Pearson correlation, matching the best single reference-based evaluator while removing the need for reference answers. We also show that online calibration identifies semantic quality as the dominant dimension and that cascade evaluation reduces cost by 72.7 percent with only modest quality loss. Results are much stronger on QA than summarization, pointing to proxy quality as the main remaining limitation.

---


### 2. [The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content](https://arxiv.org/abs/2606.11198)

**<font color=#1a73e8>作者：</font>** Yuqi Zhang, Di Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems inject external knowledge to improve LLM outputs, yet the format of injected content -- distinct from its semantic relevance -- can independently distort the model's attention distribution. We identify and formalise a phenomenon we term the structural attention tax: knowledge graph (KG) triples, due to their relational delimiters and repeated slot patterns, capture 2-3x more attention per token than semantically equivalent natural-language text ($\hat{o}$(KG) $\approx$ 0.70 vs. $\hat{o}$(neutral) $\approx$ 0.25), compressing demonstration attention by up to 42% -- regardless of whether the triples are relevant or noise. We develop a formal framework decomposing attention scores into semantic and structural components (Eq. 2), derive a compression bound (Proposition 1) connecting token-level format bias to demonstration attention loss, and show that the structural term governs how much attention is diverted while the semantic term governs whether this helps or hurts. This decoupling reveals two orthogonal axes for improving retrieval-augmented ICL: optimising retrieval quality (semantic axis) and reducing format-driven attention capture (structural axis). Empirically, across two model families (Mistral-7B, LLaMA-3-8B) and three QA benchmarks, we observe that source-task alignment dominates: task-matched BM25 retrieval achieves 58-62% on HotpotQA vs. ConceptNet's 25-27%, a >30 pp gap that dwarfs all gating strategies ($\leq$2 pp). We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention.

---


### 3. [NightFeats @ MMU-RAGent NeurIPS 2025: A Context-Optimized Multi-Agent RAG System for the Text-to-Text Track](https://arxiv.org/abs/2606.11199)

**<font color=#1a73e8>作者：</font>** Quentin Fever, Naziha Aslam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present NightFeats, a structured multi-agent retrieval-augmented generation (RAG) system submitted to the MMU-RAGent competition at NeurIPS 2025, where it was awarded Best Dynamic Evaluation in the text-to-text track. Rather than targeting benchmark maximization, this work proposes a principled pipeline that decomposes knowledge synthesis into three coordinated phases: retrieval, curation, and composition, each governed by explicit intermediate representations and handoff contracts. Inspired by Agentic Context Engineering (ACE), the system introduces temporal-semantic reranking, bounded contradiction reconciliation, and citation-preserving composition as core architectural primitives. Competition results show that NightFeats surpasses proprietary baselines including Claude-SonnetV2 and Nova-Pro on LLM-as-a-Judge and Human Likert evaluations, confirming that architectural transparency and verifiable evidence grounding are better aligned with human preferences than systems optimizing narrowly for automatic similarity metrics.

---


### 4. [Detecting AI-Generated Content on Social Media with Multi-modal Language Models](https://arxiv.org/abs/2606.11200)

**<font color=#1a73e8>作者：</font>** Chenyang Yang, Shen Yan, Yibo Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI has enabled the creation of photorealistic images and videos that are increasingly disseminated on social media, often used for spam, misinformation, manipulation, and fraud. Existing AI-generated content (AIGC) detection methods face challenges including poor generalization to new generation models, reliance on single modalities, and lack of interpretable explanations. We present our pipeline that mitigates these issues by continuously curating diverse multi-modal social media data and training a compact vision-language model for detection and explanation. Our model achieves state-of-the-art detection performance on public benchmarks and demonstrates robust detection and explanation capabilities on internal social media datasets across multiple platforms. We deployed our model for post recommendation on social media platforms and observed positive downstream impacts on user engagement, demonstrating that it is feasible to perform effective AIGC detection in dynamic, real-world social media environments.

---


### 5. [One Jailbreak, Many Tongues: Learning Language-Insensitive Intention Representations for Multilingual Jailbreak Detection](https://arxiv.org/abs/2606.11202)

**<font color=#1a73e8>作者：</font>** Shuyu Jiang, Kaiyu Xu, Xingshu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in applications for global multilingual users, yet safety training remains concentrated in dominant languages and has not progressed in parallel with multilingual capability, creating exploitable gaps for jailbreak attacks. Current jailbreak defenses are largely developed and evaluated in dominant languages, and their effectiveness is limited by the scarcity of aligned multilingual supervision and representations dispersion caused by language variation. To address this issue, we propose MLJailDe, a multilingual jailbreak detection framework designed to improve both multilingual robustness and cross-lingual generalization. MLJailDe first introduces a multilingual back-translation data augmentation algorithm to construct a semantically consistent and functionally effective dataset spanning 11 languages, consisting of 2,232 benign and 1,239 jailbreak samples. On this basis, MLJailDe employs relative-distance constraints to reduce cross-lingual representation dispersion and encourage jailbreak prompts with similar intent to form consistent clusters across languages, while an imbalance-aware classification objective is further used to alleviate class imbalance and learn more reliable multilingual decision boundaries. Experimental results show that MLJailDe outperforms state-of-the-art baselines across multiple languages, achieving an F1 score of 98.5\%, and obtains an average F1 score of 97.1\% on unseen languages, demonstrating strong effectiveness and cross-lingual generalization.

---


### 6. [Benchmarking Large Language Models for Safety Data Extraction](https://arxiv.org/abs/2606.11204)

**<font color=#1a73e8>作者：</font>** Jonas Grill, Thomas Bayer, Sören Berlinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate extraction of structured information from Safety Data Sheets (SDS) remains challenging in industrial safety due to heterogeneous document formats and the limitations of traditional rule-based methods. This study benchmarks state-of-the-art Large Language Models (LLMs) for automated SDS data extraction, comparing text-based and multimodal processing pipelines. We systematically evaluate four models: Gemini 1.5 Pro, GPT-4o, Claude 3.7 Sonnet, and Llama 3.1-70B, across three prompting strategies: zero-shot, few-shot, and chain-of-thought. The evaluation framework assessed accuracy, latency, and cost across more than 50,000 extracted data fields. Results show that text-based extraction consistently outperforms multimodal processing across all metrics. Gemini 1.5 Pro combined with a Chain-of-Thought prompt achieved the highest accuracy (84%), outperforming GPT-4o (81%) and Claude 3.7 Sonnet (79%). However, no model surpassed the 90% accuracy threshold commonly required for reliable real-world deployment. These findings indicate that general-purpose LLMs are not yet robust enough for unsupervised industrial use, though performance suggests strong potential with task-specific fine-tuning. Future research should focus on domain-adapted training, model calibration, and the integration of Human-in-the-Loop verification to ensure safety-critical reliability.

---


### 7. [Compatibility-Aware Dynamic Fine-Tuning for Large Language Models](https://arxiv.org/abs/2606.11206)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Junwei Sheng, Qianning Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) is the predominant paradigm for aligning large language models (LLMs), yet it suffers from optimization instability and limited generalization. Recent work attributes this issue to pathological gradient scaling and proposes Dynamic Fine-Tuning (DFT) to correct it at the token level. However, DFT assumes all demonstrations are equally suitable learning targets, an assumption violated by the strong heterogeneity of large-scale instruction data, where demonstration-policy mismatch induces high-variance updates at the sample level. We introduce Compatibility-Aware Dynamic Fine-Tuning (CADFT), a principled extension of DFT that controls sample-level optimization variance. CADFT derives a dynamic, policy-dependent compatibility signal from model likelihoods to modulate supervised updates, suppressing high-variance gradients from incompatible demonstrations. We further propose a delayed, low-frequency compatibility-guided rewriting strategy to transform persistently incompatible demonstrations into learnable targets. We show that CADFT can be interpreted as a variance-controlled estimator that generalizes token-level stabilization in DFT to the sample level. Extensive experiments demonstrate improved stability, generalization, and cold-start reinforcement learning initialization, while remaining fully supervised and independent of explicit reward modeling.

---


### 8. [ProcessThinker: Enhancing Multi-modal Large Language Models Reasoning via Rollout-based Process Reward](https://arxiv.org/abs/2606.11209)

**<font color=#1a73e8>作者：</font>** Jingpei Wu, Xiao Han, Weixiang Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual question answering increasingly requires multi-step reasoning. Recent post-training with reinforcement learning under verifiable rewards (RLVR) and Group Relative Policy Optimization (GRPO) can improve multimodal reasoning, but most approaches rely on sparse outcome-only rewards. As a result, they struggle to tell whether an incorrect answer comes from a small mistake late in the reasoning or from an unhelpful trajectory from the start. A common solution is to train a process reward model (PRM) for step-level supervision, but this typically requires large-scale high-quality chain-of-thought annotations and additional training cost. We propose ProcessThinker, a practical post-training pipeline that provides step-level process rewards without training an explicit PRM. ProcessThinker first rewrites reasoning traces into a step-tagged format for cold-start supervised fine-tuning, then applies GRPO with a standard format reward and our rollout-based process reward. Concretely, for each intermediate step, we sample multiple continuations from that step and use the empirical success rate (final-answer verification) as the step reward. This gives dense credit assignment and encourages reasoning steps that more reliably support a correct conclusion, helping reduce inconsistent or self-contradictory progress across steps -- a key issue in logical reasoning. Across four challenging video benchmarks (Video-MMMU, MMVU, VideoMathQA, and LongVideoBench), ProcessThinker consistently improves over the baseline model Qwen3-VL-8B-Instruct

---


### 9. [T2MM: An LLM Supported Architecture For Inquiry-Based Modeling](https://arxiv.org/abs/2606.11210)

**<font color=#1a73e8>作者：</font>** John Kos, Rudra Singh, Ashok Goel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model Construction is a foundational practice in science learning that relies on visualization and interactivity. Large Language Models, increasingly augmented with multimodal capabilities, have been integrated in education contexts to support learning. However, these tools lack visual interactivity that is required by some learning contexts. We introduce Text to Multimodal Model (T2MM), a robust, dynamic LLM supported architecture that assists in model construction within the open inquiry ecology-based modeling software Virtual Experimental Research Assistant (VERA). T2MM accounts for the current context of the learner's model and creates interactive models, rather than static images, enabling the model to remain responsive to manual adjustment. To measure technical feasibility, we evaluate T2MM through a custom procedurally generated dataset of natural language learner modeling requests and target models within the VERA system. T2MM outperforms a baseline model generation architecture implemented through LLM-supported full code generation, common in the literature, across all measured success metrics. Our contribution not only outlines LLM integration into a inquiry-based learning modeling tool, but also describes a possible architecture through which more interactive multimodal LLM tools can be created.

---


### 10. [Calibration Drift Under Reasoning: How Chain-of-Thought Budgets Induce Overconfidence in Large Language Models](https://arxiv.org/abs/2606.11211)

**<font color=#1a73e8>作者：</font>** Prakul Sunil Hiremath, Harshit R. Hiremath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ability of large language models (LLMs) to express calibrated uncertainty is important for safe deployment. Chain-of-thought (CoT) reasoning is widely used to improve accuracy and reliability, but its effect on calibration is not fully understood. We show that this picture is incomplete: in some settings, increasing the reasoning budget beyond a task-specific threshold can cause models to become systematically overconfident, assigning high confidence to incorrect answers. We call this phenomenon Calibration Drift Under Reasoning (CDUR) and study it both theoretically and empirically.
We define reasoning budget B and analyze conditions under which Expected Calibration Error ECE(B) follows a non-monotonic pattern: it first decreases as reasoning corrects errors, then increases as longer reasoning produces internally consistent but incorrect explanations. We propose a Hypothesis Lock-In model based on autoregressive generation to explain this behavior.
We evaluate Llama-3.1-8B and Llama-3.3-70B on 47 reasoning-trap questions across four reasoning budgets and three seeds (1,368 API calls; 574 valid responses). The 8B model shows non-monotonic calibration behavior, while results for the 70B model are limited to baseline evaluation and are inconclusive for budget-dependent effects.
We introduce CABStop, a calibration-aware stopping rule that halts reasoning when confidence diverges from an auxiliary accuracy estimate. These results suggest that increasing reasoning depth does not always improve reliability and should be monitored carefully.

---


### 11. [EverydayGPT: Confidence-Gated Routing for Efficient and Safe Hybrid GPT-RAG Conversational QA](https://arxiv.org/abs/2606.11212)

**<font color=#1a73e8>作者：</font>** Jaspreet Singh Nahal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard Retrieval-Augmented Generation (RAG) pipelines route every query through retrieval and generation unconditionally, incurring unnecessary computation and propagating low-quality context to the generator. We introduce EverydayGPT, a lightweight conversational QA system built around a Confidence-Gated Routing (CGR) mechanism that formalises the routing decision as a joint policy over retrieval distance and extraction adequacy. The backbone is a 205M-parameter GPT trained from scratch on 10B tokens of FineWeb-Edu. CGR avoids invoking the costly GPT pathway (~5.9s) for 85 percent of queries by resolving them via fast RAG extraction (~45 ms), yielding over 120x latency reduction on the majority of queries while maintaining answer quality. On a 500-question in-domain benchmark, the system achieves F1 = 0.226 +/- 0.004 compared to 0.171 for GPT-only and 0.210 for unconditional RAG. Gains over strong baselines are modest but consistent, while efficiency improvements are substantial (6.3x mean latency reduction). A structured grounding audit finds no unsupported claims in the sampled set, with explicit scope limitations. We position this work as a study of routing strategies under resource constraints rather than a claim of state-of-the-art performance.

---


### 12. [Afrispeech Semantics: Evaluating Audio Semantic Reasoning in Spoken Language Models Across Domains and Accents](https://arxiv.org/abs/2606.11219)

**<font color=#1a73e8>作者：</font>** Chibuzor Okocha, Christan Grant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio language models (ALMs) are increasingly used for speech-based understanding, yet their ability to perform semantic reasoning beyond transcription, Text-to-Audio Retrieval, Captioning, and Question-Answering accuracy remains insufficiently benchmarked. In particular, the effects of accent variation, domain shift, and semantic over-inference on audio reasoning are poorly understood. We evaluate audio language models across five semantic and paralinguistic reasoning tasks: entailment, consistency, plausibility, accent drift, and accent restraint. Collectively, these tasks assess a model's ability to reason over spoken audio as the primary evidence source, including whether a textual hypothesis can be inferred, contradicted, or left undetermined by the audio, whether statements align or conflict with spoken content, whether claims are plausible given the discourse, and whether model predictions remain stable or appropriately constrained across accent variation. These findings highlight critical limitations in current audio reasoning evaluations and hope to provide guidance for more robust and equitable ALM design and assessment

---


### 13. [LifeSentence: Language models can encode human life course trajectories from longitudinal panel data](https://arxiv.org/abs/2606.11220)

**<font color=#1a73e8>作者：</font>** Samuel Liu, Muchen Xi, William Yeoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forecasting human life outcomes is important to gain insights into how individuals attain long and healthy lives. Conventional statistical approaches yield limited accuracy, potentially due to discarding the sequential structure of the life course. Modern methods such as transformer architectures require large scale training data that most longitudinal panel studies lack. Here we introduce LifeSentence, a model for life-course reasoning that bridges large language models with longitudinal panel data. By representing each life event as a structured natural-language record and instruction-tuning a pretrained 24-billion-parameter language model across an 18-task evaluation taxonomy spanning prediction, robustness and reasoning, LifeSentence supplements panel data with distributional knowledge already encoded during pretraining. Trained on approximately 65,000 individuals from the German Socio-Economic Panel - roughly 45 times fewer than prior transformer-based approaches - LifeSentence outperforms classical and deep learning baselines across all task families, achieving a threefold improvement in joint event-and-timing prediction from best baselines and 91.2% Kendall's tau when reconstructing chronological order from timestamp-stripped event sets. Without explicit supervision, the model recovers documented patterns of social stratification, including the education premium, the gender wage gap and the motherhood penalty, from discrete event sequences alone. A natural-language interface further enables qualitatively new research queries, such as connecting an early-life history to a specified late-life endpoint, establishing LifeSentence as both a predictive tool and a probe for counterfactual exploration of human biographies.

---


### 14. [LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment](https://arxiv.org/abs/2606.11221)

**<font color=#1a73e8>作者：</font>** Huaihai Lyu, Chaofan Chen, Yuheng Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We take a Gromov-Wasserstein perspective on Vision-Language-Action (VLA) learning, where the goal is to make the relational geometry of action representations compatible with the semantic geometry of VL embeddings. However, this alignment is non-trivial due to the mathematical heterogeneity between the domains: the semantic space of vision-language is topologically linear and isotropic, whereas the physical manifold of robotic action is non-Euclidean and anisotropic. Their disjoint metric structures render direct regression ill-posed. To resolve this incompatibility, we introduce LAST (Lie-algebraic Action Space Tokenizer), which reconstructs the action space to establish local metric compatibility with the VL modality via a two-stage transformation: (1) Global Topological Linearization: linearizing the action manifold via Lie-algebraic mapping, converting trajectories into a fixed-length, physically additive representation. (2) Local Metric Discretization: hierarchically discretizing the representation into schemas and whitened residuals, yielding approximately isotropic local charts that are statistically aligned with the semantic metric. By resolving the structural mismatch at both global and local levels, LAST enables VLA models with superior convergence and generalizability.

---


### 15. [Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs](https://arxiv.org/abs/2606.11232)

**<font color=#1a73e8>作者：</font>** Weijia Zhang, Ruiqi Chen, Yunze Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing LLM moral benchmarks usually ask which isolated moral act, value, or foundation a model prefers. This is useful but incomplete. Realistic judgments often require a model to combine several moral signals within the same option. We introduce **Moral Trolley Arena**, a two-stage blind ELO benchmark for measuring how LLMs compose moral evidence. The single-scene arena first calibrates individual moral acts from a 229-scenario corpus across five Moral Foundations Theory foundations; the composite arena then combines calibrated acts into two-act moral items over a controlled intensity grid and measures the resulting composite preferences. Across ten frontier models, composite judgments are largely predicted by component act strength, but the relation is consistently compressed rather than simply additive. Models also show non-additive intensity anchoring, bounded foundation-specific residuals after component control, and highly convergent composite preference surfaces across providers. These results suggest that moral audits should measure composition rules for moral evidence, not only rankings over isolated acts.

---


### 16. [Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite](https://arxiv.org/abs/2606.11257)

**<font color=#1a73e8>作者：</font>** Zhiyuan Cheng, Longying Lai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) pipelines are compute-intensive, combining embedding, retrieval, reranking, and large language model (LLM) generation. Running them entirely on-device benefits privacy, latency, and offline use, but the energy cost of CPU inference is a major barrier. We present what is, to our knowledge, the first end-to-end RAG pipeline that runs all neural stages -- embedding, reranking, and LLM generation -- on the Qualcomm Hexagon NPU of the Snapdragon X Elite. Profiling on a Dell XPS 13 laptop, we compare NPU-accelerated RAG against CPU and OpenCL/Adreno GPU baselines on indexing and query workloads. On indexing, the NPU achieves 9.1x higher embedding throughput and 12.3x less system energy. On a 120-query Wikipedia-passage benchmark, it delivers 18.1x faster LLM prefilling, 4.0x lower end-to-end query latency, and 4.0x less system energy than the CPU baseline; the same workload on the integrated GPU is 1.7x slower than CPU and uses 6.5x more energy than the NPU. A GPT-4.1 LLM-as-judge evaluation finds NPU answer quality on par with CPU and GPU within evaluator noise (mean 9.32 vs. 8.95 vs. 9.03 on a 1-10 rubric), with 86.7% of queries scoring identically across all three backends. On the Snapdragon X Elite / Hexagon class of laptop SoC, the NPU thus enables practical, energy-efficient on-device RAG without quality regression -- a sustainable path toward green edge intelligence that we expect to generalize to comparable mobile NPUs (Apple Neural Engine, Intel NPU, MediaTek APU) as their software stacks mature.

---


### 17. [PermDoRA -- Understanding Adapter Interference in Language Models: Limits of Parameter-Space Geometry](https://arxiv.org/abs/2606.11262)

**<font color=#1a73e8>作者：</font>** Gowtham Sivaramakrishnan, Sarvesha Kumar Kombaiah Seetha, Kishan Gupta Balaji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Access control in large language models (LLMs) requires modular mechanisms to enable domain-specific behavior without retraining or cross-domain interference. A common hypothesis is that interference during adapter composition arises from overlap in linear parameter updates, suggesting that enforcing orthogonality or directional independence should improve multi-domain performance. We test this hypothesis using DoRA-RBAC, a hierarchical adapter composition framework based on weight-decomposed low-rank adaptation. We compare conventional Euclidean merging with a geometry-aware Riemannian-inspired merging strategy that approximates the Frechet mean via normalized directional averaging across multiple QA benchmarks (GPQA, PubMedQA, SimpleQA, WMDP) on LLaMA-3.1-8B and Mistral-7B. Our results show that while single-domain performance matches LoRA, geometry-aware merging provides no consistent advantage over standard averaging in multi-domain this http URL analysis further reveals that angular alignment and orthogonality of adapter updates are weak predictors of composition performance. These findings suggest that adapter interference is not governed primarily by parameter-space geometry, but is instead consistent with interactions in shared nonlinear representations.

---


### 18. [Seeing Before Colliding: Anticipatory Safe RL with Frozen Vision-Language Models](https://arxiv.org/abs/2606.11266)

**<font color=#1a73e8>作者：</font>** Samuel Tetteh, Cody Fleming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The cost signal that constrained-RL algorithms optimize against is almost always reactive: the simulator emits a non-zero cost only after a collision has begun, and the Lagrange multiplier of PPO-Lagrangian grows only after the episode budget has been exceeded. At race speeds, where collisions are instantaneous and irreversible, any safety mechanism that waits for cost to accumulate is structurally too late. We present VLM-Safe-RL, a framework that integrates a frozen vision-language model into the CMDP Lagrangian update as an anticipatory cost term. The framework comprises four contributions: (i) Decoupled Dual-Path CLIP, independent reward/cost paths that respect the CMDP's factorization; (ii) VLM-Lagrange, an augmented multiplier update that incorporates a per-step VLM cost as an anticipatory term; (iii) Confidence Gating, a Bayes-optimal weight derived from a logistic noise model on the CLIP margin; and (iv) VLMPPOLag, the composed algorithm. On Safety-Gymnasium FormulaOne L2, our principal evaluation ($n{=}5$ seeds, $10^{6}$ steps, budget $d_{\text{lim}}{=}25$) VLMPPOLag$+$Conf is the only configuration in our default budget comparison that simultaneously retains substantive return ($J_r{\approx}40$) and holds cost within budget on a majority of seeds; the five constraint-aware baselines (PPOLag, CPO, CPPOPID, CPO-CLG, PPOLag-RND) each fail at least one requirement. The mechanism generalizes to held-out MetaDrive Medium (catastrophe rate $41\%{\to}26\%$, 95\% bootstrap CI $[-26,-5]$\,pp) and shows directionally consistent transfer to Bullet Safety-Gym; we report honestly where it does not (MetaDrive Easy/Hard, Qwen2-VL backbone) and trace the Hard failure to a Lagrangian-regulation pathology rather than the VLM signal itself. To our knowledge, this is the first work to use frozen VLM signals as an anticipatory cost term inside the CMDP Lagrangian update.

---


### 19. [LakeFM: Toward a Foundation Model for Aquatic Ecosystems Using Irregular Multivariate Multi-depth Time Series Data](https://arxiv.org/abs/2606.11268)

**<font color=#1a73e8>作者：</font>** Abhilash Neog, Sepideh Fatemi, Medha Sawhney 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding and forecasting lake dynamics is critical for monitoring water quality and ecosystem health across lakes and reservoirs. While machine learning methods have been recently applied to ecological time-series data, existing works assume regular sampling in time and depth, and struggle to generalize across lakes with heterogeneous variables, depths, and observation patterns. To address these limitations, we introduce \textsc{LakeFM}, a foundation model for aquatic systems, pre-trained on large-scale ecological datasets comprising both simulated and observed lakes. Through extensive empirical evaluation, we show that \textsc{LakeFM} learns meaningful representations spanning broader lake-level characteristics, and achieves competitive or often superior-forecasting performance compared to existing time-series foundation and non-foundation models, while producing physically plausible predictions consistent with real-world lake dynamics.

---


### 20. [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/abs/2606.11270)

**<font color=#1a73e8>作者：</font>** Uwe Konig, Hamza Kazmi, Ruizhe Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning. While qualitative evidence supports the existence of this effect, its magnitude has not been systematically characterized. This study quantifies subliminal behavioral transfer ratios by steering two teacher models (Llama-2-7B-Chat and Qwen2.5-7B-Instruct) at varying steering strengths and distilling student models using only benign data. Evaluation on 100 JailbreakBench prompts with GPT-4.1, serving as the evaluator, indicates that transfer is robust but exhibits distinct scaling behaviors. Llama-2 demonstrates a sharp threshold ($\tau = {0.25,0.32} \ \text{beyond} \ \alpha = -0.15$), whereas Qwen2.5 displays continuous and higher levels of transfer ($\tau$ up to $0.61$).

---


### 21. [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/abs/2606.11290)

**<font color=#1a73e8>作者：</font>** Lingzhi Yuan, Chenghao Deng, Fangxu Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off. Task-level methods spend substantial offline compute yet deploy only a single workflow, leaving complementary candidates unused, while query-level methods synthesize a new workflow per query at substantial inference cost. Our motivating analysis shows these paradigms are more complementary than competing: workflows discovered during offline search often solve different subsets of queries, and many queries handled by expensive query-level generation can already be solved by cheaper precomputed workflows. This suggests a different objective: rather than searching for one universally best workflow or regenerating one per instance, we should build a compact bank of reusable, complementary workflows and select among them adaptively at inference time. Doing so requires solving three coupled problems: generating complementary rather than redundant candidates, compressing them into a small deployable portfolio, and assigning each query to the right workflow under a performance-cost trade-off. To this end, we present FlowBank, a three-stage framework for portfolio-based agentic workflow optimization. Diversifying proposes DiverseFlow to steer search toward under-covered queries and produce a high-coverage candidate pool. Curating proposes CuraFlow to compress this pool into a compact portfolio with minimal redundancy. Matching casts deployment as edge-value prediction on a query-workflow bipartite graph and routes each incoming query to the portfolio member with the best predicted utility. Across five benchmarks, FlowBank achieves the highest average score among the evaluated methods while remaining cost-competitive, improving over the strongest automated and handcrafted baselines by 4.26% and 14.92% relative, respectively.

---


### 22. [Schützen: Evaluating LLM Safety in Bulgarian and German Contexts](https://arxiv.org/abs/2606.11316)

**<font color=#1a73e8>作者：</font>** Kiril Georgiev, Yuxia Wang, Dimitar Iliyanov Dimitrov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed across professional domains, bringing hard-to-predict risks, including the generation of harmful or disrespectful content. Although substantial progress has been made in developing safety evaluation datasets, existing resources remain overwhelmingly English- and Chinese-centric. This limitation is particularly pronounced when evaluating languages that operate within shared sociocultural, legal, and ethical contexts. To address this gap, we introduce Schützen: a German--Bulgarian safety dataset designed to assess model answerability under risk, covering both a low-resource language (Bulgarian) and a high-resource language (German). Experiments with multilingual and language-specific LLMs reveal pronounced cross-language differences in safety behavior, highlighting the necessity of tailored, region-specific evaluation resources to support the responsible deployment of LLMs in Germany and Bulgaria. Datasets and code are available at this https URL. Warning: this paper contains examples that may be offensive, harmful, or biased.

---


### 23. [When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/abs/2606.11350)

**<font color=#1a73e8>作者：</font>** Nabaraj Subedi, Ahmed Abdelaty, Shivanand Venkanna Sheshappanavar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation degrades when scaled to large, heterogeneous document collections, where dense similarity loses discriminative power, and top-k retrieval increasingly returns semantically similar but contextually incorrect chunks. We refer to this failure mode as vector search dilution. Even when using hybrid dense+sparse retrieval, we observed this firsthand in a deployed Wyoming Department of Transportation corpus, where scaling from 54 to 1,128 documents (88,907 chunks) reduced accuracy from 75% to below 40%. To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks. Our results indicate that domain scoping using organizational metadata is the key fix, significantly improving P@10 from 0.77 to 0.86 ($p < 0.05$). Furthermore, our investigation of multi-agent orchestration revealed that a high degree of configuration dependence results --creating what we call the precision-faithfulness paradox. Based on these varied outcomes, our practical recommendation is simple: scope first, then perform a single synthesis call, reserving full multi-agent orchestration for genuinely multi-domain corpora paired with native-tool-call backbones. Code and Data will be made public upon acceptance.

---


### 24. [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/abs/2606.11375)

**<font color=#1a73e8>作者：</font>** Orion Reblitz-Richardson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy. The protocol works well on a snapshot but breaks across pre-training: probe accuracy saturates within the first few thousand steps, leaving most of training invisible to the instrument. We introduce fragility, a complementary per-layer metric defined as the activation-noise level at which probe accuracy collapses. Fragility is sensitive to both the margin of separability and the redundancy of representation, both of which keep evolving long after accuracy plateaus. Applied to open-checkpoint language models, fragility recovers structure that accuracy alone cannot see. Moralized representations emerge along a lexical $\to$ compositional gradient: lexical moral detection first, compositional moral encoding later. Because probe accuracy on its own tracks how lexically separable a dataset is, we establish the compositional encoding directly, by showing it transfers across construction types that share no contrast tokens. A layer-depth robustness gradient develops monotonically across training while accuracy stays flat. And matched fine-tuning corpora that produce identical probing accuracy leave distinct fragility fingerprints, showing that data curation reshapes probe robustness without changing probe accuracy. In every comparison we test, where probing accuracy returns a flat answer, fragility returns a structured one.

---


### 25. [Automated Mediator for Human Negotiation: Pre-Mediation via a Structured LLM Pipeline](https://arxiv.org/abs/2606.11379)

**<font color=#1a73e8>作者：</font>** Jamie Bergen, Sarit Kraus  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-mediation, the preparatory phase preceding direct human negotiation, plays a critical role in achieving mutually beneficial agreements, yet is often omitted due to cost, time, and limited access to trained mediators. We introduce an automated mediator for human negotiation, implemented as a structured pipeline of LLM modules, that supports pre-mediation in integrative negotiation settings. The pipeline decomposes preparation into specialized modules for dialogue, preference prediction, response-level critique, and structured summarization, separating inference, generation, and evaluation to address limitations of monolithic single-prompt approaches. We use the term "agent" for each module following common LLM-systems terminology, but the components are not autonomous and do not interact peer-to-peer; outputs are passed forward in a fixed sequence. We evaluate the system in two controlled human-subject experiments comparing AI-based pre-mediation with professional human mediators in a multi-issue negotiation scenario. On short-term self-reported measures, the automated mediator achieves preparation outcomes broadly comparable to human mediators, including trust in the mediator and confidence in reaching mutually beneficial agreements, while achieving substantially lower error on the preference-inference task under our scenario and prompts (36% lower RMSE). A second study shows that targeted prompt refinements reduce excessive affirmation patterns from 36.6% to 16.8%, matching human mediator baselines. Our findings suggest that structured LLM pipelines can provide scalable, low-effort pre-mediation support broadly comparable to human mediators on short-term self-reported preparation outcomes. The pipeline's single-party design mirrors how human mediators run pre-mediation today and enables parallel deployment across all parties to a dispute, supporting scalability.

---


### 26. [GLACIER: A Multimodal Student-Teacher Foundation Model for Molecular Property Prediction](https://arxiv.org/abs/2606.11382)

**<font color=#1a73e8>作者：</font>** Emily Nguyen, Yongchan Hong, Harsh Toshniwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models facilitate the discovery of molecules with tailored properties among billions of candidate compounds. However, the computational burden to develop and deploy state-of-the-art models continuously increases, limiting their scalability. Most large-scale models are unimodal in nature and overlook the potential to leverage complementary molecular data modalities. To address these shortcomings, this paper introduces the Graph-Language Alignment for Chemical Inference and Exploration using Representations (GLACIER) model, a student-teacher framework that integrates molecular graphs, SMILES strings, and physicochemical descriptors to learn rich molecular embeddings. Our framework consists of three stages: (1) we pretrain three student encoders on 100,000 drug-like molecules: a message-passing neural network for molecular graphs, a transformer-based encoder for SMILES strings, and a multilayer perceptron for physicochemical descriptors, (2) we fuse these student modalities using a novel Finsler geometry-aware module, and (3) distill complementary knowledge from large teacher models, including MiniMol and MolFormer, into a single lightweight model via contrastive learning. We demonstrate that GLACIER is a robust framework that delivers high predictive performance and computational efficiency in complex molecular property prediction tasks. Our code is publicly available at this https URL.

---


### 27. [DeceptionX: Explainable Deception Detection with Multimodal Large Language Models](https://arxiv.org/abs/2606.11385)

**<font color=#1a73e8>作者：</font>** Jiayu Zhang, Shuo Ye, Jiajian Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deception detection is a critical and highly challenging task within affective computing and behavioral analysis. Existing deep learning methods typically treat this task as a straightforward classification problem; however, this black-box approach lacks interpretability and fails to capture the complex logical deduction processes utilized by human experts when identifying lies. While Multimodal Large Language Models (MLLMs) have shown potential, applying them effectively requires a bridge between low-level audiovisual cues and high-level logical reasoning. In this paper, we propose DeceptionX, a novel MLLM framework that shifts the paradigm of deception detection from black-box classification to an interpretable Observe-Think-Summarize reasoning process. To address the scarcity of high-quality reasoning data, we first constructed DeceptChain, a high-quality dataset developed through a human-in-the-loop process. This dataset synthesizes fine-grained visual and auditory evidence (such as micro-expressions and vocal tremors) into structured chain-of-thought reasoning data. Furthermore, we propose a three-stage training pipeline and a Discrepancy-Aware Redundancy Elimination~(DARE) strategy for DeceptionX to further enhance the model's generalization capabilities. Extensive experiments demonstrate that DeceptionX not only outperforms existing MLLM baselines and state-of-the-art methods on standard real-world benchmarks but also provides transparent, expert-level reasoning paths, bridging the critical gap between accuracy and interpretability in multimodal deception detection.

---


### 28. [Overcoming State Inertia in Full-Duplex Spoken Language Models via Activation Steering](https://arxiv.org/abs/2606.11386)

**<font color=#1a73e8>作者：</font>** Cheng-Kuang Chang, Kai-Wei Chang, Alexander H. Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken language models (FD-SLMs) enable seamless speech interaction by allowing models to listen and speak simultaneously, yet the internal mechanism by which they coordinate listening and speaking remains underexplored. We analyze the predictive behavior encoded in FD-SLM hidden representations and find that they exhibit stream-specific predictive patterns: during listening, they preferentially predict the incoming user stream, whereas during speaking, they preferentially predict the model output stream. Building on this observation, we show that FD-SLMs dynamically modulate their internal predictive focus between two states: a generative state aligned with model output generation and a perceptive state aligned with incoming user input. However, this modulation can lag behind abrupt changes in conversational context. During user interruptions, the model remains transiently biased toward the generative state before transitioning into the perceptive state, causing it to miss the beginning of the incoming input. We term this delayed internal transition state inertia. To quantify its downstream impact, we introduce the Zero-Buffer Benchmark (ZBB), a diagnostic benchmark for evaluating immediate interruption comprehension when user speech begins abruptly. We evaluate this setting using response correctness and initial-word occurrence rate (IWOR). Finally, we mitigate state inertia through activation steering with a perception vector, a training-free intervention with little additional computational overhead. Across multiple state-of-the-art FD-SLMs, activation steering substantially improves interruption handling; for example, on PersonaPlex, it improves correctness from 28% to 45% and IWOR from 40% to 72% without any fine-tuning.

---


### 29. [Scenario-based Probing and Steering Cultural Values in Large Language Models--Extended Version](https://arxiv.org/abs/2606.11399)

**<font color=#1a73e8>作者：</font>** Trung Duc Anh Dang, Tung Kieu, Sarah Masud  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are deployed across cultural contexts but often reflect homogenized values inherited from training data. Evaluations of cultural alignment typically rely on direct prompting with survey-style questions, which frequently elicit neutral or safety-aligned responses and fail to capture underlying model preferences. We propose a framework for probing and steering latent cultural representations in LLMs along the two Inglehart--Welzel axes of the World Values Survey (WVS). By translating social value questions into scenario-based behavioral dilemmas, we extract token-level probabilities to measure implicit values and apply activation steering, optionally combined with country-conditioned prompting, to shift model behavior without retraining. Across three open-source LLMs and four target cultures, we find substantial variation in steerability and identify latent entanglement, where interventions along one cultural dimension induce shifts along another. This coupling mirrors correlations in human WVS data and persists across activation, prompt, and hybrid steering. It constrains axis-independent alignment, though general task performance is largely preserved.

---


### 30. [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/abs/2606.11409)

**<font color=#1a73e8>作者：</font>** Malikeh Ehghaghi, Boglárka Ecsedi, Marsha Chechik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly. In practice, the computational expense of different attack strategies can vary by orders of magnitude. Consequently, ASR at a fixed budget can obscure the true effort required to jailbreak a model, thereby making it hard to determine whether an attack's cost justifies its payoff to the attacker. We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort. We introduce risk-compute curves, which map compute budgets to attack risk, and derive two metrics that summarize the average pressure required for a given attack to succeed. Across ten models spanning three families and four different stages in language model training and alignment, evaluated with three attack strategies (gradient-based, iterative refinement, and template-based) on two jailbreak robustness benchmarks, we find: (1) alignment training has non-monotonic effects on compute-space robustness; (2) scaling model size reduces gradient-based attack effectiveness but has limited impact on cheaper template-based attacks; (3) gradient-based attacks optimized on a surrogate model can transfer to a separate target model, providing a way to reduce attacker costs; (4) compute cost varies by up to ${\approx}5{\times}$ across harm categories within a single model; and (5) safety-aligned RL increases aggregate cost while leaving some categories disproportionately accessible. We release our framework to enable compute-aware risk assessment and evaluation.

---


### 31. [Context-Aware Multimodal Claim Verification in Spoken Dialogues](https://arxiv.org/abs/2606.11420)

**<font color=#1a73e8>作者：</font>** Chaewan Chun, Delvin Ce Zhang, Dongwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every day, millions absorb claims from podcasts and streams that no fact-checker ever sees. Spoken misinformation is built through conversation, where credibility comes not from facts alone but from how claims are framed, reinforced, or left unchallenged across turns. Yet fact-checking has focused on isolated text, leaving dialogue audio under-studied. We introduce MAD2, a new Multi-turn Audio Dialogues benchmark for spoken claim verification, containing 1,000 two-speaker dialogues with 3,368 check-worthy claims and approximately 10 hours of audio, and propose calibrated multimodal fusion of a context-aware audio encoder and a dialogue-aware text model. Across settings, adding dialogue context improves verification, but the gains depend on scenario type. Using only preceding context often matches offline performance, supporting live-moderation settings, and audio contributes most when transcript-based models are destabilized by additional context. Overall, conversational structure matters more for verification than misinformation framing.

---


### 32. [Forecasting Future Behavior as a Learning Task](https://arxiv.org/abs/2606.11445)

**<font color=#1a73e8>作者：</font>** Mosh Levy, Yoav Goldberg, Asa Cooper Stickland  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs. For large reasoning models (LRMs), this conventional route is particularly difficult to follow: explanation methods for single token generations do not naturally generalize to long trajectories, and the trajectories themselves are often not faithful when read as natural language. We propose an alternative that bypasses the explanation step: treat behavior forecasting as a learnable task and train Behavior Forecasters that operates on a single reasoning trajectory to make the same forecasts one would typically seek from an explanation. The forecaster's training data is obtained by querying the LRM with no human annotation, and its inference is done in a single forward pass. We instantiate this approach on two tasks: how likely the LRM is to repeat its answer on re-runs, and how removing parts of the input changes its answer. We evaluate this approach on both tasks across three diverse reasoning datasets and find that trained Behavior Forecasters are more accurate than GPT-5.4 and Claude Opus-4.6 reading the same trajectories as naive readers, at a small fraction of their inference cost. We find that fine-tuning the backbone end-to-end and initializing it from the target LRM are each necessary for strong performance. These results show that the reasoning trajectory carries information about the LRM's future behavior that goes beyond what naive reading conveys.

---


### 33. [APEX: Automated Prompt Engineering eXpert with Dynamic Data Selection](https://arxiv.org/abs/2606.11459)

**<font color=#1a73e8>作者：</font>** Fei Wang, Si Si, Cho-Jui Hsieh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are highly sensitive to prompt formulation, necessitating automatic prompt optimization to unlock their full potential. While evolutionary algorithms have emerged as the dominant paradigm, they suffer from a critical bottleneck: data efficiency. Current methods treat the development dataset as a static benchmark, wasting significant compute budget on uninformative data. In this work, we introduce APEX (Automatic Prompt Engineering eXpert), a novel framework that optimizes the data usage alongside the prompt search. APEX dynamically stratifies the dataset into Easy, Hard, and Mixed tiers based on the optimization lineage. By prioritizing the Mixed tier, which identifies the data where the LLM has mixed performance, we identify two high-leverage subsets: the addressable frontier for generating informative mutations and the rank-sensitive frontier for distinguishing candidate quality. We evaluate APEX across three diverse benchmarks: IFBench, SimpleQA Verified, and FACTS Grounding. Under a fixed budget of 5,000 evaluation calls, due to its data efficiency, APEX outperforms the initial prompt by an average of 11.2% on Gemini 2.5 Flash and 6.8% on Gemma 3 27B, demonstrating that a data-centric approach is key to efficient and effective prompt optimization.

---


### 34. [The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes](https://arxiv.org/abs/2606.11470)

**<font color=#1a73e8>作者：</font>** Avinash Anand, Mahisha Ramesh, Avni Mittal 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved strong performance across natural language processing tasks, yet reliable reasoning remains an open challenge. Although modern LLMs show progress in structured inference, multi-step problem solving, and contextual understanding, their reasoning behavior is often inconsistent and sensitive to prompting strategies, task design, and model scale. This survey provides a systematic analysis of more than 300 recent papers from arXiv, Semantic Scholar, Google Scholar, Papers with Code, and the ACL Anthology to examine how reasoning capabilities emerge in LLMs and where they fail. We make three main contributions. First, we introduce a structured taxonomy of LLM reasoning research, covering Chain-of-Thought reasoning, multi-hop reasoning, mathematical reasoning, common sense reasoning, visual and temporal reasoning, code and algorithmic reasoning, retrieval-augmented reasoning, tool-augmented and agentic reasoning, and reinforcement learning-based reasoning. Second, we analyze methodological trends across these paradigms, including prompting methods, model architectures, training objectives, reward modeling, and evaluation benchmarks. Third, we synthesize recurring limitations and failure modes, such as reasoning hallucinations, brittle multi-step inference, weak causal abstraction, and poor cross-domain generalization. By organizing a rapidly expanding literature, this survey offers a unified view of the current capabilities and limitations of reasoning in LLMs. We also identify emerging research directions, including meta-reasoning, self-evolving reasoning frameworks, multimodal reasoning, and socially grounded reasoning. Overall, this work aims to serve as a reference for developing more robust, interpretable, and generalizable reasoning systems in future language models.

---


### 35. [Towards Fully Automated Exam Grading: Fairness-Aware Recognition of Handwritten Answers with Foundation Models](https://arxiv.org/abs/2606.11477)

**<font color=#1a73e8>作者：</font>** Hartwig Grabowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Correcting handwritten exams by hand is time-consuming and error-prone, particularly for large cohorts, while fully digital exams tend to force a didactic narrowing towards closed question formats. A practical middle ground keeps paper-based, problem-oriented tasks but records the assessment-relevant answers as single capital letters in a table that a machine can read. The open question is whether this reading can be made accurate and, above all, fair enough for unsupervised grading. Earlier automated approaches reached only about 88%--91% recognition -- too low -- and failed on the cases that matter most: answers placed outside the cell, crossed out, or written in cursive. We show that general-purpose vision-language foundation models (VLMs), which interpret the page rather than match pixel templates, close this gap. On a benchmark of 61 anonymised exams (3141 answer positions) the best model reaches 98.4% accuracy, well above the previous baseline. Crucially, we centre the evaluation on fairness: we distinguish false negatives (a correct answer marked wrong, which disadvantages the student) from false positives, and a lightweight prompt that supplies the reference solution as context lowers the false-negative rate to 0.58%. Under an exemplary grading scheme only three of the 61 exams would be graded worse, all caught by a student self-review step. Fully automated, fairness-aware exam grading at scale is therefore defensible; we release the anonymised benchmark to support reproducibility.

---


### 36. [OmniLoc: A Geometry-Aware Foundation Model for Anchor-Free UE Localization Across Diverse Indoor Environments](https://arxiv.org/abs/2606.11490)

**<font color=#1a73e8>作者：</font>** Lei Chu, Yuning Zhang, Omer Gokalp Serbetci 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indoor localization from wireless measurements remains challenging in large-scale deployments due to substantial variation in building geometry, the set of detectable access points (APs), and the heterogeneity of received signals. Existing learning-based methods often perform well only in limited settings and degrade under environmental shifts, making robust anchor-free localization across diverse indoor environments notoriously difficult. In this paper, we present OmniLoc, an environment-interactive foundation model for anchor-free user equipment localization across diverse indoor environments. To the best of our knowledge, OmniLoc is the first foundation-model-based approach built directly on wireless measurements for this task. OmniLoc is built on three key designs. First, a unified input tokenization module converts heterogeneous wireless measurements into a common representation that is more amenable to learning. Second, a geometry-aware Transformer performs AP-aware feature extraction by emphasizing dominant APs while aggregating complementary evidence from supporting APs. Third, a geometry-aware location estimation module conditions regression on geometric embeddings to produce geometrically consistent location predictions. We evaluate OmniLoc on both a large-scale in-house dataset and a public benchmark dataset. Results show that OmniLoc significantly outperforms existing methods, consistently improves existing backbones when its design components are integrated, and demonstrates strong generalization in cross-environment evaluations.

---


### 37. [When Roleplaying, Do Models Believe What They Say?](https://arxiv.org/abs/2606.11502)

**<font color=#1a73e8>作者：</font>** Benjamin Sturgeon, David Africa, Sid Black  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can state that "the Earth orbits the Sun" and, when role-playing Aristotle, assert the opposite. Recent work argues that persona adoption is fundamental to how language models operate, with models constantly selecting the most appropriate persona for a given context. Does such role-playing merely change the model's outputs, or does it also affect what the model internally represents as truthful? We study this question with linear truth probes, applying them to LLMs role-playing historical personas whose likely beliefs differ from modern consensus. For each persona, we compare false claims the persona would likely have endorsed (*era-believed*) with topic-matched false claims they would not have endorsed (*era-false*). Across prompting, in-context learning, and supervised fine-tuning, persona induction suppresses era-believed statements less than equally false alternatives, yet they remain classified as false overall. Role-play therefore shifts what these models say more than what they internally represent as true. We contrast this with models trained on harmful advice that exhibit Emergent Misalignment (EM). Across three model families (Qwen 2.5 14B, Qwen 3 8B, and Llama 3.3 70B), their false claims move substantially toward the true region of probe space, are defended under challenge roughly half the time versus about a sixth for role-play, and are used in downstream reasoning. Role-play and Emergent Misalignment thus are points on a spectrum of belief internalization, where role-play changes what a model says with little representational change, while Emergent Misalignment shifts the internal representation of false claims without fully marking them as true.

---


### 38. [SceneMiner: Identity-Preserving Multi-Task Fine-Tuning for Unified BEV Scene Mining](https://arxiv.org/abs/2606.11507)

**<font color=#1a73e8>作者：</font>** Abdalmalek Aburaddaha, Venkatraman Narayanan, Keval Thaker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mining hard, safety-critical scenes from driving logs is bottlenecked by the absence of difficulty labels, and no single proxy, collision risk, trajectory ambiguity, or semantic rarity suffices to find such scenes on its own. We present SceneMiner, a unified, camera-only bird's-eye-view pipeline that emits complementary mining signals from a frozen vision-language backbone in a single forward pass, with no LiDAR or radar: a retrieval embedding for text-prompted scenario search, a multi-label scene-tag distribution, and a continuous physics-based risk score (a motion forecast is a byproduct, not a contribution). Building such a multi-head model exposes our central finding, a failure mode we term cross-task interference: adding or upgrading one head shifts a shared activation stream and degrades weight-frozen sibling heads, so freezing parameters alone is insufficient. Our contribution, identity-preserving multi-task fine-tuning, removes this interference by zero-initializing every new sub-module and freezing every parameter that feeds the shared stream. The mining heads are thereby preserved bit-identically while training only ~102k parameters. The tagging head reaches mAP 0.4614 (micro-F1 0.5557) on 20 scene tags by pooling each scene into 32 visual tokens, and the embedding head supports text-prompted retrieval, validated qualitatively. Code is available at: this https URL

---


### 39. [SAGE: Answer-Conditioned Uncertainty Targets for Verbal Uncertainty Alignment](https://arxiv.org/abs/2606.11512)

**<font color=#1a73e8>作者：</font>** Kaiwen Shi, Zheyuan Zhang, Yanfang Ye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly express uncertainty through natural-language statements, yet these expressions often fail to reflect the model's sampled behavior. We study verbal uncertainty alignment as a distributional calibration problem: the appropriate uncertainty target for a prompt should be estimated from repeated model outputs rather than from an isolated response. However, group rollouts alone are insufficient, since the resulting target must provide a useful training signal. Existing targets only partially satisfy this requirement. We propose SAGE, Semantic-Answer Guided Entropy, a group-level uncertainty target that constructs an answer-conditioned uncertainty geometry over sampled responses. SAGE preserves categorical, numeric, and symbolic answer distinctions while maintaining a smooth and scale-preserving calibration signal. We further apply this target through Group-Uncertainty Preference Optimization, or GUPO, an uncertainty-channel training framework that supervises verbal uncertainty expressions rather than the full response. Experiments across factual, mathematical, and multiple-choice reasoning tasks show improved uncertainty ranking, lower calibration error, and reduced overconfidence.

---


### 40. [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/abs/2606.11520)

**<font color=#1a73e8>作者：</font>** Siyuan Luo, Nairong Zheng, Lin Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets. We propose ISE (Intent -> Simulate -> Execute), a three-stage synthesis paradigm that addresses these gaps jointly. Stage 1 constructs roughly 50000 structured intents via a 4D framework (Persona x Domain x Task x Complexity); after deduplication the pool contains 43956 unique intents and attains a Vendi Score of 61.57 over the entire pool on mpnet-base-v2 embeddings (cosine kernel, q=1). Stage 2 drives multi-turn user-agent interaction through a role-locked user simulator that grounds each user turn in actual execution outcomes, producing 23132 complete trajectories averaging 8.12 user turns and 68.24 total dialogue turns. Stage 3 runs every tool call inside a live, isolated OS workspace, generating authentic failure-recovery dynamics instead of simulated responses. Fine-tuning on ISETrace improves ClawEval pass@1 from 19.3 to 37.7 using Qwen3-8B on agent tool-use tasks with a standard protocol. This result outperforms zero-shot GPT-4o and the larger Qwen3-32B base model which is four times bigger. An ablation on Stage 2 proves multi-turn simulation brings a large portion of the performance gain. We release all source code and dataset at this https URL.

---


### 41. [VL-DINO: Leveraging CLIP Vision-Language Knowledge for Open-Vocabulary Object Detectio](https://arxiv.org/abs/2606.11546)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Qinran Lin, Linqi Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models like CLIP can provide rich semantic priors for open-vocabulary object detection. However, jointly integrating both textual and visual knowledge into detection architectures remains challenging. In this paper, we propose VL-DINO, an open-vocabulary detector that enhances DINO through more effective exploitation of CLIP's vision-language knowledge. Specifically, a Query-guided Positive Sample Construction (QPSC) module is first developed to construct additional high-quality positive samples, enabling the vanilla DINO framework to better accommodate mixed training across heterogeneous data sources while providing more vision-language alignment signals, thereby incorporating richer textual knowledge during training. A Visual Semantic Encoder (VSE) module is then introduced to distill CLIP visual knowledge into backbone-extracted features, producing fused features for subsequent encoder refinement. Based on the fused features, an Object-Region Semantic Alignment (ORSA) module extracts object-centric region features and aligns them with the corresponding textual embeddings, further incorporating textual cues. In the zero-shot setting, VL-DINO-T and VL-DINO-L achieve 36.3 and 38.1 AP on the LVIS benchmark, respectively, consistently outperforming prior advanced approaches. Extensive experiments demonstrate the effectiveness and competitive performance of the proposed design.

---


### 42. [Teaching Diffusion to Speculate Left-to-Right](https://arxiv.org/abs/2606.11552)

**<font color=#1a73e8>作者：</font>** Lexington Whalen, Yuki Ito, Ryo Sakamoto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve remarkable performance across a wide range of tasks, but their autoregressive decoding process incurs substantial inference costs due to inherently sequential token generation. Speculative decoding addresses this bottleneck by employing a lightweight draft model to propose multiple future tokens that are subsequently verified in parallel by a larger target model. Recent work has demonstrated that diffusion language models are well suited for this setting, as they can generate entire blocks of draft tokens in parallel and thereby alleviate the sequential constraints of autoregressive drafting. A subtlety of this regime is that block-diffusion drafters generate tokens bidirectionally within a block, whereas verification is performed by an autoregressive target model that evaluates tokens in a strictly left-to-right manner, leaving a gap between the symmetric training-time objective and the asymmetric verification-time reward. In this work, we offer an empirical analysis of three training-time interventions that narrow this gap: token positional weighting, a first-error focal loss that targets the position that breaks the accepted prefix within each block, and a chain loss term that substitutes a differentiable surrogate for the expected accepted length. The three interventions act along orthogonal axes (position, block-conditional first error, joint prefix) and compose additively; they are likewise orthogonal to test-time alignment mechanisms such as multi-draft self-selection, with which they can in principle be combined. Across four target models and six reasoning, code, and dialogue benchmarks, the three interventions raise accepted draft length by 21-76% per benchmark over a position-uniform baseline, without adding additional forward passes and without changing the inference pipeline or the rejection-sampling exactness contract.

---


### 43. [APEX: A Network-Native Time-Series Foundation Model for Forecasting and Anomaly Detection for Wireless Edge Operations](https://arxiv.org/abs/2606.11553)

**<font color=#1a73e8>作者：</font>** Swadhin Pradhan, Niloo Bahadori, Peiman Amini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generic time-series foundation models transfer poorly to wireless network telemetry whose signals are bursty, zero-inflated, and coupled across protocol layers. We present APEX, a network-native, decoder-only transformer for forecasting enterprise AP telemetry, and evaluate it on DHCP degradation as a representative network task. APEX is pre-trained on 10-channel multivariate telemetry from ~4,500 production wireless networks (~100K AP time series, 34 metrics per AP), and is available as APEX-Large (269M, cloud) and APEX-Edge (10.5M, edge). On a 192-step (4-day) DHCP degradation benchmark, APEX-Large reduces MAE by 18% over the strongest foundation-model baseline (Toto) and 38% over SARIMA, with anomaly-detection F1 = 0.93, while APEX-Edge enables sub-second, privacy-preserving inference on AP-class edge hardware. These results suggest network-native pre-training is a practical foundation for proactive wireless operations.

---


### 44. [HERO: Hindsight-Enhanced Reflection from Environment Observations for Agentic Self-Distillation](https://arxiv.org/abs/2606.11559)

**<font color=#1a73e8>作者：</font>** Haoran Liu, Yuwei Zhang, Xiyao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning typically improves multi-turn agent capabilities through the terminal outcome of the trajectories, which makes it difficult to determine credit assignments for each intermediate turns. Recent on-policy self-distillation methods offer a promising alternative by converting privileged feedback into dense token-level supervision through a self-teacher. Our study is motivated by the unexpected performance degradation observed when naively extending this paradigm to multi-turn settings, which we attribute to a lack of alignment between privileged feedback, such as successful trajectories or terminal outcomes, and the student's current decision context. We introduce HERO, a hindsight-enhanced self-distillation framework that uses next environment observations as locally aligned feedback. After each rollout, HERO reflects on the completed interaction to convert each observation into a compact turn-level diagnosis, that captures actionable feedback about the original action such as its necessity, validity or failure cause. On TauBench and WebShop, HERO improves task success and reduces unnecessary turns over environment-feedback-only self-distillation and GRPO. It is especially effective under limited training turn budgets, where successful rollouts are rare and GRPO provides weak reward-contrast signals.

---


### 45. [GraphInfer-Bench: Benchmarking LLM's Inference Capability on Graphs](https://arxiv.org/abs/2606.11562)

**<font color=#1a73e8>作者：</font>** Zhuoyi Peng, Jingzhou Jiang, Hanlin Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph analysis underlies many applications whose answers cannot be looked up in a single record or retrieved along a path: laundering rings, drug repurposing, user preference, and scientific theme are all inferred from a node together with its neighbourhood. We introduce GraphInfer-Bench, a benchmark for whether LLMs can perform this graph inference: producing an open-ended answer that no single node supports and no path retrieves. Existing graph-QA protocols cannot test this capability: algorithm simulation, node classification, single-node description, KG-QA, and GraphRAG all admit answers retrievable from one node or along a path. GraphInfer-Bench defines five tasks along Description (what a region is) and Comparison (how regions differ), each constructed so the ground truth lives in no single node. The release contains 42,000 samples across six real-world graphs, produced automatically and screened by a four-layer quality-control protocol. We evaluate four method families against the same tasks: graph-token alignment models, zero-shot frontier closed-source LLMs, Graph2Text supervised fine-tuning, and plain GNNs as a structural reference. No method family closes the gap. Graph-token alignment partially handles description tasks (relational, theme) but collapses on comparison tasks. Frontier LLMs lead on outlier detection and community partition among LLM-based methods but lag on masked-node prediction. Graph2Text SFT is the strongest LLM-based method on the description side yet falls behind frontier LLMs on comparison. Across every task, plain GNNs match or beat the strongest LLM-based row, with the largest margin on community detection. GraphInfer-Bench surfaces graph inference as an open capability gap rather than a property of any one architecture.

---


### 46. [4DP-QA: Scalable QA for 4D Perception in Vision Language Models](https://arxiv.org/abs/2606.11568)

**<font color=#1a73e8>作者：</font>** Seokju Cho, Abhishek Badki, Hang Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, Vision Language Models (VLMs) still struggle to grasp the dynamics of the world. We note that the ability to reason about a 4D scene, challenging in itself, is further complicated by two factors. First, VLMs observe motion indirectly via its projection onto 2D images. Second, existing datasets fail to disentangle object and camera motion. To address these challenges, we present a QA generation pipeline that focuses on motion-related scene understanding. We take particular care of the entanglement of camera and object motion by casting tracking in both the traditional way and in a novel, fixed reference system, dubbed True-Motion Tracking, which provides an intuitive description of motion. From this pipeline, we generate a large-scale training dataset of 400K samples, 4DP-QA (4D Perception QA), and a 2.2K-sample benchmark, 4DP-QA-Bench. Training existing models on our dataset yields performance improvements on an external benchmark, validating the effectiveness of our method.

---


### 47. [AVIS: Adaptive Test-Time Scaling for Vision-Language Models](https://arxiv.org/abs/2606.11576)

**<font color=#1a73e8>作者：</font>** Ahmadreza Jeddi, Minh Ngoc Le, Amirhossein Kazerouni 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language Models (VLMs) benefit from chain-of-thought prompting and test-time scaling, but these gains often come with prohibitive inference cost due to large visual contexts and long decoding chains. We view this cost through two coupled axes: Visual Context Scaling (VCS), which controls how much visual evidence is passed to the language model, and Visual Reasoning Scaling (VRS), which controls how much inference-time reasoning search is performed. Existing methods typically optimize one axis at a time, leaving the joint allocation of compute across these axes underexplored. We introduce Adaptive Visual Inference Scaling (AVIS), a lightweight policy that adapts both VCS and VRS per query. AVIS realizes VCS through Key Diversity Visual (KDV) pruning, a training-free $O(N)$ key-based rule for removing redundant visual tokens before prefilling, and realizes VRS through adaptive self-consistency, using a learned difficulty predictor to select the number of reasoning rollouts. AVIS is deployment-friendly and compatible with shared-prefill inference, where all rollouts reuse a single prefilling pass and KV cache. Across diverse image and video reasoning benchmarks, AVIS improves the accuracy--compute trade-off relative to VCS-only and VRS-only baselines, and remains effective on top of RL post-trained VLMs while keeping compute and latency low.

---


### 48. [Beyond the Golden Teacher: Enhancing Graph Learning through LLM-GNN Co-teaching](https://arxiv.org/abs/2606.11583)

**<font color=#1a73e8>作者：</font>** Zhuoyi Peng, Hanlin Gu, Lixin Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-attributed graphs (TAGs) underlie real-world applications such as citation networks, social media, and e-commerce. Few-shot graph learning on TAGs is hard: with only a handful of labels per class and the rest of the graph unannotated, neither GNNs nor LLMs can learn well on their own. GNNs read topology and fail on cold nodes; LLMs read text and fail on text-ambiguous nodes. Existing LLM-GNN methods all follow the same recipe: designate one model as the golden teacher and use its outputs (e.g., features or pseudo-labels) to supervise the other. We argue this golden-teacher assumption breaks under sparse supervision: neither model is golden, and treating either as such transfers its blind spots into the student. We therefore ask: can we avoid designating either model as the golden teacher, and still perform effective graph learning? We answer with LLM-GNN Co-Teaching, a bidirectional co-teaching framework in which neither model is fixed as teacher. The GNN and LLM exchange their most confident pseudo-labels under an architecture-specific small-loss criterion, and both update every round. Supervision is then mined from the trajectory: whenever a node moves from cross-model contradiction at round t to cross-model agreement at round t+1, the LLM's two answers on the same input form a preference pair (old contradicting self < new peer-endorsed self) for DPO training. We call this Round-based Pseudo-Label Preference Optimization (RPL-PO). On six benchmarks, LLM-GNN Co-Teaching consistently outperforms GNN-as-Judge and all prior methods, with absolute 3-shot gains of 7.86% on Cora and 7.73% on ogbn-arxiv; improvements carry over to 5-shot and to zero-shot cross-dataset transfer. Error-structure analysis further shows that abandoning the golden-teacher assumption substantially improves the LLM's graph learning capability on challenging samples.

---


### 49. [When is Your LLM Steerable?](https://arxiv.org/abs/2606.11599)

**<font color=#1a73e8>作者：</font>** Chenrui Fan, Yize Cheng, Ming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering offers a lightweight approach to control language models' behavior at inference time, but whether it succeeds or fails heavily depends on the prompt, concept, model, and steering configuration. Finding the regime and boundaries of successful steering typically requires expensive grid searches and post-hoc evaluation of full autoregressive rollouts. In this work, we investigate whether steerability can be predicted from the model's internal states at the beginning of the generation process, e.g., after generating the first few tokens, and how to leverage such a predictor to improve steering success rate. To this end, we first introduce ASTEER, a testbed including 1.4M steered generations, spanning 150 concepts with each steering success/failure labeled. Leveraging this testbed, we analyze the model's early decoding dynamics by extracting features that compare hidden states before and after steering across layers and initial decoding steps. These features help us understand how steering's effects propagate along layers and token positions, which provide key information for steerability prediction. We then train a Gradient Boosting Decision Trees (GBDT) classifier on these features to predict whether an intervention will under-steer, succeed, or over-steer without requiring full rollout. Our predictor achieves around 0.7 macro-F1 score on unseen concepts, demonstrating that early hidden states encode substantial, structured information about eventual steering efficacy. We further leverage this steerability predictor as guidance for steering strength searching, achieving near-optimal performance with a small fraction of decoding cost.

---


### 50. [Physics-Distilled Neural Network enabled by Large Language Models for Manufacturing Process-Property Predictive Modeling](https://arxiv.org/abs/2606.11605)

**<font color=#1a73e8>作者：</font>** Ge Song, Kiarash Naghavi Khanghah, Anandkumar Patel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting process-property relationships in manufacturing is often challenged by high experimental costs and the limited interpretability of complex 'black-box' models. This paper proposes a novel knowledge distillation framework designed to achieve high-accuracy predictions in data-scarce scenarios. The framework integrates analytical physics priors, which are systematically extracted from scientific literature via Large Language Models, into a privileged teacher model. We employ a Graph-Masked Attention layer to capture the complex physical dependencies among input variables showing strict setpoints or a combination of static and high-frequency temporal signatures. This privileged knowledge is distilled into a lightweight student predictor for inference. The feasibility and robustness of the framework are evaluated through a comprehensive experiment across five diverse manufacturing processes. To ensure statistical reliability, given the small dataset sizes, a repeated K-fold cross-validation technique is employed to quantify model stability and generalization. Results indicate that the proposed framework consistently achieves high predictive accuracy across all evaluated domains. Most importantly, the architecture demonstrates significant fault tolerance by maintaining robust predictive performance even in scenarios where LLM-derived analytical priors are suboptimal or incomplete. Furthermore, the student predictor achieves an inference frequency exceeding 6000 Hz, which facilitates real-time edge deployment on standard industrial hardware. This work provides a scalable solution for bridging the gap between theoretical physics and real-time industrial monitoring in data-limited environments.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-128](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
