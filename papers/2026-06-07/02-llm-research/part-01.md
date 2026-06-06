# 🧠 大模型相关研究 | 2026年06月07日

> 本类共 **185** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-185](./part-04.md)

---

### 1. [The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage for Large Language Models](https://arxiv.org/abs/2606.05169)

**<font color=#1a73e8>作者：</font>** Jason Z Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a stereological theory of LLM benchmark coverage. For any suite with effective dimensionality d_eff, the visible Hausdorff distance between two convex capability profiles consistent with the same scores is bounded by epsilon + C R m^(-1/(d_eff-1)), with matching Lipschitz lower bound. Empirically, three independent leaderboards (Open LLM v2, an extended 12-benchmark suite, LiveBench) all have d_eff in [2.86, 4.80] on their competitive frontier; the structural blind spot exceeds the observed runner-up score gap by two orders of magnitude and dominates statistical noise by 52-127x. Under a chi-squared projection model, the isotropic prior is the optimistic case; across six hidden-capability priors and four ambient dimensions the simulated half-split swap rate of the top two models stays in [0.38, 0.49], and a 500-trial random visible/held-out split shows that 92% of trials swap the top-1 ranking with on average 2.83 of 5 top-5 models changing. A submodular greedy algorithm with the Nemhauser (1 - 1/e) guarantee finds a stable core of 4 benchmarks; 7 of 12 suffice for 90% coverage, and the trained subset transfers across temporal quarters with 93-97% retention. A counterfactual validation across 12 internal benchmarks and 27 Chatbot Arena categories confirms that the eigenstructure predicts which evaluations are irreplaceable (rho = -0.69, p = 0.013 for removal disruption) and which external evaluations bring new information (rho = +0.38). As a second, independent theoretical contribution, we resolve Gardner's Problem 1.5 (1995) for C^2 support functions, establishing the minimax rate Theta(R/(kappa m^(2/(D-1)))) in general dimension via optimal recovery theory on S^(D-1).

---


### 2. [ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models](https://arxiv.org/abs/2606.05170)

**<font color=#1a73e8>作者：</font>** Jason Z Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> At matched accuracy, open-weight LLMs differ substantially in the shape of their error severity distribution -- a difference invisible to the scalar error rate. Hallucination benchmarks report a single error count and treat all errors as equivalent, yet a wrong date and a fabricated court ruling differ by orders of magnitude. We introduce Errorquake-10k, a 10,000-query benchmark scoring each response on a continuous 0-4 severity scale across 8 domains and 5 difficulty tiers, and we fit per-model severity distributions for 21 open-weight models. For each model we estimate a severity distribution index (b, the Gutenberg-Richter upper-tail slope) with 95% bootstrap confidence intervals. Headline: across the 210 model pairs, 85 have disjoint 95% b confidence intervals at matched accuracy (|Delta epsilon| < 0.05) on human-consensus scoring, e.g. deepseek-v3.2 vs. ministral-14b at epsilon = 0.586 and Delta b = 0.47. A 519-item three-rater human validation study confirms measurement reliability (ICC(2,k=3) = 0.85), validates the LLM-judge ranking (rho = 0.89), and confirms the dense-model scaling correlation on human data (rho_s = -0.86). We prove a Non-Reducibility Theorem showing that severity profile and error rate are informationally non-redundant (I(b; model | epsilon) = 1.56 bits; 64.5% of cross-model b variance is unexplained by epsilon). A severity mechanism taxonomy (kappa = 0.83) reveals that error type shifts categorically with severity: low-severity errors are retrievals (71%); high-severity errors are fabrications (39%) -- and this composition differs by model size (p < 0.0001). Severity distribution should be reported alongside accuracy; it carries discriminative information that the error rate cannot.

---


### 3. [Improving Heart-Focused Medical Question Answering in LLMs via Variance-Aware Rubric Rewards with GRPO](https://arxiv.org/abs/2606.05174)

**<font color=#1a73e8>作者：</font>** Arash Ahmadi, Parisa Masnadi, Sarah Sharif 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong promise in healthcare applications. Yet deploying general-purpose models in real-world settings remains difficult due to data privacy constraints, inference costs, and limited suitability for edge or on-device use. These challenges motivate the development of smaller, more efficient models that require robust post-training strategies to ensure reliable medical reasoning. In this work, we investigate Group Relative Policy Optimization (GRPO) for post-training LLMs on heart-focused medical question answering with rubric-based supervision derived from RaR-Medicine. We propose a Variance-Aware Reward Framework that extends the Explicit Aggregation and Implicit Aggregation strategies of Rubrics as Rewards by replacing weighted binary criterion aggregation and single overall Likert-style scoring with continuous analytical reward functions derived from criterion-level rubric outcomes. This formulation provides richer optimization signals for feedback that is sparse, multi-criteria, and difficult to verify automatically, and enables more stable on-policy reinforcement learning. On a held-out heart-related subset of HealthBench, our best GRPO variant improves accuracy from 0.362 to 0.502 and F1 from 0.532 to 0.668 relative to the Qwen3-14B base model, while remaining competitive with GPT-OSS-120B (0.508 accuracy, 0.674 F1). Our findings show that carefully designed rubric-based rewards provide a practical strategy for improving heart-focused medical question answering in LLMs, with potential to extend to other rubric-based tasks.

---


### 4. [PEFT of SLM for Telecommunications Customer Support: A Comparative Study of LoRA Configurations with Energy Consumption Analysis](https://arxiv.org/abs/2606.05176)

**<font color=#1a73e8>作者：</font>** Lucas Tamic, Ilan Jaffeux-Cheniout, Xavier Marjou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) show strong performance in natural language understanding and generation, their evaluation and adaptation to domain-specific constraints in telecommunications customer support remain limited. In addition, data sovereignty, regulatory constraints, and the handling of sensitive customer and network information complicate the use of externally hosted foundation models in this domain.
We present a systematic study of parameter-efficient fine-tuning (PEFT) using Low-Rank Adaptation (LoRA) applied to Qwen2.5-3B to build a domain-specific conversational assistant. We introduce a combinatorial synthetic data generation approach based on a glossary of 52 industry-specific terms, producing approximately 30,000 training examples across 1,560 distinct problem scenarios via a generative pipeline powered by Gemini 2.0 Flash.
We evaluate 16 LoRA configurations by varying hyperparameters and target modules. Our evaluation extends beyond standard metrics by incorporating energy consumption analysis and qualitative assessment using an LLM-as-a-judge framework with GPT-5.2 and Claude 4.5 Sonnet.
Results show a clear divergence between quantitative and qualitative performance: models achieving the lowest validation loss do not necessarily obtain the best human-aligned rankings. The best validation loss (0.5024) ranks only 6th-7th in qualitative evaluation, while the worst loss (0.6807) ranks first according to both judges.
This work contributes (1) a combinatorial method for synthetic dataset construction, (2) insights into the impact of target module selection for LoRA injection, (3) evidence that validation loss alone is insufficient for selecting fine-tuning configurations in conversational AI, and (4) an energy-performance trade-off analysis for sustainable LLM deployment.

---


### 5. [MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models](https://arxiv.org/abs/2606.05177)

**<font color=#1a73e8>作者：</font>** Manh Luong, Tamas Abraham, Junae Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing multimodal safety benchmarks focus solely on visual inputs and cannot assess Omni Large Language Models (LLMs) that process vision, audio, and text. We introduce MCBench, a benchmark with 1196 scenarios spanning four safety categories that require integrating multiple modalities for accurate safety assessment. Each unsafe scenario is paired with a minimally different safe counterpart to assess model sensitivity. Our evaluations of state-of-the-art models reveal significant challenges. Omni LLMs struggle with subtle or non-physical risks but perform better when salient visual or acoustic cues are present. Analysis of reasoning traces shows that, although models can extract modality-specific information, they often fail to integrate these cues effectively for safety judgments. Our findings reveal that current Omni LLMs lack robust cross-modal reasoning in safety-critical settings, underscoring the need for improved architectures and training strategies for multimodal safety.

---


### 6. [From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment](https://arxiv.org/abs/2606.05180)

