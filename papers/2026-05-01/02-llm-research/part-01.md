# 🧠 大模型相关研究 | 2026年05月01日

> 本类共 **75** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-75](./part-02.md)

---

### 1. [Analysing Lightweight Large Language Models for Biomedical Named Entity Recognition on Diverse Ouput Formats](https://arxiv.org/abs/2604.25920)

**<font color=#1a73e8>作者：</font>** Pierre Epron, Adrien Coulet, Mehwish Alam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their strong linguistic capabilities, Large Language Models (LLMs) are computationally demanding and require substantial resources for fine-tuning, which is unadapted to privacy and budget constraints of many healthcare settings. To address this, we present an experimental analysis focused on Biomedical Named Entity Recognition using lightweight LLMs, we evaluate the impact of different output formats on model performance. The results reveal that lightweight LLMs can achieve competitive performance compared to the larger models, highlighting their potential as lightweight yet effective alternatives for biomedical information extraction. Our analysis shows that instruction tuning over many distinct formats does not improve performance, but identifies several format consistently associated with better performance.

---


### 2. [One Word at a Time: Incremental Completion Decomposition Breaks LLM Safety](https://arxiv.org/abs/2604.25921)

**<font color=#1a73e8>作者：</font>** Samee Arif, Naihao Deng, Zhijing Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are trained to refuse harmful requests, yet they remain vulnerable to jailbreak attacks that exploit weaknesses in conversational safety mechanisms. We introduce Incremental Completion Decomposition (ICD), a trajectory-based jailbreak strategy that elicits a sequence of single-word continuations related to a malicious request before eliciting the full response. In addition, we propose variants of ICD by manually picking or model-generating the one-word continuation, as well as prefilling when eliciting the full model response in the final step. We systematically evaluate these variants across a broad set of model families, demonstrating superior Attack Success Rate (ASR) on AdvBench, JailbreakBench, and StrongREJECT compared to existing methods. In addition, we provide a theoretical account of why ICD is effective and present mechanistic evidence that successful attack trajectories systematically suppress refusal-related representations and shift activations away from safety-aligned states.

---


### 3. [Generative AI-Based Virtual Assistant using Retrieval-Augmented Generation: An evaluation study for bachelor projects](https://arxiv.org/abs/2604.25924)

**<font color=#1a73e8>作者：</font>** Dumitru Verşebeniuc, Martijn Elands, Sara Falahatkar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models have been increasingly employed in the creation of Virtual Assistants due to their ability to generate human-like text and handle complex inquiries. While these models hold great promise, challenges such as hallucinations, missing information, and the difficulty of providing accurate and context-specific responses persist, particularly when applied to highly specialized content domains. In this paper, we focus on addressing these challenges by developing a virtual assistant designed to support students at Maastricht University in navigating project-specific regulations. We propose a virtual assistant based on a Retrieval-Augmented Generation system that enhances the accuracy and reliability of responses by integrating up-to-date, domain-specific knowledge. Through a robust evaluation framework and real-life testing, we demonstrate that our virtual assistant can effectively meet the needs of students while addressing the inherent challenges of applying Large Language Models to a specialized educational context. This work contributes to the ongoing discourse on improving LLM-based systems for specific applications and highlights areas for further research.

---


### 4. [MATH-PT: A Math Reasoning Benchmark for European and Brazilian Portuguese](https://arxiv.org/abs/2604.25926)

**<font color=#1a73e8>作者：</font>** Tiago Teixeira, Ana Carolina Erthal, Juan Belieni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The use of large language models (LLMs) for complex mathematical reasoning is an emergent area of research, with fast progress in methods, models, and benchmark datasets. However, most mathematical reasoning evaluations exhibit a significant linguistic bias, with the vast majority of benchmark datasets being exclusively in English or (at best) translated from English. We address this limitation by introducing {\sc Math-PT}, a novel dataset comprising 1,729 mathematical problems written in European and Brazilian Portuguese. {\sc Math-PT} is curated from a variety of high-quality native sources, including mathematical Olympiads, competitions, and exams from Portugal and Brazil. We present a comprehensive benchmark of current state-of-the-art LLMs on {\sc Math-PT}, revealing that frontier reasoning models achieve strong performance in multiple choice questions compared to open weight models, but that their performance decreases for questions with figures or open-ended questions. To facilitate future research, we release the benchmark dataset and model outputs.

---


### 5. [Information Extraction from Electricity Invoices with General-Purpose Large Language Models](https://arxiv.org/abs/2604.25927)

**<font color=#1a73e8>作者：</font>** Javier Gómez, Javier Sánchez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information extraction from semi-structured business documents remains a critical challenge for enterprise management. This study evaluates the capability of general-purpose Large Language Models to extract structured information from Spanish electricity invoices without task-specific fine-tuning. Using a subset of the IDSEM dataset, we benchmark two architecturally distinct models, Gemini 1.5 Pro and Mistral-small, across 19 parameter configurations and 6 prompting strategies. Our experimental framework treats prompt engineering as the primary experimental variable, comparing zero-shot baselines against increasingly sophisticated few-shot approaches and iterative extraction strategies. Results demonstrate that prompt quality dominates over hyperparameter tuning: the F1-score variation across all parameter configurations is marginal, while the gap between zero-shot and the best few-shot strategy exceeds 19 percentage points. The best configuration (few-shot with cross-validation) achieves an F1-score of 97.61% for Gemini and 96.11% for Mistral-small, with document template structure emerging as the primary determinant of extraction difficulty. These findings establish that prompt design is the critical lever for maximizing extraction fidelity in LLM-based document processing, thereby providing an empirical framework for integrating general-purpose LLMs into business document automation.

---


### 6. [CogRAG+: Cognitive-Level Guided Diagnosis and Remediation of Memory and Reasoning Deficiencies in Professional Exam QA](https://arxiv.org/abs/2604.25928)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Zilong Wang, Zhaoyan Ming  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Professional domain knowledge underpins human civilization, serving as both the basis for industry entry and the core of complex decision-making and problem-solving. However, existing large language models often suffer from opaque inference processes in which retrieval and reasoning are tightly entangled, causing knowledge gaps and reasoning inconsistencies in professional tasks. To address this, we propose CogRAG+, a training-free framework that decouples and aligns the retrieval-augmented generation pipeline with human cognitive hierarchies. First, we introduce Reinforced Retrieval, a judge-driven dual-path strategy with fact-centric and option-centric paths that strengthens retrieval and mitigates cascading failures caused by missing foundational knowledge. We then develop cognition-stratified Constrained Reasoning, which replaces unconstrained chain-of-thought generation with structured templates to reduce logical inconsistency and generative redundancy. Experiments on two representative models, Qwen3-8B and Llama3.1-8B, show that CogRAG+ consistently outperforms general-purpose models and standard RAG methods on the Registered Dietitian qualification exam. In single-question mode, it raises overall accuracy to 85.8\% for Qwen3-8B and 60.3\% for Llama3.1-8B, with clear gains over vanilla baselines. Constrained Reasoning also reduces the unanswered rate from 7.6\% to 1.4\%. CogRAG+ offers a robust, model-agnostic path toward training-free expert-level performance in specialized domains.

---


### 7. [LLMs Generate Kitsch](https://arxiv.org/abs/2604.25929)

**<font color=#1a73e8>作者：</font>** Xenia Klinge, Stefan Ortlieb, Alexander Koller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to generate pictures, texts, music, videos, and other works that have traditionally required human creativity. LLM-generated artifacts are often rated better than human-generated works in controlled studies. At the same time, they can come across as generic and hollow. We propose to resolve this tension by arguing that LLMs systematically generate kitsch, and that this is a consequence of the way in which they are trained. We also show empirically that readers perceive LLM-generated stories as kitschier, if we control for their definition of "kitsch". We discuss implications for the design of future studies and for creative tasks such as research and coding.

---


### 8. [Anchored Confabulation: Partial Evidence Non-Monotonically Amplifies Confident Hallucination in LLMs](https://arxiv.org/abs/2604.25931)

