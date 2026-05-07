# 🧠 大模型相关研究 | 2026年05月08日

> 本类共 **126** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-126](./part-03.md)

---

### 1. [Structured Progressive Knowledge Activation for LLM-Driven Neural Architecture Search](https://arxiv.org/abs/2605.04057)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Yuhan Liu, Jingwen Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper focuses on a key challenge in Neural Architecture Search (NAS): integrating established architectural knowledge while exploring new designs under expensive evaluations. Large language models (LLMs) are a promising assistant for NAS because they can translate rich architectural and coding priors into executable code edits. However, in practice, seemingly local revisions often propagate into non-local behavioral and performance shifts because a single edit can inadvertently couple multiple interacting functional factors, a phenomenon we refer to as functional entanglement. To make LLM knowledge usable under such entanglement, we propose Structured Progressive Knowledge Activation (SPARK), which activates relevant priors by explicitly selecting the functional factor to modify and conditioning the edit on that factor. This factor-conditioned editing reduces entangled side effects and yields more targeted, reliable architecture modifications. On CLRS-DFS, SPARK achieves a 28.1x sample-efficient architecture evolution speedup and yields a 22.9 percent relative improvement in OOD accuracy.

---


### 2. [MP-ISMoE: Mixed-Precision Interactive Side Mixture-of-Experts for Efficient Transfer Learning](https://arxiv.org/abs/2605.04058)

**<font color=#1a73e8>作者：</font>** Yutong Zhang, Zimeng Wu, Shangcai Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient transfer learning (PETL) has emerged as a pivotal paradigm for adapting pre-trained foundation models to downstream tasks, significantly reducing trainable parameters yet suffering from substantial memory overhead caused by gradient backpropagation during fine-tuning. While memory-efficient transfer learning (METL) circumvents this challenge by bypassing backbone gradient computation via lightweight small side networks, its stringent memory constraint severely limits learning capacity of side networks, thereby significantly compromising performance. To address these limitations, we propose a novel Mixed-Precision Interactive Side Mixture-of-Experts framework (MP-ISMoE). Specifically, we first propose a Gaussian Noise Perturbed Iterative Quantization (GNP-IQ) scheme to quantize weights into lower-bits while effectively decreasing quantization errors. By leveraging memory conserved from GNP-IQ, we subsequently employ Interactive Side Mixture-of-Experts (ISMoE) to scaling up side networks without sacrificing overall memory efficiency. Different from conventional mixture-of-experts, ISMoE learns to select optimal experts by interacting with salient features from frozen backbones, thus suppressing knowledge forgetting and boosting performance. Extensive experiments across diverse vision-language and language-only tasks demonstrate that MP-ISMoE remarkably promotes accuracy compared to state-of-the-art METL approaches, while maintaining comparable parameter and memory efficiency.

---


### 3. [Single-Position Intervention Fails: Distributed Output Templates Drive In-Context Learning](https://arxiv.org/abs/2605.04061)

**<font color=#1a73e8>作者：</font>** Bryan Cheng, Jasper Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how large language models encode task identity from few-shot demonstrations is a central open problem in mechanistic interpretability. Prior work uses linear probing to localize task representations, reporting high classification accuracy at specific layers. We reveal a striking dissociation: probing accuracy completely fails to predict causal importance. Single-position activation intervention achieves 0% task transfer across all 28 layers of Llama-3.2-3B-despite 100% probing accuracy at those same positions. This null result is itself a key finding, demonstrating that task encoding is fundamentally distributed. Multi-position intervention-replacing activations at all demonstration output tokens simultaneously-achieves up to 96% transfer (N=50, 95% CI: [87%, 99%]) at layer 8, pinpointing for the first time the causal locus of ICL task identity. We establish the generality of these findings across four models spanning three architecture families (LLaMA, Qwen, Gemma), discovering a universal intervention window at ~30% network depth. Causal tracing uncovers an asymmetric architecture: the query position is strictly necessary (53-100% disruption) while no individual demonstration position is necessary (0% disruption)-resolving a key ambiguity in prior accounts. Crucially, transfer depends on internal representation compatibility, not surface similarity (r=-0.05 vs r=0.31), ruling out trivial explanations. These results establish the distributed template hypothesis: ICL task identity is encoded as output format templates distributed across demonstration tokens, fundamentally reshaping our understanding of how in-context learning operates.

---


### 4. [EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation](https://arxiv.org/abs/2605.04062)

**<font color=#1a73e8>作者：</font>** Shu-Hao Zhang, Le-Tong Huang, Xiang-Sheng Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed an increasing interest in deploying LLMs on resource-constrained devices, among which quantization has emerged as a promising lightweight technique that converts full-precision model weights and activations into lower-bit formats. Existing weight quantization approaches can be roughly divided into three categories: Post-Training Quantization (PTQ) that calibrates quantized parameters on a small dataset without retraining but suffers from severe performance degradation below 4-bit, Quantization-Aware Training (QAT) that searches low-bit parameters using surrogate gradients but demands substantial computational resources, and Quantization-Aware Distillation that integrates QAT with knowledge transfer from a full-precision teacher but manually selects features to distill and relies heavily on teacher-specific data. In this paper, we propose EdgeRazor, a lightweight framework for LLMs with mixed-precision and extremely low-bit weight quantization. The EdgeRazor framework contains three modules: Mixed-Precision Quantization-Aware Distillation for the fine-grained control of precision, Adaptive Feature Distillation that derives an $n$-bit student from its 16-bit teacher, and Entropy-Aware KL Divergence on both human-annotated and distilled datasets, whose forward-reverse balance is determined solely by the teacher's output distribution. Empirical investigations of EdgeRazor are conducted on base, instruction-tuned, and multimodal LLMs. Notably, EdgeRazor with 1.88-bit surpasses all contenders with the 3-bit precision, especially outperforms the leading 2-bit PTQ methods by 11.3 points, within a 4-10$\times$ lower training budget than the leading QAT approach. EdgeRazor delivers higher compression ratios at all bit width; the 1.58-bit Qwen3-0.6B reduces storage from 1.41 GB to 0.28 GB while accelerating decoding by 15.1$\times$ relative to the 16-bit baseline.

---


### 5. [Improving Medical VQA through Trajectory-Aware Process Supervision](https://arxiv.org/abs/2605.04064)

**<font color=#1a73e8>作者：</font>** Halil Ibrahim Gulluk, Olivier Gevaert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning capabilities are crucial for reliable medical visual question answering (VQA); however, existing datasets rarely include reasoning explanations.
We address this by generating reasoning trajectories for six medical VQA benchmarks using the COMCTS algorithm with open-source vision-language models, with an LLM serving as the verification judge.
Building on these generated datasets, we propose a two-stage training framework: supervised fine-tuning followed by Group Relative Policy Optimization (GRPO) with a novel process-based reward.
While standard approaches rely solely on exact-match rewards for final answers, we introduce a trajectory-aware reward that measures the similarity between generated and ground-truth reasoning processes.
Specifically, we embed reasoning steps using sentence transformers and compute the Dynamic Time Warping (DTW) distance between the resulting vector sequences.
Experiments across six benchmarks demonstrate that combining the DTW-based process reward with exact-match reward consistently outperforms SFT-only training, raising mean accuracy from 0.598 to 0.689, mean BERTScore from 0.845 to 0.881, and mean ROUGE-L from 0.665 to 0.748.
Our results highlight the importance of process supervision in training reasoning-capable medical VLMs.
We make our code and generated reasoning datasets publicly available at this https URL

---


### 6. [Free Energy-Driven Reinforcement Learning with Adaptive Advantage Shaping for Unsupervised Reasoning in LLMs](https://arxiv.org/abs/2605.04065)

**<font color=#1a73e8>作者：</font>** Yiming Huang, Zhenbo Shi, Xin-Cheng Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unsupervised reinforcement learning (RL) has emerged as a promising paradigm for enabling self-improvement in large language models (LLMs). However, existing unsupervised RL-based methods often lack the capacity to adapt to the model's evolving reasoning capabilities during training. Therefore, these methods can misdirect policy optimization in the absence of ground-truth supervision. To address this issue, we introduce FREIA, a novel RL-based algorithm built on two key innovations: (1) Free Energy-Driven Reward (FER) adapts rewards to balance consensus and exploration based on the Free Energy Principle. (2) Adaptive Advantage Shaping (AAS) adaptively adjusts learning signals based on the statistical characteristics of sampled rewards. Empirical evaluations on nine datasets across three reasoning tasks showcase that FREIA outperforms other unsupervised RL-based baselines. Notably, in mathematical reasoning tasks, FREIA surpasses other methods by an average of 0.5 to 3.5 points in Pass@1 using the DeepSeek-R1-Distill-Qwen-1.5B model.

---