**<font color=#1a73e8>作者：</font>** Ivo Bueno, Babette Bühler, Philipp Stark 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated scoring models are increasingly used to assign rubric-based quality ratings to complex language performances, including classroom transcripts, yet they typically provide little insight into why a particular score is produced. We propose a general framework for sentence-level interpretability of rubric-based scoring that combines model-agnostic Shapley-value attributions with rationales generated by large language models (LLMs). Instantiated on the Quality of Feedback dimension of the CLASS framework using the NCTE corpus, the framework enables systematic comparison of fine-tuned pretrained language models (PLMs) and prompted LLMs on both scoring performance and explanation faithfulness. Across 6k annotated transcript segments, fine-tuned PLMs outperform LLMs in prediction accuracy but exhibit label compression toward mid-scale scores. Deletion-based tests show that SHAP identifies sentences that reliably drive model predictions, producing typically larger and more coherent prediction shifts than LLM-generated rationales. Cross-model analyses further reveal that SHAP attributions transfer robustly across architectures, whereas LLM rationales exert limited and inconsistent influence. Overall, the findings demonstrate that SHAP provides more faithful and transferable explanations for rubric-based scoring, and that the proposed framework offers a principled basis for evaluating both scoring models and their explanations in high-stakes educational settings and other rubric-based language assessment tasks.

---


### 7. [LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations](https://arxiv.org/abs/2606.05182)

**<font color=#1a73e8>作者：</font>** Rahul Subramani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models discard critical details when conversation history is compacted to fit within finite context windows. We present LANTERN (Layered Archival aNd Temporal Episodic Retrieval Network), a lightweight memory layer that proactively archives every conversation turn and restores relevant details after compaction via hybrid retrieval -- requiring zero LLM calls and adding fewer than 25ms of latency per turn. On 94 real multi-turn conversations (1,894 ground-truth facts, human-validated at kappa=0.81), LANTERN-Rerank recovers 78.3% of verifiable facts lost to compaction, significantly outperforming a faithful reimplementation of MemGPT's LLM-driven extraction and multi-query search pipeline (72.4%; Wilcoxon p<0.0001, 95% CI [+3.1, +8.6] pp, d=0.43) at a fraction of the inference cost. Even without the reranker, base LANTERN matches or exceeds this LLM-driven baseline (p=0.005) using zero LLM calls. When four production LLMs answer fact-bearing questions using LANTERN-restored context, accuracy improves by 8.4 percentage points on average (Wilcoxon p<0.05 for each model individually), demonstrating that the recovered context is useful across diverse model architectures. We release the full evaluation framework -- paired significance tests, failure analysis, fact-type stratification, and compaction robustness analysis -- to support reproducibility and future work.

---


### 8. [The Granularity Gap: A Multi-Dimensional Longitudinal Audit of Sycophancy in Gemini Models](https://arxiv.org/abs/2606.05183)

**<font color=#1a73e8>作者：</font>** Patrick Keough  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as high-stakes advisors, yet standard alignment benchmarks treat sycophancy as a binary failure mode. We introduce the Granularity Gap: coarse binary metrics mask substantial social-compliance behaviors where models capitulate to user framing, validate questionable premises, or soften factual corrections without producing overtly false outputs. We evaluate six Gemini variants across generations 2.0, 2.5, and 3.0 on 73 adversarial prompts under three guardrail conditions (Control, Simple, Protocol), yielding 8,830 graded responses. Using a 0-4 Likert scale validated against a human annotator triad (Fleiss kappa = 0.71; Cohen kappa = 0.78 vs AI consensus; 95.9 percent binary accuracy, 100 percent specificity), we quantify sycophancy as continuous rather than binary. Three findings emerge. First, 27.2 percent of responses contain substantial sycophantic content (Likert >= 2.0) and 22.7 percent reach moderate or severe levels (>= 3.0), while binary win-rate framing reports only modest failure rates; coarse metrics explain just 29 percent of graded variance. Second, generational progress is non-monotonic: Gen 2.5 regresses sharply (mean Control 2.64) relative to Gen 2.0 (1.90) and Gen 3.0 (2.01), and Gen 2.5 shows inverse scaling (Pro 1.94 worse than Flash 1.71) while Gen 3.0 restores standard scaling. Third, we document an Alignment Tax: Spearman rho = -0.63 between sycophancy and truthfulness, indicating social compliance trades against factual accuracy. Egotistical Validation prompts act as a sycophancy trap (mean 3.27), nearly double Unethical Proposals (1.72). Simple guardrails outperform elaborate Protocol scaffolding on flagship models, but distilled Gen 3.0 Flash inverts this, suggesting small models may structurally require chain-of-thought scaffolding. We release the dataset and rubric to support continuous sycophancy measurement.

---


### 9. [Temporal Preference Concepts and their Functions in a Large Language Model](https://arxiv.org/abs/2606.05194)

**<font color=#1a73e8>作者：</font>** Ian Rios-Sialer, Shantanu Darveshi, Shuai Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being deployed to make decisions that require trading off near-term gains against long-term consequences, yet little is known about how they internally represent or resolve these tradeoffs. In this work, we causally localize an underlying subgraph for temporal preference in a distilled LLM (Qwen3-4B-Instruct-2507), identifying mid-to-upper-layer nodes through converging evidence from gradient-based attribution and activation patching. We find that the geometry of time horizon is encoded in the residual stream at the expected localized layers. A behavioral analysis reveals that unintervened LLMs discount the future several times less steeply than humans, yet this preference is unstable across contexts, motivating explicit control rather than implicit reliance on training. Finally, we find suggestive evidence that steering vectors can shift temporal preference. Our work demonstrates how mechanistic interpretability can bring us closer to reliable control over how LLMs plan and reason

---


### 10. [State commitment learning: training language models to distinguish computation from memory](https://arxiv.org/abs/2606.05201)

**<font color=#1a73e8>作者：</font>** Fei Ding, Yongkang Zhang, Runhao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning language models do not distinguish tokens used for computation from tokens that constitute persistent state: once generated, all hidden thoughts remain in context and influence future predictions. As a result, downstream reasoning may depend on failed attempts, dead ends, and private scratch work that should not be safely relied on later. We recast this phenomenon as a new training objective, state commitment learning: training models to explicitly distinguish information that should be committed as persistent state from temporary computation that can be discarded. We define a counterfactual criterion, persistent-state sufficiency, which makes it trainable and measurable whether an answer remains usable after hidden thoughts are erased. We then propose Counterfactual Erasure RL (CERL), which evaluates, under the same prefix, both a path that keeps hidden thoughts and a path that erases them, and gives reward only when the erasure path remains correct. We also introduce the Erasure Dependence Protocol and show across mathematics, long-chain logic, scientific QA, and multi-turn tool-use evaluation that CERL substantially reduces answer dependence on hidden thoughts without sacrificing accuracy, consistently outperforming correctness-only RL and long-answer SFT baselines.

---


### 11. [How Far Did They Go? The Persuasive Tactics of Covert LLM Agents in a Discontinued Field Experiment](https://arxiv.org/abs/2606.05256)

**<font color=#1a73e8>作者：</font>** Kokil Jaidka, Saifuddin Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study analyzes a publicly released dataset from a discontinued field experiment on Reddit's r/ChangeMyView. The intervention, conducted by unknown, external researchers and halted following ethical backlash, involved undisclosed AI-generated accounts engaging users in live debate. After public disclosure, Reddit authorized moderators to release an archive of the AI-generated comments, creating a rare opportunity to examine how large language models operated in an identity-rich deliberative forum without disclosure. We conduct a structured content analysis of this corpus, evaluating identity performance, authority signaling, alignment strategies, and activation of cognitive heuristics. Identity targeting or adoption appears in over two-thirds of comments, alignment moves and authority claims in nearly all of them, and cognitive-bias triggers -- particularly confirmation bias, representativeness, and availability -- in the large majority. These patterns co-occur systematically, composing a rhetorical architecture calibrated for persuasive efficiency rather than authentic deliberative participation. Compared against human-authored CMV counter-arguments, the agents inverted the typical distribution on every dimension: denser authority use, more adversarial alignment, and heavier reliance on external citation over experiential grounding. In such environments, distinctions between authentic and synthetic epistemic standing grow increasingly opaque -- an asymmetry that disclosure mandates alone cannot address. The results point toward auditing frameworks capable of assessing how AI systems structure credibility, not merely whether they are present.

---


### 12. [Scaling Laws for Behavioral Foundation Models over User Event Sequences](https://arxiv.org/abs/2606.05257)

**<font color=#1a73e8>作者：</font>** Rickard Brüel Gabrielsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly trained on sequences of user actions in recommendation, payments, fraud, and commerce, but these models still lack the kind of compute calibration that scaling laws provide for language models. We study a common two-part behavioral-model architecture: a feature-based event embedder maps each multi-modal item to a vector, and a decoder-only transformer predicts the next event from the resulting sequence. Across roughly 600 runs on real interaction data, spanning $10^{15}$-$10^{19}$ training FLOPs, we jointly vary four deployment-relevant axes: the two-part parameter split, critical batch size, model/data allocation, and the number of sampled negatives used after freezing the embedder. A small embedder ($s^{\star}\!\approx\!2\%$ of parameters) is compute-optimal at every budget we test because embedder parameters are both more expensive per step and exposed to far more repeated items than contextualizer parameters. Compute-optimal training is data-heavy relative to text at low compute, but its $D/N$ ratio moves toward the Chinchilla heuristic as compute increases. The sampled training objective and deployed ranking metrics disagree in ways that themselves scale: critical batch size, optimal negative count after freezing, and the agreement between loss and ranking quality all shift with compute and with the chosen evaluation metric. For negative sampling, larger budgets increasingly prefer more negatives; by $10^{19}$ FLOPs the active constraint is candidate-axis memory rather than FLOPs. In behavioral foundation models, the evaluation metric is therefore part of the scaling law: changing it can change the compute-optimal recipe.

