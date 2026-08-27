# 🧠 大模型相关研究 | 2026年08月28日

> 本类共 **209** 篇论文：已确认 **195** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-209**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-209**

---

### 201. [AutoVerifier: Residual-Guided Non-Parametric Optimization for Reference-Based Answer Verification](https://arxiv.org/abs/2608.25637)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zebei Zhao, Zhihao Shi, Minqi Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-based verifiers are important for evaluating reasoning models and providing accurate outcome rewards in reinforcement learning with verifiable rewards. To improve verification accuracy, prior work has explored rule-based, model-based, and tool-augmented verifiers for checking answer equivalence across diverse answer forms. However, the equivalence of answer forms such as $1+3.14$ and $1+\pi$ may depend on the question and scoring criterion. We frame such implicit assumptions as verifier inductive biases. To address this challenge, we propose AutoVerifier, a residual-guided non-parametric optimization method that learns these biases from recurring verifier errors. Specifically, AutoVerifier records these biases in rule cards and promotes them to code modules or prompt guidance only after replay validation detects no direct regressions, keeping accepted updates auditable, editable, and reusable. Experiments on four verifier benchmarks demonstrate that AutoVerifier outperforms state-of-the-art verifiers by a large margin.

---


### 202. [TailSFT: Filtered Fine-Tuning Improves Post-Training Performance](https://arxiv.org/abs/2608.25756)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sadhika Malladi, Samy Jelassi, Dylan Foster 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training drives reasoning and agentic capabilities in modern AI systems, yet a growing body of work shows that it is most effective when used to fine-tune an already capable base model. We question whether existing pipelines yield models that are most suitable for reinforcement learning. Building on prior work highlighting the role of coverage and pass@K as predictors of post-RL performance, we design a simple modification to supervised fine-tuning, TailSFT, which filters out already fit sequences during training, thereby focusing learning on under-modeled regions, or the tail, of the data distribution. We justify and validate the design choices in TailSFT, particularly the specific filtering criteria, through a combination of controlled experiments and theoretical analysis. On OLMo-3 7B, TailSFT often improves pass@16 performance on math and coding evaluations, with gains up to 17% absolute, while incurring minimal computational overhead. These higher-coverage checkpoints consistently translate to up to 4% absolute pass@1 gains in subsequent GRPO runs, demonstrating that TailSFT checkpoints serve as better initializations for RL. We further introduce a lightweight diagnostic for identifying settings where TailSFT is most likely to help. More broadly, our results motivate a principled, stage-aware approach to model development, in which intermediate checkpoints are judged by how effectively they support subsequent training.

---


### 203. [MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum](https://arxiv.org/abs/2608.25768)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Furkan Yilmaz, Habibe Aleyna Tasdemir, Muhammed Faruk Gozay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turkish encoder models have adopted modern architectures while leaving the pretraining objective fixed at masked language modelling. This paper introduces MoganBert-TR, a 149M-parameter Turkish encoder foundation model trained from scratch on a language-specifically filtered corpus, together with an embedding model derived from it (MoganBert-Embed).
MoganBert-TR is trained over 237.3B tokens with a two-stage CLM-to-MLM curriculum: causal language modelling first, masked language modelling for the remainder, with the transition made inside the stable phase of a WSD schedule. In a controlled ablation under an equal step budget, this design outperforms pure MLM by 2.7-3.7x on Turkish MS MARCO retrieval; the measured mechanism is embedding geometry, where a single direction absorbs 28.1% of the variance under pure MLM against 11.9% under the curriculum. Long-context extension and learning-rate decay are then split into two branches after a shared prefix: running the final portion of decay at 1024 context improves the TrGLUE average by 0.49 +/- 0.26 points across five paired seeds (p = 0.013) and beats a model-soup alternative by 0.75 points at ~4.3% additional cost.
MoganBert-TR attains 78.41 on TrGLUE, the best among the Turkish ModernBERT models compared, and 77.73 on TabiBench, where it leads two of the eight categories with the largest margin on code retrieval (+3.62 points over TabiBERT). MoganBert-Embed, produced through teacher distillation and multi-signal contrastive fine-tuning, ranks first among student models on the MTEB(Turkish) overall average with 68.30 and reaches 99.5% of its 7.57B-parameter teacher's score with a 51x smaller backbone. The accompanying 50,048-token tokenizer outperforms all compared Turkish tokenizers on compression and fertility across two independent test sets. Weights, tokenizer, embedding model and evaluation code: this https URL