### 7. [Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning](https://arxiv.org/abs/2605.04066)

**<font color=#1a73e8>作者：</font>** Yiming Huang, Zhenbo Shi, Shuzheng Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is an essential paradigm that enhances the reasoning capabilities of Large Language Models (LLMs). However, existing methods typically rely on static policy optimization schemes that misalign with the model's evolving reasoning capabilities. To address this issue, we propose Adaptive Power-Mean Policy Optimization (APMPO), which comprises two main innovations: Power-Mean Policy Optimization (PMPO) and Feedback-Adaptive Clipping (FAC). Specifically, PMPO introduces a generalized power-mean objective. This enables the model to adaptively transition from the signal-amplifying behavior of the arithmetic mean to the consistency-enforcing behavior of the geometric mean. FAC adaptively adjusts clipping bounds based on real-time reward statistics to overcome the limitations of static mechanisms. Capitalizing on these innovations, APMPO improves learning dynamics and reasoning performance. Extensive experiments on nine datasets across three reasoning tasks showcase the superiority of APMPO over state-of-the-art RLVR-based baselines. For instance, APMPO boosts the average Pass@1 score on mathematical reasoning benchmarks by 3.0 points compared to GRPO when using Qwen2.5-3B-Instruct.

---


### 8. [A Physics-Aware Framework for Short-Term GPU Power Forecasting of AI Data Centers](https://arxiv.org/abs/2605.04074)

**<font color=#1a73e8>作者：</font>** Mohammad AlShaikh Saleh, Sanjay Chawla, Sertac Bayhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI data centers experience rapid fluctuations in power demand due to the heterogeneity of computational tasks that they have to support. For example, the power profile of inference and training of large language models (LLMs) is quite distinct and big divergences can result in the instability of the underlying electricity grid. In this paper we propose, to the best of our knowledge, the first physics-informed DLinear time-series model that can accurately forecast power utilization of an AI data center 5-80 minutes (short-term forecasting) into the future. The physics, based on a multi-node lumped thermal resistance-capacitance (RC) network consistent with Newton's law of cooling, is captured using newly derived time-dependent ordinary differential equations (ODE) that separately models and interlinks power consumption with the GPU compute and memory utilization and temperature. The resulting model, that we refer to as PI-DLinear, trained and evaluated on a real AI data center dataset and is not only more accurate than the state-of-the-art (SOTA) models tested, but the forecast profile respects the underlying physics under power throttling and load transient events. Relative to the SOTA transformer-based and non-transformer-based models, improvements in forecasting accuracy (averaged across all look-back and prediction windows) range from 0.782%-39.08% for MSE, 0.993%-51.82% for MAE, and 0.370%-22.28% for RMSE.

---


### 9. [RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction](https://arxiv.org/abs/2605.04075)

**<font color=#1a73e8>作者：</font>** Sihao Liu, YuFan Xiong, Zhonghua Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models face severe challenges in computational efficiency and memory consumption due to the substantial expansion of the visual KV cache when processing long visual contexts. Existing KV cache compression methods typically rely on the "persistence of importance" hypothesis to prune tokens. However, this approach proves fragile in multimodal settings due to two key issues: 1) Visual tokens display "deferred importance," initially exhibiting low salience but becoming pivotal during later decoding, which can lead to premature eviction. 2) Discrete pruning disrupts the inherent spatial continuity of visual cues. To address these challenges, we propose RetentiveKV, an entropy-driven KV cache optimization method that reformulates KV eviction from "discrete context truncation" to "continuous memory evolution" based on State Space Models. Our method leverages information entropy to quantify the information potential of low-attention tokens and integrates tokens scheduled for eviction into a continuous state space through entropy-guided state transitions, enabling their dynamic reactivation when semantic relevance arises during subsequent decoding. Extensive experiments on multimodal benchmarks demonstrate that RetentiveKV achieves 5.0 times KV cache compression and 1.5 times decoding acceleration.

---


### 10. [Validity-Calibrated Reasoning Distillation](https://arxiv.org/abs/2605.04078)

**<font color=#1a73e8>作者：</font>** Khouloud Saadi, Di Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning distillation aims to transfer multi-step reasoning capabilities from large language models to smaller, more efficient ones. While recent methods have shown promising gains, they typically rely on static teacher-student hierarchies and frame distillation as trajectory imitation. This is misaligned with the structure of reasoning, where intermediate steps are often locally under-specified: global correctness constrains the final answer, but does not uniquely determine each intermediate move. We propose validity-calibrated reasoning distillation, a framework that treats reasoning distillation as a problem of local learning-signal allocation rather than path alignment. Instead of enforcing token-level imitation, we compare the student's and teacher's proposed next-step actions under the same prefix and use their relative local validity to modulate the strength of the distillation update. This yields a dynamic, context-dependent supervision mechanism that preserves the teacher's structural guidance while adapting update strength to local reasoning quality. Across mathematical reasoning, code generation, and instruction-following benchmarks, our method consistently outperforms strong distillation baselines. These results indicate that effective LLM reasoning distillation is governed not by rigid trajectory imitation, but by principled, locally calibrated allocation of learning signal.

---


### 11. [Efficient Handwriting-Based Alzheimer,s Disease Diagnosis Using a Low-Rank Mixture of Experts Deep Learning Framework](https://arxiv.org/abs/2605.04079)

**<font color=#1a73e8>作者：</font>** Wu Wang, Yuang Cheng, Fouzi Harrou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early and reliable detection of Alzheimer's disease (AD) is crucial for timely clinical intervention and improved patient management. It also supports the evaluation of emerging therapeutic strategies. In this paper, we propose a Low-Rank Mixture of Experts (LoRA-MoE) deep learning framework for Alzheimer's disease diagnosis based on handwriting analysis. Handwriting signals provide a non-invasive and scalable digital biomarker that captures subtle cognitive-motor impairments associated with early AD progression. The proposed architecture allows multiple experts to specialize in different handwriting patterns while sharing a common base network. This design enables efficient learning of general representations while reducing interference between experts. Each expert is equipped with lightweight low-rank adapters. This mechanism significantly reduces the number of trainable parameters compared with standard Mixture of Experts (MoE) models and improves training stability. The proposed framework is evaluated on the Diagnosis AlzheimeR WIth haNdwriting (DARWIN) dataset. Extensive experiments are conducted, including ablation studies on key architectural parameters such as hidden dimension size, number of experts, and LoRA rank. The method is compared with multilayer perceptron (MLP) and conventional MoE architectures. In addition, stacking ensemble strategies (StackMean and StackMax) are investigated to improve robustness and predictive performance. Experimental results show that the LoRA-MoE framework achieves powerful diagnostic performance while activating significantly fewer parameters during inference. These results highlight the potential of the proposed approach as an accurate and computationally efficient solution for handwriting-based Alzheimer's disease screening and digital health applications.

---


### 12. [AsymmetryZero: A Framework for Operationalizing Human Expert Preferences as Semantic Evals](https://arxiv.org/abs/2605.04083)

**<font color=#1a73e8>作者：</font>** Tadhg Looram, Lucas Nuzzi, Kyle Waters 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Much of the focus in RL today is on evaluation design: building meaningful evals that serve simultaneously as benchmarks and as well-defined reward signals for post-training. Yet, many real-world tasks are governed by subjective, procedural, and domain-specific requirements that are difficult to encode as exact-match targets or open-ended preference judgments frequently used in RL pipelines today. In this work, we present AsymmetryZero, a framework for operationalizing human expert preferences as semantic evals. AsymmetryZero represents each task as a stable evaluation contract that makes grading criteria explicit: what is being graded, how each criterion is judged, and how criterion-level decisions are aggregated into a task outcome. The same contract can be executed using Inspect for model-only evaluations, as well as the Harbor Framework for agentic evaluations, enabling comparable scores and shared audit artifacts across both settings. We argue that the central challenge in post-training today is the faithful encoding of expert requirements into the evaluation itself. To that end, we present a study using Harbor that holds task contracts fixed and compares a five-model frontier jury against a five-model compact jury across four frontier-class solvers (Claude Opus 4.6, GPT-5.4, Grok-4.20, Gemini-3.1-Pro). We find that criterion-level frontier-vs-compact agreement ranges from $75.9\%$ to $89.6\%$ (strict common-subset agreement: $77.8\%$ to $92.1\%$), while compact juries exhibit substantially higher internal dissent (3--2 split rate $28.7\%$--$32.4\%$) than frontier juries ($6.1\%$--$11.5\%$). Verifier traces further show that compact juries reduce per-criterion judging cost to roughly $4.2\%$--$5.6\%$ of frontier and latency to roughly $21.7\%$--$27.1\%$, even as aggregated task-level outcomes often remain comparatively stable.

---


### 13. [FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression](https://arxiv.org/abs/2605.04084)