---


### 13. [Data-efficient flood depth prediction through domain-aware coreset selection and tabular foundation models](https://arxiv.org/abs/2606.05265)

**<font color=#1a73e8>作者：</font>** Lipai Huang, Adithi Srinath, Manas Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Near-real-time flood depth prediction demands surrogate models that are accurate, fast, and transferable across watersheds. Supervised surrogates can match physics-based simulators in accuracy but need millions of training rows per watershed and cannot extrapolate beyond their original mesh. We propose a domain-aware coreset construction pipeline that conditions a tabular foundation model at inference time. The pipeline stratifies storms by return period and most-affected watershed, then samples hexagons with a target-aware spatial selector. With 0.7% of the per-watershed training pool, the model attains a mean $R^2$ of 0.663 across nine Houston-area watersheds, within 98.5% of the supervised reference ($R^2$ = 0.673). It transfers to held-out watersheds without task-specific retraining, staying ahead of a coreset-trained supervised baseline. On real storms it exceeds the supervised reference on a far out-of-distribution case and trails it on a mostly in-distribution one. Domain-aware coreset construction lets tabular foundation models deliver data-efficient, watershed-transferable flood predictions without per-watershed training.

---


### 14. [Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents](https://arxiv.org/abs/2606.05296)

**<font color=#1a73e8>作者：</font>** Dae Yon Hwang, Raunaq Suri, Valentin Villecroze 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents operate in two distinct regimes: open-weight agents amenable to reinforcement learning (RL) and black-box agents whose behaviour must be controlled purely at test time. Although black-box agents are often backed by state-of-the-art proprietary LLMs, API-only access precludes parameter-level optimization, rendering most RL methods inapplicable. To address this limitation, we turn to a known equivalence between RL and Bayesian inference. We propose Agentic Monte Carlo (AMC) to directly sample from the optimal policy of a black-box agent rather than training it through RL. The optimal policy is a posterior over trajectories whose prior we define as the fixed black-box LLM agent. We employ Sequential Monte Carlo to sample from this posterior by learning a value function to steer the agent while leaving the underlying black-box model unchanged. We validate AMC on three diverse environments from the AgentGym benchmark, demonstrating significant improvements over prompting baselines and even outperforming Group Relative Policy Optimization (GRPO) as we scale the test-time compute of our method. AMC demonstrates the feasibility of performing principled RL-style optimization of black-box LLM agents. Code is available at this https URL

---


### 15. [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308)

**<font color=#1a73e8>作者：</font>** Abhishek Divekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With PRECISE, we extended Prediction-Powered Inference to produce bias-corrected estimates of ranking evaluation metrics by combining a small human-labeled set with a large LLM-judged set. PPI is provably unbiased regardless of the LLM judge's error profile. We make it applicable to hierarchical metrics like Precision@K, where annotations are per-document but the metric is per-query, by reducing the output-space computation from O(2^|C|) to O(2^K). On the ESCI benchmark, augmenting 30 human annotations with Claude 3 Sonnet judgments reduces the standard error of Precision@4 estimates from 4.45 to 3.50 (a 21% relative reduction). In a production system, our framework correctly identified the best of three system variants from 100 human labels and 2 hours of domain-expert annotation; A/B testing confirmed this ranking with +407 bps in daily sales.

---


### 16. [LoRi: Low-Rank Distillation for Implicit Reasoning](https://arxiv.org/abs/2606.05315)

**<font color=#1a73e8>作者：</font>** Ryan Solgi, Jiayi Tian, Zheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Implicit chain-of-thought (iCoT) methods aim to internalize reasoning in large language models, but often underperform explicit CoT prompting. We empirically find that hidden-state reasoning trajectories exhibit low-rank structure. Motivated by this observation, we propose a low-rank distillation framework that transfers reasoning by aligning teacher and student trajectories in a shared low-rank tensor subspace using first- and second-order statistics. The resulting formulation captures the global structure of reasoning while supporting a compact latent reasoning process. We evaluate the method across multiple model families, including LLaMA and Qwen, at different scales on mathematical reasoning benchmarks. Our approach consistently improves performance, especially on challenging multi-step tasks, approaching explicit CoT accuracy and outperforming prior iCoT distillation methods.

---


### 17. [Trajectory Dynamics in Language Model Hidden States Predict Human Processing Costs Beyond Surprisal](https://arxiv.org/abs/2606.05346)

**<font color=#1a73e8>作者：</font>** Elan Barenholtz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human language comprehension unfolds sequentially: each word is processed in the context of those that came before, and the interpretation builds incrementally over time. Surprisal, the negative log probability of a word given its context, has been the dominant predictor of incremental processing cost. But surprisal reduces rich sequential representations to a single scalar at each word, discarding information about the direction in which the interpretation has been evolving. Dynamical-systems approaches suggest that the trajectory of the evolving interpretive state, not just its position at each moment,should shape processing, and language itself may have local momentum, since speakers plan utterances a few words at a time. We introduce trajectory extrapolation error: at each word, we fit a linear trajectory to the preceding hidden states of a transformer language model and measure deviation from the extrapolated path. On the Natural Stories corpus, this measure is nearly orthogonal to surprisal (r = .044) and independently predicts self-paced reading times. The effect is especially pronounced in garden-path sentences, strengthens with model scale (GPT-2 Small to Large), and replicates across architectures with different positional encoding schemes (GPT-2 vs. Pythia/RoPE). A displacement control shows the effect is not reducible to representational change magnitude: displacement and extrapolation error predict in opposite directions. These findings reveal two dissociable components of processing cost: word-level prediction error (surprisal) and sensitivity to the local momentum of the unfolding interpretation (trajectory extrapolation error).

---


### 18. [Biomazon: A Multimodal Dataset for 3D Forest Structure and Biomass Modeling in the Amazon Basin](https://arxiv.org/abs/2606.05368)

**<font color=#1a73e8>作者：</font>** Sayan Mandal, Rocco Sedona, Simon Besnard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate, spatially explicit characterization of tropical forest structure is essential for carbon accounting and ecosystem monitoring, yet most ML pipelines predict canopy-top height proxies (e.g., RH95/RH98) or AGBD as separate scalar targets, rather than learning the forest vertical structure as an ordered profile. The community lacks a ML-ready multimodal benchmark for predicting the entire GEDI RH profile jointly with AGBD, or for evaluating methods that enforce physically consistent ordering across RH percentiles. We address this with Biomazon, a 20 m multimodal benchmark dataset over the Amazon Basin that pairs GEDI RH and AGBD targets with multi-sensor predictors (Sentinel-1/2, ALOS-2 PALSAR-2, Copernicus DEM, Dynamic World LULC, and AlphaEarth embeddings) under standardized spatial splits and evaluation protocols. Using a shared encoder-decoder with task-specific heads as a baseline framework, we conduct a comprehensive ablation study of (i) backbone/model scale, (ii) modality contributions, and (iii) the use of auxiliary embeddings under standalone and fusion settings, and we report both single-target and joint-target results to quantify tradeoffs under a unified training protocol. Finally, we contextualize baseline performance through regionally aligned comparisons against existing gridded products, including GEDI L4D RH10-RH98 and AGBD, at matching temporal scale. Biomazon, together with the accompanying protocols and baseline results, establishes a reference benchmark for future work on structurally consistent RH-profile prediction and structure-biomass modeling in tropical forests.

---


### 19. [SHALA-LLM: Smartly Handling Ambiguous Labels in Aligning LLMs](https://arxiv.org/abs/2606.05376)