**<font color=#1a73e8>作者：</font>** Ashish Balkishan Lathkar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify a previously unknown calibration property of large language models: providing one confirmed intermediate fact toward a multi-step reasoning chain increases the model's confident-wrong-answer rate before full evidence eliminates it. We call this anchored confabulation: a partial anchor commits the model to confident parametric completion of remaining reasoning steps. We formalize it as Parametric Hallucination Confidence (PHC) and establish it across six lines of evidence including a causal injection experiment (PHC 0.613 to 0.656 to 0.595 to 0.536, N=160) and capability scaling across five model families (Spearman rho=0.900, p=0.037). The Anchoring Threshold Law k*(n)=floor(n/3) predicts PHC amplification by hop depth with four confirmed predictions. Applied to RAG routing, a LearnedRouter exploiting PHC closes 81.1% of the oracle performance gap (macro F1=0.426, p<1e-6) on 1,800 queries across four benchmarks with no model fine-tuning and 50x fewer labels than prior RL-based work. An epistemic humility prompt reduces the PHC spike by -0.118; explicit self-rating (PHC=0.684, p<0.001) outperforms lexical confidence as a routing signal.

---


### 9. [A Multimodal and Explainable Machine Learning Approach to Diagnosing Multi-Class Ejection Fraction from Electrocardiograms](https://arxiv.org/abs/2604.25942)

**<font color=#1a73e8>作者：</font>** Catherine Ning, Yu Ma, Cindy Beini Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Left ventricular ejection fraction (LVEF) assessment depends on echocardiography, limiting access in primary care and resource-constrained settings. We developed a multimodal machine-learning framework that combines engineered 12-lead ECG timeseries features with structured EHR variables to classify LVEF into four clinically used strata: normal (>50%), mildly reduced (40-50%), moderately reduced (30-40%), and severely reduced (<30%). To support model explainability, we identified the most influential ECG and EHR features via SHAP attributions. Using retrospective data from Hartford HealthCare, we trained XGBoost models on 36,784 ECG-echocardiogram pairs from 30,952 outpatients and evaluated temporal generalizability on 19,966 ECGs from a subsequent period. The multimodal model achieved one-vs-rest AUROCs of 0.95 (severe), 0.92 (moderate), 0.82 (mild), and 0.91 (normal), outperforming ECG-only and EHR-only baselines, and maintained performance under temporal validation. This work supports ECG-based, multimodal LVEF stratification as a practical screening and triage aid to prioritize confirmatory imaging where resources are limited.

---


### 10. [Evaluating the Alignment Between GeoAI Explanations and Domain Knowledge in Satellite-Based Flood Mapping](https://arxiv.org/abs/2604.26051)

**<font color=#1a73e8>作者：</font>** Hyunho Lee, Wenwen Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing number of satellites has improved the temporal resolution of Earth observation, making satellite-based flood mapping a promising approach for operational flood monitoring. Deep learning-based approaches for flood mapping using satellite imagery, an important application within Geospatial Artificial Intelligence (GeoAI), have shown improved predictive performance by learning complex spatial and spectral patterns from large volumes of remote sensing data. However, the opaque decision-making processes of deep learning models remain a major barrier to their integration into critical scientific and operational workflows. This highlights the need for a systematic assessment of whether model explanations align with established domain knowledge in remote sensing. To address this research gap, this study introduces the ADAGE (Alignment between Domain Knowledge And GeoAI Explanation Evaluation) framework. The proposed framework is designed to systematically evaluate how well explanations of deep learning models align with established remote sensing knowledge, particularly regarding the distinctive spectral properties of the Earth's surface. The ADAGE framework employs Channel-Group SHAP (SHapley Additive exPlanations) method to estimate the contributions of grouped input channels to pixel-level predictions. Experiments on two satellite-based flood mapping tasks demonstrate that the ADAGE framework can (1) quantitatively assess the alignment between model explanations and reference explanations derived from domain knowledge and (2) help domain experts identify misaligned explanations through alignment scores. This study contributes to bridging the gap between explainability and domain knowledge in GeoAI for Earth observation, enhancing the applicability of GeoAI models in scientific and operational workflows.

---


### 11. [From Prompt Risk to Response Risk: Paired Analysis of Safety Behavior of Large Language Model](https://arxiv.org/abs/2604.26052)

**<font color=#1a73e8>作者：</font>** Mengya Hu, Qiong Wei, Sandeep Atluri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of large language models (LLMs) typically report binary outcomes such as attack success rate, refusal rate, or harmful/not-harmful response classification. While useful, these can hide how risk changes between a user's input and the model's response. We present a paired, transition-based analysis over 1250 prompt-response records with human-provided labels over four harm categories (Hate, Sexual, Violence, Self-harm) and ordinal severity levels aligned with the Azure AI Content Safety taxonomy. 61% of responses de-escalate harm relative to the prompt, 36% preserve the same severity, and 3% escalate to higher harm. A per-category persistence/drift-up decomposition identifies Sexual content as 3x harder to de-escalate than Hate or Violence, driven by persistence on already-sexual prompts, not by newly introducing sexual harm from benign inputs. Jointly measuring response relevance reveals an empirical signature of the helpfulness-harmlessness tradeoff: all compliance-escalation cases (from non-zero prompts) are relevance-3 (high-quality, on-task content at elevated severity), while medium-severity responses show the lowest relevance (64%), driven by tangential elaborations in Violence and Sexual categories.

---


### 12. [reward-lens: A Mechanistic Interpretability Library for Reward Models](https://arxiv.org/abs/2604.26130)

**<font color=#1a73e8>作者：</font>** Mohammed Suhail B Nadaf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every RLHF-trained language model is shaped by a reward model, yet the mechanistic interpretability toolkit -- logit lens, direct logit attribution, activation patching, sparse autoencoders -- was built for generative LLMs whose primitives all project onto a vocabulary unembedding. Reward models replace that with a scalar regression head, breaking each tool. We present reward-lens, an open-source library that ports this toolkit to reward models, organised around one observation: the reward head's weight vector $w_r$ is the natural axis for every interpretability question. The library provides a Reward Lens, component attribution, three-mode activation patching, a reward-hacking probe suite, TopK SAE feature attribution, cross-model comparison, and five theory-grounded extensions (distortion index, divergence-aware patching, misalignment cascade detection, reward-term conflict analysis, concept-vector analysis). A ten-method adapter protocol covers Llama, Mistral, Gemma-2, and ArmoRM multi-objective heads, with a generic adapter for any HuggingFace sequence classification model. We validate on two production reward models across ~695 RewardBench pairs. The central empirical finding is negative: linear attribution does not predict causal patching effects (mean Spearman $\rho = -0.256$ on Skywork, $-0.027$ on ArmoRM). The framework treats this disagreement as a property to expose, not a bug -- motivating a design that keeps observational and causal views first-class and directly comparable.

---


### 13. [HIVE: Hidden-Evidence Verification for Hallucination Detection in Diffusion Large Language Models](https://arxiv.org/abs/2604.26139)

**<font color=#1a73e8>作者：</font>** Guoshenghui Zhao, Weijie Zhao, Tan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models generate text through multi-step denoising, where hallucination signals may emerge throughout the trajectory rather than only in the final output. Existing detectors mainly rely on output uncertainty or coarse trace statistics, which often fail to capture the richer hidden dynamics of D-LLMs. We propose HIVE, a hidden-evidence verification framework that extracts compressed hidden evidence from denoising trajectories, selects informative step-layer evidence, and conditions a verifier language model on the selected evidence through prefix embeddings. HIVE produces both a continuous hallucination score from verifier decision logits and structured verification outputs, including hallucination types, evidence pairs, and short rationales. Across two D-LLMs and three QA benchmarks, HIVE consistently outperforms eight strong baselines and achieves up to 0.9236 AUROC and 0.9537 AUPRC. Ablation studies further confirm the importance of hidden-evidence conditioning, learned evidence selection, two-stream evidence representation, and step-layer embeddings. These results suggest that selected hidden evidence from denoising trajectories provides a stronger and more usable hallucination signal than output-only uncertainty or coarse trace statistics.

---