**<font color=#1a73e8>作者：</font>** Ye Qiao, Yian Wang, Zhiheng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compressing large language models (LLMs) for deployment on commodity GPUs remains challenging: conventional scalar quantization is limited to fixed bit-widths (e.g., 8/4/3-bit), offers only a few discrete compression points, and typically requires calibration data. We present FASQ (Flexible Accelerated Subspace Quantization), a calibration-free framework that applies product quantization to LLM weight matrices. By tuning two parameters, sub-vector size and codebook cardinality, FASQ exposes a continuous design space spanning 27-49% of the original FP16 model size, filling compression gaps that fixed-bit schemes cannot reach. On Meta-Llama-3-8B, FASQ surpasses 4-bit GPTQ and AWQ in accuracy (67.1-67.7 avg.) at 37-42% model size, with consistent results on Qwen3-8B and Qwen3.5-9B-Base. To make product quantization practical at inference time, we design custom CUDA kernels: a LUT-free direct-compute GEMV for decode and an output-stationary double-buffered LUT GEMM for prefill, both with split-K parallelism. On an RTX~3090, FASQ achieves 45.2 tok/s decode at effective 4-bit (2.56x memory reduction) and 51.8 tok/s at effective 3-bit (2.80x), both surpassing FP16 tensor-core performance (43.9 tok/s) and delivering 1.6 to 1.8x the throughput of AWQ, 2.5 to 2.5x of GPTQ, and 4.3 to 5x of RTN. FASQ is the only compressed method that accelerates decode beyond FP16, offering calibration-free compression, continuous size-quality trade-offs, and real-time inference on a single consumer GPU.

---


### 14. [Are Multimodal LLMs Ready for Clinical Dermatology? A Real-World Evaluation in Dermatology](https://arxiv.org/abs/2605.04098)

**<font color=#1a73e8>作者：</font>** Roy Jiang, Hyunjae Kim, Zhenyue Qin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated promise on publicly available dermatology benchmarks. However, benchmark performance may not generalize to real-world dermatologic decision-making. To quantify this benchmark-to-bedside gap, we evaluated four open-weight MLLMs (InternVL-Chat v1.5, LLaVA-Med v1.5, SkinGPT4 and MedGemma-4B-Instruct) and one commercial MLLM (GPT-4.1) across three publicly available dermatology datasets and a retrospective multi-site hospital-based dermatology consultation cohort comprising 5,811 cases and 46,405 clinical images. Models were evaluated on two clinically relevant tasks: differential diagnosis generation and severity-based triage. Diagnostic performance was modest on public datasets and declined substantially in the real-world cohort. On public benchmarks, top-3 diagnostic accuracy reached 26.55% for the best open-weight model and 42.25% for GPT-4.1. On real-world consultation cases using images alone, top-3 diagnostic accuracy fell to 1.50%-13.35% among open-weight models and 24.65% for GPT-4.1. Incorporating clinical context improved performance across all models, increasing top-3 diagnostic accuracy up to 28.75% among open-weight models and 38.93% for GPT-4.1. However, model outputs were highly sensitive to incomplete or erroneous consultation context. For severity-based triage, models achieved moderate sensitivity (above 60%), suggesting potential utility for screening but insufficient reliability for clinical deployment. These findings demonstrate that benchmark performance substantially overestimates the real-world clinical capability of current dermatology MLLMs.

---


### 15. [FMI_SU_Yotkova_Kastreva at SemEval-2026 Task 13: Lightweight Detection of LLM-Generated Code via Stylometric Signals](https://arxiv.org/abs/2605.04157)

**<font color=#1a73e8>作者：</font>** Elitsa Yotkova, Violeta Kastreva, Dimitar Dimitrov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SemEval-2026 Task 13 investigates machine-generated code detection across multiple programming languages and application scenarios, asking participating systems to generalize to unseen languages and domains. This paper describes our participation in Subtask A (binary classification) and explores both pretrained code encoders and lightweight feature-based methods. We design ratio-based features that are less sensitive to snippet length. To support the extraction of descriptiveness-related signals, we use parsing engines and a programming-language classifier. Additionally, we train a separate code-vs-text line classifier to identify raw natural language segments embedded within samples. We combine a shallow decision tree with heuristic rules derived from data analysis to produce the final predictions. Our approach is computationally efficient, requires only CPU resources for training, and achieves near-instant inference time, offering a lightweight alternative to large pretrained models.

---


### 16. [Not All That Is Fluent Is Factual: Investigating Hallucinations of Large Language Models in Academic Writing](https://arxiv.org/abs/2605.04171)

**<font color=#1a73e8>作者：</font>** Humam Khan, Md Tabrez Nafis, Shahab Saquib Sohail 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language models (LLMs) show extraordinary abilities, but they are still prone to hallucinations, especially when we use them for generating Academic content. We have investigated four popular LLMs, ChatGPT, Grok, Gemini, and Copilot for hallucinations specifically for academic writing. We have designed 80 prompts across four categories, namely, reference generation, factual explanation, abstract generation, and writing improvement. We evaluated the model using a 0-5 rubric score, which checks factual accuracy, reference validity, coherence, style consistency, and academic tone. A novel weighted metric, Hallucination Index (HI), was introduced to measure hallucination in the responses generated by the models. Some of the most widely used evaluation metrics often fail to check errors which alter sentiment in machine-translated text. We found that Grok and Copilot perform better on reference generation tasks, but they often struggle with abstract or stylistic prompts, with HI values of 0.67 and 0.70, respectively. Whereas, Gemini and ChatGPT have done well with having stronger tone control, but they lack in writing factual tasks and higher hallucination risk with HI scores of 0.53 and 0.57, respectively. Our study found that hallucination behavior does not depend solely on model architecture but also on the type of task and the prompting conditions we are providing. We propose that our work opens new research dimensions for future researchers.

---


### 17. [Are LLMs Ready for Conflict Monitoring? Empirical Evidence from West Africa](https://arxiv.org/abs/2605.04177)

**<font color=#1a73e8>作者：</font>** Hoffmann Muki, Olukunle Owolabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs enter conflict monitoring, understanding systematic distortions in their outputs is critical for humanitarian accountability. We evaluate four vanilla open-weight models Gemma 3 4B, Llama 3.2 3B, Mistral 7B, and OLMo 2 7B and two domain-adapted models, AfroConfliBERT and AfroConfliLLAMA, on Nigeria and Cameroon conflict-event classification against ACLED, a gold-standard dataset with multi-stage verification. We find a bifurcated divergence in normative directionality. Open-weight models exhibit statistically significant False Illegitimation bias: Gemma misclassifies to 18.29% of legitimate battles as civilian-targeted violence while making zero False Legitimation errors. By contrast, AfroConfliBERT and AfroConfliLLAMA achieve near-directional neutrality, with Legitimization Bias differences indistinguishable from zero. Yet domain adaptation does not eliminate actor-based selection bias. Both adapted models show statistically significant actor bias comparable to vanilla LLMs; in Nigeria, state actors are legitimized 36.5% more often than non-state actors in identical tactical contexts. Open-weight outputs are also fragile to geography-specific lexical framing: delegitimizing phrases produce flip rates up to 66.7% in Cameroon and 34.2% in Nigeria, while perturbations salient in one context may not matter in another. Error trace profiling shows models mask normative bias through unfaithful rationale confabulations. In contrast, AfroConfliBERT and AfroConfliLLAMA are largely robust, with near-zero flip rates across perturbation categories. Overall, current models are not ready for unsupervised deployment in conflict monitoring. We call for fairness-aware fine-tuning to reduce actor-based selection bias, mandatory adversarial robustness evaluation against lexical manipulation, and context-specific human-in-the-loop oversight calibrated to regional difficulty.

---


### 18. [MedFabric and EtHER: A Data-Centric Framework for Word-Level Fabrication Generation and Detection in Medical LLMs](https://arxiv.org/abs/2605.04180)

**<font color=#1a73e8>作者：</font>** Tung Sum Thomas Kwok, Qian Qian, Xiaofeng Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models exhibit strong reasoning and semantic understanding capabilities but often hallucinate in domains that require expert knowledge, among which fabrications, the generation of factually incorrect yet fluent statements, pose the greatest risk in medical contexts. Existing medical hallucination datasets inadequately capture fabrication phenomena due to limited fabrication coverage, stylistic disparities between human and LLM-authored texts, and distributional drift during hallucinated sample synthesis. To address this, we propose a data-centric pipeline to generate realistic and word-level fabrications that preserve syntactic and stylistic fidelity while introducing subtle factual deviations, resulting in MedFabric. Building upon this dataset, we introduce ETHER, a modular word-level fabrication detector integrating Text2Table Decomposition, Word Masking and Filling and Hybrid Sentence Pair Evaluation to enhance factual alignment. Empirical results demonstrate that MedFabric outperforms state-of-the-art detectors by over 15% on word-level fabrication benchmarks while maintaining consistent performance across structural similarities, offering a comprehensive framework for reliable and domain-specific factuality detection.

