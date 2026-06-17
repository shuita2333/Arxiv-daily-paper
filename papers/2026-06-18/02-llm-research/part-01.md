# 🧠 大模型相关研究 | 2026年06月18日

> 本类共 **133** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-133](./part-03.md)

---

### 1. [Correct When Paired, Wrong When Split: Decoupling and Editing Modality-Specific Neurons in MLLMs](https://arxiv.org/abs/2606.17057)

**<font color=#1a73e8>作者：</font>** Tingchao Fu, Wenkai Wang, Fanxiao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although Knowledge Editing provides an efficient mechanism for updating the knowledge of Multimodal Large Language Models (MLLMs), we find that current paradigms still suffer from an important yet remain underexplored issue : editing decoupling failure, where entity-related knowledge can be updated when the model is triggered by multimodal inputs (text--image query pairs), however, it often reverts to outdated pre-edit facts when the paired inputs are split into unimodal ones. Our in-depth empirical analysis reveals that the entity knowledge in MLLMs is not stored as a unified representation, but is instead distributed across disentangled modality-specific pathways. As a result, updates biased toward multimodal queries fail to propagate effectively to unimodal circuits. To bridge this gap, we propose DECODE, which explicitly disentangles and localizes modality-specific neuron groups for targeted knowledge. Extensive experiments demonstrate that DECODE consistently achieves effective knowledge updates under different modality triggers, thereby mitigating editing decoupling failures.

---


### 2. [The Critical Role of Model Selection in Causal Inference: A Comparative Analysis of Classification Models within the InferBERT Framework for Pharmacovigilance](https://arxiv.org/abs/2606.17113)

**<font color=#1a73e8>作者：</font>** Csaba Kiss, Roland Molontay, Gabriele Pergola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distinguishing causal adverse drug events (ADEs) from spurious correlations remains a central challenge in pharmacovigilance. The InferBERT framework integrates transformer models with Do-calculus, but its success hinges on the underlying classification model. This study evaluates the impact of model choice in InferBERT, assessing whether simpler models suffice, if domain-specific pre-training helps, whether scaling to LLMs improves causal detection, and the effect of post-hoc calibration. We performed a comparative study on two benchmarks: Analgesics-induced Acute Liver Failure (AILF) and Tramadol-related Mortalities (TRAM). Four models were evaluated-XGBoost (baseline), ALBERT (original InferBERT), BioBERT (biomedical transformer), and Med-LLaMA (medical LLM)-using 5-fold cross-validation repeated over 20 runs. We measured accuracy, Expected Calibration Error (ECE) pre- and post-isotonic regression, and Jaccard concordance of causal terms with PRR, ROR, and EBGM; significance was tested with paired t-tests. BioBERT achieved the highest accuracy on both datasets, while Med-LLaMA underperformed despite its size and parameter-efficient fine-tuning. Domain-specific pre-training was decisive. Calibration improved ECE but had mixed effects on accuracy and causal discovery. BioBERT's superiority also yielded the strongest concordance with traditional pharmacovigilance signals. These results show that domain-specific pre-training provides a clear advantage over simpler baselines and larger LLMs. Investing in manageable, domain-aware models is more effective for computational pharmacovigilance than simply scaling model size.

---


### 3. [Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis](https://arxiv.org/abs/2606.17115)

**<font color=#1a73e8>作者：</font>** Jingyu Hu, Giuseppe Tripodi, Reed Naidoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) have emerged as powerful representation extractors for medical data, yet their generalizability to datasets under distribution shift remains underexplored. This work systematically evaluates FM-based representations on a suite of computational pathology tasks across two real-world commercial cohorts, IH-BC and IH-NSCLC, drawn from the licensed in-house (IH) oncology dataset. The analysis focuses on two modalities, whole-slide images and transcriptomic profiles, drawn from the IH multimodal data. We first benchmark unimodal probing performance across five FMs on eight downstream classification tasks, and find that image and omics representations carry complementary predictive signals. Then we investigate whether multimodal fusion can yield additional gains over unimodal baselines by comparing three image-omics fusion strategies built on paired representations. The trustworthiness of selected unimodal and multimodal pipelines is further assessed through conformal prediction. Our results show that FM representations achieve competitive performance on out-of-distribution data and that multimodal fusion helps mainly when no single modality dominates the signal. Conformal prediction reveals that in the majority of cases where a point prediction fails, the true diagnosis remains recoverable within the prediction set, reinforcing the value of uncertainty-aware inference for clinical support.

---


### 4. [MODE: Modality-Decomposed Expert-Level Mixed-Precision Quantization for MoE Multimodal LLMs](https://arxiv.org/abs/2606.17118)

**<font color=#1a73e8>作者：</font>** Yuanteng Chen, Peisong Wang, Zhilei Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts Multimodal Large Language Models (MoE-MLLMs) offer remarkable performance but incur prohibitive GPU memory costs, making compression essential. Among PTQ methods, expert-level mixed-precision quantization has proven effective for MoE-LLMs, yet suffers notable degradation on MoE-MLLMs due to two overlooked biases in expert importance estimation. (1) At the cross-modal level, the numerical dominance of vision tokens causes expert selection frequency to be dominated by vision tokens, masking experts that are critical to the text modality; (2) at the intra-vision level, the large proportion of redundant vision tokens further skew frequency statistics, obscuring experts critical for informative visual content. To bridge gaps, we propose MODE, a modality-decomposed expert-level mixed-precision quantization framework for MoE-MLLMs that decomposes expert selection frequency by modality, filters redundant vision tokens to obtain denoised visual frequency, and further evaluates quantization sensitivity per modality as a complementary signal to frequency-based estimation. These signals are integrated into an Integer Linear Programming formulation to assign per-expert bit-widths under a given budget. Extensive experiments show that MODE is particularly well-suited for MoE-MLLMs, limiting average performance loss to within 2.9% at W3A16, with larger gains at the extreme 2-bit setting.

---


### 5. [PromptMN: Pseudo Prompting Language](https://arxiv.org/abs/2606.17164)

**<font color=#1a73e8>作者：</font>** Enkhzol Dovdon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompting has become the primary interface between humans and generative AI, yet many natural language prompts remain fragile: roles, goals, constraints, and expected outputs are often buried in prose or left implicit. In agentic and software development workflows, a misread at the first handoff can propagate through every step, since a significant portion of agent failures stem from context ambiguities rather than model limitations. This paper introduces PromptMN, a pseudo-prompting domain-specific language that annotates natural language with compact, %-prefixed typed directives covering roles, goals, requirements, priorities, constraints, plans, inputs, and outputs. Semantic resolution lets authors write in any order while the model interprets directives by function. PromptMN sits between informal prompting and programming-style pseudocode: structured enough to be inspectable and reusable, yet lightweight enough for analysts, managers, developers, and stakeholders across the software development lifecycle (SDLC). PromptMN also pairs with reverse prompt engineering. Asking a model to restate a desired outcome as PromptMN lets users inspect the inferred roles, goals, constraints, and missing assumptions before acting, reducing repair cycles and yielding a reusable artifact for aligning people and AI tools. PromptMN's feasibility is evaluated across several frontier models, including Claude Fable 5, Claude Opus 4.8, Gemini 3.1 Pro, and GPT-5.5. The models correctly resolved PromptMN instructions, including complex structures such as repetition, conditionals, methods, and a prime-checking task, without fine-tuning. The same vocabulary applies across new codebases, maintenance, and redesign in the SDLC scenarios presented. While large-scale validation remains future work, these early results suggest PromptMN is a practical step toward clearer, more reviewable human-to-AI interaction.

---


### 6. [RepSelect: Robust LLM Unlearning via Representation Selectivity](https://arxiv.org/abs/2606.17168)