### 14. [EvoSelect: Data-Efficient LLM Evolution for Targeted Task Adaptation](https://arxiv.org/abs/2604.26170)

**<font color=#1a73e8>作者：</font>** Ting-Wei Li, Sirui Chen, Jiaru Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to a targeted task efficiently and effectively remains a fundamental challenge. Such adaptation often requires iteratively improving the model toward a targeted task, yet collecting high-quality human-labeled data to support this process is costly and difficult to scale. As a result, synthetic data generation has emerged as a flexible and scalable alternative. One straightforward approach is through an iterative generation-training loop, where candidate data are synthesized through an external generator, the model is updated using these data and the process is repeated over iterations. However, generated samples can be noisy, highly redundant, or even misaligned with the targeted task distribution. Training indiscriminately on such data can dilute useful learning signals and even degrade model performance. To address this, we introduce a refined paradigm, namely an iterative generation-selection-training loop, which incorporates a selection step prior to model updates. Building on this paradigm, we propose EvoSelect, a data-efficient framework to evolve LLM effectively. Given candidate samples produced by the data generator, EvoSelect selects training data by jointly modeling targeted task alignment and diversity. We estimate task relevance through optimal transport with proxy gradient representations, which quantifies how well candidate samples align with the targeted task distribution. To mitigate redundancy, we incorporate a diversification mechanism that promotes coverage of complementary training samples. By interleaving alignment and diversification, EvoSelect enables progressive LLM evolution toward targeted tasks. Extensive experiments on various benchmarks demonstrate that with either weak or strong data generators, EvoSelect consistently improves adaptation efficacy over existing data selection methods.

---


### 15. [Entropy Centroids as Intrinsic Rewards for Test-Time Scaling](https://arxiv.org/abs/2604.26173)

**<font color=#1a73e8>作者：</font>** Wenshuo Zhao, Qi Zhu, Xingshan Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An effective way to scale up test-time compute of large language models is to sample multiple responses and then select the best one, as in Grok Heavy and Gemini Deep Think. Existing selection methods often rely on external reward models, which requires training a strong reward model and introduces additional computation overhead. As an alternative, previous approaches have explored intrinsic signals, such as confidence and entropy, but these signals are noisy with naive aggregation. In this work, we observe that high-entropy tokens tend to cluster into consecutive groups during inference, providing a more stable notion of model uncertainty than individual tokens. Together, these clusters reveal temporal patterns of model uncertainty throughout the inference process. Motivated by this observation, we propose to use the temporal structure of uncertainty as an intrinsic reward. To this end, we first formalize the basic unit of segment-level uncertainty as the High Entropy Phase (HEP), a variable-length segment that begins at a high-entropy token and ends when consecutive low-entropy tokens appear. We then define the Entropy Centroid, inspired by the concept of the center of mass in physics, as the weighted average position of all HEPs along the trajectory. Intuitively, a lower centroid indicates early exploration followed by confident generation, which we find often corresponds to higher response quality. Based on this insight, we propose the Lowest Centroid method, which selects the response with the lowest entropy centroid among multiple candidates. Experiments on mathematics, code generation, logical reasoning, and agentic tasks, across model scales ranging from 14B to 480B, show that Lowest Centroid consistently outperforms existing baselines and delivers stable gains as model size increases. Code is available at this https URL.

---


### 16. [SWAN: World-Aware Adaptive Multimodal Networks for Runtime Variations](https://arxiv.org/abs/2604.26181)

**<font color=#1a73e8>作者：</font>** Jason Wu, Shir-Kang Scott Jinn, Yuyang Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal deep neural networks deployed in realistic environments must contend with runtime variations: changes in modality quality, overall input complexity, and available platform resources. Current networks struggle with such fluctuations -- adaptive networks cannot adhere to a strict compute budget, controller-based networks neglect to consider input complexity, and statically provisioned networks fail at all the above. Consequently, they do not extract maximum utility from the expended computational resources. We present SWAN (Sample and World-Aware Multimodal Network), the first adaptive multimodal network that accomplishes all three goals. SWAN employs a quality-aware controller to assign resources among modalities according to a variable user-specified maximum budget. Within this budget, an adaptive gating module further optimizes efficiency by scaling layer utilization according to sample complexity. For further gains, SWAN also employs a token dropping module that masks semantically irrelevant multimodal features before performing detections. We evaluate SWAN in the domain of autonomous driving with complex multi-object 3D detection, reducing FLOPs by up to 49% with minimal degradation.

---


### 17. [Lifting Embodied World Models for Planning and Control](https://arxiv.org/abs/2604.26182)

**<font color=#1a73e8>作者：</font>** Alex N. Wang, Trevor Darrell, Pavel Izmailov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. To address this issue, we train a lightweight policy that maps high-level actions to sequences of low-level joint actions. Composing this policy with the frozen world model produces a lifted world model that predicts a sequence of future observations from a single high-level action. We instantiate this framework for a human-like embodiment, defining the high-level action space as a small set of 2D waypoints annotated on the current observation frame, each specifying a near-term goal position for a leaf joint (pelvis, head, hands). Waypoints are low-dimensional, visually interpretable, and easy to specify manually or to search over. We show that the lifted world model substantially outperforms searching directly in low-level joint space ($3.8\times$ lower mean joint error to the goal pose), while remaining more compute-efficient and generalizing to environments unseen by the policy.

---


### 18. [FASH-iCNN: Making Editorial Fashion Identity Inspectable Through Multimodal CNN Probing](https://arxiv.org/abs/2604.26186)

**<font color=#1a73e8>作者：</font>** Morayo Danielle Adeyemi, Ryan A. Rossi, Franck Dernoncourt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion AI systems routinely encode the aesthetic logic of specific houses, editors, and historical moments without disclosing it. We present FASH-iCNN, a multimodal system trained on 87,547 Vogue runway images across 15 fashion houses spanning 1991-2024 that makes this cultural logic inspectable. Given a photograph of a garment, the system recovers which house produced it, which era it belongs to, and which color tradition it reflects. A clothing-only model identifies the fashion house at 78.2% top-1 across 14 houses, the decade at 88.6% top-1, and the specific year at 58.3% top-1 across 34 years with a mean error of just 2.2 years. Probing which visual channels carry this signal reveals a sharp dissociation: removing color costs only 10.6pp of house identity accuracy, while removing texture costs 37.6pp, establishing texture and luminance as the primary carriers of editorial identity. FASH-iCNN treats editorial culture as the signal rather than background noise, identifying which houses, eras, and color traditions shaped each output so that users can see not just what the system predicts but which houses, editors, and historical moments are encoded in that prediction.

---


### 19. [Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction](https://arxiv.org/abs/2604.26209)

**<font color=#1a73e8>作者：</font>** Theodore Glavas, Nikhita Vedula, Dushyanta Dhyani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Some text generation tasks, such as Attribute Value Extraction (AVE), require decoding multiple independent sequences from the same document context. While standard autoregressive decoding is slow due to its sequential nature, the independence between output sequences offers an opportunity for parallelism. We present Hyper-Parallel Decoding, a novel decoding algorithm that accelerates offline decoding by leveraging both shared memory and computation across batches. HPD enables out-of-order token generation through position ID manipulation, significantly improving efficiency. Experiments on AVE show that attribute-value pairs are conditionally independent, enabling us to parallelize value generation within each prompt. By further stacking multiple documents within a single prompt, we can decode in parallel up to 96 tokens per prompt. HPD works with all LLMs, and reduces both inference costs and total inference time by up to 13.8X without compromising output quality, potentially saving hundreds of thousands of dollars on industry AVE tasks. Although designed for attribute extraction, HPD makes no assumptions unique to the AVE domain and can in theory be applied to other scenarios with independent output structures.

---


### 20. [A New Semisupervised Technique for Polarity Analysis using Masked Language Models](https://arxiv.org/abs/2604.26230)