---


### 19. [Nsanku: Evaluating Zero-Shot Translation Performance of LLMs for Ghanaian Languages](https://arxiv.org/abs/2605.04208)

**<font color=#1a73e8>作者：</font>** Stephen E. Moore, Mich-Seth Owusu, Akwasi Asare 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated impressive multilingual capabilities for well-resourced languages, yet their performance on low-resource African languages remains poorly understood and largely unevaluated. This paper presents Nsanku, a systematic benchmark that evaluates the zero-shot machine translation performance of 19 open-weight and proprietary LLMs across 43 Ghanaian languages paired with English. Evaluation sentences were sourced from the YouVersion Bible platform, providing 300 sentence pairs per language. Two complementary automatic metrics are employed: Bilingual Evaluation Understudy (BLEU) and Character n-gram F-Score (chrF), alongside an average accuracy score and a cross-language consistency dimension. Nsanku represents the most comprehensive LLM translation evaluation for Ghanaian languages conducted to date. Results show that gemini-2.5-flash achieves the highest overall average score of 26.88 (BLEU: 24.60, chrF: 29.16), followed by claude-sonnet-4-5 at 24.87 (BLEU: 22.46, chrF: 27.28) and gpt-4.1 at 23.20 (BLEU: 21.15, chrF: 25.24). Among open-weight models, kimi-k2-instruct-0905 leads at an average score of 20.87. A critical finding from the consistency analysis is that no model and no language reached the Leaders quadrant of high performance and high consistency simultaneously, indicating that current LLMs are not yet reliably usable for Ghanaian language translation at scale. Siwu achieved the highest per-language average score at 25.73 while Nkonya scored lowest at 11.65. Nsanku establishes a publicly available, community-extensible evaluation infrastructure for African language NLP research.

---


### 20. [Predict-then-Diffuse: Adaptive Response Length for Compute-Budgeted Inference in Diffusion LLMs](https://arxiv.org/abs/2605.04215)

**<font color=#1a73e8>作者：</font>** Michael Rottoli, Subhankar Roy, Stefano Paraboschi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based Large Language Models (D-LLMs) represent a promising frontier in generative AI, offering fully parallel token generation that can lead to significant throughput advantages and superior GPU utilization over traditional autoregressive paradigm. However, this parallelism is constrained by the requirement of a fixed-size response length prior to generation. This architectural limitation imposes a severe trade-off: oversized response length results in computational waste on semantically meaningless padding tokens, while undersized response length cause output truncation requiring costly re-computations that introduce unpredictable latency spikes. To tackle this issue, we propose Predict-then-Diffuse, a simple and model-agnostic framework, that enables compute-budgeted inference per input query by first estimating the response length and then using it to run inference with D-LLM. At its core lies a Adaptive Response Length Predictor (AdaRLP) auxiliary predictor that predicts the optimal response length given an input query. As a measure against under-predicting the response length and re-running inference with a higher response length, we introduce a data-driven safety mechanism, which trades a negligible padding overhead. As a whole, our framework limits the significant waste of computation on padding tokens and preserves output quality. Experimental validation on multiple datasets demonstrate that Predict-then-Diffuse significantly reduces computational costs (FLOP) compared to the default D-LLM inference mechanism and baselines based on heuristics, while being robust to skewed data distributions.

---


### 21. [Self-Prompting Small Language Models for Privacy-Sensitive Clinical Information Extraction](https://arxiv.org/abs/2605.04221)

**<font color=#1a73e8>作者：</font>** Yao-Shun Chuang, Tushti Mody, Uday Pratap Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical named entity recognition from dental progress notes is challenging because documentation is highly unstructured, domain-specific, and often privacy-sensitive. We developed a locally deployable framework that enables small language models to self-generate, verify, refine, and evaluate entity-specific prompts for extracting multiple clinical entities from dental notes. Using 1,200 annotated notes, we evaluated candidate open-weight models with multi-prompt ensemble inference and further adapted selected models using QLoRA-based supervised fine-tuning and direct preference optimization. Model performance varied substantially, highlighting the need for task-specific evaluation rather than reliance on generic benchmarks. Qwen2.5-14B-Instruct achieved the strongest baseline performance. After DPO, Qwen2.5-14B-Instruct and Llama-3.1-8B-Instruct achieved micro/macro F1 scores of 0.864/0.837 and 0.806/0.797, respectively. These findings suggest that automated prompt optimization combined with lightweight preference-based post-training can support scalable clinical information extraction using locally deployed small language models.

---


### 22. [Pro$^2$Assist: Continuous Step-Aware Proactive Assistance with Multimodal Egocentric Perception for Long-Horizon Procedural Tasks](https://arxiv.org/abs/2605.04227)

**<font color=#1a73e8>作者：</font>** Lilin Xu, Bufang Yang, Siyang Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural tasks with multiple ordered steps are ubiquitous in daily life. Recent advances in multimodal large language models (MLLMs) have enabled personal assistants that support daily activities. However, existing systems primarily provide reactive guidance triggered by user queries, or limited proactive assistance for isolated short-term events rather than long-horizon procedural tasks. In this work, we introduce Pro$^2$Assist, a step-aware proactive assistant that continuously tracks fine-grained task progress and reasons over the user's evolving state to provide timely assistance throughout tasks. Pro$^2$Assist leverages multimodal data from augmented reality (AR) glasses to achieve motion-based perception. It then extracts step-oriented procedural context from multi-scale temporal dynamics and task-specific expert knowledge. Based on both sensory input and procedural context, Pro$^2$Assist performs continuous reasoning to infer user needs and display timely assistance on AR glasses. We evaluate Pro$^2$Assist using a dataset curated from public sources and a real-world dataset collected on our testbed with AR glasses. Extensive evaluations show that Pro$^2$Assist outperforms the best-performing baselines by over 21% in procedural action understanding accuracy, and it achieves up to 2.29x the proactive timing accuracy of baselines. A user study with 20 participants further shows that 90% find Pro$^2$Assist useful, indicating its effectiveness for real-world procedural assistance.

---


### 23. [Adaptive Consensus in LLM Ensembles via Sequential Evidence Accumulation: Automatic Budget Identification and Calibrated Commit Signals](https://arxiv.org/abs/2605.04236)

**<font color=#1a73e8>作者：</font>** Roberto Medina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model ensembles improve reasoning accuracy up to a performance boundary; beyond it, additional deliberation degrades accuracy. Static-budget methods cannot detect this boundary. Extended-thinking architectures compound the problem: a wrong answer after 120k tokens is indistinguishable from a correct one. We introduce DASE (Deliberative Adaptive Stopping Ensemble), a stopping heuristic for iterative ensemble deliberation that commits early on genuine consensus and applies a global-frequency fallback on fragmented evidence. Two configurations are evaluated: a persistence heuristic and DASE-Spatial (arena half-width W). Three contributions. (1) DASE produces a commit-type routing partition complementary to verbalized single-call confidence. On a contamination-controlled corpus (AIME 2010-2023, N=254, 3 seeds), a 120B ensemble achieves a 24.8 pp routing gap (right-wall 97.1% vs. left-wall 73.6%), statistically equivalent to Opus 4.6 Standard verbalized confidence at coverage-matched threshold (25.7 pp gap; bootstrap CI on difference: [-12.0, +10.3] pp, p=0.873). The two mechanisms disagree on 27% of routing assignments, establishing them as complements rather than substitutes; every DASE decision is accompanied by a machine-readable deliberation record. (2) Adaptive stopping, not injection bandwidth, drives accuracy gains. On AIME-300, bandwidth accounts for only 0.3 pp (ns); on GPQA-Extended, 4.4 pp bandwidth versus 5.0 pp stopping effect. DASE-Spatial ties Debate-Dense at its optimal budget using one-tenth the injection bandwidth and identifies that budget automatically; W=8 (65.0%) significantly outperforms W=4 (59.3%) on AIME-300 (adj p=0.0042). (3) Injection-based methods exhibit a retrospective accuracy-vs-inference inverted-U on both benchmarks; this pattern is hypothesis-generating for future work.

---


### 24. [Densification and forecasting of Sentinel-2 time series from multimodal SAR and Optical satellite data using deep generative models](https://arxiv.org/abs/2605.04239)