**<font color=#1a73e8>作者：</font>** Filip Sondej, Yushi Yang, Adam Mahdi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Making large language models (LLMs) deeply forget specific knowledge and values without sacrificing general capabilities remains a central challenge in unlearning. However, current methods are easily reversed by fine-tuning or few-shot prompting, suggesting their forgetting is only shallow. We identify the root cause. Existing methods target representations shared with both the retain set and the subspace recovered by a fine-tuning attacker, making unlearning both disruptive to general capabilities and easy to reverse. We propose RepSelect (Representation Selectivity), isolates forget-set-specific representations by collapsing top principal components of weight gradients before each update, leaving general capabilities intact while limiting what fine-tuning can recover. We evaluate across two forget categories, biohazardous knowledge and abusive tendencies, and four model families spanning dense and Mixture-of-Experts architectures (Llama 3, Qwen 3.5, Gemma 4 E4B, DeepSeek V2 Lite). Compared to five popular baselines (GradDiff, NPO, SimNPO, RMU, UNDIAL), RepSelect achieves a 4-50x larger reduction in post-relearning answer accuracy than the strongest baseline, and is near-perfectly robust to few-shot prompting attacks. Targeting selective representations is thus an important step towards deep and robust LLM forgetting.

---


### 7. [Self-Generated Error Training for Token Editing in Diffusion Language Models](https://arxiv.org/abs/2606.17175)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-to-token (T2T) editing lets LLaDA2.1 revise committed tokens during block-diffusion decoding. The released recipe trains this editor on random vocabulary corruptions, but at inference the editor sees the model's own fluent, high-confidence draft errors instead. We study this training-inference mismatch and propose self-generated T2T, which performs a no-gradient draft pass, fills masked positions with predicted tokens, and supervises recovery in a second pass under these self-generated corruptions. We implement the update as a short LoRA continued-pretraining pass on LLaDA2.1-mini and evaluate on several benchmarks under the official Q-Mode T2T procedure with unchanged inference parameters. The method generally improves accuracy while reducing T2T edit intensity, mitigating failure modes such as final-digit transcription errors after otherwise correct reasoning and excessive self-correction before short factual answers.

---


### 8. [Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems](https://arxiv.org/abs/2606.17182)

**<font color=#1a73e8>作者：</font>** Sajjad Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems share state through memory stores, vector indices, and tool registries. We model such sharing as long-running read-generate-write operations under deterministic-generation semantics -- the regime durable-execution engines enforce by deterministic replay -- and formalize four concurrency anomalies in TLA+: stale-generation, phantom-tool, causal-cascade, and tool-effect reordering, structural analogues of classical isolation anomalies, each with a TLC counter-example. The exclusion lattice over these anomalies is trivial; the contribution is the mechanically verified realizability and strict separation of one maximal chain within it, $L_0 \subsetneq \cdots \subsetneq L_4$, to our knowledge the first machine-checked consistency hierarchy for such runtimes. A development of 274 Verus obligations (zero assume, zero admit; trust base: two structural axioms and a mutex correspondence) proves the detectors sound and complete against the specifications and each runtime its avoidance set. Three deployed Rust runtimes realize L0-L1 (pessimistic locking, serializable snapshot isolation, default-SI), each verified against stale-generation and refined to its state machine; L2-L4 are exec-mode-verified with dependency-free prevention twins (A3, A6, A2: 0/1000 versus 1000/1000), and L2 is run live across three model families (A3 prevented in all 120 retracted sessions). We reproduce a silent lost update in ByteDance's deer-flow, formalizing its fix as a verified $L_0 \to L_1$ refinement, and exhibit tool-effect reordering in LangGraph's ToolNode on unmodified output, removed by an L3 commit-order sequencer. The verified detector, refinements, and realizability artifacts are the contribution; the phenomena and lattice are classical.

---


### 9. [PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation](https://arxiv.org/abs/2606.17199)

**<font color=#1a73e8>作者：</font>** Anhao Zhao, Junlong Tong, Yingqi Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard on-policy distillation (OPD) for large language models estimates the reverse-KL objective using student-sampled tokens, yielding an unbiased single-sample Monte Carlo estimator that avoids vocabulary-wide computation. However, we show that this estimator suffers from severe training pathologies in practice: sample inefficiency, unstable generation dynamics, and a substantial performance gap compared to exact full-vocabulary OPD. Reward-level diagnosis traces these pathologies to the log-ratio reward, which is unbounded by construction, producing extremely high-variance gradients concentrated at early positions and persisting throughout training; standard post-hoc scaling fail as they operate only after this distortion occurs. To solve this problem, we propose PowerOPD: a family of natively bounded, sign-consistent rewards from the Box-Cox power transformation, parameterized by alpha > 0, of which the log-ratio is the degenerate alpha -> 0 limit. Across six mathematical reasoning benchmarks and four Qwen3 teacher-student pairs, PowerOPD achieves benchmark-averaged Avg@8/Pass@8 gains of up to +6.37/+5.71 over vanilla OPD, +3.01/+3.54 over post-hoc stabilization, and +2.59/+8.90 over full-vocabulary OPD, while reducing wall-clock time by 59.2% and peak GPU memory by 23.1%. Larger alpha generally improves accuracy, consistently shortens responses, and keeps gradient norms more than 3,000x smaller than vanilla OPD.

---


### 10. [Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search](https://arxiv.org/abs/2606.17209)

**<font color=#1a73e8>作者：</font>** Sidhaarth Murali, João Coelho, Jingjie Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling for agentic search typically increases depth (i.e., more turns and tokens per trajectory) or breadth (i.e., more parallel rollouts). Here we focus on breadth scaling, showing that standard parallel sampling yields diminishing returns, tracing this to query redundancy at the first turn. When models issue similar first queries across rollouts, the threads retrieve overlapping evidence, and subsequent turns are conditioned on this shared retrieval. We address this limitation with DivInit, a training-free intervention at the first turn. Rather than sampling k independent first queries, DivInit draws n candidates from a single call, picks k < n diverse seeds, and runs them as parallel trajectories. Across five open-weight models and eight benchmarks, DivInit consistently improves over standard parallel sampling, with average gains of five to seven points on multi-hop QA at matched compute. Code available at this https URL

---


### 11. [Revisiting LLM Adaptation for 3D CT Report Generation: A Study of Scaling and Diagnostic Priors](https://arxiv.org/abs/2606.17213)

**<font color=#1a73e8>作者：</font>** Vanshali Sharma, Andrea M. Bejar, Halil Ertugrul Aktas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal learning, including large language models (LLMs) and vision-language models (VLMs), have demonstrated strong adaptability to natural images. However, extending their use to the medical domain, particularly for volumetric (3D) images, is challenging due to high computational complexity, volumetric dependencies and the semantic gap between visual features and clinical terminology. Naively fine-tuning LLMs on limited medical data often leads to overfitting and clinical hallucination, where linguistic fluency is prioritized over clinical factuality. In this study, we investigate parameter-efficient adaptation strategies for volumetric CT report generation and introduce RAD3D-Prefix, a lightweight diagnostic-prior conditioning framework that minimizes the need for extensive parameter training. This module integrates image embeddings with multi-label diagnostic classification logits, preserving critical clinical details while bridging the semantic gap. By keeping the LLM frozen, our method requires minimal trainable parameters and mitigates the risk of overfitting on small, domain-specific datasets. Through a systematic study spanning LLMs from 96.1M to 1.6B parameters, we find that fine-tuning is most beneficial for smaller LLMs, whereas freezing larger (~1B+ LLMs and training only lightweight projection layers provides a superior trade-off between performance, generalization, and computational efficiency. Across multiple automatic metrics and a clinical reader study, RAD3D-Prefix outperforms comparable parameter-efficient baselines and demonstrates strong out-of-domain generalization while using substantially fewer trainable parameters than fully fine-tuned alternatives.

---


### 12. [Rift: A Conflict Signature for Deception in Language Models](https://arxiv.org/abs/2606.17229)