**<font color=#1a73e8>作者：</font>** Kohei Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> I developed a new version of Latent Semantic Scaling (LSS) employing word2vec as a masked language model. Unlike original spatial models, it assigns polarity scores to words and documents as predicted probabilities of seed words to occur in given contexts. These probabilistic polarity scores are more accurate, interpretable and consistent than those spatial polarity models can produce in text analysis. I demonstrate these advantages by applying both probabilistic and spatial models to China Daily's coverage of China and other countries during the coronavirus disease (COVID) pandemic in terms of achievement in health issues. The result suggests that more advanced masked language models would further improve the semisupervised machine learning technique.

---


### 21. [Persuadability and LLMs as Legal Decision Tools](https://arxiv.org/abs/2604.26233)

**<font color=#1a73e8>作者：</font>** Oisin Suttle, David Lillis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are proposed as legal decision assistants, and even first-instance decision-makers, across a range of judicial and administrative contexts, it becomes essential to explore how they answer legal questions, and in particular the factors that lead them to decide difficult questions in one way or another. A specific feature of legal decisions is the need to respond to arguments advanced by contending parties. A legal decision-maker must be able to engage with, and respond to, including through being potentially persuaded by, arguments advanced by the parties. Conversely, they should not be unduly persuadable, influenced by a particularly compelling advocate to decide cases based on the skills of the advocates, rather than the merits of the case. We explore how frontier open- and closed-weights LLMs respond to legal arguments, reporting original experimental results examining how the quality of the advocate making those arguments affects the likelihood that a model will agree with a particular legal point of view, and exploring the factors driving these results. Our results have implications for the feasibility of adopting LLMs across legal and administrative settings.

---


### 22. [DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training](https://arxiv.org/abs/2604.26256)

**<font color=#1a73e8>作者：</font>** Tianhao Hu, Xiangcheng Liu, Youshao Xiao 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a critical paradigm for LLM post-training, yet the rollout phase -- accounting for 50--80% of total step time -- is bottlenecked by skewed generation: long-tailed trajectories indispensable for model performance block the entire training pipeline. Asynchronous training offers a natural remedy by overlapping generation with training, but introduces a fundamental tension between efficiency and algorithmic correctness. We identify three constraints in asynchronous training to preserve convergence: intra-trajectory policy consistency, data integrity, and bounded staleness. Existing approaches fail to intrinsically address the long-tailed trajectory problem, which is further exacerbated by the imbalance characteristic of Mix-of-Experts models, or deviate from the standard RL training formulation, thereby hindering model convergence. Therefore, we propose DORA (Dynamic ORchestration for Asynchronous Rollout), which addresses this challenge through algorithm-system co-design. DORA introduces multi-version streaming rollout, a novel asynchronous paradigm that maintains multiple policy versions concurrently -- simultaneously achieving full bubble elimination without compromising algorithmic constraints. Experimental results demonstrate that our DORA system achieves substantial improvements in throughput -- up to 2--3 times higher than state-of-the-art systems on open-source benchmarks -- without compromising convergence. Furthermore, in large-scale industrial applications with tens of thousands of accelerators, DORA accelerates RL training by 2--4 times compared to synchronous training across various scenarios. The resultant open-source models, LongCat-Flash-Thinking, exhibit competitive performance on complex reasoning benchmarks, matching the capability of most advanced LLMs.

---


### 23. [FlowBot: Inducing LLM Workflows with Bilevel Optimization and Textual Gradients](https://arxiv.org/abs/2604.26258)

**<font color=#1a73e8>作者：</font>** Hongyeon Yu, Young-Bum Kim, Yoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM workflows, which coordinate structured calls to individual LLMs (each augmented with varying instructions and tools) to achieve a particular goal, offer a promising path towards extending the capabilities of LLMs and building powerful systems that can tackle diverse tasks. However, existing approaches for building such workflows generally rely on human-crafted pipelines and prompts, which presents a substantial bottleneck in real world deployment. How can automatically induce and optimize such workflows in a data-driven way? This paper describes a simple data-driven approach for automatically inducing LLM workflows. We formulate workflow induction as a bilevel optimization problem: an outer loop which optimizes a high-level sketch of the workflow (in particular how the LLM calls should be structured), and an inner loop which optimizes each individual LLM call one-by one. Both loops are optimized with ``textual gradients'' where for the inner loop we optimize each component in a modular way through ``backpropagating'' textual gradients layer-by-layer. We find that LLM workflows discovered through our \textsc{FlowBot} (work\textbf{flow} induction through \textbf{b}ilevel \textbf{o}ptimization and \textbf{t}extual gradients) approach performs competitively against strong baselines that make use of human-crafted or automatically-generated workflows.

---


### 24. [Multiple Consistent 2D-3D Mappings for Robust Zero-Shot 3D Visual Grounding](https://arxiv.org/abs/2604.26261)

**<font color=#1a73e8>作者：</font>** Yufei Yin, Jie Zheng, Qianke Meng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot 3D Visual Grounding (3DVG) is a critical capability for open-world embodied AI. However, existing methods are fundamentally bottlenecked by the poor quality of open-vocabulary 3D proposals, suffering from inaccurate categories and imprecise geometries, as well as the spatial redundancy of exhaustive multi-view reasoning. To address these challenges, we propose MCM-VG, a novel framework that achieves robust zero-shot 3DVG by explicitly establishing Multiple Consistent 2D-3D Mappings. Instead of passively relying on noisy 3D segments, MCM-VG enforces 2D-3D consistency across three fundamental dimensions to achieve precise target localization and reliable reasoning. First, a Semantic Alignment module corrects category mismatches via LLM-driven query parsing and coarse-to-fine 2D-3D matching. Second, an Instance Rectification module leverages VLM-guided 2D segmentations to reconstruct missing targets, back-projecting these reliable visual priors to establish accurate 3D geometries. Finally, to eliminate spatial redundancy, a Viewpoint Distillation module clusters 3D camera directions to extract optimal frames. By pairing these optimal RGB frames with Bird's Eye View maps into concise visual prompt sets, we formulate the final target disambiguation as a multiple-choice reasoning task for Vision-Language Models.
Extensive evaluations on ScanRefer and Nr3D benchmarks demonstrate that MCM-VG sets a new state-of-the-art for zero-shot 3D visual grounding. Remarkably, it achieves 62.0\% and 53.6\% in Acc@0.25 and Acc@0.5 on ScanRefer, outperforming previous baselines by substantial margins of 6.4\% and 4.0\%.

---


### 25. [CheXthought: A global multimodal dataset of clinical chain-of-thought reasoning and visual attention for chest X-ray interpretation](https://arxiv.org/abs/2604.26288)

**<font color=#1a73e8>作者：</font>** Sonali Sharma, Jin Long, George Shih 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray interpretation is one of the most frequently performed diagnostic tasks in medicine and a primary target for AI development, yet current vision--language models are primarily trained on datasets of paired images and reports, not the cognitive processes and visual attention that underlie clinical reasoning. Here, we present CheXthought, a global, multimodal resource containing 103,592 chain-of-thought reasoning traces and 6,609,082 synchronized visual attention annotations across 50,312 multi-read chest X-rays from 501 radiologists in 71 countries. Our analysis reveals clinical reasoning patterns in how experts deploy distinct visual search strategies, integrate clinical context, and communicate uncertainty. We demonstrate the clinical utility of CheXthought across four dimensions. First, CheXthought reasoning significantly outperforms state--of--the--art vision--language model chain-of-thought in factual accuracy and spatial grounding. Second, visual attention data used as an inference--time hint recovers missed findings and significantly reduces hallucinations. Third, models trained on CheXthought data achieve significantly stronger pathology classification, visual faithfulness, temporal reasoning and uncertainty communication. Fourth, leveraging CheXthought's multi-reader annotations, we predict both human--human and human--AI disagreement directly from an image, enabling transparent communication of case difficulty, uncertainty and model reliability. These findings establish CheXthought as a resource for advancing multimodal clinical reasoning and the development of more transparent, interpretable vision--language models.

---


### 26. [A Systematic Comparison of Prompting and Multi-Agent Methods for LLM-based Stance Detection](https://arxiv.org/abs/2604.26319)