**<font color=#1a73e8>作者：</font>** Véronique Defonte, Dawa Derksen, Alexandre Constantin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical satellite image time series are extensively used in many Earth observation applications, including agriculture, climate monitoring, and land surface analysis. However, clouds and swath edges result in irregular sampling along the temporal dimension, limiting continuous monitoring. To address this issue, a growing body of work has focused on temporal densification and reconstruction of satellite image time series, with the objective of filling missing or cloud-contaminated observations within the temporal extent of the available data. While these approaches improve temporal continuity, they are inherently restricted to the reconstruction of the gaps within the observed time periods, and do not address the prediction of future observations. This work proposes a probabilistic deep learning framework for the densification and forecasting of Sentinel-2 time series by generating optical images at arbitrary past or future dates. The approach leverages multimodal satellite data by jointly exploiting Sentinel-2 optical and Sentinel-1 SAR observations. Unlike most existing works, we propose to focus on the uncertainty of the generated images. Experimental results demonstrate effective densification and forecasting, on sparse and temporally misaligned time series.

---


### 25. [Temporal Reasoning Is Not the Bottleneck: A Probabilistic Inconsistency Framework for Neuro-Symbolic QA](https://arxiv.org/abs/2605.04243)

**<font color=#1a73e8>作者：</font>** Tran Quang Liem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite significant advances, large language models (LLMs) continue to exhibit brittle performance on complex temporal reasoning tasks. This failure mode is widely attributed to inherent deficits in autoregressive logical deduction. In this paper, we challenge this prevailing narrative, demonstrating that temporal reasoning is not the fundamental bottleneck; rather, the locus of failure lies in unstructured text-to-event representation. We introduce a novel neuro-symbolic question-answering framework governed by a Probabilistic Inconsistency Signal (PIS) that explicitly isolates perceptual errors from reasoning failures. By lifting unstructured text into explicit event graphs and interval constraints, our architecture strictly decouples semantic extraction from a symbolic reasoning engine. To robustly detect structural breaks, the PIS elegantly unifies symbolic credal intervals with epistemic neural uncertainty extracted via Evidential Deep Learning on LLM hidden states. Empirical evaluations reveal a striking paradigm shift: when provided with correct structural representations, our system's explicit proof traces achieve perfect 1.0 accuracy (4000/4000) and strictly zero false positives/negatives on temporal arithmetic benchmarks. On broader, noise-injected QA settings, the framework maintains a competitive 75.1\% accuracy while enabling deterministic, step-level failure localization. Ultimately, by isolating the representation bottleneck from the reasoning substrate, this work reframes temporal QA from an algorithmic reasoning challenge to a structural alignment problem, charting a verifiable path forward for reliable neuro-symbolic AI.

---


### 26. [Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.04264)

**<font color=#1a73e8>作者：</font>** Diego F. Cuadros, Abdoul-Aziz Maiga, Helen Meskhidze 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Persistent memory is turning language-model-based agents from stateless participants in isolated interactions into state-bearing components of LLM-based multi-agent systems. As memory becomes durable, reloadable, and behavior-shaping across agents, sessions, or versions, a design question arises that is not captured by retrieval accuracy or access control alone: which candidate memories should become shared institutional state? This Viewpoint frames that problem as governed collaborative memory. We argue that memory governance functions as a selection regime, determining which memory variants persist, which remain private, and which are rejected, abstained from, or superseded. We distinguish ungoverned persistence, constitutional or hybrid selection, automatic metric-based selection, and human-ratified artificial selection, emphasizing that these regimes are not a ranking but a design choice over target properties. We then describe a layered architecture that separates agent-local memory, shared institutional memory, archive memory, and project-continuity memory, with provenance and version lineage making selection inspectable. Documented traces from one running LLM-based multi-agent ecosystem illustrate unmanaged false-memory persistence, ratified institutional memory, rejection and revision, identity-preserving expansion, and governance-as-learning. The contribution is a design agenda: persistent LLM-based multi-agent systems should evaluate memory not only for recall and performance, but also for provenance fidelity, selection traceability, epistemic quality, correction pathways, and role preservation.

---


### 27. [Explaining and Preventing Alignment Collapse in Iterative RLHF](https://arxiv.org/abs/2605.04266)

**<font color=#1a73e8>作者：</font>** Etienne Gauthier, Francis Bach, Michael I. Jordan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) typically assumes a static or non-strategic reward model (RM). In iterative deployment, however, the policy generates the data on which the RM is retrained, creating a feedback loop. Building on the Stackelberg game formulation of this interaction, we derive an analytical decomposition of the policy's true optimization gradient into a standard policy gradient and a parameter-steering term that captures the policy's influence on the RM's future parameters. We show that standard iterative RLHF, which drops this steering term entirely, suffers from alignment collapse: the policy systematically exploits the RM's blind spots, producing low-quality, high-reward outputs whose feedback reinforces the very errors it exploits. To mitigate this, we propose foresighted policy optimization (FPO), a mechanism-design intervention that restores the missing steering term by regularizing the policy's parameter-steering effect on RM updates. We instantiate FPO via a scalable first-order approximation and demonstrate that it prevents alignment collapse on both controlled environments and an LLM alignment pipeline using Llama-3.2-1B.

---


### 28. [Material Database Agent: A Multimodal Agentic Framework for Scientific Literature Mining](https://arxiv.org/abs/2605.04278)

**<font color=#1a73e8>作者：</font>** Achuth Chandrasekhar, Omid Barati Farimani, Radheesh Sharma Meda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Materials science workflows rely on structured and unstructured data from the vast body of available scientific literature. However, most of the experimental details remain buried in text, tables, graphs and figures. Thus, constructing databases that incorporate this data is a manual, time-consuming, and hard-to-scale process. Multimodal large language models have made it feasible to extract information from text and scientific figures with high speed and accuracy. This opens the possibility of an AI system that can create production-scale material databases. Material Database Agent (MDA) is a modular, multi-agent system architecture for converting research literature into structured databases. MDA accepts article PDFs as input, which are subsequently processed in parallel into markdown files and figures. Multiple sub-agents read these markdown files and figures in parallel to assemble sub-databases for each paper. These sub-databases are then compiled into a single tabular database by an agent. As opposed to using either a rule-based approach or a single-pass pipeline for extracting information, MDA is a specialized architecture for transforming the literature into a database in the field of materials science. More generally, this study provides a basis for positioning multimodal agentic information extraction as a viable means for constructing next-generation scientific databases from the primary literature.

---


### 29. [Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion](https://arxiv.org/abs/2605.04291)

**<font color=#1a73e8>作者：</font>** Tarun Kathuria, Sachin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a discrete diffusion-based language model using Glauber dynamics from statistical physics. Our main insight is that instead of trying to train a discrete state space diffusion model using Glauber dynamics with a uniform transition kernel as the forward process, one can set up an ``energy function'' based on pretrained causal/masked language models. When viewed as the stationary distribution, this energy function allows us to significantly improve the quality of the generated text. Incorporating UL2 as the pretrained model into our diffusion pipeline, we outperform prior diffusion based LMs and perform competitively with autoregressive models of comparable model sizes. Furthermore, our models are competitive with or outperform prior diffusion models and GPT-2 style auto-regressive models on zero-shot common sense reasoning tasks as well as planning and search tasks like Sudoku and Zebra puzzles.

---


### 30. [LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy](https://arxiv.org/abs/2605.04295)

**<font color=#1a73e8>作者：</font>** Hamed Karimi, Vaishali Meyappan, Reza Samavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs' overconfidence, particularly when hallucinating, poses a significant challenge for the deployment of the models in safety-critical settings and makes a reliable estimation of uncertainty necessary. Existing approaches for uncertainty quantification typically prioritize lexical or probabilistic measures; however, these techniques often ignore the semantic variance of different responses with similar meaning. In this paper, we propose Adaptive Conformal Semantic Entropy (ACSE), a method for estimating prompt-level uncertainty by adaptively measuring semantic dispersion in LLMs outputs. Our uncertainty scoring function is based on clustering semantic entropy of multiple diverse responses to the same prompt. The function adaptively adjusts the uncertainty score based on semantic features of each cluster. To ensure statistical reliability of our score, we use conformal calibration to apply a decision rule to accept/abstain the prompts, providing a finite-sample, distribution-free guarantee such that the error rate among the accepted responses remains bounded by a user-specified tolerance. Our extensive experimental evaluations using different LLMs and datasets, demonstrate that our approach consistently outperforms state-of-the-art uncertainty quantification baselines using discriminative performance, conformal guarantees, and probabilistic calibration indicators. As a highlight, for TriviaQA dataset, AUROC of our approach is 0.88 compared to 0.65 produced by the token entropy approach.

---


### 31. [Towards Self-Referential Analytic Assessment: A Profile-Based Approach to L2 Writing Evaluation with LLMs](https://arxiv.org/abs/2605.04298)