**<font color=#1a73e8>作者：</font>** Petr Nyoma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A model that lies while knowing the truth is the central case ELK cannot handle with behavioral evaluation alone. We ask whether such deception leaves an internal signature distinguishing it from honest error. Our key move is a control for wrongness: we contrast a sleeper agent (knows the truth, lies on trigger) against a naive liar (fine-tuned to emit the same wrong answers with no honest training). Both produce identical wrong outputs; any difference is about knowledge conflict, not incorrectness. We find deceptive forward passes carry a conflict signature - 2.1-2.3x higher residual rank than naive-liar passes on the same wrong answer - strong enough to identify which of two responses is the lie with 100% accuracy and no labels, across GPT-2 small/medium (three seeds) and three instruct models. Across Qwen2.5-1.5B/7B and Phi-3-mini, instructed deception raises residual rank on every tested fact (18/18, 40/40, 34/34); on Phi-3, lies separate perfectly from both honest answers and hallucinations (AUC 1.0, Wilcoxon p~6e-11). The signature survives strategic self-constructed deception (model invents its own lie, AUC 1.0), active concealment attempts (AUC 1.0), and length-controlled replication (20/20, AUC 1.0, p~1e-6). Using basis-free relative representations, a probe trained on one model family detects deception in two other families zero-shot (mean AUC 0.933), surviving simultaneous architecture and format change (AUC 0.821), and transfers across five languages (AUC 1.000, length-controlled). The signature is read-only: detectable but not injectable (0/8 both directions). Honest limitations and six negative experiments are documented in full.

---


### 13. [Speaking in Self-Assessing Tongues: On the Verbalized Confidence of LLMs in Machine Translation](https://arxiv.org/abs/2606.17234)

**<font color=#1a73e8>作者：</font>** Ali Marashian, Alexis Palmer, Katharina von der Wense  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid rise in popularity of large language models (LLMs) for translation calls for a thorough study of the reliability of their confidence in their own outputs. Unlike many generation tasks, translation errors and confidence levels can be useful at different levels of granularity (tokens, words, or spans). Unsupervised approaches based on internal signals like predicted probabilities can be misleading because they reflect certainty among alternatives rather than correctness. In addition, they require access to such internal signals. Here, we devise five verbalized methods of extracting an LLM's per-token confidence without those shortcomings and compare their reliability with that of the model's internal signals of certainty. We evaluate reliability using two forms of alignment: fine-grained error detection and calibration. For both, internal and verbalized methods perform similarly, although results vary by model. Interestingly, we find little to no correlation between internal and verbalized methods.

---


### 14. [GeoDisaster: Benchmarking Orchestrated Agents for Operational Disaster Geo-Intelligence](https://arxiv.org/abs/2606.17246)

**<font color=#1a73e8>作者：</font>** Maram Hasan, Aman Verma, Savitra Roy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote-sensing vision-language models (RS-VLMs) have advanced Earth-observation analysis toward visual interpretation and instruction-following, yet fall short of operational geo-intelligence, which demands tool-grounded spatial reasoning and structured, evidence-backed decisions. We introduce GeoDisaster, an operational geospatial disaster reasoning benchmark with 2,921 verified instances across 43 question types and five task families: deforestation monitoring, multi-hazard analysis, building-damage assessment, flood-safe routing, and Sentinel-1 SAR flood monitoring. Instances integrate heterogeneous EO/GIS evidence-optical and SAR imagery, raster masks, vector geometries, road networks, and exposure layers-spanning hazard detection, damage assessment, exposure estimation, and diagnostic report generation. Ground-truth answers are grounded in executable geospatial workflows and deterministic consistency checks, removing the need for language-model annotation. We further propose an orchestrated multi-agent framework with 18 disaster-oriented tools, where role-specialized agents coordinate through explicit execution contracts, aligned via Role-Contract Expectation Alignment (RCEA): failure-aware supervised fine-tuning combined with contract-grounded reinforcement learning over dense step-level signals. Experiments show that GeoDisaster challenges existing RS-VLMs and agentic systems, while RCEA improves tool use, evidence grounding, state consistency, and decision generation.

---


### 15. [Rethinking Groups in Critic-Free RLVR](https://arxiv.org/abs/2606.17250)

**<font color=#1a73e8>作者：</font>** Yihong Wu, Liheng Ma, Lingfeng Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a central paradigm for post-training large language models. Existing critic-free RL methods typically generate a group of rollouts for the same question to estimate value baselines for advantage computation. However, this design suffers from data inefficiency, group synchronization barriers, and inflexibility with structured rollouts. In this work, we revisit the role of the ``group'' and show that its underlying function is not merely to estimate baselines but to prevent false penalties on negative samples. Building on this insight, we propose negative token filtering, a simple and effective strategy that enables stable single-rollout training. We apply it to two batch-level advantage methods, achieving comparable performance on reasoning tasks and stronger performance on agentic tasks relative to group-based RL techniques.

---


### 16. [Pulling The REINS: Training-Free Safety Alignment of Video Diffusion Models via Representation Steering](https://arxiv.org/abs/2606.17257)

**<font color=#1a73e8>作者：</font>** Rohit Kundu, Arindam Dutta, Sarosij Bose 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-weight video diffusion models can generate photorealistic unsafe content, from violence to misinformation, yet existing defenses either require expensive safety fine-tuning that degrades general capability, or apply external filters that are trivially bypassed by adversarial prompts. We present REINS (REpresentation-space INference-time Safety steering), a training-free method that aligns video diffusion models at inference time by steering their internal representations toward safe generation. Our key finding is that safety-relevant structure is linearly encoded in the hidden-state activations of video diffusion transformers, and a single direction, discovered via Supervised PCA on binary safety labels, suffices to separate safe from unsafe generation trajectories. At inference, adding this direction to hidden states at an intermediate transformer layer redirects generation from harmful content to semantically related safe alternatives, with no weight updates, no concept enumeration, and negligible computational overhead. Through mechanistic analysis, we reveal that while safety information accumulates monotonically with transformer depth, steering effectiveness peaks at intermediate layers (~50% depth), exposing a fundamental tradeoff between information availability and downstream propagation capacity. We evaluate REINS across 9 video diffusion models, multiple parameter scales (1.3B-5B), and both text-to-video and image-to-video generation, to our knowledge, the broadest safety evaluation suite in the video generation literature.

---


### 17. [Training LLMs with Reinforcement Learning over Digital Twin Representations for Reasoning-Intensive Surgical VideoQA](https://arxiv.org/abs/2606.17279)

**<font color=#1a73e8>作者：</font>** Yiqing Shen, Han Zhang, Mathias Unberath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video question answering requires multi-step reasoning across semantic, spatial, and temporal dimensions. Existing methods architecturally compress videos into discrete token representations and couple visual perception with reasoning. This approach fragments continuous spatial-temporal relationships and has been shown to restrict multi-step reasoning capabilities. We introduce a reinforcement learning (RL) framework that trains large language models (LLMs) to decouple perception from reasoning by operating over digital twin representations constructed from surgical foundation models. Additionally, we introduce hierarchical representations across frame, temporal window, and procedure levels with probabilistic uncertainty estimates. Finally, we propose a novel reward that combines format validation with accuracy assessment through clinical plausibility evaluation and uncertainty-aware calibration for training. To demonstrate the capabilities of this approach, we introduce REAL-Colon-Reason, a colonoscopic benchmark with 2000 question-answer pairs across three complexity levels. We achieve state-of-the-art performance on REAL-Colon-Reason and two existing surgical VideoQA benchmarks REAL-Colon-VQA and EndoVis18-VQA.

---


### 18. [Are you speaking my languages? On spoken language adherence in multimodal LLMs](https://arxiv.org/abs/2606.17281)

**<font color=#1a73e8>作者：</font>** Hyungwon Kim, Kandarp Joshi, Lillian Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Model (LLM) based Automatic Speech Recognition (ASR) enables seamless multilingual use, models often misidentify the output language, compromising transcription fidelity and downstream application quality. To preserve flexibility and code-switching capabilities, we propose a soft prompting approach that hints at potential spoken languages without strictly constraining the output. We formally define this challenge as a lack of language adherence, introduce a novel metric to quantify violations, and evaluate three mitigation strategies: (1) zero-shot prompting for robust guidance under uncertainty, (2) supervised fine-tuning (SFT) to improve prompt adherence, and (3) Chain-of-Thought (CoT) reasoning to enforce adherence during decoding. We present a comparative analysis of these methods across multiple languages, evaluating effectiveness in reducing the language violation while maintaining overall ASR performance. Finally, we discuss trade-offs to guide strategy selection under various compute constraints.

---


### 19. [Nothing from Something: Can a Language Model Discover 0?](https://arxiv.org/abs/2606.17289)