**<font color=#1a73e8>作者：</font>** Genan Dai, Zini Chen, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection identifies the attitude of a text author toward a given target. Recent studies have explored various LLM-based strategies for this task, from zero-shot prompting to multi-agent debate. However, existing works differ in data splits, base models, and evaluation protocols, making fair comparison difficult. We conduct a systematic comparison that evaluates five methods across two categories -- prompt-based inference (Direct Prompting, Auto-CoT, StSQA) and agent-based debate (COLA, MPRF) -- on four datasets with 14 subtasks, using 15 LLMs from six model families with parameter sizes from 7B to 72B+. Our experiments yield several findings. First, on all models with complete results, the best prompt-based method outperforms the best agent-based method, while agent methods require 7 to 12 times more API calls per sample. Second, model scale has a larger impact on performance than method choice, with gains plateauing around 32B. Third, reasoning-enhanced models (DeepSeek-R1) do not consistently outperform general models of the same size on this task.

---


### 27. [Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control](https://arxiv.org/abs/2604.26326)

**<font color=#1a73e8>作者：</font>** Bolian Li, Yifan Wang, Yi Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has unlocked complex reasoning abilities in large language models (LLMs). However, most RL algorithms suffer from performance saturation, preventing further gains as RL training scales. This problem can be characterized by the collapse of entropy, a key diagnostic for exploration in RL. Existing attempts have tried to prevent entropy collapse through regularization or clipping, but their resulting entropy curves often exhibit instability in the long term, which hinders performance gains. In this paper, we introduce Entrocraft, a simple rejection-sampling approach that realizes any user-customized entropy schedule by biasing the advantage distributions. Entrocraft requires no objective regularization and is advantage-estimator-agnostic. Theoretically, we relate per-step entropy change to the advantage distribution under minimal assumptions, which explains the behavior of existing RL and entropy-preserving methods. Entrocraft also enables a systematic study of entropy schedules, where we find that linear annealing, which starts high and decays to a slightly lower target, performs best. Empirically, Entrocraft addresses performance saturation, significantly improving generalization, output diversity, and long-term training. It enables a 4B model to outperform an 8B baseline, sustains improvement for up to 4x longer before plateauing, and raises pass@K by 50% over the baseline.

---


### 28. [DSIPA: Detecting LLM-Generated Texts via Sentiment-Invariant Patterns Divergence Analysis](https://arxiv.org/abs/2604.26328)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Aodu Wulianghai, Guangyan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) presents new security challenges, particularly in detecting machine-generated text used for misinformation, impersonation, and content forgery. Most existing detection approaches struggle with robustness against adversarial perturbation, paraphrasing attacks, and domain shifts, often requiring restrictive access to model parameters or large labeled datasets. To address this, we propose DSIPA, a novel training-free framework that detects LLM-generated content by quantifying sentiment distributional stability under controlled stylistic variation. It is based on the observation that LLMs typically exhibit more emotionally consistent outputs, while human-written texts display greater affective variation. Our framework operates in a zero-shot, black-box manner, leveraging two unsupervised metrics, sentiment distribution consistency and sentiment distribution preservation, to capture these intrinsic behavioral asymmetries without the need for parameter updates or probability access. Extensive experiments are conducted on state-of-the-art proprietary and open-source models, including GPT-5.2, Gemini-1.5-pro, Claude-3, and LLaMa-3.3. Evaluations on five domains, such as news articles, programming code, student essays, academic papers, and community comments, demonstrate that DSIPA improves F1 detection scores by up to 49.89% over baseline methods. The framework exhibits superior generalizability across domains and strong resilience to adversarial conditions, providing a robust and interpretable behavioral signal for secure content identification in the evolving LLM landscape.

---


### 29. [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](https://arxiv.org/abs/2604.26340)

**<font color=#1a73e8>作者：</font>** Weihang Li, Jianchun Liu, Hongli Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA-MoE has emerged as an effective paradigm for parameter-efficient fine-tuning, combining the low training cost of LoRA with the increased adaptation capacity of Mixture-of-Experts (MoE). However, existing LoRA-MoE frameworks typically adopt a fixed and uniform expert configuration across heterogeneous Transformer modules (\eg, attention query/key projections and MLP gating networks), ignoring their distinct functional roles and capacity requirements. This design leads to localized over-provisioning, redundant trainable parameters, and unnecessary optimizer-state overhead. Moreover, prior methods enforce load balancing among experts throughout training. Although beneficial in the early stage, this constraint becomes restrictive once routing patterns stabilize, limiting expert specialization on downstream tasks. In this paper, we propose DMEP, a novel LoRA-MoE fine-tuning framework based on Dynamic Module-wise Expert Pruning. DMEP tracks expert utilization during training and physically removes low-utility experts on a per-module basis, yielding a more compact expert structure tailored to different modules. The pruned model then continues training without the load-balancing constraint, freeing the remaining experts to focus entirely on the downstream task and develop specialized expertise. By jointly adapting module-wise expert capacity and eliminating unnecessary balancing, DMEP improves both parameter efficiency and training efficiency. Extensive experiments on multiple reasoning benchmarks show that DMEP reduces trainable parameters by 35\%--43\% and improves training throughput by about 10\%, while maintaining or surpassing the downstream reasoning accuracy of uniform LoRA-MoE baselines.

---


### 30. [A Dual-Task Paradigm to Investigate Sentence Comprehension Strategies in Language Models](https://arxiv.org/abs/2604.26351)

**<font color=#1a73e8>作者：</font>** Rei Emura, Saku Sugawara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) behave more like humans when their cognitive resources are restricted, particularly in predicting sentence processing costs such as reading times. However, it remains unclear whether such constraints similarly affect sentence comprehension strategies. Besides, existing methods do not directly target the balance between memory storage and sentence processing, which is central to human working memory. To address this issue, we propose a dual-task paradigm that combines an arithmetic computation task with a sentence comprehension task, such as "The 2 cocktail + blended 3 =..." Our experiments show that under dual-task conditions, GPT-4o, o3-mini, and o4-mini shift toward plausibility-based comprehension, mirroring humans' rational inference. Specifically, these models show a greater accuracy gap between plausible sentences (e.g., "The cocktail was blended by the bartender") and implausible sentences (e.g., "The bartender was blended by the cocktail") in the dual-task condition compared to the single-task conditions. These findings suggest that constraints on the balance between memory and processing resources promote rational inference in LMs. More broadly, they support the view that human-like sentence comprehension fundamentally arises from the allocation of limited cognitive resources.

---


### 31. [Shorthand for Thought: Compressing LLM Reasoning via Entropy-Guided Supertokens](https://arxiv.org/abs/2604.26355)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhao, Sander Land, Dan Bikel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning in Large Language Models incurs significant inference-time compute, yet the token-level information structure of reasoning traces remains underexplored. We observe that reasoning tokens split into two functional types: low-entropy \textit{structural} tokens (recurring phrases that scaffold the reasoning process) and higher-entropy \textit{organic} tokens (problem-specific content that drives toward a solution). This asymmetry motivates a simple, model-agnostic compression pipeline: apply cross-word BPE merges on a model's own reasoning traces to derive \textit{supertokens} that capture frequent structural patterns, then teach the model to adopt them via supervised fine-tuning. Across three model families and five mathematical reasoning benchmarks, our approach shortens reasoning traces by 8.1\% on average with no statistically significant accuracy loss on any model--benchmark pair. Beyond compression, supertokens act as interpretable reasoning-move annotations (backtracking, verification, strategy shifts), exposing the model's high-level strategy at a glance. Analyzing transitions between structural categories reveals systematic differences between correct and incorrect traces: correct traces show productive recovery (backtracking followed by strategy shifts and verification), while incorrect traces are dominated by confusion cycles (repeated hedging and unresolved contradictions). These diagnostic signals suggest applications in reward shaping and early stopping for RL-based reasoning training.

---


### 32. [Topology-Aware Representation Alignment for Semi-Supervised Vision-Language Learning](https://arxiv.org/abs/2604.26370)