**<font color=#1a73e8>作者：</font>** Stefano Bannò, Kate Knill, Mark Gales  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated essay scoring (AES) research often relies on rank-based correlation metrics to validate analytic assessment. However, such metrics obscure both intrinsic intercorrelations among analytic dimensions that arise from the structure of writing proficiency itself and halo effects, whereby holistic impressions bleed into fine-grained component scores. As a result, high correlations may mask a system's true diagnostic behaviour. In this study, we propose a novel self-referential assessment evaluation framework that focuses on identifying intra-learner strengths and weaknesses rather than assessing inter-learner rankings. We conduct experiments on the publicly available ICNALE GRA, a uniquely dense second-language writing dataset annotated holistically and analytically by up to 80 trained raters. To obtain reliable reference scores, we apply two-facet Rasch modelling to calibrate rater severity and derive fair average scores across ten analytic aspects and holistic proficiency. We compare the analytic scoring performance of human operational raters and three large language models (LLMs) in a zero-shot setting. Our results show that LLMs tend to outperform single human raters in identifying relative weaknesses (negative feedback) across several proficiency aspects, while human raters remain stronger at identifying relative strengths (positive feedback). Overall, our findings highlight the limitations of rank-based evaluation for analytic assessment and demonstrate the value of intra-learner, profile-based methods for assessing and deploying LLMs in AES.

---


### 32. [LUCAS-MEGA: A Large-Scale Multimodal Dataset for Representation Learning in Soil-Environment Systems](https://arxiv.org/abs/2605.04323)

**<font color=#1a73e8>作者：</font>** Kuangdai Leng, Simon Jeffery, Panos Panagos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding soil is fundamental to agriculture, carbon cycling, and environmental sustainability, yet progress is limited by fragmented and heterogeneous datasets that constrain modeling to small-scale predictive settings rather than high-dimensional representation learning. We introduce LUCAS-MEGA, a large-scale multimodal dataset constructed through systematic data fusion of European soil-environment observations, with the LUCAS survey as its backbone. The fused dataset comprises over 70,000 samples and more than 1,000 features spanning physical, chemical, environmental, biological, and visual attributes, aggregated from 68 source datasets. To enable integration at scale, we develop SoilFuser, a multi-agent, human-in-the-loop data fusion pipeline that standardizes heterogeneous data formats and measurement protocols, resolves inconsistencies and invalid entries (e.g., unit inconsistencies, codebook mismatches, and erroneous values), incorporates natural language annotations, and harmonizes multimodal attributes and metadata into a unified, machine learning-ready feature space. The resulting dataset captures key characteristics of real-world soil observations, including multimodality, uneven feature coverage, and heterogeneous uncertainty. To demonstrate the usability of LUCAS-MEGA for data-driven modeling, we pretrain a multimodal tabular transformer (SoilFormer) using a self-supervised objective based on feature masking, achieving stable training, strong predictive performance, and representations that support uncertainty-aware prediction. We further show that the learned representations recover relationships consistent with established soil processes. LUCAS-MEGA is released with open access and is accompanied by composable, agent-friendly APIs that support structured querying and data-driven workflows.

---


### 33. [Budgeted LoRA: Distillation as Structured Compute Allocation for Efficient Inference](https://arxiv.org/abs/2605.04341)

**<font color=#1a73e8>作者：</font>** Mohammed Sabry, Anya Belz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study distillation for large language models under explicit compute constraints, with the goal of producing student models that are not only cheaper to train, but structurally efficient at inference time. While prior approaches to parameter-efficient distillation, such as LoRA, reduce adaptation cost, they leave the dense backbone unchanged and therefore fail to deliver meaningful inference savings. We propose Budgeted LoRA, a distillation framework that treats model compression as a structured compute allocation problem. Instead of using a fixed student architecture, we introduce a global compute budget that sets the final target fraction of dense computation retained. Under this constraint, the model redistributes capacity across dense and low-rank pathways via (i) module-level dense retention coefficients, (ii) adaptive low-rank allocation, and (iii) post-training compression that selectively removes, approximates, or preserves dense components. This formulation yields a family of students controlled by a single budget dial. Empirically, Budgeted LoRA matches standard LoRA perplexity at a moderate budget with a 1.74x compressed-module speedup; at an aggressive budget it achieves a 4.05x speedup with moderate perplexity degradation, and it preserves higher accuracy on function-style in-context learning probes. These results suggest that, under compute-constrained distillation, retaining behavior is less about matching perplexity or removing more parameters than it is about controlling how dense computation is transferred to low-rank pathways.

---


### 34. [Probing Structural Mathematical Reasoning in Language Models with Algebraic Trapdoors](https://arxiv.org/abs/2605.04352)

**<font color=#1a73e8>作者：</font>** Igor Rivin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a benchmark suite for evaluating structural mathematical reasoning in language models, built on subgroup-construction problems in SL(3, Z) with cryptographic-style verifier-prover asymmetry. Each instance presents a finitely generated subgroup as a list of integer matrices and asks for an arithmetic invariant -- index, surjection-at-prime, or membership -- that the construction-time information (N, K) pins down in O(1) closed form, but that the solver, lacking that information, must derive by either Aschbacher-classification analysis or by a membership query in SL(3, Z) of unknown decidability. The benchmark therefore distinguishes models with internalized algebraic priors (Aschbacher classes, McLaughlin's theorem, Property (T), the congruence subgroup property) from models that rely on general-purpose computation. We report empirical results across five representative reasoning traces from two state-of-the-art models. The headline result: on the index variant, one model spent 152 minutes of reasoning, explicitly identified the kernel-side membership question as the bottleneck, attempted constructive verification, and abstained with "DON'T KNOW" rather than commit to its computed cokernel candidate -- demonstrating calibrated meta-cognition on the open-decidability boundary that the benchmark was designed to probe. We argue that the benchmark exposes a four-way classification of model behavior (commit-correct, commit-wrong, abstain-correct, abstain-wrong) that standard answer-key scoring conflates.

---


### 35. [Efficiently Aligning Language Models with Online Natural Language Feedback](https://arxiv.org/abs/2605.04356)

**<font color=#1a73e8>作者：</font>** Christine Ye, Joe Benton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has been used to elicit impressive performance from language models in many domains. But, broadly beneficial deployments of AI may require us to train models with strong capabilities in "fuzzy", hard-to-supervise domains. In this paper, we develop methods to align language models in fuzzy domains where human experts are still able to provide high-quality supervision signal, but only for a small number of model outputs, using online natural language feedback. Specifically, we train models by iteratively optimizing against proxy reward signals, stopping at the point of over-optimization, collecting fresh expert supervision, and updating the proxy reward. We construct proxy reward models from language models using in-context learning (ICL) and fine-tuning. We test our methods by eliciting creative writing and alignment research capabilities in Qwen3-8B and Haiku 4.5 respectively. For Qwen3-8B, ICL methods recover up to 35% of performance with 50x fewer expert samples, while fine-tuning methods recover 80% with up to 20x fewer samples and 100% with 3x fewer samples. For Haiku 4.5, ICL methods recover up to 35% of performance with 30x fewer samples, and fine-tuning methods recover 100% with 10x fewer samples. Our results suggest that online natural language feedback can substantially improve the data efficiency of expert supervision.

---


### 36. [Mitigating Label Shift in Tabular In-Context Learning via Test-Time Posterior Adjustment](https://arxiv.org/abs/2605.04363)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jaehoon Lee, Jun Seo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TabPFN has recently gained attention as a foundation model for tabular datasets, achieving strong performance by leveraging in-context learning on synthetic data. However, we find that TabPFN is vulnerable to label shift, often overfitting to the majority class in the training dataset. To address this limitation, we propose DistPFN, the first test-time posterior adjustment method designed for tabular foundation models. DistPFN rescales predicted class probabilities by downweighting the influence of the training prior (i.e., the class distribution of the context) and emphasizing the contribution of the model's predicted posterior, without architectural modification or additional training. We further introduce DistPFN-T, which incorporates temperature scaling to adaptively control the adjustment strength based on the discrepancy between prior and posterior. We evaluate our methods on over 250 OpenML datasets, demonstrating substantial improvements for various TabPFN-based models in classification tasks under label shift, while maintaining strong performance in standard settings without label shift. Code is available at this repository: this https URL.

---


### 37. [Demystifying Manifold Constraints in LLM Pre-training](https://arxiv.org/abs/2605.04418)

**<font color=#1a73e8>作者：</font>** Kang An, Jiaxiang Li, Donald Goldfarb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The empirical success of large language model (LLM) pre-training relies heavily on heuristic stabilization techniques, such as explicit normalization layers and weight decay. While recent constrained optimization approaches that explicitly restrict weights may improve numerical stability and performance, the mechanism and motivation for adding constraints still remain elusive. This paper systematically demystifies the role of explicit manifold constraints in LLM pre-training. By introducing the Msign-Aligned Constrained Riemannian Optimizer (MACRO)-a provably convergent, single-loop optimization framework-our study disentangles weight regularization heuristics from interacting mechanisms like RMS normalization and decoupled weight decay. Theoretical analyses and comprehensive empirical evaluations reveal that manifold constraints independently bound forward activation scales and enforce stable rotational equilibrium, thereby subsuming the roles of these heuristic mechanisms. Evaluations on large-scale LLM architectures demonstrate that MACRO achieves highly competitive performance while rigorously preserving the theoretical guarantees of exact Riemannian optimization.