**<font color=#1a73e8>作者：</font>** Phoebe Zeng, Thomas L. Griffiths, Brenden M. Lake  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems based on artificial neural networks are being developed with aspirations of pushing the boundary of human mathematical knowledge. A key question for these systems is how much they can reach beyond their training data. Mathematical discovery requires a strong form of out of distribution generalization; the ability to hypothesize genuinely new - and potentially logically more powerful - mathematical structures. It has been hypothesized that language abilities support such generalizations in human cognition. In this work, we use simple arithmetic as a case study for examining how modern AI models could expand their mathematical horizons, evaluating whether these models can independently discover the concept of "zero". We show that We show that (1) language models of a GPT-2 size are unable to perform this generalization at test time regardless of language pretraining, but (2) models can improve substantially after training on tens or hundreds of examples of zero. Additionally, we find that language pretraining reduces the number of required examples by approximately $50\%$, showing that language abilities can scaffold mathematical discovery in neural models.

---


### 20. [Pareto LoRA: Mitigating Modality Imbalance in Unified Multimodal Models via Pareto-Optimal Gradient Integration](https://arxiv.org/abs/2606.17296)

**<font color=#1a73e8>作者：</font>** Xiwen Wei, Mark Nutter, Madhusudhanan Srinivasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) have recently emerged as a promising paradigm for integrating multimodal understanding and generation within a single autoregressive transformer. However, during multimodal instruction tuning, these models often exhibit pronounced modality imbalance: language gradients dominate optimization, thus leading to lower image generation quality, especially under parameter-efficient fine-tuning such as LoRA. In this work, we systematically analyze modality imbalance in LoRA-based fine-tuning of UMMs for interleaved text-image generation. We show that vision modality performance degrades substantially more than text modality performance when compared to unimodal counterparts, and that modality-specific gradients can differ by orders of magnitude across various tasks and layers. Motivated by this observation, we reformulate the multimodal instruction tuning as a bi-objective optimization problem and propose Pareto LoRA, a Pareto-optimal gradient integration strategy that balances the text and image objectives by modulating the gradient direction and strength. Experiments on the CoMM benchmark with Emu2 demonstrate that Pareto LoRA consistently improves multimodal generation balance, achieving up to 44.9% gains in perceptual image quality over vanilla LoRA while maintaining comparable text performance.

---


### 21. [Quantifying Consistency in LLM Logical Reasoning via Structural Uncertainty](https://arxiv.org/abs/2606.17312)

**<font color=#1a73e8>作者：</font>** Baishali Chaudhury, Mengdie Flora Wang, Hyunji Hayley Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can arrive at the same answer through reasoning paths that are unstable, contradictory, or difficult to rank consistently -- a failure mode especially prevalent in multi-step deductive reasoning. Existing methods assess reliability primarily through output dispersion -- measuring how much sampled answers differ -- but this discards a complementary signal: whether the model can consistently rank competing reasoning candidates. We propose structural uncertainty, a consistency-aware framework derived from the stability of self-preference-induced rankings over sampled reasoning solutions. Given a query, we generate multiple candidate solutions and ask the model to judge pairwise preferences among its own outputs. We aggregate self-preferences into ranking distributions via Bradley-Terry modeling with PageRank, and decompose the signal into two entropy-based components: across-trial ranking instability and within-trial candidate ambiguity. Across five LLMs and eight benchmarks, structural signals provide information complementary to answer dispersion: on logical and mathematical reasoning tasks, the combination improves identification of unreliable instances, while on factual retrieval the structural signal collapses toward uniformity, diagnosing a regime boundary where reasoning-level consistency evaluation is uninformative. The two components relate differently to accuracy: within-trial ambiguity correlates positively with correctness -- consistent with settings where multiple plausible solution paths remain competitive -- while across-trial instability correlates negatively, signaling unreliable reasoning. Structural uncertainty is best understood not as a universal confidence estimator, but as a regime-sensitive evaluator of logical reasoning consistency.

---


### 22. [ProCUA-SFT Technical Report](https://arxiv.org/abs/2606.17321)

**<font color=#1a73e8>作者：</font>** Jaehun Jung, Ximing Lu, Brandon Cui 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training computer-use agents (CUAs) -- models that interact with graphical desktops through screenshots and keyboard/mouse actions -- requires large-scale, diverse trajectory data collected in full desktop environments. The largest public resource, AgentNet (22.5K human trajectories), leads to negative transfer when used for supervised fine-tuning (SFT): continuing training UI-TARS 7B on AgentNet causes OSWorld success rate to fall from 26.3% to 8-10%. We present ProCUA-SFT, a dataset of 3.1M step-level SFT samples distilled from 93K synthetic trajectories across 2,484 application combinations. The dataset is produced by a fully automated pipeline that (i) synthesizes grounded tasks on live desktops seeded with real-world content -- 912 spreadsheets from SpreadsheetBench, approximately 10K permissively-licensed presentations from Zenodo10K, and multi-application OSWorld configs -- and (ii) verifies each task's feasibility through binary precondition checking before rollout. A single VLM (Kimi-K2.5) serves as goal generator, precondition judge, and trajectory executor, eliminating planner-actor capability gaps. Each trajectory is expanded into step-prefix samples that exactly reproduce the context layout seen at inference time. Fine-tuning UI-TARS 7B on ProCUA-SFT for one epoch yields 45.0% on OSWorld -- an 18.7 percentage-point improvement over the base model and over 35% above AgentNet-trained counterparts. A subset of ProCUA was incorporated into the training data for the Nemotron 3 Nano Omni model, contributing to its computer-use capabilities.

---


### 23. [Geometry-Consistent Endoscopic Representations for Image-Guided Navigation via Structured Foundation Model Adaptation](https://arxiv.org/abs/2606.17340)

**<font color=#1a73e8>作者：</font>** Hongchao Shu, Roger D. Soberanis-Mukul, Hao Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate vision-based navigation in monocular endoscopy is difficult due to limited depth cues, weak tissue texture, non-rigid deformation, and substantial appearance variation across domains, all of which complicate pose estimation, depth prediction, and image-to-anatomy alignment. Although recent vision foundation models have shown promise, their learned representations often remain insufficiently geometry-consistent, hindering stable feature correspondence and limiting their reliability for downstream navigation tasks. We propose a unified framework for learning geometry-consistent and domain-robust image representations for monocular endoscopy. The framework combines a synthetic data pipeline that provides accurate geometric supervision with Hierarchy-Aware Geometry-Semantic Adaptation, a structured alternative to standard LoRA that inserts low-rank adapters selectively across the transformer hierarchy and couples them with layer-wise training objectives to encourage geometric correspondence in intermediate features and semantic consistency in deeper features. Experiments on public and proprietary datasets show improved geometric and semantic representation quality, leading to better performance on downstream navigation tasks including pose estimation and monocular depth estimation. The learned representations show favorable synthetic-to-real transfer on clinical bronchoscopy and provide a useful initialization for adaptation to sinus endoscopy and colonoscopy under limited supervision. The framework also shows favorable scaling with model size and training data. These results support hierarchy-aware, geometry-guided adaptation as a practical approach for endoscopic representation learning.

---


### 24. [Do Large Language Models Always Tell The Same Stories?](https://arxiv.org/abs/2606.17350)

**<font color=#1a73e8>作者：</font>** Thennal DK, Hans Ole Hatzel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled the generation of high-quality prose, yet the question of whether these models are capable of generating diverse outputs remains contested. In this work, we investigate the diversity of LLM-generated stories through the framework of narrative similarity. Using a contrastive framework and a dataset of human-written stories and prompts from r/WritingPrompts, we collect narrative similarity judgments across 10 representative LLMs, utilizing both human evaluations and three different automatic annotation methods. Our findings reveal a consistent trend: LLM-generated narratives are consistently more similar to each other than human-written stories are. We demonstrate that frontier models in particular converge on a ``mean'' generic narrative that approximates individual human stories but lacks the collective diversity of human authors. Finally, we show that common mitigation strategies, including negative prompting and temperature scaling, fail to meaningfully address this homogeneity.

---


### 25. [DriveJudge: Rethinking Autonomous Driving Evaluation with Vision-Language Models](https://arxiv.org/abs/2606.17362)