**<font color=#1a73e8>作者：</font>** Jingyao Wu, Ashley Wang, Keane Ong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many human-centered tasks, including natural language inference (NLI) and emotion recognition (ER), have multiple plausible interpretations, leading to label ambiguity and challenging disagreements across human annotators. As LLMs are increasingly deployed in real-world settings, faithfully modeling such ambiguity is essential to identify contested inputs, preserve variability in ambiguous cases, and capture the full distribution of human judgments. Yet, existing LLM alignment approaches have predominantly assumed a single correct label, excluding annotator disagreement during optimization. Instead of treating this ambiguity as noise, we show how to treat it as information that improves model behavior through a new algorithm called SMARTLY HANDLING AMBIGUOUS LABELS IN ALIGNING LLMS (SHALA-LLM). This reinforcement learning framework provides a new way for LLMs to learn directly from annotator distributions while dynamically prioritizing highly ambiguous samples during optimization. Experiments on ambiguity-sensitive NLI and ER benchmarks, including ChaosNLI, GoEmotions, and MSP-Podcast, demonstrate that SHALA-LLM improves agreement with annotator label distributions, e.g. on ChaosNLI, it reduces Jensen-Shannon Distance by up to 62.1%. At the same time, SHALA-LLM improves F1 by up to 16.7%, showing that modeling annotator disagreement can also strengthen classification performance.

---


### 20. [Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models](https://arxiv.org/abs/2606.05378)

**<font color=#1a73e8>作者：</font>** Yongzhong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We test whether a single screen-and-ablate recipe -- identify attention-head circuits by task-pattern selectivity, then verify by causal ablation against a matched-random null -- produces consistent mechanistic claims across model families. The recipe ports across pipelines; the specific circuit it identifies does not. Across four composed tasks (indirect-object identification, greater-than, successor sequences, variable binding) and three 1B-class language models from distinct training pipelines (Pythia 1B / Pile / dense; OLMo 1B / DCLM / dense; OLMoE 1B-7B / DCLM / mixture-of-experts), we run a unified protocol with the matched-random null sampled across ten seeds per cell. The resulting 12 (task, model) cells contain no two that share the same primary causal screen at comparable effect size: the same task, with the same behavioral capability, is implemented through different attention-pattern types across models.
We introduce a five-category screen-outcome taxonomy -- primary cause, secondary cause, correlate, interferer, null -- with quantitative thresholds, and show that all five outcomes appear in the panel. We propose a falsifiable hypothesis: the MoE model in our panel builds composed-task circuits on top of a foundational previous-token positional substrate (the prev-token-circuit ablation is the strongest causal screen on 3 of 4 tasks for OLMoE 1B-7B), with the IOI exception consistent with IOI being a final-position name-copying task whose structure directly probes a different pattern. The hypothesis comes with explicit predictions for other MoE language models.
We frame the methodology honestly: the spectral participation-ratio signal from the companion methodology paper is a general indicator of specialized computation; what makes a finding task-specific is the task-pattern screen plus a per-model causal verification.

---


### 21. [Synthetic Contrastive Reasoning for Multi-Table Q&A](https://arxiv.org/abs/2606.05382)

**<font color=#1a73e8>作者：</font>** Ankit Pratap Singh, Xin Su, Phillip Howard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-table question answering requires models to retrieve relevant evidence, link schemas, and perform compositional reasoning across relational tables. Existing multi-table Q&A resources typically provide questions and final answers but lack reasoning supervision that explains how answers are derived. To address this gap, we construct a synthetic contrastive reasoning-trace dataset for MMQA by generating validated positive traces and plausible negative traces with heterogeneous LLMs. We then use the resulting preference pairs to fine-tune open-weight LLMs with Contrastive Preference Optimization (CPO). Across Qwen3-14B, Mistral-8B, and Llama-3.1-8B, CPO achieves absolute average improvements over Q&A supervised fine-tuning ranging from 9.7%-16.3%, with gains up to 21 percentage points on MMQA. Ablations show that heterogeneous positive and negative trace generators strengthen the contrastive signal, and automated as well as human evaluations indicate that the generated pairs are largely faithful, coherent, and meaningfully contrastive.

---


### 22. [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384)

**<font color=#1a73e8>作者：</font>** Srimonti Dutta, Akshata Kishore Moharir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge evaluation is widely used in benchmarking pipelines, where model outputs are compared and ranked using automated evaluators. These pipelines typically assume that judgments are stable properties of fixed inputs. We show that this assumption does not hold under interaction. We study post-decision manipulability: the extent to which an evaluation outcome can be altered through subsequent conversation with the judge after an initial decision has been made. Across controlled experiments on MT-Bench and AlpacaEval, we find that LLM judges are highly stable under repeated and neutral reevaluation, yet become substantially reversible under targeted post-decision challenge. An anti-baseline challenge protocol shows that stable judgments can be overturned through motivated interaction, while a counterbalanced target-validation protocol separates this reversibility from net target-directed steering. These reversals have practical consequences: they can degrade agreement with human preferences, shift benchmark rankings, and produce harmful evaluation changes despite high self-reported confidence. Authority framing is especially destabilizing, and revised judgments are often accompanied by low-overlap justifications, suggesting post hoc rationalization rather than reliable error correction. We introduce the Evaluation Robustness Score (ERS) to quantify interactional robustness by combining reversal susceptibility with counterbalanced directional effects. Our findings identify post-decision interaction as a distinct failure mode for LLM-as-judge evaluation and motivate evaluation protocols that measure not only static agreement, but robustness under challenge.

---


### 23. [Ahoy: LLMs Enacting Multiagent Interaction Protocols](https://arxiv.org/abs/2606.05390)

**<font color=#1a73e8>作者：</font>** Omkar Joshi, Munindar P. Singh, Amit K. Chopra  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An interaction protocol formalizes how the agents in a multiagent system interact, which facilitates implementing agents. Existing approaches yield agent implementations specific to the selected protocols. How can we engineer intelligent agents that can enact protocols but are programming-free? Our contribution, Ahoy, addresses this question by creating LLM agents that dynamically select and enact declarative protocols to achieve user goals. We demonstrate that an \ahoy agent can correctly and intelligently enact multiple protocols - concurrently if appropriate to the user goal - without specialized training. Ahoy's significance lies in that it brings together declarative protocols and LLMs, both approaches that promise improved knowledge engineering for agents.

---


### 24. [ReasoningFlow: Discourse Structures for Understanding LLM Reasoning Traces](https://arxiv.org/abs/2606.05402)

**<font color=#1a73e8>作者：</font>** Jinu Lee, Shivam Agarwal, Amruta Parulekar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) produce reasoning traces with non-linear structures, such as backtracking and self-correction, that complicate the evaluation and monitoring of the reasoning process. We introduce ReasoningFlow, a framework that captures the discourse structures of LRM reasoning traces into fine-grained directed acyclic graphs (DAGs). We develop and validate our annotation schema through careful manual annotation of 31 traces (2.1k steps), achieving high inter-annotator agreement, then scale to automatic annotation of 1,260 traces (247.7k steps) spanning three tasks (math, science, argumentation) and five models (Qwen2.5-32B-Inst, QwQ-32B, DeepSeek-V3, DeepSeek-R1, GPT-oss-120B). By analyzing ReasoningFlow graphs, we find: (1) LRMs exhibit structurally similar traces, despite being trained from different base models and potentially non-overlapping post-training data. (2) ReasoningFlow reveals diverse fine-grained reasoning behaviors (e.g., local verification, self-reflection, and assumptions) that can be used for better reasoning trace monitorability. (3) In LRMs, most of the erroneous steps are not used to derive final answers. (4) Mechanistic causal dependencies between steps do not reflect the language-level discourse structure. We release the dataset and code in: this https URL.

---


### 25. [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403)

**<font color=#1a73e8>作者：</font>** Rohan N. Pradhan, Steve Goley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models increasingly act as epistemic proxies, synthesizing evidence from multiple sources to inform decisions. Whether they evaluate the quality of that evidence, or merely aggregate it based on surface presentation, remains poorly understood. We show that models possess the capability to detect fabricated statistics (correct identification rates of 0.76-1.00 for methodology in isolation) but do not recruit this capability during multi-source synthesis, producing similar numeric estimates whether the statistics are fabricated or valid. Specifically, source influence is governed by a methodology-register gate that responds to the distributional register of analytical text but not to numeric validity: for example, statistically impossible confidence intervals receive the same weight as valid ones. The behavioral dissociation replicates across five models from three families (Claude, Qwen, OLMo) and three professional domains. Mechanistic analyses, including causal tracing, linear probes, and component-level attribution, converge on the same account: the model encodes and causally uses a methodology-register representation that transfers across domains (probe AUC 0.83-0.92), while numeric-validity signals, decodable in isolation, are suppressed to chance during multi-source synthesis. Prompting-based mitigations, even an oracle checklist naming the exact statistical checks, produce blanket skepticism rather than selective discernment, and the post-training pipelines we examine reinforce the stylistic shortcut without building numeric verification. Unlike sycophancy, which tracks user preference, this failure tracks whether a source presents as analytically credible, not whether its claims are internally consistent. We term this epistemic alignment: like preference and safety alignment, the question is not capability but deployment.

---