**<font color=#1a73e8>作者：</font>** Junwon You, Mihyun Jang, Sangwoo Mo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models have shown strong performance, but they often generalize poorly to specialized domains. While semi-supervised vision-language learning mitigates this limitation by leveraging a small set of labeled image-text pairs together with abundant unlabeled images, existing methods remain fundamentally pairwise and fail to model the global structure of multimodal representation manifolds. Existing topology-based alignment methods rely on persistence diagram matching, which neither guarantees geometric alignment nor utilizes the image-text pairing information central to vision-language learning. We propose Topology-Aware Multimodal Representation Alignment (ToMA), a framework that uses persistent homology to identify topologically salient edges and aligns them across modalities through available cross-modal correspondences. ToMA leverages both H_0-death edges and lightweight H_1-birth edges, allowing it to capture both connectivity and cycle structure without constructing 2-simplices. Experiments show that ToMA yields stable gains, with clear improvements on remote sensing and modest but consistent benefits on fashion retrieval. Additional analysis shows that ToMA is more stable than alternative topology-based objectives and that lightweight H_1-birth edges provide useful higher-order structural signals.

---


### 33. [CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs](https://arxiv.org/abs/2604.26378)

**<font color=#1a73e8>作者：</font>** Zhe Ding, Su Pan, Duowei Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) has become an important technique for reducing the inference cost of Large Language Models (LLMs). While recent mixed-precision methods improve ultra-low bit quantization by preserving critical subspaces in high precision, they typically construct these subspaces relying solely on activation statistics. This ignores the fundamental nature of linear operations, where the output perturbation is jointly driven by both activation and weight quantization noise. In this paper, we propose CoQuant, a joint weight-activation subspace projection method. By theoretically modeling the expected output error, CoQuant formulates a closed-form weighted PCA solution that balances activation and weight covariances to select the optimal high-precision subspace. Extensive experiments on Llama-3.2 and Qwen2.5 models show that CoQuant consistently outperforms strong PTQ baselines in both WikiText perplexity and zero-shot common-sense reasoning accuracy. These results demonstrate that joint weight-activation subspace modeling provides a principled and effective direction for low-bit LLM quantization. The source code is available at this https URL.

---


### 34. [A Multimodal Pre-trained Network for Integrated EEG-Video Seizure Detection](https://arxiv.org/abs/2604.26379)

**<font color=#1a73e8>作者：</font>** Tong Lu, Ke Xu, Zimo Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable seizure detection in mouse models is essential for preclinical epilepsy research, yet manual review of synchronized video-EEG recordings is labor-intensive and single-modality systems fail for complementary reasons: video-based methods are easily confounded by benign behaviors, whereas EEG-based methods are vulnerable to ictal motion artifacts. We present EEGVFusion, a multimodal framework that combines self-supervised EEG representation learning, spatio-temporal video encoding, optimal-transport alignment, and bidirectional cross-attention to integrate neural and behavioral evidence. We also curate an expert-annotated dataset of synchronized EEG and video recordings comprising 93 sessions from 15 mice for training and evaluation. In the random-session split, EEGVFusion achieved a Balanced Accuracy of 0.9957 with perfect event sensitivity and an Event FAR of 0.6250 FP/h, indicating strong seizure detection performance with a low false-alarm burden. In a single held-out-subject evaluation with Subject 110 reserved for testing, EEGVFusion achieved a Balanced Accuracy of 0.9718 and reduced Event FAR from 2.7250 FP/h for the EEG-only counterpart to 0.4833 FP/h while preserving perfect event sensitivity. Targeted ablations further showed that EEG pre-training and OT alignment help reduce false alarms while preserving event sensitivity.

---


### 35. [Benchmarking Complex Multimodal Document Processing Pipelines: A Unified Evaluation Framework for Enterprise AI](https://arxiv.org/abs/2604.26382)

**<font color=#1a73e8>作者：</font>** Saurabh K. Singh, Sachin Raj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most enterprise document AI today is a pipeline. Parse, index, retrieve, generate. Each of those stages has been studied to death on its own -- what's still hard is evaluating the system as a whole.
We built EnterpriseDocBench to take a swing at it: parsing fidelity, indexing efficiency, retrieval relevance, and generation groundedness, all on the same corpus. The corpus is built from public, permissively licensed documents across six enterprise domains (five represented in the current pilot). We ran three pipelines through it -- BM25, dense embedding, and a hybrid -- all with the same GPT-5 generator.
The headline numbers: hybrid retrieval narrowly beats BM25 (nDCG@5 of 0.92 vs. 0.91), and both beat dense embedding (0.83). Hallucination doesn't grow monotonically with document length -- short documents and very long ones both hallucinate more than medium ones (28.1% and 23.8% vs. 9.2%). Cross-stage correlations are very weak: parsing->retrieval r=0.14, parsing->generation r=0.17, retrieval->generation 0.02. If quality were cascading the way most of us assume, those numbers would be much higher; they aren't. Design caveats are real (parsing fixed, generator shared, automated proxy metrics) and we don't oversell the result.
One result that genuinely surprised us: factual accuracy on stated claims is 85.5%, but answer completeness averages 0.40. The system is right when it answers -- it just leaves things out. That gap matters more for real deployments than the headline accuracy number does.
We also describe three reference architectures (ColPali, ColQwen2, agentic complexity-based routing) which are not yet integrated end-to-end. Framework, metrics, baselines, and collection scripts will be released open-source on acceptance.

---


### 36. [Decoupled Prototype Matching with Vision Foundation Models for Few-Shot Industrial Object Detection](https://arxiv.org/abs/2604.26404)

**<font color=#1a73e8>作者：</font>** Hari Prasanth S. M., Nilusha Jayawickrama, Risto Ojala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial object detection systems typically rely on large annotated datasets, which are expensive to collect and challenging to maintain in industrial scenarios where the inventory of objects changes frequently. This work addresses the challenge of few-shot object detection in such industrial scenarios, where only a limited number of labeled samples are available for newly introduced objects. We present a detection framework that leverages vision foundation models to recognize objects with minimal supervision. The method constructs class prototypes from a small set of reference samples by extracting feature representations. For a given query scene during inference, object regions are generated using a segmentation model, and feature embeddings are extracted and matched with class prototypes using similarity matching. We evaluate the detection method on three established industrial datasets from the Benchmark for 6D Object Pose Estimation benchmark following the official 2D object detection evaluation protocol. We demonstrate competitive detection performance, improving AP by 6.9% compared to the state-of-the-art training-free detection methods. Furthermore, the presented method is able to onboard new objects using only a few reference images, without requiring any CAD models or large annotated datasets. These properties make the approach well-suited for real-world industrial applications.

---


### 37. [Sparsity as a Key: Unlocking New Insights from Latent Structures for Out-of-Distribution Detection](https://arxiv.org/abs/2604.26409)

**<font color=#1a73e8>作者：</font>** Ahyoung Oh, Wonseok Shin, Songkuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) have demonstrated significant success in interpreting Large Language Models (LLMs) by decomposing dense representations into sparse, semantic components. However, their potential for analyzing Vision Transformers (ViTs) remains largely under-explored. In this work, we present the first application of SAEs to the ViT [CLS] token for out-of-distribution (OOD) detection, addressing the limitation of existing methods that rely on entangled feature representations. We propose a novel framework utilizing a Top-k SAE to disentangle the dense [CLS] features into a structured latent space. Through this analysis, we reveal that in-distribution (ID) data exhibits consistent, class-specific activation patterns, which we formalize as Class Activation Profiles (CAPs). Our study uncovers a key structural invariant: while ID samples preserve a stable pattern within CAPs, OOD samples systematically disrupt this structure. Leveraging this insight, we introduce a scoring function based on the divergence of core energy profiles to quantify the deviation from ideal activation profiles. Our method achieves strong results on the FPR95 metric, critical for safety-sensitive applications across multiple benchmarks, while also achieving competitive AUROC. Overall, our findings demonstrate that the sparse, disentangled features revealed by SAEs can serve as a powerful, interpretable tool for robust OOD detection in vision models.

---


### 38. [Delineating Knowledge Boundaries for Honest Large Vision-Language Models](https://arxiv.org/abs/2604.26419)