**<font color=#1a73e8>作者：</font>** Xinglong Sun, Kevin Xie, Jenny Schmalfuss 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving has shifted towards end-to-end policy learning, where reliable, interpretable policy evaluation is a fundamental challenge as driving quality is highly context-dependent. Commonly used rule-based driving metrics like EPDMS are interpretable but lack context-awareness, while recent VLMbased evaluations are context-aware but limited by ambiguous VLM outputs and weak physical grounding. To evaluate driving in a manner that is both interpretable and context-aware, we introduce DriveJudge. DriveJudge is a driving evaluation agent that combines rule-grounded evaluation with Vision-Language Model (VLM) reasoning and selectively invokes physically-grounded deterministic rule functions after interpreting the environmental context. To train and evaluate DriveJudge, we curate a large-scale dataset of 33,577 challenging driving samples with human annotations on whether the driving behavior is reasonable in the given scenario. With this dataset, we address the underexplored problem of driving metric evaluation, and introduce two human-aligned benchmark tasks: Driving Quality Classification and Trajectory Preference Selection. DriveJudge outperforms EPDMS for driving quality classification by 21.23 AUC, and the recent VLM-based DriveCritic for trajectory preference selection by 6.5%, setting a new standard for interpretable and precise driving evaluation.

---


### 26. [Implicit vs. Explicit Prompting Strategies for LVLMs in Referential Communication](https://arxiv.org/abs/2606.17372)

**<font color=#1a73e8>作者：</font>** Peter Zeng, Amie J. Paige, Weiling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Two recent studies (Jones et al. (2026); Zeng et al. (2026)) reach apparently contradictory conclusions about whether LVLMs can coordinate on efficient referring expressions. We control for task differences between the studies while directly comparing their prompting styles. We replicate the finding that models can coordinate efficient referring expressions when explicitly prompted to do so, suggesting that other task differences are not responsible for divergent results. However, we also find that the same models fail to infer the need for communicative efficiency from a more implicit prompt, highlighting critical differences between how humans and AI systems communicate.

---


### 27. [Visuals Lie, Consistency Speaks: Disentangling Spatial Attention from Reliability in Vision-Language Models](https://arxiv.org/abs/2606.17389)

**<font color=#1a73e8>作者：</font>** Logan Mann, Yi Xia, Ajit Saravanan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Foundation Models are increasingly used as reasoning agents, making reliability, knowing when a model may hallucinate, critical. A common intuition, which we call the Attention-Confidence Assumption, holds that reliability follows from "structural" visual perception: tight attention on relevant regions should signal a trustworthy answer, while scattered attention signals confusion. We challenge this through the VLM Reliability Probe (VRP), a systematic cross-family study of reliability signals in contemporary Vision-Language Models (VLMs). We introduce structural-attention metrics, cluster counts (C_k) and spatial entropy (H_s), to quantify the visual encoder's gaze, and track its evolution (Delta H_s) across layers. This reveals a "Symbolic Detachment": models often "Early Lock" visual features only to diffuse attention later, severing early perception from final generation. Contrary to the grounding hypothesis, we find a "Cluster Failure": spatial attention has near-zero correlation (R approx 0.001) with accuracy. Instead, reliability is a phenomenon of generation dynamics and internal-state distributions. Self-Consistency, the agreement rate across sampled reasoning paths, is the dominant predictor of truth (R = 0.429). Scaling causal interventions exposes a sharp architectural divergence: LLaVA locks its prediction in a fragile late-stage bottleneck, whereas PaliGemma and Qwen2-VL distribute reliability globally, staying resilient even when ~50% or more of their most predictive layer is destroyed. For current VLMs, reliability signals are detached from visual grounding maps and are best inferred from generation-time dynamics and hidden-state probes.

---


### 28. [NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama](https://arxiv.org/abs/2606.17391)

**<font color=#1a73e8>作者：</font>** Logan Mann, Abdur Rahman, Mohammad Saifullah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open benchmark of nine narrative-structure metrics evaluated across horizons h in {10, 20, 50, 100, 200}, with cross-lingual evaluation across four Indic languages (Hindi, Tamil, Telugu, Marathi). We introduce N-VSSM, a Narrative Variational State-Space Model that maintains a structured 256-dimensional latent world state over more than 200 episodes via a Mamba-2 backbone with an event-conditioned posterior and an 8B decoder. N-VSSM holds plot-beat F1 >= 0.84 across all horizons at 4x lower compute than the closed-frontier band. A learned Cultural Transfer Function lifts cross-language fidelity by +0.20 to +0.23 Likert points. In a within-subjects writer study (n = 12 professional authors, 240 trials), N-VSSM is preferred over Claude Opus 4.5 on long-arc consistency 71% of the time and rated +1.3 Likert points higher on controllability.

---


### 29. [Attention Alignment Between Humans and Vision-Language Models](https://arxiv.org/abs/2606.17410)

**<font color=#1a73e8>作者：</font>** Isaac R. Christian, Udith Haputhanthrige, Hanna Hornfeld 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception depends on top-down goals and bottom-up sensory mechanisms. Vision-language models implement both, allowing us to treat each component as a separable hypothesis about what drives where we look. We compared spatial attention maps from six vision-language models against human fixation heatmaps recorded on 200 images during two tasks (general description and social captioning). The six models spanned a 2$\times$2 factorial of CNN vs.\ ViT encoders crossed with LSTM vs.\ Transformer decoders, plus Molmo 7B-D and Qwen3.5 9B. We found that both decoder and encoder architecture shaped alignment, but decoder choice dominated. LSTM vs.\ Transformer decoders increased alignment by 40--50 percentage points (80--87\% vs.\ 40--59\% of the human noise ceiling). In contrast, CNN vs.\ ViT encoders contributed a secondary 5--20 point advantage depending on decoder family, with CNN-LSTM the most aligned model overall (85--87\%). Despite their alignment advantage, LSTM-decoder attention maps were spatially diffuse and minimally task-differentiated; ViT-Transformer, the weakest in alignment, showed the sharpest spatial concentration and strongest task differentiation. A hemispatial-neglect simulation confirmed that ablating attention impacted LSTM decoders more than Transformer decoders. In an exploratory extension using TRIBE-simulated synthetic neural responses, fixation alignment and neural relevance dissociate: CNN-Transformer attention maps better predicted synthetic brain activity despite lower fixation alignment, with attention maps best predicting early visual cortex. Together, top-down and bottom-up components trade off what they predict in behavioral and synthetic neural data.

---


### 30. [CIAN: Multi-Stage Framework for Event-Enriched Image Captioning via Retrieval-Augmented Generation](https://arxiv.org/abs/2606.17430)

**<font color=#1a73e8>作者：</font>** Trinh Thi Thu Hien, Trung-Nghia Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-enriched image captioning describes not only visible content but also the broader context of events, including timing, location, and participants, capabilities missing in most pixel-bound models. We propose the Contextual Image-Article Narrator (CIAN), a multi-stage framework that enriches captions with external narratives. CIAN retrieves relevant articles using SigLIP, summarizes them to guide a Narrative Generation stage with a LoRA-fine-tuned Qwen model, and applies N-Gram-based Refinement for fluency and coherence. On the OpenEvents-V1 benchmark, CIAN achieves high retrieval performance (mAP 0.979) and improves caption quality, increasing CIDEr from 0.030 to 0.094. These results highlight the effectiveness of retrieval-augmented reasoning combined with linguistic refinement for generating context-aware, human-like captions.

---


### 31. [LADBench: A Benchmark for Logical Fault Detection in Images](https://arxiv.org/abs/2606.17433)