### 26. [Harnessing Generalist Agents for Contextualized Time Series](https://arxiv.org/abs/2606.05404)

**<font color=#1a73e8>作者：</font>** Zihao Li, Kaifeng Jin, Yuanchen Bei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series are often embedded in rich contexts that are essential for holistic modeling. Moreover, real-world practitioners often require end-to-end workflows for analyzing temporal dynamics, where widely studied tasks such as forecasting are only one step in a broader solution loop. While generalist AI agents offer a promising interface for such workflows under complex contexts, they still operate primarily in textual spaces that are not fully aligned with structured temporal signals. In this work, we introduce TimeClaw, an agentic harness framework for time series that equips generalist LLM agents with the time series-native runtime support needed for contextualized temporal reasoning. TimeClaw integrates executable temporal tools for grounded and auditable analysis, experience-driven capability evolution for creating reusable analytical routines, and episodic multimodal memory for retrieving relevant reasoning traces. Together, these components unlock harnessed open-ended temporal reasoning with contextual information. Extensive evaluation on multiple benchmarks covering diverse tasks across energy, finance, weather, traffic, and other real-world domains demonstrates improved performance of TimeClaw. Code is available at this https URL.

---


### 27. [Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution](https://arxiv.org/abs/2606.05408)

**<font color=#1a73e8>作者：</font>** Can Gurkan, Forrest Stonedahl, Uri Wilensky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM repeatedly mutates a program, does it explore new forms or circle back to the same ones? We study this question by analyzing LLM-driven mutation chains in the absence of selection pressure within a domain-specific language, varying prompt design, model family, and stochastic replication. We find that LLM-based mutation consistently converges toward restricted attractor regions in program space. Convergence is especially severe at the structural level: in 87% of chains, over 93% of mutations revisit a previously seen structural form, with most variation confined to terminal substitutions within recurring templates. Cycle analysis reveals short cycles and self-loops dominating the transition structure. The rate of convergence varies with prompt wording and model choice, but the phenomenon is robust across conditions. A classical GP subtree mutation operator does not exhibit comparable convergence, suggesting that the effect is intrinsic to the LLM mutation pipeline. These findings reveal a tension at the heart of LLM-driven program evolution: the same capabilities that enable semantics-aware program transformation also carry a systematic bias toward structural homogeneity that must be accounted for if such systems are to sustain open-ended exploration. Source code is available at this https URL.

---


### 28. [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414)

**<font color=#1a73e8>作者：</font>** Avinash Baidya, Xinran Liang, Ruocheng Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Early failure alerting requires deciding, while a dialog or agent trajectory is still unfolding, whether to flag it as likely to fail. This is challenging because supervision is typically available only as a trajectory-level success/failure label while alerts must be raised from partial interactions. Prior early-classification methods often bridge this gap by assigning the terminal label to every prefix, treating every turn as failure evidence. We hypothesize that this prefix-label assumption is poorly matched to multi-turn language interactions, where evidence of eventual failure is sparse and often delayed. In this paper, we introduce a two-stage approach that learns from this sparse evidence structure and uses the resulting risk estimates for controllable early alerting. Specifically, our attention-based failure predictor learns sparse turn-level failure evidence from trajectory labels and uses it to estimate failure risk from partial histories. We then pair this predictor with $\alpha$-STOP, a single preference-conditioned stopping policy that selects an accuracy-earliness operating point at inference time rather than training a separate trigger for each preference. Across five benchmarks spanning customer support, task-oriented dialog, persuasion, tool use, and planning, we first show that high-relevance failure evidence occupies only 4.7-11.3% of turns and first appears after 59.0-83.6\% of trajectories on average. We further show that the attention-based predictor improves Pareto-frontier quality (hypervolume) by 1-10\% over naive prefix supervision, and that the full system improves frontier quality by 3-42\% over state-of-the-art trigger policies while reducing training cost per operating point by 1-3 orders of magnitude.

---


### 29. [Minimizing the Hidden Cost of Scales: Graph-Guided Ultra-Low-Bit Quantization for Large Language Models](https://arxiv.org/abs/2606.05429)

**<font color=#1a73e8>作者：</font>** Rayyan Abdalla, Amir Hussein, Min Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is critical for the efficient deployment of large language models (LLMs). Recent ultra-low-bit PTQ methods rely on rigid weight-saliency assumptions or position heuristics, introducing substantial hidden scaling overhead. We propose SAGE-PTQ (Saliency-Aware Graph-guided Efficient PTQ), a novel ultra-low-bit quantization framework for LLMs that minimizes hidden scaling cost. SAGE-PTQ separates salient and unsalient weights using distributional statistics, then models subsampled unsalient weights as a sparse graph to estimate the optimal number of groups per layer. SAGE-PTQ applies dual-mode quantization, assigning multi-bit precision to salient weights and binarizing unsalient weights. To reduce scaling overhead, SAGE-PTQ uses one per-channel scale for salient weights and one scalar per unsalient group. Finally, SAGE-PTQ implements adaptive saliency thresholding to select the optimal saliency ratio per matrix. SAGE-PTQ achieves 1.03 weight bits and only 0.004 scaling bits per matrix on average, outperforming state-of-the-art methods such as BiLLM and PB-LLM. On LLaMA-3-8B, SAGE-PTQ achieves 6.74 WikiText2 perplexity, compared to 55.8 for BiLLM, while using less than 50% of BiLLM's GPU memory. On LLaMA-2-70B, SAGE-PTQ provides 1.5x faster decoding on one NVIDIA L40 GPU, demonstrating practical inference efficiency.

---


### 30. [Selective-Advantage Entropy-Adaptive Horizon GRPO: Asymmetric Token-Level Discounting for Efficient Reinforcement Learning of Language Models](https://arxiv.org/abs/2606.05434)

**<font color=#1a73e8>作者：</font>** Chirag Chawla, Rohan Charudatt Salvi, Madhav S. Baidya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimisation (GRPO) has emerged as an effective reinforcement-learning algorithm for aligning language models on reasoning tasks, but it treats every token position and every sampled rollout symmetrically. We introduce two complementary extensions: (i) Adaptive-Horizon GRPO (AH-GRPO), which weights each token's policy gradient using a cumulative entropy-based discount that reduces the effective horizon when the model is uncertain, and (ii) Selective-Advantage AH-GRPO (SA-AH-GRPO), which applies this discounting only to negative-advantage rollouts, leaving positive-advantage, successful trajectories unattenuated. We evaluate standard GRPO with alpha = 0, AH-GRPO with alpha = 0.5, and SA-AH-GRPO with alpha = 0.5 on the GSM8K mathematical reasoning benchmark using both Qwen 2.5-1.5B-Instruct and Qwen 2.5-3B-Instruct fine-tuned with LoRA. On the 3B model, SA-AH-GRPO achieves Pass@1 = 0.858 at its peak at step 30 and maintains 0.846 at 180 steps, with training variance reduced to 0.0246, a 3.6 times reduction relative to GRPO while matching its peak accuracy. On the 1.5B model, SA-AH-GRPO achieves a peak Pass@1 of 0.686, improving over the zero-shot baseline of 0.637. Our analysis shows that asymmetric discounting preserves the full gradient signal on correct solutions, prevents entropy collapse, and substantially stabilises training, suggesting a principled inductive bias for reinforcement learning with verifiable rewards on structured generation tasks.

---


### 31. [Ten Headache Specialists versus Artificial Intelligence for Clinical Literature Summarization: A Critical Evaluation and Comparison](https://arxiv.org/abs/2606.05436)

**<font color=#1a73e8>作者：</font>** Alejandro Lozano, Keiko Ihara, Ping-Hao Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Summarizing the latest medical literature to guide clinical decision-making is essential for evidence-based medicine and high-quality patient care. Yet clinicians face increasing challenges due to limited time with patients and a rapidly growing volume of published articles. Although retrieval-augmented large language models (LLMs) have shown promise in clinical summarization, human evaluations of their effectiveness in synthesizing broader scientific literature and direct comparisons to expert-written syntheses remain scarce. We constructed a RAG-based agentic AI framework using three state-of-the-art LLMs: Sonnet, GPT-4o, and Llama 3.1. A headache specialist created 13 questions, three for prompt optimization and ten for evaluation. Ten headache specialists across the United States and Canada each wrote a summary for one question, yielding four summaries per question (expert, Sonnet, GPT-4o, and Llama). The experts, blinded to authorship, critically evaluated the summaries, excluding the topic for which they wrote a summary, based on correctness, completeness, conciseness, and clinical utility, scoring each from 1 to 10 using standardized rubrics. They also ranked the summaries by preference and indicated whether they believed each summary was written by an expert or an LLM. Our study, comparing LLM- and expert-written literature summaries evaluated by headache specialists, showed that expert-written summaries were preferred, although experts sometimes found it challenging to distinguish between human- and AI-generated summaries. We also identified key expert-valued features beyond standard evaluation metrics that can guide future refinement of both human and AI literature summarization pipelines.