**<font color=#1a73e8>作者：</font>** Junru Song, Yimeng Hu, Yijing Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (VLMs) have achieved remarkable multimodal performance yet remain prone to factual hallucinations, particularly in long-tail or specialized domains. Moreover, current models exhibit a weak capacity to refuse queries that exceed their parametric knowledge. In this paper, we propose a systematic framework to enhance the refusal capability of VLMs when facing such unknown questions. We first curate a model-specific "Visual-Idk" (Visual-I don't know) dataset, leveraging multi-sample consistency probing to distinguish between known and unknown facts. We then align the model using supervised fine-tuning followed by preference-aware optimization (e.g., DPO, ORPO) to effectively delineate its knowledge boundaries. Results on the Visual-Idk dataset show our method improves the Truthful Rate from 57.9\% to 67.3\%. Additionally, internal probing also demonstrates that the model genuinely recognizes its boundaries instead of just memorizing refusal patterns. Our framework further generalizes to out-of-distribution medical and perceptual domains, providing a robust path toward more trustworthy and prudent visual assistants.

---


### 39. [Attribution-Guided Multimodal Deepfake Detection via Cross-Modal Forensic Fingerprints](https://arxiv.org/abs/2604.26453)

**<font color=#1a73e8>作者：</font>** Wasim Ahmad, Wei Zhang, Xuerui Mao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual deepfakes have reached a level of realism that makes perceptual detection unreliable, threatening media integrity and biometric security. While multimodal detection has shown promise, most approaches are binary classification tasks that often latch onto dataset-specific artifacts rather than genuine generative traces. We argue that a detector incapable of identifying how a video was forged is likely learning the wrong signal. Unlike binary detection, attribution-guided learning imposes a stronger geometric constraint on the shared embedding space, forcing the model to encode generator-specific forensic content rather than shortcuts.
We propose the Attribution-Guided Multimodal Deepfake Detection (AMDD) framework, which jointly learns to detect and attribute manipulation. AMDD treats generator attribution as a structured regularization that constrains representation geometry toward forensically meaningful features. We introduce a Cross-Modal Forensic Fingerprint Consistency (CMFFC) loss to enforce alignment between generator-induced artifacts in visual and audio streams. This exploits the fact that coherent manipulation leaves correlated traces across modalities, grounded in the physical coupling between speech and facial articulation that synthetic pipelines routinely disrupt.
Architecturally, we pair a ResNet50 with temporal attention for visual encoding against a pretrained ResNet18 for mel spectrograms, closing the encoder capacity gap found in prior models. On FakeAVCeleb, AMDD achieves 99.7% balanced accuracy and 99.8% AUC with 95.9% attribution accuracy. Cross-dataset evaluation on DeepfakeTIMIT, DFDM, and LAV-DF confirms that real video detection generalizes robustly, while fake detection on unseen generators remains an open challenge that we analyze in depth.

---


### 40. [Naamah: A Large Scale Synthetic Sanskrit NER Corpus via DBpedia Seeding and LLM Generation](https://arxiv.org/abs/2604.26456)

**<font color=#1a73e8>作者：</font>** Akhil Rajeev P, Annarao Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The digitisation of classical Sanskrit literature is impeded by a scarcity of annotated resources, particularly for Named Entity Recognition. While recent methodologies utilise generic Large Language Models (LLMs) for data augmentation, these approaches remain prone to error and often lack the reasoning depth required for classical grammar. In this work, we introduce Naamah, a high quality silver standard Sanskrit NER dataset comprising 102,942 sentences. We propose a methodology that combines entity extraction from DBpedia with the generative capabilities of a 24B parameter hybrid reasoning model to create grammatically natural and synthetically diverse training data. We utilize this dataset to benchmark two transformer architectures: the massive multilingual XLM RoBERTa and the parameter efficient IndicBERTv2.

---


### 41. [Theory-Grounded Evaluation Exposes the Authorship Gap in LLM Personalization](https://arxiv.org/abs/2604.26460)

**<font color=#1a73e8>作者：</font>** Yash Ganpat Sawant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stylistic personalization - making LLMs write in a specific individual's style, rather than merely adapting to task preferences - lacks evaluation grounded in authorship science. We show that grounding evaluation in authorship verification theory transforms what benchmarks can measure. Drawing on three measurement traditions - LUAR, a trained authorship verification model; an LLM-as-judge with decoupled trait matching; and classical function-word stylometrics - we evaluate four inference-time personalization methods across 50 authors and 1,000 generations. The theory-grounded metric, LUAR, provides what ad hoc alternatives cannot: calibrated baselines, with a human ceiling of 0.756 and a cross-author floor of 0.626, that give scores absolute meaning. All methods score below this floor, from 0.484 to 0.508, exposing an authorship gap invisible to uncalibrated metrics. The three metrics produce near-zero pairwise correlations, with absolute r less than 0.07, confirming that without theoretical grounding, metric choice determines conclusions: an LLM judge declares a clear winner while LUAR finds no meaningful differentiation. These findings demonstrate the theory-benchmark cycle in action: authorship theory exposes evaluation failures that ad hoc benchmarks miss.

---


### 42. [Cross-Domain Transfer of Hyperspectral Foundation Models](https://arxiv.org/abs/2604.26478)

**<font color=#1a73e8>作者：</font>** Nick Theisen, Peer Neubert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging (HSI) semantic segmentation typically relies on in-domain training, but limited data availability often restricts model performance in real-world applications. Current approaches to leverage foundation models in proximal sensing use cross-modality techniques, bridging RGB and HSI to exploit vision foundation models. However, these methods either discard spectral information or introduce architectural complexity. We propose cross-domain transfer as an alternative, reusing HSI foundation models - originally trained in remote sensing - for proximal sensing applications. By eliminating the need to bridge modality gaps, our approach preserves spectral information while maintaining a simple architecture. Using the HS3-Bench benchmark, we systematically evaluate and compare conventional in-domain, in-modality training, cross-modality transfer and cross-domain transfer strategies. Our results demonstrate that cross-domain transfer achieves large performance improvements over in-domain, in-modality training, reduces the performance gap to cross-modality approaches and maintains strong performance in limited data settings. Thus, this work advances more effective HSI semantic segmentation in diverse applications.

---


### 43. [Do Larger Models Really Win in Drug Discovery? A Benchmark Assessment of Model Scaling in AI-Driven Molecular Property and Activity Prediction](https://arxiv.org/abs/2604.26498)

**<font color=#1a73e8>作者：</font>** Jinjiang Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of molecular foundation models and general-purpose large language models has encouraged a scale-centric view of artificial intelligence in drug discovery, in which larger pretrained models are expected to supersede compact cheminformatics models and task-specific graph neural networks (GNNs). We test this assumption on 22 molecular property and activity endpoints, including public ADMET and Tox21 benchmarks and two internal anti-infective activity datasets. Across 167,056 held-out task--molecule evaluations under structure-similarity-separated five-fold cross-validation (37,756 ADMET, 77,946 Tox21, 49,266 anti-TB and 2,088 antimalaria), classical machine-learning (ML) models such as RF(ECFP4) and ExtraTrees(RDKit descriptors) win ten primary-metric tasks, GNNs such as GIN and Ligandformer win nine, and pretrained molecular sequence models such as MoLFormer and ChemBERTa2 win three. Rule-based SAR reasoning baselines, represented by GPT5.5-SAR and Opus4.7-SAR, do not win under the prespecified primary metrics, although train-fold-derived SAR knowledge provides measurable but uneven gains for SAR reasoning and interpretation. These results indicate that compact, specialized models remain highly effective for molecular property and activity prediction. The performance differences among classical ML, GNN and pretrained sequence models are often modest and endpoint-dependent, whereas larger or more general models do not provide a universal predictive advantage. Large models may still add value for zero-shot reasoning, SAR interpretation and hypothesis generation, but the results suggest that predictive performance depends on the alignment among molecular representation, inductive bias, data regime, endpoint biology and validation protocol.

---


### 44. [SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts](https://arxiv.org/abs/2604.26506)