**<font color=#1a73e8>作者：</font>** Sahasra Kondapalli, Lara Radovanovic, Aadi Palnitkar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision Language Models (VLMs) excel at visual question answering and semantic grounding, but their capacity for autonomous logical reasoning remains underexplored. Existing anomaly benchmarks emphasize visual errors or direct prompting rather than the physical and social common sense needed for open-world deployment. To address this, we introduce LAD-bench, a benchmark of more than 1,000 curated synthetic images with logical anomalies across four domains: Residential, Urban, Collaborative, and Nature. We further propose a Tiered Prompting Protocol based on progressive disclosure, which measures how much explicit assistance a model needs to localize and reason about a logical fault. Evaluating leading foundation models reveals substantial weaknesses: even the best achieves only 70.11% overall accuracy, showing that implicit logical fault detection remains unsolved. Crucially, models often fail to identify anomalies even after receiving explicit hints in deeper tiers. By surfacing these limitations in sequential multimodal reasoning, LAD-Bench offers a rigorous framework for advancing the safety, reliability, and cognitive alignment of autonomous visual systems. Dataset and Code: this https URL

---


### 32. [UoU: A Universal Fingerprint Foundation Model Based on Large-Scale Unsupervised Learning](https://arxiv.org/abs/2606.17436)

**<font color=#1a73e8>作者：</font>** Xiongjun Guan, Jianjiang Feng, Jie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fingerprint recognition is still dominated by task-specific pipelines, where enhancement, structural parsing, alignment, and matching are optimized in isolation. Although effective in narrow settings, this design limits representation reuse across sensors, qualities, and downstream applications. We therefore present UoU, short for ``a \textbf{U}niversal fingerprint foundation model based \textbf{o}n large-scale \textbf{U}nsupervised learning,'' which reframes fingerprint feature extraction as a domain-specific foundation-model problem. UoU is organized around a multi-level representation hierarchy spanning image restoration, structural fields, semantic tokens, point-level biometric entities, and compact global descriptors. Its training recipe combines a supervised cold start on precise annotations, large-scale weakly supervised refinement, and large-scale unsupervised consolidation, with the latter two stages iterated during large-scale training so that weak supervision broadens semantic coverage while unsupervised learning stabilizes correspondences, invariances, and representation geometry. Rather than treating fingerprint imagery as generic texture, UoU exploits domain-specific symmetries and intermediate structure, including orientation flow, periodic ridge patterns, sparse biometric entities, and spatial equivariance. The framework is intentionally architecture-agnostic: while the present study includes an initial transformer-based structured-prediction instantiation, the broader design supports multi-task learning, scalable model configurations, and downstream specialization for matching, alignment, enhancement, registration, and related fingerprint applications. This paper presents the technical motivation, system design, and validation protocol of UoU, and part of the baseline implementation is publicly available at this https URL.

---


### 33. [Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems](https://arxiv.org/abs/2606.17443)

**<font color=#1a73e8>作者：</font>** Xi Chu, Yupeng Hou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming a major way for consumers to find products, but we do not yet understand how brands compete in this new channel. We study brand dynamics in LLM recommendations using skincare products -- a category where consumers cannot easily judge quality before buying and must rely on brand reputation -- across three commercial LLMs (GPT-4o-mini, Claude Sonnet, Gemini 3 Flash), with a robustness check on search goods. In three experiments, we find: (1) a Conditional Monopoly where well-known brands get recommended 100% of the time (IAI = 10.0) when all products have the same specifications, but this dominance disappears with less than a +0.1-star rating advantage for a competitor; (2) authority-style marketing language, including fabricated clinical-evidence claims, breaks this monopoly at a Bias Surplus Value equal to +0.17 rating points, with each model responding differently; and (3) a social dilemma in multi-brand GEO competition: when all brands adopt the same optimization strategy, individual payoff falls from +0.802 to +0.007 in our payoff proxy, and non-participating brands receive zero recommendations in our tests. Our results suggest that generative engine optimization (GEO) should be studied not only as a security risk, but also as an emerging marketing practice that shapes market competition.

---


### 34. [MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented Generation Evaluation](https://arxiv.org/abs/2606.17449)

**<font color=#1a73e8>作者：</font>** Zehang Wei, Jiaxin Dai, Jiamin Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Multimodal Retrieval-Augmented Generation (M-RAG) enhances Large Vision-Language Models, it remains highly susceptible to cross-modal hallucinations, causal fabrications, and sycophancy. Furthermore, existing mitigation pipelines often face an intervention paradox: static rules tend to unnecessarily disrupt accurate generations, whereas leaving the multi-modal reasoning completely unguided allows existing mismatches to cascade into severe logical fabrications. To quantify and mitigate these hallucinations, we propose a Multi-Agent system, MODE-RAG, driven by Variational Free Energy (VFE) and internal attention states to dynamically gate interventions. High-risk queries are routed to five stage-specific agents, integrating Monte Carlo Tree Search (MCTS) for rigorous causal derivation and logit perturbations to penalize sycophancy. Dedicated Correction and Overseer agents ensure formatting stability and perform post-hoc factual verification. To objectively evaluate our approach, we introduce ModeVent, a challenging subset derived from the MultiVent dataset. Extensive experiments indicate that our system effectively reduces hallucination rates and logical fabrication, significantly improving the robustness of M-RAG systems.

---


### 35. [Dissecting model behavior through agent trajectories](https://arxiv.org/abs/2606.17454)

**<font color=#1a73e8>作者：</font>** Gaurav Gupta, Vatshank Chaturvedi, Jun Huan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent performance is not just a modeling problem, it is fundamentally a systems problem. The advanced capabilities of models are realized through agent harnesses. Therefore, a gap between model assumptions and harness behavior can easily prevent the model's full capabilities from translating into agent performance. We formalize this as the `intent-execution' gap: the mismatch between what the model intends and what the harness executes, and vice versa. We argue that minimizing this intent-execution gap is as important as other aspects of harness design such as tools and execution loops. To illustrate the impact of this harness-model alignment, we develop a simple and customizable harness called `Simple Strands Agent' (SSA). SSA aims to find the bulk of common patterns which generalize across different model families (such as Claude, Gemini, GPT, Grok, Qwen), as well as a small number of model-specific preferences. We make two contributions: (i) we $\textbf{reproduce or improve on the pass@1}$ performance reported by diverse model-provider families on popular agentic benchmarks (SWE-Pro, SWE-Verified and Terminal-Bench-2), and (ii) building on an $\textbf{analysis of 138k trajectories generated by SSA}$, we look beyond the $\texttt{pass@1}$ numbers which tend to be relatively even across frontier models. By representing agent trajectories in code state-spaces, we observe model-level differences in problem-solving behavior. Finer-grained metrics such as edit frequency, testing activity, and phase-transitions reveal how individual models allocate effort across different stages of autonomous problem solving.

---


### 36. [Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role Agent Simulation](https://arxiv.org/abs/2606.17459)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Xueqing Peng, Lingfei Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the decision-making capabilities of large language models (LLMs) is a growing research priority, yet existing benchmarks focus on isolated cognitive tasks such as reasoning, knowledge retrieval, and economic rationality in stylized settings. These evaluations overlook the defining challenge of real executive decision-making: integrating conflicting recommendations from specialized stakeholders under information asymmetry, organizational constraints, and temporal dependencies. We introduce \textsc{CEO-Bench}, a multi-agent benchmark that evaluates LLMs on CEO-level strategic resource reallocation -- the process of redirecting capital across business units in a multi-round, constraint-rich organizational environment. In \textsc{CEO-Bench}, LLM agents receive conflicting advice from four role-conditioned C-suite advisors (CFO, CTO, COO, CMO), each with private signals and distinct priorities, and must synthesize these into a concrete allocation plan evaluated along four dimensions: role integration, conditional boldness, history-sensitive judgment, and plan validity. Experiments across five frontier models on 13 scenarios reveal that all models achieve high structural validity but diverge sharply on strategic calibration -- the hardest capability layer. We identify systematic failure modes including single-advisor capture, conservative default under ambiguity, and historical amnesia, and uncover a structural integration-boldness tradeoff: models that engage more deeply with conflicting perspectives tend to produce less decisive action. These findings delineate the current capability boundary of LLMs as organizational decision-makers and inform the design of future AI-assisted executive systems.

---


### 37. [CheckMIABench: Firm Foundations For Membership Inference Attacks on Language Models](https://arxiv.org/abs/2606.17464)