---


### 32. [GOTabPFN: From Feature Ordering to Compact Tokenization for Tabular Foundation Models on High-Dimensional Data](https://arxiv.org/abs/2606.05441)

**<font color=#1a73e8>作者：</font>** Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Kumar Gyawali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate how to make small tabular foundation models effective for High-Dimensional, Low-Sample Size (HDLSS) tabular prediction without retraining large backbones. We introduce Graph-guided Ordering with Local Refinement (GO-LR), show its equivalence to weighted Minimum Linear Arrangement, and interpret the practical solver as a TSP-path-style surrogate. We propose GOTabPFN,which builds on GO-LR, and a Neuro-Inspired Subunit Compression (NSC) unit to pool locally adjacent ordered features into meta-features, yielding a compact representation that makes TabPFN-style prediction practical in HDLSS regimes. Across tabular benchmarks, GOTabPFN improves stability and accuracy under tight token budgets.

---


### 33. [Brick-Composer: Using MLLMs for Assembly with Diverse Bricks](https://arxiv.org/abs/2606.05445)

**<font color=#1a73e8>作者：</font>** Jiateng Liu, Bingxuan Li, Zhenhailong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We dream of AI agents that can read arbitrary designs and construct real-world objects from reusable building blocks. As a first step toward this vision, we study whether multimodal large language models (MLLMs) possess the visual grounding and spatial reasoning capabilities required for brick assembly. We formulate brick assembly as a sequential decision-making problem, where each step involves two subtasks: brick selection, identifying the target brick from candidate components, and brick pose estimation, predicting where and how the selected brick should be placed. To support this study, we introduce BC-Bench (Brick Construction Benchmark), the first benchmark for evaluating MLLMs on assembly with diverse bricks. Experiments show that current state-of-the-art MLLMs remain far from reliable builders, struggling with fine-grained brick selection and failing at precise pose estimation. To bridge this gap, we propose Brick-Composer, a learning framework that equips MLLMs with assembly skills through three complementary signals: Human Design Sparks, which provide affordance-rich construction demonstrations; World Feedback, which grounds predicted actions in visual and physical consequences; and Synthetic Experience, which scales learning beyond existing object designs. Brick-Composer improves brick selection accuracy by over three times, substantially reduces pose estimation errors, and raises strict step-level assembly success from less than 1% to around 15%. After training, a Qwen-3-8B can correctly compose up to 42% of the steps for a complete object, suggesting that MLLMs can acquire assembly capabilities through targeted, physically grounded learning.

---


### 34. [Insurance of Agentic AI](https://arxiv.org/abs/2606.05449)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence (AI) systems are transforming the risk landscape by extending beyond information generation to autonomous planning, tool invocation, decision execution, and persistent modification of digital and physical environments. These capabilities introduce novel exposures that do not fit neatly within traditional insurance categories such as cyber, professional liability, product liability, or directors and officers coverage. This paper examines the emerging insurance market for agentic AI and develops a framework for understanding its underwriting, pricing, reinsurance, and product-design implications. We characterize agentic AI as a continuum of autonomy and delegated authority, emphasizing the distinction between informational outputs and systems capable of independently generating insured events through external actions. We analyze major risk pathways, including hallucinations, prompt-injection attacks, autonomous decision errors, model drift, dependency failures, and cyber-physical harms, and evaluate how existing insurance products are adapting to address these exposures. The paper further proposes an actuarial framework based on exposure assessment, scenario analysis, dependency mapping, and accumulation-risk management, drawing parallels to the evolution of cyber insurance. Finally, we present a coordinated insurance architecture that integrates cyber, technology errors and omissions, product liability, performance-warranty, and affirmative AI-liability coverages through explicit allocation mechanisms and dedicated AI aggregates. The analysis suggests that the future of agentic-AI insurance lies not in a single monoline product but in a layered ecosystem of complementary coverages supported by improved governance, transparency, telemetry, and regulatory clarity.

---


### 35. [PSEBench: A Controllable and Verifiable Benchmark for Evaluating LLMs in Patient Safety Event Triage](https://arxiv.org/abs/2606.05463)

**<font color=#1a73e8>作者：</font>** Keqi Han, Ryan Young, Annabel Strauss 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patient safety event triage, determining whether a clinical event is reportable under jurisdiction-specific policy, is a high-stakes task typically performed manually by patient safety experts. Although LLMs may support this workflow, reliable evaluation is limited by the lack of benchmarks to capture evidence-grounded policy reasoning, proactive information seeking for incomplete reports, and principled abstention in irreducibly ambiguous cases. We address this gap with a policy-grounded construction methodology centered on the clause card, a structured representation that factorizes regulatory text into auditable decision specifications. Combining clause cards with anchor-driven instantiation and closed-loop verification, our scalable pipeline produces narratives with by-construction ground truth and naturally supports generating missing information and uncertain variants. We instantiate this method on Minnesota's 29 Reportable Adverse Health Events, producing PSEBench, a 5,074-case benchmark with an agentic evaluation environment. Evaluation on 15 representative LLMs reveals consistent capability trends, demonstrates the benchmark's utility, and identifies actionable gaps toward reliable LLM-based patient safety event triage.

---


### 36. [Step-by-Step Optimization-like Reasoning in LLMs over Expanding Search Spaces](https://arxiv.org/abs/2606.05464)

**<font color=#1a73e8>作者：</font>** Nicolás Astorga, Nabeel Seedat, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifiable reward training has improved mathematical and coding reasoning, but these domains capture only part of step-by-step decision making. Many real-world tasks require finding a high-value feasible plan among many valid alternatives. We introduce OPT*, a scalable family of optimization-style tasks for training and evaluating LLM step-by-step optimization-like reasoning along a complexity axis: each task provides a feasibility checker and evaluator, while a complexity parameter expands the search space without requiring new human labels. This motivates studying these tasks in two regimes: (i) solver-guided online policy optimization, which uses a solver as a value oracle for partial states and applies rank-based reward shaping to reinforce better next steps, and (ii) search-based offline RL when such solvers are unavailable. Theoretically, we relate success in large search spaces to the information a reasoner extracts per unit of search budget. Empirically, we ablate the ingredients that make search efficient on OPT* and show that training on OPT* improves step-by-step optimization-like reasoning.

---


### 37. [Towards Unified and Data-Efficient Prognostics and Health Management with Tabular Foundation Models](https://arxiv.org/abs/2606.05481)

**<font color=#1a73e8>作者：</font>** Raffael Theiler, Lev Telyatnikov, Leandro Von Krannichfeldt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven Prognostics and Health Management (PHM) uses time-varying condition-monitoring data to diagnose system states and estimate remaining useful life in engineered assets. These tasks are central to maintenance planning, but industrial PHM data are often fragmented, partially observed, and poorly labeled, which hinders supervised learning. Foundation models offer a route toward reusable predictive systems, yet most time-series foundation models are designed for forecasting and assume long, coherent, regularly sampled sequences. To address this gap, we propose a framework for applying Tabular Foundation Models to industrial time series using in-context learning, and we evaluate them on a variety of PHM tasks. By converting raw unit-level signals into tabular rows, we show that these models perform well across multiple tasks - including prognostics, and diagnostics - and are highly data efficient. We compare them directly with sequence models, transformer baselines, and gradient-boosted trees under a common evaluation protocol. The results indicate that tabular foundation models achieve the best average ranks across prognostic and diagnostic tasks. Our findings further show that PFN-based models are competitive in low-data regimes, that temporal context can be preserved in the tabular representation, and that performance depends on representative context construction under subsampling. These results demonstrate that tabular foundation models provide a practical and general interface for heterogeneous PHM problems.

---


### 38. [Localizing Prompt Ambiguity in Large Language Models with Probe-Targeted Attribution](https://arxiv.org/abs/2606.05486)

**<font color=#1a73e8>作者：</font>** Govind Ramesh, Yao Dou, Wei Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt ambiguity is a common source of failure in large language models, but is difficult to localize because it is a latent property of the prompt, while existing attribution methods are designed to explain observable outputs such as logits or generated tokens. We introduce PRIG, a gradient attribution method that uses a probe logit to attribute latent ambiguity to token positions. Specifically, PRIG trains a linear probe to distinguish clear prompts from ambiguous prompts and attributes the probe score to earlier token representations in the residual stream. To enable token-level evaluation, we construct synthetic ambiguity datasets across coding, math, and writing by rewriting one task-critical sentence per prompt, and complement them with a human-written gold benchmark. In this setting, PRIG localizes ambiguous spans substantially better than gradient attribution baselines, achieving 0.840 AUROC on the combined synthetic benchmark and 0.891 AUROC on the gold set. It also outperforms GPT-5.4 on sentence-level ambiguity identification and retains useful signal out-of-domain. These results establish PRIG as a practical tool for identifying which parts of a prompt are ambiguous. More broadly, they suggest that latent prompt properties can be localized through intermediate representations, rather than through output-level attribution.