**<font color=#1a73e8>作者：</font>** Yuan Xin, Yixuan Weng, Minjun Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly integrated into academic peer review, their vulnerability to adversarial prompts -- adversarial instructions embedded in submissions to manipulate outcomes -- emerges as a critical threat to scholarly integrity. To counter this, we propose a novel adversarial framework where a Generator model, trained to create sophisticated attack prompts, is jointly optimized with a Defender model tasked with their detection. This system is trained using a loss function inspired by Information Retrieval Generative Adversarial Networks, which fosters a dynamic co-evolution between the two models, forcing the Defender to develop robust capabilities against continuously improving attack strategies. The resulting framework demonstrates significantly enhanced resilience to novel and evolving threats compared to static defenses, thereby establishing a critical foundation for securing the integrity of peer review.

---


### 45. [Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models](https://arxiv.org/abs/2604.26508)

**<font color=#1a73e8>作者：</font>** Cyril Shih-Huan Hsu, Wig Yuan-Cheng Cheng, Chrysa Papagianni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms. Conversely, fully offloading inference to the cloud is often impractical in bandwidth-limited environments, where transmitting raw visual data introduces substantial latency overhead. While recent edge-cloud collaborative architectures attempt to partition VLM workloads across devices, they typically rely on transmitting fixed-size representations, lacking adaptability to dynamic network conditions and failing to fully exploit semantic redundancy. In this paper, we propose a progressive semantic communication framework for edge-cloud VLM inference, using a Meta AutoEncoder that compresses visual tokens into adaptive, progressively refinable representations, enabling plug-and-play deployment with off-the-shelf VLMs without additional fine-tuning. This design allows flexible transmission at different information levels, providing a controllable trade-off between communication cost and semantic fidelity. We implement a full end-to-end edge-cloud system comprising an embedded NXP i.MX95 platform and a GPU server, communicating over bandwidth-constrained networks. Experimental results show that, at 1 Mbps uplink, the proposed progressive scheme significantly reduces network latency compared to full-edge and full-cloud solutions, while maintaining high semantic consistency even under high compression. The implementation code will be released upon publication at this https URL.

---


### 46. [Lyapunov-Guided Self-Alignment: Test-Time Adaptation for Offline Safe Reinforcement Learning](https://arxiv.org/abs/2604.26516)

**<font color=#1a73e8>作者：</font>** Seungyub Han, Hyungjin Kim, Jungwoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) agents often fail when deployed, as the gap between training datasets and real environments leads to unsafe behavior. To address this, we present SAS (Self-Alignment for Safety), a transformer-based framework that enables test-time adaptation in offline safe RL without retraining. In SAS, the main mechanism is self-alignment: at test time, the pretrained agent generates several imagined trajectories and selects those satisfying the Lyapunov condition. These feasible segments are then recycled as in-context prompts, allowing the agent to realign its behavior toward safety while avoiding parameter updates. In effect, SAS turns Lyapunov-guided imagination into control-invariant prompts, and its transformer architecture admits a hierarchical RL interpretation where prompting functions as Bayesian inference over latent skills. Across Safety Gymnasium and MuJoCo benchmarks, SAS consistently reduces cost and failure while maintaining or improving return.

---


### 47. [AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents](https://arxiv.org/abs/2604.26522)

**<font color=#1a73e8>作者：</font>** Mahnoor Shahid, Hannes Rothe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents exhibit systemic failures in compositional generalization, limiting their robustness in interactive environments. This work introduces AGEL-Comp, a neuro-symbolic AI agent architecture designed to address this challenge by grounding actions of the agent. AGEL-Comp integrates three core innovations: (1) a dynamic Causal Program Graph (CPG) as a world model, representing procedural and causal knowledge as a directed hypergraph; (2) an Inductive Logic Programming (ILP) engine that synthesizes new Horn clauses from experiential feedback, grounding symbolic knowledge through interaction; and (3) a hybrid reasoning core where an LLM proposes a set of candidate sub-goals that are verified for logical consistency by a Neural Theorem Prover (NTP). Together, these components operationalize a deduction--abduction learning cycle: enabling the agent to deduce plans and abductively expand its symbolic world model, while a neural adaptation phase keeps its reasoning engine aligned with new knowledge. We propose an evaluation protocol within the \texttt{Retro Quest} simulation environment to probe for compositional generalization scenarios to evaluate our AGEL agent. Our findings clearly indicate the better performance of our AGEL model over pure LLM-based models. Our framework presents a principled path toward agents that build an explicit, interpretable, and compositionally structured understanding of their world.

---


### 48. [TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models](https://arxiv.org/abs/2604.26553)

**<font color=#1a73e8>作者：</font>** Jinho Choo, JunSeung Lee, Jimyeong Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong multilingual capabilities, yet often fail to consistently generate responses in the intended language, exhibiting a phenomenon known as language confusion. Prior mitigation approaches based on sequence-level fine-tuning, such as DPO, ORPO, and GRPO, operate at the level of entire responses and can lead to unintended degradation of general model capabilities, motivating the need for more fine-grained alternatives. To address this, we introduce Token-Level Policy Optimization (TLPO), a fine-tuning framework designed to mitigate language confusion through localized, token-level updates. TLPO identifies error-prone positions, explores alternative candidate tokens, and updates the policy using a tailored objective to suppress error-inducing outputs at a granular level. This selective intervention enables effective mitigation of language confusion without compromising the model's general abilities. Experiments on multiple multilingual LLMs across diverse languages demonstrate that TLPO significantly outperforms baselines in improving language consistency while preserving downstream task accuracy.

---


### 49. [DenseStep2M: A Scalable, Training-Free Pipeline for Dense Instructional Video Annotation](https://arxiv.org/abs/2604.26565)

**<font color=#1a73e8>作者：</font>** Mingji Ge, Qirui Chen, Zeqian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term video understanding requires interpreting complex temporal events and reasoning over procedural activities. While instructional video corpora, like HowTo100M, offer rich resources for model training, they present significant challenges, including noisy ASR transcripts and inconsistent temporal alignments between narration and visual content. In this work, we introduce an automated, training-free pipeline to extract high-quality procedural annotations from in-the-wild instructional videos. Our approach segments videos into coherent shots, filters poorly aligned content, and leverages state-of-the-art multimodal and large language models (Qwen2.5-VL and DeepSeek-R1) to generate structured, temporally grounded procedural steps.
This pipeline yields DenseStep2M, a large-scale dataset comprising approximately 100K videos and 2M detailed instructional steps, designed to support comprehensive long-form video understanding. To rigorously evaluate our pipeline, we curate DenseCaption100, a benchmark of high-quality, human-written captions. Evaluations demonstrate strong alignment between our auto-generated steps and human annotations. Furthermore, we validate the utility of DenseStep2M across three core downstream tasks: dense video captioning, procedural step grounding, and cross-modal retrieval. Models fine-tuned on DenseStep2M achieve substantial gains in captioning quality and temporal localization, while exhibiting robust zero-shot generalization across egocentric, exocentric, and mixed-perspective domains. These results underscore the effectiveness of DenseStep2M in facilitating advanced multimodal alignment and long-term activity reasoning. Our dataset is available at this https URL.

---


### 50. [Multimodal LLMs are not all you need for Pediatric Speech Language Pathology](https://arxiv.org/abs/2604.26568)

**<font color=#1a73e8>作者：</font>** Darren Fürst, Sebastian Steindl, Ulrich Schäfer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Sound Disorders (SSD) affect roughly five percent of children, yet speech-language pathologists face severe staffing shortages and unmanageable caseloads. We test a hierarchical approach to SSD classification on the granular multi-task SLPHelmUltraSuitePlus benchmark. We propose a cascading approach from binary classification to type, and symptom classification. By fine-tuning Speech Representation Models (SRM), and using targeted data augmentation we mitigate biases found by previous works, and improve upon all clinical tasks in the benchmark. We also treat Automatic Speech Recognition (ASR) with our data augmentation approach. Our results demonstrate that SRM consistently outperform the LLM-based state-of-the-art across all evaluated tasks by a large margin. We publish our models and code to foster future research.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-75](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