---


### 204. [EXAONE Tabular 1.0 : Technical Report](https://arxiv.org/abs/2608.25774)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Moonjung Eo, Min-Kook Suh, Hye-Seung Cho 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EXAONE Tabular is a compact tabular foundation model family for classification and regression via in-context learning, producing predictions without dataset-specific gradient updates. Pretrained exclusively on a synthetic structural-causal-model (SCM) prior, its central contribution is an architecture-centered redesign of tabular in-context learning. Rather than compressing features into a fixed row embedding before a separate row-level learner, EXAONE Tabular interleaves feature-axis attention within each item with support-conditioned item-axis attention within each feature at every Transformer layer, mediated by item-summary and feature-summary tokens. Across four public benchmarks, EXAONE Tabular combines strong predictive performance with high efficiency. On TabArena, its 20.81M-parameter classification model ranks first overall, surpassing tuned ensembles and 4-hour AutoML pipelines, while regression reaches the performance regime of the 1.64B-parameter TabFM at roughly 1/11 the inference cost. On BCCO and TALENT, EXAONE Tabular ranks second in classification and first in regression. On ScoringBench, it achieves the best mean rank for both point-estimation and predictive-distribution quality, leading the $R^2$, RMSE, and CRPS evaluations. Together, these results establish EXAONE Tabular as a state-of-the-art compact tabular foundation model family, combining strong predictive performance across classification, point regression, and probabilistic regression with an efficient model design.

---


### 205. [Precipitation Downscaling Using Foundation Model-Conditioned Diffusion](https://arxiv.org/abs/2608.25858)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Victor Nascimento Ribeiro, Jorge Guevara, Jorge Sebastian Moraga 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution precipitation fields are essential for hydrological impact assessment, yet global climate model outputs are too coarse and biased for direct use. AI-based statistical downscaling with diffusion models offers a promising approach, but the mechanism by which large-scale atmospheric predictors condition generation remains largely unexplored. We investigate three conditioning strategies for a denoising diffusion probabilistic model applied to daily precipitation downscaling: channel concatenation of upsampled coarse predictors, cross-attention conditioning with a learned convolutional encoder, and cross-attention conditioning with the frozen encoder of the pretrained Prithvi WxC weather foundation model. All strategies are evaluated against an unconditioned baseline under identical conditions using probabilistic, distributional, spectral, and extreme-event metrics for the Colorado River Basin. Concatenation conditioning achieves the lowest point-wise CRPS and MSE, but tends to produce over-smoothed fields that suppress high-intensity events. In contrast, cross-attention conditioning provides substantially better distributional realism and modest improvements in spectral fidelity. Improvements are greatest for extremes: the Prithvi-WxC conditioned model retains over half of >100mm/day events, although estimates are uncertain due to limited samples. When trained on the full dataset, the learned convolutional model performs similarly to the foundation model-conditioned approach while requiring lower computational resources. However, the Prithvi-WxC-conditioned model achieves comparable performance with only five years of training data. These results indicate that cross-attention conditioning offers advantages over simple concatenation for probabilistic precipitation downscaling, and that pre-trained foundation model representations may offer benefits in data-limited settings.

---


### 206. [A General-Purpose Molecular Foundation Model Transfers Across Diverse Olfactory Tasks](https://arxiv.org/abs/2608.25893)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yikun Han, Yi Wang, Neil Mankodi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models have transformed molecular property prediction, yet it remains unclear whether a molecular foundation model, fine-tuned on a single canonical olfactory prediction task, can learn representations that transfer across diverse machine olfaction problems. We investigate this question by fine-tuning Uni-Mol2 on the GS-LF benchmark for multi-label odor descriptor prediction and evaluating the resulting model, without additional deep-learning training, on four complementary downstream settings: cross-dataset odor descriptor prediction, odorous-versus-odorless classification, enantiomer evaluation, and odor mixture discriminability. The fine-tuned model matches or exceeds the performance of the state-of-the-art olfaction-specific baseline on the primary GS-LF benchmark and consistently transfers across these downstream evaluations. The enantiomer analysis further shows that three-dimensional molecular representations distinguish mirror-image molecules in a way that two-dimensional graph models fundamentally cannot, although accurately predicting the perceptual consequences of stereochemistry remains an open challenge. Together, these results support a train-once, transfer-across-tasks paradigm for machine olfaction and suggest that chemically pretrained molecular representations provide a strong foundation for transferable olfactory prediction.