---


### 39. [LLM-Guided ANN Index Optimization for Human-Object Interaction Retrieval](https://arxiv.org/abs/2606.05489)

**<font color=#1a73e8>作者：</font>** Shahrzad Esmat, Chaunte W. Lacewell, Sameh Gobriel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval systems underpin modern AI applications -- spanning visual search, recommendation engines, and multi-modal question answering. Modern multi-stage retrieval systems require the joint optimization of highly coupled parameters, yet traditional hyperparameter optimization (HPO) methods -- including Tree-structured Parzen Estimators (TPE) and Gaussian Process Bayesian Optimization -- rely on an independence assumption that fundamentally prevents them from navigating these coupled configuration spaces. We address this limitation with a phase-aware large language model (LLM) agent that conditions each proposal on its full optimization history, navigating the coupled parameter space across phase-partitioned exploration, exploitation, and fine-tuning stages. Evaluated on the HICO-DET human-object interaction retrieval benchmark using Intel VDMS (Visual Data Management System), our agent outperforms Optuna TPE by +33.3% and VDTuner by +34.2% under SIEVE (Safeguarded Index Evaluation of Vector-search Efficiency, a quality-constrained throughput metric), delivering a 15.3x throughput gain over UniIR. Validation across three benchmarks confirms that the agent's advantage grows with the degree of parameter coupling: +33.3% on HICO-DET (high coupling), methods converge within 1% on GLDv2 (moderate coupling) and within 3.6% on SIFT1M (near-independent control). Cross-system validation on Milvus confirms the optimizer ranks first on all three datasets without modification, demonstrating transferability across vector database management system (VDBMS) platforms.

---


### 40. [LEVANTE-bench: Multi-Scale Comparison of VLMs to Children Using Cognitive Tasks (or, "Is Your VLM Smarter Than a 5th Grader?")](https://arxiv.org/abs/2606.05497)

**<font color=#1a73e8>作者：</font>** Alvin Wei Ming Tan, David Cardinal, Tania Lorido-Botran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given the inherently multimodal nature of human experience, vision-language models (VLMs) hold substantial promise for modeling human cognition as it grows and develops with experience. Realizing their potential requires tools for comparing VLMs with human cognitive development across tasks, ages, and populations. We present LEVANTE-bench, a benchmark based on tasks and data from the Learning Variability Network (LEVANTE), which distributes open-source tasks and data measuring children's cognition across languages and cultures. In LEVANTE-bench, we systematically assess VLMs on six tasks, comparing their alignment with children aged 5-12 ($N$ = 1547) across three countries. We compare models at multiple scales, assessing their overall accuracy, their task- and item-level alignment with children, and how well they match children's trial-level error distributions. Alignment was heterogeneous across scales: at the level of tasks and items, more capable models aligned better with humans. However, match to human error distributions varied widely across tasks, and for several tasks, smaller models matched younger children's errors better. In addition, even the best-performing VLMs struggled on matrix reasoning and mental rotation tasks. Thus, current VLM architectures align only partially with the cognitive abilities of children.

---


### 41. [BRepCLIP: Contrastive Multimodal Pretraining on BRep Primitives for CAD Understanding](https://arxiv.org/abs/2606.05515)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Didier Stricker, Mohammad Sadil Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning representations of CAD models is a largely open problem. While 3D representation learning has flourished around point clouds and meshes, the native format of CAD - boundary representations BReps, which encodes exact parametric surfaces, curves, and their topology, has received little attention as a representation learning substrate. We introduce BRepCLIP, the first framework to align BRep geometry with language and image embeddings through contrastive pretraining. We model each CAD object as a sequence of face and edge tokens with separate discrete vocabularies for surface and curve geometry, augmented with spatial and semantic descriptors that capture surface types (e.g., cylindrical, torus, NURBS) and curve primitives (e.g., line, arc, B-spline). A transformer encoder aggregates these tokens into a global BRep embedding, aligned with CLIP's text and image encoders via a joint contrastive objective. BRepCLIP generates more discriminative and semantically grounded embeddings than existing point-based alternatives, improving Top-1 retrieval over OpenShape by 40.4%, 22.0%, and 23.9% on ABC, CADParser, and Automate, respectively, and improving zero-shot classification on FabWave by 15% in Top-1 score. We further demonstrate its utility as a CAD-aware similarity metric for evaluating text and image-conditioned CAD generation, establishing the importance of structure-aware pretraining for multimodal CAD understanding. Project page is available at this https URL

---


### 42. [Dominant-Layer ZO: A Single Layer Dominates Zeroth-Order Fine-Tuning of LLMs](https://arxiv.org/abs/2606.05516)

**<font color=#1a73e8>作者：</font>** Wanhao Yu, Ziyan Wang, Zheng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables memory-efficient fine-tuning of large language models (LLMs) using only forward passes, but it remains unclear how useful adaptation is distributed across layers. In this work, we reveal a surprising phenomenon: ZO fine-tuning is sharply dominated by a single decoding layer. Across multiple LLM families and downstream tasks, fine-tuning this dominant layer alone consistently matches or even exceeds full-model ZO fine-tuning. We further show that the dominant layer is task-agnostic but model-specific, and can be identified before training through a simple inference-only analysis of activation outliers. Specifically, the dominant layer consistently aligns with the first activation-outlier layer in the pre-trained model. To explain this phenomenon, we analyze how perturbation effects propagate under ZO optimization. We find that the dominant layer combines two key properties: high perturbation sensitivity and early placement in the residual stream, allowing perturbation-induced effects to propagate and accumulate through remaining subsequent decoding layers. As a result, this layer produces disproportionately strong and stable optimization signals under forward-only updates. Extensive experiments on LLaMA2-7B and Qwen3-8B across nine benchmarks show that dominant-layer ZO fine-tuning improves average performance over full-model MeZO and LoRA-based ZO fine-tuning while achieving up to 4.52$\times$ training speedup.

---


### 43. [CHASE: Adversarial Red-Blue Teaming for Improving LLM Safety using Reinforcement Learning](https://arxiv.org/abs/2606.05523)

**<font color=#1a73e8>作者：</font>** Rahul Markasserithodi, Aditya Joshi, Yuekang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in safety alignment, prompt-rewriting attacks such as persona modulation, fictional framing and persuasion-based reformulation, can bypass safety filters even on frontier models. Existing defenses either rely on non-scalable human curation or white-box optimisation that overfits to specific model internals, leaving aligned models brittle against the very class of adaptive black-box adversaries they will face in deployment. To address this gap, we introduce CHASE (Co-evolutionary Hardening through Adversarial Safety-Escalation), a closed-loop red-blue teaming framework in which a black-box attacker and a safety-aligned defender co-evolve. The attacker is trained via Group Relative Policy Optimization (GRPO) under a multiplicative reward that jointly enforces bypass effectiveness and intent fidelity, while the defender is hardened on the harvested adversarial rewrites through a two-stage GRPO + rejection-sampled SFT pipeline balanced with benign data. Evaluated on BeaverTails and JailbreakBench against five held-out attack families (PAIR, TAP, AutoDAN, PAP, Translation), CHASE cuts mean StrongREJECT score by 43.2\% with 0\% false-refusal on benign prompts. Beyond the headline result, CHASE shows that template-free RL exploration recovers latent attack primitives that transfer across mechanistically distinct attack families, suggesting a path toward LLM safety hardening that generalises beyond the narrow distributions achieved thus far in adversarial training.

---


### 44. [Almieyar-Oryx-BloomBench: A Bilingual Multimodal Benchmark for Cognitively Informed Evaluation of Vision-Language Models](https://arxiv.org/abs/2606.05531)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abootorabi, Omid Ghahroodi, Anas Madkoor 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of Vision-Language Models (VLMs), the field lacks benchmarks that rigorously diagnose their true reasoning abilities and chart meaningful progress toward human-like multimodal intelligence. Most existing evaluations focus on piecemeal or disconnected tasks, obscuring critical cognitive weaknesses and providing little insight for targeted improvement. To address this gap, we introduce BloomBench, part of the Almieyar benchmarking series, the first cognitively human-grounded, bilingual (English-Arabic) multimodal benchmark for VLMs. Grounded in Bloom's Taxonomy, BloomBench systematically evaluates six levels of cognition (Remember, Understand, Apply, Analyze, Evaluate, Create) through carefully designed image-question-answer tasks. Built with a semi-automated pipeline and validated through a stratified hybrid quality assurance protocol, it ensures scalability, cultural inclusivity, and linguistic fidelity. Leveraging this framework, we conduct a comprehensive study of state-of-the-art VLMs to diagnose their cognitive profiles. Our analysis reveals a sharp cognitive asymmetry: while state-of-the-art models achieve strong performance ceilings in semantic understanding, they struggle substantially with factual recall and creative synthesis. This demonstrates that current general multimodal proficiency masks deeper limitations in specific cognitive layers. Furthermore, our study highlights a critical performance gap between Arabic and English, exposing limitations in current cross-lingual multimodal reasoning. These findings establish a foundation for developing more cognitively aligned and inclusive VLMs. The benchmark framework and dataset is available at: this https URL.

