# 🔐 大模型安全相关研究 | 2026年11月10日

> 本类共 **7** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AttentionSwitch: Jailbreak Defense for LLMs via Joint Learning of Sparse Attention-Head Selection and Scaling](https://arxiv.org/abs/2611.08752)

**<font color=#1a73e8>作者：</font>** Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable performance across a wide range of tasks, yet they remain susceptible to jailbreak attacks that circumvent safety mechanisms and elicit harmful or unintended outputs. Although safety can be improved through model fine-tuning, such approaches can be computationally expensive and may degrade previously acquired capabilities through catastrophic forgetting. Recent jailbreak defenses have therefore explored targeted interventions on specific model components associated with unsafe behavior. However, existing approaches typically decouple two inherently related decisions: where to intervene and how to modify the selected components. Such sequential optimization may be suboptimal because the optimal intervention location can depend on the intervention applied there, and vice versa. In this work, we introduce AttentionSwitch, the first jailbreak defense to jointly optimize intervention sites and strengths within a frozen LLM. Specifically, AttentionSwitch learns a sparse set of attention heads together with query-conditioned multiplicative scaling factors, allowing the outputs of the selected heads to be either attenuated or amplified without altering the directions of their representations. Across popular language models and jailbreak attacks, AttentionSwitch outperforms existing defenses, with particularly strong results when training data is scarce.

---


### 2. [Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate](https://arxiv.org/abs/2611.08756)

**<font color=#1a73e8>作者：</font>** Liting Huang, Huizhi Liang, Yi Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge attacks on Large Language Models, such as manipulating fact-checking judgments, pose significant risks to AI reliability. Existing approaches -- adversarial suffix/template injection and single-agent self-reflection -- lack robustness across diverse defenses and are prone to confirmation bias and costly trial-and-error, respectively. We propose Debate-to-Deceive (D2D), a multi-agent debate framework grounded in human debate structure and rhetorical style, enabling agents to generate adversarial passages that are semantically coherent, rhetorically effective, and resistant to early confirmation bias. D2D formalizes the adversarial process as an evolutionary game in which agents adaptively evolve their rhetorical strategies (Logos, Pathos, Ethos) through competition. To manage the intractably large LLM output space, we decouple agent behavior into a strategic layer, which selects a rhetorical action from a compact strategy space via evolutionary-inspired learning dynamics, and a generation layer, where the LLM produces a concrete passage conditioned on that strategy and the debate context. On four fact-checking benchmarks (FEVER, HealthVer, CLIMATE-FEVER, and SciFact), D2D substantially outperforms existing attacks and evades most defenses.

---


### 3. [Guardrail Erosion in Domain Fine-Tuned Large Language Models: A Paired Audit of Knowledge-Centric Abstention in Biomedical LLMs](https://arxiv.org/abs/2611.08780)

**<font color=#1a73e8>作者：</font>** Stephen Peng, Vineet Jagadeesan Nair, Noah Broestl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The number of domain fine-tuned models, particularly in the biomedical domain, is rapidly expanding. Fine-tuning promises high-performing models at a fraction of the cost of training a base model, but it can also produce unintended behavioral changes. Multiple studies have shown that safety guardrails can erode with fine-tuning, yet large-scale studies across model architectures, data mixtures, and fine-tuning methodologies remain limited. Where prior work in this space has studied value-centric refusal, this work focuses on knowledge-centric abstention. We audit 25 biomedical domain fine-tuned large language models against 11 paired base checkpoints on MedAbstain and ClinDet-Bench to evaluate the impact of fine-tuning on knowledge-centric abstention. We find that defined appropriate abstention measured by these benchmarks, already low in base models (median 8.3% on MedAbstain), falls further after fine-tuning (median 4.2%, decreasing in 21 of 25 pairs on MedAbstain), and that the magnitude and direction of change are heterogeneous across pairs. These results motivate fine-tuning methods that improve domain-specific capability while preserving appropriate caution.

---


### 4. [Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks](https://arxiv.org/abs/2611.08834)

**<font color=#1a73e8>作者：</font>** Mark Heimann, Katherine Taylor, Bruno Jacob  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specialized prompt injection guards are deployed in front of document analysis systems, but no false positive rate has been published for any of them on legal contracts. We measure eleven open-weights guards on two corpora of legal contracts and find that existing guards struggle: document-level false positive rates are as high as 92.39%; two guards fall below chance on paired AUC; and a five-regex baseline is not Pareto-dominated by any guard in the panel. Controlled probes locate model-specific as well as general failure modes. Prompted LLMs resolve the tested failures, including a second threat category (unauthorized scope claims) on which every guard scores zero. A cascaded LLM solution, where the positives of a mid-tier model are verified by a frontier model, is 6.5x cheaper than using exclusively a frontier model and approaches its performance.

---


### 5. [Jev as an LLM Safety Guardrail: An Empirical Study of Input Filtering, Selective Output Review, and Over-Refusal](https://arxiv.org/abs/2611.08845)

**<font color=#1a73e8>作者：</font>** Olivia Cognetti, Bhaskar Krishnamachari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> External safety filters can prevent unsafe requests from reaching a large language model (LLM), but may also reject legitimate queries. We present an end-to-end empirical evaluation of Jev, a probabilistic decision model, as a safety guardrail for a Qwen2.5-1.5B-based pipeline. Three configurations are compared on 970 benchmark prompts: an unfiltered LLM, Jev input filtering, and tiered Jev input filtering with selective output review. Across 720 prompts labeled harmful (520 AdvBench and 200 XSTest-unsafe), the fraction recorded as answered decreases from 527/720 (73.2%) without filtering to 17/720 (2.4%) with input filtering. On 250 XSTest-safe prompts, however, non-answer/refusal increases from 3/250 (1.2%) to 27/250 (10.8%). Tiered filtering yields 40/720 (5.6%) harmful-prompt answers and 10/250 (4.0%) benign-prompt refusals, with 79/970 (8.1%) of prompts requiring output review. Joint optimization of the tiered thresholds improves macro-F1 from 0.9351 to 0.9512, while reducing harmful-prompt answers and output-review frequency at the same benign-refusal rate. Matched-budget comparisons reveal modest additional gains over a retuned single gate on the evaluation data, although these gains are not consistently observed on a held-out split.

---


### 6. [MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory](https://arxiv.org/abs/2611.09721)

**<font color=#1a73e8>作者：</font>** David H. Yang, Blake Bullwinkel, Amanda Minnich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning across different memory architectures, we introduce MemoryDojo, a benchmark for tracing the lifecycle of poisoned information through agent memory and measuring its influence on subsequent agent behavior. MemoryDojo is easily extensible, consists of 155 multi-session long-horizon trajectories covering four domains, and supports five different memory systems. Through our evaluation, we find that all memory systems are susceptible to memory poisoning, with substantial variation in downstream effects. We further propose a memory-aware poison optimization process that increases the poisoning efficacy, highlighting differences between memory architectures. We hope that MemoryDojo will support research on understanding and mitigating agentic memory risks.

---


### 7. [GuardrailAgent: An Agentic Framework for Jailbreak Defense](https://arxiv.org/abs/2611.09734)

**<font color=#1a73e8>作者：</font>** Tianze Chang, Junjie Chu, Yixin Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite undergoing safety training to align with human values, large language models (LLMs) remain vulnerable to jailbreak attacks that circumvent built-in safeguards and elicit malicious behaviors given by the adversary. Existing defenses are mostly static and fail to adapt to new or unknown attack strategies, providing limited resilience. To address these, we propose a multi-agent defense framework, GuardrailAgent, that offers adaptive, end-to-end protection. The system autonomously gathers and summarizes attack characteristics into a continuously updated knowledge base that supports both input- and output-side detection. A feedback module integrates misclassified cases for iterative improvement at minimal cost. Tested on over ten representative jailbreaks, the framework achieved a 93.1% input-side detection rate, 93.9% overall detection, and a 95.8% F1 score, while rapidly adapting to unseen attacks. These results demonstrate GuardrailAgent's outstanding capability to maintain LLM safety in the face of evolving jailbreak tactics.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