**<font color=#1a73e8>作者：</font>** Jeffrey G. Wang, Jason Wang, Marvin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) are a canonical way to assess a machine learning model's privacy properties. Although several attempts have been made to evaluate MIAs on language models, the extant literature has suffered numerous difficulties in constructing clean evaluations to test new techniques. In particular, subtle distribution shifts between member and non-member sets can undermine the statistical validity of MIAs; recent work has underscored this by showing that "blind" methods with no access to the underlying model can perform far better than published methods on the same benchmarks. This paper constructs a benchmark for principled evaluation of MIAs against LLMs, by leveraging the insight that training data before and after a fixed point during training are drawn from the same distribution. Therefore, all open-source models with intermediate checkpoints and public training data can be converted into MIA testbeds. We apply our framework to a half-dozen published attacks on the Pythia and OLMo family of models, from 70M to 7B parameters. To facilitate further privacy research, we open-source a modular library for designing and implementing attacks in this setting: this https URL.

---


### 38. [AIPatient Arena: EHR-grounded evaluation of large language models in end-to-end clinical consultation workflows](https://arxiv.org/abs/2606.17474)

**<font color=#1a73e8>作者：</font>** Jiahui Niu, Huizi Yu, Wenkong Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly considered for use in clinical consultation tasks, yet most medical evaluations remain static, single-turn, or narrowly outcome-based, limiting their ability to reflect the sequential, uncertain, and interactive nature of real-world care. Here, we propose AIPatient Arena, an EHRs-grounded evaluation framework for assessing the clinical utility of LLMs across eight dimensions of clinical competence. The framework integrates EHR data into patient-specific knowledge graphs, enabling multi-turn physician-patient interactions. We applied AIPatient Arena on a primary cohort of 437 patients and two out-of-distribution validation cohorts of 119 and 67 patients. We observe that LLMs performed well in medical interview questioning skills (QS; mean scores, 4.43-4.99/5), ethical and professional conduct (ET; 4.38-4.93/5), and clarity and transparency of clinical explanations (EX; 3.80-4.72/5). Performance was moderate in information integration (II; 3.19-4.21/5) and medication safety and justification (MS; 3.13-3.78/5), but persistent weaknesses were observed in handling of ambiguous patient responses (HR; 2.57-3.32/5), information coverage (IC; 2.08-3.02/5), and diagnostic accuracy and reasoning (Dx; 2.63-3.55/5). Process-based evaluation revealed recurrent interaction failures, including repetitive questioning, omission of past medical history, and inadequate handling of uncertainty. Richer conversational context improved diagnostic reasoning but yielded limited gains in treatment planning. These findings indicate that final-answer accuracy alone is insufficient for evaluating clinical readiness and highlight the importance of assessing how models gather, interpret, and communicate information throughout a consultation. AIPatient Arena provides an EHR-grounded framework for workflow-oriented pre-deployment evaluation of medical LLMs.

---


### 39. [Decoding Hidden Deception in Reasoning LLMs: Activation Explainers for Deception Auditing](https://arxiv.org/abs/2606.17478)

**<font color=#1a73e8>作者：</font>** Kexin Chen, Yi Liu, Haonan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs acquire stronger reasoning capabilities, deceptive behavior becomes an increasingly serious safety concern. Existing deception monitors either score visible transcripts or derive scalar probe scores from representation vectors, leaving little inspectable evidence about why a response is suspicious. We introduce STATEWITNESS, an activation explainer for deception auditing. A separate decoder reads a target model's hidden states, then answers natural-language queries or emits structured reports about them. We evaluate STATEWITNESS on two target reasoning LLMs across seven deception datasets. STATEWITNESS reaches 0.916 mean AUROC, a relative gain of 11.6% over the best black-box text monitor and 25.0% over the best activation-probe baseline under the same evaluation protocol. When combined with existing monitors, STATEWITNESS reduces missed deceptive examples in simple threshold ensembles. Beyond scalar detection, the decoder returns query-level answers, schema reports, and token- or sentence-level evidence traces for human inspection. We view this interface as a potential building block for broader interpretability and alignment tools.

---


### 40. [SPHINX: First Explain, Then Explore](https://arxiv.org/abs/2606.17482)

**<font color=#1a73e8>作者：</font>** Nguyen Do, Tue M. Cao, Tien Van Do 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating adversarial driving scenarios is critical for evaluating and improving autonomous vehicle decision-making systems in simulation. Recent approaches, such as ChatScene and LLM-Attacker, rely primarily on the prior knowledge of Large Language Models and Vision-Language Models to generate driving scenarios procedurally. We argue that adversarial scenes should be generated based on the failure diagnosis (e.g., indecisiveness, multi-frame inconsistency) of the driving policy to specifically address the policy's weaknesses instead of relying on prior assumptions. In this paper, we propose SPHINX, a closed-loop framework for adversarial scenario synthesis guided by a simple principle: first explain, then explore. Beyond blindly exploring the scenario space, SPHINX leverages explainable artificial intelligence methods to analyze the policy, identifying key visual concepts and their influence on policy outputs, and the uncertainty of the decisions. Given the interpretable evidence extracted from the policy's own decision process, we use a vision language model to rationalize and criticize failure modes of the current policy. These critics are then used to generate targeted adversarial scenarios for policy retraining and improvement. We demonstrate that SPHINX can highlight an interpretable account of policy failures while other adversarial scene generation cannot. Across the evaluated benchmarks and test suites, SPHINX can be applied to diverse state-of-the-art autonomous vehicle architectures and yields consistent robustness improvements over existing scenario-generation methods.

---


### 41. [Online LLM Selection via Constrained Bandits with Time-Varying Demand](https://arxiv.org/abs/2606.17489)

**<font color=#1a73e8>作者：</font>** Yin Huang, Qingsong Liu, Jie Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in edge-cloud inference systems to handle diverse user tasks with heterogeneous accuracy, latency, and cost profiles. Selecting the appropriate LLM for each incoming task is critical for ensuring service quality and efficient resource utilization. However, model heterogeneity, stochastic and unknown performance characteristics, and time-varying task demands make static selection strategies inadequate. Real-world deployments often impose hard resource budgets such as monetary expenditure limits, along with soft service-level requirements such as latency guarantees. These constraints introduce additional challenges for online decision-making. We formulate this problem as a constrained stochastic bandit learning task, where the learner sequentially selects models under both packing-type (hard) and covering-type (soft) constraints, while adapting to time-varying task demand. The learner operates without access to the underlying reward, cost, or latency distributions and must rely on partial feedback. We develop a novel online learning algorithm that leverages confidence-bound estimates and demand predictions to balance reward maximization with long-term constraint satisfaction. We provide theoretical guarantees showing sublinear regret and sublinear covering constraint violations compared to an offline benchmark with full information. Experimental results on synthetic workloads demonstrate the effectiveness and robustness of our approach in dynamic, resource-constrained environments.

---


### 42. [Evaluating Second-Order Bias of LLMs Through Epistemic Entitlement](https://arxiv.org/abs/2606.17506)

**<font color=#1a73e8>作者：</font>** Ramaravind Kommiya Mothilal, Terry Jingchen Zhang, Raiyan Ahmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of social bias in LLMs largely focus on whether models generate or imply biased content. However, as LLMs are increasingly used as judges of bias, they may exhibit social biases in subtler ways in how they evaluate biased content, which current methods do not systematically capture. We call this second-order bias: social bias in an LLM's judgment about social bias, which we evaluate through a novel, philosophically grounded reasoning task. Drawing on entitlement epistemology, we conceptualize bias as misplaced foundational knowledge that shapes an agent's rational inquiry, and derive a logical reasoning task for LLMs to judge to whom a biased text is acceptable or non-acceptable. We develop two simple metrics to measure how biased LLM judges are in inferring demographics for acceptability without sufficient support, and how these inferences vary across groups targeted by biased texts. Evaluating open and closed models, we find that our task evades safety guardrails by surfacing bias in model judgment. It varies systematically across target groups, reflects implicit social maps, and shows how models are still triggered by demographic labels. Our work points to the need for LLM bias evaluation in judgment tasks and broadly, for more theoretically grounded approaches to bias evaluation in NLP. We release our code and model responses at this https URL.

---


### 43. [LLM-as-Judge in Education: A Curriculum-Grounded Marking Pipeline](https://arxiv.org/abs/2606.17507)