---


### 38. [Joint Semantic Token Selection and Prompt Optimization for Interpretable Prompt Learning](https://arxiv.org/abs/2605.04425)

**<font color=#1a73e8>作者：</font>** Yating Wang, Yaqi Zhao, Yongshun Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP achieve strong visual-textual alignment, but often suffer from overfitting and limited interpretability when adapted through continuous prompt learning. While discrete prompt optimization improves interpretability, it usually depends on large external models, leading to high computational costs and limited scalability. In this paper, we propose Interpretable Prompt Learning (IPL), a hybrid framework that alternates between discrete semantic token selection and continuous prompt optimization. Specifically, IPL formulates semantic token selection as an approximate submodular optimization problem, encouraging tokens that are both human-understandable and semantically diverse. It further adopts an alternating optimization strategy to integrate discrete token selection with continuous prompt tuning, improving interpretability while preserving adaptability to downstream tasks. Our framework is plug-and-play, allowing seamless integration with existing prompt learning methods. Extensive experiments on multiple benchmarks show that IPL consistently improves both interpretability and accuracy across five representative prompt learning methods, providing an effective and scalable extension to existing frameworks.

---


### 39. [Deep Reprogramming Distillation for Medical Foundation Models](https://arxiv.org/abs/2605.04447)

**<font color=#1a73e8>作者：</font>** Siyuan Du, Yuhang Zhou, Haolin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical foundation models pre-trained on large-scale datasets have shown powerful versatile performance. However, when adapting medical foundation models for specific medical scenarios, it remains the inevitable challenge due to the gap induced by the discrepancy between pre-training and downstream tasks, the real-world computation, and speed constraints. Relevant techniques that probably handle this challenge more or less suffer from some intrinsic limitations. For example, knowledge distillation (KD) assumes that teacher and student models share the same task, training strategy, and model structure family, while prevalent parameter-efficient fine-tuning (PEFT) fails to achieve personalized and lightweight deployment. Even the combination of PEFT and KD still struggles to resolve model structures and training strategies inconsistencies between teacher and student models, leading to inefficient knowledge transfer. In this study, we propose a novel framework called Deep Reprogramming Distillation (DRD) to combat the general adaptation challenge. Specifically, DRD introduces the novel reprogramming module that on the one side overcomes the domain and task discrepancy between pretraining and downstream scenarios, and on the other side builds the student-friendly efficient distillation from foundation models to lightweight downstream models. Furthermore, to mitigate variability under different training conditions, we design a centered kernel alignment (CKA) distillation method to promote robust knowledge transfer. Empirical results show that DRD surpasses previous PEFT and KD methods across 18 medical downstream tasks under different foundation models, covering various scenarios including 2D/3D classification and 2D/3D segmentation.

---


### 40. [Stabilizing LLM Supervised Fine-Tuning via Explicit Distributional Control](https://arxiv.org/abs/2605.04468)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Changzhi Sun, Yuanbin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training large language models (LLMs) often suffers from catastrophic forgetting, where improvements on a target objective degrade previously acquired capabilities. Recent evidence suggests that this phenomenon is primarily driven by excessive distributional drift during optimization. Motivated by this perspective, we propose Anchored Learning, a simple framework that explicitly controls distributional updates during offline fine-tuning via a dynamically evolving moving anchor. Instead of matching a fixed reference distribution, the anchor interpolates between the current model and a frozen reference to construct an intermediate target that the model distills toward, transforming global fine-tuning into a sequence of local trust-region updates in distribution space. Theoretically, we prove this anchor-based update admits a linear KL-divergence upper bound per iteration, ensuring a stable transition between model distributions. Extensive experiments on iGSM, MedCalc, and IFEval show that Anchored Learning consistently lies on the Pareto frontier of gain-stability trade-offs, achieving near-optimal performance improvements while substantially reducing degradation compared to strong baselines. For example, while standard SFT suffers from over 53% performance degradation on iGSM and MedCalc, Anchored Learning slashes this drop to under 5% while maintaining near-optimal gains (e.g., 75.2% on iGSM).

---


### 41. [CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies](https://arxiv.org/abs/2605.04470)

**<font color=#1a73e8>作者：</font>** Keyu Chen, Nanfei Ye, Yida Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-loop imitation learning has advanced modern autonomous driving policy architectures, but closed-loop deployment remains vulnerable to policy-induced distribution shift. Existing post-training paradigms exhibit fundamental trade-offs: closed-loop RL fine-tuning provides grounded feedback from executed actions but is constrained by the sparsity of informative events, whereas counterfactual fine-tuning provides dense supervision over candidate futures but inherits bias from imperfect future estimates. We introduce Counterfactual-to-Interactive Reinforcement Fine-Tuning (CRAFT), an on-policy framework that formulates closed-loop post-training as proxy-residual optimization. CRAFT uses group-normalized counterfactual advantages as a dense proxy for real closed-loop advantages and aligns this proxy with the closed-loop world through grounded residual correction from interaction-critical events. To stabilize adaptation, CRAFT regularizes the online policy toward an EMA teacher via asymmetric KL self-distillation. Theoretically, CRAFT decomposes the real closed-loop policy gradient into proxy and residual terms under the same visited-state distribution, reducing residual variance with an aligned proxy while mitigating proxy bias through grounded residual approximation. Empirically, CRAFT achieves the strongest closed-loop gains on Bench2Drive across hierarchical planning, vision-language-action, and vocabulary-scoring architectures. Ablations, scaling behavior, stability analyses, and transfer results further validate the complementary roles of dense counterfactual proxy and grounded residual correction. Project page: this https URL.

---


### 42. [Automated Formal Proofs of Combinatorial Identities via Wilf-Zeilberger Guidance and LLMs](https://arxiv.org/abs/2605.04472)

**<font color=#1a73e8>作者：</font>** Beibei Xiong, Hangyu Lv, Junqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automating formal proofs of combinatorial identities is challenging for LLM-based provers, as long-horizon proof planning is required and unconstrained search quickly explodes. Symbolic methods such as the Wilf-Zeilberger (WZ) method can achieve a mechanized proof of combinatorial identities by constructing special auxiliary functions and demonstrating that they satisfy specific recurrence relations. We propose WZ-LLM, a neuro-symbolic framework that turns WZ proof plans into executable proof sketches in Lean 4 and uses an LLM-based prover to discharge the resulting machine-checkable subgoals. We also train a dedicated WZ-Prover via a Lean-kernel-verified bootstrapping loop with expert-verified iteration, followed by DAPO-based refinement. Experiments show that WZ-LLM achieves a 34% proof success rate on LCI-Test (100 classic combinatorial identities), outperforming strong baselines such as DeepSeek-V3 and Goedel-Prover-V2, and delivering consistent gains on CombiBench and PutnamBench-Comb. These results indicate that our framework provides two complementary strengths: improved direct proving for identities beyond the scope of WZ, and substantially higher end-to-end success when WZ sketches guide a specialized prover.

---


### 43. [Data-dependent Exploration for Online Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2605.04477)

**<font color=#1a73e8>作者：</font>** Zhen-Yu Zhang, Yuting Tang, Jiandong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning from human feedback (RLHF) has emerged as a promising paradigm for aligning large language models (LLMs) by continuously collecting new preference feedback during training. A foundational challenge in this setting is exploration, which requires algorithms that enable the LLMs to generate informative comparisons that improve sample-efficiency in online RLHF. Existing exploration strategies often derive bonuses via on-policy expectations, which are difficult to estimate reliably from the limited historical preference data available during training; as a result, the policy can prematurely down-weight under-explored regions that may contain high-value behaviors. In this paper, we propose data-dependent exploration for preference optimization (DEPO), a simple and scalable method that leverages historical data to construct an extra uncertainty bonus for high-uncertainty regions, encouraging exploration toward potentially high-value data. Theoretically, we provide a data-dependent regret bound for the proposed algorithm, showing that it adapts to the hardness of the learning task itself and can be tighter than worst-case bounds in practice. Empirically, the proposed method consistently outperforms strong baselines across benchmarks, demonstrating improved sample efficiency.

---


### 44. [How Does Thinking Mode Change LLM Moral Judgments? A Controlled Instant-vs-Thinking Comparison Across Five Frontier Models](https://arxiv.org/abs/2605.04488)