---


### 207. [Query-Side Attacks on GNN-Based KGQA: Tracing Failures from Entity Linking to Answer Generation](https://arxiv.org/abs/2608.25922)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pankaj Kumar, Subhankar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GNN-based Knowledge Graph Question Answering (KGQA) pipelines process queries through four discrete stages: entity linking, subgraph retrieval, GNN reasoning, and answer generation. Standard robustness evaluations conflate stage-level failures into a single end-to-end metric, obscuring both the source of brittleness and the appropriate mitigation target. We ask which stage fails, and why, when the pipeline is subjected to adversarial perturbations on the input question. We introduce a stage-isolation protocol with two answer-preserving adversarial perturbations verified against the knowledge graph: Compositional Restructuring (CR) and Relation Synonym Swap (RS) target distinct stages while leaving entity seeds intact. Evaluated across ComplexWebQuestions and WebQSP, the results run counter to prevailing assumptions: the GNN reasoning stage retains near-baseline accuracy when the subgraph is intact, while subgraph construction accounts for over 99\% of the end-to-end collapse under CR, occurring even when the gold answer is present in 74\% of retrieved subgraphs. This exposes a fundamental distinction between answer presence and answer reachability that end-to-end metrics cannot detect, and places the mitigation target firmly at the subgraph construction stage rather than the reasoning model. Perturbed datasets and evaluation infrastructure are released at this https URL .

---


### 208. [UltraPIPS: Improving model perception in B-mode ultrasound with foundation models](https://arxiv.org/abs/2608.26033)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tal Grutman, Tali Ilovitsh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In medical imaging, it is common to use learned perceptual image patch similarity (LPIPS) to compare images semantically in feature space. Although backbones pretrained on natural images are widely used for LPIPS computation, B-mode ultrasound images possess distinct speckle patterns and acoustic-specific image statistics that are fundamentally different from natural images and even from other images in radiology. Consequently, we propose that domain-specific models are needed to measure perceptual similarity in ultrasound data, a finding which is not necessarily the case for other imaging modalities. We compare LPIPS metrics across downstream tasks like classification, segmentation and reconstruction using natural image, medical generalist and ultrasound backbone models and show that selection of LPIPS backbone is a non-trivial design choice. In particular, the ultrasound backbone models were more correlated with downstream performance of supervised models than classical and natural image models, and optimization of the LPIPS loss with an ultrasound backbone achieved a strong balance between reconstruction quality and realism. Our code is available at this https URL and introduces the UltraPIPS library, a set of LPIPS metrics based on the open-source foundation models analyzed in this paper.

---


### 209. [Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings](https://arxiv.org/abs/2608.26088)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Evelyn Ma, Rama Kumar Pasumarthi, Kishwar Shafin 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predictive planetary models remains bottlenecked by a fragmented data ecosystem, requiring manual data retrieval, multimodal data curation and fusion along with iterative model selection. We present the Planetary Prediction Engine (PPE), an autonomous AI system that executes this end-to-end workflow directly from natural-language queries. PPE synthesizes multimodal datasets on the fly, retrieving spatiotemporally relevant covariates across open-web and Earth observation platforms (Data Commons, Google Earth Engine) and fusing them with geospatial foundation model embeddings (PDFM, AlphaEarth). Simultaneously, it searches over task-tailored model architecture families with automated overfitting guards. Across diverse tasks, geographies, and scientific domains, PPE consistently outperforms state-of-the-art or manually tuned expert baselines. For US spatial regression, PPE improves mean $R^2$ across 21 CDC health indicators (76.8% vs. 60.0%), FEMA national risk indices (64.9% vs. 60.0%), and the Social Vulnerability Index (66.2% vs. 58.6%). For spatial downscaling in data-scarce settings, PPE integrates localized proxies to double baseline accuracy in Nigerian food security indicators ($R^2$ of 66.1% vs. 31.5%). For epidemiological nowcasting of the 2026 DRC Bundibugyo Ebola outbreak, PPE achieves a Recall@10 of 83.3% (identifying 15 of 18 newly invaded health zones across five weekly forecasts), a +10.3 percentage-point improvement over the public state-of-the-art modeling (~73%). By combining autonomous multimodal planetary data discovery with targeted model optimization, PPE lowers the technical barrier to planetary-scale analytics, enabling rapid, customized, expert-level deployment.

---


> [!TIP]
> 当前位于：**201-209**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-209**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