**<font color=#1a73e8>作者：</font>** Xiwei Xu, Chen Wang, Jacky Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI and large language models (LLMs) are increasingly applied to question generation and automated assessment. However, deploying LLMs in preparation for high-stakes exams requires more than prompt engineering; it demands software pipelines that systematically ground model outputs in authorised curriculum artefacts and marking guidelines issued by education authorities. This paper presents a curriculum-grounded, configurable LLM-as-Judge pipeline for question-level marking, co-developed with an industrial partner, to support exam preparation for university admission. The pipeline identifies the relevant topics, subtopics, and cognitive demand of a question, and assembles verifiable and authorised context to support LLM judgement. Curriculum intent is operationalised through concrete syllabus artefacts, including prescribed verbs and outcomes, performance band descriptors, glossary definitions, and marking-guideline principles. A staged LLM workflow is employed to first generate question-specific rubrics, capturing structured expectations of performance, and then derive and evaluate marking criteria used to allocate marks to student responses. This design improves consistency, transparency, and alignment with official marking practices. Preliminary evaluation shows that the proposed LLM-as-Judge pipeline delivers marking outcomes comparable to human tutors, while yielding justifications that are more traceable to authorised curriculum artefacts and marking standards. The pipeline has also been integrated into an online study platform, where early deployment data provide initial insights into operational usage and manual overrides.

---


### 44. [Learning to Refine Hidden States for Reliable LLM Reasoning](https://arxiv.org/abs/2606.17524)

**<font color=#1a73e8>作者：</font>** Chia-Hsuan Hsu, Jui-Ming Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models show strong reasoning ability, but their internal reasoning process can remain unstable in complex multi-step settings, where early hidden-state errors may propagate to incorrect predictions. We propose ReLAR, a reinforcement-guided latent refinement framework that iteratively updates hidden representations before decoding. ReLAR maintains a compact latent reasoning state and uses learned depth and action controllers to adaptively determine both the number and direction of refinement steps. The controllers are trained with a policy gradient objective based on step-wise likelihood improvement, enabling efficient input-dependent reasoning without explicit chain-of-thought generation. Experiments on medical, mathematical, multi-hop reasoning, and open-ended generation benchmarks show that ReLAR improves accuracy, generation quality, and reasoning stability with substantially lower inference overhead than explicit reasoning baselines.

---


### 45. [MGUP: A Momentum-Gradient Alignment Update Policy for Stochastic Optimization](https://arxiv.org/abs/2606.17526)

**<font color=#1a73e8>作者：</font>** Da Chang, Ganzhao Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient optimization is essential for training large language models. Although intra-layer selective updates have been explored, a general mechanism that enables fine-grained control while ensuring convergence guarantees is still lacking. To bridge this gap, we propose \textbf{MGUP}, a novel mechanism for selective updates. \textbf{MGUP} augments standard momentum-based optimizers by applying larger step-sizes to a selected fixed proportion of parameters in each iteration, while applying smaller, non-zero step-sizes to the rest. As a nearly {plug-and-play} module, \textbf{MGUP} seamlessly integrates with optimizers such as AdamW, Lion, and Muon. This yields powerful variants such as \textbf{MGUP-AdamW}, \textbf{MGUP-Lion}, and \textbf{MGUP-Muon}. Under standard assumptions, we provide theoretical convergence guarantees for \textbf{MGUP-AdamW} (without weight decay) in stochastic optimization. Extensive experiments across diverse tasks, including MAE pretraining, LLM pretraining, and downstream fine-tuning, demonstrate that our \textbf{MGUP}-enhanced optimizers achieve superior or more stable performance compared to their original base optimizers. We offer a principled, versatile, and theoretically grounded strategy for efficient intra-layer selective updates, accelerating and stabilizing the training of large-scale models. The code is publicly available at this https URL.

---


### 46. [OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation](https://arxiv.org/abs/2606.17536)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Yufei Liu, Chengqian Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

---


### 47. [Reinforcing Dual-Path Reasoning in Spatial Vision Language Models](https://arxiv.org/abs/2606.17539)

**<font color=#1a73e8>作者：</font>** Yatai Ji, An-Chieh Cheng, Yang Fu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial VLMs have made substantial progress in geometric perception, yet complex spatial reasoning requiring multi-step inference over depth, distance, and scene relations remains challenging. Moreover, different spatial queries call for fundamentally different strategies: some are best addressed through purely linguistic, step-by-step deduction, while others require explicit 3D grounding before quantitative inference. We present Dual-Path Spatial Reasoning via Reinforcement Learning for Spatial VLMs (SR-REAL), a unified framework that equips a spatial VLM with two complementary reasoning paths: Language-Only Reasoning (LOR), which performs step-by-step linguistic deduction, and Detect-Then-Reason (DTR), which detects 3D geometric cues (e.g., centers or bounding boxes) via region tokens before explicit geometric inference. SR-REAL begins with a cold-start supervised fine-tuning stage that constructs LOR and DTR chain-of-thought supervision and exposes a region-to-3D interface, followed by RL that optimizes the policy model with accuracy and format rewards; for DTR, a discrete center-based detection reward further refines geometric alignment. Across diverse spatial benchmarks, SR-REAL significantly outperforms spatial VLM baselines: (i) a single RL-trained model supports both reasoning paths, with DTR excelling in region-aware tasks through precise 3D localization and LOR enhancing general spatial reasoning; (ii) jointly training both paths fosters mutual reinforcement; (iii) high-quality, blended cold-start data is crucial for stable RL optimization; and (iv) the model generalizes across datasets and domains without per-task tuning, demonstrating positive transfer between LOR and DTR.

---


### 48. [Evaluating Large Language Models Abilities for Addressee, Turn-change, and Next Speaker Prediction in Meetings](https://arxiv.org/abs/2606.17542)

**<font color=#1a73e8>作者：</font>** Ryo Fukuda, Takatomo Kano, Siddhant Arora 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate turn-taking in multimodal multi-party conversations using large language models (LLMs). We construct an evaluation framework for three tasks: addressee detection, turn-change prediction, and next speaker prediction. We compare supervised models trained for these tasks, text-based LLMs, multimodal LLMs (MM-LLMs), and human subjects. Experiments on the AMI corpus showed that LLMs outperformed supervised models and humans in next speaker prediction, despite not being trained on the target domain and without access to audio or visual information. An MM-LLM performed better than text-based LLMs on addressee detection and turn-change prediction but remained below human performance, indicating difficulty leveraging raw audio-visual signals. Ablation analyses revealed that conversational context was critical, particularly for next speaker prediction. We observed that human and LLM prediction patterns were similar, and intervals with frequent turn changes were difficult for both.

---


### 49. [SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.17546)

**<font color=#1a73e8>作者：</font>** Congjie Zheng, Chuanyi Xue, Bin Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

---


### 50. [Geometric Consistency Protocol for Foundation Model Features in Multi-View Satellite Imagery](https://arxiv.org/abs/2606.17564)

**<font color=#1a73e8>作者：</font>** Qiyan Luo, Jie Yang, Yingdong Pi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standardized evaluation protocols are indispensable for robust benchmarking in remote sensing, particularly as foundation features are increasingly transferred across diverse sensors and complex imaging geometries. In satellite multi-view reconstruction, conventional evaluations relying on unconstrained 2D global matching are often misleading. The Rational Function Model (RFM) and its Rational Polynomial Coefficients (RPC) dictate a curved, height-dependent epipolar geometry that render flat 2D search spaces physically inconsistent. We propose a geometry-faithful and reproducible protocol tailored for the RPC framework. Our approach integrates an RPC-projected 3D consistency metric with a geometry-constrained dense matching proxy, specifically evaluating whether similarity responses remain localized and unique under physically plausible search manifolds. A pivotal finding of our joint reporting strategy is the decoupling of semantic agreement and geometric localization: high cross-view similarity at a projected 3D point does not guarantee reliable matchability in practical inference. Our benchmark demonstrates that incorporating geometric constraints is fundamental to the problem definition in satellite imagery. Furthermore, we show that state-of-the-art 2D backbones remain remarkably competitive against specialized 3D-aware models when subjected to this RPC-consistent evaluation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-133](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