**<font color=#1a73e8>作者：</font>** Sai Sourabh Madur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate whether enabling provider-exposed reasoning mode changes moral judgments within the same model checkpoint. Across 100 moral-judgment scenarios and five frontier reasoning-trained LLMs (Claude Sonnet 4.6, GPT 5.5, Gemini 3 Flash, DeepSeek V3.1, and Qwen3.5 397B), aggregate binary-verdict agreement remains high and statistically indistinguishable between instant and thinking modes (Krippendorff's alpha = 0.78 vs. 0.79). However, disagreement is concentrated in 21 model-disputed scenarios, where instant-mode agreement is near chance (alpha = 0.08). On these scenarios, reasoning directionally narrows cross-model disagreement, increasing mean pairwise agreement from 5.4 to 6.7 out of 10. Reasoning also reduces demographic-judgment inconsistency in three of five models and does not increase it for any model. Across all five model families, reasoning changes self-labeled ethical frameworks more often than binary verdicts.

---


### 45. [Towards General Preference Alignment: Diffusion Models at Nash Equilibrium](https://arxiv.org/abs/2605.04494)

**<font color=#1a73e8>作者：</font>** Jiaming Hu, Jiamu Bai, Haoyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has been popular for aligning text-to-image (T2I) diffusion models with human preferences. As a mainstream branch of RLHF, Direct Preference Optimization (DPO) offers a computationally efficient alternative that avoids explicit reward modeling and has been widely adopted in diffusion alignment. However, existing preference-based methods for diffusion alignment still rely on reward-induced preference signals and typically assume that human preferences can be adequately modeled by the Bradley--Terry (BT) model, which may fail to capture the full complexity of human preferences. In this paper, we formulate diffusion alignment from a game-theoretic perspective. We propose Diffusion Nash Preference Optimization (Diff.-NPO), an intuitive general preference framework for diffusion alignment. Diff.-NPO encourages the current policy to play against itself to achieve self improvement and lead to a better alignment. Empirically, we demonstrate the effectiveness of Diff.-NPO on the text-to-image generation task via various metrics. Diff.-NPO consistently outperforms existing preference-based diffusion alignment methods.

---


### 46. [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](https://arxiv.org/abs/2605.04495)

**<font color=#1a73e8>作者：</font>** Zhipeng Song, Yizhi Zhou, Xiangyu Kong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) depends on document ranking to provide useful evidence for generation, but conventional reranking methods mainly optimize query-document relevance rather than generation usefulness. A relevant document may still introduce noise, while a lower-ranked document may better reduce the generator's uncertainty. We propose CAR (Confidence-Aware Reranking), a query-guided, training-free, and plug-and-play reranking framework that uses generator confidence change as a document usefulness signal. CAR estimates confidence through the semantic consistency of multiple sampled answers under query-only and query-document conditions. Documents that significantly increase confidence are promoted, those that decrease confidence are demoted, and uncertain cases preserve the baseline order, while a query-level gate avoids unnecessary intervention on already confident queries. Experiments on four BEIR datasets show that CAR consistently improves NDCG@5 across sparse and dense retrievers, LLM-based and supervised rerankers, and four LLM backbones. Notably, CAR improves the YesNo reranker by 25.4 percent on average under Contriever retrieval, and its ranking gains strongly correlate with downstream generation F1 improvements, achieving Spearman rho = 0.964.

---


### 47. [SCOUT: Active Information Foraging for Long-Text Understanding with Decoupled Epistemic States](https://arxiv.org/abs/2605.04496)

**<font color=#1a73e8>作者：</font>** Zhenliang Zhang, Wenqing Wang, Yong Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-Text Understanding (LTU) at million-token scale requires balancing reasoning fidelity with computational efficiency. Frontier long-context LLMs can process millions of token contexts end-to-end, but they suffer from high token consumption and attention dilution. In parallel, specialized LTU agents often sacrifice fidelity through task-agnostic abstractions like graph construction or indexing. We identify a key insight for LTU: query-relevant information is typically sparse relative to the full document, so effective reasoning should rely on a query-sufficient subset rather than the entire context. To address this, we propose SCOUT, a new paradigm for LTU that shifts from passive processing to active information foraging. It treats the document as an explorable environment and answers from a compact, provenance-grounded epistemic state. Guided by state-level gap diagnosis, SCOUT adaptively alternates between coarse-to-fine exploration and anchored state updates that progressively contract its epistemic state toward query sufficiency. Experiments show that SCOUT matches state-of-the-art proprietary models while reducing token consumption by up to 8x. Moreover, SCOUT remains stable as context length scales, substantially alleviating the practical cost-performance trade-off.

---


### 48. [DiffCap-Bench: A Comprehensive, Challenging, Robust Benchmark for Image Difference Captioning](https://arxiv.org/abs/2605.04503)

**<font color=#1a73e8>作者：</font>** Yuancheng Wei, Haojie Zhang, Linli Yao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image Difference Captioning (IDC) generates natural language descriptions that precisely identify differences between two images, serving as a key benchmark for fine-grained change perception, cross-modal reasoning, and image editing data construction. However, existing benchmarks lack diversity and compositional complexity, and standard lexical-overlap metrics (e.g., BLEU, METEOR) fail to capture semantic consistency or penalize hallucinations, which together prevent a comprehensive and robust evaluation of multimodal large language models (MLLMs) on IDC. To address these gaps, we introduce DiffCap-Bench, a comprehensive IDC benchmark covering ten distinct difference categories to ensure diversity and compositional complexity. Furthermore, we propose an LLM-as-a-Judge evaluation protocol grounded in human-validated Difference Lists, enabling a robust assessment of models' ability to both capture and describe visual changes. Through extensive evaluation of state-of-the-art MLLMs, we reveal significant performance gaps between proprietary and open-source models, highlight the critical importance of reasoning capability, and identify clear limitations in model scaling. Our framework also demonstrates strong alignment with human expert judgments and strong correlation with downstream image editing data construction quality. These findings establish DiffCap-Bench as both a reliable IDC evaluation framework and a practical predictor of downstream utility. The benchmark and code will be made publicly available to support further research.

---


### 49. [Distilling Bayesian Belief States into Language Models for Auditable Negotiation](https://arxiv.org/abs/2605.04507)

**<font color=#1a73e8>作者：</font>** Zongqi Cui, Baihan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negotiation agents must infer what their counterpart values, update those beliefs over dialogue turns, and choose actions under uncertainty. End-to-end large language models (LLMs) can imitate negotiation dialogue, but their opponent beliefs are usually implicit and difficult to inspect. We propose BOND (Bayesian Opponent-belief Negotiation Distillation), a framework for auditable negotiation. BOND consists of an LLM-based Bayesian teacher that scores dialogue contexts against the six possible opponent priority orderings, updates a posterior over those orderings, and uses the posterior for menu-based decision making, as well as a smaller 8B student language model that emits both negotiation actions and normalized posterior beliefs as tagged text. In the CaSiNo negotiation dataset, BOND outperforms the state-of-the-art and achieves mean Brier score 0.085 over opponent-priority posteriors. The distilled student preserves much of this belief signal, achieving Brier 0.114, below the uniform six-ordering reference of 5/36, approximately 0.139. Compared with a 70B structured-CoT baseline, the significantly smaller 8B student model yields substantially better elicited posterior calibration. We further showcase auditability through posterior trajectories, belief-versus-policy error decomposition, and posterior-prefix interventions. These diagnostics reveal that distillation preserves a scoreable belief report more strongly than causal belief-conditioned control, making weak belief-action coupling visible, not hidden.

---


### 50. [From Priors to Perception: Grounding Video-LLMs in Physical Reality](https://arxiv.org/abs/2605.04515)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Chaofan Gan, Shijie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Video Large Language Models (Video-LLMs) excel in general understanding, they exhibit systematic deficits in fine-grained physical reasoning. Existing interventions not only suffer from limited generalization but fundamentally conflate generative artifacts with genuine physical fallacies. Furthermore, we find that models fail systematically not only in anti-physics anomalies but also in counter-intuitive scenarios where visual facts contradict statistical expectations. Accordingly, we propose the Unified Attribution Theory: this dual failure stems not from perception deficiency, but from Semantic Prior Dominance -- the reasoning mechanism is deeply hijacked by internal narrative scripts. To address this, we construct the Programmatic Adversarial Curriculum (PACC), the first high-fidelity adversarial video dataset synthesized based on physical laws, thoroughly decoupling visual artifacts from logical errors. Concurrently, we design the Visual-Anchored Reasoning Chain (VARC) to force models to explicitly ground their judgments in low-level visual facts prior to logical adjudication. Experiments demonstrate that without invasive architectural modifications, standard LoRA fine-tuning with the PACC curriculum effectively neutralizes prior interference in state-of-the-art (SOTA) models, yielding a substantial leap in physical reasoning capabilities.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-126](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