---


### 45. [Noise-Aware Visual Representation Learning for Medical Visual Question Answering](https://arxiv.org/abs/2606.05535)

**<font color=#1a73e8>作者：</font>** I Putu Adi Pratama, Bahadorreza Ofoghi, Atul Sajjanhar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical visual question answering (Med-VQA) has strong potential for clinical decision support by enabling AI models to interpret medical images and answer clinically relevant queries. Recent approaches typically connect off-the-shelf vision encoders with large language models (LLMs) through lightweight mapping networks to reduce computational cost. However, these methods often overlook the importance of handling noise and small irrelevant changes in visual representations. To address these challenges, we propose a noise-aware Med-VQA framework that incorporates a denoising autoencoder before visual embeddings are mapped into the input space of an LLM. The denoising autoencoder is pretrained to reconstruct clean visual embeddings from corrupted inputs, encouraging the model to learn robust visual representations that are less sensitive to noise. The resulting embeddings are then projected into the language model embedding space using a multi-layer perceptron (MLP), forming visual prefix tokens that provide image information to the LLM. To enable efficient adaptation without full retraining, we employ parameter-efficient fine-tuning using low-rank adaptation (LoRA). The proposed method is evaluated on the SLAKE and PathVQA benchmarks. Experimental results show improved robustness to noisy input embeddings while maintaining competitive clean performance across multiple evaluation criteria. These findings suggest that learning more robust visual representations can enhance Med-VQA performance and robustness.

---


### 46. [Less is MoE: Trimming Experts in Domain-Specialist Language Models](https://arxiv.org/abs/2606.05538)

**<font color=#1a73e8>作者：</font>** Haoze He, Xinkai Zou, Xuan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models achieve strong performance through conditional computation, but their large parameter footprint poses deployment challenges. Prior MoE compression approaches catastrophically fail when evaluated on general-purpose benchmarks beyond commonsense reasoning. We trace this failure to the granularity of compression: important capabilities are distributed across experts but concentrated in FFN sparse intermediate dimensions. To identify these dimensions, we use Fisher importance which outperforms activation-, router-score-, and magnitude-based alternatives, and identifies tiny sets of task-critical dimensions: in Qwen1.5-MoE, removing as few as 12 of 1.35M routed-FFN intermediate dimensions collapses GSM8K accuracy while largely preserving factual-knowledge performance. Building on this, we propose Fisher-MoE, which operates within FFN to remove intermediate dimensions ranked by Fisher importance. At the same 50% MoE compression ratio, Fisher-MoE preserves model capability, while reducing weight memory by ~45% and improving inference throughput by 21%. These findings suggest intermediate dimension granularity is an effective unit for both compression and ranking where capability concentrates in MoE models.

---


### 47. [AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents](https://arxiv.org/abs/2606.05557)

**<font color=#1a73e8>作者：</font>** Yang Li, Jiaxiang Liu, Jiang Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A situated query like "where is Lin Wei?" often encodes more than its literal content: the user may also want to know whether Lin Wei is free, in a good mood, or worth interrupting now. Standard tool-use agents answer the literal question and stop. AURA inserts an inference step between scene perception and tool use that produces an IntentFrame: a structured estimate of the implicit need with a scalar gap score that controls per-query probe budget and tool selection. On a 100-query four-scene implicit-intent benchmark, AURA improves implicit-need coverage over ReAct-style probing (Delta = +0.07, p < 10^-6); three of four scenes are individually significant, the gain reproduces on a second backbone, and a prompt ablation attributes the lift to gap calibration rather than answer memorisation. On factual lookup the controller trades raw accuracy for 82% fewer probes and zero forbidden-tool violations on a privacy-sensitive slice; scope conditions are detailed in Limitations. Code, simulator, and benchmark are released at this https URL.

---


### 48. [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558)

**<font color=#1a73e8>作者：</font>** Kaixuan Liu, Guojun Xiong, Weinan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating large language model (LLM) agents in multi-turn interactive environments is expensive and risky, as it requires online environment interaction. We propose ADWM (Autoregressive Diffusion World Model), an evaluation framework that estimates the performance of a new LLM agent policy purely from pre-collected trajectories. The core idea is to learn a latent diffusion world model that simulates how the environment responds to the evaluation policy, without ever executing it in the real environment. Existing diffusion-based OPE methods guide full trajectories in a single pass by jointly diffusing states and actions, an assumption that breaks down for LLM agents whose actions are discrete text that must be sampled from the policy after observing the environment. Unlike autoregressive world models that suffer from compounding errors, ADWM models each transition as an independent denoising process, enabling reliable step-by-step rollouts where the world model and agent alternate in causal order. Crucially, the LLM agent under evaluation directly guides the diffusion generation at each step via a policy-conditioned score function, ensuring that simulated trajectories accurately reflect its decision-making patterns. Empirically, ADWM achieves accurate value estimates and evaluation reliability across diverse multi-turn agent tasks, demonstrating its promise as a practical framework for offline LLM agent evaluation.

---


### 49. [SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations](https://arxiv.org/abs/2606.05563)

**<font color=#1a73e8>作者：</font>** Taewon Yun, Hyeonseong Park, Jeonghwan Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM mediators remains challenging, as mediation unfolds as a real-time trajectory shaped by disputants' shifting emotions, intentions, and context. Existing testbeds rely on a few expert-authored domains, vary mainly strategic posture, and score every turn against every topic, introducing off-topic noise. We introduce SoCRATES, a benchmark for evaluating proactive LLM mediators in realistic, multi-domain testbeds. It constructs scenarios from real conflicts through an agentic pipeline across eight domains, probes five socio-cognitive adaptation axes (strategic posture, party composition, history length, emotional reactivity, and cultural identity), and scores each topic only on the turns that advance it via a topic-localized evaluator. The evaluator reaches 0.82 alignment with human experts, more than doubling a per-turn baseline. Benchmarking eight frontier LLMs, we find that even the strongest mediator closes only about a third of the unmediated consensus gap under diverse and realistic testbeds, with performance varying sharply by socio-cognitive axis, highlighting that progress lies in social adaptation to diverse conditions.

---


### 50. [Using Large Language Models to Support High Volume Application Review for an Undergraduate Research Program](https://arxiv.org/abs/2606.05564)

**<font color=#1a73e8>作者：</font>** Varun Aggarwal, Kay Kobak, John Howarter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Undergraduate research programs such as the Summer Undergraduate Research Fellowship (SURF) at Purdue University receive thousands of applications every year, requiring significant time and effort for program staff to evaluate each submission consistently and within tight timelines. This work-in-progress paper describes the development and initial deployment of a large language model (LLM)-based tool to assist in the evaluation of approximately 1,200 student Statements of Purpose (SoPs) for the SURF 2026 cycle at Purdue University. The workflow utilizes OpenAI GPT models (GPT-4o, GPT-5-mini, and GPT-5.2) and uses a structured rubric across six subcategories, each scored on a 0-3 scale. A few SoPs, graded by program staff, were used to tune the model responses. The model prompt was designed to generate both numerical scores, rationales (including positive and negative aspects) and short excerpts from each submission. Using GPT-5.2, the full batch of 1,200 SoPs was processed in approximately 4.6 hours of compute time, averaging roughly 14 seconds per SoP (with per-SoP timing varying with SoP length, which ranged from 500 to 2,000 words). Notable differences in rubric adherence were observed across model versions, with GPT-5.2 adhering most closely. Disagreement in model scores was more pronounced for lower-scoring submissions. The LLM outputs replicated the role previously played by distributed human graders, providing the program coordinator with scored and rationale-annotated outputs for the entire applicant pool. The program coordinator then reviewed these outputs alongside each applicant's SoP, applying the same downstream office criteria used in prior SURF cycles, to produce a shortlist of strong candidates. This coordinator review was completed in approximately 4 hours, compared to the multi-week coordination effort required in prior program cycles.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-185](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
